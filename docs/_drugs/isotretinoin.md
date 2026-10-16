---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Isotretinoin: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder / hypertension"
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Isotretinoin: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

The data compiled for this report list hypertension as the original indication for isotretinoin, but this appears to be a knowledge-graph artefact, because isotretinoin is marketed in Australia as an oral retinoid for severe recalcitrant acne. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction (**Evidence Level L5**, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; the ARTG entry has no indication text, and the label use is likely severe acne) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isotretinoin is a retinoid (13-cis-retinoic acid) with no established antihypertensive mechanism. The "original indication" of hypertension in the knowledge graph is most likely a data artefact.

Possible links through retinoid effects on renal inflammation or the renin-angiotensin system are speculative. The second-ranked prediction, malignant renovascular hypertension, has an identical score (99.01%), suggesting the two predictions share the same graph neighbourhood rather than representing independent signals. The overall prediction should be treated as a hypothesis only.

Other predictions follow the same pattern:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.01% | L5 | No evidence; score identical to rank 1 |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 98.89% | L4 | Only indirectly related papers (see below) |
| Pulmonary hypertension with unclear multifactorial mechanism | 98.89% | L5 | No evidence; pregnancy risk is a major concern |
| Braddock syndrome | 98.66% | L5 | No evidence; rare disease |
| Chronic pulmonary heart disease | 88.70% | L5 | No evidence |
| Cholangiocarcinoma, susceptibility to | 61.91% | L5 | No evidence; a susceptibility phenotype |
| Obsolete functional visual loss | 59.19% | L5 | Not credible given ocular adverse effects |
| Mitral valve prolapse, myxomatous | 59.11% | L5 | No plausible mechanism |
| Ocular tuberculosis | 58.68% | L5 | No antimycobacterial activity |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (malignant hypertensive renal disease), or for any of the other nine predicted indications.

## Literature Evidence

Currently no related literature available for the top-ranked prediction. The only publications retrieved were for the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), and they are only indirectly related:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16549710](https://pubmed.ncbi.nlm.nih.gov/16549710/) | 2006 | Case report | Archives of Dermatology | Diffuse dermal angiomatosis of the breast; not about pulmonary hypertension |
| [10030263](https://pubmed.ncbi.nlm.nih.gov/10030263/) | 1999 | Clinical study | Int J Radiat Oncol Biol Phys | Tumour oxygenation in cervical cancer during radiotherapy, with and without 13-cis-retinoic acid/interferon-alpha |
| [9830438](https://pubmed.ncbi.nlm.nih.gov/9830438/) | 1998 | Clinical study | Strahlentherapie und Onkologie | Two-week pretreatment with 13-cis-retinoic acid plus interferon-alpha-2a improved tumour oxygenation in cervical cancer |

None of these studies examined pulmonary hypertension or hypertensive renal disease.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 11621P | Roaccutane | Capsule 20 mg (oral) | Not specified in the data compiled |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

