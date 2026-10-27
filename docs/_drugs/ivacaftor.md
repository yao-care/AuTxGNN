---
layout: default
title: Ivacaftor
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ivacaftor: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Cystic fibrosis"
monitor_inn: "Ivacaftor"
predicted_indications: ["rheumatoid arthritis", "HIV infectious disease", "leprosy", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "multiple endocrine neoplasia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "cytomegalovirus infection"]
---

# Ivacaftor
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

## Ivacaftor: From Cystic Fibrosis to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Ivacaftor is a CFTR potentiator originally used to treat cystic fibrosis.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (the Australian licence entry has no indication text recorded; this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ivacaftor is a CFTR potentiator, its use in cystic fibrosis is established, and any mechanistic applicability to rheumatoid arthritis remains speculative.

No mechanistic link is established in the data compiled for this report. One hypothesis is that CFTR expressed in immune or epithelial cells may modulate inflammation, but nothing in the available evidence supports it. The TxGNN score is a graph-based computational prediction only, and no similarity analysis between the original and predicted indications has been completed.

Other high-scoring predictions for this drug (HIV infection, leprosy, cytomegalovirus infection, and several rare genetic syndromes) also have no supporting trials or literature. Two entries (simian immunodeficiency virus infection and feline acquired immunodeficiency syndrome) share an identical score, which suggests a shared signal from the lentiviral disease cluster rather than independent findings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10170G | Kalydeco | Tablet 150 mg (oral) | Not recorded in the compiled data |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records; 20 are shown in the compiled data. Major interactions include:
  - **Aprepitant** (Major)
  - **Clarithromycin** (Major)

  Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), loperamide, cimetidine, cisapride, clotrimazole, eliglustat, eluxadoline, and sulfonylureas (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide). Fidaxomicin is a Minor interaction.

  Corticosteroids and other agents commonly used in rheumatoid arthritis are relevant to this prediction, so combination use would need careful review.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rheumatoid arthritis is supported only by a model score (L5), with no registered trials, no publications, and no established mechanistic link. Safety data from the product label could not be reviewed, and the drug has a large number of recorded interactions.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and a plausible CFTR-related rationale for rheumatoid arthritis
- Product Information warnings and contraindications for safety screening
- A literature search and preclinical or early-phase evidence in rheumatoid arthritis
- Review of interactions with agents used in rheumatoid arthritis, particularly corticosteroids
- Confirmation of the approved indication text for the Australian licence entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

