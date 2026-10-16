---
layout: default
title: Moxonidine
parent: Model Prediction Only (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Moxonidine: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension (essential hypertension…"
---

# Moxonidine
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

# Moxonidine: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Moxonidine is a centrally acting antihypertensive, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no supporting publications** were found for this prediction.
The prediction rests on the model's graph-based score alone and has no known pharmacological basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (essential hypertension, hypertensive disorder). The ARTG entry in the compiled data has no indication text. |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Moxonidine is generally described as an imidazoline I1 receptor / alpha-2 adrenergic agonist that lowers sympathetic outflow. Its efficacy in hypertension is established. Pharmacology data confirm that it binds the alpha-2A, alpha-2B and alpha-2C adrenoceptors.

No mechanistic link to this new indication has been established. Hypotrichosis simplex of the scalp is a genetic hair-follicle developmental disorder. No known pathway connects central sympatholytic activity to it. Unlike minoxidil, moxonidine does not act through direct vasodilation of the scalp.

The high TxGNN score is a graph-based prediction only. It likely reflects shared neighbouring nodes in the knowledge graph rather than pharmacology. Other top-ranked predictions are also hair disorders (congenital hypotrichosis milia, diffuse alopecia areata, alopecia). None has trial or mechanistic support.

Predictions with a more plausible rationale are listed below.

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.67% | L4 | Indirect link via sympathetic overactivity. Malignant hypertension usually needs rapid parenteral blood pressure control, not an oral centrally acting agent. |
| Malignant renovascular hypertension | 99.67% | L4 | Sympathetic inhibition is relevant, but no disease-specific data were provided. |
| Primary hereditary glaucoma | 99.54% | L5 | Class-level rationale from alpha-2 agonists lowering intraocular pressure. No moxonidine-specific data. |

The pulmonary hypertension predictions and Braddock syndrome appear to reflect name similarity with "hypertension" and are not supported by mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For the fourth-ranked prediction (alopecia), one publication was linked:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/) | 2024 | Case report | Georgian Med News | Case of Graham-Little-Piccardi-Lasseur syndrome (a lichenoid scarring alopecia) in a 64-year-old woman. Based on its title and the limited abstract, it does not evaluate moxonidine and is not evidence for the drug. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13552G | Moxonidine GX | Tablet 400 micrograms | Not recorded in the compiled data |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. The warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no relevant literature and no plausible mechanistic link. It is supported only by the model score (Evidence Level L5). The one linked publication does not involve moxonidine.

**To proceed, the following is needed:**
- A mechanistic hypothesis connecting alpha-2 / I1-imidazoline agonism to hair-follicle biology, followed by preclinical testing
- Detailed mechanism of action data for moxonidine
- The TGA Product Information, including warnings and contraindications, and the approved indication text for the ARTG entry
- If a repurposing direction is pursued, consider a better supported option, such as the hypertension-related predictions (malignant renovascular hypertension) or glaucoma, with a literature review and a preclinical or early clinical plan
- A review of route compatibility: only an oral tablet is registered in Australia, and a topical or ocular route would need separate formulation and safety work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

