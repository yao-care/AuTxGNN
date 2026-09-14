---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From Unspecified Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor referenced throughout this evidence pack, but the specific original indication and detailed mechanism of action were not captured in the source data. The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital genetic disorder, with **0 clinical trials** and **0 publications** supporting this specific association — the prediction score alone is very high, but there is no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no ARTG license or original indication data recorded) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tadalafil was not available in this evidence pack (flagged as a High-severity data gap). Based on the rationale fields captured across the predicted indications, Tadalafil is characterised as a **PDE5 (phosphodiesterase type 5) inhibitor**, acting via cGMP accumulation to produce vascular smooth muscle relaxation.

For the top-ranked candidate, Ambras type hypertrichosis universalis congenita, the evidence pack itself states the theoretical link explicitly: PDE5-mediated vasodilation shares a distant conceptual connection with vasodilator-class agents (e.g. minoxidil) that are known to promote hair growth. However, Ambras syndrome is a rare **congenital, genetically determined** disorder (not an acquired, pharmacologically modifiable condition), and the evidence pack confirms there is no clinical or mechanistic evidence beyond the raw model score.

**Important caveat:** because this is a structural/genetic condition rather than an acquired disease process, the biological plausibility of pharmacological reversal is low regardless of mechanism. The high TxGNN score most likely reflects knowledge-graph embedding similarity (e.g. proximity to other hair-growth-related nodes) rather than a genuine, actionable therapeutic signal. This should be treated as a low-priority, exploratory signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries are currently recorded for Tadalafil in this evidence pack (0 licenses; market status: not marketed).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: TFDA warning/contraindication data for this drug could not be retrieved and is flagged as a **Blocking** data gap, meaning a formal safety pre-assessment (S1 stage) cannot proceed until this is resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and targets a congenital genetic disorder that is mechanistically unlikely to respond to pharmacological intervention. Combined with a Blocking safety data gap and the drug's unmarketed status in Australia, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism of action data for Tadalafil (DG002)
- Independent mechanistic or preclinical evidence specific to Ambras type hypertrichosis universalis congenita before any further evaluation
- Consideration of whether lower-ranked candidates with at least some literature signal (e.g. rank 3 and rank 9, though currently non-supportive or contradictory in direction) merit review instead, given the top candidate's biological implausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

