---
layout: default
title: Granisetron
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetron: From Chemotherapy-Associated Nausea and Vomiting to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist marketed in Australia as an oral tablet (Kytril). The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but this is a model prediction only, with **no clinical trials** and **no publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Granisetron is known to be a selective 5-HT3 receptor antagonist.

It has been hypothesised that 5-HT3 modulation may influence the dopaminergic and serotonergic signalling relevant to mood regulation. This link is speculative. The original indication was not recorded, so the relationship between the original and new indication cannot be assessed here.

The high TxGNN score (0.996) is a computational prediction only. It is not backed by any trial or literature data.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|---|---|---|---|
| 2 | Tourette syndrome | 99.52% | Speculative. 5-HT3 antagonism may indirectly modulate dopaminergic circuits, and other agents in the class (e.g. ondansetron) have been explored. |
| 3 | Acute contagious conjunctivitis | 99.49% | No clear rationale. Likely a graph-association artefact. |
| 4 | Angioedema | 99.36% | Weak. Granisetron does not target histamine or bradykinin pathways. |
| 5 | Allergic urticaria | 99.32% | Weak. Serotonin may contribute to itch and mast cell responses. |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 99.32% | No plausible mechanism (AVPR2 gain-of-function). |
| 7 | Trichotillomania | 99.23% | Speculative. Serotonergic dysregulation is implicated in the obsessive-compulsive spectrum. |
| 8 | Bronchitis | 99.18% | No established mechanistic connection. |
| 9 | Cold urticaria | 99.10% | Minor, indirect role of serotonin in mast cell-related itch. |
| 10 | Conjunctivitis | 99.09% | No plausible mechanistic link. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5898K | Kytril | Tablet 2 mg (as hydrochloride) | Not available in the compiled data |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not product label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest, and heart conduction disease. These point to a QT-prolongation and cardiac conduction concern and should be checked against the label.
- **Drug interactions:** 100 interactions were identified in total (DDInter). Examples from the first 20 reviewed:
  - **Major:** fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide. Several of these involve QT prolongation or serotonergic effects.
  - **Moderate:** abametapir (topical), abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no registered trials or publications, the mechanistic link to mania is speculative, and the compiled data contain no label-based safety information. The knowledge-graph cardiac contraindication signals and the many major interactions add further caution.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm the approved indication, warnings and contraindications
- Mechanism of action data (e.g. from DrugBank)
- A systematic literature and trial registry search (including ANZCTR) for granisetron or 5-HT3 antagonists in bipolar mania
- A mechanistic and preclinical rationale for mood-disorder use
- A cardiac safety assessment (QT and conduction) for the target population, which often takes interacting psychotropic medicines
- Route and formulation compatibility assessment for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

