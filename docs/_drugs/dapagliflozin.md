---
layout: default
title: Dapagliflozin
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dapagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Dapagliflozin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Dapagliflozin
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

# Dapagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Dapagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but there are currently **no clinical trials** and **no publications** supporting this prediction.
This is a computational prediction only and should be treated as hypothesis-generating.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the ARTG entry in the data compiled for this report has no approved indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Dapagliflozin is known to be an SGLT2 inhibitor that lowers blood glucose by increasing urinary glucose excretion, and its efficacy in type 2 diabetes is established.

No plausible mechanistic link has been established between SGLT2 inhibition and stiff person syndrome. Stiff person syndrome is an autoimmune neurological disorder, typically involving anti-GAD65 antibodies and impaired GABAergic signalling. The data compiled for this report contains no supporting evidence for a link.

The prediction appears to be driven by proximity in the model's disease graph. The score is identical for focal stiff limb syndrome (98.20%), which suggests shared graph neighbours rather than independent evidence. A high score alone is not sufficient to support clinical use.

### Other Predicted Indications (for context)

All other predictions are also at low evidence levels and are on **Hold**.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Focal stiff limb syndrome | 98.20% | L5 | Same score as rank 1; no evidence |
| 3 | Opsismodysplasia | 98.06% | L5 | Rare skeletal dysplasia; no link supported |
| 4 | Thiamine-responsive dysfunction syndrome | 98.03% | L5 | Diabetes is a feature of some forms, so the link is speculative |
| 5 | Drug-induced localised lipodystrophy | 97.03% | L5 | Hypothetical metabolic association |
| 6 | Centrifugal lipodystrophy | 96.90% | L5 | Mainly dermatological; unverified |
| 7 | Pressure-induced localised lipoatrophy | 96.82% | L5 | No plausible systemic mechanism |
| 8 | Idiopathic localised lipodystrophy | 96.67% | L5 | Clustered with other lipodystrophy subtypes |
| 9 | Pancreatic agenesis | 96.59% | L4 | Preclinical and case-report literature only, with no direct efficacy evidence |
| 10 | Autoimmune oophoritis | 90.43% | L5 | Lowest score; speculative |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For context, the two publications below were retrieved for the rank 9 prediction (pancreatic agenesis). They provide indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33559163](https://pubmed.ncbi.nlm.nih.gov/33559163/) | 2021 | Preclinical (animal) | J Cell Physiol | Dapagliflozin ameliorated pancreatic injury and activated kidney autophagy via AMPK/mTOR signalling in obese rats |
| [42369057](https://pubmed.ncbi.nlm.nih.gov/42369057/) | 2026 | Case report | Front Endocrinol | Two cases of HNF1B-MODY (MODY-5), a rare diabetes form with multisystem features; does not demonstrate dapagliflozin efficacy |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10011X | Forxiga | Tablet 10 mg (as propanediol monohydrate) | Not available in the data compiled for this report |

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs in total, and the 20 shown here are mainly of moderate severity. Examples include:
- Diuretics and antihypertensives (furosemide, hydrochlorothiazide, acetazolamide, nifedipine, aliskiren, fosinopril, acebutolol, alfuzosin)
- Sympathomimetics and bronchodilators (phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol)
- Corticosteroids (hydrocortisone, moderate; topical hydrocortisone and topical alclometasone, minor)
- Others (ethanol, levonorgestrel, fosamprenavir, gemifloxacin)

**Considerations specific to this report:** In the pancreatic agenesis context, glucose-lowering could only be considered for the resulting diabetes, and SGLT2 inhibitors carry a ketoacidosis risk in insulin-deficient patients.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-derived only (L5), with no clinical trials or publications and no established mechanistic link between SGLT2 inhibition and stiff person syndrome. The identical score for focal stiff limb syndrome suggests the result reflects graph structure rather than independent evidence.

**To proceed, the following is needed:**
- Mechanism of action data for dapagliflozin, and a mechanistic rationale for stiff person syndrome (for example, links to GABAergic or autoimmune pathways)
- Preclinical or literature evidence in relevant models
- TGA Product Information, to complete safety screening (warnings, contraindications and approved indication text)
- Assessment of whether any other predicted indication has stronger evidence than this top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

