---
layout: default
title: Glipizide
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Glipizide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Glipizide"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Glipizide
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

# Glipizide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Glipizide is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, but there are **no clinical trials** and **no relevant publications** supporting this prediction. It is a model-based signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Glipizide is a sulfonylurea, a class known to stimulate insulin release by closing pancreatic K-ATP channels. Its efficacy in type 2 diabetes is established.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency), which affect PI3K/insulin signalling and bone growth. The only plausible connection is a shared insulin-signalling network. **No direct mechanistic link is established.** The high score (0.988) is a graph-based prediction and should not be read as evidence of benefit.

Other candidates were also reviewed (for example, classic stiff person syndrome, focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, several localised lipodystrophies, pancreatic agenesis and autoimmune oophoritis). All are at evidence level L5 with a recommendation of Hold. Most appear to reflect shared diabetes or metabolic network proximity rather than a therapeutic effect. For pancreatic agenesis, a sulfonylurea is mechanistically implausible because it requires functional beta cells.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

(For pancreatic agenesis, the fifth-ranked-by-volume candidate with retrieved publications, the five results concerned animal diabetes, a danazol/lovastatin adverse event and incretin effects in mice. None assessed glipizide and none are relevant evidence.)

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14019W | Melizide | Tablet 5 mg (oral) | Not available in the compiled data |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text): kidney disease, liver disease, gallbladder disease, pituitary hormone deficiencies (including hypopituitarism and Sheehan syndrome), adrenocortical insufficiency/Addison disease, thymus gland disease, infectious disease, and substance abuse/dependence.
- **Drug Interactions:** 100 interactions were identified. Examples at moderate level include:
  - Beta-agonists and sympathomimetics: salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
  - Beta-blocker: acebutolol
  - Corticosteroids: hydrocortisone
  - NSAIDs: ibuprofen, ketorolac
  - H2 blockers: famotidine, ranitidine
  - Others: acetazolamide, acitretin, ethinylestradiol, hydrochlorothiazide, albiglutide, nitazoxanide, ethanol

  Minor-level examples include topical hydrocortisone and topical alclometasone.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications, as label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no clinical trials or relevant literature, and there is no plausible mechanism linking a sulfonylurea to opsismodysplasia. Evidence is at level L5.

**To proceed, the following is needed:**
- Mechanism of action data for glipizide
- Product Information warnings and contraindications from the TGA or PBS source
- Preclinical or mechanistic evidence linking K-ATP channel or insulin-secretion effects to SHIP2/INPPL1-related bone disease
- A targeted literature search for glipizide in opsismodysplasia and in the other predicted conditions
- Approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

