---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metformin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Metformin
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

# Metformin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Metformin is an oral antidiabetic drug, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but this is a graph-based prediction only, with **no clinical trials** and **no publications** directly supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; no approved indication text is available for the registered product) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metformin is a long-established oral antidiabetic, and its efficacy in type 2 diabetes is well proven. It is generally understood to act through AMPK activation and suppression of hepatic glucose production, but this was not part of the data compiled for this report.

The mechanistic link to the predicted indication is weak. Stiff person syndrome is an autoimmune neurological disorder typically associated with GAD65 antibodies, and there is no clear connection to metformin's metabolic actions. The high score most likely reflects the frequent co-occurrence of diabetes and GAD-antibody autoimmunity in the knowledge graph, which is probably a graph artifact rather than a true therapeutic signal.

The second-ranked prediction, focal stiff limb syndrome, has an identical score (99.45%). This suggests the two share a graph neighbourhood as variants of the same disease family, rather than being independent signals.

Other lower-ranked predictions, none with direct evidence, include opsismodysplasia, thiamine-responsive dysfunction syndrome, several localised lipodystrophies, pancreatic agenesis and homozygous familial hypercholesterolemia. Of these, only homozygous familial hypercholesterolemia has any preclinical signal. A 1988 in vitro study showed metformin reduced cholesterol metabolism in cultured human fibroblasts. This is weak support (L4), and it would not be expected to compensate for absent LDL receptor function.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13847T | Diaformin XR 1000 | Extended-release tablet containing metformin hydrochloride 1 g | Not available in the data compiled for this report |

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
The prediction rests only on a graph-based score. There are no clinical trials or relevant publications, and no plausible mechanistic link between metformin and stiff person syndrome. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for metformin
- Product Information warnings and contraindications from the TGA-approved PI
- A targeted literature search for metformin in stiff person syndrome and GAD-antibody-associated disease
- A mechanistic rationale beyond the GAD-antibody and diabetes co-occurrence in the knowledge graph
- If a lower-ranked candidate is preferred, such as homozygous familial hypercholesterolemia, further preclinical work to move beyond the single 1988 in vitro study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

