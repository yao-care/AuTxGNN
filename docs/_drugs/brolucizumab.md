---
layout: default
title: Brolucizumab
parent: Model Prediction Only (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brolucizumab: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA a… (evidence level L5). Approved use: Macular degeneration"
monitor_inn: "Brolucizumab"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices with bleeding", "esophageal varices without bleeding", "exocrine pancreatic insufficiency", "MRCS syndrome", "pigmented paravenous retinochoroidal atrophy", "familial flecked retinopathy", "ectopia lentis-chorioretinal dystrophy-myopia syndrome", "retinal dystrophy in systemic or cerebroretinal lipidoses", "senile reticular retinal degeneration"]
---

# Brolucizumab
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

## Brolucizumab: From Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder (Nuclear DNA Anomalies)
{: .text-alpha }

## One-Sentence Summary

Brolucizumab is an anti-VEGF-A antibody fragment given by intravitreal injection, originally used to treat macular degeneration.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration (the approved indication text is not listed on the ARTG entry in the data compiled for this report) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, brolucizumab is a single-chain antibody fragment that inhibits VEGF-A. Its use in macular degeneration is established, and its action is on VEGF-driven pathological angiogenesis and vascular leakage in the eye.

The link to the predicted indication is weak. Mitochondrial oxidative phosphorylation disorders caused by nuclear DNA anomalies arise from defects in nuclear-encoded respiratory chain components, and there is no obvious dependence on VEGF-A. Any connection would be speculative, for example through retinal manifestations or hypoxia signalling. The high TxGNN score (0.997) is a graph-based prediction only and is not backed by mechanistic or clinical data here.

**Other predicted indications (all L5, all Hold):** The model also ranked nine further conditions. None has any registered clinical trials or literature in the data compiled for this report.

| Rank | Predicted Indication | TxGNN Score | Comment |
|---|---|---|---|
| 2 | Oesophageal varices with bleeding | 99.12% | VEGF-driven angiogenesis in portal hypertension is theoretical only. Anti-VEGF is not an established approach, and thromboembolic risk is a concern in acute bleeding. |
| 3 | Oesophageal varices without bleeding | 99.12% | Identical score to the bleeding variant, suggesting the model does not distinguish between these closely related nodes. |
| 4 | Exocrine pancreatic insufficiency | 99.07% | A digestive enzyme deficiency, not known to be VEGF-A driven. No plausible direct mechanism. |
| 5 | MRCS syndrome | 98.54% | Rare syndrome. Any link to VEGF inhibition is speculative. |
| 6 | Pigmented paravenous retinochoroidal atrophy | 98.33% | Ocular tissue and intravitreal route overlap, but neovascularisation is not a primary driver. Intraocular inflammation risk would need careful consideration. |
| 7 | Familial flecked retinopathy | 97.90% | Inherited retinal disorder without a known VEGF-driven component. |
| 8 | Ectopia lentis-chorioretinal dystrophy-myopia syndrome | 97.82% | Relevant only if secondary choroidal neovascularisation develops. Indirect. |
| 9 | Retinal dystrophy in systemic or cerebroretinal lipidoses | 97.73% | Driven by lysosomal storage and neurodegeneration, not VEGF. |
| 10 | Senile reticular retinal degeneration | 97.71% | Closest to the approved macular context, but generally non-neovascular and without evidence of VEGF dependence. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12667Q | Beovu | Solution for intravitreal injection 19.8 mg in 0.165 mL pre-filled syringe | Not listed in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signals (not label text):** Uveitis, iris disease, ciliary body disease, panuveitis, eye infectious disease and conjunctivitis.

No drug interaction records were found. For key warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature, and no plausible mechanistic link to VEGF-A inhibition. The intravitreal route and ocular inflammation-related contraindication signals also make extrapolation to non-ocular conditions difficult.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic analysis
- Product Information warnings and contraindications from the TGA-approved PI, to complete safety screening
- Any preclinical or clinical evidence linking VEGF-A inhibition to the predicted condition
- Route compatibility assessment, since the available intravitreal formulation may not suit non-ocular indications
- If any indication is pursued, the ocular candidates (for example senile reticular retinal degeneration) have the most plausible context and would be the logical starting point for a literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

