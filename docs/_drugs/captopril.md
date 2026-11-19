---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 130
evidence_level: L5
indication_count: 3
monitor_inn: "Captopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
last_modified_at: 2026-11-20
description: "Captopril: predicted new indication malignant hypertensive renal disease (evidence level L5). In Australia: 1 PBS item (1 currently listed)"
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Captopril: ACE inhibitor → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an angiotensin-converting enzyme (ACE) inhibitor that is currently marketed in Australia. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, with a score of **0.9928**. No clinical trials are registered for this prediction, and the only publication retrieved is a **single diagnostic case report**, so evidence is limited to the model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for captopril: "The mechanism of action of captopril tablets have not yet been fully elucidated. Its beneficial effects in hypertension and heart failure appear to result primarily from suppression of the renin-angiotensin-aldosterone system." ([DailyMed: captopril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ccbffd30-4b21-4522-bdb8-abba8d592017), label version 2026-11-11; accessed 2026-11-19.) Captopril is, however, a member of the ACE inhibitor class. These drugs reduce production of angiotensin II, a key effector of the renin-angiotensin system (RAS).

Malignant hypertension with renal injury is a condition in which RAS activation is thought to play a role in driving blood pressure and kidney damage. That gives a plausible mechanistic link to RAS blockade.

This link is theoretical. The only retrieved publication is a case report in which a positive captopril renography led to the discovery of a renal cell carcinoma. It is a diagnostic report and does not show that captopril treats malignant hypertensive renal disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | A positive captopril renography, which usually indicates renin-dependent hypertension from renal artery stenosis, was instead caused by a large chromophobe renal cell carcinoma. Hypertension resolved after nephrectomy. This is diagnostic, not therapeutic, evidence. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8760C | Capoten | Oral solution 5 mg per mL, 95 mL | Not recorded in the local data |

## Safety Considerations

**Drug Interactions** (the data compiled for this report lists 100 interactions; the first 20 are summarised here):

- **Moderate:**
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Glucose-lowering agents: metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, acetohexamide, chlorpropamide
  - Others: bupropion, morphine, acetylsalicylic acid, dronabinol
- **Minor:** aluminium hydroxide, calcium carbonate

No warning or contraindication text from the TGA-approved Product Information is available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered clinical trials, and the single retrieved publication is a diagnostic case report that does not test captopril as a treatment. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Clinical or observational studies that directly examine ACE inhibition in malignant hypertensive renal disease
- Detailed mechanism of action data
- Safety review based on the TGA-approved Product Information, including renal function and potassium monitoring in this population
- Confirmation of the approved indication text for the Australian product

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for captopril is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: captopril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ccbffd30-4b21-4522-bdb8-abba8d592017) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

