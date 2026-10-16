---
layout: default
title: Bisacodyl
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bisacodyl: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Constipation disorder"
monitor_inn: "Bisacodyl"
predicted_indications: ["exercise-induced malignant hyperthermia", "dyspepsia", "nephrogenic syndrome of inappropriate antidiuresis", "malignant hyperthermia, susceptibility to", "common cold", "pharyngitis", "familial periodic paralysis", "acute laryngopharyngitis", "malignant hyperthermia of anesthesia", "acute pulmonary heart disease"]
---

# Bisacodyl
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

# Bisacodyl: From Constipation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Bisacodyl is a stimulant laxative, originally used to treat constipation.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder (the approved indication text was not available in the data compiled for this report) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 97.69% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bisacodyl is a stimulant laxative. Its active metabolite (BHPM) acts locally on the colonic mucosa to stimulate peristalsis and secretion, and its efficacy in constipation is established.

No mechanistic link to the predicted indication was identified. Malignant hyperthermia involves dysregulated calcium release in skeletal muscle (for example, RYR1 variants), a pathway on which bisacodyl has no known action. The high TxGNN score is a graph-based prediction and has no supporting biological rationale in the data compiled for this report.

Other top-ranked predictions show the same pattern. Several are related malignant hyperthermia entries (susceptibility, anaesthesia-related), so their scores likely reflect graph proximity rather than independent evidence. The remaining predictions (dyspepsia, nephrogenic syndrome of inappropriate antidiuresis, common cold, pharyngitis, familial periodic paralysis, acute laryngopharyngitis, acute pulmonary heart disease) also have no trials or literature. Dyspepsia is plausible only at a symptom level, and familial periodic paralysis raises a safety concern rather than a potential benefit (see Safety Considerations).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10578R | Dulcolax | Suppositories 10 mg, 10 | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease contraindication links in the TxGNN knowledge graph, not from product label text):
epilepsy, kidney disease, pyoureter, congestive heart failure, potassium deficiency disease, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, ileus, intestinal obstruction, toxic megacolon, appendicitis, atrioventricular block, hyperkalaemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita, *Clostridium difficile* colitis, and anal disease.

**Drug Interactions:** The interaction query returned 100 records. The entries compiled for this report are all rated Moderate. Examples include:
- Diuretics and related agents: furosemide, hydrochlorothiazide, amiloride, acetazolamide
- Corticosteroids: hydrocortisone, triamcinolone
- Salbutamol
- QT-prolonging or arrhythmia-related agents: amiodarone, amisulpride, anagrelide, gilteritinib, gemifloxacin, foscarnet
- Others: abiraterone, tramadol, apalutamide, apomorphine, alfuzosin, fostemsavir, propofol

Many of these interactions are plausibly linked to electrolyte disturbance (for example, potassium loss with diarrhoea), which is relevant to the predicted periodic paralysis indication.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanistic link between bisacodyl's local colonic action and the pathophysiology of malignant hyperthermia. The other top-ranked predictions are similarly unsupported.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), for example from DrugBank
- The TGA-approved Product Information (PI), including approved indication, warnings and contraindications
- A biological rationale linking bisacodyl to the predicted condition, followed by a systematic literature and trial registry search (ClinicalTrials.gov, ANZCTR)
- Review of the knowledge-graph contraindications and electrolyte-related interactions against any proposed new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

