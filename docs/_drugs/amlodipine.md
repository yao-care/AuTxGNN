---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 9
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-17
description: "Amlodipine: predicted new indication brain stem infarction (evidence level L5). In Australia: at least 20 PBS items"
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amlodipine: dihydropyridine calcium channel blocker → brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is an oral dihydropyridine calcium channel blocker that is marketed in Australia. The TxGNN model predicts it may be useful for **brain stem infarction**, but the data compiled for this report contain **no clinical trials and no publications** that study this condition directly, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | brain stem infarction |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for amlodipine: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), label version 2026-09-28; accessed 2026-11-19.) Amlodipine is a calcium channel blocker, a class that relaxes vascular smooth muscle by limiting calcium entry into the cells. Brain stem infarction is an ischaemic cerebrovascular event, so a drug acting on vascular tone and blood pressure could plausibly be relevant to it.

This is a general pharmacological argument, not evidence for this specific condition. No study in the compiled data tests amlodipine in brain stem infarction, and the model score has not been confirmed by any trial or publication. The brain stem is a small, anatomically distinct region, so findings from other cerebrovascular conditions cannot simply be assumed to apply.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Amlodipine is marketed in Australia. The local records show at least 20 current PBS items, all oral tablets, including single-ingredient amlodipine and combinations with perindopril, atorvastatin, valsartan, olmesartan and telmisartan. The approved indication is not recorded in the local data.

<!-- review:begin au-lic-20261117-amlodipine-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The local records show one valid single-ingredient licence, for an oral tablet (5 mg, as besilate)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-amlodipine-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. The 20 shown in the compiled data are all graded Moderate, including:
  - corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone)
  - aprepitant
  - acetylsalicylic acid
  - bupropion
  - clarithromycin
  - clotrimazole
  - SGLT2 inhibitors (canagliflozin, dapagliflozin)
  - several calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate, phosphate and others)

Warning and contraindication text from the TGA-approved Product Information was not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no trial or publication studies amlodipine in brain stem infarction. The evidence level is therefore L5 (model prediction only), and there is nothing to support moving forward.

**To proceed, the following is needed:**
- Clinical or observational studies that directly address brain stem infarction, ideally with a specific focus on amlodipine
- Detailed mechanism of action data
- Review of the TGA-approved Product Information for warnings, contraindications and the registered indication
- A safety plan covering hypotension risk in acute ischaemic stroke and the moderate-level interactions noted above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

