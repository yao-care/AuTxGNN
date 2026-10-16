---
layout: default
title: Naltrexone
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Naltrexone: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Substance abuse/dependence, obesity disorder, monogenic obesity"
---

# Naltrexone
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

# Naltrexone: From Substance Dependence and Obesity to Hypervitaminosis (Prediction Only)

## One-Sentence Summary

Naltrexone is an opioid receptor antagonist, originally used for substance abuse/dependence and obesity-related disorders.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The prediction rests on a graph-based score alone and should be treated as a hypothesis, not a finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Substance abuse/dependence, obesity disorder, monogenic obesity (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, naltrexone is an opioid receptor antagonist. Its use in substance dependence and obesity is established, but a mechanistic link to the predicted indication cannot be established from the data compiled for this report.

No identifiable mechanistic link exists between opioid receptor antagonism and vitamin excess states. The high TxGNN score is a graph-based prediction only, and its rank (13,245) suggests that a high score alone is not strong evidence. With no supporting trials or literature, this prediction is likely a model artefact.

### Other Predictions Reviewed

The other nine predictions were also reviewed. None has clinical trial evidence.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Proximal 16p11.2 microdeletion syndrome | 98.13% | L5 | Indirect hypothesis: this deletion is associated with obesity, and naltrexone is used in obesity. No direct evidence. |
| 3 | Obsolete hypertelorism | 95.64% | L5 | Craniofacial anomaly; the term is obsolete, so likely an ontology artefact. |
| 4 | Frontorhiny | 93.19% | L5 | Congenital malformation; no pharmacological rationale. |
| 5 | Restless legs syndrome | 92.20% | L4 | Opioid system involvement is plausible, but an antagonist may act in the opposite direction. The retrieved papers are indirect. This is the only candidate framed as a research question. |
| 6 | DECR deficiency encephalopathy | 72.94% | L5 | Mitochondrial metabolic disorder; no link. |
| 7 | Myxomatous mitral valve prolapse | 62.59% | L5 | Structural valve condition; no link. |
| 8 | ADHD, inattentive type | 62.20% | L5 | Speculative link via reward pathways and impulsivity; no evidence. |
| 9 | Triphalangeal thumb, nonopposable | 61.77% | L5 | Congenital skeletal malformation; no rationale. |
| 10 | Hypospadias 3, autosomal | 61.77% | L5 | Congenital genitourinary malformation; no link. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypervitaminosis.

---

## Literature Evidence

Currently no related literature available for hypervitaminosis.

For context, five papers were retrieved for the rank 5 candidate, restless legs syndrome. Based on titles and abstracts, none appears to study naltrexone in that condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40686928](https://pubmed.ncbi.nlm.nih.gov/40686928/) | 2025 | Cohort | Brain, Behavior, & Immunity - Health | Neuropsychiatric disorders in mast cell activation syndrome; tangential |
| [33238082](https://pubmed.ncbi.nlm.nih.gov/33238082/) | 2020 | Review | J Clin Psychiatry | Critical appraisal of gabapentin for alcohol-related disorders; tangential |
| [41090493](https://pubmed.ncbi.nlm.nih.gov/41090493/) | 2025 | Review | Cochrane Database Syst Rev | Treatments for impulsive-compulsive behaviours in Parkinson's disease; tangential |
| [15130554](https://pubmed.ncbi.nlm.nih.gov/15130554/) | 2004 | Cohort | Neurophysiol Clin | Gabapentin for symptoms (including restless legs) after rapid opiate detoxification |
| [39893547](https://pubmed.ncbi.nlm.nih.gov/39893547/) | 2026 | Pharmacovigilance analysis | Expert Opin Drug Saf | Adverse event signals for naltrexone from the FAERS database |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8370M | Naltrexone GH | Tablet containing naltrexone hydrochloride 50 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from graph relationships, not from approved label text, and should be verified against the TGA-approved Product Information):
- Liver conditions: liver failure, acute liver failure, liver disease, hepatitis
- Impaired renal function
- Respiratory conditions: respiratory failure, chronic obstructive pulmonary disease
- Adrenal conditions: Addison disease, adrenal insufficiency, congenital adrenal hyperplasia and related disorders
- Thyroid conditions: hypothyroidism, myxoedema
- Neurological and psychiatric conditions: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- Gastrointestinal and other conditions: pancreatitis, gallbladder disease, chronic diarrhoeal disease, paralytic ileus, benign prostatic hyperplasia, hypotensive disorder

**Drug Interactions:** The interaction screen returned 100 interactions, of which 20 are shown in the data compiled for this report.
- **Major:** fentanyl, codeine, dihydrocodeine, tramadol. These opioids are pharmacologically opposed by naltrexone.
- **Moderate (examples):** ethanol, acetaminophen, ibuprofen, ketorolac, abacavir, lamivudine, zidovudine, abemaciclib, abiraterone, afatinib, acarbose, isotretinoin, acitretin, aldesleukin, alectinib, trastuzumab emtansine.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypervitaminosis has no clinical trials, no literature and no identifiable mechanistic link, so it is Level L5 (model prediction only). The high score is not enough to justify further investment. Of all ten predictions, only restless legs syndrome (L4) merits consideration as a research question, and the direction of effect there is unresolved.

**To proceed, the following is needed:**
- Mechanism of action data for naltrexone (currently missing)
- Approved indication text and Product Information warnings from the TGA-approved PI
- A targeted literature search for naltrexone in the predicted indication
- For restless legs syndrome, a review of whether opioid antagonism could worsen symptoms before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

