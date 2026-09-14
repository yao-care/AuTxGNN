---
layout: default
title: Triethylenetetramine
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
---

# Triethylenetetramine
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

# Triethylenetetramine: From Copper Chelation to Thyroid Gland Undifferentiated (Anaplastic) Carcinoma

## One-Sentence Summary

Triethylenetetramine (Trientine, DrugBank ID DB06824) is a copper-chelating agent; the evidence pack does not contain a formally recorded original indication (TGA-approved indication text is a Blocking data gap), but the drug is internationally known for copper chelation therapy. The TxGNN model's top prediction is **Thyroid Gland Undifferentiated (Anaplastic) Carcinoma**, with a prediction score of 99.87%, but this is supported by **zero clinical trials and zero publications**, and the model's own rationale flags it as possible knowledge-graph noise rather than a biologically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TGA-approved indication text is missing from this evidence pack (Blocking Data Gap DG001). Internationally recognised as a copper chelator. |
| Predicted New Indication | Thyroid Gland Undifferentiated (Anaplastic) Carcinoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable (Data Gap DG002). Based on the drug classification referenced throughout this evidence pack, Triethylenetetramine acts as a copper chelator, a mechanism most relevant to copper-overload conditions such as Wilson's disease.

The top-ranked prediction — thyroid gland undifferentiated (anaplastic) carcinoma — has **no established mechanistic link** to copper chelation. The model's own repurposing rationale for this candidate explicitly states: *"there is no known association between anaplastic thyroid carcinoma and copper-chelating mechanisms; the high TxGNN score may reflect graph noise rather than biological plausibility, and no evidence supports it."* This should be read as a caution against over-interpreting the raw TxGNN score.

Notably, among the 10 candidates in this pack, rank 5 — **idiopathic copper-associated cirrhosis** — has a substantially stronger mechanistic rationale (direct correspondence between copper chelation and copper-associated liver disease) and is flagged by the model as a "Research Question" rather than "Hold," despite a lower raw score and L4 evidence level. This suggests the top-ranked prediction by score is not necessarily the most biologically credible candidate in this set, and mechanistic plausibility should be weighted alongside raw prediction rank when prioritising follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Triethylenetetramine currently has no ARTG entries and is **Not Marketed** in Australia (`total_licenses: 0`). No product, dosage form, or approved indication information is available in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack does not contain safety warnings, contraindications, or drug interaction data — the absence of TGA-equivalent warnings/contraindications is flagged as a **Blocking data gap (DG001)** that must be resolved before any safety-relevant evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (thyroid gland undifferentiated carcinoma) has an L5 evidence level with no clinical trials, no literature, and a mechanistic rationale that the model itself characterises as likely noise rather than a genuine signal. Combined with a Blocking safety data gap (TGA-equivalent warnings/contraindications not available), there is insufficient basis to advance this candidate beyond S0.

**To proceed, the following is needed:**
- Resolve Blocking Data Gap DG001 (TGA-equivalent warnings/contraindications, via source PI)
- Resolve High-priority Data Gap DG002 (confirmed mechanism of action, via DrugBank)
- Obtain a formally documented original indication/regulatory history for Triethylenetetramine
- If pursuing further evaluation, prioritise mechanistically coherent candidates (e.g. idiopathic copper-associated cirrhosis, rank 5) over the top-scored but mechanistically unsupported thyroid carcinoma prediction
- Independent literature/clinical trial search specific to copper-chelation-relevant oncology and hepatology indications, as none currently exist in this pack for any of the 10 candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

