---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 7
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
last_modified_at: 2026-11-24
description: "Cladribine: predicted new indication parameningeal embryonal rhabdomyosarcoma (evidence level L5). In Australia: 5 PBS items (5 currently listed)"
---

# Cladribine
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

## Cladribine: purine nucleoside analogue → parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## One-Sentence Summary

Cladribine is a purine nucleoside analogue that is marketed in Australia as an oral tablet. The TxGNN model predicts it may be relevant to **parameningeal embryonal rhabdomyosarcoma**, with a score of 0.9977. However, **no clinical trials and no publications** directly support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (5 of 5 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cladribine: "The mechanism by which cladribine exerts its therapeutic effects in patients with multiple sclerosis has not been fully elucidated but is thought to involve cytotoxic effects on B and T lymphocytes through impairment of DNA synthesis, resulting in depletion of lymphocytes." ([DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144), label version 2026-05-27; accessed 2026-11-19.) From general pharmacology, cladribine is a purine nucleoside analogue that resists breakdown by adenosine deaminase and is cytotoxic to lymphocytes and monocytes. Its activity depends on activation by deoxycytidine kinase (dCK).

The link to parameningeal embryonal rhabdomyosarcoma is weak. This is a solid tumour of muscle-lineage origin, and solid tumours of this type are generally not reported to be sensitive to cladribine. No mechanism specific to this disease has been established.

The score is also not independent evidence. Several closely related rhabdomyosarcoma subtypes and the parent term received near-identical scores in the same range, which suggests one shared model signal rather than separate lines of support. A sensible first research step would be laboratory testing of dCK-dependent sensitivity in rhabdomyosarcoma cell lines.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this disease.

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4326Q | Leustatin | Cladribine | Solution for I.V. infusion 10 mg in 10 mL single use vial | Valid |
| 7225G | Leustatin | Cladribine | Solution for I.V. infusion 10 mg in 10 mL single use vial | Valid |
| 11603Q | Mavenclad | Cladribine | Tablet 10 mg | Valid |
| 11604R | Mavenclad | Cladribine | Tablet 10 mg | Valid |
| 11611D | Mavenclad | Cladribine | Tablet 10 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The approved indication text is not recorded in the local data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling requirements |

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 recorded interactions. Those shown are mostly rated Major, including:
  - Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Radiopharmaceuticals and radioimmunotherapy: ibritumomab tiuxetan, tositumomab, iobenguane (I-131), samarium (153Sm) lexidronam, strontium chloride Sr-89
  - Deferiprone

  Moderate interactions include palifermin, dipyridamole, cilostazol and eltrombopag.

Warnings and contraindications from the label are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trial or publication studies cladribine in parameningeal embryonal rhabdomyosarcoma, and no disease-specific mechanism is established, so the evidence level is L5.

**To proceed, the following is needed:**
- Preclinical data showing cladribine sensitivity in rhabdomyosarcoma models, including dCK expression and activity
- Mechanism of action data
- Label warnings and contraindications from the TGA Product Information
- A specific safety and myelosuppression review, given the cytotoxic nature of the drug

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

