---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 7
monitor_inn: "Azathioprine"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
last_modified_at: 2026-11-24
description: "Azathioprine: predicted new indication colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Azathioprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Azathioprine: purine antimetabolite immunosuppressant → colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## One-Sentence Summary

Azathioprine is an oral immunosuppressant (a purine antimetabolite) that is marketed in Australia. The TxGNN model predicts it may be relevant to **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, an ultra-rare developmental malformation syndrome. **No clinical trials and no publications** in the data compiled for this report support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 (rounded to 4 decimals) |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of azathioprine as: Amidophosphoribosyltransferase inhibitor; DNA inhibitor ([ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542), CC BY-SA 3.0; accessed 2026-11-19.) Azathioprine is generally understood as a purine antimetabolite that suppresses lymphocyte proliferation and so dampens immune-mediated disease.

The predicted condition is a congenital developmental syndrome affecting the eye and skeleton. No immune-mediated or inflammatory driver is recognised that azathioprine's action would plausibly target, so no mechanistic link can be established. The high TxGNN score reflects a network-based computational prediction only. It is not evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2687K | APO-Azathioprine | Azathioprine | Tablet 50 mg | Valid |
| 2688L | APO-Azathioprine | Azathioprine | Tablet 25 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

Azathioprine is currently marketed in Australia. The data compiled for this report record two valid single-ingredient products, oral 50 mg and 25 mg tablets.

<!-- review:begin au-lic-20261117-azathioprine-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The data compiled for this report record one valid single-ingredient product, an oral 50 mg tablet." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-azathioprine-1 -->

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 recorded interactions. The main entries listed in the compiled data are:
  - **Moderate:** mesalazine, balsalazide, olsalazine and sulfasalazine.
  - **Minor:** zinc acetate, zinc gluconate and zinc sulfate.
  - **Level not classified:** several other agents, including aspirin, omeprazole, pantoprazole, metformin, doxycycline, amphotericin B and morphine.

Warnings and contraindications were not captured in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information. Azathioprine is myelosuppressive and increases infection risk, so any use in a new, unstudied population needs careful consideration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no supporting trials or publications, and no plausible immune-mediated mechanism links azathioprine to this developmental syndrome.

**To proceed, the following is needed:**
- Published or registered studies that directly address colobomatous microphthalmia-rhizomelic dysplasia syndrome
- A mechanistic rationale, supported by detailed mechanism-of-action data for azathioprine
- Safety information from the TGA-approved PI, including warnings and contraindications, and a risk assessment for the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism-of-action data for azathioprine are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

