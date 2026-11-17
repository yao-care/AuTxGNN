"""AU（PBS Schedule 公用 API）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

注意：AU 站的本地資料原本就是 PBS（藥品給付）清單，不是 TGA ARTG 許可證；ARTG 沒有可程式下載的全量檔、
衛生部 API 入口要澳洲 Digital ID（用戶無法申請）。用戶 2026-10-30 選「沿用現有來源排程」。
來源：PBS public API（https://data-api.health.gov.au/pbs/api/v3/items，CSV），衛生部說明對所有人免費開放、不需登入
（https://data.pbs.gov.au/api/api-public.html）。請求要帶 subscription-key：由 GitHub Actions secret PBS_PUBLIC_KEY 提供
（取自官方 Postman 公開 collection 的共用金鑰；不寫進 repo）。限流：所有使用者共用每 20 秒 1 次，這裡只發 1 次請求。
欄位 pbs_code（＝證據包 license_id，例 1195X）。只列當期 PBS 品項、沒有狀態欄：在列不改紀錄，
新清單查不到的代碼保留原狀態、列在 summary（不推定為撤銷）。

2026-11-17（用戶要求確認 11-16 排程「新資料查不到」的 16 張）：pbs_code 是 PBS 品項代碼（藥＋劑型＋給付計畫），不是 TGA ARTG 號碼；
PBS Schedule 只列當期給付的品項，代碼消失＝「no longer listed on the PBS Schedule」，不等於 ARTG 註冊失效（ARTG 狀態不在這份資料裡）。
API 保留 12 個月的 schedule：16 張在 2025-12～2026-08 的 schedule 都還在、2026-11-01（當期 4753）沒有，6 張有 non_effective_date。做法：
- fetch() 把當期 schedule 的代碼記成 CURRENT（少於 MIN_CURRENT 不判定）。
- preprocess：證據包裡不在 CURRENT 的代碼標 license_status＝cancelled（本站事實層「cancelled」＝不在當期 PBS Schedule）、
  pbs_not_listed＝第一次發現日，status 改「No longer listed on the PBS Schedule」（原值存 status_before_pbs_not_listed）；
  又出現在清單就還原。頁面照 PBS 的口徑寫，不寫 TGA 註冊失效。
- confirmed_absent(lid)：CURRENT 有資料且代碼不在裡面。
"""
import re
import csv
import io
import os
import time

import requests

RAW_FILE = "raw/pbs_item_codes.json"
CURRENT: set = set()   # fetch() 填：當期 PBS Schedule 的 pbs_code；空的就不做「不在清單」判定
MIN_CURRENT = 5000     # 2026-11-01 版 15,365 列、7,156 個不重複代碼
NOT_LISTED = "No longer listed on the PBS Schedule"
CODE_RE = re.compile(r"^\d{2,5}[A-Z]$")


def _get(params, key, path="items", csv_=True):
    for attempt in range(4):
        try:
            r = requests.get(f"https://data-api.health.gov.au/pbs/api/v3/{path}", params=params, timeout=300,
                             headers={"subscription-key": key, "Accept": "text/csv" if csv_ else "application/json"})
            r.raise_for_status()
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(30 * (attempt + 1))  # 共用限流 20 秒一次


def fetch():
    key = os.environ.get("PBS_PUBLIC_KEY")
    if not key:
        raise RuntimeError("沒有設定 PBS_PUBLIC_KEY（GitHub Actions secret）")
    # 只看當期 schedule（API 保留 12 個月，全抓會把近一年已下架的也算在列）
    sch = _get({"limit": 100}, key, "schedules", csv_=False).json().get("data") or []
    today = time.strftime("%Y-%m-%d")
    cur = max((s for s in sch if str(s.get("effective_date", "")) <= today), key=lambda s: str(s.get("effective_date", "")), default=None)
    if not cur:
        raise RuntimeError("schedules 端點沒有生效中的 schedule")
    out, page = [], 1
    while True:
        time.sleep(21)
        rows = list(csv.DictReader(io.StringIO(_get({"schedule_code": cur["schedule_code"], "limit": 100000, "page": page}, key).content.decode("utf-8-sig"))))
        if rows and "pbs_code" not in rows[0]:
            raise RuntimeError(f"欄位改變：{list(rows[0])[:8]}")
        out += [{"pbs_code": (x["pbs_code"] or "").strip(), "schedule": cur["schedule_code"]} for x in rows if x.get("pbs_code")]
        if len(rows) < 100000:
            break
        page += 1
    CURRENT.clear()
    if len({r["pbs_code"] for r in out}) >= MIN_CURRENT:
        CURRENT.update(r["pbs_code"] for r in out)
    return out


def confirmed_absent(lid):
    """給 license_refresh：當期 PBS Schedule 確認已不列這個品項代碼（不代表 TGA ARTG 註冊失效）"""
    lid = str(lid).strip()
    return bool(CURRENT) and bool(CODE_RE.match(lid)) and lid not in CURRENT


def preprocess(bundle):
    """不在當期 PBS Schedule 的代碼標 cancelled＋pbs_not_listed；又出現在清單就還原。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not CODE_RE.match(lid):
            continue
        if lid in CURRENT:
            if r.get("pbs_not_listed"):
                r.pop("pbs_not_listed", None)
                r.pop("license_status", None)
                r["status"] = r.pop("status_before_pbs_not_listed", "")
                ch = True
        elif not r.get("pbs_not_listed"):
            r["status_before_pbs_not_listed"] = r.get("status") or ""
            r["status"] = NOT_LISTED
            r["license_status"] = "cancelled"
            r["pbs_not_listed"] = today
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 3000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["pbs_code"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary
