---
layout: default
title: Cetuximab
parent: Model Prediction Only (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
monitor_inn: "Cetuximab"
predicted_indications: ["bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "ductal or ductular proliferation", "non-seminomatous lesion", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "cystic neoplasm", "epiglottis neoplasm", "pre-malignant neoplasm"]
last_modified_at: 2026-11-24
description: "Cetuximab: predicted new indication bronchial adenomas/carcinoids childhood (evidence level L5). In Australia: 14 PBS items (14 currently listed)"
---

# Cetuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Cetuximab: EGFR-targeted monoclonal antibody → bronchial adenomas/carcinoids childhood
{: .text-alpha }

## One-Sentence Summary

Cetuximab is an anti-EGFR monoclonal antibody marketed in Australia as Erbitux.
The TxGNN model predicts it may be relevant to **bronchial adenomas/carcinoids childhood**, but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | bronchial adenomas/carcinoids childhood |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (14 of 14 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 14 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cetuximab: "The epidermal growth factor receptor (EGFR, HER1, c-ErbB-1) is a transmembrane glycoprotein that is a member of a subfamily of type I receptor tyrosine kinases including EGFR, HER2, HER3, and HER4. The EGFR is constitutively expressed in many normal epithelial tissues, including the skin and hair follicle. […] Cetuximab binds specifically to the EGFR on both normal and tumor cells, and competitively inhibits the binding of epidermal growth factor (EGF) and other ligands, such as transforming growth factor-alpha." ([DailyMed: Erbitux (cetuximab) prescribing information, ImClone LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8bc6397e-4bd8-4d37-a007-a327e4da34d9), label version 2026-04-16; accessed 2026-11-19.) Cetuximab is known to bind the epidermal growth factor receptor (EGFR), and the pharmacology data lists EGFR as its target.

The data compiled for this report does not support a link between EGFR blockade and childhood bronchial carcinoids. No trial or publication addresses this disease, and the mechanistic rationale is therefore unconfirmed. The prediction should be treated as a hypothesis for further investigation, not as a supported use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4312Y | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 4435K | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 4436L | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 4731B | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 7223E | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 7240C | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 7242E | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 7273T | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 10262D | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 10265G | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 12816M | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 12817N | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 12820R | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |
| 12821T | Erbitux | Cetuximab | Solution for I.V. infusion 100 mg in 20 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 20 interaction records were compiled. Two are rated **Major**: aminolevulinic acid and thalidomide. Most others are rated Moderate, including proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), platinum agents (cisplatin, carboplatin, oxaliplatin), fluorouracil, capecitabine, idelalisib, methoxsalen, verteporfin, omacetaxine mepesuccinate and topical photosensitising agents.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9995) but no trials or publications directly studying childhood bronchial adenomas/carcinoids, so the evidence level is L5.

**To proceed, the following is needed:**
- Published or registered studies directly addressing EGFR targeting in childhood bronchial carcinoids
- Mechanism of action data to support a biological rationale
- The TGA Product Information, to review warnings and contraindications
- A paediatric-specific safety and dosing assessment

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Erbitux (cetuximab) prescribing information, ImClone LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8bc6397e-4bd8-4d37-a007-a327e4da34d9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

