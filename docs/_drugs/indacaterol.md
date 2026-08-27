---
layout: default
title: Indacaterol
parent: 高證據等級 (L1-L2)
nav_order: 348
evidence_level: L1
indication_count: 10
---

# Indacaterol
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

# Indacaterol：從 COPD／氣喘維持治療 到 支氣管疾病（廣義適應症擴展）

## 一句話摘要

Indacaterol 是一種長效型 β2-腎上腺素受體促效劑（LABA），已知的臨床使用機轉為 COPD／氣喘維持治療的支氣管擴張劑成分之一，但**尚未在台灣上市**（無 TFDA 核准字號）。TxGNN 模型針對此藥共列出 10 項預測新適應症，其中僅**「支氣管疾病（bronchial disease）」**具備實質支持——**37 筆臨床試驗**與**20 篇文獻**，且多筆為 Phase 3 大型對照試驗；其餘 9 項預測分數雖高，但均無臨床試驗或文獻佐證，且部分機轉方向與藥理學已知作用相反。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（台灣未上市，無 TFDA 核准適應症紀錄；證據包內機轉敘述顯示國際間核准用途為 COPD／氣喘維持治療） |
| 預測新適應症 | Bronchial disease（支氣管疾病，廣義呼吸道適應症類別） |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L1 |
| 台灣上市狀態 | 未上市 |
| TFDA 核准字號筆數 | 0 |
| 建議決策 | Proceed with Guardrails（附條件推進） |

> 註：TxGNN 依分數排序的第一名預測為「nephrogenic syndrome of inappropriate antidiuresis」（分數 99.54%），但該候選完全無臨床試驗、無文獻，且模型自身的機轉理由已明確指出與 β2 促效機轉無關（見文末「其他預測適應症」）。本報告以**證據等級最高、具實際決策價值**的「支氣管疾病」作為主要評估對象。

---

## 為什麼這個預測合理？

目前尚無完整的作用機轉（MOA）結構化資料可用（DrugBank 查詢欄位為資料缺口）。但根據證據包內機轉敘述，Indacaterol 為**長效型 β2-腎上腺素受體促效劑（LABA）**，透過活化氣道平滑肌上的 β2 受體促使支氣管擴張，此機轉已是其國際間核准用於 COPD 與氣喘維持治療的臨床應用基礎。

「支氣管疾病」為廣義的呼吸道適應症分類，與 Indacaterol 既有的 COPD／氣喘適應症在病理生理上高度重疊，因此 TxGNN 預測在機轉上具有直接、明確的藥理對應關係，而非跨系統的新穎連結。換言之，此項預測較接近**既有核准用途的分類擴展確認**，而非傳統意義上的「老藥新用」。也因此，證據強度雖高（L1），但臨床新穎性有限，實際效益需視此分類是否對應到台灣尚未涵蓋的特定適應症子類別而定。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | 已完成 | 2216 | 比較兩種劑量 QMF149（indacaterol／mometasone）與 mometasone 單方於控制不佳氣喘患者之療效與安全性 |
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Phase 3 | 已完成 | 3092 | 比較 QVM149（indacaterol/glycopyrronium/mometasone 三合一）與 QMF149 兩種劑量之療效與安全性 |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | 已完成 | 805 | 以 salmeterol 為活性對照，評估 indacaterol 300/600 µg 於中重度持續性氣喘患者 26 週安全性 |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Phase 3 | 已完成 | 1426 | QVM149 對比 salmeterol/fluticasone + tiotropium 自由組合治療，證實非劣性 |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | 已完成 | 511 | 以 salmeterol 為活性對照之隨機雙盲試驗，評估 indacaterol 14 天支氣管擴張療效 |
| [NCT00941798](https://clinicaltrials.gov/study/NCT00941798) | Phase 2 | 已完成 | 2283 | QMF149 與 mometasone 單方之安全性比較，事件驅動試驗評估嚴重氣喘惡化發生率 |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | 已完成 | 335 | 12 週劑量探索試驗，支持 QMF149 固定劑量組合之劑量選擇 |
| [NCT05562466](https://clinicaltrials.gov/study/NCT05562466) | Phase 3 | 招募中 | 200 | QMF149 對比 budesonide，於 6-12 歲兒童氣喘患者之療效與安全性 |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | 已完成 | 79 | 評估 indacaterol acetate 於 6-12 歲兒童氣喘患者之肺功能與全身暴露量 |
| [NCT02059434](https://clinicaltrials.gov/study/NCT02059434) | Phase 1 | 已完成 | 55 | 吸入式支氣管擴張劑於氣喘與 COPD 患者之安全性、耐受性與藥效初步試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT (Phase 3) | Lancet Respir Med | IRIDIUM 試驗：每日一次 mometasone-indacaterol-glycopyrronium 三合一 vs. 雙合一或每日兩次 fluticasone-salmeterol，用於控制不佳氣喘患者 |
| [33711782](https://pubmed.ncbi.nlm.nih.gov/33711782/) | 2021 | 匯總分析（Phase 3） | Respir Med | 匯總多項 Phase 3 試驗，評估 mometasone/indacaterol 與三合一組合之心血管安全性 |
| [28768531](https://pubmed.ncbi.nlm.nih.gov/28768531/) | 2017 | RCT（交叉試驗） | Respir Res | 三向交叉試驗，評估 glycopyrronium 與 indacaterol 單用及合併對輕度氣喘患者 methacholine 劑量反應曲線之影響 |
| [35348408](https://pubmed.ncbi.nlm.nih.gov/35348408/) | 2023 | 開放性長期安全性研究 | J Asthma | 兩項 52 週開放性研究，評估 IND/GLY/MF 高劑量於日本氣喘患者之長期安全性 |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | 藥動橋接研究 | Pulm Pharmacol Ther | MF/IND 與 MF/IND/GLY 固定劑量組合間 mometasone 劑量橋接資料 |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | Indacaterol/glycopyrronium/mometasone（Enerzair）於氣喘治療之整體回顧 |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Review | Adv Ther | Indacaterol 作為新型每日一次 LABA 於阻塞性呼吸道疾病治療之臨床前及臨床資料回顧 |
| [39905183](https://pubmed.ncbi.nlm.nih.gov/39905183/) | 2025 | 系統性回顧與統合分析 | Sci Rep | 比較不同三合一治療於控制不佳氣喘患者之相對療效 |
| [35072888](https://pubmed.ncbi.nlm.nih.gov/35072888/) | 2022 | Review | Adv Ther | IND/GLY/MF 首創同類每日一次三合一固定劑量組合藥物開發策略回顧 |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Review | Respir Med | Ultra-LABA（含 indacaterol）於氣喘治療角色之回顧 |

---

## 台灣市場資訊

目前查無 TFDA 核准之 Indacaterol 上市許可證（`total_licenses = 0`），台灣市場狀態為**未上市**。此為進入下一階段評估前需優先補齊的資料缺口（見結論）。

---

## 安全性考量

請參閱 TFDA 核准之藥品仿單（PI）以獲取安全性資訊。目前查無仿單警語、禁忌症及藥物交互作用（DDI）資料，此為 Blocking 等級資料缺口，須於下一階段補齊後方可進行初步安全性評估。

---

## 結論與後續步驟

**決策：Proceed with Guardrails（附條件推進）**

**理由：**
「支氣管疾病」預測具備多筆已完成 Phase 3 大型對照試驗與 20 篇文獻支持（L1），機轉合理性明確，但此適應症分類與 Indacaterol 既有 LABA 核准用途重疊度高，臨床新穎性有限；同時台灣尚未上市、仿單安全性資料全數缺口，須待補齊後才能進入正式安全性初評。

**推進前需補齊：**
- TFDA 仿單警語、禁忌症資料（Blocking，DG001）
- DrugBank 完整作用機轉（MOA）資料（High，DG002）
- 台灣上市申請狀態追蹤（目前 0 筆核准字號）
- 釐清「支氣管疾病」此廣義分類相對於現行 COPD／氣喘適應症的實際新增臨床價值

---

### 附註：其他 TxGNN 預測適應症（證據不足，暫緩）

以下 9 項候選適應症雖 TxGNN 分數與「支氣管疾病」相近甚至更高，但均無臨床試驗或文獻支持，證據等級 L5，建議 **Hold**：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉合理性摘要 |
|------|-----------|-----------|---------------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 99.54% | V2 受體基因突變致病，與 β2 促效機轉無關 |
| 2 | Headache disorder | 99.53% | 所列試驗實為 COPD 耐受性研究，頭痛僅為不良反應監測項目；β 阻斷劑（非促效劑）才是偏頭痛預防機轉，方向相反 |
| 3 | Trigeminal autonomic cephalalgia | 99.33% | 無已知機轉關聯 |
| 4 | Paratenonitis | 99.26% | 無已知機轉關聯 |
| 5 | Calcific tendinitis | 99.25% | 無已知機轉關聯 |
| 6 | Hypertrichosis (disease) | 99.23% | 多毛症機轉為鉀通道開放劑，與 β2 促效無關 |
| 8 | Myositis | 99.12% | 無實證支持 |
| 9 | Anaphylaxis | 99.07% | 過敏性休克首選為腎上腺素，indacaterol 起效與藥動特性不適用於急性處置 |
| 10 | Ambras type hypertrichosis universalis congenita | 99.06% | 染色體重排罕見疾病，與藥理路徑無關 |

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後方可應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

