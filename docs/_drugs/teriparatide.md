---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 711
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Teriparatide: predicted new indication duodenal ulcer (disease) (evidence level L5). Approved use: Postmenopausal osteoporosis"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Teriparatide: From Osteoporosis to duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) used to treat osteoporosis, including postmenopausal osteoporosis.
The TxGNN model ranks **duodenal ulcer** as its top predicted new indication, but **no clinical trials and no publications** support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis; osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for teriparatide: "Endogenous 84-amino acid parathyroid hormone (PTH) is the primary regulator of calcium and phosphate metabolism in bone and kidney. Physiological actions of PTH include regulation of bone metabolism, renal tubular reabsorption of calcium and phosphate, and intestinal calcium absorption. […] The biological actions of PTH and teriparatide are mediated through binding to specific high-affinity cell-surface receptors." ([DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c), label version 2026-08-31; accessed 2026-11-20.) Pharmacology records show that teriparatide acts on the PTH1 receptor (PTH1R) and also binds the PTH2 receptor (PTH2R). Its established clinical role is as a bone-building (anabolic) agent for patients at high risk of fracture.

No plausible link between this bone-anabolic signalling and duodenal ulcer healing was found in the supplied data. The prediction (score 0.9986) comes from the TxGNN model (deep learning) alone. A high score may reflect similarities the model learned between related diseases, not biological evidence, and does not show demonstrated biology or clinical benefit. Without supporting studies, this prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 14093R | Terrosa | Teriparatide | Injection 250 micrograms per mL, 2.4 mL in multi-dose pre-filled pen | Valid |
| 14482F | Terrosa | Teriparatide | Injection 250 micrograms per mL, 2.4 mL in multi-dose pre-filled pen | Valid |
| 15152L | Ritosa | Teriparatide | Injection 250 micrograms per mL, 2.4 mL in multi-dose pre-filled cartridge | Valid |
| 15188J | Ritosa | Teriparatide | Injection 250 micrograms per mL, 2.4 mL in multi-dose pre-filled cartridge | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

Product Information (PI) warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for label safety information.

- **Disease-level contraindication signals (knowledge graph, not label text):** hypercalcaemia, hyperparathyroidism, bone osteosarcoma, bone Paget disease (including juvenile), osteomalacia, rickets, renal osteodystrophy, osteitis fibrosa, nephrocalcinosis, urolithiasis, phosphorus metabolism disease and hypotensive disorder. Verify each against the PI.
- **Drug interactions (8 records):**
  - Moderate: calcitriol (topical), calcipotriol (topical), digoxin and digitoxin.
  - Minor: hydrochlorothiazide and furosemide.
  - Two further records are receptor-target entries (PTH1R and PTH2R), not drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no literature and no plausible mechanism for duodenal ulcer. Evidence is insufficient to justify further investment in this indication.

**To proceed, the following is needed:**
- A mechanistic rationale linking PTH receptor signalling to duodenal mucosal healing, followed by preclinical data
- Any clinical or observational evidence of teriparatide in peptic or duodenal disease
- Retrieval and review of the TGA-approved PI for warnings and contraindications
- Review of the lower-ranked prediction **pregnancy-associated osteoporosis** (rank 8). It has L3 evidence from 20 publications, mostly reviews and observational studies, and a "Proceed with Guardrails" assessment. Study designs there were inferred from titles and need verification against the full texts. Use would need to be after lactation has ceased and pregnancy excluded.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "The data compiled for this report do not include a curated mechanism-of-action statement" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

