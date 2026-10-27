---
layout: default
title: Gliclazide
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gliclazide: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Gliclazide"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Gliclazide
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

## Gliclazide: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Gliclazide is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; no approved indication text is available in the Australian licence data) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gliclazide is a sulfonylurea that acts on K-ATP channels in pancreatic beta cells to stimulate insulin release. Its efficacy in type 2 diabetes is established, but a therapeutic mechanism for stiff person syndrome is not apparent.

Stiff person syndrome is an autoimmune disorder of GABAergic neurotransmission, typically with anti-GAD65 antibodies. The most plausible link to gliclazide is the co-occurrence of anti-GAD autoimmunity and diabetes. This is a comorbidity association, not a therapeutic mechanism. The prediction probably reflects shared neighbouring nodes (GAD-related and diabetes-related) in the knowledge graph. No evidence suggests gliclazide relieves neurological symptoms such as stiffness or spasm.

**Other predicted indications (all L5, all Hold, no trials or literature):**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Focal stiff limb syndrome | 97.96% | Variant of the stiff person spectrum; same reasoning as above |
| 3 | Thiamine-responsive dysfunction syndrome | 97.79% | Diabetes is a feature, so the link would be symptomatic glycaemic control only; thiamine is standard therapy |
| 4 | Opsismodysplasia | 97.72% | INPPL1/SHIP2 involvement in insulin signalling may explain the association; no direct evidence |
| 5 | Pancreatic agenesis | 96.64% | Beta cells are absent or severely deficient, so gliclazide is unlikely to work; insulin is standard |
| 6 | Drug-induced localised lipodystrophy | 96.43% | Link runs only through diabetes comorbidity |
| 7 | Centrifugal lipodystrophy | 96.23% | No mechanism connecting gliclazide to pathogenesis |
| 8 | Pressure-induced localised lipoatrophy | 96.14% | Likely an artefact of lipodystrophy cluster similarity |
| 9 | Idiopathic localised lipodystrophy | 95.94% | Localised forms are usually metabolically silent |
| 10 | Autoimmune oophoritis | 88.15% | Link only through autoimmune comorbidity |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13896J | APX-Gliclazide | Tablet 80 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interaction records were found in the data compiled for this report, and no knowledge-graph contraindications were listed. This should not be read as an absence of risk. Gliclazide is a sulfonylurea, and hypoglycaemia is a well-recognised concern with this class, so any use outside diabetes would need careful review of this risk in people without diabetes.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5), with no registered trials or publications. No plausible therapeutic mechanism links a K-ATP channel blocker to stiff person syndrome, and the apparent link is most likely a diabetes and anti-GAD comorbidity artefact in the knowledge graph. The same applies to the other nine predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to the predicted indications
- Safety information from the TGA-approved Product Information (warnings, contraindications, interactions), which is currently missing
- Any preclinical or clinical evidence showing a benefit in stiff person syndrome beyond comorbid glycaemic control
- Approved indication text for the ARTG entry
- Assessment of hypoglycaemia risk in patients without diabetes
- Confirmation that thiamine-responsive dysfunction syndrome and pancreatic agenesis, where diabetes is a feature, are better served by their established standard therapies (thiamine and insulin respectively)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

