---
layout: default
title: Sulthiame
parent: Model Prediction Only (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Sulthiame: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Sulthiame"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "neurocirculatory asthenia", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "MVP1", "autonomic nervous system disease"]
---

# Sulthiame
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

## Sulthiame: From Original Indication (Not Recorded) to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Sulthiame is marketed in Australia as Ospolot 50 mg tablets, but the data compiled for this report do not record an approved indication.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is computational only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Sulthiame is generally known as a carbonic anhydrase inhibitor used mainly as an antiepileptic. This background is general pharmacology and is not confirmed by the compiled data.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots. No plausible pharmacological rationale linking sulthiame to this condition is evident, and no mechanistic link is established. The high TxGNN score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no clinical or literature support.

**Other predictions from the model** share the same limitation. All have an L5 evidence level, no trials, no publications, and a recommendation of Hold:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Obsolete neurogenic bladder (disease) | 0.9994 |
| 3 | Irritable bowel syndrome | 0.9986 |
| 4 | Neurocirculatory asthenia | 0.9979 |
| 5 | Anaphylaxis | 0.9972 |
| 6 | Food-dependent exercise-induced anaphylaxis | 0.9962 |
| 7 | Familial mitral valve prolapse | 0.9949 |
| 8 | Mitral valve prolapse (disease) | 0.9948 |
| 9 | MVP1 | 0.9943 |
| 10 | Autonomic nervous system disease | 0.9935 |

Several of these cluster together (autonomic themes, and three mitral valve prolapse entries). This suggests the TxGNN model (deep learning) is picking up similarities it learned between related diseases rather than independent evidence. The "obsolete neurogenic bladder" entry is an outdated ontology term, so its score may reflect these learned similarities rather than biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13916K | Ospolot | Tablet 50 mg (oral) | Not recorded |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model score. There are no clinical trials or publications, no mechanistic link, and no recorded original indication or safety data. The evidence level is L5.

**To proceed, the following is needed:**
- The approved indication from the TGA-approved Product Information (PI), to establish the original indication
- Mechanism of action data (for example from DrugBank)
- Warnings and contraindications from the PI, so that safety screening can be done
- A literature and trial search for sulthiame in cauda equina syndrome and the other predicted conditions
- A clear pharmacological rationale for the predicted indication before any further evaluation
- Reassessment of the lower-ranked predictions, noting that several are redundant or obsolete ontology terms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

