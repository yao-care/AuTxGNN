---
layout: default
title: Semaglutide
parent: Model Prediction Only (L5)
nav_order: 668
evidence_level: L5
indication_count: 10
---

# Semaglutide
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

# Semaglutide: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Semaglutide is a GLP-1 receptor agonist, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph indication data; the ARTG entry has no indication text recorded) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Semaglutide is a GLP-1 receptor agonist whose efficacy in type 2 diabetes is established. No direct mechanism links GLP-1 receptor agonism to the pathophysiology of stiff person syndrome (SPS).

SPS is an autoimmune neurological disorder, often with anti-GAD65 antibodies, and is associated with type 1 diabetes and other autoimmune diseases. This comorbidity overlap may partly explain the graph-based prediction. The identical score for focal stiff limb syndrome (a variant in the same spectrum) suggests the signal comes from a shared disease-node neighbourhood rather than a drug-specific mechanism.

Other predictions in this set (all L5, all Hold) are also unsupported by clinical evidence:

| Predicted Indication | Score | Comment |
|------|------|------|
| Focal stiff limb syndrome | 98.64% | Same signal as classic SPS; no plausible direct GLP-1 mechanism |
| Opsismodysplasia | 98.59% | INPPL1/SHIP2 insulin-signalling link is hypothesis-level only |
| Thiamine-responsive dysfunction syndrome | 98.58% | Diabetes is a feature; semaglutide would at most treat hyperglycaemia symptomatically |
| Drug-induced localised lipodystrophy | 97.66% | Weight-reducing agent could plausibly worsen fat loss; injection-site lipodystrophy is a known concern with injectables |
| Centrifugal lipodystrophy | 97.56% | Likely reflects lipodystrophy-category neighbours in the graph |
| Pressure-induced localised lipoatrophy | 97.49% | No recognised GLP-1 pathway involvement |
| Idiopathic localised lipodystrophy | 97.35% | Same lipodystrophy-cluster signal |
| Pancreatic agenesis | 97.31% | Efficacy mechanistically implausible, as GLP-1 action requires functional beta cells |
| Autoimmune oophoritis | 95.05% | Some anti-inflammatory and reproductive-endocrine effects of GLP-1 RAs, but no direct evidence |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For context, three publications were retrieved for the lower-ranked prediction of pancreatic agenesis. They are indirect and relate to pancreatic safety only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24608440](https://pubmed.ncbi.nlm.nih.gov/24608440/) | 2014 | Preclinical (animal histopathology) | Diabetes | Liraglutide and semaglutide showed no histopathological effects on the pancreas in non-human primates |
| [40805859](https://pubmed.ncbi.nlm.nih.gov/40805859/) | 2025 | Review / clinical assessment | Healthcare (Basel) | Pre-treatment assessment of semaglutide users, with concerns about thyroid and pancreatic disorders |
| [38735240](https://pubmed.ncbi.nlm.nih.gov/38735240/) | 2024 | Preclinical | Psychiatry Research | Serotonin/GLP-1 circuitry in a rodent model of psychiatric and metabolic dysfunction |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12075M | Ozempic | Solution for injection 4 mg in 3 mL pre-filled pen | Not recorded in the data compiled for this report |

## Safety Considerations

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction screen returned 100 potential interactions. Most of those shown are Moderate, with a few Minor. Examples include:
- **Moderate:** phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, acetazolamide, hydrochlorothiazide, hydrocortisone, triamcinolone, estradiol, ethinylestradiol, levonorgestrel, norethisterone, alpelisib, aripiprazole, asenapine, asparaginase, ethanol
- **Minor:** topical hydrocortisone, topical alclometasone

Many of these (for example corticosteroids, sympathomimetics and beta-agonists) may affect glycaemic control, so a clinician should review the full list before any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no clinical trials or literature, and no plausible mechanism links GLP-1 receptor agonism to stiff person syndrome. The high score likely reflects shared graph neighbours such as autoimmune and diabetes comorbidity.

**To proceed, the following is needed:**
- Mechanism of action data for semaglutide, and a mechanistic rationale for SPS
- A systematic literature search specific to SPS and GLP-1 receptor agonists
- The TGA Product Information for warnings, contraindications and approved indications (these are currently missing)
- Preclinical or case-level evidence before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

