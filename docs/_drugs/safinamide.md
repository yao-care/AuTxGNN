---
layout: default
title: Safinamide
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
description: "Safinamide: predicted new indication Rasmussen subacute encephalitis (evidence level L5). In Australia: 4 PBS items (4 currently listed)"
---

# Safinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Safinamide: Rasmussen subacute encephalitis
{: .text-alpha }

## One-Sentence Summary

Safinamide is an oral MAO-B inhibitor originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for safinamide: "The precise mechanism by which XADAGO exerts its therapeutic effects in PD is unknown. XADAGO is an inhibitor of monoamine oxidase B (MAO-B). Inhibition of MAO-B activity, by blocking the catabolism of dopamine, is thought to result in an increase in dopamine levels and a subsequent increase in dopaminergic activity in the brain." ([DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2), label version 2026-10-05; accessed 2026-11-19.) Based on general pharmacology, safinamide is a MAO-B inhibitor that is also thought to modulate glutamate release through sodium channel blockade. This could plausibly relate to seizure control, which is a key feature of Rasmussen encephalitis.

However, Rasmussen encephalitis is driven mainly by T-cell-mediated autoimmune inflammation affecting one brain hemisphere. Safinamide's dopaminergic and anti-glutamatergic actions do not address that underlying process, so the mechanistic link is weak and speculative. The high score (0.9963) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as clinical evidence.

Other predictions in the top ten are worth noting for context:
- **Closest to the original indication:** Paralysis agitans, juvenile, of Hunt (a juvenile parkinsonian syndrome), and PLA2G6-associated neurodegeneration (which includes parkinsonism-dystonia phenotypes). Symptomatic dopaminergic benefit is conceivable, but no supporting data were found.
- The only item is a 2026 systematic review on REM sleep behaviour disorder treatments in synucleinopathies, which is indirect evidence. This is the most promising lead for further research.
- **Weak or no mechanistic rationale:** Myelitis (0.9946). The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Rasmussen subacute encephalitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42623795](https://pubmed.ncbi.nlm.nih.gov/42623795/) | 2026 | Systematic review | Sleep Medicine | Evaluates the effectiveness and safety of drug treatments for REM sleep behaviour disorder in synucleinopathies (Parkinson disease, Parkinson disease dementia, dementia with Lewy bodies, multiple system atrophy, isolated RBD). Safinamide-specific findings have not been verified. |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 11656L | Xadago | Safinamide | Tablet 50 mg | Valid |
| 11666B | Xadago | Safinamide | Tablet 100 mg | Valid |
| 14391K | Xadago | Safinamide | Tablet 50 mg | Valid |
| 14528P | Xadago | Safinamide | Tablet 100 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

Warnings and contraindications are not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** A screen identified 100 potential interactions. The first 20 reviewed include one **Major** interaction and the rest **Moderate**.
- **Major:** Bupropion
- **Moderate, antidiabetic agents:** Chlorpropamide, glimepiride, acetohexamide, nateglinide, repaglinide, empagliflozin, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, isophane, regular, inhaled)
- **Moderate, sympathomimetic or stimulant agents:** Isometheptene, diethylpropion, phentermine
- **Moderate, other:** Metoclopramide, rosuvastatin

The remaining interactions were not itemised in the data compiled for this report and should be checked against the PI and an interaction database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Rasmussen subacute encephalitis rests on a model score alone (evidence level L5), with no trials or publications, and the proposed mechanism does not match the autoimmune nature of the disease.

**To proceed, the following is needed:**
- Detailed mechanism of action data (for example from DrugBank)
- TGA Product Information review for warnings, contraindications and the approved indication
- Preclinical or mechanistic evidence for any effect on neuroinflammation or seizure control
- A full review of the interaction list, especially the Major interaction with bupropion

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available from the compiled sources" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

