# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）。
本站照 UsTxGNN 的試做版建立，規則與程式都在本 repo，頁面文字用英文、依據是澳洲衛生部 PBS 給付清單（PBS Schedule）與 TGA 的 ARTG。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁「## Review Log」表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/autxgnn/regulatory/page_format.py` | 頁首＝Quick Overview「Evidence Level」格的**第一個**等級（主預測）。2026-11-12 實測本站現有頁面全部是這個規則（第一個等級跟格內最高等級不同的頁也照第一個），照實寫成程式；Tw 是整格取最高，本站不同 |
| 撤回預測 | `src/autxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/au_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/autxgnn/regulatory/licenses.py` | 快照存事實層與本藥號碼；gate 依快照驗市場段落的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的許可證紀錄目前沒有適應症文字時，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 許可證修正時直接刪掉的矛盾子句（10-31 7203dc4f4（只剩註銷許可句）、11-06 37a0310a1（單方／複方說法）），2026-11-12 由 scripts/reviews_from_edits.py 依 git 前後版本轉入。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。

## 新資料查不到的許可證（2026-11-17）

11-16 每週排程「新資料查不到」16 張（證據包 833 個代碼的 1.9%，沒開 issue）。本站的號碼是 PBS 品項代碼（pbs_code：藥＋劑型＋給付計畫，不是 TGA ARTG 號碼），
PBS Schedule 只列當期給付的品項——代碼消失＝「no longer listed on the PBS Schedule」，不等於 ARTG 註冊失效（ARTG 狀態不在這份資料裡，也沒有可下載的全量檔）。
2026-11-17 用戶要求確認實際狀態：用 PBS public data API（items、schedules）逐號查 API 保留的 13 期 schedule（2025-12-01～2026-11-01）：16 張全部在 2025-12-01 起的 schedule 裡、
當期（schedule 4753，2026-11-01 生效，15,365 列、7,156 個代碼）沒有；最後在列 2026-03-01～2026-08-01，其中 6 張 API 記有 non_effective_date。API 的 items 涵蓋所有給付計畫（GE、R1、IN、CA、HS…），沒有「其實還在別份清單上」的號。
- `scripts/license_adapter.py`：fetch() 把當期 schedule 的代碼記成 CURRENT（少於 5,000 個不判定）；preprocess 對不在 CURRENT 的代碼標
  `license_status: cancelled`（本站事實層 cancelled＝不在當期 PBS Schedule）＋`pbs_not_listed`（第一次發現日），status 改「No longer listed on the PBS Schedule」（原值存 `status_before_pbs_not_listed`），又出現在清單就還原。
  `confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」。本機試跑時金鑰用 PBS 官方 Postman 公開 collection 的共用 subscription-key（環境變數 PBS_PUBLIC_KEY，不寫進 repo）。
- 頁面照 PBS 的口徑寫，不寫 TGA 註冊失效：母目錄 check_drug_page.py 加 AU 的 SCOPE_CANCELLED（全部不在當期清單的頁狀態列＝「Not on the current PBS Schedule (N of N PBS items in this data no longer listed) – TGA (ARTG) registration status is not included in this data」，14 頁）；本站 tools/txgnn 同步同一份。
- 證據包多數藥只收 1 個 PBS 品項（753 個藥），全部不在列的 14 頁裡有 9 個藥（apixaban、brimonidine、desmopressin、edaravone、etanercept、fludarabine、naproxen、pembrolizumab、phenelzine）當期仍有同成分的其他 PBS 品項，
  fluvastatin、patisiran、quinagolide、toremifene 當期沒有任何品項，atazanavir 只剩 cobicistat 複方。狀態列只陳述「本資料的品項」不在列；依成分補收品項同日另做（見下節）。
- 16 頁狀態列／張數列、3 格許可證表狀態格照事實層同步；正文跟新事實矛盾的 2 頁以紀錄更正：desmopressin（「marketed in Australia as a nasal spray」→本資料的鼻噴劑品項 12458Q 已不在 PBS、其他鼻噴劑與錠劑仍在列，`au-lic-20261117-desmopressin-1`）、
  vitamin_a（「Both entries are valid products」→2 個品項中 14426G 已不在列，`au-lic-20261106-vitamin_a-1` 同 id 重發、前版存 history）。

## 依成分補收當期 PBS 品項（2026-11-17）

用戶 2026-11-17 決定「依成分補收」：證據包的 PBS 品項是 collectors/aufda.py 依 drug_mapping.csv（藥名→DrugBank ID→品項代碼）收的，但 data/loader.py 的 load_pbs_data() 依 drug_name 去重、每個 PBS 藥名只留第一個 pbs_code，
所以多數藥只收到 1 個品項；那個品項不在當期 Schedule 時頁面寫「Not on the current PBS Schedule」，即使當期還有同成分的其他品項。
- `scripts/add_current_pbs_items.py`：當期 PBS Schedule（PBS public data API items，金鑰同 license_adapter 的 PBS_PUBLIC_KEY；也可 `--csv` 給下載好的當期 items）每個品項的 drug_name 照 drug_mapping.csv 的「原始主成分」對 DrugBank ID
  （含當初的複方逐成分對照；映射失敗的不收；drug_mapping 沒有的新藥名用本站同一支 map_fda_drugs_to_drugbank），跟證據包 drugbank_ids 有交集、代碼不在證據包的就補一筆（欄位照 aufda._format，
  加 source＝schedule 代碼與生效日、added＝補收日）；records 照原收集器最多存 20 筆（單方優先），超過的只記在 `pbs_items_not_stored` 並算進 total_matches（頁面寫「at least N」）。只加不刪、可重複執行。
- 2026-11-17 第一次跑（Schedule 4753，2026-11-01 生效）：670 個證據包補 5,969 個品項（存進 records 4,317 筆、1,652 筆超過上限只算張數）；668 頁概覽狀態列／張數列由程式同步（例：sirolimus 1→16、hydrocortisone 1→12）。
  原本 14 頁全部不在列的藥：apixaban（7 of 8）、brimonidine（9 of 10）、desmopressin（16 of 17）、edaravone（2 of 3）、etanercept（at least 19）、fludarabine（3 of 4）、naproxen（14 of 15）、pembrolizumab（12 of 13）、phenelzine（1 of 2）改成在列；
  atazanavir 補到 Evotaz（atazanavir＋cobicistat）、變成 1 of 2 在列（drug_mapping 本來就把複方逐成分對到 atazanavir）；fluvastatin、patisiran、quinagolide、toremifene 當期沒有任何品項，維持 Not on the current PBS Schedule。
- 正文依舊證據包（1～2 個品項）寫的張數與「唯一劑型」說法跟新事實矛盾的 81 句以 80 筆新的 `au-lic-20261117-*` 紀錄與 1 筆同 id 重發更正（checker M3 的 19 頁＋另掃市場段落 62 頁：「one valid licence」「The only registered product is …」等；
  只描述表上那一筆的「This is a single-ingredient product…」、只講給藥途徑且仍成立的句子、待辦條目不改）；`au-lic-20261117-desmopressin-1`、`au-lic-20261106-ethinylestradiol-1` 同 id 重發，前版存 history。
- 照原規則一併收進來、沒有另外處理的：isoleucine、tyrosine、threonine 等證據包含「amino acid formula without …」配方（drug_mapping 的對照如此）。
- `.github/workflows/license-refresh.yml` 在 license_refresh 前先跑這支（金鑰用既有的 secrets.PBS_PUBLIC_KEY），有補收就照常發新 Release。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 578 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Detailed mechanism of action data is not available in the data compiled for this report.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `au-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：「According to the … section of the US FDA-approved prescribing information for <藥>: "…" ([DailyMed: …](…), label version …; accessed …)」。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 2026-11-19 結果：518 頁寫入紀錄（美國仿單 482、ChEMBL 36），60 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 8 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）22 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Approved use: Not recorded in the local data」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：PBS 品項（不寫 ARTG）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「Approved use: Not recorded in the local data」→「In Australia: 10 PBS items (10 currently listed)」；2026-11-19 改了 393 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site AuTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 市場段落 PBS 品項表與正文張數由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站「許可證張數與狀態不再每週過期」，本站做表＋B）：每週排程只改得到概覽表狀態列／張數列，「## Australia Market Information」段落裡 AI 寫的自由格式表
（609 頁表頭「| ARTG Number | Product Name | Dosage Form | Approved Indication |」、156 頁「| Licence | Product | Dosage form | Status |」、19 頁其他三欄／四欄寫法）不會跟著 PBS Schedule 變，
而且第一欄其實是 PBS 品項代碼（不是 ARTG 號碼）、適應症欄全是「Not recorded…」，多數表只列 11-17 依成分補收前的 1～2 個品項。
- A. `scripts/sync_license_tables.py`：市場段落第一張許可證表換成程式依證據包（tfda.records）產生的表 `| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |`
  （產品名、成分、劑型照 PBS public data API 原文；證據包的 pandas 空值「nan」寫成「–」）；狀態＝在當期 Schedule「Valid」（本站既有寫法）、不在當期 Schedule 用證據包原文「No longer listed on the PBS Schedule」；
  在列的在前、同狀態依代碼，最多 20 列；列數少於總數時表下一句「The table shows N of M PBS items for this ingredient in these data (items on the current PBS Schedule first).」
  （M＝total_matches，含 add_current_pbs_items.py 因 20 筆上限沒存的品項）；最後一行來源句（PBS listing 不含 TGA ARTG 狀態）；沒有品項時一句 NONE_LINE。前後 `<!-- licenses:begin/end -->`；段落沒有表的 4 頁補在段落開頭。
  快照 `snapshots/au_licenses.json.gz` 存 rows／show（program_rows）；gate 第 18 項（licenses.page_problems → sync_license_tables.block_problems）擋「程式區塊≠快照重算」「市場段落沒有程式區塊」「程式區塊外還有 AI 許可證表」。
  接上：`scripts/apply_drug_reviews.py`（非 --check）結尾、`scripts/build_license_snapshot.py` 結尾（`--no-rewrite` 不跑）、每週排程 `license_adapter.sync_tables`（--bundles，全站比對、只寫有變的）與 `PAGE_NOTE`（3b 放行程式區塊的非表格行）。
  add_current_pbs_items.py 的行為沒動。
- B. `scripts/rewrite_license_counts.py`＋`src/autxgnn/regulatory/count_prose.py`（照 Kr／My／DE 移植，英文句型）：「N current PBS items」「N valid PBS items」「N of M PBS items are listed」「(N listed, M no longer listed)」依快照事實層改寫
  （本站 valid＝在當期 PBS Schedule、cancelled＝不在）；有保留、講證據包或查詢、相對數、劑型／單方複方／廠商子集、TGA／ARTG 口徑、講表格筆數、partial 頁不動；同一行有判斷不了的整行不動；
  0／1 跨越與 both（單複數）、「all … listed」而事實不符（premise）不改、列待查。不寫查核框；gate 第 22 項擋「再跑一次會變」。2026-11-24 量測：句型對得到的 44 句，數字全部已等於事實層，改寫 0 句、待查 0 句。
- 2026-11-24 套用（資料 data-20261117-130853）：程式表 788 頁（公開 749＋noindex 39；AI 表取代 784 頁、補表 4 頁）；magnesium_sulfate 的「1 (valid: 1)」原本寫在舊 AI 表的品名格，概覽表缺張數列，補上「| Number of PBS Items | 1 (valid: 1) |」。
  查核紀錄更正文字講舊表筆數的 8 筆同 id 重發（前版存 history）：codeine、hydrocortisone、isoleucine、propylene_glycol、temozolomide、tyrosine（「The table lists one of 12…」「The five entries in the table…」等→只留總數）、
  emtricitabine（「the seven named above」）、terbutaline（「the Bricanyl injection in the table」）；新增 2 筆：`au-lic-20261124-emtricitabine-1`（「Two further entries are registered: Genvoya (ARTG 11114Y)…」→代碼是 PBS 品項代碼、不再是表外的「further」）、
  `au-lic-20261124-acetic_acid-1`（「so a product table cannot be provided」）。被取代的表上沒有錨著的查核紀錄（0 筆 superseded）。
  checker 全量前後 0／0；gate exit 0；last_modified_at：788 頁表格內容有變，改 2026-11-24。
  另寫的寬偵測（數字不等於事實層任一讀法、the only／sole、all … valid 而有註銷、講表格）全量掃公開頁：改前 100 句、改後 90 句，剩下都不是這次的張數句：
  「The only Australian product is an oral capsule」這類只講劑型／給藥途徑的句子（11-17 依成分補收後品項變多，劑型說法沒有逐張確認）、「one entry was found」等待辦條目、交互作用與文獻的「entries／items」誤中。
- 母目錄 `.claude/license_labels/AuTxGNN.json` 只有「Valid」：建議加 `"No longer listed on the PBS Schedule": "cancelled"`（preferred.cancelled）；目前排程把有效格翻成註銷時會用證據包原文（同一字樣），所以不影響同步。

## 劑型說法逐張對照（2026-11-24 第二輪）

用戶 2026-11-24 第二輪決定：正文依 11-17 依成分補收前的舊證據包（多數只收 1～2 個 PBS 品項）寫的劑型／規格說法（「The only Australian product is an oral capsule」「marketed in Australia as a 150 mg tablet」「Only an injectable form is registered」等），逐句對照證據包（data-20261117-130853，PBS Schedule 4753）全部品項的劑型。
- 偵測（全量、公開頁）：劑型字樣＋市場字樣的句子 386 句（另放寬：only／sole／single＋市場＋product/item/form 字樣、市場動詞＋規格數字、「marketed … as」），逐句對照證據包劑型類別（給藥途徑）與細分（錠／膠囊／口服液…、規格）。
- 判定規則：全稱說法（the only／only／sole／「the product is …」）要跟本藥全部單方品項的劑型與規格（有寫才算）一致；描述說法（marketed/registered in Australia as …）有不同給藥途徑的單方品項、或寫了單一規格而另有其他規格，才算不成立；「沒有 X 劑型」的說法查有無該途徑品項。證據包沒有單方品項時拿全部品項比；只有複方才有的劑型不算推翻描述說法。
- 結果：不成立 69 句（56 頁）以 69 筆 `au-lic-20261124b-*` 更正（劑型 51、規格 9、劑型與規格 3、以「只有一筆／兩筆」為前提的待辦 3、未區分單方與複方 3）；更正文字只列劑型類別與規格、不寫張數；待辦條目只改錯的前提。成立的保留（例：aflibercept 全為玻璃體內注射、benzydamine 全為口腔噴洗劑、gefitinib 全為 250 mg 錠）。待查清單 11-24 沒有新增項目（第一輪 B 待查 0 句）。
- `scripts/reviews_from_edits.py` 的 figures() 改成不寫張數（指向概覽表與程式 PBS 品項表）；寫死張數的 `au-lic-20261031-lurasidone-1` 說明同 id 重發（前版存 history）。
- 已知問題（2026-11-24 第三輪已處理，見下節）：`au-lic-20261031-lurasidone-1` 是 10-31 刪句工具把「1 clinical trial (withdrawn…) and 20 publications」誤當許可證註銷句刪掉的（一句話摘要只剩半句）。

## 第三輪：誤刪的試驗句還原、缺市場段落的防線（2026-11-24）

用戶 2026-11-24 第三輪決定（本站做 B、C）：
- C. `au-lic-20261031-lurasidone-1` 撤回（status withdrawn，withdrawn_on／withdrawn_note／withdrawn_reason）：10-31 刪句工具（checker ONLY_CANCEL）把一句話摘要裡講臨床試驗的「but only **1 clinical trial** (withdrawn, with no participants enrolled) and **20 publications** …」當成許可證註銷句刪掉；
  母目錄 checker 963a4ab8 已把「only … trial (withdrawn)」等試驗／文獻語境排除。撤回的紀錄不會自動還原原句，頁面原句依 7203dc4f4^ 手動還原（模型報告原文），查核紀錄表註明撤回；還原後 checker 全量仍 0。
  全站查同類：刪改轉紀錄（reviews_from_edits，10-31 7203dc4f4、11-06 37a0310a1）只有 3 筆，另 2 筆（ethinylestradiol、vitamin_a）刪的確是許可證單方／有效說法；其他 correct 紀錄刪改的文字也都是許可證／劑型句，沒有同類。
- B. `scripts/sync_license_tables.py` 的 add_section（照 JpTxGNN 第二輪）：公開頁沒有「## Australia Market Information」、證據包有 PBS 品項紀錄的，補段落＋程式表，位置在「## Cytotoxicity」（有這段的頁市場段落固定在它前面）→「## Safety Considerations」→「## Conclusion and Next Steps」→「## Disclaimer」之前；noindex 頁不補。
  gate（licenses.page_problems）加一條「公開頁沒有市場段落、證據包卻有紀錄」就擋；PAGE_NOTE（license_adapter 共用）放行新標題行。2026-11-24 量測：788 頁（公開 749＋noindex 39）都有市場段落，補 0 頁；這是給之後整頁重產的頁用的防線（以拿掉段落的頁試過：gate 擋、補回後與原頁相同、noindex 不補、可重複執行）。


## 證據包收錯品項排除（2026-11-25 第五輪）

用戶 2026-11-25 決定（第五輪第 1 條）：collectors/aufda.py 與 scripts/add_current_pbs_items.py 依 drug_mapping.csv（PBS drug_name → DrugBank ID）收品項，drug_mapping 把別的成分對到本藥 ID：PBS drug_name「bicarbonate」（Sodibic 840 mg，PBS li_drug_name 是 Sodium bicarbonate）對到 DB11098 Potassium bicarbonate、「Ichthammol」（Egoderm Cream）對到 DB01005 Hydroxyurea。
- 排除表 `config/bundle_record_exclusions.json`（比照 CHTxGNN 第三輪；每條附 reason、basis）：證據包名在 bundles 裡、紀錄成分欄（PBS drug_name，「 + 」分隔）沒有一段符合 require 就排除；`src/autxgnn/regulatory/record_exclusions.py` 判定，`scripts/exclude_mismatched_records.py` 移到 `tfda.excluded_records`（附 excluded、excluded_reason、excluded_basis；total_matches 扣掉；可重複執行）；aufda.py 收集時、add_current_pbs_items.py 補收時照同一份規則不收、excluded_records 的代碼不補回；`.github/workflows/license-refresh.yml` 在補收之後、license_refresh 之前跑。
- 量測：報告確認組 potassium_bicarbonate 2 筆（13933H、9470K Sodibic）；另寫的獨立偵測（全部證據包，紀錄成分欄沒有本藥名的）逐組看過，同類另有 hydroxyurea 1 筆（4281H Egoderm Cream＝ichthammol，頁面正文寫「唯一澳洲產品是 hydroxyurea 1% 外用乳膏」）；其餘是寫法（ciclosporin、glyceryl trinitrate、mitozantrone、chlormethine、phytomenadione、trientine、panthenol、risedronate 等），照收。
- 對照修正（data/processed/drug_mapping.csv，Release）：3093T Hydroxycarbamide 原本對照失敗，補 INN 別名對到 DB01005；13933H Sodibic 改對 DB01390 Sodium bicarbonate。add_current_pbs_items.py（Schedule 4753 items）因此補收 3 筆：hydroxyurea＋3093T（Capsule 500 mg）、sodium_bicarbonate＋13933H、9470K；第二次跑 0 筆。
- 套用（證據包 Release data-20261117-130853）：2 個證據包移出 3 筆；證據包 local_regulatory 重算；potassium_bicarbonate（4→2 張）、hydroxyurea（1→1 張，換成 hydroxycarbamide 膠囊）、sodium_bicarbonate（2→4 張）概覽列、程式表、description 由程式同步；正文矛盾 2 筆 `au-lic-20261125-hydroxyurea-*`（「唯一產品是外用乳膏、沒有口服劑型」與結論理由的同一前提）。checker 前後 0；gate exit 0。
