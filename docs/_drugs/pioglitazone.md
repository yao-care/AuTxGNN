---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Pioglitazone"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitising medicine originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia** (a rare skeletal dysplasia), but there are currently **0 clinical trials** and **0 publications** specific to this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pioglitazone is generally recognised as a PPAR-gamma agonist (a thiazolidinedione insulin sensitiser), and its efficacy in type 2 diabetes is well established.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2), a negative regulator of PI3K/insulin signalling. A link to pioglitazone through insulin-signalling pathways is conceivable, but no mechanistic link is supported by the data compiled for this report. The high TxGNN score is a graph-based prediction only and should be read as a hypothesis, not evidence of benefit.

Other predicted indications were also reviewed, and all remain at evidence level L5 with a "Hold" recommendation:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 99.50% | Possible immunomodulatory rationale; hypothetical |
| 3 | Focal stiff limb syndrome | 99.50% | Same score as the classic form; shared graph-based prediction |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | Associated with diabetes, but pioglitazone does not address the thiamine transport defect |
| 5 | Drug-induced localised lipodystrophy | 99.30% | PPAR-gamma adipogenesis is plausible; withdrawing the causative agent is usual management |
| 6 | Centrifugal lipodystrophy | 99.26% | Plausible but unverified; often self-limiting |
| 7 | Pressure-induced localised lipoatrophy | 99.24% | Mechanically induced and localised |
| 8 | Idiopathic localised lipodystrophy | 99.19% | No clinical data supplied |
| 9 | Pancreatic agenesis | 99.18% | Retrieved papers concern type 2 diabetes, not this disease; mechanistically unlikely |
| 10 | Autoimmune oophoritis | 98.06% | Speculative immunomodulatory rationale |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature specific to opsismodysplasia is available. The only publications retrieved were for rank 9 (pancreatic agenesis), and they concern type 2 diabetes rather than that disease, so they are not presented as supporting evidence.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13898L | ARX-PIOGLITAZONE | Tablet 15 mg (as hydrochloride) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, congestive heart failure, adrenocortical insufficiency/Addison disease, thymus gland disease, infectious disease, and a range of pituitary hormone deficiencies and hypogonadotropic hypogonadism conditions (including Kallmann syndrome and Sheehan syndrome). These come from graph associations and should be verified against the Product Information.
- **Drug Interactions**: 100 interactions were identified. Examples at Moderate level include abiraterone, acetazolamide, hydrochlorothiazide, hydrocortisone, salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine, alpelisib and ethanol. Minor examples include nifedipine, ethinylestradiol and lipoic acid.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for opsismodysplasia is based solely on a graph-model score, with no clinical trials, no disease-specific literature and no identified mechanistic link. Evidence is at level L5.

**To proceed, the following is needed:**
- Mechanism of action data for pioglitazone, and a plausible biological link to INPPL1/SHIP2 signalling
- Disease-specific preclinical or clinical evidence
- TGA Product Information warnings and contraindications, including the approved indication text for ARTG 13898L
- A safety review for the paediatric population, given that opsismodysplasia is a childhood-onset skeletal disorder and the KG-derived contraindications include heart failure, liver and kidney disease
- Consideration of better-supported candidates, such as lipodystrophy-type conditions, where a PPAR-gamma rationale is more biologically plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

