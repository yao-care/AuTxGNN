---
layout: default
title: Racementhol
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Racementhol: predicted new indication Acne keloid (evidence level L5). Approved use: Seborrheic dermatitis"
monitor_inn: "Racementhol"
predicted_indications: ["acne keloid", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial", "postinfectious vasculitis", "post-bacterial disorder"]
---

# Racementhol
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

# Racementhol: From Seborrheic Dermatitis to Acne Keloid

## One-Sentence Summary

Racementhol (racemic menthol) is a topical agent whose knowledge-graph indications include seborrheic dermatitis, pityriasis simplex, dermatitis, seborrheic keratosis and pityriasis versicolor.
The TxGNN model predicts it may be effective for **acne keloid**, but there are currently **no clinical trials** and **no publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Seborrheic dermatitis (knowledge-graph indication; the ARTG entry has no indication text) |
| Predicted New Indication | Acne keloid |
| TxGNN Prediction Score | 95.15% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, racementhol is a topical cooling and antipruritic agent that is thought to act through TRPM8 activation. This general knowledge could not be confirmed from the data compiled here.

Its known uses are in inflammatory and scaling skin conditions such as seborrheic dermatitis. Acne keloid is a chronic inflammatory follicular condition. A plausible but unverified link is symptomatic relief of itch or irritation. There is no evidence that racementhol alters scarring or the underlying disease process.

**Other predictions.** The model's other top-ranked predictions are also supported by no clinical evidence:
- **Neurodermatitis** (score 81.2%) has the strongest biological rationale. Its itch-scratch cycle fits menthol's cooling and antipruritic action. Its score is lower than that of acne keloid, but it is the most plausible candidate for follow-up.
- **Amyopathic dermatomyositis** (94.4%) is conceivable only for symptomatic itch relief.
- **Acrodermatitis chronica atrophicans, neonatal dermatomyositis, hydroa vacciniforme, exanthem, postinfectious vasculitis and post-bacterial disorder** have weak or non-specific rationales. Menthol is also generally avoided in neonates and young children because of the risk of respiratory irritation or apnoea.
- **Childhood secondary interstitial lung disease** (94.6%) is a pulmonary condition with no relevant route or mechanism for a topical dermatological agent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 7308P | Not recorded | Not recorded | Not recorded |

The entry is a valid single-ingredient licence. Manufacturer and indication text are not recorded in the data compiled for this report.

## Safety Considerations

Product-specific warnings, contraindications and drug interaction data were not available. Please refer to the TGA-approved Product Information (PI) for safety information.

The TxGNN knowledge graph lists the following conditions as drug-disease contraindication edges. This is not label text and should be verified against the PI:
- **Liver and gallbladder:** liver failure, liver disease, gallbladder disease
- **Kidney and urinary:** kidney disease, pyoureter
- **Gastrointestinal:** gastritis
- **Blood and iron:** sickle cell anaemia, hereditary persistence of fetal haemoglobin, methaemoglobinaemia, sulfhaemoglobinaemia, blood coagulation disease, haemophilia, anaemia, macrocytic anaemia, G6PD deficiency, hereditary haemochromatosis, haemosiderosis, iron metabolism disease
- **Metabolic and genetic:** diabetes mellitus, diabetic ketoacidosis, primary hyperoxaluria, Wilson disease, glycogen storage disease, cystinuria, galactosaemia
- **Cardiac and neurological:** sudden cardiac arrest, heart conduction disease, epilepsy
- **Skin infections:** anogenital human papillomavirus infection, common wart

Menthol should also be used with caution in infants and young children.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne keloid prediction rests only on a model score (95.15%), with no trials, no publications and no confirmed mechanism (Evidence Level L5). The acne keloid link is speculative, limited at most to symptom relief.

**To proceed, the following is needed:**
- A literature search on topical menthol in chronic pruritus and inflammatory follicular conditions, prioritising **neurodermatitis**, which has the strongest rationale
- Mechanism of action data (for example from DrugBank)
- The TGA Product Information (warnings, contraindications, indications and dosage form for ARTG 7308P)
- Confirmation of route compatibility between the marketed product and the proposed indication
- An age-specific safety assessment before considering use in children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

