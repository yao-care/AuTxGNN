---
layout: default
title: Umeclidinium
parent: Model Prediction Only (L5)
nav_order: 760
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Umeclidinium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report (the registered indic…"
monitor_inn: "Umeclidinium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "primary hereditary glaucoma", "nephrogenic syndrome of inappropriate antidiuresis", "gastroduodenitis", "common cold", "atrophoderma vermiculata", "peptic ulcer disease", "allergic urticaria"]
---

# Umeclidinium
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

## Umeclidinium: From COPD Maintenance Treatment to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Umeclidinium is an inhaled long-acting muscarinic antagonist (LAMA) marketed in Australia as Incruse Ellipta. The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction with no clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the registered indication text is blank) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 96.36% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, umeclidinium is a long-acting muscarinic antagonist delivered by inhalation, with poor systemic absorption. Its registered use is as a respiratory inhaler, although the approved indication text was not captured.

A link to migraine is speculative. Muscarinic signalling has been proposed to modulate trigeminovascular and cortical pathways, but this has not been established for an inhaled, locally acting agent with minimal central nervous system exposure. The high TxGNN score reflects graph-based proximity, not supporting clinical data.

Other top-ranked predictions are also weakly supported:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Migraine with brainstem aura | 95.83% | Likely reflects proximity to the parent migraine node. No plausible mechanism at low systemic exposure. |
| 3 | Open-angle glaucoma | 93.28% | Anticholinergics can raise intraocular pressure. Likely a risk signal rather than a benefit. |
| 4 | Primary hereditary glaucoma | 92.91% | Muscarinic antagonism is expected to be neutral or harmful. |
| 5 | Nephrogenic syndrome of inappropriate antidiuresis | 92.03% | Driven by AVPR2 variants. No known activity at this receptor. |
| 6 | Gastroduodenitis | 91.91% | Weak class-level rationale. Systemic exposure is too low. |
| 7 | Common cold | 91.74% | Intranasal anticholinergics reduce rhinorrhoea. Inhaled delivery is unsuitable. |
| 8 | Atrophoderma vermiculata | 91.24% | No recognised mechanism. |
| 9 | Peptic ulcer disease | 91.05% | Superseded by PPIs and H. pylori eradication. |
| 10 | Allergic urticaria | 90.66% | Histamine-driven. Muscarinic blockade is not a primary mechanism. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports umeclidinium for migraine disorder.

For the lower-ranked prediction of common cold, the only linked document is a COPD review, which does not provide evidence for umeclidinium in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29583021](https://pubmed.ncbi.nlm.nih.gov/29583021/) | 2018 | Review | COPD | Annual review of 2017 COPD studies, including fluticasone furoate/vilanterol/umeclidinium. Not relevant to the common cold. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10187E | Incruse Ellipta | Powder for oral inhalation in breath actuated device, 62.5 micrograms (as bromide) per dose, 30 doses | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified, and 20 are shown in the data compiled. All listed are Moderate severity, mainly additive anticholinergic effects with other antimuscarinic agents. Examples include:
  - Atropine, hyoscyamine, scopolamine
  - Glycopyrronium, aclidinium, trospium
  - Dicyclomine, clidinium, propantheline
  - Promethazine, chlorpheniramine
  - Prucalopride, eluxadoline
  - Inhaled human insulin
- **Glaucoma**: Anticholinergics can cause mydriasis and raise intraocular pressure. Umeclidinium labelling carries a warning for narrow-angle glaucoma, which is directly relevant to the glaucoma predictions.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for migraine disorder rests only on a graph-based model score, with no clinical trials or publications and a speculative mechanism for an inhaled, minimally absorbed drug. The glaucoma predictions may reflect a safety risk rather than a benefit.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm the approved indication, warnings and contraindications
- Mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic evidence for muscarinic involvement in migraine at the exposure levels achieved by inhalation
- Assessment of route compatibility, since inhaled delivery may not reach relevant sites
- Any registered or published studies of umeclidinium or other LAMAs in migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

