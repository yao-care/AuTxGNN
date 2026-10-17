---
layout: default
title: Linagliptin
parent: Model Prediction Only (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Linagliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Linagliptin"
predicted_indications: ["opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy", "homozygous familial hypercholesterolemia"]
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Linagliptin is an oral DPP-4 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the ARTG record in the data compiled for this report has no indication text; this is taken from the knowledge graph) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 94.90% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Linagliptin is a member of the DPP-4 inhibitor class. Its efficacy in type 2 diabetes is established: it prolongs incretin activity and so enhances glucose-dependent insulin secretion.

On current information, the prediction is difficult to justify mechanistically. Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2). No established pathway connects DPP-4 inhibition to SHIP2 or skeletal development. The high score of 0.949 is a graph-based prediction only.

Other top-ranked predictions show the same pattern. They mostly reflect shared diabetes or metabolic phenotypes in the knowledge graph rather than a therapeutic rationale. Examples are thiamine-responsive dysfunction syndrome, stiff person syndrome, the localized lipodystrophies and homozygous familial hypercholesterolemia. The prediction for pancreatic agenesis is mechanistically unlikely to work, because linagliptin depends on existing beta cells.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for opsismodysplasia. Currently no related literature available for this indication.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13954K | Trajenta | Tablet 5 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: hypoglycaemia and pancreatitis are linked to linagliptin as contraindicated conditions.
- **Drug Interactions**: 100 interactions were identified. The sample reviewed was mostly Moderate, with a few Minor. Moderate examples include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol
  - Hormonal agents: estradiol, levonorgestrel, norethisterone, desogestrel, hydrocortisone
  - Others: hydrochlorothiazide, acetazolamide, benazepril, alpelisib, apalutamide, amobarbital, ethanol

  Minor examples include topical hydrocortisone and topical alclometasone.

Please refer to the TGA-approved Product Information (PI) for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature, and no plausible mechanistic link between DPP-4 inhibition and SHIP2-related skeletal dysplasia. Evidence is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for linagliptin (for example, from DrugBank)
- Product Information warnings and contraindications from the TGA record, as the safety data is incomplete
- Preclinical or mechanistic evidence linking DPP-4 inhibition to INPPL1/SHIP2 pathways or skeletal development
- Review of lower-ranked predictions in which the diabetes link is more direct, since the top-ranked ones appear to be graph artefacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

