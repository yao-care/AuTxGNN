---
layout: default
title: Prazosin
parent: 僅模型預測 (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
---

# Prazosin
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

# Prazosin: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Prazosin is an alpha-1 adrenergic receptor antagonist, historically used to treat hypertension (it is not currently marketed in Australia). The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but at present **no clinical trials** and **no published literature** specifically support this indication — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(general pharmacological knowledge — no Australian regulatory record exists for this field, as the drug is not marketed here)* |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 90.23% |
| Evidence Level | L5 (no clinical trials or literature identified for this specific indication) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Prazosin is not available in this evidence pack. Based on the repurposing rationale supplied by the model, Prazosin is an **alpha-1 adrenergic receptor antagonist**, a mechanism well established for lowering blood pressure in essential hypertension.

The theoretical link to malignant hypertensive renal disease is that blood-pressure control via alpha-1 blockade could, in principle, indirectly reduce the renal damage driven by malignant hypertension. However, this is a mechanistic extrapolation only — there is no indication-specific literature or trial evidence confirming efficacy in this exact disease. The prediction reflects TxGNN's inference from drug class (antihypertensive) and semantic proximity between the original and predicted disease terms, rather than any direct clinical observation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Prazosin is **not marketed in Australia** — there are no ARTG entries on record, so no product/dosage-form table can be produced.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. *(No key warnings, contraindications, or drug interaction data were returned for this drug — a DDI query specifically came back "not found".)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- With zero clinical trials and zero literature specific to "malignant hypertensive renal disease," this candidate has no empirical support beyond the raw TxGNN model score — insufficient to progress past initial screening.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information — warnings and contraindications (currently a **Blocking** data gap; required before any safety assessment can begin)
- Detailed mechanism of action (MOA) data from DrugBank (currently a **High**-severity data gap; needed to assess mechanistic plausibility)
- At least indication-specific preclinical or observational evidence before this candidate can move beyond Hold
- **Alternative worth reviewing**: "Malignant renovascular hypertension" (rank 2, same TxGNN score band) has materially stronger support — 3 relevant publications including a 1975 drug-specific clinical case series (PMID 1055318) showing Prazosin's efficacy in severe renovascular hypertension — and is already at evidence level L3 / decision stage S1 ("Research Question"). This may be a more productive candidate to prioritise than rank 1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

