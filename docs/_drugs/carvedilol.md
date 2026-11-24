---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 4
monitor_inn: "Carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Carvedilol: predicted new indication malignant hypertensive renal disease (evidence level L5). In Australia: 7 PBS items (7 currently listed)"
---

# Carvedilol
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

## Carvedilol: non-selective β-blocker with α1-blocking activity → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Carvedilol is a non-selective β-blocker that also blocks α1-adrenergic receptors. The TxGNN model predicts it may be relevant to **malignant hypertensive renal disease**. The data compiled for this report contain **no clinical trials and no publications** on this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (7 of 7 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for carvedilol: "COREG is a racemic mixture in which nonselective β-adrenoreceptor blocking activity is present in the S(-) enantiomer and α1-adrenergic blocking activity is present in both R(+) and S(-) enantiomers at equal potency. COREG has no intrinsic sympathomimetic activity." ([DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39), label version 2026-07-31; accessed 2026-11-19.) Carvedilol is known as a non-selective β-blocker with α1-adrenergic blocking and antioxidant activity. The rationale for this prediction is extrapolated from that blood-pressure-lowering pharmacology and from reported renal and vascular protective effects.

The link is indirect. Malignant hypertensive renal disease is kidney damage driven by severe, uncontrolled blood pressure, so a drug that lowers blood pressure could plausibly help. No study retrieved for this report examined carvedilol in this condition. The high TxGNN score is probably inflated by the model's similarity to hypertension-related uses, so it should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 8255L | Vedilol 3.125 | Carvedilol | Tablet 3.125 mg | Valid |
| 8256M | Dilatrend 6.25 | Carvedilol | Tablet 6.25 mg | Valid |
| 8257N | Dilatrend 12.5 | Carvedilol | Tablet 12.5 mg | Valid |
| 8258P | Dilatrend 25 | Carvedilol | Tablet 25 mg | Valid |
| 13387N | Dilatrend 25 | Carvedilol | Tablet 25 mg | Valid |
| 13417E | Dilatrend 6.25 | Carvedilol | Tablet 6.25 mg | Valid |
| 13418F | Dilatrend 12.5 | Carvedilol | Tablet 12.5 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

Seven current PBS items are recorded, all single-ingredient oral tablets.

<!-- review:begin au-lic-20261117-carvedilol-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The single registered product is a valid, single-ingredient oral tablet." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-carvedilol-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen was completed and returned 100 interacting drugs, of which 20 are summarised here.
  - **Major**: epinephrine.
  - **Moderate**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, hyoscyamine, atropine, bupropion, morphine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate).
  - **Minor**: acetylsalicylic acid, aluminium hydroxide, attapulgite.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or publications for malignant hypertensive renal disease, so the evidence level is L5. The prediction score alone is not enough to support a repurposing decision.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic argument for this kidney condition
- Preclinical or clinical studies that directly address malignant hypertensive renal disease
- Review of TGA Product Information warnings and contraindications for a severely hypertensive, renally impaired population
- Review of the interaction profile, especially the major interaction with epinephrine

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

