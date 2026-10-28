---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 567
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Phenol: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "phenol"
predicted_indications: ["acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "dry eye syndrome"]
---

# Phenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Phenol: From Dermatitis to Acrodermatitis Chronica Atrophicans
{: .text-alpha }

## One-Sentence Summary

Phenol is an antiseptic and chemical agent, here in a topical gel (Egopsoryl-TA), and dermatitis is listed as its original indication.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is recorded for the Australian listing) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, phenol is a topical antiseptic and chemical agent, its original indication is dermatitis, and no mechanism has been established that would make it applicable to the predicted condition.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of Lyme borreliosis, and it is treated with antibiotics. Phenol has no known antimicrobial or anti-inflammatory mechanism relevant to this disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. Neonatal and amyopathic dermatomyositis, familial hydroa vacciniforme, paediatric connective tissue disease-associated interstitial lung disease and severe non-proliferative diabetic retinopathy all lack supporting evidence. Several of them (neonatal skin, lung, eye) also raise serious safety concerns, because phenol is toxic and absorbed through the skin.

The only prediction with any related literature is **acne keloid**, ranked 5th (score 0.9994). A single observational paper (PMID 17204096) describes a modified phenol peel (Exoderm) for facial wrinkles and acne scars in Asian patients. Phenol peels cause controlled dermal injury and remodelling, which is plausibly relevant to scarring. This is indirect evidence only, and keloid-specific efficacy and safety have not been shown. It is best treated as a research question rather than a candidate for adoption.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for acrodermatitis chronica atrophicans.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4505D | Egopsoryl-TA | Topical gel, 30 g (phenol 2.5% in a multi-ingredient formulation) | Not recorded |

## Cytotoxicity

Phenol is not an antineoplastic agent, so this section does not apply.

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Knowledge-graph contraindication signals** (from drug-disease graph links, not label text): epilepsy, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, sudden cardiac arrest, heart conduction disease and atrioventricular block, respiratory failure, peripheral vascular and arterial disease, active peptic ulcer disease, herpes simplex, herpes zoster, cytomegalovirus infection, anogenital HPV infection, common wart, cancer, lymphoma and related conditions, and progressive multifocal leukoencephalopathy. These graph links are unverified and need confirmation against the product label.
- Phenol is toxic and absorbed through skin. Neonatal, ocular and inhalational exposure are particular concerns. Phenol peels have been associated with arrhythmia, hypopigmentation and scarring.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model output only (L5), with no clinical trials, no relevant literature and no plausible mechanism. Phenol's toxicity profile adds further concern. The acne keloid prediction (L4) is the only one with any indirect support, and it remains a research question.

**To proceed, the following is needed:**
- Mechanism of action data for phenol and the Egopsoryl-TA formulation
- The TGA Product Information, including warnings and contraindications
- A documented approved indication for the Australian listing
- For acne keloid, controlled studies of phenol-based treatment specific to keloid and acne scarring, with safety data
- For acrodermatitis chronica atrophicans, any biological rationale showing a benefit beyond standard antibiotic therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

