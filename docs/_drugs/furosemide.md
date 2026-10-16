---
layout: default
title: Furosemide
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Furosemide: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and congestive heart failure (the registered indication…"
---

# Furosemide
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

# Furosemide: From Hypertension and Congestive Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Furosemide is a loop diuretic, originally used for hypertension and congestive heart failure. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** were found for this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the registered indication text for the Australian product is not available) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Furosemide is a loop diuretic. It blocks the NKCC2 transporter in the thick ascending limb of the loop of Henle, which reduces volume overload and lowers blood pressure.

Malignant hypertensive renal disease is kidney damage caused by severely raised blood pressure, and volume expansion contributes to it. That makes a diuretic mechanistically plausible. However, the prediction largely extends furosemide's existing hypertension indication rather than describing a new mechanism. The high score of 98.03% is a model output only. It is not supported by any trial or published study.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| ARTG 12222G | Frusemix-M | Tablet 20 mg (oral) |

The approved indication text for this entry is not available in the data compiled for this report.

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (drug-disease links, not product label text). Items fall into the following groups:
  - Low blood pressure and autonomic disorders: orthostatic hypotension, hypotensive disorder, multiple system atrophy, postural orthostatic tachycardia syndrome.
  - Renal and urinary: anuria, bladder neck obstruction, benign prostatic hyperplasia.
  - Metabolic and electrolyte: potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, diabetes mellitus, diabetic ketoacidosis, gout and hyperuricaemia.
  - Cardiac: myocardial infarction, coronary thrombosis.
  - Other: systemic lupus erythematosus (including paediatric), haemoglobinopathy, pancreatitis, hearing disorders and auditory system disease.
- **Drug Interactions**: The interaction query returned 100 interactions.
  - The only major interaction among those listed is **dolasetron**.
  - Moderate interactions include acarbose, rabeprazole, hydrocortisone, betamethasone, beclomethasone, amphotericin B, bisacodyl, chlorpropamide, and the diabetes agents albiglutide, alogliptin, dulaglutide, canagliflozin, dapagliflozin and empagliflozin.
  - Minor interactions include doxycycline and acetylsalicylic acid.

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature. It is largely an extension of furosemide's existing hypertension use, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or observational evidence of furosemide in malignant hypertensive renal disease.
- Detailed mechanism of action data.
- Approved indication text and PI warnings and contraindications for the Australian product.
- Review of the knowledge-graph contraindications (for example hypotension, anuria and electrolyte disorders) against this patient group.

**Note on other predictions:** In the same prediction set, **chronic kidney disease** has stronger support (L2, with a completed Phase 4 trial on blood pressure control in stage 3-4 CKD). It is rated "Proceed with Guardrails", limited to volume overload and blood pressure control with monitoring of electrolytes, renal function and ototoxicity. It may be a better candidate for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

