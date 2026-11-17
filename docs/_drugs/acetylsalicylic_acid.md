---
layout: default
title: Acetylsalicylic Acid
parent: Model Prediction Only (L5)
nav_order: 21
evidence_level: L5
indication_count: 7
monitor_inn: "Acetylsalicylic acid"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-03
description: "Acetylsalicylic Acid: predicted new indication atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Acetylsalicylic Acid
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

## Acetylsalicylic acid: antiplatelet COX inhibitor → atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a widely used antiplatelet and anti-inflammatory drug that inhibits cyclooxygenase.
The TxGNN model predicts it may be effective for **atrophoderma vermiculata**, a rare follicular atrophic skin disorder,
but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (9 of 9 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Aspirin is generally known to irreversibly inhibit COX-1 and COX-2, which reduces prostaglandin and thromboxane A2 production, giving it antiplatelet and anti-inflammatory effects.

Atrophoderma vermiculata is a rare condition in which follicular atrophy produces a honeycomb-like pattern on the cheeks. No plausible mechanistic link has been identified between aspirin's COX inhibition or antiplatelet activity and the pathology of this disorder. The high TxGNN score appears to be a model-based prediction artefact rather than a finding supported by clinical or laboratory evidence, and it should be treated with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 104L | Not recorded | Not recorded | Not recorded |

The data compiled for this report contain nine current PBS items: six single-ingredient aspirin items (mostly 100 mg oral tablets or capsules) and three combinations (clopidogrel with aspirin, aspirin with codeine). Indication text is not recorded in the local data.

<!-- review:begin au-lic-20261117-acetylsalicylic_acid-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The data compiled for this report contain one single-ingredient licence, which is valid. Product name, dosage form and indication text are not recorded in the local data." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-acetylsalicylic_acid-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries; the first 20 are available for this report. Major-level interactions among them include:
  - Acalabrutinib
  - Acetazolamide
  - Ketorolac
  - Trastuzumab emtansine
  - Ibuprofen
  - Fondaparinux

  Moderate-level interactions include abciximab, nifedipine, hydrocortisone, ethanol, alendronic acid, fluvoxamine, fosinopril and gemifloxacin. Minor-level interactions include acebutolol, caffeine, rabeprazole, fosphenytoin and furosemide. Many of these relate to additive bleeding risk or gastrointestinal toxicity. Please also refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications for atrophoderma vermiculata and no plausible mechanistic link, so the evidence level is L5.

**To proceed, the following is needed:**
- Any disease-specific clinical, case-series or laboratory evidence for aspirin in atrophoderma vermiculata
- A plausible pathophysiological rationale linking COX inhibition or antiplatelet activity to follicular atrophy
- Detailed mechanism of action data
- Label-based warnings and contraindications from the TGA Product Information, and the full interaction list

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

