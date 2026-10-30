---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 241
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Eflornithine: predicted new indication Esotropia (evidence level L5). Approved use: Human African trypanosomiasis"
monitor_inn: "Eflornithine"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
---

# Eflornithine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Eflornithine: From Human African Trypanosomiasis to Esotropia
{: .text-alpha }

## One-Sentence Summary

Eflornithine was originally used to treat human African trypanosomiasis (sleeping sickness).
The TxGNN model predicts it may be effective for **esotropia**, but the prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Human African trypanosomiasis (the Australian licence record has no approved indication text) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Eflornithine irreversibly inhibits ornithine decarboxylase (ODC), the first enzyme in polyamine synthesis. This is the basis of its use in human African trypanosomiasis. The data compiled for this report did not include a detailed mechanism of action, so this description relies on the pharmacology records.

No mechanistic link was identified between ODC inhibition and esotropia (a form of strabismus). No known pathway connects polyamine synthesis to ocular motor control. The high score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Esotropia is also unrelated to the original infectious indication.

For context, the other top-ranked predictions were also reviewed. Most had no identifiable mechanistic link and no supporting evidence. The one biologically coherent prediction was **bovine trypanosomiasis** (rank 6, L4). It is essentially an extension of the original indication to a veterinary host, and the supporting studies are indirect: one preclinical study of eflornithine and hydroxyurea against *Babesia* and *Theileria*, and one mechanistic study of trypanosomatid polyamine pathways. It is a research question rather than a new human repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for esotropia.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14880E | Ifinwil | Tablet 192 mg (as hydrochloride) | Not stated in the data compiled |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: Exanthem (rash) and dermatitis are recorded as contraindication associations.
- **Drug Interactions**: The interaction query returned only a pharmacological target record (ornithine decarboxylase, ODC1), not a drug-drug interaction. No clinically graded interactions were identified.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications. The PI safety data could not be retrieved for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction has no clinical, literature or mechanistic support and is based solely on a score from the TxGNN model (deep learning). At L5 evidence, there is no basis to progress.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking polyamine/ODC inhibition to esotropia or ocular motor control
- Preclinical or clinical evidence in strabismus
- Retrieval and review of the TGA Product Information, including warnings and contraindications
- The approved indication text for the Australian ARTG entry
- Confirmation of the drug's mechanism of action from a primary source
- Route and formulation assessment (the only Australian product is an oral tablet, and an ocular condition may need a different approach)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

