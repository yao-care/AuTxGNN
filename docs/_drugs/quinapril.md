---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Quinapril
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

# Quinapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril is an angiotensin-converting enzyme (ACE) inhibitor, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The Australian ARTG entry has no indication text, so this comes from the knowledge graph used by the model |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, quinapril is an ACE inhibitor. It lowers blood pressure by reducing angiotensin II formation, and it may also lower pressure within the kidney's filtering units (intraglomerular pressure).

Malignant hypertensive renal disease is a severe form of hypertension with kidney involvement. It is therefore a close extension of quinapril's original indication rather than a true repurposing candidate. The high score probably reflects this close disease relationship.

Several other predictions were also generated. The most notable is **pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.85%, L4). It is supported by one 1996 animal study (PMID 8873672) in which tissue ACE inhibition with quinapril reduced hypoxic pulmonary hypertension and vascular remodelling. This is preclinical evidence only. The other predictions, including malignant renovascular hypertension, Braddock syndrome, Prinzmetal angina and intracerebral haemorrhage, have no direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for malignant hypertensive renal disease. The table below lists the publications retrieved for the other predicted indications, all of which are indirect or preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Preclinical animal study | Circulation | Tissue ACE inhibition with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodelling (pulmonary hypertension due to lung disease/hypoxia) |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Preclinical animal study | J Cardiovasc Pharmacol | Quinapril helped preserve left ventricular function and energy metabolism in rats after myocardial infarction (only indirectly relevant) |
| [8160617](https://pubmed.ncbi.nlm.nih.gov/8160617/) | 1994 | Small clinical haemodynamic study | Am J Cardiol | A single dose of quinapril improved left ventricular performance in chronic mitral regurgitation (different condition) |
| [3035534](https://pubmed.ncbi.nlm.nih.gov/3035534/) | 1987 | Adverse-effect report | Presse Med | Eight cases of ACE inhibitor cough (one with quinapril), resolving after withdrawal (a safety issue) |
| [35098999](https://pubmed.ncbi.nlm.nih.gov/35098999/) | 2022 | Preclinical screening (zebrafish) | Dis Model Mech | Drug screen identifying candidate neuroprotective therapies after intracerebral haemorrhage (the role of quinapril is not confirmed) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1968N | ACQUIN | Tablet 5 mg (as hydrochloride), oral | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindications and conditions of concern (from the knowledge graph, not label text)**: Kidney disease, anuria, liver disease, hepatic encephalopathy, pancreatitis, angioedema (including hereditary and ACE inhibitor-induced forms), systemic lupus erythematosus and other connective tissue diseases, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hypotension, neutropenia and agranulocytosis, hyperparathyroidism, gout and hyperuricaemia, and neonatal jaundice. These are model-derived associations and should be verified against the Product Information.
- **Drug Interactions**: 100 interactions were identified.
  - **Major**: potassium citrate (risk of hyperkalaemia).
  - **Moderate (examples)**: metformin, canagliflozin, dapagliflozin, chlorpropamide, acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), doxycycline, tetracycline, bupropion, morphine and atropine.
- **Additional considerations**: ACE inhibitors carry a known risk of acute renal failure in bilateral renal artery stenosis, which matters for renovascular hypertension. ACE inhibitor cough may be relevant in patients with chronic lung disease.

Please also refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.86%), but there are no clinical trials or publications for this indication, so the evidence level is L5. The indication is also largely an extension of quinapril's existing hypertension use rather than a distinct repurposing opportunity.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information, including the approved indications, warnings and contraindications (the ARTG indication text and label safety data were unavailable)
- Mechanism of action data
- Clinical studies or a systematic literature search specific to malignant hypertension with renal involvement
- A renal safety assessment, particularly for renovascular disease and existing kidney impairment
- If a distinct opportunity is wanted, further evaluation of pulmonary hypertension (L4), starting with clinical feasibility and safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

