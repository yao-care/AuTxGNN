---
layout: default
title: Dulaglutide
parent: Model Prediction Only (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dulaglutide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Dulaglutide"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a once-weekly injectable GLP-1 receptor agonist, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia** (a rare skeletal dysplasia), but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the model alone and has no clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note: The original indication is taken from the knowledge-graph indication data, as the ARTG entry compiled for this report has no approved indication text.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dulaglutide belongs to the GLP-1 receptor agonist class. Its efficacy in type 2 diabetes is established through glucose-dependent stimulation of insulin secretion.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency), which affects PI3K/insulin signalling and endochondral bone growth. Any link between this pathway and incretin signalling is speculative. There is no clear mechanistic connection, and the high TxGNN score is likely driven by graph proximity through insulin-related biology rather than a demonstrated therapeutic effect.

Other top-ranked predictions show the same pattern. Most are linked to diabetes or lipodystrophy in the knowledge graph rather than to any plausible GLP-1 mechanism:

| Rank | Predicted Disease | Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 97.05% | Shared GAD65 autoimmunity and diabetes association; no established role for GLP-1 agonists |
| 3 | Focal stiff limb syndrome | 97.05% | Variant of the stiff person spectrum; no demonstrated mechanism |
| 4 | Thiamine-responsive dysfunction syndrome | 96.81% | Diabetes is a core feature, but thiamine is the standard therapy |
| 5 | Drug-induced localised lipodystrophy | 95.62% | No known effect on localised fat loss |
| 6 | Pancreatic agenesis | 95.55% | Mechanistically implausible, as dulaglutide needs functional beta cells |
| 7 | Centrifugal lipodystrophy | 95.37% | No mechanism linking GLP-1 agonism to fat loss correction |
| 8 | Pressure-induced localised lipoatrophy | 95.29% | No plausible pathway |
| 9 | Idiopathic localised lipodystrophy | 94.99% | No evidence of benefit |
| 10 | Autoimmune oophoritis | 69.57% | Notably lower score; no evidence in autoimmune ovarian disease |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11364D | Trulicity | Injection 1.5 mg in 0.5 mL single dose pre-filled pen | Not stated in the data compiled for this report |

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 recorded interactions (first 20 reviewed). Most are of moderate severity, with a few minor. Examples include:
- **Moderate:** phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, acetazolamide, furosemide, hydrochlorothiazide, ethinylestradiol, estradiol, norethisterone, hydrocortisone, ethanol, fosamprenavir, fosphenytoin, gemifloxacin, alpelisib, aripiprazole
- **Minor:** topical hydrocortisone, topical alclometasone

Many of these likely relate to effects on blood glucose control. The full list should be reviewed before any use.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5). There are no registered trials or publications, and no plausible mechanism links dulaglutide to opsismodysplasia. The same applies to the other nine predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data, and a clear biological rationale linking GLP-1 receptor agonism to SHIP2/INPPL1-related skeletal growth
- Preclinical evidence (for example, cell or animal models of INPPL1 deficiency)
- Safety information from the TGA-approved PI, including warnings and contraindications, as well as the full interaction list
- Assessment of the relevance of the product in a paediatric rare-disease setting, as the available ARTG entry is a single pre-filled pen presentation
- Review of whether any of the lower-ranked predictions has better mechanistic support, since none currently does
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

