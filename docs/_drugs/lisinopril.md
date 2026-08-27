---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension/Heart Failure to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is a well-established ACE inhibitor used for hypertension and heart failure. The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on model similarity scoring alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (no ARTG-approved indication text available); Lisinopril is an established ACE inhibitor used for hypertension and heart failure |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Lisinopril is an ACE inhibitor; its efficacy in hypertension and in reducing post-myocardial-infarction morbidity is well established, and mechanistically this class is already used for ventricular remodelling and afterload reduction after MI.

However, the specific prediction here targets an anatomical MI subtype (posterolateral). ACE inhibitor benefit after myocardial infarction in general is already established clinical practice, but this evidence pack contains no trials or literature specific to the posterolateral subtype that would distinguish this prediction from that general, already-known post-MI ACEi effect. The high TxGNN score appears to reflect embedding similarity across MI-related disease terms rather than subtype-specific evidence.

Because no supporting studies were retrieved for this exact indication, the mechanistic plausibility cannot currently be separated from a false-positive signal driven by the knowledge graph structure.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries were found for Lisinopril in this evidence pack (total licenses: 0; market status: not marketed). No product-level dosage form or approved-indication data is currently available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No specific warnings, contraindications, or drug-interaction data were retrieved for this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for posterolateral myocardial infarction is evidence level L5 — a model prediction with zero supporting clinical trials or literature — and cannot currently be distinguished from the already-established general post-MI use of ACE inhibitors. Safety documentation (TGA PI, warnings, contraindications) is also unavailable, which blocks any preliminary safety assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap
- Mechanism of action detail from DrugBank to support or refute the mechanistic rationale
- Literature or trial evidence specific to the posterolateral MI subtype (rather than general post-MI ACEi use)
- Confirmation of Australian market/registration status, since no ARTG entries were found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

