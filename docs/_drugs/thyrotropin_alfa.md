---
layout: default
title: Thyrotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 672
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Thyrotropin Alfa: From Unspecified Indication to Migraine Disorder

## One-Sentence Summary

Thyrotropin alfa (recombinant human TSH, DrugBank ID DB00024) has no original indication or mechanism-of-action data recorded in this evidence pack. The TxGNN model predicts a possible link to **Migraine Disorder**, with a very high statistical score (99.98%), but this is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic analysis finds no biological rationale connecting TSH receptor activation to migraine pathophysiology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — no approved indication text on file, and the drug is not marketed in Australia |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for thyrotropin alfa is not available as a structured field in this evidence pack (data gap DG002). However, the model's own rationale text describes thyrotropin alfa as a **TSH receptor agonist** that stimulates thyroid follicular cells to increase hormone synthesis and iodine uptake. No original indication is documented, so a direct comparison between "original use" and "predicted use" cannot be made from the supplied data.

Critically, the evidence pack's own repurposing rationale for migraine disorder states there is **no known mechanistic connection** between TSH receptor agonism and migraine pathophysiology (the trigeminovascular system and CGRP pathway). The same applies to the second-ranked prediction, migraine with brainstem aura. This means the top prediction is driven purely by the TxGNN embedding score, without any supporting biological hypothesis, clinical trial, or literature evidence.

It is also worth noting that among the ten predictions in this pack, the only one with actual clinical trial history is **hyperthyroidism** (rank 10) — but the rationale there flags a **mechanistic contradiction**: thyrotropin alfa is an exogenous TSH agonist that would be expected to *induce or worsen* hyperthyroidism rather than treat it, and the two related Phase 2 trials were actually for pre-treatment in benign nodular goitre prior to radioiodine therapy, not for treating hyperthyroidism itself. This pattern across the bundle indicates low overall biological plausibility for this candidate drug's top-ranked predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Migraine Disorder.

*Note: limited clinical trial evidence exists elsewhere in this evidence pack (2 completed Phase 2 studies) but relates to a lower-ranked, mechanistically contradictory candidate (hyperthyroidism/goitre pre-treatment, rank 10) — not to the top-ranked migraine prediction.*

---

## Literature Evidence

Currently no related literature available for Migraine Disorder.

---

## Australia Market Information

Thyrotropin alfa currently has **0 ARTG entries** and is **not marketed in Australia**. No product listing, dosage form, or approved indication text is available for extraction from this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: A DrugBank interaction search returned no results (`query_status: not_found`); this does not confirm the absence of clinically significant interactions, only that none were found in the queried source.
- Key warnings and contraindications are not available in the current evidence pack. This is flagged in the pack as a **blocking data gap (DG001)** for TGA/overseas Product Information — safety review cannot proceed to initial screening (S1) until this is resolved.
- As the product is not currently registered in Australia, there is no TGA-approved PI to reference locally; any safety assessment would need to draw on the overseas-approved Product Information (e.g. for the reference product Thyrogen) before further development.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (migraine disorder) is an L5, model-only prediction with no clinical trial or literature support, and the evidence pack's own mechanistic analysis finds no plausible biological link. Combined with a blocking data gap on TFDA/TGA warnings and contraindications (DG001), missing mechanism-of-action data (DG002), and the drug's absence from the Australian market, there is no basis to advance this candidate at this time. Across the full set of ten TxGNN predictions supplied, every candidate is scored "Hold," including the only one with actual trial history (hyperthyroidism), which carries a pharmacological contradiction rather than a therapeutic rationale.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action documentation for thyrotropin alfa (resolve DG002)
- TFDA/TGA-equivalent Product Information (warnings, contraindications, DDI) to enable an initial safety screen (resolve DG001, currently blocking)
- If any indication in this bundle is to be progressed, prioritise candidates with actual trial or literature support and independently re-verify mechanistic plausibility rather than relying on the TxGNN score alone
- Confirmation of Australian regulatory pathway/market status before any further evaluation, given the drug is currently unregistered here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

