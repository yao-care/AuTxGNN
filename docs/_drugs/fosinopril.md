---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 319
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Fosinopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Fosinopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Fosinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Fosinopril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Fosinopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (top-ranked prediction, score 0.9987), but there are currently **no clinical trials and no publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |


---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fosinopril belongs to the ACE inhibitor class. Its efficacy in hypertension is established, and by blocking the renin-angiotensin-aldosterone system (RAAS) it may be applicable to related hypertensive kidney conditions.

Malignant hypertension with renal involvement is a severe extension of the approved hypertension indication, so RAAS blockade is mechanistically plausible. However, acute malignant hypertension is usually managed with intravenous agents, so oral fosinopril would be an adjunct at most. The high TxGNN score is a model prediction only, with no supporting trials or literature.

A specific safety concern applies: ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis or stenosis in a solitary kidney.

This is a well-established class mechanism, and ACE inhibitors are guideline-supported in diabetic kidney disease. The question here is fosinopril-specific positioning rather than a new-drug repurposing signal.

Other predictions (pulmonary hypertension variants, Braddock syndrome, chronic pulmonary heart disease, rare small vessel and hereditary syndromes, intracerebral haemorrhage) have weak or non-specific mechanistic rationale and no direct supporting evidence.

---

## Clinical Trial Evidence

No trials are registered for the top-ranked prediction (malignant hypertensive renal disease).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00315016](https://clinicaltrials.gov/study/NCT00315016) | Phase 2 | Completed | 30 | Eplerenone vs doubling the ACE inhibitor dose for reducing urinary albumin loss in diabetes. Fosinopril is likely background therapy, not the investigational drug. |

---

## Literature Evidence

No publications were retrieved for malignant hypertensive renal disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16634995](https://pubmed.ncbi.nlm.nih.gov/16634995/) | 2006 | Clinical study | Diabetes Obes Metab | Efficacy and tolerability of fosinopril over 2 years in 38 Chinese type 2 diabetic patients with moderate renal impairment |
| [23816723](https://pubmed.ncbi.nlm.nih.gov/23816723/) | 2013 | Open-label randomised comparative study | Saudi J Kidney Dis Transpl | Fosinopril compared with the herbal drug *Dioscorea bulbifera* in diabetic nephropathy |
| [13129736](https://pubmed.ncbi.nlm.nih.gov/13129736/) | 2003 | Clinical study | Di 1 Jun Yi Da Xue Xue Bao | Losartan plus fosinopril combination in early diabetic nephropathy |
| [9736436](https://pubmed.ncbi.nlm.nih.gov/9736436/) | 1998 | Review | J Cardiovasc Pharmacol | Relationships among diabetes, microalbuminuria and ACE inhibition |
| [7771972](https://pubmed.ncbi.nlm.nih.gov/7771972/) | 1995 | Review | Aust Fam Physician | Critical assessment of ACE inhibitors, including delay of diabetic nephropathy progression |
| [26617877](https://pubmed.ncbi.nlm.nih.gov/26617877/) | 2015 | Preclinical (rat) | Int J Clin Exp Pathol | Fosinopril effect on chemerin and VEGF expression in diabetic nephropathy rats |
| [9037329](https://pubmed.ncbi.nlm.nih.gov/9037329/) | 1997 | Preclinical (rat) | Am J Hypertens | Cicaprost and fosinopril effects on progression of rat diabetic nephropathy |
| [31853288](https://pubmed.ncbi.nlm.nih.gov/31853288/) | 2020 | Preclinical (rat) | Exp Ther Med | Fosinopril effect on renal cortex protein expression in OLETF rats |

For other predictions, the literature is indirect or unhelpful. For pulmonary hypertension owing to lung disease, [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) (1998) reports hypoxic eosinophilic pneumonia in two patients treated with ACE inhibitors (including fosinopril), which is an adverse-effect signal rather than a benefit.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1182F | Monace 10 | Tablet containing fosinopril sodium 10 mg (oral) | Not listed in the data compiled for this report |

*The licence number is reported as given in the data and should be verified against the ARTG.*

---

## Safety Considerations

Contraindication data from product labelling is not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

**Knowledge-graph contraindication signals** (from drug-disease network links, not label text) include:
- Kidney and liver disease, hepatic encephalopathy
- Angioedema, including hereditary and ACE inhibitor-related forms
- Pancreatitis and gallbladder disease
- Systemic lupus erythematosus and connective tissue disease
- Diabetes, diabetic ketoacidosis and potassium deficiency
- Neutropenia and agranulocytosis
- Aortic stenosis and hypotensive disorders
- Hyperparathyroidism and bone disease

**Drug interactions:** the interaction screen returned 100 interactions in total. The ones shown include:
- **Major:** potassium bicarbonate and potassium citrate (hyperkalaemia risk)
- **Moderate:** corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, triamcinolone), aspirin, and glucose-lowering drugs (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), plus bupropion, morphine, dronabinol, picosulfuric acid and polyethylene glycol with electrolytes

**Indication-specific concerns:**
- Renovascular hypertension: risk of acute renal failure with bilateral renal artery stenosis or stenosis in a solitary kidney
- Hypoxic lung disease: reported ACE inhibitor-associated eosinophilic pneumonia

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (malignant hypertensive renal disease) has a very high model score but no trials or literature, so it remains at L5. Acute management usually relies on intravenous agents.
- Fosinopril-specific human RCT evidence is limited, no Phase 3 data are shown, and the single trial uses fosinopril only as likely background therapy. Because ACE inhibitors are already used clinically in this setting, this is a question of fosinopril-specific positioning rather than a new repurposing signal.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA-approved PI (warnings, contraindications and approved indication text)
- For malignant hypertensive renal disease: any clinical or observational evidence for oral fosinopril, and a defined role alongside intravenous therapy
- Review of the knowledge-graph contraindication signals against the label before any new-population use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

