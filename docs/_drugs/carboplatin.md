---
layout: default
title: Carboplatin
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 9
monitor_inn: "Carboplatin"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-11-17
description: "Carboplatin: predicted new indication rectum mucinous adenocarcinoma (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Carboplatin
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

## Carboplatin: platinum-based DNA-crosslinking cytotoxic agent → rectum mucinous adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy agent. The TxGNN model predicts it may be effective for **rectum mucinous adenocarcinoma**, but the data compiled for this report contain **no clinical trials and no publications** for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | rectum mucinous adenocarcinoma |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for carboplatin: "Carboplatin is a platinum-based drug that binds to DNA and forms DNA cross-links. These crosslinks inhibit DNA replication and transcription and trigger cytotoxic processes that lead to cell death." ([DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b), label version 2026-11-09; accessed 2026-11-19.) Carboplatin belongs to the platinum class of cytotoxic drugs, which act by forming DNA crosslinks in dividing tumour cells.

The prediction likely reflects a shared mucinous adenocarcinoma phenotype with ovarian mucinous tumours, rather than any direct evidence in rectal cancer. Platinum agents are also reported to have limited efficacy in mucinous colorectal histology, which weakens the mechanistic argument. The score is a computational output only and should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4309T | Carboplatin Accord | Solution for I.V. injection 450 mg in 45 mL | Not recorded in the local data |

Two current PBS items are recorded. Carboplatin is supplied as an injectable (intravenous) solution.

<!-- review:begin au-lic-20261117-carboplatin-1 -->

> **Review correction (2026-11-17)**: Originally stated: "One licence is recorded, and it is valid." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-carboplatin-1 -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | High (thrombocytopenia, neutropenia, leukopenia and anaemia are recognised concerns) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential, liver and renal function; also consider hearing and peripheral neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

No label-based warnings or contraindications are available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

Conditions listed as contraindication-related in the compiled data (these are not label text):
- Kidney disease, liver disease, gallbladder disease
- Thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic anaemia), blood coagulation disease
- Peripheral neuropathy and peripheral nervous system disease
- Hearing and auditory system disorders
- Functional visual loss

**Drug interactions:** 100 interactions were identified. The main ones listed are mostly of moderate severity:
- Proton pump inhibitors: rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole
- Aminoglycosides and glycopeptides: kanamycin, neomycin, streptomycin, vancomycin
- Statins: rosuvastatin, simvastatin
- Nitroimidazoles: metronidazole, tinidazole
- Minor: levofloxacin

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9928), but there are no clinical trials or publications for rectum mucinous adenocarcinoma, so the evidence level is L5. Platinum agents are also reported to have limited efficacy in mucinous colorectal histology.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence of carboplatin activity in rectal mucinous adenocarcinoma
- Mechanism of action data to support the proposed link
- Label-based warnings and contraindications from the TGA-approved Product Information
- A review of current rectal cancer guidelines to judge whether a platinum agent has a role in this histology

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

