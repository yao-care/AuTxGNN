---
layout: default
title: Quinine
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Quinine: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Malaria (including Plasmodium falciparum malaria)"
monitor_inn: "Quinine"
predicted_indications: ["Smouldering systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia", "systemic mastocytosis", "nephrogenic syndrome of inappropriate antidiuresis", "thoracic malformation", "polycystic kidney disease 3 with or without polycystic liver disease", "trigeminal nerve neoplasm", "renal-hepatic-pancreatic dysplasia", "adult familial nephronophthisis-spastic quadriparesia syndrome", "karyomegalic interstitial nephritis"]
---

# Quinine
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

## Quinine: From Malaria to Smouldering Systemic Mastocytosis
{: .text-alpha }

## One-Sentence Summary

Quinine is an antimalarial medicine, originally used to treat malaria, including *Plasmodium falciparum* malaria.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, but this is a computational prediction only,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (including *Plasmodium falciparum* malaria) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 96.90% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, quinine is an established antimalarial, and its efficacy in malaria is proven. Mechanistically, however, no link to smouldering systemic mastocytosis has been established.

Quinine is known to block potassium channels and has other ion-channel activity, but nothing in the data compiled for this report connects this to mast cell proliferation or KIT-driven disease. The high score (0.969) most likely reflects how closely related disease entries sit together in the knowledge graph.

The three top predictions (smouldering systemic mastocytosis, lymphoadenopathic mastocytosis with eosinophilia, and systemic mastocytosis) are closely related disease nodes, so they should not be treated as independent evidence. Approved targeted therapies for mastocytosis (KIT inhibitors) work through a very different mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

(One publication, PMID 11743679, was retrieved for a lower-ranked prediction, thoracic malformation. It is a 2001 case report on imported malaria and is not relevant to the predicted indication, so it is not counted as evidence.)

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1975Y | Quinate | Tablet containing quinine sulfate dihydrate 300 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** long QT syndrome (including familial), torsades de pointes, atrial fibrillation and flutter, liver disease, gallbladder disease, thrombocytopenia and thrombocytopenic purpura, haemolytic-uraemic syndrome, myasthenia gravis and other neuromuscular junction disease, hypoglycaemia, chronic kidney disease and end-stage renal failure, optic neuritis, and blackwater fever.
- **Drug Interactions:** 100 interactions were identified. Those rated **Major** include loperamide, clarithromycin, dolasetron, picosulfuric acid, sodium sulfate, and polyethylene glycol (3350 with electrolytes). Examples rated Moderate include famotidine, aprepitant, dexamethasone, bisacodyl, palonosetron, and several antidiabetic agents (chlorpropamide, glimepiride, insulins). Many of the major interactions relate to QT prolongation or electrolyte disturbance.
- **Other considerations:** Quinine's known hyponatraemia and renal adverse-event profile argues for caution in the lower-ranked renal predictions.

Please also refer to the TGA-approved Product Information (PI) for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials, no supporting literature, and no established mechanistic link. Quinine also carries significant cardiac, haematological and drug-interaction risks.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible biological link to mast cell disease
- Preclinical studies (for example in KIT-mutant mast cell models) or a systematic literature search
- TGA Product Information, including warnings, contraindications and approved indications for the ARTG entry
- A risk-benefit assessment against approved targeted therapies for mastocytosis, including QT and interaction risks
- Route and dosing compatibility assessment for the oral tablet formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

