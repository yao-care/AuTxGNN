---
layout: default
title: Pilocarpine
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
---

# Pilocarpine
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

# Pilocarpine: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is a muscarinic receptor agonist with an established role in lowering intraocular pressure and stimulating glandular secretion. The TxGNN model's top-ranked prediction for this drug is **Primary Hereditary Glaucoma**, but this signal is currently unsupported by any dedicated clinical trials or published literature — it appears to be a generalisation from the broader "glaucoma" disease category rather than subtype-specific evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in current records — Pilocarpine is not currently marketed and no TFDA/ARTG licence data is on file |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is not available for Pilocarpine in this evidence pack. However, the dataset's own analysis of related indications confirms Pilocarpine is a **non-selective muscarinic receptor (M1–M3) agonist** — the well-established pharmacological basis for its classic use in lowering intraocular pressure (via ciliary muscle and iris sphincter contraction, which increases trabecular meshwork outflow) and in stimulating salivary and other glandular secretion.

The predicted indication, Primary Hereditary Glaucoma, sits within the same broad disease category (glaucoma) that Pilocarpine's pharmacology already targets. However, this hereditary/congenital subtype typically involves **trabeculodysgenesis** — a developmental defect of the trabecular meshwork itself — and is managed primarily by surgery rather than pharmacotherapy. The evidence pack's own repurposing rationale explicitly flags this as a likely generalisation artefact: TxGNN's high score may reflect broad associations with "glaucoma" as a category rather than subtype-specific pharmacological or clinical evidence. No clinical trials or literature specific to Pilocarpine in primary hereditary glaucoma were found in this search.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Pilocarpine currently has no ARTG entries on file — market status is "Not marketed," and 0 licences were found in the source registry data.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This specific prediction (Primary Hereditary Glaucoma) has no supporting clinical trials or literature, and the mechanistic rationale itself notes it is likely a category-level generalisation rather than subtype-specific evidence — insufficient basis to advance.

**To proceed, the following is needed:**
- TFDA/PI safety warnings and contraindications (currently a blocking data gap for safety screening)
- Confirmed mechanism-of-action documentation for Pilocarpine (currently a high-severity data gap)
- Subtype-specific evidence connecting Pilocarpine's pharmacology to trabeculodysgenesis-related glaucoma, or reclassification of this signal as low priority if no such evidence emerges

**Note for reviewers:** this same evidence pack contains other Pilocarpine indication signals with substantially stronger support — notably *open angle glaucoma* (L1 evidence, multiple completed Phase 3/4 trials, "Proceed with Guardrails") and *oral candidiasis* (L3 evidence, Phase 3 trial plus supporting literature, "Research Question"). Those candidates warrant separate, dedicated review rather than being folded into this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

