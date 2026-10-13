---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used to treat **type 2 diabetes mellitus**.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Empagliflozin is known as an SGLT2 inhibitor that lowers blood glucose by reducing renal glucose reabsorption, and its efficacy in type 2 diabetes is established.

For focal stiff limb syndrome, no plausible mechanistic link has been identified. The condition belongs to the stiff-person spectrum, a neuro-immunological disorder involving impaired GABAergic or glycinergic inhibition, often with anti-GAD antibodies. SGLT2 inhibition has no known effect on this pathway.

The high score is most likely an artefact of the knowledge graph, probably driven by the association between GAD autoimmunity and diabetes. It should not be read as evidence of benefit.

Other predictions in the same list show a similar pattern. They include classic stiff person syndrome (99.06%), opsismodysplasia (99.03%), thiamine-responsive dysfunction syndrome (98.99%), several localised lipodystrophies, pancreatic agenesis and autoimmune oophoritis (92.37%). None has any clinical trial support. For pancreatic agenesis, the two retrieved papers concern type 2 diabetes and diabetic retinopathy, not the predicted condition. Use in insulin-deficient states such as pancreatic agenesis would also carry a risk of ketoacidosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10202Y | Jardiance | Tablet 25 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions. Most of those listed are of moderate severity, and a few are minor. Examples include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Cardiovascular drugs: acebutolol, nifedipine, fosinopril, furosemide
  - Other: acetazolamide, hydrocortisone, ethinylestradiol, ethanol, fosphenytoin, fosamprenavir

  Minor interactions were listed for topical corticosteroids (hydrocortisone, alclometasone).

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no plausible mechanistic link. It is likely a knowledge-graph artefact linked to GAD autoimmunity and diabetes. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking SGLT2 inhibition to the stiff-person spectrum
- Preclinical or clinical evidence in focal stiff limb syndrome (none currently exists)
- Review of the TGA-approved Product Information for warnings and contraindications
- Approved indication text for the Australian ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

