---
layout: default
title: Avatrombopag
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Avatrombopag: predicted new indication Macrothrombocytopenia with mitral valve insufficiency (evidence level L5). Approved use: Thrombocytopenia"
monitor_inn: "Avatrombopag"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "dense granule disease", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "lower motor neuron syndrome with late-adult onset", "amyotrophic lateral sclerosis, susceptibility to", "Mills syndrome", "monomelic amyotrophy"]
---

# Avatrombopag
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

# Avatrombopag: From Thrombocytopenia to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is an oral thrombopoietin receptor agonist, originally used to treat thrombocytopenia.
The TxGNN model predicts it may be effective for **macrothrombocytopenia with mitral valve insufficiency**,
but there are currently **no clinical trials** and **no publications** supporting this prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia (from the knowledge graph; no approved indication text is recorded in the Australian licence data) |
| Predicted New Indication | Macrothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the drug's known class, avatrombopag is a thrombopoietin receptor (TPO-R/c-Mpl) agonist. It stimulates megakaryocyte proliferation and platelet production, which is why it is used in thrombocytopenia.

The TxGNN prediction most likely reflects the shared thrombocytopenia feature between the original and predicted conditions. However, inherited macrothrombocytopenia often arises from defects in megakaryocyte maturation or cytoskeletal genes, so TPO-R agonism may only partly address the underlying cause. The mitral valve component is not plausibly affected by the drug.

The prediction rests on graph similarity alone, with no supporting clinical or literature evidence.

### Other Predicted Indications (Context)

The remaining top-ranked predictions also have no trials or literature, and all are rated L5 with a Hold recommendation.

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Hereditary thrombocytopenia with normal platelets | 99.995% | Biologically plausible, since TPO-R agonism may raise platelet counts. Response likely depends on genotype. |
| 3 | Transient neonatal thrombocytopenia | 99.995% | Self-limiting condition and no established neonatal safety data, so the risk-benefit balance is unfavourable. |
| 4 | Dense granule disease | 99.995% | A platelet function defect rather than a count problem. Weak rationale, and thrombotic risk is an added concern. |
| 5-10 | Amyotrophic lateral sclerosis (and susceptibility entry), bilateral parasagittal parieto-occipital polymicrogyria, lower motor neuron syndrome with late-adult onset, Mills syndrome, monomelic amyotrophy | 99.990-99.993% | No plausible mechanistic link. Likely graph-topology artefacts. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13313Q | Doptelet | Tablet 20 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 52 interactions were identified. The first 20 are listed below.
  - **Major**: fosphenytoin, carbamazepine, carfilzomib, dabrafenib, enzalutamide, fluconazole, imatinib
  - **Moderate**: clarithromycin, nitisinone, cobicistat, fosamprenavir, gemfibrozil, fenofibrate, apalutamide, atazanavir, amprenavir, boceprevir, ceritinib, delavirdine, idelalisib
- **Class concern**: Thrombotic risk is a recognised concern with TPO-R agonists, particularly relevant to conditions involving platelet function defects.
- **Paediatric/neonatal use**: No established safety data.

Warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the TxGNN model score, with no clinical trials or publications (Evidence Level L5). The leading prediction, macrothrombocytopenia with mitral valve insufficiency, combines a partly plausible platelet-count mechanism with a cardiac feature the drug is not expected to affect. The most biologically credible candidate is hereditary thrombocytopenia with normal platelets, though it still lacks supporting evidence.

**To proceed, the following is needed:**
- Product Information warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Literature review and case reports of TPO-R agonist use in inherited thrombocytopenias, including genotype-specific responses
- Clarification of the approved indication text for the Australian ARTG entry
- Consideration of hereditary thrombocytopenia as a more promising lead before further work on the top-ranked prediction
- Thrombotic risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

