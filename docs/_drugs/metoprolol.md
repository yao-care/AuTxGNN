---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 6
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-11-17
description: "Metoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Australia: 11 PBS items (11 currently listed)"
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Metoprolol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Metoprolol is a beta-blocker. The Australian licence records compiled for this report do not state an approved indication. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (11 of 11 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metoprolol: "Metoprolol is a beta 1 -selective (cardioselective) adrenergic receptor blocking agent. This preferential effect is not absolute, however, and at higher plasma concentrations, metoprolol also inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a), label version 2026-03-03; accessed 2026-11-19.) Based on general pharmacology, metoprolol is a beta-1 selective blocker that lowers heart rate, cardiac output and renin release. This is the usual basis for its blood pressure-lowering effect.

Malignant hypertensive renal disease is a severe form of hypertension with kidney damage. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The new indication is largely an extension of an existing hypertension relation to a severe, end-organ-damage presentation. In acute settings this presentation is typically managed with intravenous agents, so the oral metoprolol products registered in Australia may not suit it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13420H | Metrol-XL 190 | Tablet 190 mg (controlled release) | Not stated in the records compiled |
| ARTG 1324Q | Metoprolol Sandoz | Tablet containing metoprolol tartrate 50 mg | Not stated in the records compiled |

All eleven current PBS items are single-ingredient oral products (metoprolol succinate and metoprolol tartrate).

<!-- review:begin au-lic-20261117-metoprolol-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Both entries are single-ingredient oral products and both are currently valid." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-metoprolol-1 -->

## Safety Considerations

TGA-approved Product Information (PI) warnings and contraindications were not available in the data compiled. Please refer to the PI for authoritative safety information.

- **Contraindication relations recorded in the knowledge graph** (not label text): these include diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, liver disease, pancreatitis, myasthenia gravis, phaeochromocytoma, psoriasis, systemic lupus erythematosus, gout, hepatic encephalopathy, anuria, anxiety and neurotic disorders, and several metabolic disorders (hypercalcaemia, hyperparathyroidism, potassium deficiency).
- **Drug Interactions:** The interaction screen returned 100 records. Most of those shown are Moderate, including epinephrine, bupropion, cimetidine, morphine, systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, glycopyrronium), and some glucose-lowering drugs (canagliflozin, dapagliflozin, chlorpropamide). Acetylsalicylic acid and magnesium oxide were Minor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or publications for this disease, so the evidence level is L5. Malignant hypertensive renal disease is usually an acute, high-risk presentation managed with intravenous therapy, and the registered Australian products are oral tablets.

**To proceed, the following is needed:**
- Clinical or observational studies that directly examine metoprolol in malignant hypertensive renal disease
- Mechanism of action data and a clearer mechanistic link to this condition
- TGA Product Information warnings and contraindications, to complete the safety review
- Confirmation of the approved indication wording for the two ARTG entries
- An assessment of route and formulation suitability for an acute severe hypertension setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

