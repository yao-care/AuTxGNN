#!/usr/bin/env python3
"""市場段落的 PBS 品項表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 DETxGNN／UkTxGNN／SgTxGNN 同名檔）。

為什麼：「## Australia Market Information」段落裡的表原本是 AI 寫的自由格式表（609 頁表頭「| ARTG Number | Product Name |
Dosage Form | Approved Indication |」，156 頁「| Licence | Product | Dosage form | Status |」等）。第一欄其實是 PBS 品項代碼
（pbs_code，不是 TGA ARTG 號碼），適應症欄全是「Not recorded…」；而且多數表只列了 2026-11-17 依成分補收前的 1～2 個品項，
PBS Schedule 每月變，AI 表不會跟著改。改成程式依證據包（data/bundles 的 tfda.records）產生，每週排程
（license_adapter.sync_tables）自動同步。

表的內容（全程不用 AI；產品名、成分、劑型照 PBS public data API 原文）：
  | PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
  狀態欄：在當期 PBS Schedule＝「Valid」（本站既有寫法，母目錄 .claude/license_labels/AuTxGNN.json）；
  不在當期 Schedule（license_adapter.preprocess 標的 pbs_not_listed）＝證據包原文「No longer listed on the PBS Schedule」。
  排序：在列的在前，同狀態依代碼；最多 MAX_ROWS 列。表下：列數少於總數時一句 SHOW（總數＝證據包 total_matches，
  含 add_current_pbs_items.py 因 20 筆上限只算張數、沒存進 records 的品項）；最後一行來源句 SOURCE。
  證據包沒有任何品項時整個區塊只有 NONE_LINE 一行。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、gate 用來分辨程式寫的字）。
放在哪：取代市場段落裡的第一張許可證表（表頭含 ARTG／Licence）；段落沒有表時放在段落開頭。沒有市場段落的公開頁
  （2026-11-24 第三輪起）由 add_section 補段落；noindex 頁不補。
  表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照改寫）；--migrate 另拿掉緊接在舊表前後、
  只講「舊表列了幾筆」的說明句（CAPTION），查核紀錄的更正文字所在的句子不動。
資料來源：預設讀快照 snapshots/au_licenses.json.gz 的 rows／show（scripts/build_license_snapshot.py 用 program_rows 算好）；
  --bundles 改讀 data/bundles（每週排程在建新快照前用）。gate（scripts/check_seo_docs.py 的許可證項，
  src/autxgnn/regulatory/licenses.py）檢查程式區塊＝快照重算的結果、市場段落有程式表。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程
  license_adapter.sync_tables（--bundles）。sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.run，所以也會重新產生。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [--migrate] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "au_licenses.json.gz"
SEC = "## Australia Market Information"
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = "| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |"
SEP = "|------|------|------|------|------|"
VALID = "Valid"
NOT_LISTED = "No longer listed on the PBS Schedule"
SOURCE = ("Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and "
          "dosage forms as recorded there. \"Valid\" means the item is on the current PBS Schedule; TGA (ARTG) registration "
          "status is not included in these data.")
SHOW = "The table shows {n} of {m} PBS items for this ingredient in these data (items on the current PBS Schedule first)."
SHOW_RX = r"The table shows \d+ of \d+ PBS items for this ingredient in these data \(items on the current PBS Schedule first\)\."
NONE_LINE = ("No PBS items for this ingredient are recorded in these data; TGA (ARTG) registration status is not included "
             "in these data.")
MAX_ROWS = 20
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份；
# 2026-11-24 第三輪起另有 add_section 補的市場段落標題行）
PAGE_NOTE = r"^(" + "|".join(re.escape(x) for x in (SEC, BEGIN, END, SOURCE, NONE_LINE)) + "|" + SHOW_RX + r")$"
# --migrate：緊接舊表、只講表上列了幾筆的說明句（換成程式表後列數對不上）
CAPTION = re.compile(r"^(?:The (?:table|list) (?:above |below )?(?:shows|lists|includes|contains) [^.]*\.|"
                     r"(?:Selected|Representative|Example) (?:PBS items|entries|products)[^.]*:)$", re.I)


def _cell(x, n=80):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    if t.lower() in ("nan", "none", "null"):  # 證據包轉換時 pandas 的空值
        t = ""
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def _key(code):
    m = re.match(r"(\d+)(\D*)$", code)
    return (int(m.group(1)), m.group(2)) if m else (10 ** 9, code)


def rows_of(tf, fc=None):
    """證據包 tfda → (表格列, 總數)。總數＝total_matches 與不重複代碼數取大者。"""
    seen, listed, other = set(), [], []
    for r in tf.get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        gone = r.get("license_status") == "cancelled" or r.get("pbs_not_listed")
        st = (str(r.get("status") or "").strip() or NOT_LISTED) if gone else VALID
        row = f"| {k} | {_cell(r.get('brand_name_en') or r.get('brand_name_zh'), 80)} | {_cell(r.get('ingredients'), 90)} | " \
              f"{_cell(r.get('dosage_form'), 120)} | {st} |"
        (other if gone else listed).append((_key(k), row))
    rows = [x[1] for x in sorted(listed)] + [x[1] for x in sorted(other)]
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_rows(tf, fc=None):
    """給 build_license_snapshot：(表格列（最多 MAX_ROWS）, 表下的程式文字行)"""
    rows, total = rows_of(tf, fc)
    show = []
    if rows:
        if total > min(len(rows), MAX_ROWS):
            show.append(SHOW.format(n=min(len(rows), MAX_ROWS), m=total))
        show.append(SOURCE)
    else:
        show.append(NONE_LINE)
    return rows[:MAX_ROWS], show


def program_block(rows, show):
    if not rows:
        return list(show)
    out = [HEAD, SEP] + rows[:MAX_ROWS] + [""]
    for s in show:
        out += [s, ""]
    return out[:-1]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _is_license_table_head(lines, k):
    return lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|")) \
        and re.search(r"ARTG|Licen[cs]e|PBS", lines[k]) and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])


def section(lines):
    if SEC not in lines:
        return None
    a = lines.index(SEC)
    b = next((k for k in range(a + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
    return a, b


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def _drop_caption(lines, x, y, protect):
    """舊表 lines[x:y] 前後緊接、整行只講表上列了幾筆的說明句：拿掉（查核紀錄文字所在的行不動）。回傳 (lines, x, y)"""
    def ok(k):
        s = lines[k].strip()
        return s and CAPTION.match(s) and not any(p and p in s for p in protect)
    k = x - 1
    while k >= 0 and not lines[k].strip():
        k -= 1
    if k >= 0 and ok(k):
        lines = lines[:k] + lines[k + 1:]
        x, y = x - 1, y - 1
    k = y
    while k < len(lines) and not lines[k].strip():
        k += 1
    if k < len(lines) and ok(k):
        lines = lines[:k] + lines[k + 1:]
    return lines, x, y


def process(text, rows, show, migrate=False, protect=()):
    """回傳新內容（沒有市場段落時原樣）。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, show))
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk))
    sec = section(lines)
    if sec is None:
        return add_section(text, rows, show)
    a, b = sec
    tb = [k for k in range(a + 1, b) if _is_license_table_head(lines, k)]
    if tb:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        y += 1
        if migrate:
            lines, x, y = _drop_caption(lines, x, y, protect)
        return "\n".join(_splice(lines, x, y, blk))
    return "\n".join(_splice(lines, a + 1, a + 1, blk))


# 2026-11-24 第三輪（用戶決定；照 JpTxGNN 第二輪 add_section）：公開頁沒有「## Australia Market Information」段落、
# 但證據包有 PBS 品項紀錄的，補一個段落放程式表。位置：「## Cytotoxicity」之前（本站有這段的頁，市場段落固定在它前面）；
# 沒有就「## Safety Considerations」之前（預測頁的固定順序）；再沒有就「## Conclusion and Next Steps」、「## Disclaimer」之前。
# noindex 頁與證據包沒有紀錄的頁不補。2026-11-24 量測：公開頁 0 頁缺市場段落（788 頁都有），這是給之後整頁重產的頁用的防線。
ADD_BEFORE = ("## Cytotoxicity", "## Safety Considerations", "## Conclusion and Next Steps", "## Disclaimer")


def is_noindex(text):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    return bool(re.search(r"^noindex:\s*true", fm, re.M))


def add_section(text, rows, show):
    if not rows or is_noindex(text):
        return text
    lines = text.split("\n")
    at = next((lines.index(h) for h in ADD_BEFORE if h in lines), None)
    if at is None:
        return text
    return "\n".join(_splice(lines, at, at, [SEC, ""] + wrap(program_block(rows, show))))


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def _protect():
    p = ROOT / "docs/_data/drug_reviews.json"
    out = {}
    if p.exists():
        for r in json.loads(p.read_text(encoding="utf-8")).get("records", []):
            out.setdefault(r["file"], []).extend(x for x in (r.get("replacement"), r.get("anchor"), r.get("claim")) if x)
    return out


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def run(from_bundles=False, check=False, only=None, migrate=False):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    prot = _protect() if migrate else {}
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = _bundle(p.stem)
            if b is None:
                continue
            rows, show = program_rows(b.get("tfda") or {})
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, show = e["rows"], e["show"]
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, show, migrate, prot.get(p.name, ()))
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def block_problems(sec_lines, entry):
    """gate 用：段落裡的程式區塊＝快照重算的結果（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in sec_lines, END in sec_lines
    if has_b != has_e:
        return ["程式許可證區塊標記不成對"]
    if "rows" not in entry:
        return []
    if not has_b:
        return ["市場段落沒有程式 PBS 品項表（跑 python3 scripts/sync_license_tables.py）"]
    i, j = sec_lines.index(BEGIN), sec_lines.index(END)
    out = [k for k in range(len(sec_lines)) if not i < k < j and _is_license_table_head(sec_lines, k)]
    if out:
        return [f"市場段落程式區塊外還有 AI 許可證表（{sec_lines[out[0]][:60]}）"]
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["show"]) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）"]
    return []


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only, migrate="--migrate" in a)
    print(f"程式 PBS 品項表：{'待改' if '--check' in a else '改'} {len(ch)} 頁")
    if "--check" in a:
        sys.exit(1 if ch else 0)
