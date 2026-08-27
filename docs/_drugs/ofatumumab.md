---
layout: default
title: Ofatumumab
parent: 高證據等級 (L1-L2)
nav_order: 485
evidence_level: L1
indication_count: 10
---

# Ofatumumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Ofatumumab：從尚未於澳洲上市，到預測用於慢性淋巴球性白血病/小淋巴球性淋巴瘤

## 一句話摘要

Ofatumumab（DrugBank：DB06650）為全人源抗 CD20 單株抗體，目前**未於澳洲上市**（ARTG 收錄數為 0），本地原始核准適應症資料尚缺。
TxGNN 模型預測其可用於**慢性淋巴球性白血病/小淋巴球性淋巴瘤（CLL/SLL）**，
此為 Ofatumumab 在國際上已具實證基礎的既有用途方向，目前有 **34 項相關臨床試驗**（含多項完成的 Phase 3 RCT）與 **20 篇文獻**支持。
另有次要方向濾泡性淋巴瘤（follicular lymphoma）以多項 Phase 2 試驗支持，機轉相同（詳見下方說明）。

---

## 重點總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 尚無本地（澳洲）核准適應症資料；藥品目前未於澳洲上市 |
| 預測新適應症 | 慢性淋巴球性白血病/小淋巴球性淋巴瘤（CLL/SLL） |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L1 |
| 澳洲市場狀態 | 未上市 |
| ARTG 收錄數量 | 0 |
| 建議決策 | Proceed with Guardrails（有條件推進） |

---

## 為什麼這個預測合理？

根據證據包內的機轉關聯說明，Ofatumumab 是全人源抗 CD20 單株抗體，透過補體依賴性細胞毒殺（CDC）與抗體依賴性細胞毒殺（ADCC）機轉清除 CD20 陽性 B 淋巴球。CLL/SLL 屬於 CD20 陽性 B 細胞惡性腫瘤，機轉直接對應。此適應症在部分國際市場已為核准用途，本站標記「未上市」僅反映澳洲當地法規登記狀態，並非療效存在不確定性。

支持證據相當扎實：現有已完成的 Phase 3 RCT 包括 NCT00824265（ofatumumab 併用 fludarabine-cyclophosphamide vs. 單用 FC，n=365，復發性 CLL）、NCT02004522（Duvelisib vs. Ofatumumab 頭對頭試驗，n=319）、NCT01578707（Ibrutinib vs. Ofatumumab，RESONATE，n=391）等，符合 L1 證據等級門檻（≥2 項已完成 Phase 3 RCT）。

同一藥物證據包中，另有次要方向「濾泡性淋巴瘤」（TxGNN 分數 99.70%，證據等級 L2）機轉相同（同屬 CD20+ B 細胞淋巴瘤），並有多項 Phase 2 試驗（如 NCT01190449、NCT01294579）支持初治族群療效，可作為後續追蹤方向。至於惡性螺旋腺瘤、Langerhans 細胞組織球增生症、組織細胞/樹突細胞腫瘤及兒童縱膈神經源性腫瘤等其他預測（證據等級 L5、決策階段 S0），因無任何試驗或文獻支持，且細胞來源與 CD20 表現無關，證據包本身已標註為模型雜訊，建議排除，不納入本報告主要評估範圍。

需注意：MOA 詳細資料（DrugBank 查詢）與 TFDA/PI 仿單警語資料目前仍為缺口（DG001、DG002），其中 DG001 屬 Blocking 等級，會影響安全性初評（S1）的進行，即便療效證據已達 L1，最終決策仍需待此缺口補齊。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00824265](https://clinicaltrials.gov/study/NCT00824265) | Phase 3 | Completed | 365 | Ofatumumab 併用 fludarabine-cyclophosphamide vs. 單用 FC，評估復發性 CLL 安全性與療效 |
| [NCT02004522](https://clinicaltrials.gov/study/NCT02004522) | Phase 3 | Completed | 319 | DUO 試驗：Duvelisib vs. Ofatumumab 單藥頭對頭比較，復發/難治 CLL/SLL |
| [NCT01578707](https://clinicaltrials.gov/study/NCT01578707) | Phase 3 | Completed | 391 | RESONATE 試驗：Ibrutinib vs. Ofatumumab，評估 PFS 於復發/難治 CLL/SLL |
| [NCT01313689](https://clinicaltrials.gov/study/NCT01313689) | Phase 3 | Completed | 122 | Ofatumumab vs. 醫師選擇治療，用於 bulky fludarabine-refractory CLL 之確認性試驗 |
| [NCT01039376](https://clinicaltrials.gov/study/NCT01039376) | Phase 3 | Terminated | 480 | Ofatumumab 維持治療 vs. 觀察，復發 CLL 已對誘導治療反應者 |
| [NCT01217749](https://clinicaltrials.gov/study/NCT01217749) | Phase 1b/2 | Completed | 71 | BTK 抑制劑（PCI-32765）併用 Ofatumumab，復發/難治 CLL/SLL |
| [NCT02049515](https://clinicaltrials.gov/study/NCT02049515) | Phase 3 | Completed | 99 | Duvelisib 或 Ofatumumab 單藥治療於前期研究病程進展病人（延伸試驗） |
| [NCT01453062](https://clinicaltrials.gov/study/NCT01453062) | N/A | Completed | 1 | 歐盟真實世界觀察性研究，CLL 病人接受 Ofatumumab 治療 |
| [NCT01520922](https://clinicaltrials.gov/study/NCT01520922) | Phase 2 | Completed | 99 | Ofatumumab 併用 bendamustine，未治療或復發 CLL |
| [NCT01024010](https://clinicaltrials.gov/study/NCT01024010) | Phase 2 | Completed | 82 | Ofatumumab 併用 pentostatin、cyclophosphamide，未治療 CLL/SLL |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31512258](https://pubmed.ncbi.nlm.nih.gov/31512258/) | 2019 | RCT（長期追蹤） | American Journal of Hematology | RESONATE 試驗最終分析，Ibrutinib 對比 Ofatumumab 於已治療 CLL/SLL，最長 6 年追蹤結果 |
| [37138022](https://pubmed.ncbi.nlm.nih.gov/37138022/) | 2023 | Meta-analysis | Annals of Hematology | 統合分析評估 Ofatumumab 治療 CLL 之整體療效 |
| [25828085](https://pubmed.ncbi.nlm.nih.gov/25828085/) | 2015 | Review | Haematologica | 綜述 Ofatumumab 作為 CLL 免疫治療之角色 |
| [20481657](https://pubmed.ncbi.nlm.nih.gov/20481657/) | 2010 | Review | Drugs | Ofatumumab 藥理特性回顧，含關鍵性 fludarabine/alemtuzumab 難治 CLL 研究 |
| [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/) | 2015 | Review（安全性） | Expert Opinion on Drug Safety | Ofatumumab 治療 CLL 之安全性剖析 |
| [25736010](https://pubmed.ncbi.nlm.nih.gov/25736010/) | 2015 | Guideline | Journal of the National Comprehensive Cancer Network | CLL/SLL 治療指引，列入 Ofatumumab 作為核准單株抗體選項 |
| [20068404](https://pubmed.ncbi.nlm.nih.gov/20068404/) | 2009 | Review | mAbs | Ofatumumab 藥物概述，含 CLL 核准申請背景 |
| [28782884](https://pubmed.ncbi.nlm.nih.gov/28782884/) | 2017 | Review | American Journal of Hematology | CLL 診斷、風險分層與治療更新 |
| [29212732](https://pubmed.ncbi.nlm.nih.gov/29212732/) | 2018 | Review | The Oncologist | CLL 治療中抗 CD20 單株抗體（含 Ofatumumab）角色與生物相似藥探討 |
| [24947256](https://pubmed.ncbi.nlm.nih.gov/24947256/) | 2014 | Review | Future Oncology | Ofatumumab 作為未治療 CLL 一線治療之定位討論 |

---

## 澳洲市場資訊

Ofatumumab 目前**未於澳洲藥品登記系統（ARTG）註冊**，無任何核准劑型或適應症紀錄。

---

## 細胞毒性資訊

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療／免疫治療（抗 CD20 單株抗體，非傳統化療藥物） |
| 骨髓抑制風險 | 請參考核准仿單（PI）警語與注意事項 |
| 致吐性分類 | 請參考核准仿單（PI）警語與注意事項 |
| 監測項目 | 請參考核准仿單（PI）警語與注意事項 |
| 處理防護 | 請參考核准仿單（PI）警語與注意事項 |

---

## 安全性考量

目前無可用之警語、禁忌症或藥物交互作用資料。請參考 TGA 核准之產品說明書（PI）以取得安全性資訊。

---

## 結論與後續步驟

**決策：Proceed with Guardrails（有條件推進）**

**理由：**
CLL/SLL 適應症方向已有多項已完成的 Phase 3 RCT 支持（符合 L1 證據等級），機轉明確且部分市場已核准此用途；但藥品本身之 TFDA/PI 仿單警語與詳細作用機轉資料仍為缺口（其中仿單警語資料為 Blocking 等級缺口），在完整安全性初評（S1）尚未完成前，不建議直接列為 Go。

**推進所需補充：**
- 取得 TFDA（或澳洲對應之 TGA）仿單警語與禁忌症資料，完成 S1 安全性初評
- 補齊 DrugBank 作用機轉（MOA）詳細資料，強化機轉關聯性分析
- 若考慮推進次要方向濾泡性淋巴瘤，需另行評估其證據等級（現為 L2）是否足以支持後續決策階段
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

