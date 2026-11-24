---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fluconazole is an azole antifungal originally used to treat candidiasis (oral, oesophageal, vulvovaginal and invasive forms) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are currently **no clinical trials** and **no publications** supporting this prediction. It rests on a model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis, candidaemia, disseminated candidiasis, cryptococcal meningitis (the approved indication text for the Australian listing was not available) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fluconazole: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), label version 2026-04-02; accessed 2026-11-19.) Based on known information, fluconazole is a triazole antifungal. Its efficacy in candidiasis and cryptococcal infection is established, and it is generally understood to act by inhibiting fungal ergosterol synthesis.

Punctate epithelial keratoconjunctivitis is most often viral (commonly adenoviral) or inflammatory. A fungal cause would be needed for an antifungal mechanism to be relevant. The high TxGNN score (0.9924) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No supporting clinical or literature evidence was found. The link between fluconazole and this condition is therefore currently weak and unconfirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1471K | Diflucan | Fluconazole | Capsule 50 mg | Valid |
| 1472L | Diflucan | Fluconazole | Capsule 100 mg | Valid |
| 1475P | Diflucan | Fluconazole | Capsule 200 mg | Valid |
| 5446P | Diflucan | Fluconazole | Powder for oral suspension 50 mg in 5 mL, 35 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The listed dosage forms are oral capsules (50 mg, 100 mg and 200 mg) and a powder for oral suspension. Whether an ophthalmic or topical route would be needed for the predicted indication has not been assessed.

<!-- review:begin au-lic-20261117-fluconazole-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Oral capsule is the only dosage form listed." Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-fluconazole-1 -->

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, kidney disease, liver disease, gallbladder disease and pyoureter. These should be verified against the TGA-approved Product Information.
- **Drug Interactions:** The interaction screen returned 100 potential interactions; 20 are shown in the data compiled for this report.
  - **Major:** chlorpropamide.
  - **Moderate:** proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole), famotidine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aprepitant, loperamide, saxagliptin, and several laxatives and bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol).
  - **Minor:** amphotericin B and clarithromycin.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, and no plausible mechanism links an antifungal to what is usually a viral or inflammatory eye condition.

**To proceed, the following is needed:**
- Evidence of a fungal or otherwise azole-responsive aetiology in punctate epithelial keratoconjunctivitis
- Preclinical or clinical studies of fluconazole in this condition
- Detailed mechanism of action data
- Assessment of route and formulation suitability, since only oral forms (capsules and a powder for oral suspension) are listed in Australia
- Safety information from the TGA-approved Product Information, including the knowledge-graph flags for QT prolongation and kidney and liver disease

<!-- review:begin au-lic-20261124b-fluconazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "since only an oral capsule is listed in Australia" Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261124b-fluconazole-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |
| 2026-11-24 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

