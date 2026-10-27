---
layout: default
title: Alogliptin
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alogliptin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Alogliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Alogliptin
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

## Alogliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Alogliptin is a DPP-4 inhibitor, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **no clinical trials** and **no publications** specific to this indication, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Alogliptin belongs to the DPP-4 inhibitor class, and its efficacy in type 2 diabetes is established. A mechanistic link to stiff person syndrome has not been demonstrated.

Stiff person syndrome is an autoimmune neurological disorder, typically involving anti-GAD65 antibodies and impaired GABAergic signalling. DPP-4 (CD26) has a role in T-cell activation, which offers a speculative immunomodulatory connection at best.

A more likely explanation for the high score is knowledge-graph proximity. Stiff person syndrome frequently co-occurs with autoimmune diabetes (anti-GAD65), so the model may be picking up disease association rather than a true therapeutic effect. The same score was given to the related focal stiff limb syndrome, which supports this interpretation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For context, the other predicted indications also have very little support. Only pancreatic agenesis (rank 6, score 96.5%) returned any publications, and these concern type 2 diabetes rather than that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20859539](https://pubmed.ncbi.nlm.nih.gov/20859539/) | 2010 | Review | Vascular Health and Risk Management | Pioglitazone plus alogliptin combination therapy in type 2 diabetes |
| [22071236](https://pubmed.ncbi.nlm.nih.gov/22071236/) | 2011 | Review | Clinical Therapeutics | Tolerability of DPP-4 inhibitors |
| [21205126](https://pubmed.ncbi.nlm.nih.gov/21205126/) | 2011 | Preclinical (mouse) | Diabetes, Obesity & Metabolism | Chronic alogliptin and beta-cell function in diabetic mice |

Pancreatic agenesis is biologically implausible as a target, since alogliptin depends on functional beta cells.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13897K | Nesina | Tablet 6.25 mg (as benzoate) | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Most listed are of moderate severity, including:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol
  - Diuretics: furosemide, hydrochlorothiazide, acetazolamide
  - Corticosteroids: hydrocortisone
  - Others: ethinylestradiol, ethanol, fosinopril, fosphenytoin, gemifloxacin, fosamprenavir, acetohexamide, alpelisib, aloe vera leaf
  - Minor interactions: topical hydrocortisone and topical alclometasone

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (98.01%), with no trials or literature for stiff person syndrome. The mechanistic link is speculative and may reflect shared association with autoimmune diabetes rather than a therapeutic effect.

**To proceed, the following is needed:**
- Mechanism of action data for alogliptin
- Preclinical or mechanistic evidence for DPP-4 inhibition in stiff person syndrome or anti-GAD65 autoimmunity
- Review of TGA Product Information for warnings and contraindications
- Approved indication text for the ARTG entry
- Any case reports or observational data in patients with both diabetes and stiff person syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

