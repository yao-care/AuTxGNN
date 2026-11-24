---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 688
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). In Australia: 4 PBS items (4 currently listed)"
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Spironolactone: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone is an oral aldosterone (mineralocorticoid receptor) antagonist, originally used for hypertension, congestive heart failure and primary aldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for spironolactone: "Spironolactone and its active metabolites are specific pharmacologic antagonists of aldosterone, acting primarily through competitive binding of receptors at the aldosterone-dependent sodium-potassium exchange site in the distal convoluted renal tubule. Spironolactone causes increased amounts of sodium and water to be excreted, while potassium is retained." ([DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc), label version 2025-11-28; accessed 2026-11-19.) Spironolactone is known to block aldosterone receptors, which explains its use in hypertension, heart failure and primary aldosteronism. It also has anti-androgenic activity, through androgen receptor antagonism and reduced androgen synthesis. This is the basis for its use in androgen-driven hair loss.

The link to this prediction is weak. Hypotrichosis simplex is a rare inherited hair disorder, associated with variants in genes such as *CDSN*, *APCDD1* and *RPL21*. It is not driven by androgens. The high TxGNN score therefore appears to reflect network proximity to other hair disorders rather than a plausible pharmacological mechanism. The connection with the drug's original cardiovascular and renal indications is also indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2339D | Spiractin 25 | Spironolactone | Tablet 25 mg | Valid |
| 2340E | Spiractin 100 | Spironolactone | Tablet 100 mg | Valid |
| 13503Q | Spiractin 25 | Spironolactone | Tablet 25 mg | Valid |
| 14042C | Spiractin 100 | Spironolactone | Tablet 100 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

All four current PBS items are single-ingredient products. No manufacturer is recorded.

<!-- review:begin au-lic-20261117-spironolactone-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The single entry is a valid single-ingredient product." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-spironolactone-1 -->

---

## Safety Considerations

The data compiled for this report contains no label-based warnings or contraindications. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindication signals (knowledge graph, not label text)**:
  - Renal: kidney disease, anuria, pyoureter, nephrocalcinosis.
  - Electrolyte and mineral: potassium deficiency disease, hypercalcaemia, phosphorus metabolism disease.
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, osteitis fibrosa, gout, hyperuricaemia.
  - Hepatic: hepatic coma, hepatic encephalopathy, neonatal jaundice.
  - Other: pancreatitis, systemic lupus erythematosus, including the paediatric form.
- **Drug interactions**: The interaction screen returned 100 interactions in total. Loperamide is rated **Major**. Examples rated Moderate include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone).
  - Metformin.
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin).
  - Exenatide, bupropion, morphine and bisacodyl.

  Examples rated Minor include doxycycline, aspirin and fidaxomicin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). No trials or publications exist for hypotrichosis simplex, and the proposed mechanism does not fit a genetic, non-androgen-driven condition.

**To proceed, the following is needed:**
- Any mechanistic or genetic rationale linking mineralocorticoid or androgen receptor blockade to hypotrichosis simplex, or preclinical data supporting one.
- Detailed mechanism of action data.
- Safety information from the TGA Product Information, including warnings and contraindications.

- It is supported by a completed Phase 2 trial comparing spironolactone with topical minoxidil (NCT00175617, n=40), plus several systematic reviews, including one on oral and topical spironolactone.
- Suggested guardrails:
  - Monitor potassium and blood pressure.
  - Ensure contraception, given teratogenicity and feminisation risks.
  - Avoid use in men.
- Phase 3 randomised evidence is still lacking.

This is worth evaluating as a separate candidate.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

