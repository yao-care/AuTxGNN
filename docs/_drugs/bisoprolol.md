---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 4
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-17
description: "Bisoprolol: predicted new indication malignant hypertensive renal disease (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Bisoprolol
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

## Bisoprolol: beta-1 selective adrenergic blocker → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Bisoprolol is a beta-1 selective adrenergic blocker used to lower blood pressure. The TxGNN model predicts it may be relevant to **malignant hypertensive renal disease**. There are currently **no clinical trials** and **no publications** directly studying this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for bisoprolol: "BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose." ([DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e), label version 2026-11-11; accessed 2026-11-19.) Bisoprolol is a beta-1 selective adrenergic blocker, a class that lowers blood pressure and reduces renin release from the kidney.

Malignant hypertensive renal disease is a severe kidney complication of very high, uncontrolled blood pressure. Because bisoprolol lowers blood pressure, a link is plausible. However, the prediction is a computational output only. Acute malignant hypertension is usually managed with intravenous agents, and beta-blockers are not first-line treatment. The score therefore should not be read as evidence of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13419G | Bisoprolol generichealth | Tablet containing bisoprolol fumarate 2.5 mg | Not recorded in the local data |

This is a single-ingredient product and it is currently valid.

---

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples of those listed):
- **Moderate:** epinephrine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, methscopolamine, hyoscyamine, atropine, bupropion, morphine, acetohexamide, and several calcium salts (acetate, carbonate, citrate, gluconate, glubionate)
- **Minor:** acetylsalicylic acid, aluminium hydroxide, attapulgite

For warnings, contraindications and other safety information, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9994), but no clinical trials or publications address malignant hypertensive renal disease, so the evidence level is L5. Beta-blockers are also not first-line therapy for this acute condition.

**To proceed, the following is needed:**
- Clinical or observational studies of bisoprolol in malignant hypertension with renal involvement
- Mechanism of action data for bisoprolol
- Review of the TGA Product Information for warnings and contraindications
- Assessment of how bisoprolol would fit alongside standard intravenous management of malignant hypertension

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

