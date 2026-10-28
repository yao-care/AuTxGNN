---
layout: default
title: Lactic Acid
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Lactic Acid: predicted new indication Atypical coarctation of aorta (evidence level L5). Approved use: Not available"
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome"]
---

# Lactic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Lactic Acid: From an Unspecified Original Indication to Atypical Coarctation of Aorta
{: .text-alpha }

## One-Sentence Summary

Lactic acid is registered in Australia (one ARTG entry), but the data compiled for this report contain no approved indication text for it.
The TxGNN model (deep learning) predicts it may be effective for **atypical coarctation of aorta**. This prediction may reflect similarities the model learned between related diseases, not biological evidence, and **0 clinical trials** and **0 publications** support it.
Across all ten top-ranked predictions, none has a clinical trial or a publication showing lactic acid as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the registered licence has no approved indication text) |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The original indication is also not recorded in the data compiled for this report, so the link between the original and predicted indications cannot be assessed.

For atypical coarctation of aorta, no mechanistic link has been identified. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There are no linked trials or publications, and lactic acid has no known role in aortic structural development or in treating a congenital vascular malformation. Such conditions are managed surgically or by intervention, not pharmacologically.

The other top-ranked predictions are similarly weak:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Aortic malformation | 0.9935 | Literature is incidental (lactate as a perioperative biomarker, polylactic acid device materials). No therapeutic evidence. |
| 3 | Non-syndromic oesophageal malformation | 0.9923 | No data. Surgical condition. |
| 4 | Amenorrhoea | 0.9916 | One baboon vaginal microbiota study. No therapeutic link. |
| 5 | Dry eye syndrome | 0.9913 | Literature covers probiotics, biomarkers and tissue engineering. Lactic acid is a known ocular irritant at higher concentrations. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No ANZCTR entries were identified either.

---

## Literature Evidence

For the top-ranked prediction (atypical coarctation of aorta), currently no related literature is available.

The second-ranked prediction (aortic malformation) retrieved 14 publications, none of which tests lactic acid as a treatment. The most relevant are shown below for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | RCT | J Cardiothorac Vasc Anesth | Combined ultrafiltration strategy in paediatric cardiac surgery for congenital heart disease. Not related to lactic acid therapy. |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | Preclinical | J Vasc Surg | Aortic wall respiration and glycolysis proximal and distal to coarctation in rabbits on standard or atherogenic diets. |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | Preclinical | Catheter Cardiovasc Interv | Poly-l-lactic acid biodegradable stent in the rabbit descending aorta. This concerns the material, not lactic acid as a drug. |
| [31714687](https://pubmed.ncbi.nlm.nih.gov/31714687/) | 2020 | Case series | Catheter Cardiovasc Interv | Absorbable poly-l-lactic acid atrial septal defect closure device, preclinical to first-in-human. |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | Case report | Pediatr Cardiol | Absorbable poly-l-lactic acid microplates for bronchomalacia in infants with congenital heart disease. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 113Y (licence number as recorded) | Not recorded | Not recorded | Not recorded |

One valid single-ingredient entry is recorded. Product name, dosage form and approved indication are not available in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions**: 17 interactions were identified from DDInter. None is rated major.
  - **Moderate (10)**: doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline, acetylsalicylic acid, sodium salicylate, ephedrine (including nasal), pseudoephedrine.
  - **Minor (7)**: chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide, methotrexate.
- **Other considerations from the literature**: preclinical findings suggest lactic acid may promote choroidal neovascularisation and may suppress immunotherapy response in tumour microenvironments. Lactic acid is also an ocular irritant at higher concentrations. These are not clinical safety findings, but they argue for caution with any ocular or oncology use.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as none were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN scores are high, but none of the top ten predictions has a registered trial or literature supporting lactic acid as a therapy. For the leading prediction, structural congenital conditions have no plausible pharmacological role for lactic acid. Several findings (ocular neovascularisation, immunotherapy suppression) point to possible harm. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for lactic acid
- The approved indication, product name and dosage form for the Australian licence
- Warnings and contraindications from the TGA Product Information, which are needed before safety screening can proceed
- A plausible biological rationale for any predicted indication, followed by preclinical evidence, before clinical investigation is considered
- Consideration of other candidate indications, since the top-ranked predictions are largely structural or surgical conditions where a drug is unlikely to be effective
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

