---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

> Vildagliptin is a DPP-4 inhibitor originally used to improve glycaemic control in type 2 diabetes mellitus by enhancing endogenous incretin (GLP-1/GIP) activity.
> The TxGNN model's top-ranked prediction is **Classic Stiff Person Syndrome**, with a score of **99.88%**,
> but currently **0 clinical trials** and **0 publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (per literature evidence; DPP-4 inhibitor / incretin-based therapy) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa` is marked as a data gap). Based on the supporting literature captured elsewhere in this pack, vildagliptin is a selective DPP-4 inhibitor that raises endogenous GLP-1 and GIP levels, thereby enhancing glucose-dependent insulin secretion and suppressing glucagon release — its established mechanism in type 2 diabetes.

Classic Stiff Person Syndrome, however, is an autoimmune neurological disorder mediated by anti-GAD65 antibodies that disrupts GABAergic neurotransmission. There is no known mechanistic overlap between DPP-4/incretin signalling and GABAergic pathology. The TxGNN model assigns a very high score, but the accompanying rationale explicitly flags this as a likely **statistical false positive** arising from graph structure rather than genuine biological plausibility — the prediction is not corroborated by any clinical trial or publication.

For context, this Evidence Pack also contains nine other candidate indications for vildagliptin. Most (ranks 1–8, including focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and several lipodystrophy subtypes) share this same pattern: high TxGNN scores with no mechanistic rationale and zero supporting evidence. The one exception is **rank 10, Type 1 Diabetes Mellitus**, which has a lower TxGNN score (99.37%) but is supported by L2-level evidence — including a completed Phase 3 trial and a completed Phase 2 trial directly testing vildagliptin in T1DM populations, plus multiple RCT/cohort publications. This candidate is mechanistically plausible (DPP-4 inhibition may support residual β-cell function and glucagon counter-regulation in T1DM) and warrants separate evaluation, though it is outside the scope of the rank-1 prediction covered by this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Vildagliptin has **0 ARTG entries** and is currently **not marketed** in Australia (`total_licenses: 0`, `market_status: 未上市`). No product licence data is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No PI-derived warnings, contraindications, or drug interaction data are currently available in this Evidence Pack for vildagliptin, and the drug does not currently hold Australian market authorisation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Classic Stiff Person Syndrome) has no clinical trial or literature support and no plausible mechanistic link to vildagliptin's known DPP-4/incretin pharmacology; the evidence pack's own rationale flags it as a likely false positive. Combined with vildagliptin's absence from the Australian market (0 ARTG entries), there is no basis to proceed on this indication.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for vildagliptin (currently a data gap)
- TGA Product Information / regulatory dossier, since the drug is not currently marketed in Australia
- If repurposing interest continues, redirect evaluation toward **Type 1 Diabetes Mellitus (rank 10)**, which carries L2 evidence (completed Phase 2/3 trials, multiple RCT/cohort publications) and a defensible mechanistic rationale, rather than the unsupported rank-1 candidate
- Independent expert review of TxGNN's clustering of unsupported "localized lipodystrophy" and rare-disease predictions (ranks 1–8) to assess whether this reflects a systematic false-positive pattern in the model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

