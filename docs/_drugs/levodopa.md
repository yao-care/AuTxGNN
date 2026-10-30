---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease and related parkinsonian syndromes"
monitor_inn: "levodopa"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **no registered clinical trials** and **no publications** supporting this direction. The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian syndromes (the Australian licence entries in the data compiled for this report do not include approved indication text) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levodopa is a dopamine precursor used to replace dopamine in Parkinson disease and related parkinsonian syndromes. Its efficacy in those conditions is established, but the mechanistic link to Rasmussen encephalitis cannot be validated from the data compiled for this report.

Rasmussen encephalitis is a rare, chronic, unilateral inflammatory brain disorder. It is marked by intractable focal seizures, progressive hemispheric atrophy and neurological decline. Its proposed pathology is T-cell-mediated, with possible autoimmune and viral contributors.

A plausible connection is the overlap in movement-disorder features (for example hemiparesis, dystonia or hemiparkinsonism-like presentations). Another is the similarity to hemiparkinsonism-hemiatrophy syndrome that the TxGNN model (deep learning) may have learned. However, dopaminergic replacement is not expected to affect the inflammatory, immune-mediated or epileptogenic mechanisms that drive the disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11910W | Duodopa | Intestinal gel containing levodopa 20 mg with carbidopa monohydrate 5 mg per mL, 100 mL | Not available in the data compiled |
| ARTG 14356N | Madopar Rapid 62.5 | Dispersible tablet containing levodopa 50 mg with 12.5 mg benserazide (as hydrochloride) | Not available in the data compiled |
| ARTG 14357P | Lecteva | Tablet 150 mg-37.5 mg (as monohydrate)-200 mg | Not available in the data compiled |

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The knowledge graph links levodopa with the following conditions. These should be verified against the PI.
  - Neurological and psychiatric: multiple system atrophy, drug-induced dyskinesia, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
  - Cardiovascular: orthostatic hypotension, postural orthostatic tachycardia syndrome, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease
  - Eye: open-angle glaucoma, angle-closure glaucoma
  - Metabolic, organ and other: diabetes mellitus, diabetic ketoacidosis, kidney disease, liver disease, gallbladder disease, gastric ulcer, peptic ulcer disease, pyoureter, melanoma, haemoglobinopathy, diarrhoeal disease
- **Drug Interactions**: 104 interactions were recorded in total, and 20 are listed in the data compiled for this report.
  - Moderate: epinephrine, ephedrine, bupropion, metronidazole, pyridoxine, iron, metoclopramide, and the anticholinergics atropine, hyoscyamine, methscopolamine, glycopyrronium, clidinium, dicyclomine and mepenzolate
  - Minor: aluminium hydroxide, calcium carbonate, magaldrate, and magnesium carbonate, hydroxide and oxide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score of 0.9906, with no clinical trials, literature or mechanistic data. Rasmussen encephalitis is immune-mediated and epileptogenic, and dopamine replacement is not expected to act on these processes. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data for levodopa, and a credible mechanistic link to Rasmussen encephalitis
- Preclinical or published clinical evidence in Rasmussen encephalitis
- TGA Product Information warnings and contraindications for the Australian products, since this safety screening step is currently blocked
- Review of route compatibility, as the data for this are still pending
- Consideration of whether established immunotherapies and seizure management make a levodopa approach clinically relevant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

