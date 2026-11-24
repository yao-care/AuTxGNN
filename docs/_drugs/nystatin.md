---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: predicted new indication Disease of orbital region (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Nystatin
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

## Nystatin: Disease of orbital region
{: .text-alpha }

## One-Sentence Summary

Nystatin is a polyene antifungal that is marketed in Australia as an oral suspension, tablets and capsules, and as a vaginal cream. The TxGNN model predicts it may be effective for **disease of orbital region**. However, there are **0 directly relevant clinical trials** and **0 publications** on this condition, so the prediction is not backed by any study evidence.

<!-- review:begin au-lic-20261124b-nystatin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "marketed in Australia as an oral suspension." Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261124b-nystatin-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Disease of orbital region |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for nystatin: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), label version 2026-02-06; accessed 2026-11-19.) As a polyene antifungal, nystatin is generally understood to bind ergosterol in fungal cell membranes and disrupt them. This mechanism is relevant to fungal infections.

No plausible mechanistic link between nystatin and disease of orbital region was identified. The condition is a broad category of eye-socket disorders, and the supplied data give no sign that an antifungal acts on it. The only trial linked to this prediction studies a different drug in a retinal disease. The very high score is therefore most likely a modelling artefact and should not be read as clinical support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | Recruiting | 42 | Safety and tolerability of ASP7317 in geographic atrophy secondary to age-related macular degeneration. It does not involve nystatin and does not address an orbital disease. |

This trial is not evidence for nystatin in the predicted condition.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1696G | Nilstat | Nystatin | Tablet 500,000 units | Valid |
| 1699K | Nilstat | Nystatin | Capsule 500,000 units | Valid |
| 2971J | Otocomb Otic | triamcinolone + neomycin + gramicidin + nystatin | Ear drops containing triamcinolone acetonide 0.9 mg with neomycin 2.25 mg (as sulfate), gramicidin 225 micrograms and n… | Valid |
| 2974M | Otocomb Otic | triamcinolone + neomycin + gramicidin + nystatin | Ear ointment containing triamcinolone acetonide 1 mg with neomycin 2.5 mg (as sulfate), gramicidin 250 micrograms and n… | Valid |
| 3342X | Nilstat | Nystatin | Tablet 500,000 units | Valid |
| 3345C | Nilstat | Nystatin | Capsule 500,000 units | Valid |
| 4013F | Nilstat | Nystatin | Vaginal cream 100,000 units per dose, 15 doses, 75 g | Valid |
| 10854G | Pharmacy Action Nystatin Oral Drops | Nystatin | Oral suspension 100,000 units per mL, 24 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

This is a single-ingredient product, and the licence is currently valid.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interacting drugs, with severity not classified in the source. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, bortezomib, tramadol, lorazepam and sildenafil. Each should be checked against the TGA-approved Product Information (PI) before any use.

No key warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trial or publication for this disease, and the only linked trial concerns a different drug and a retinal condition. No mechanistic rationale is apparent, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or preclinical studies that directly examine nystatin in orbital region disease
- A clearer clinical definition of which orbital conditions are of interest, and whether an antifungal mechanism could plausibly apply
- Detailed mechanism of action data
- Safety information from the TGA-approved PI, including warnings, contraindications and prioritised interaction severity

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |
| 2026-11-24 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

