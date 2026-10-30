---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 620
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
description: "Raloxifene: predicted new indication Duodenal ulcer (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Raloxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Raloxifene: Duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM), originally used to treat and prevent postmenopausal osteoporosis.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but this is a computational prediction only, with **no clinical trials** and **no relevant publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal ulcer (disease) |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, raloxifene is a SERM that acts as an estrogen agonist in bone and an antagonist in some other tissues. Its efficacy in postmenopausal osteoporosis is established.

No mechanistic link between raloxifene and duodenal ulcer is supported by the data compiled for this report. The high TxGNN score (0.9972) is a computational output only. Duodenal ulcer is mainly driven by *Helicobacter pylori* infection, NSAID use and acid secretion, and none of these relates to raloxifene's known pharmacology. The prediction is best regarded as hypothesis-generating.

For context, the other top predictions are also unsupported by any trials or literature:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hypoalphalipoproteinemia | 0.9965 | L5 | Raloxifene modestly lowers LDL cholesterol, but no evidence of an HDL effect |
| 3 | Duodenal obstruction | 0.9964 | L5 | Largely mechanical; likely a model artefact |
| 4 | Duodenogastric reflux | 0.9959 | L5 | No supported mechanism |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for duodenal ulcer.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13426P | Evista | Tablet containing raloxifene hydrochloride 60 mg (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not label text):** hypertensive disorder, hypertension, liver disease, gallbladder disease, atrial fibrillation, hypertriglyceridemia, thrombophlebitis, coronary artery disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, pulmonary embolism, retinal artery occlusion, thrombophilia, impaired renal function, transient ischemic attack, vertebrobasilar insufficiency, and antiphospholipid syndrome.
- **Drug Interactions:** The interaction query returned 100 records, none with a severity rating. Examples include calcitriol, pantoprazole, omeprazole, lansoprazole, glimepiride, metformin, simvastatin, doxycycline, tetracycline, morphine and sucralfate. Clinical significance cannot be judged from these data.

For complete warnings and precautions, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanistic link. The safety profile, including the thromboembolic and cardiovascular contraindications, also offers no offsetting benefit.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking raloxifene to duodenal ulcer
- A systematic literature search and review of trial registries (including ANZCTR) for any relevant studies
- Approved indication text and warnings/contraindications from the TGA Product Information, and graded interaction severity data
- Preclinical or exploratory evidence before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

