---
layout: default
title: Sitagliptin
parent: Model Prediction Only (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sitagliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Sitagliptin"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Sitagliptin
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

# Sitagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Sitagliptin is a DPP-4 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia** (a rare skeletal dysplasia), but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on network-based modelling alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.87% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Sitagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor, a class that raises incretin activity and improves glycaemic control in type 2 diabetes. Its efficacy in that condition is established.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency), which affect PI3K/insulin signalling and endochondral ossification. The only conceivable overlap with type 2 diabetes is insulin-signalling biology, and this is not a plausible mechanistic link to DPP-4 inhibition and incretin degradation. The high score (0.989) is a network-based prediction only, with no supporting trials or literature. The model's rank of 11,305 for this prediction also suggests that the score alone should be interpreted cautiously.

The other nine predictions in the data (for example stiff person syndrome, lipodystrophy subtypes, pancreatic agenesis and autoimmune oophoritis) are likewise L5, with no trials and weak or speculative mechanistic links. None is better supported than opsismodysplasia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13871C | Sitagliptin Sandoz Pharma | Tablet 100 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

Safety information was drawn from knowledge-graph contraindication edges and drug interaction data, not from product label text.

- **Knowledge-graph contraindication signals** (disease associations, not label text): pancreatitis, kidney disease, liver disease, gallbladder disease, adrenocortical insufficiency/Addison disease, infectious disease, thymus gland disease, and a broad group of pituitary hormone deficiency and hypogonadotropic hypogonadism conditions.
- **Drug interactions**: 100 interactions were identified. Those shown in the data are mostly Moderate, with a few Minor. Moderate examples include:
  - sympathomimetics and bronchodilators (phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol)
  - corticosteroids (hydrocortisone, triamcinolone)
  - hormonal agents (estradiol, levonorgestrel, norethisterone, desogestrel)
  - others (hydrochlorothiazide, acetazolamide, benazepril, aripiprazole, alpelisib, apalutamide, ethanol)
  
  Minor examples are topical hydrocortisone and topical alclometasone.
- **Pancreatitis**: a case report in the compiled literature (PMID 32337116) describes sitagliptin-induced pancreatitis after long-term use. This is relevant to any new use.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature support (evidence level L5). No plausible mechanistic link exists between DPP-4 inhibition and INPPL1/SHIP2-related skeletal dysplasia.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), for example from DrugBank
- TGA Product Information warnings and contraindications, to complete safety screening
- Preclinical evidence (for example, an INPPL1-deficient model) showing a biological effect of DPP-4 inhibition on the disease
- Consideration of whether any other predicted indication has a stronger rationale, since none has clinical evidence at present
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

