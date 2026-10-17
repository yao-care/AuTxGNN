---
layout: default
title: Asenapine
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Asenapine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Manic bipolar affective disorder, bipolar disorder, schizophrenia"
monitor_inn: "Asenapine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "syndromic myopia", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Asenapine
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

# Asenapine: From Bipolar Disorder and Schizophrenia to Retinal Dystrophy

## One-Sentence Summary

Asenapine is an atypical antipsychotic originally used for **bipolar I disorder (manic and mixed episodes)** and **schizophrenia**.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**.
However, there are **no clinical trials** and **no publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Manic bipolar affective disorder, bipolar disorder, schizophrenia |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Asenapine is known as an atypical antipsychotic that antagonises serotonin, dopamine, alpha-adrenergic and histamine receptors. Its efficacy in mania and schizophrenia is established.

No plausible mechanistic link to retinal dystrophy has been identified. Retinal dystrophies are largely genetic conditions affecting the retina, and asenapine's receptor pharmacology has no known connection to those genetic causes. The high score (0.998) most likely reflects patterns in the underlying knowledge graph rather than biological rationale.

**Note:** Among the other predictions, "major affective disorder" (rank 10, score 99.57%) is the only one with supporting literature. It is essentially on-label or closely related to asenapine's approved uses, so it is not a true repurposing candidate. Its evidence is summarised in the conclusion below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5140M | Saphris | Sublingual wafer 5 mg (as maleate) | Not stated in the data compiled; refer to the TGA Product Information |

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** The knowledge graph links asenapine to the following conditions. Key groups are:
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, myocardial infarction, myocardial ischaemia, coronary artery disease
- **Cerebrovascular:** stroke, cerebral infarction, cerebrovascular disorder
- **Blood:** neutropenia, agranulocytosis, leukopenia, severe congenital neutropenia
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, obesity, potassium deficiency
- **Neurological and autonomic:** epilepsy, neuroleptic malignant syndrome, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- **Hepatic:** liver failure

**Drug Interactions:** The interaction query returned 100 interactions in total. The main ones listed are:
- **Major:** bupropion, morphine, cisapride
- **Moderate (examples):** metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide (antidiabetic agents), famotidine, cimetidine, clarithromycin, epinephrine, atropine, hyoscyamine, loperamide, bisacodyl

For full safety information, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The retinal dystrophy prediction is supported only by a model score. There are no trials or publications, and no plausible mechanism links asenapine's receptor antagonism to this largely genetic group of retinal diseases.
- By contrast, the "major affective disorder" prediction is supported by a meta-analysis of randomised trials (PMID 23719049) and several reviews. It would be rated L1 and "Proceed with Guardrails", but it largely restates existing indications.

**To proceed, the following is needed:**
- A biological rationale or preclinical data linking asenapine to retinal dystrophy pathways
- Detailed mechanism of action data
- Label-based warnings and contraindications from the TGA Product Information
- If the affective disorder direction is pursued, clarification of its scope (acute mania or mixed episodes versus bipolar depression or unipolar depression), plus monitoring of metabolic and extrapyramidal effects and a review of the high interaction burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

