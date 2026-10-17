---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Atenolol: predicted new indication Posterolateral myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "primary hereditary glaucoma"]
---

# Atenolol
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

# Atenolol: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective beta-blocker, originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**,
but there are currently **no registered clinical trials** and **no publications** specific to this subtype. This is an anatomical subtype of an indication atenolol already holds, so it is not a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; no approved indication text is available in the ARTG data) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atenolol is a beta-1 selective adrenergic blocker. Its efficacy in hypertension and myocardial infarction is established. By lowering heart rate, contractility and myocardial oxygen demand, it is mechanistically applicable to myocardial infarction.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an established atenolol indication. The high TxGNN score most likely reflects closeness to the parent disease in the knowledge graph rather than a new therapeutic signal. No trials or publications specific to this subtype were identified.

### Other Predicted Indications

The other top-ranked predictions are summarised below. None has strong supporting evidence.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Posteroinferior myocardial infarction | 99.87% | L4 | Subtype of the approved indication. One 1985 small single-blind crossover study of anti-ischaemic activity (atenolol vs diltiazem) after infarction. Indirect and dated. |
| 3 | Malignant hypertensive renal disease | 99.85% | L5 | Plausible via blood pressure control, but atenolol is renally cleared and needs dose adjustment. No data. |
| 4 | Malignant renovascular hypertension | 99.85% | L4 | Beta-blockade reduces renin release. Only a single case report, which is anecdotal. |
| 5 | Pulmonary hypertension, unclear multifactorial mechanism | 99.84% | L5 | No data. Beta-blockers are not an established treatment and may affect right ventricular function. |
| 6 | Pulmonary hypertension owing to lung disease or hypoxia | 99.84% | L4 | Mostly off-target or animal studies with conflicting findings. Safety concerns outweigh the weak signal. |
| 7 | Septal myocardial infarction | 99.84% | L4 | Subtype of the approved indication. One 1981 thallium-201 imaging study, not an outcome trial. |
| 8 | Braddock syndrome | 99.80% | L5 | No data or documented mechanism. Graph-based prediction only. |
| 9 | Chronic pulmonary heart disease | 99.04% | L4 | Literature is general beta-blocker and hypertension material, not specific to cor pulmonale. |
| 10 | Primary hereditary glaucoma | 98.84% | L5 | Class-level plausibility (topical beta-blockers such as timolol), but oral atenolol has no documented role. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (posterolateral myocardial infarction), currently no related literature is available.

The closest supporting literature, found under related predictions, is listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Randomised crossover study (single-blind, small) | La Revue de médecine interne | Atenolol 200 mg vs diltiazem 240 mg in 23 patients with residual ischaemia 4 weeks after a postero-inferior or anterior infarction, using computerised exercise testing. |
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Small clinical imaging study | Zeitschrift für Kardiologie | Thallium-201 stress scintigraphy in 14 coronary artery disease patients after intravenous atenolol 5 mg. A physiological study, not an outcome trial. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1081X | Atenolol GH | Tablet 50 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

The knowledge graph links atenolol with the following conditions as contraindications. These are graph-derived associations, not label text, and should be verified against the Product Information.

- **Cardiac and vascular:** atrioventricular block, Raynaud disease
- **Respiratory and allergic:** asthma (including intrinsic and allergic asthma), anaphylaxis
- **Metabolic and endocrine:** type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency
- **Other:** liver failure, anuria, pancreatitis, systemic lupus erythematosus (including paediatric), psoriasis and parapsoriasis, anxiety, neurotic and dysthymic disorders

**Drug Interactions:** 100 interactions were identified. Those retrieved are mainly moderate. Examples include:
- Moderate: epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide, and calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate)
- Minor: acetylsalicylic acid, aluminium hydroxide, attapulgite

For label warnings and contraindications, please refer to the TGA-approved Product Information (PI), as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posterolateral myocardial infarction is a subtype of an indication atenolol is already used for, so the prediction adds little new information. There are no trials or publications specific to this subtype, and the evidence level is L5. Among the other predictions, those outside the cardiovascular space (pulmonary hypertension, hereditary glaucoma, Braddock syndrome) lack supporting data or carry safety concerns.

**To proceed, the following is needed:**
- The TGA-approved Product Information (PI), including approved indications, warnings and contraindications
- Detailed mechanism of action data (MOA)
- Confirmation of whether the existing myocardial infarction indication already covers this subtype
- For any genuinely new indication (such as malignant renovascular hypertension), controlled clinical evidence, with renal dosing considerations
- A safety review against the graph-derived contraindication signals, particularly asthma, diabetes and atrioventricular block
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

