---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Isotretinoin
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

## Isotretinoin: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

The data compiled for this report list hypertension as the original indication for isotretinoin, but this appears to be a TxGNN model (deep learning) artefact, because isotretinoin is marketed in Australia as an oral retinoid for severe recalcitrant acne. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction (**Evidence Level L5**, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for isotretinoin: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), label version 2026-09-20; accessed 2026-11-19.) Isotretinoin is a retinoid (13-cis-retinoic acid) with no established antihypertensive mechanism.

Possible links through retinoid effects on renal inflammation or the renin-angiotensin system are speculative. The score of 0.9901 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The overall prediction should be treated as a hypothesis only.

Other predictions follow the same pattern:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (malignant hypertensive renal disease), or for any of the other nine predicted indications.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16549710](https://pubmed.ncbi.nlm.nih.gov/16549710/) | 2006 | Case report | Archives of Dermatology | Diffuse dermal angiomatosis of the breast; not about pulmonary hypertension |
| [10030263](https://pubmed.ncbi.nlm.nih.gov/10030263/) | 1999 | Clinical study | Int J Radiat Oncol Biol Phys | Tumour oxygenation in cervical cancer during radiotherapy, with and without 13-cis-retinoic acid/interferon-alpha |
| [9830438](https://pubmed.ncbi.nlm.nih.gov/9830438/) | 1998 | Clinical study | Strahlentherapie und Onkologie | Two-week pretreatment with 13-cis-retinoic acid plus interferon-alpha-2a improved tumour oxygenation in cervical cancer |

None of these studies examined pulmonary hypertension or hypertensive renal disease.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2549E | Dermatane | Isotretinoin | Capsule 40 mg | Valid |
| 2591J | Dermatane | Isotretinoin | Capsule 10 mg | Valid |
| 2592K | Dermatane | Isotretinoin | Capsule 20 mg | Valid |
| 11621P | Roaccutane | Isotretinoin | Capsule 20 mg | Valid |
| 11716P | Oratane | Isotretinoin | Capsule 5 mg | Valid |
| 11921K | Oratane | Isotretinoin | Capsule 30 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Cytotoxicity

Isotretinoin is not classed as an antineoplastic drug in the data compiled, and the original indication is not oncological, so a cytotoxicity assessment is not applicable.

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Knowledge-graph contraindication signals** (not label text): anxiety and other mental disorders (including psychotic and schizoaffective disorders), kidney disease, liver disease, gallbladder disease, pancreatitis, inflammatory bowel disease, osteoporosis, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, angioedema (several forms), neutropenia and agranulocytosis, potassium deficiency, and hypotensive disorder. Kidney disease is particularly relevant to the top-ranked prediction.
- **Drug interactions**: 98 interactions were recorded. Examples include:
  - **Major**: tetracycline, doxycycline, minocycline and vitamin A.
  - **Moderate**: systemic corticosteroids (for example prednisone, dexamethasone, hydrocortisone), warfarin, naltrexone, ethanol, ivacaftor and lumacaftor.
- **Other concerns noted in the analysis**: isotretinoin is teratogenic and contraindicated in pregnancy, and it is associated with ocular adverse effects such as dry eye and reduced night vision.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or relevant literature, no plausible antihypertensive mechanism, and a likely erroneous original indication. The safety profile (teratogenicity, kidney-disease contraindication signal, many interactions) further argues against progression.

**To proceed, the following is needed:**
- Verification of the original indication, and the TGA-approved indication text for ARTG 11621P
- Mechanism of action data, and a mechanistic rationale for retinoids in hypertensive renal or pulmonary vascular disease
- Preclinical or clinical evidence in the predicted indication
- Product Information warnings and contraindications for formal safety screening
- A pregnancy-prevention and risk-management assessment for any new use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

