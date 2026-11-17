"""AU 證據包補收當期 PBS Schedule 上、依本站原本的比對規則屬於本藥、卻不在證據包的 PBS 品項（2026-11-17，用戶決定「依成分補收」；全程不用 AI）。

證據包的許可證紀錄（tfda 區塊）是 collectors/aufda.py 依 data/raw/tables_as_csv/items.csv（PBS 舊版下載檔）＋ data/processed/drug_mapping.csv 收的：
藥名 → DrugBank ID → drug_mapping 裡對到同一個 DrugBank ID 的 PBS 品項代碼（單方、複方都收；複方由 drug_mapping 逐成分對到各成分的 DrugBank ID），
最多存 20 筆（單方排前）、total_matches 記總數。但 data/loader.py 的 load_pbs_data() 依 drug_name 去重、每個藥名只留第一個 pbs_code，
所以 drug_mapping 每個 PBS 藥名只有 1 個品項代碼，多數藥的證據包只收到 1 個品項；那個品項不在當期 Schedule 時，頁面就寫「Not on the current PBS Schedule」，
即使當期還有同成分的其他品項（例：apixaban 10414D 已不列，當期仍有 Eliquis 等品項）。

這支照同一套規則補收（不放寬）：
- 當期 PBS Schedule（PBS public data API items，schedule_code＝當期）每個品項的 drug_name → DrugBank ID：
  drug_name 在 drug_mapping.csv「原始主成分」裡有的，照 drug_mapping 的結果（含當初的複方逐成分對照；映射失敗的照舊不收）；
  drug_mapping 沒有的新藥名，用本站同一支 mapping（autxgnn.mapping.drugbank_mapper.map_fda_drugs_to_drugbank）。
- 跟證據包的 drugbank_ids 有交集、而代碼不在證據包的品項，補一筆（欄位照 aufda.LocalFDACollector._format：license_id＝pbs_code、
  brand_name＝brand_name、ingredients＝drug_name、dosage_form＝li_form，status 空白＝在列），加 source（schedule 代碼與生效日）與 added（補收日）。
  同一個 pbs_code 有多列（不同品牌／給付計畫）時取第一列，同 load_pbs_data()。
- total_matches 加上補收的品項數（原本的 total_matches 不含這些代碼）；records 照原收集器最多存 20 筆（單方優先），
  超過的不存、只算進 total_matches（證據包算部分收錄，頁面寫「at least N」）。
可重複執行（已在證據包的代碼不重補）、只加不刪。
用法（repo 根目錄）：python3 scripts/add_current_pbs_items.py [--csv <當期 items CSV>] [--dry-run] [--report out.tsv]
  不給 --csv 就用 PBS public data API 下載當期 schedule（要環境變數 PBS_PUBLIC_KEY；共用限流每 20 秒 1 次）。
"""
import argparse
import csv
import io
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

MAX_RECORDS = 20       # 同 aufda.LocalFDACollector._format
MIN_ROWS = 5000        # 當期 schedule 少於這個列數就不補（疑似下載或格式有問題）


def _n_ing(s):
    return len(re.split(r"[,;+/&]|&&| and | with ", str(s or "")))


def fetch_current():
    import os
    import license_adapter as la
    key = os.environ.get("PBS_PUBLIC_KEY")
    if not key:
        sys.exit("沒有設定 PBS_PUBLIC_KEY")
    sch = la._get({"limit": 100}, key, "schedules", csv_=False).json().get("data") or []
    today = time.strftime("%Y-%m-%d")
    cur = max((s for s in sch if str(s.get("effective_date", "")) <= today), key=lambda s: str(s.get("effective_date", "")), default=None)
    if not cur:
        sys.exit("schedules 端點沒有生效中的 schedule")
    rows, page = [], 1
    while True:
        time.sleep(21)
        got = list(csv.DictReader(io.StringIO(la._get({"schedule_code": cur["schedule_code"], "limit": 100000, "page": page}, key).content.decode("utf-8-sig"))))
        rows += got
        if len(got) < 100000:
            break
        page += 1
    return rows, str(cur["schedule_code"]), str(cur.get("effective_date") or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--effective-date", default="", help="給 --csv 時標在 source 的 schedule 生效日")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report")
    a = ap.parse_args()
    if a.csv:
        rows = list(csv.DictReader(open(a.csv, encoding="utf-8-sig", newline="")))
        sc = {r.get("schedule_code") for r in rows} - {"", None}
        if len(sc) != 1:
            sys.exit(f"CSV 的 schedule_code 不是單一值：{sorted(sc)[:5]}")
        sched, eff = sc.pop(), a.effective_date
    else:
        rows, sched, eff = fetch_current()
    if len(rows) < MIN_ROWS or (rows and "pbs_code" not in rows[0]):
        sys.exit(f"當期 schedule 只有 {len(rows)} 列或欄位不符，疑似下載或格式有問題")

    items = {}
    for r in rows:
        c = (r.get("pbs_code") or "").strip()
        if c and c not in items:
            items[c] = r

    # drug_name → DrugBank ID（同 Phase 1 對照）
    mp, seen = {}, set()
    with open(ROOT / "data/processed/drug_mapping.csv", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            seen.add(r["原始主成分"])
            if str(r.get("映射成功")).strip().lower() in ("true", "1", "yes") and r.get("drugbank_id"):
                mp.setdefault(r["原始主成分"], set()).add(r["drugbank_id"].strip().upper())
    new_names = sorted({r["drug_name"] for r in items.values()} - seen)
    if new_names:
        import pandas as pd
        from autxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
        df = pd.DataFrame([{"許可證字號": n, "中文品名": n, "主成分略述": n} for n in new_names])
        for _, r in map_fda_drugs_to_drugbank(df).iterrows():
            if r["映射成功"]:
                mp.setdefault(r["許可證字號"], set()).add(str(r["drugbank_id"]).upper())
    code_db = {c: mp.get(r["drug_name"], set()) for c, r in items.items()}

    src = f"PBS Schedule {sched}" + (f"（effective {eff}）" if eff else "") + "，PBS public data API items"
    today = time.strftime("%Y-%m-%d")
    out, n_b, n_cap = [], 0, 0
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        dbs = {str(x).upper() for x in (t.get("drugbank_ids") or [])}
        if not dbs:
            continue
        have = {str(r.get("license_id") or "").strip() for r in recs}
        have |= set(t.get("pbs_items_not_stored") or [])
        add = sorted((c for c, d in code_db.items() if c not in have and d & dbs),
                     key=lambda c: (_n_ing(items[c]["drug_name"]), c))
        if not add:
            continue
        tm = max(int(t.get("total_matches") or 0), len(recs))
        room = max(0, MAX_RECORDS - len(recs))
        for i, c in enumerate(add):
            r = items[c]
            out.append(f"{f.parent.name}\t{c}\t{r.get('brand_name','')}\t{r['drug_name']}\t{r.get('li_form','')}\t{'stored' if i < room else 'counted_only'}")
            if i >= room:
                continue
            recs.append({
                "license_id": c,
                "brand_name_zh": (r.get("brand_name") or "").strip(),
                "brand_name_en": (r.get("brand_name") or "").strip(),
                "ingredients": (r.get("drug_name") or "").strip(),
                "indication": "",
                "dosage_form": (r.get("li_form") or "").strip(),
                "manufacturer": "",
                "license_holder": "",
                "approval_date": "",
                "expiry_date": "",
                "status": "",
                "source": src,
                "added": today,
            })
        extra = add[room:]
        if extra:
            n_cap += len(extra)
            t["pbs_items_not_stored"] = sorted(set(t.get("pbs_items_not_stored") or []) | set(extra))
        t["total_matches"] = tm + len(add)
        t["records"], t["found"] = recs, True
        b["tfda"] = t
        n_b += 1
        if not a.dry_run:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"補收 {len(out)} 筆、{n_b} 個證據包（其中 {n_cap} 筆超過 {MAX_RECORDS} 筆上限只算進 total_matches；{src}）"
          f"{'（試跑，未寫回）' if a.dry_run else ''}")
    if a.report:
        Path(a.report).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
