---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-11-24
description: "Bevacizumab: predicted new indication Epiglottis neoplasm (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Bevacizumab
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

## Bevacizumab: anti-VEGF-A monoclonal antibody → epiglottis neoplasm
{: .text-alpha }

## One-Sentence Summary

Bevacizumab is a monoclonal antibody that neutralises VEGF-A and is listed in Australia as a marketed product. The TxGNN model predicts it may be useful for **epiglottis neoplasm**, but no clinical trials or publications were found for this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bevacizumab: "Bevacizumab products bind VEGF and prevent the interaction of VEGF to its receptors (Flt-1 and KDR) on the surface of endothelial cells. The interaction of VEGF with its receptors leads to endothelial cell proliferation and new blood vessel formation in in vitro models of angiogenesis." ([DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe), label version 2026-08-21; accessed 2026-11-19.) Based on what is generally known, bevacizumab binds and neutralises VEGF-A, which can limit the growth of new blood vessels that tumours depend on.

Because many head and neck tumours rely on angiogenesis, there is a plausible biological reason to consider an anti-VEGF agent for a tumour of the epiglottis. This link is theoretical only. No trials or publications were retrieved for epiglottis neoplasm, so the prediction cannot be considered supported by clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered for this disease.

## Literature Evidence

Currently no related literature available for this disease.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 12479T | Mvasi | Bevacizumab | Solution for I.V. infusion 100 mg in 4 mL | Valid |
| 12508H | Mvasi | Bevacizumab | Solution for I.V. infusion 100 mg in 4 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Label warnings and contraindications are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Drug Interactions:** 22 interactions were recorded in the data compiled for this report. Major-level interactions include:
- Deferiprone
- Samarium (153Sm) lexidronam
- Panitumumab
- Sunitinib
- Thalidomide

Moderate-level interactions include bisphosphonates (alendronic, risedronic, etidronic, pamidronic and tiludronic acids, ibandronate), colony-stimulating factors (filgrastim, pegfilgrastim, sargramostim), palifermin, idelalisib, strontium chloride Sr-89, radium Ra 223 dichloride, romosozumab and sodium phosphate (P32).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for epiglottis neoplasm has no supporting trials or publications, so the evidence level is L5 (model prediction only). The mechanistic argument is generic and does not justify moving forward on its own.

**To proceed, the following is needed:**
- A targeted literature and trial search for bevacizumab in laryngeal, supraglottic and wider head and neck tumours
- Mechanism of action data
- Label warnings and contraindications from the TGA Product Information
- Clarification of the approved indication for the Australian product
- Assessment of the risk-benefit balance in this rare tumour site

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

