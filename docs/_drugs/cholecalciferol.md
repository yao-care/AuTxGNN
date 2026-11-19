---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 4
monitor_inn: "cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-11-20
description: "Cholecalciferol: predicted new indication Acromesomelic dysplasia, Campailla Martinelli type (evidence level L5). Approved use: Osteoporosis, vitamin D deficiency, osteomalacia…"
---

# Cholecalciferol
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

## Cholecalciferol: From Vitamin D-Related Bone and Mineral Disorders to Acromesomelic Dysplasia, Campailla Martinelli Type
{: .text-alpha }

## One-Sentence Summary

The TxGNN model (deep learning) predicts that cholecalciferol (vitamin D3) may be effective for **acromesomelic dysplasia, Campailla Martinelli type**, a rare genetic skeletal dysplasia. This score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence. There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, vitamin D deficiency, osteomalacia, rickets and related conditions (relations recorded in the knowledge graph; no approved indication text is available in the data compiled for this report) |
| Predicted New Indication | Acromesomelic dysplasia, Campailla Martinelli type |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of cholecalciferol as: Vitamin D receptor agonist ([ChEMBL CHEMBL1042 (cholecalciferol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1042), CC BY-SA 3.0; accessed 2026-11-19.) Cholecalciferol is a vitamin D3 precursor that is converted in the body to active vitamin D, which supports calcium and phosphate handling and bone mineralisation. The TxGNN model (deep learning) score may reflect similarities the model learned between related diseases, not biological evidence.

Acromesomelic dysplasia is a rare inherited skeletal disorder. It is generally thought to involve bone growth signalling pathways rather than vitamin D or mineral deficiency. The data compiled for this report establish no plausible direct mechanistic link between cholecalciferol and this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13835E | Fosamax Plus 70 mg/140 mcg | Oral tablet, 70 mg (as alendronate sodium) with 140 micrograms colecalciferol | Not provided in the data compiled for this report |

All six current PBS items found are combination products (alendronate plus colecalciferol, Fosamax Plus tablets). It therefore does not show how cholecalciferol on its own is approved or marketed in Australia.

<!-- review:begin au-lic-20261117-cholecalciferol-1 -->

> **Review correction (2026-11-17)**: Originally stated: "This is the only ARTG entry found, and it is a combination product (alendronate plus colecalciferol)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-cholecalciferol-1 -->

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): hypertension, kidney disease, liver disease, gallbladder disease, gastritis, sarcoidosis, diabetes mellitus, diabetic ketoacidosis, atrial fibrillation, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, blood coagulation disease, sickle cell anaemia, primary hyperoxaluria, hereditary haemochromatosis, Wilson disease, hyperlipidaemia, breast carcinoma and prostate cancer, among others.
- **Drug interactions:** 56 interactions were identified. Of the 20 listed in the data compiled for this report, the following are rated **Major**: calcifediol, calcitriol, dihydrotachysterol and doxercalciferol. These are other vitamin D agents, so combining them risks additive vitamin D effects. Many others are rated Moderate, including thiazide diuretics, barbiturates, carbamazepine, digoxin and digitoxin, and bile acid sequestrants (cholestyramine, colestipol, colesevelam).

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score. No clinical trials or publications address this disease, and no plausible mechanism has been established. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Mechanistic evidence linking vitamin D biology to the pathway underlying this skeletal dysplasia
- Any preclinical, case-based or clinical data in this specific condition
- Detailed mechanism of action data and TGA PI warnings and contraindications for cholecalciferol
- Confirmation of how cholecalciferol is licensed as a single ingredient in Australia, as the only entry found is a combination product

For context, other TxGNN predictions for this drug, such as renal osteodystrophy, have more supporting evidence and may be better candidates for further review.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1042 (cholecalciferol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1042) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

