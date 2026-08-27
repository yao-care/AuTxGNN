---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lenalidomide：從多發性骨髓瘤／缺失5q骨髓化生不良症候群 到 骨髓性白血病

## 一句話摘要

Lenalidomide（來那度胺）目前已知用於多發性骨髓瘤及帶有5q缺失異常之骨髓化生不良症候群（MDS）治療。
TxGNN 模型預測其可能對**骨髓性白血病（Myeloid Leukemia）**有效，
目前有 **0 項專屬臨床試驗**與 **20 篇相關文獻**支持此方向，其中包含 2 篇系統性回顧／統合分析。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 台灣藥證資料無記錄（未上市）；依證據包內文獻，Lenalidomide 已知用於多發性骨髓瘤（合併 dexamethasone）及 del(5q) 異常之 MDS |
| Predicted New Indication | Myeloid Leukemia（骨髓性白血病） |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L3（系統性回顧／統合分析 + 前瞻性早期臨床研究，未見該適應症之已完成 Phase 2/3 RCT） |
| Australia Market Status | 未上市 |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

作用機轉資料在本證據包中標記為資料缺口（DG002）。然而證據包所收錄的文獻本身提供了機轉線索：Lenalidomide 是衍生自 thalidomide 的口服免疫調節藥物（immunomodulatory drug, IMiD）；其抗白血病活性透過結合 cereblon（CRBN）E3 泛素連接酶複合體，促使 IKZF1/IKZF3 泛素化並降解而發揮作用（PMID 23316859、39881283）。此機轉屬於分子標靶型態，而非傳統細胞毒殺型化療。

多發性骨髓瘤與 del(5q) MDS 皆屬於骨髓造血幹細胞區室的克隆性疾病，而 MDS 本身即有相當比例會轉化為急性骨髓性白血病（AML）。這使得 Lenalidomide 用於「骨髓性白血病」的預測在病理生理上具有合理性——證據包中已收錄多篇將 Lenalidomide 併用 azacitidine 用於高風險 MDS、AML、慢性骨髓單核球性白血病（CMML）的研究（如 PMID 31221030 統合分析、PMID 30271212 系統性回顧），顯示此老藥新用方向並非僅止於模型推論，臨床探索已有一定基礎。

---

## Clinical Trial Evidence

目前無與「Myeloid Leukemia」直接關聯之已登錄臨床試驗。

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | 系統性回顧／統合分析 | Hematology (Amsterdam) | Azacitidine 併用 Lenalidomide 治療 AML、高風險 MDS、CMML 之療效與不良事件統合分析 |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | 系統性回顧／統合分析 | Cancer Management and Research | Lenalidomide 治療 AML 之療效與安全性系統性回顧 |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | 前瞻性臨床研究（Azalena-Trial） | Haematologica | Azacitidine + Lenalidomide + 供者淋巴球輸注，用於異體移植後 AML/MDS/CMML 復發之第一線 salvage 治療 |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | 前瞻性研究 | Frontiers in Immunology | Azacitidine + 低劑量 Lenalidomide 作為 AML 異體移植後復發預防之維持療法 |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib 試驗 | Journal of Geriatric Oncology | Lenalidomide 作為老年 AML 患者緩解後維持治療之安全性評估 |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase I 劑量遞增研究 | Bone Marrow Transplantation | Lenalidomide 維持療法用於移植後高風險 AML/MDS 之安全性與耐受性 |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | 原始研究 | Blood | Lenalidomide 與 TP53 突變治療相關骨髓腫瘤（t-MN）發生之關聯性分析 |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | 綜述 | Expert Opinion on Investigational Drugs | Lenalidomide 作為 AML 新治療選項之機轉與臨床發展回顧 |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | 綜述 | Blood | MDS 臨床決策與治療策略更新 |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | 綜述 | Lancet | 骨髓化生不良症候群整體回顧，含轉化為 AML 之病程說明 |

---

## Safety Considerations

請參考 TGA 核可之藥品仿單（Product Information, PI）以取得完整安全性資訊。

（本證據包標記 TFDA 仿單警語／禁忌為 Blocking 等級資料缺口 DG001，DDI 查詢無結果，安全性初評 S1 目前無法進行。）

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- 仿單安全性資料為 Blocking 等級缺口（DG001），無法完成 S1 安全性初評；藥品目前未於澳洲上市（0 筆 ARTG 登錄）；「Myeloid Leukemia」此一預測適應症目前僅有系統性回顧與早期前瞻性研究支持，未見已完成之 Phase 2/3 RCT，證據等級為 L3。

**To proceed, the following is needed:**
- 取得 TFDA／TGA 核准仿單（警語、禁忌、藥物交互作用）— Blocking，需優先補齊
- 透過 DrugBank API 補齊作用機轉（MOA）結構化資料
- 檢索是否有專門針對「骨髓性白血病／AML」適應症之已完成 Phase 2/3 RCT（現有試驗多集中於 MDS del(5q) 或多發性骨髓瘤族群）
- 若考慮於澳洲市場申請新適應症，需評估 ARTG 登錄路徑（現況未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

