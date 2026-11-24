---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Lisinopril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
description: "Lisinopril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Lisinopril: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used for hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**.
There are currently **no clinical trials** and **no publications** supporting this specific subtype, so the prediction rests on model output and mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lisinopril: "Lisinopril inhibits angiotensin-converting enzyme (ACE) in human subjects and animals. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II. Angiotensin II also stimulates aldosterone secretion by the adrenal cortex." ([DailyMed: Qbrelis (lisinopril) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6e4e57-a489-4b36-b093-b93865d3717c), label version 2025-12-16; accessed 2026-11-19.) Lisinopril belongs to the ACE inhibitor class. These drugs reduce angiotensin II formation, lower afterload and limit adverse ventricular remodelling after a heart attack.

The very high TxGNN score (0.9989) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same pattern appears in the other top predictions:
- **Malignant hypertensive renal disease and malignant renovascular hypertension** are extensions of the hypertension indication. ACE inhibitors can worsen renal function in bilateral renal artery stenosis or stenosis in a solitary kidney.
- **Pulmonary hypertension** and **chronic pulmonary heart disease** are mechanistically plausible but not guideline-supported. The evidence is mostly preclinical, apart from two small Russian-language clinical studies on chronic cor pulmonale (PMIDs 14524095 and 17047621) of uncertain design.
- **Braddock syndrome** and a rare COL4A1-related syndrome have no supporting evidence and no clear mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2456G | Zestril | Lisinopril | Tablet 5 mg | Valid |
| 2457H | Zestril | Lisinopril | Tablet 10 mg | Valid |
| 2458J | Zestril | Lisinopril | Tablet 20 mg | Valid |
| 13402J | Zestril | Lisinopril | Tablet 20 mg | Valid |
| 13583X | Zestril | Lisinopril | Tablet 5 mg | Valid |
| 13584Y | Zestril | Lisinopril | Tablet 10 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

No label-based warnings or contraindications were available. The knowledge graph links lisinopril to the following conditions as contraindications (these are graph associations, not label text):

- **Angioedema:** including hereditary, acquired and RAAS-blocker-induced forms.
- **Kidney and liver disease:** kidney disease, liver disease, hepatic encephalopathy.
- **Cardiovascular:** aortic stenosis and hypotensive disorders.
- **Metabolic and electrolyte:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency and hyperparathyroidism.
- **Haematological and immune:** neutropenia, agranulocytosis, systemic lupus erythematosus and connective tissue disease.
- **Other:** pancreatitis, gallbladder disease and bone disease.

**Drug interactions:** the interaction query returned 100 interactions; the first 20 are summarised here.
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia).
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aspirin, morphine, bupropion, dronabinol, bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes), and several diabetes medicines (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide).

A published case report also describes severe hypotension and bradycardia when lisinopril was combined with tizanidine (PMID 20852161).

Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posterolateral MI is a subtype of an indication lisinopril already covers, so the prediction adds little beyond the existing approval. No trial or literature evidence exists for this subtype (Evidence Level L5).

**To proceed, the following is needed:**
- The approved indication wording from the TGA Product Information, to confirm whether MI subtypes are already covered
- Label-based warnings and contraindications from the PI, which are currently missing
- Mechanism of action data for lisinopril
- Subtype-specific data, such as post-hoc analyses of existing ACE inhibitor MI trials by infarct location
- If pursuing other predictions, the most developed is chronic pulmonary heart disease (L3), which would need controlled trial evidence and a hypotension safety review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Qbrelis (lisinopril) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6e4e57-a489-4b36-b093-b93865d3717c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

