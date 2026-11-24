---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 4
monitor_inn: "Cabergoline"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
last_modified_at: 2026-11-24
description: "Cabergoline: predicted new indication progeria-short stature-pigmented nevi syndrome (evidence level L5). In Australia: 7 PBS items (7 currently listed)"
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cabergoline: dopamine D2 receptor agonist → progeria-short stature-pigmented nevi syndrome
{: .text-alpha }

## One-Sentence Summary

Cabergoline is a dopamine receptor agonist that is marketed in Australia as Dostinex tablets. The TxGNN model predicts it may be relevant to **progeria-short stature-pigmented nevi syndrome**, but this is a computational prediction only. **No clinical trials** and **no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | progeria-short stature-pigmented nevi syndrome |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (7 of 7 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cabergoline: "Cabergoline is an ergot derivative and dopamine receptor agonist with a high affinity for D2 receptors. Results of in vitro studies demonstrate that cabergoline exerts a direct inhibitory effect on the secretion of prolactin by rat pituitary lactotrophs." ([DailyMed: cabergoline prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e497366b-a124-4d7f-bd45-a883c392d4bb), label version 2026-06-30; accessed 2026-11-19.) Cabergoline is generally understood to act as a dopamine D2 receptor agonist.

No plausible dopaminergic mechanism is evident for this rare syndrome. The high TxGNN score reflects a computational pattern only. It has not been supported by any mechanistic study, clinical trial or publication, so the prediction should be treated as a hypothesis for exploration, not as a reasoned repurposing case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 8114C | Dostinex | Cabergoline | Tablet 500 micrograms | Valid |
| 8115D | Dostinex | Cabergoline | Tablet 500 micrograms | Valid |
| 8393R | Cabaser | Cabergoline | Tablet 1 mg | Valid |
| 8394T | Cabaser | Cabergoline | Tablet 2 mg | Valid |
| 13901P | Dostinex | Cabergoline | Tablet 500 micrograms | Valid |
| 14516B | Cabaser | Cabergoline | Tablet 1 mg | Valid |
| 14543K | Cabaser | Cabergoline | Tablet 2 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

Seven current single-ingredient PBS items are on record.

<!-- review:begin au-lic-20261117-cabergoline-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The one licence on record is a valid single-ingredient product." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-cabergoline-1 -->

## Safety Considerations

- **Drug Interactions**: 60 interactions were identified in the data compiled for this report. The main ones are:
  - **Major**: lorcaserin and clarithromycin.
  - **Moderate**: metoclopramide.
  - Many other interactions are of unknown severity (for example, proton pump inhibitors, corticosteroids, metformin and simvastatin).

No label-based warnings or contraindications are available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no trials, no literature and no plausible mechanistic link to support progeria-short stature-pigmented nevi syndrome.

**To proceed, the following is needed:**
- A documented biological rationale linking dopamine D2 signalling to this syndrome
- Any preclinical or clinical studies that directly address this condition
- Mechanism of action data for cabergoline and its safety information from the TGA Product Information
- An assessment of the risk-benefit balance in this rare patient population, given the interaction profile and the lack of any efficacy data

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: cabergoline prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e497366b-a124-4d7f-bd45-a883c392d4bb) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

