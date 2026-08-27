---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pegfilgrastim: From Neutrophil-Support Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a pegylated G-CSF (granulocyte colony-stimulating factor) analogue whose established pharmacological role is stimulating bone marrow neutrophil production; formal original-indication licensing text is not available in this Evidence Pack. The TxGNN model predicts possible efficacy in **severe nonproliferative diabetic retinopathy**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in Evidence Pack (known pharmacological role: G-CSF analogue supporting neutrophil production) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not formally available for this candidate (flagged as a High-severity data gap). Based on the information present in the repurposing rationale, Pegfilgrastim is a pegylated G-CSF analogue that acts on bone marrow G-CSF receptors to promote neutrophil generation — this is its well-established clinical role, though the Evidence Pack does not record a formal licensed indication text.

The link to severe nonproliferative diabetic retinopathy rests on a speculative hypothesis: that G-CSF-mediated mobilisation of bone marrow stem cells could support repair of ischaemic retinal tissue. This is explicitly flagged in the evidence as mechanistically uncertain, and there is a competing concern in the literature that G-CSF may promote or worsen angiogenesis-related vascular pathology — a direction that could be counterproductive in a disease characterised by abnormal retinal vascular proliferation.

It is also worth noting that this candidate sits within a cluster of related predictions (diabetic retinopathy, diabetic cataract, senile cataract, cortical cataract, nuclear senile cataract) that likely reflect shared "diabetes-related comorbidity" nodes in the knowledge graph rather than distinct direct pharmacological mechanisms. Separately, one lower-ranked candidate in this same prediction set (drug-induced osteoporosis) appears to directly contradict known G-CSF pharmacology, since G-CSF agents are associated with bone marrow expansion and bone pain rather than protection against bone loss — this reinforces that these predictions require independent mechanistic verification before any further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an Evidence Level L5 (model prediction only) candidate with no supporting clinical trials or literature, no confirmed original-indication data, and no TGA/ARTG market presence in Australia. The proposed mechanistic link is speculative and potentially conflicts with known G-CSF pharmacology (pro-angiogenic effects vs. a disease of pathological retinal vascularisation).

**To proceed, the following is needed:**
- Formal Product Information / TGA labelling data, including warnings and contraindications (currently a Blocking data gap)
- Verified mechanism-of-action documentation from a primary source (e.g., DrugBank/TGA PI)
- Preclinical or mechanistic studies specifically addressing G-CSF's effect on diabetic retinal vasculature, given the plausible conflicting-direction signal
- At minimum, early-phase clinical or observational data before this candidate can be re-scored above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

