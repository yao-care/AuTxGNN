---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-17
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Naproxen
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

## Naproxen: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) used for arthritis, gout, tendon and joint inflammation, migraine and other pain conditions.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (14 of 15 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 15 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, naproxen inhibits cyclooxygenase (COX-1 and COX-2), which reduces prostaglandin-mediated inflammation and pain.

**No plausible mechanistic link was identified** between this action and brachydactyly-syndactyly syndrome. The syndrome is a rare congenital disorder of limb development, not an inflammatory condition, so COX inhibition would not address its cause. The high TxGNN score (0.9935) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| ARTG 14854T | Pediapharm Naproxen Suspension 25 mg/mL (Medexus Pharma, Canada) | Oral suspension 125 mg per 5 mL, 474 mL (S19A) |

Fourteen current oral PBS items are recorded (tablets, sustained-release tablets and oral suspensions); the Section 19A oral suspension (imported supply) in this data is no longer listed. Approved indication text was not available in the data compiled for this report, so please refer to the Product Information.

<!-- review:begin au-lic-20261117-naproxen-1 -->

> **Review correction (2026-11-17)**: Originally stated: "This is a single oral product supplied under Section 19A (imported supply)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-naproxen-1 -->

## Safety Considerations

- **Contraindications and warnings (associations learned by the TxGNN model, not label text):** The TxGNN model (deep learning) associates naproxen with a wide range of conditions, which may reflect similarities the model learned between related diseases, not biological evidence, including:
  - Cardiovascular: hypertension, congestive heart failure, coronary artery disease, myocardial infarction and stroke or cerebrovascular disorders.
  - Kidney and liver: kidney disease and liver disease or failure.
  - Other: blood coagulation disorders, anaemia, diabetes mellitus, epilepsy, osteoporosis and gallbladder disease.

  These are not confirmed label contraindications and should be verified against the Product Information.
- **Drug Interactions:** 100 interactions were recorded. The ones listed in the data are all rated Moderate and include:
  - Acid suppressants: famotidine, ranitidine, cimetidine, rabeprazole and dexlansoprazole.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide and triamcinolone.
  - Anti-diabetic agents: metformin and chlorpropamide.
  - Salicylates and related agents: acetylsalicylic acid, mesalazine and balsalazide.
  - Others: aprepitant, potassium citrate and potassium bicarbonate.

Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials, no literature and no plausible mechanism for a congenital limb malformation. Naproxen's known safety risks (cardiovascular, gastrointestinal, renal) are not justified by any expected benefit.

**To proceed, the following is needed:**
- A biological rationale linking COX inhibition or prostaglandin signalling to the pathology of brachydactyly-syndactyly syndrome
- Preclinical or case-based evidence supporting any benefit
- Mechanism of action data and the Australian Product Information (indications, warnings and contraindications)

**Other predictions in the data:** Two lower-ranked predictions have more supporting evidence, but both are largely existing uses of naproxen rather than true repurposing. They are better assessed separately.
- **Inflammatory spondylopathy** (axial spondyloarthritis): L1 with Proceed with Guardrails, supported by completed Phase 3 trials.
- **Polyarticular juvenile rheumatoid arthritis**: L3 with Proceed with Guardrails, supported by older comparative studies and one randomised trial using naproxen as the comparator.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

