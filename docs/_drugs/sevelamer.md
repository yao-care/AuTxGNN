---
layout: default
title: Sevelamer
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Sevelamer
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

# Sevelamer: From Hyperphosphatemia in Chronic Kidney Disease to Breast Fibrocystic Disease

## One-Sentence Summary

Sevelamer is an oral phosphate-binding polymer conventionally used for hyperphosphatemia in dialysis-dependent chronic kidney disease patients.
The TxGNN model's highest-scoring prediction is **Breast Fibrocystic Disease**, with a prediction score of **92.46%**,
but currently **zero clinical trials** and **zero publications** support this specific link, and the model's own rationale states no known mechanistic connection exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — Sevelamer is not ARTG-registered in Australia. (Description above is inferred from phosphate-binding/dialysis context mentioned in the supporting trial and literature records, not from formal regulatory data.) |
| Predicted New Indication | Breast Fibrocystic Disease |
| TxGNN Prediction Score | 92.46% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Sevelamer in this evidence pack (flagged as a High-severity data gap). Based on information embedded elsewhere in the evidence pack — trial descriptions and literature rationale for other candidate indications — Sevelamer is recognised internationally as a non-absorbed, enteral phosphate- and bile-acid-binding polymer, historically used to manage hyperphosphatemia in dialysis patients.

For the top-ranked prediction, **Breast Fibrocystic Disease**, the model's own repurposing rationale is explicit that there is **no known mechanistic link**: "Sevelamer 為腸道磷酸鹽/膽酸結合劑，與乳房纖維囊性病變之荷爾蒙／增生機轉無已知關聯，純屬 TxGNN 模型預測分數，無任何臨床或機轉支持" (Sevelamer is an intestinal phosphate/bile-acid binder with no known relationship to the hormonal or proliferative mechanisms of fibrocystic breast disease; this is a model score alone, with no clinical or mechanistic support). The same applies to the other breast-tissue-related predictions in this evidence pack (ranks 2, 3, 4, 7, 8) and the unrelated rare neurodevelopmental disorder prediction (rank 10) — all are Evidence Level L5, Hold.

Notably, this evidence pack also contains lower-ranked but far better-supported candidates for the same drug: **AIDS** (rank 6, Evidence Level L2, one completed Phase 2 trial plus three publications) and **HIV infectious disease** (rank 5, Evidence Level L3, two publications), both grounded in a plausible mechanism — Sevelamer binding intestinal lipopolysaccharide to reduce microbial translocation and chronic immune activation. Reviewers may wish to prioritise those candidates over the top-scored but mechanistically unsupported breast fibrocystic disease prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that Sevelamer is not currently marketed in Australia, so no ARTG-approved local PI exists; overseas regulatory labelling (e.g. FDA/EMA) should be consulted as an interim reference. Formal TFDA/TGA warning and contraindication data was not retrievable for this evidence pack (Blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top TxGNN-predicted indication (Breast Fibrocystic Disease) has a high model score but zero supporting clinical trials or literature, and the model's own rationale confirms no known mechanistic plausibility — this is Evidence Level L5, insufficient to progress.
- A Blocking data gap (missing TGA/TFDA product information warnings and contraindications) prevents even an initial safety screen (S1) for this drug.

**To proceed, the following is needed:**
- TGA/TFDA-approved Product Information (warnings, contraindications, DDI) — currently blocking
- Mechanism of action data from DrugBank — currently missing
- Any preclinical or mechanistic evidence linking phosphate/bile-acid binding to fibrocystic breast pathophysiology, if this indication is to be pursued further
- Alternatively, consider redirecting evaluation toward the better-evidenced AIDS/HIV candidates in this same evidence pack (completed Phase 2 trial NCT01543958, five supporting publications), which warrant a separate S1/S2 safety and evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

