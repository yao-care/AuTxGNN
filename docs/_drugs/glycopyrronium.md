---
layout: default
title: Glycopyrronium
parent: Model Prediction Only (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Glycopyrronium: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not available in the data compiled"
monitor_inn: "Glycopyrronium"
predicted_indications: ["irritable bowel syndrome", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "neurocirculatory asthenia", "migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "autonomic nervous system disease", "primary hereditary glaucoma", "dysthymic disorder"]
---

# Glycopyrronium
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

# Glycopyrronium: From an Inhaled Bronchodilator (Indication Not Recorded) to Irritable Bowel Syndrome

## One-Sentence Summary

Glycopyrronium is a long-acting antimuscarinic (anticholinergic) agent. In Australia it is registered as an inhaled capsule (Seebri Breezhaler), but the approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, with **no clinical trials** and **no publications** currently supporting this specific prediction.
The evidence rests on a model score and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled (the single ARTG entry has no indication text) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, glycopyrronium is a quaternary ammonium antimuscarinic. It blocks muscarinic receptors, which reduces smooth muscle contraction and glandular secretions.

In irritable bowel syndrome (IBS), other antimuscarinics such as dicyclomine and hyoscyamine are already used to relieve abdominal cramping. It is therefore biologically plausible that glycopyrronium could act similarly on gastrointestinal smooth muscle. However, no trials or publications were found for this drug and indication pair. The support is a high model score plus class-level reasoning only.

Other high-scoring predictions are listed below for context. Most have weak or doubtful rationale.

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Cauda equina syndrome | 98.51% | Indirect link via neurogenic bladder/bowel dysfunction only |
| 3 | Neurogenic bladder (obsolete term) | 97.73% | Plausible via detrusor muscarinic blockade; the term should be mapped to a current ontology term before any evidence search |
| 4 | Neurocirculatory asthenia | 96.91% | Speculative; anticholinergic tachycardia could worsen symptoms |
| 5–6 | Migraine and migraine with brainstem aura | 96.08% / 95.68% | No clear rationale; minimal blood-brain barrier penetration |
| 7, 9 | Open-angle and primary hereditary glaucoma | 95.61% / 95.30% | More likely a safety caution than an opportunity |
| 8 | Autonomic nervous system disease | 95.55% | Only indication with any evidence (L4); see below |
| 10 | Dysthymic disorder | 93.68% | No credible mechanism |

The autonomic nervous system disease prediction is the only one with some supporting material. It is broad, and specific conditions such as hyperhidrosis and drooling should be evaluated separately.

## Clinical Trial Evidence

No clinical trials are registered for glycopyrronium in irritable bowel syndrome. Currently no related clinical trials registered.

For context, one trial exists for the rank 8 prediction (autonomic nervous system disease). It is only indirectly relevant:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02872090](https://clinicaltrials.gov/study/NCT02872090) | Phase 4 | Completed | 42 | Randomised, double-blind, crossover study of tiotropium, glycopyrronium and indacaterol on cardiac autonomic control in mild COPD. It examines autonomic effects as a physiological or safety outcome, not efficacy in an autonomic disease. |

## Literature Evidence

No publications were found for glycopyrronium in irritable bowel syndrome. Currently no related literature available.

For context, one publication relates to the rank 8 prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37714301](https://pubmed.ncbi.nlm.nih.gov/37714301/) | 2024 | Review | Actas Dermo-Sifiliográficas | Narrative review of topical anticholinergics in focal hyperhidrosis, an autonomic disorder. It offers indirect support only. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10059K | Seebri Breezhaler | Capsule containing powder for oral inhalation, 50 micrograms (as bromide), for use in Breezhaler | Not available in the data compiled |

The only registered route is oral inhalation. Route compatibility with a gastrointestinal indication such as IBS has not been assessed. An inhaled product is unlikely to be suitable for it.

## Safety Considerations

Specific warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** An interaction query returned 100 records. Most listed are of Moderate severity, and a few are Minor. Examples include:
- **Additive anticholinergic effects:** other antimuscarinics such as aclidinium, hyoscyamine and homatropine, and sedating antihistamines such as chlorpheniramine, acrivastine and phenyltoloxamine
- **Opioids and central nervous system depressants:** fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, loperamide and ethanol
- **Others:** botulinum toxin type A, amantadine, amitriptyline, acebutolol, acetylcholine (Moderate); acetaminophen and hydrochlorothiazide (Minor)

**Class-level cautions from the prediction analysis:**
- Antimuscarinics may precipitate angle closure or raise intraocular pressure in glaucoma. This is relevant to two of the predicted indications.
- Peripheral anticholinergic effects such as urinary retention and tachycardia still apply, although the quaternary structure limits CNS penetration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IBS prediction has a high model score and a plausible class-level mechanism, but there are no trials or publications for this drug and indication pair (Evidence Level L5). The only registered Australian product is an inhaled capsule, and the safety data and indication text are missing.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm the approved indication, warnings and contraindications
- Detailed mechanism of action data
- A systematic literature and trial search for glycopyrronium in IBS, and for the other predictions with stronger rationale (neurogenic bladder, using a current ontology term)
- Separate evaluation of specific autonomic conditions (hyperhidrosis, drooling) rather than the broad "autonomic nervous system disease" term
- An assessment of route and formulation compatibility, as only an inhaled product is currently registered in Australia
- A safety plan covering anticholinergic burden, interactions and ocular risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

