---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: predicted new indication Classic stiff person syndrome (evidence level L5). In Australia: at least 20 PBS items"
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Metformin: Classic stiff person syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is an oral antidiabetic drug, originally used to treat type 2 diabetes mellitus.
The TxGNN model (deep learning) predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **no clinical trials** and **no publications** directly supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metformin: "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), label version 2026-09-21; accessed 2026-11-19.) Metformin is a long-established oral antidiabetic, and its efficacy in type 2 diabetes is well proven. It is generally understood to act through AMPK activation and suppression of hepatic glucose production, but this was not part of the data compiled for this report.

The mechanistic link to the predicted indication is weak. Stiff person syndrome is an autoimmune neurological disorder typically associated with GAD65 antibodies, and there is no clear connection to metformin's metabolic actions. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The second-ranked prediction, focal stiff limb syndrome, has an identical score (0.9945). The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The two are variants of the same disease family, so they are probably not independent signals.

Other lower-ranked predictions, none with direct evidence, include opsismodysplasia, thiamine-responsive dysfunction syndrome, several localised lipodystrophies, pancreatic agenesis and homozygous familial hypercholesterolemia. A 1988 in vitro study showed metformin reduced cholesterol metabolism in cultured human fibroblasts. This is weak support (L4), and it would not be expected to compensate for absent LDL receptor function.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1801T | APX-METFORMIN | Metformin | Tablet containing metformin hydrochloride 850 mg | Valid |
| 2430X | Metformin GH | Metformin | Tablet containing metformin hydrochloride 500 mg | Valid |
| 3439B | Diaformin XR 1000 | Metformin | Tablet (extended release) containing metformin hydrochloride 1 g | Valid |
| 8607B | Metformin GH | Metformin | Tablet containing metformin hydrochloride 1 g | Valid |
| 9435N | APO-Metformin XR 500 | Metformin | Tablet (extended release) containing metformin hydrochloride 500 mg | Valid |
| 10032B | Nesina Met 12.5/850 | Alogliptin + metformin | Tablet containing 12.5 mg alogliptin (as benzoate) with 850 mg metformin hydrochloride | Valid |
| 10033C | Nesina Met 12.5/500 | Alogliptin + metformin | Tablet containing 12.5 mg alogliptin (as benzoate) with 500 mg metformin hydrochloride | Valid |
| 10035E | Nesina Met 12.5/1000 | Alogliptin + metformin | Tablet containing 12.5 mg alogliptin (as benzoate) with 1 g metformin hydrochloride | Valid |
| 10038H | Trajentamet | Linagliptin + metformin | Tablet containing 2.5 mg linagliptin with 500 mg metformin hydrochloride | Valid |
| 10044P | Trajentamet | Linagliptin + metformin | Tablet containing 2.5 mg linagliptin with 1000 mg metformin hydrochloride | Valid |
| 10045Q | Trajentamet | Linagliptin + metformin | Tablet containing 2.5 mg linagliptin with 850 mg metformin hydrochloride | Valid |
| 10048W | Kombiglyze XR 2.5/1000 | Saxagliptin + metformin | Tablet (modified release) containing 2.5 mg saxagliptin (as hydrochloride) with 1000 mg metformin hydrochloride | Valid |
| 10051B | Kombiglyze XR 5/1000 | Saxagliptin + metformin | Tablet (modified release) containing 5 mg saxagliptin (as hydrochloride) with 1000 mg metformin hydrochloride | Valid |
| 10055F | Kombiglyze XR 5/500 | Saxagliptin + metformin | Tablet (modified release) containing 5 mg saxagliptin (as hydrochloride) with 500 mg metformin hydrochloride | Valid |
| 10089B | Janumet XR | Sitagliptin + metformin | Tablet (modified release) containing 100 mg sitagliptin with 1000 mg metformin hydrochloride | Valid |
| 13847T | Diaformin XR 1000 | Metformin | Tablet (extended release) containing metformin hydrochloride 1 g | Valid |
| 13899M | APO-Metformin XR 500 | Metformin | Tablet (extended release) containing metformin hydrochloride 500 mg | Valid |
| 13952H | APX-METFORMIN | Metformin | Tablet containing metformin hydrochloride 850 mg | Valid |
| 13976N | Metformin GH | Metformin | Tablet containing metformin hydrochloride 500 mg | Valid |
| 14056T | Metformin GH | Metformin | Tablet containing metformin hydrochloride 1 g | Valid |

The table shows 20 of 58 PBS items for this ingredient in these data (items on the current PBS Schedule first).

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease edges, not label text): liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, congestive heart failure, adrenocortical insufficiency, and a range of pituitary hormone deficiency and hypogonadotropic hypogonadism conditions.
- **Drug Interactions** (100 interactions identified; selected examples from the first 20 reviewed):
  - **Major:** acetazolamide, ethanol
  - **Moderate:** dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acetohexamide
  - **Minor:** acarbose and topical corticosteroids

Please refer to the TGA-approved Product Information (PI) for full label warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or relevant publications, and no plausible mechanistic link between metformin and stiff person syndrome. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for metformin
- Product Information warnings and contraindications from the TGA-approved PI
- A targeted literature search for metformin in stiff person syndrome and GAD-antibody-associated disease
- A mechanistic rationale beyond the similarities the TxGNN model (deep learning) learned between related diseases, such as GAD-antibody autoimmunity and diabetes

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

