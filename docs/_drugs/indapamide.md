---
layout: default
title: Indapamide
parent: Model Prediction Only (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Indapamide
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

# Indapamide: From Hypertension to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Indapamide is a thiazide-like diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **chronic pulmonary heart disease**, but **no clinical trials** and only **2 loosely related publications** (a general review and an overdose case report) support this prediction.
The evidence is model prediction only, so this should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the approved indication text for the Australian listing was not available) |
| Predicted New Indication | Chronic pulmonary heart disease |
| TxGNN Prediction Score | 92.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, indapamide is a thiazide-like diuretic. Its efficacy in hypertension is established, and it reduces blood pressure and fluid volume. Chronic pulmonary heart disease (cor pulmonale) can involve right-heart volume overload, so a diuretic effect is plausible in principle.

However, the literature linked to this prediction does not test indapamide in this disease. One paper is a general review of the transition from hypertension to heart failure, and the other is a case report of an overdose. The high TxGNN score is a computational output without clinical backing.

Other top-ranked predictions are even weaker. Pulmonary hypertension (two categories), acute pulmonary heart disease, Braddock syndrome and primary hereditary glaucoma have no mechanistic rationale or supporting trials. Malignant hypertensive renal disease and malignant renovascular hypertension are unsuited to a chronic oral diuretic. Of the lower-ranked predictions, chronic kidney disease (CKD, rank 10, score 77.97%) has the most literature (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature linked to the top-ranked prediction (chronic pulmonary heart disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Fail | General update on how long-standing hypertension progresses to heart failure. It does not study indapamide or cor pulmonale. |
| [19623566](https://pubmed.ncbi.nlm.nih.gov/19623566/) | 2009 | Case report (overdose) | Pharmacoepidemiol Drug Saf | Overdose of methyldopa, indapamide and theophylline in an elderly patient caused prolonged hypotension, marked diuresis and hypokalaemia. This is a safety report, not evidence of benefit. |

**Note on the lower-ranked CKD prediction (rank 10):** this has the largest body of literature (20 publications in total), although evidence is mostly observational, review-level or based on a perindopril/indapamide combination. The most relevant items are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20501479](https://pubmed.ncbi.nlm.nih.gov/20501479/) | 2010 | Clinical study (ADVANCE analysis) | Eur Heart J | Perindopril-indapamide fixed combination assessed for renal and cardiovascular outcomes in type 2 diabetes by baseline CKD stage. |
| [38920202](https://pubmed.ncbi.nlm.nih.gov/38920202/) | 2023 | Cohort | Ann Acad Med Singap | Thiazide and thiazide-like diuretics were associated with improved cardiovascular and renal outcomes in CKD. |
| [34233330](https://pubmed.ncbi.nlm.nih.gov/34233330/) | 2021 | Review | Am J Nephrol | Reviews the often overlooked antiproteinuric properties of diuretics. |
| [23136355](https://pubmed.ncbi.nlm.nih.gov/23136355/) | 2012 | Review | Ann Pharmacother | Examines whether thiazides have a chronic antihypertensive effect in severe renal disease or dialysis, even without diuresis. |
| [7618651](https://pubmed.ncbi.nlm.nih.gov/7618651/) | 1995 | Clinical study | Am J Nephrol | In patients with impaired renal function and hypertension, indapamide was associated with increased creatinine clearance, whereas hydrochlorothiazide was associated with a decrease. |
| [6346847](https://pubmed.ncbi.nlm.nih.gov/6346847/) | 1983 | Clinical study | Am Heart J | Indapamide 2.5 mg/day was reported as safe and effective for lowering blood pressure in hypertensive patients, including those with chronic renal failure and those on haemodialysis. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13378D | Dapa-Tabs | Oral tablet containing indapamide hemihydrate 2.5 mg | Not available in the data compiled for this report |

## Safety Considerations

The data compiled for this report did not include label-based warnings or contraindications. Please refer to the TGA-approved Product Information (PI) for these.

- **Conditions linked to indapamide as contraindications in a knowledge graph** (not label text): liver disease, gallbladder disease, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, hyperparathyroidism, osteitis fibrosa, anuria and gout.
- **Drug interactions:** 100 interactions were identified. The first 20 reviewed are mostly Moderate, with a few Minor. Notable moderate interactions include:
  - Antidiabetic agents: acarbose, alogliptin, albiglutide and metformin.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone and beclomethasone.
  - Amphotericin B (including the lipid complex).
  - Others: bupropion, morphine, omeprazole, rabeprazole, cholecalciferol and bisacodyl.
- **Minor interactions:** doxycycline, hyoscyamine and atropine.
- **Safety signals in the linked literature:** overdose can cause prolonged hypotension, marked diuresis and hypokalaemia (PMID 19623566). Indapamide-associated choroidal effusion and acute angle-closure glaucoma have been reported (PMID 34736431), which argues against repurposing for glaucoma without further safety work.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions rest only on a computational score, with no registered trials and no literature that tests indapamide in these diseases. The linked papers are a general review and an overdose case report. Of the lower-ranked predictions, chronic kidney disease (L3) has the most supporting literature, but it is mostly observational or combination-based, so it is best treated as a research question rather than a candidate for adoption.

**To proceed, the following is needed:**
- Mechanism of action data for indapamide.
- The approved indication text and label-based warnings and contraindications from the TGA Product Information.
- A focused literature review and any clinical trial data for indapamide in right-heart failure or cor pulmonale.
- For CKD, a systematic review separating the effect of indapamide alone from perindopril combination effects, with confirmation of efficacy at low eGFR.
- A safety assessment of the electrolyte, metabolic and ocular risks in the target population.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

