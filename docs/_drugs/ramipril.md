---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Ramipril is a widely used ACE inhibitor for hypertension, though no Australia-specific approved indication text is currently available because the product is **not marketed here**. The TxGNN model's top-ranked prediction for this drug is **pulmonary hypertension with unclear multifactorial mechanism**, but this specific candidate is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only prediction with no verifiable evidence trail.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor class) — no Australia-specific approved indication text available (not marketed) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ramipril in this evidence pack (flagged as a High-severity data gap). Based on generally known information, ramipril is an ACE inhibitor that blocks the renin-angiotensin-aldosterone system (RAAS), and its efficacy in hypertension is well established internationally — this classification is echoed throughout the evidence pack's own rationale text for other candidate indications (e.g., "ACE inhibitors are a known drug class mechanism for renovascular hypertension via RAAS blockade").

For this specific top-ranked prediction, however, the evidence pack itself flags the link as weak: the rationale notes that TxGNN assigned a high score despite **no supporting trials or literature**, and that the target disease description is itself labelled "unclear multifactorial mechanism" — meaning even the disease's own pathophysiology is not well defined. Blood-pressure and vascular effects of ACE inhibition are mechanistically plausible contributors to some pulmonary hypertension subtypes, but this connection is not yet supported by any verifiable data source for ramipril specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Ramipril currently has **no ARTG entries** and is **not marketed** in Australia according to this evidence pack — no product, dosage form, or approved indication text is available to list.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: this evidence pack flags TGA/PI-level warnings and contraindications as a **Blocking** data gap, meaning a formal safety pre-assessment (S1) cannot yet proceed for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This top-ranked candidate (pulmonary hypertension with unclear multifactorial mechanism) has a high TxGNN score but zero clinical trials or literature support, and the drug is not currently marketed in Australia — there is no verifiable evidence chain to act on yet.

**To proceed, the following is needed:**
- TGA-approved Product Information / warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data via DrugBank (currently a High-severity data gap)
- Disease-specific clinical trial or literature evidence for this exact predicted indication
- Consider instead prioritising this drug's other TxGNN-predicted indications with stronger evidence in this same pack — notably **cerebral artery occlusion** (Evidence Level L2, 1 completed Phase 2 trial + 5 publications) and **intracerebral hemorrhage** (Evidence Level L3, 4 publications) — which may offer a more actionable starting point for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

