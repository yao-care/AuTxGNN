---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Fosinopril is an angiotensin-converting enzyme (ACE) inhibitor established in the treatment of hypertension.
> The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction score alone is high, the underlying evidence base is not.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor class) — no ARTG-approved indication text available, since this product is not currently marketed in Australia |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form for this evidence pack. Based on established pharmacology, fosinopril is an ACE inhibitor: it blocks conversion of angiotensin I to angiotensin II, lowering systemic vascular resistance and intraglomerular pressure. This class-level mechanism is referenced repeatedly across the other candidate indications in this same evidence pack (e.g. the diabetic nephropathy and chronic pulmonary heart disease entries below), which describe fosinopril reducing angiotensin II generation and proteinuria.

Malignant hypertensive renal disease is, by definition, severe/accelerated hypertension causing renal microvascular damage. A drug that lowers blood pressure and reduces intraglomerular pressure is mechanistically plausible for this indication — but plausibility is not the same as evidence. TxGNN's score reflects a graph-based relational inference, not a direct pharmacological study of fosinopril in this specific condition.

Importantly, this evidence pack flags a closely related candidate (rank 2, "malignant renovascular hypertension," same score) where ACE inhibitors carry a specific safety caveat: they are relatively contraindicated when bilateral renal artery stenosis is present, and can precipitate acute renal failure in that setting. Because "malignant hypertensive renal disease" and "malignant renovascular hypertension" sit adjacent in the TxGNN output with identical scores, this caution is clinically relevant here too and should not be overlooked simply because it was attached to a neighbouring candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

This medicine is not currently marketed in Australia — there are 0 ARTG entries for fosinopril in this evidence pack, so no product/dosage-form table can be produced.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — no structured warnings, contraindications, or drug interaction data were retrievable in this evidence pack (query status: not found).

**Note:** A closely related candidate indication in this same evidence pack (malignant renovascular hypertension) carries an explicit caution — ACE inhibitors are relatively contraindicated in bilateral renal artery stenosis, where they can precipitate acute renal failure. Given the clinical overlap between renovascular and malignant hypertensive renal disease, renal artery status should be assessed before considering fosinopril in this population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this candidate has zero supporting clinical trials or literature, is not currently marketed in Australia, and the drug-level safety data needed for even a preliminary safety screen (TGA PI warnings/contraindications) is a blocking data gap. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings and contraindications) — currently a blocking data gap
- Confirmed mechanism of action data from DrugBank or equivalent source
- Preclinical or clinical evidence specific to malignant hypertensive renal disease (not just class-level ACEI data)
- Clarification of renal artery stenosis status in any target population, given the ACEI contraindication risk noted for the adjacent renovascular hypertension candidate
- Confirmation of Australian market/import pathway, since the product currently has no ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

