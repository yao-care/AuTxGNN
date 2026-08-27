---
layout: default
title: Phenoxybenzamine
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Phenoxybenzamine
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

# Phenoxybenzamine: From Phaeochromocytoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Phenoxybenzamine is a long-established, non-selective α1/α2-adrenergic antagonist, historically used for phaeochromocytoma and related catecholamine-excess states (general pharmacological knowledge — this drug is not currently marketed in Australia, so no local regulatory indication text is available). The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, but this direction is currently supported by **no clinical trials and no literature**, and the proposed mechanism runs counter to established glaucoma pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Australian regulatory data (drug not marketed in Australia); historically used for phaeochromocytoma / hypertensive crises (general pharmacological reference, not sourced from this evidence pack) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this drug is not available in the structured dataset (`original_moa` is a data gap). Drawing on the repurposing rationale supplied alongside this prediction: Phenoxybenzamine is an irreversible, non-selective α1/α2-adrenergic receptor antagonist.

Intraocular pressure control in glaucoma is typically achieved through α2-agonists (e.g. brimonidine), which *reduce* aqueous humour production, or through β-blockers and prostaglandin analogues. Phenoxybenzamine's pharmacology — α-receptor *blockade* — points in the opposite direction to these established mechanisms. The evidence pack's own rationale flags this as a weak mechanistic link, and no clinical or literature evidence currently exists to support the connection. This prediction appears to be driven primarily by the TxGNN model's network-based score rather than by any known or plausible pharmacological pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Phenoxybenzamine has no active ARTG entries — it is not currently marketed in Australia (0 licences on record).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that this evidence pack flags two related data gaps: TFDA/local product-information warnings and contraindications (blocking severity), and detailed mechanism-of-action data (high severity) — both would need to be sourced before any safety assessment could proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by the TxGNN model score (L5, no trials, no literature), and the proposed mechanism (α-adrenergic blockade) is pharmacologically inconsistent with established glaucoma treatment approaches. There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Phenoxybenzamine (currently a data gap)
- TFDA/TGA product information warnings and contraindications (currently a blocking data gap)
- Preclinical or mechanistic evidence specifically linking α-adrenergic antagonism to intraocular pressure reduction, given the current rationale points the opposite direction
- Note: within this same evidence pack, the rank-3 candidate ("respiratory failure", TxGNN score 98.80%, evidence level L4) has 18 literature results with a more plausible mechanistic rationale (catecholamine excess states) and may warrant separate evaluation ahead of this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

