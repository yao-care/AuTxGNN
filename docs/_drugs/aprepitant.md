---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

# Aprepitant: From Its Approved Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a substance P/neurokinin-1 (NK1) receptor antagonist marketed in Australia as a 165 mg oral capsule. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Aprepitant is an NK1 receptor antagonist. Detailed mechanism of action data was not available in the data compiled for this report, so this description reflects general pharmacological knowledge of the drug class.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor, which lead to water retention and low blood sodium. There is no established mechanistic link between NK1 antagonism and this pathway. Substance P/NK1 signalling has been loosely discussed in relation to water balance, but this is speculative. The very high TxGNN score is a graph-based model output and is not backed by any clinical or literature data.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Hypertrichosis | 99.91% | No plausible mechanistic link to NK1 antagonism |
| 3 | Pulmonary hypertension | 99.90% | Indirect preclinical association only; the one linked paper is not relevant (see below) |
| 4 | Leprosy | 99.90% | Theoretical neuroimmune role of substance P only |
| 5 | Ambras-type hypertrichosis universalis congenita | 99.87% | Rare genetic disorder; likely a graph-proximity artefact |
| 6 | Malformation syndrome with odontal/periodontal component | 99.86% | Genetic developmental condition; no rationale |
| 7 | Kyphoscoliotic heart disease | 99.86% | No mechanistic link |
| 8 | Syndrome with Dandy-Walker malformation | 99.86% | Structural congenital defect; no rationale |
| 9 | Subarachnoid haemorrhage | 99.85% | Weak, indirect preclinical hypothesis (substance P in blood-brain barrier disruption and cerebral oedema); the most biologically plausible of the list, but still hypothesis-level |
| 10 | Isolated genetic hair shaft abnormality | 99.85% | No recognised connection |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication.

For the third-ranked prediction (pulmonary hypertension), one publication was linked (PMID [28261651](https://pubmed.ncbi.nlm.nih.gov/28261651/)). It is a Phase I dose-escalation study of pazopanib plus cisplatin in advanced solid tumours. It does not involve aprepitant or pulmonary hypertension and is **not valid supporting evidence**.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2518M | Aprepitant APOTEX | Capsule 165 mg (oral) | Not stated in available data |

## Safety Considerations

- **Knowledge-graph contraindication signal**: liver failure (from the TxGNN knowledge graph, not from product label text).
- **Drug interactions**: 100 interactions were found in the DDInter database. Examples by severity:
  - **Major**: fentanyl, alfentanil, acalabrutinib
  - **Moderate**: paclitaxel, abemaciclib, lidocaine, dihydrocodeine, rabeprazole, nifedipine, ibuprofen, levonorgestrel, hydrocortisone, albendazole, fluvoxamine, fosamprenavir, fosphenytoin, fostamatinib, gefitinib, abametapir (topical)
  - **Minor**: dolutegravir

Warnings and contraindications from the label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. There are no clinical trials or relevant publications, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that underlies NSIAD. Label safety data was also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Obtain the TGA Product Information (approved indications, warnings and contraindications) to complete safety screening
- Obtain mechanism of action data (for example, from DrugBank)
- Conduct a targeted literature search for aprepitant/NK1 antagonism in NSIAD and water-balance disorders
- Establish a mechanistic rationale, with preclinical evidence, before any clinical consideration
- Consider re-prioritising subarachnoid haemorrhage, which has the most plausible (though still hypothetical) biology among the predicted indications, for a focused evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

