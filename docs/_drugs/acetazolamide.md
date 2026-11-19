---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-10-30
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). In Australia: 1 PBS item (1 currently listed)"
---

# Acetazolamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Acetazolamide: carbonic anhydrase inhibitor → Exercise-induced malignant hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is an oral carbonic anhydrase inhibitor marketed in Australia as Diamox tablets.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, with a score of 0.9995.
However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for acetazolamide: "Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic." ([DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b), label version 2026-11-10; accessed 2026-11-19.) Acetazolamide is known as a carbonic anhydrase inhibitor, which alters acid-base balance and ion handling.

A possible link to exercise-induced malignant hyperthermia is that these changes might influence muscle ion handling and the body's response to exertion. This is speculative: no study in the compiled data tests the idea, and the relationship between the drug's known actions and this condition has not been established. The high score should be treated as a hypothesis for further investigation, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1004W | Diamox | Tablet 250 mg | Not recorded in the local data |

## Safety Considerations

Safety information in the compiled data is limited to drug interaction screening. Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

**Drug interactions** (100 interactions were identified; examples below):
- **Major:** acetylsalicylic acid (aspirin), cisapride
- **Moderate:** antidiabetic agents (e.g. acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide), corticosteroids (e.g. beclomethasone, betamethasone, dexamethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil)
- **Minor:** doxycycline

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high score but no supporting clinical trials, publications or defined mechanism (Evidence Level L5). A recommendation to proceed cannot be justified on model output alone.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible, testable pathway linking carbonic anhydrase inhibition to exercise-induced malignant hyperthermia
- Preclinical or clinical studies that directly address this condition
- TGA Product Information review for warnings, contraindications and approved-use details
- A safety assessment for the target population, including the drug interactions identified above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

