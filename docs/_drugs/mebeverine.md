---
layout: default
title: Mebeverine
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mebeverine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Irritable bowel syndrome (the approved indication text for the Austra…"
monitor_inn: "Mebeverine"
predicted_indications: ["cauda equina syndrome", "insomnia (disease)", "obsolete neurogenic bladder (disease)", "autonomic nervous system disease", "rhinitis", "familial mitral valve prolapse", "dysautonomia", "gastroduodenitis", "mitral valve prolapse (disease)", "MVP1"]
---

# Mebeverine
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

# Mebeverine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Mebeverine is a smooth-muscle antispasmodic originally used to treat irritable bowel syndrome (IBS).
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a model-based prediction only, with **no clinical trials** and **no publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome (the approved indication text for the Australian product is not available; the original indications listed are irritable bowel syndrome, Clostridium difficile colitis and neurocirculatory asthenia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mebeverine is a musculotropic antispasmodic that acts on smooth muscle, and its use in IBS is well established. Mechanistically, it may be applicable to symptoms of smooth-muscle dysfunction in other conditions.

Cauda equina syndrome is a compressive neurological emergency, and its main management is surgical decompression. Neurogenic bowel and bladder dysfunction could be a secondary symptom target for an antispasmodic, but there is no direct mechanistic rationale for treating the underlying condition. The high TxGNN score reflects a graph-based prediction only and should be interpreted with caution.

Other predictions in the list (for example, insomnia, rhinitis and mitral valve prolapse) have no credible mechanistic link. The more plausible secondary candidates are gastroduodenitis (symptomatic relief of upper GI cramping, flagged as a research question) and neurogenic bladder (the ontology term is obsolete and should be mapped to a current term such as neurogenic detrusor overactivity before further review).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4328T | Colofac | Tablet 135 mg | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications were recorded.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no registered trials or publications, no clear mechanistic link, and the primary condition is managed surgically, so there is no basis to advance.

**To proceed, the following is needed:**
- Mechanism of action data for mebeverine (for example, from DrugBank)
- TGA Product Information, including warnings, contraindications and the approved indication text
- A systematic literature and trial search for mebeverine in cauda equina syndrome and neurogenic bowel or bladder dysfunction
- Mapping of the obsolete neurogenic bladder term to a current ontology term, and consideration of gastroduodenitis as a lower-priority research question
- Route and formulation compatibility assessment (currently only an oral 135 mg tablet is registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

