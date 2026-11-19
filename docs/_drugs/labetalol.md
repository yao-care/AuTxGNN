---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Labetalol: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Labetalol
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

## Labetalol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Labetalol is a combined alpha-1/beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but this is largely an extension of its existing indication.
Evidence is limited to **0 clinical trials** and **1 publication** (a 1981 case report), so support is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for labetalol: "Labetalol has both competitive alpha1-adrenergic blocking and competitive beta-adrenergic blocking activity. In man, the ratio of alpha- to beta-blockade has been estimated to be approximately 1:7 following intravenous administration." ([DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55), label version 2025-12-19; accessed 2026-11-19.) Based on known pharmacology, labetalol combines alpha-1 and beta-adrenergic blockade. It lowers blood pressure by reducing systemic vascular resistance and heart rate, and it is already used for severe hypertension and hypertensive emergencies.

Malignant renovascular hypertension is a severe hypertensive state, so blood pressure lowering by this mechanism is plausibly relevant. The new indication overlaps heavily with the approved use, so this is closer to an extension of the original indication than true repurposing. No disease-specific data were found.

Other high-scoring predictions have a weaker rationale. Pulmonary hypertension is unlikely to benefit, because beta-blockade may harm right-ventricular function. The high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Medical Journal of Australia | A 20-year-old man developed malignant hypertension and renal arteritis after hallucinogenic drug use. Arteritis resolved with prednisone. Minoxidil and labetalol were useful for initial blood pressure control. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13887X | Presolol 100 | Tablet containing labetalol hydrochloride 100 mg (oral) | Not stated in the data compiled |

## Safety Considerations

- **Disease contraindications (knowledge graph, not label text):** The knowledge graph lists many conditions where labetalol is contraindicated or cautioned. Notable ones include:
  - Cardiorespiratory: atrioventricular block, pulmonary emphysema, bronchial disease, hypotensive disorder
  - Hepatic: liver failure, liver disease, hepatic coma and encephalopathy
  - Renal and metabolic: kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, gout
  - Other: systemic lupus erythematosus, pancreatitis, intraoperative floppy iris syndrome
- **Drug Interactions:** 100 interactions were recorded. Those shown include:
  - **Major:** epinephrine, dolasetron
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine, dicyclomine), morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide and calcium salts
  - **Minor:** acetylsalicylic acid, magnesium oxide

Please also refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Labetalol is plausibly useful in malignant renovascular hypertension, but this is essentially an extension of its approved antihypertensive use. The only supporting evidence is a single 1981 case report, with no registered trials and no disease-specific efficacy data.

**To proceed, the following is needed:**
- Product Information (PI) warnings, contraindications and approved indication text for the ARTG entry
- Mechanism of action data
- Clinical data specific to renovascular or malignant hypertension, such as guideline positioning and comparative studies
- A review of the knowledge-graph contraindications against the target population, particularly renal disease and anuria, which are relevant to hypertensive renal disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

