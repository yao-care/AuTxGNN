---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Salicylic Acid
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

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is a long-established keratolytic and anti-inflammatory agent, used for skin conditions such as acne, seborrhoeic dermatitis and tinea, and for inflammatory conditions such as rheumatoid arthritis and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for salicylic acid: "Although the exact mode of action for salicylic acid in the treatment of warts is unknown, its activity appears to be associated with its keratolytic action, which results in mechanical removal of epidermal cells infected with wart viruses." ([DailyMed: Xalix (salicylic acid) prescribing information, Cintex Services, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41369b38-7f15-b597-e063-6394a90a614b), label version 2025-10-15; accessed 2026-11-19.) Based on known information, salicylic acid is thought to act through anti-inflammatory pathways (such as COX inhibition and NF-kB modulation), although the pharmacology source compiled for this report notes that public bioactivity data confirming a primary molecular target are lacking. It is already used for allergic and inflammatory conditions such as allergic rhinitis, which gives a loose, plausible link to allergic or inflammatory conjunctival disease.

There are important limits to this reasoning. Topical ocular use of salicylic acid is irritating and potentially unsafe, and no ocular-specific mechanism or data were available. The high TxGNN score reflects a computational prediction, not demonstrated benefit.

Other top-ranked predictions were also reviewed. Most (for example, genetic skeletal dysplasias such as brachyolmia, pseudoachondroplasia and acromesomelic dysplasia) have no plausible mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Two are worth noting:
- **Spondyloarthropathy (susceptibility)** is the most biologically coherent candidate, since NSAIDs are first-line therapy and salicylates are used in related joint conditions. This rationale is class-level only, and other NSAIDs are better established. It is flagged as a research question.
- **Rosacea conjunctivitis** has only a weak indirect rationale, with the same ocular irritation concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Eight current PBS items were identified in the data compiled for this report, including salicylic acid extemporaneous preparations and combination products (Duofilm with lactic acid; Ionil-T and Sebitar with coal tar). Product names and dosage forms are recorded only for the combination products; approved indication text is not available in the data compiled for this report.

<!-- review:begin au-lic-20261117-salicylic_acid-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Two valid single-ingredient ARTG entries were identified. Product names, dosage forms and approved indication text were not available in the data compiled for this report." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-salicylic_acid-1 -->

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 117E | – | Salicylic Acid | – | Valid |
| 4447C | Sebitar | tar + coal tar solution + salicylic acid | Scalp cleanser 20 mg-10 mg-10 mg per mL (2%-1%-1%), 250 mL | Valid |
| 4560B | Ionil-T | coal tar solution + salicylic acid | Scalp cleanser 20 mg-50 mg per mL (2%-5%), 200 mL | Valid |
| 7502W | – | Salicylic Acid and Sulfur Aqueous | – | Valid |
| 7568H | – | Salicylic Acid | – | Valid |
| 7926E | – | Salicylic Acid | – | Valid |
| 7928G | – | Salicylic Acid (extemporaneous formula) | – | Valid |
| 11959K | Duofilm Solution | Salicylic acid + lactic acid | Liquid 167 mg-150 mg per g (16.7%-15%), 15 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Pharmacology note**: The data list ASIC3 (an acid-sensing ion channel) as a pharmacological target of salicylic acid. This is not a drug-drug interaction in the usual clinical sense.
- **Ocular use**: Topical ocular application of salicylic acid is irritating and potentially unsafe, a key concern for the predicted conjunctival indications.

No label-based warnings or contraindications were available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests solely on a model score, with no clinical trials, no literature and a safety concern with ocular application. The evidence level is L5.

**To proceed, the following is needed:**
- Obtain the TGA Product Information for the listed products to confirm approved indications, dosage forms, warnings and contraindications
- Detailed mechanism of action data, including ocular-relevant pharmacology
- Preclinical ocular tolerability and safety data for any conjunctival use
- A systematic literature search for salicylates or NSAIDs in allergic conjunctivitis
- Consideration of spondyloarthropathy as a better-grounded research question, using class-level NSAID evidence

<!-- review:begin au-lic-20261124b-salicylic_acid-1 -->

> **Review correction (2026-11-24)**: Originally stated: "for both ARTG entries" Corrected: the data compiled for this report list more PBS items for this ingredient than the two entries assumed here; see the PBS item table in the Australia Market Information section. PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261124b-salicylic_acid-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xalix (salicylic acid) prescribing information, Cintex Services, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41369b38-7f15-b597-e063-6394a90a614b) |
| 2026-11-24 | Corrected: removed the assumption that there are only two entries | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

