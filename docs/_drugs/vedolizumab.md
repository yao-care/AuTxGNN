---
layout: default
title: Vedolizumab
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vedolizumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Crohn's disease, ulcerative colitis and inflammatory bowel disease"
monitor_inn: "Vedolizumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "dermatitis", "neonatal dermatomyositis", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "bronchitis", "drug-induced osteoporosis"]
---

# Vedolizumab
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

# Vedolizumab: From Inflammatory Bowel Disease to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Vedolizumab is a gut-selective monoclonal antibody originally used to treat Crohn's disease and ulcerative colitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are **no registered clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, ulcerative colitis and inflammatory bowel disease (from the knowledge graph; the ARTG indication text is not available) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 94.51% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, vedolizumab is an antibody that blocks α4β7 integrin, which limits the homing of lymphocytes to the gut. Its efficacy in inflammatory bowel disease is established.

A mechanistic link to diabetic retinopathy is not supported by the data. Diabetic retinopathy is driven mainly by hyperglycaemia-induced microvascular damage, VEGF signalling and retinal inflammation, none of which clearly depend on gut-selective lymphocyte trafficking. The high score (0.945) is a graph-based prediction only.

The other predicted indications (dermatitis, dermatomyositis forms, bronchitis, drug-induced osteoporosis and others) are also Hold. For dermatitis, the literature mostly reports vedolizumab as a cause of skin reactions, not a treatment, so that direction may be a safety signal rather than a therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10384M | Entyvio | Powder for injection 300 mg | Not available in the data compiled for this report |

Vedolizumab is available only as an injectable product. Route compatibility with any retinal indication has not been assessed.

## Safety Considerations

- **Drug Interactions**: The interaction query identified 69 interacting drugs, mostly with immunosuppressive or immunomodulatory agents and live vaccines. The following are flagged **Major**:
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
- Several **Moderate** interactions were also listed, including azathioprine, alemtuzumab, anakinra, canakinumab, denosumab, dimethyl fumarate, diroximel fumarate, roflumilast, alefacept, and some vaccines (anthrax, tetanus toxoid, live cholera). Interactions with zinc salts are Minor.
- The literature for related predictions reports skin reactions linked to vedolizumab, including atopic, psoriasiform and acneiform eruptions and hidradenitis suppurativa. These are case-level observations.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it, and no plausible mechanistic link between gut-selective integrin blockade and diabetic retinopathy is supported by the data. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale for retinal disease
- Preclinical or observational evidence in diabetic retinopathy
- The approved indication text and the PI warnings and contraindications for the ARTG entry
- An assessment of whether systemic injectable dosing is suitable for this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

