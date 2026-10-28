---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 5
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-10-28
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Calcitriol: active form of vitamin D (hormonal vitamin D metabolite) → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active hormonal form of vitamin D and is marketed in Australia as an oral capsule.
The TxGNN model predicts it may be relevant to **obsolete vitamin D deficiency** (a disease term flagged as obsolete in the ontology).
**No clinical trials and no publications** were found for this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Calcitriol is the active form of vitamin D, so a mechanistic link to vitamin D deficiency is biologically plausible.

There are important caveats. The disease term is flagged as obsolete in the ontology, so it may not map cleanly onto a current clinical diagnosis. Nutritional vitamin D deficiency is usually treated with cholecalciferol or ergocalciferol rather than calcitriol, which is the already-activated hormone. The high TxGNN score is a model prediction only and is not supported by trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13457G | Rocaltrol | Capsule 0.25 microgram (oral) | Not recorded in the local data |

---

## Safety Considerations

- **Drug Interactions** (100 interactions recorded in total; main examples):
  - **Major:** cholecalciferol, calcifediol, burosumab. Co-administration with other vitamin D products or analogues risks additive effects, including hypercalcaemia.
  - **Moderate:**
    - Thiazide diuretics (hydrochlorothiazide, bendroflumethiazide, chlorothiazide, chlorthalidone, benzthiazide)
    - Enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital)
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
    - Digoxin and digitoxin
    - Aluminium hydroxide
    - Topical calcipotriol

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications. The disease term is obsolete, and standard care for nutritional vitamin D deficiency uses other vitamin D forms. The evidence level is L5.

**To proceed, the following is needed:**
- Clarification of which current clinical diagnosis the obsolete disease term corresponds to
- Evidence from trials or studies that directly address this condition with calcitriol
- Mechanism of action data and TGA Product Information warnings and contraindications
- A comparison against standard vitamin D supplementation (cholecalciferol or ergocalciferol), including a hypercalcaemia monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

