---
layout: default
title: Saxagliptin
parent: Model Prediction Only (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Saxagliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Saxagliptin"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Saxagliptin
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

# Saxagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Saxagliptin is an oral DPP-4 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. This is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Saxagliptin belongs to the DPP-4 inhibitor class, which prolongs the action of incretin hormones and helps lower blood glucose in type 2 diabetes.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency), which affects PI3K/insulin signalling. The only apparent link to saxagliptin is proximity to insulin and glucose pathways in the knowledge graph.

No direct mechanistic connection has been established. The high score most likely reflects knowledge-graph proximity rather than a validated biological rationale, so this prediction should be treated with caution.

**Other predicted indications (all L5, Hold):**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 97.66% | Association via GAD autoimmunity and diabetes; no demonstrated DPP-4 effect |
| 3 | Focal stiff limb syndrome | 97.66% | Variant of the above; same associative link only |
| 4 | Thiamine-responsive dysfunction syndrome | 97.50% | Diabetes phenotype likely drives the prediction; standard care is thiamine and insulin |
| 5 | Drug-induced localised lipodystrophy | 96.35% | Linked to injected therapies; no rationale for an oral DPP-4 inhibitor |
| 6 | Pancreatic agenesis | 96.24% | Mechanistically implausible, as saxagliptin relies on residual beta-cell function |
| 7 | Centrifugal lipodystrophy | 96.12% | Unclear aetiology; graph similarity only |
| 8 | Pressure-induced localised lipoatrophy | 96.02% | Mechanically induced; no plausible mechanism |
| 9 | Idiopathic localised lipodystrophy | 95.75% | Unknown cause; no evidence |
| 10 | Autoimmune oophoritis | 85.22% | Speculative immunomodulation via CD26/DPP-4; no clinical data |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for opsismodysplasia, the top predicted indication.

For reference, one publication was linked to a lower-ranked prediction (pancreatic agenesis). It is a general review and does not support that indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22071236](https://pubmed.ncbi.nlm.nih.gov/22071236/) | 2011 | Review | Clinical Therapeutics | Review of the tolerability of DPP-4 inhibitors in type 2 diabetes; no data on pancreatic agenesis |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10128C | Onglyza | Tablet 2.5 mg (as hydrochloride) | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries; 20 are shown in the data compiled for this report. Most are rated Moderate, and a few are Minor. Examples include:
  - Moderate: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, nifedipine, hydrochlorothiazide, acetazolamide, amiodarone, benazepril, estradiol, ethinylestradiol, levonorgestrel, hydrocortisone, alpelisib, amobarbital, ethanol, abametapir (topical)
  - Minor: topical hydrocortisone, topical alclometasone
- **Knowledge-graph contraindication signals** (model-derived, not label text): kidney disease, liver disease, gallbladder disease, pituitary hormone deficiency conditions, hypogonadotropic hypogonadism, Kallmann syndrome, adrenocortical insufficiency, Addison disease, thymus gland disease, infectious disease and substance abuse/dependence. These must be verified against the approved label.

Please refer to the TGA-approved Product Information (PI) for confirmed warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (Evidence Level L5). There are no clinical trials or relevant publications, and no plausible mechanistic link between DPP-4 inhibition and opsismodysplasia has been established.

**To proceed, the following is needed:**
- Detailed mechanism of action data for saxagliptin
- A mechanistic rationale linking DPP-4 inhibition to INPPL1/SHIP2 pathway biology, supported by preclinical data
- TGA Product Information review for warnings, contraindications and approved indication text
- Any relevant clinical or preclinical studies in opsismodysplasia, or a re-evaluation of other candidates with stronger rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

