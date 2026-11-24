---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
description: "Docusate: predicted new indication Plummer-Vinson syndrome (evidence level L5). In Australia: 3 PBS items (3 currently listed)"
---

# Docusate
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

## Docusate: Plummer-Vinson syndrome
{: .text-alpha }

## One-Sentence Summary

Docusate is a surfactant stool softener used for constipation. Any scores on this page come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of docusate as: Surfactant laxative ([ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036), CC BY-SA 3.0; accessed 2026-11-19.) Docusate is an anionic surfactant stool softener, and its efficacy in constipation is established. There is no known mechanism linking it to Plummer-Vinson syndrome.

Plummer-Vinson syndrome is characterised by iron deficiency anaemia together with oesophageal webs. The high score (0.9918) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Docusate has no known effect on iron absorption or on oesophageal webs, so the link has no pharmacological rationale.

Other top-ranked predictions show the same pattern. They include B12- and folate-independent megaloblastic anaemia (0.9915), which sits close to the anaemia indications. None has any trial or publication support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4199B | Waxsol | Docusate | Ear drops 5 mg per mL (0.5%), 10 mL | Valid |
| 4200C | Coloxyl 50 | Docusate | Tablet 50 mg | Valid |
| 10177P | Co-Senna | docusate + sennoside B | Tablet containing docusate sodium 50 mg with sennoside B 8 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

Note that the current PBS items include an ear-drop product (Waxsol, ceruminolytic use) and oral laxative tablets (Coloxyl 50 and docusate with sennoside B).

<!-- review:begin au-lic-20261117-docusate-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Note that the only ARTG entry is an ear-drop product (ceruminolytic use). It is not an oral laxative formulation, so no registered route matches the predicted systemic indications." Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-docusate-1 -->

## Safety Considerations

- **Drug Interactions** (4 recorded):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor
- **Disease-level contraindication signals** (from the knowledge graph, not product label text): peptic ulcer disease, potassium deficiency, sickle cell anaemia, haemolytic anaemia, hereditary haemochromatosis, haemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, appendicitis, chronic atrophic gastritis, gastroenteritis, primary hyperoxaluria, hereditary persistence of fetal haemoglobin and Leber hereditary optic neuropathy.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available. Please refer to the PI for confirmed safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data for docusate, and a testable hypothesis for Plummer-Vinson syndrome
- Product Information warnings and contraindications for a relevant formulation
- Any preclinical or clinical evidence supporting benefit in the predicted condition
- A route and formulation assessment, since the only ARTG entry is an ear-drop product
- Consideration of whether a more established treatment, such as iron replacement and oesophageal dilatation for Plummer-Vinson syndrome, already addresses the need

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

