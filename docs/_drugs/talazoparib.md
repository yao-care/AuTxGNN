---
layout: default
title: Talazoparib
parent: 中證據等級 (L3-L4)
nav_order: 651
evidence_level: L3
indication_count: 10
---

# Talazoparib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Talazoparib：從 BRCA 突變 HER2 陰性乳癌到 HER2 陽性乳癌

## 一句話總結

Talazoparib（Talzenna）是一款 PARP 抑制劑，國際核准適應症為 BRCA1/2 生殖系突變、**HER2 陰性**之局部晚期或轉移性乳癌。TxGNN 模型將其預測分數最高的新適應症標記為 **HER2 陽性乳癌**，證據等級為 **L3**，但支持證據（10 篇臨床試驗、14 篇文獻）在人工核對後幾乎全部指向 HER2 **陰性**族群，與預測標籤本身直接矛盾，判讀時需特別留意此資料品質疑義。

> ⚠️ **重要提醒**：本候選適應症的疾病標籤（HER2 陽性）與其實證資料庫中的試驗族群（HER2 陰性）不一致，很可能是本體論（ontology）比對錯誤所致，非藥物真正具有 HER2 陽性乳癌療效之訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | BRCA1/2 生殖系突變、HER2 陰性轉移性乳癌（依文獻 PMID 36952230，非本地藥證資料） |
| 預測新適應症 | HER2 Positive Breast Carcinoma（HER2 陽性乳癌） |
| TxGNN 預測分數 | 98.98%（排名 10415） |
| 證據等級 | L3 |
| 澳洲市場狀態 | 未上市（無 ARTG 登記） |
| ARTG 登記筆數 | 0 |
| 建議決策 | Hold |

---

## 為什麼此預測看似合理？

目前尚無詳細作用機轉（MOA）結構化資料，但依證據包中多篇臨床試驗摘要描述，Talazoparib 是一款口服 **PARP（poly ADP-ribose polymerase）抑制劑**，透過阻斷 DNA 單股斷裂修復酶，在 BRCA1/2 或同源重組修復（HRR）缺陷的腫瘤細胞中誘發「合成致死（synthetic lethality）」效應，進而達到抗腫瘤效果。

從機轉角度而言，PARP 抑制劑的療效理論上取決於腫瘤的 BRCA/HRD（同源重組缺陷）狀態，與 HER2 表現量並無直接因果關係。然而，Talazoparib 目前已核准及主要臨床開發族群幾乎全數限定為 **HER2 陰性**乳癌（如 NCT06735742 標題明載「HER2-Negative」，PMID 36952230 摘要亦明確定義核准族群為「HER2-negative」）。

因此，本次 TxGNN 預測的「HER2 陽性乳癌」很可能是資料標記或本體比對錯誤，而非藥物真正在該族群展現新療效訊號。若要嚴謹評估此候選適應症，需先由人工核實疾病標籤是否應更正為 HER2 陰性。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點摘要 |
|---------|------|------|------|---------|
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | gBRCA1/2 突變、**HER2 陰性**早期乳癌之 talazoparib 單藥新輔助治療 |
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | HR+ 晚期乳癌 ctDNA 導引換藥時機研究（轉譯研究，非 talazoparib 專屬） |
| [NCT06735742](https://clinicaltrials.gov/study/NCT06735742) | N/A | Active, not recruiting | 3 | TALZENNA 上市後安全性調查，族群為 BRCA 突變、**HER2 陰性**乳癌（日本）——標題與本適應症標籤矛盾 |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 併用 talazoparib 於三陰性/HER2 陰性轉移性乳癌 |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Recruiting | 36 | Talazoparib 於具 DNA 損傷修復基因異常之晚期實體瘤 |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib+talazoparib 於三陰性/BRCA1/2 陽性、**HER2 陰性**乳癌——族群與本適應症矛盾 |
| [NCT02401347](https://clinicaltrials.gov/study/NCT02401347) | Phase 2 | Completed | 21 | Talazoparib 於 BRCA 野生型三陰性乳癌或 HRR 突變實體瘤——非 HER2 陽性特異性研究 |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY2 適應性平台試驗，涵蓋含 HER2+ 在內之多種乳癌亞型，但非 talazoparib 專屬分析 |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH 生物標記導向之已核准藥物籃式試驗，已終止且樣本數小 |
| [NCT04508803](https://clinicaltrials.gov/study/NCT04508803) | Phase 2 | Completed | 37 | HX008 併用 niraparib 於生殖系突變轉移性乳癌——試驗藥物非 talazoparib |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點摘要 |
|------|-----|------|------|---------|
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | 比較性研究 | Frontiers in Immunology | 回顧性比較 talazoparib 與傳統化療；摘要內容描述族群為 HER2 **陰性**晚期乳癌，與標題「HER2-positive」不一致 |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | 真實世界世代研究 | The Oncologist | 美國真實世界 talazoparib 治療 gBRCA 突變、HER2 陰性晚期乳癌之特徵與結果（EMBRACA 核准族群） |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | 真實世界世代研究 | Clinical Breast Cancer | Mayo Clinic 真實世界 PARP 抑制劑於轉移性乳癌之處方模式與結果 |
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | 統合分析（GRADE） | Breast (Edinburgh) | PARP 抑制劑（olaparib/talazoparib）於 BRCA1/2 相關 **HER2 陰性**晚期乳癌之統合分析（義大利腫瘤內科學會） |
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | 指引回顧 | J Clin Oncol | ASCO 指引更新：HR 陽性、**HER2 陰性**轉移性乳癌之內分泌與標靶治療 |
| [35343197](https://pubmed.ncbi.nlm.nih.gov/35343197/) | 2022 | 回顧 | Indian J Cancer | PARP 抑制劑於 **HER2 陰性**轉移性乳癌治療角色綜述 |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | 回顧 | Oncology (Williston Park) | 轉移性三陰性乳癌新治療綜述，含免疫治療與抗體藥物複合體 |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | 回顧 | Mol Diagn Ther | 多族裔乳癌病人分子標靶可行性回顧，涵蓋 PARP 抑制劑（olaparib/talazoparib）核准族群 |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase 1/2 試驗報告 | Breast Cancer Res Treat | Gedatolisib+talazoparib 於晚期三陰性/BRCA1/2 陽性、**HER2 陰性**乳癌 |
| [32869930](https://pubmed.ncbi.nlm.nih.gov/32869930/) | 2020 | 基因體圖譜研究 | The Oncologist | 312 例乳癌病人之整合基因體圖譜與 PD-L1 生物標記分析 |

---

## 澳洲市場資訊

Talazoparib 目前**未於澳洲上市**，無 ARTG 登記資料，因此無法列出核准適應症、劑型或仿單內容。

---

## 細胞毒性資訊

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療（Targeted therapy）——PARP 抑制劑，透過合成致死機轉選擇性作用於 BRCA/HRD 缺陷腫瘤細胞，非傳統廣泛細胞毒殺化療 |
| 骨髓抑制風險 | 中度（依證據包中對其他適應症之風險評估註記，Talazoparib 已知常見不良反應包含骨髓抑制導致之血小板減少症） |
| 催吐性分類 | 請參考 TGA 核准仿單（PI）之警語與注意事項 |
| 監測項目 | 全血球計數（FBC，含分類計數），並依骨髓抑制風險追蹤血小板與血色素變化 |
| 處理防護 | 請參考 TGA 核准仿單（PI）之警語與注意事項 |

---

## 安全性考量

請參考 TGA 核准仿單（PI）以取得完整安全性資訊。目前查無藥物交互作用（DDI）資料。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
- 排名第一之預測適應症（HER2 陽性乳癌）與其自身佐證的試驗/文獻族群（幾乎全數為 HER2 陰性）直接矛盾，證據包本身亦已標註此為疑似標籤錯誤，須先釐清才能可靠評估。
- 藥物於澳洲未上市，且 TFDA/TGA 仿單警語與禁忌屬「Blocking」等級資料缺口（DG001），無法完成 S1 安全性初評。

**若要推進，需補充：**
- 人工核實「HER2 positive breast carcinoma」標籤是否應更正為 HER2 陰性（或改列為候選排除項）
- 取得 TGA 核准仿單（PI）之警語、禁忌與 DDI 資料
- 取得完整作用機轉（MOA）結構化資料
- 建議另行評估同一資料集中排名第 3 之 **progesterone-receptor negative breast cancer**（證據等級 L2、決策階段 S2、建議 Proceed with Guardrails），其試驗族群與 talazoparib 已知核准機轉一致性較高，證據基礎相對更扎實
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

