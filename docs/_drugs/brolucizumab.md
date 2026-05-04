---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Brolucizumab
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

# Brolucizumab: From Neovascular Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

Brolucizumab is an anti-VEGF-A intravitreal injection used internationally for neovascular age-related macular degeneration (nAMD); formal regulatory data for Australia is not available in the current dataset.
The TxGNN model's top prediction identifies **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies** as a candidate new indication, with a prediction score of **99.67%**.
However, **no clinical trials and no supporting literature** exist for this indication, and across all 10 top-ranked predictions, every candidate is classified at **Evidence Level L5** (model prediction only) — none are currently actionable.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular age-related macular degeneration (nAMD) — referenced from prediction rationale; not formally recorded in current regulatory dataset |
| Predicted New Indication (Rank 1) | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data has not been retrieved from DrugBank for this report. Based on information referenced within the prediction rationale, Brolucizumab is an anti-VEGF-A single-chain antibody fragment (scFv) delivered via intravitreal injection. Its known clinical application is for ophthalmic diseases driven by pathological neovascularisation — most notably nAMD — where VEGF-A inhibition suppresses abnormal blood vessel growth beneath the retina.

Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies is a fundamentally different disease category. It arises from nuclear DNA mutations impairing the mitochondrial respiratory chain complexes (Complexes I–V), leading to defective cellular energy metabolism. The primary pathophysiology involves ATP production failure in high-energy-demand tissues (brain, muscle, heart) — not angiogenesis or VEGF signalling. There is no established mechanistic connection between VEGF-A inhibition and mitochondrial respiratory chain function.

The high TxGNN score (99.67%, ranked 4,470th globally) is most likely attributable to topological noise within the knowledge graph. Rare disease nodes can share graph-structural properties with well-connected drug nodes without reflecting genuine biological plausibility. This pattern is consistent across the top four predictions, which span four entirely unrelated disease categories (mitochondrial disorder, oesophageal varices, exocrine pancreatic insufficiency, and MRCS syndrome) — all biologically disconnected from VEGF-A pharmacology. Clinicians and researchers should interpret these scores as hypothesis-generating signals requiring rigorous biological validation, not as indicators of clinical readiness.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries were returned for Brolucizumab in the current dataset (market status: not marketed, 0 ARTG entries).

> **Action required:** Brolucizumab (brand name Beovu®, Novartis) may be registered with the TGA under a different formulation or entry. Please verify directly via the [TGA ARTG Public Summary Search](https://www.tga.gov.au/resources/artg) or contact Novartis Australia before drawing conclusions about regulatory status.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> Formal safety data (key warnings, contraindications, drug interactions) were not retrieved in this Evidence Pack. Healthcare professionals should consult the Beovu® Australian PI directly, noting that intravitreal anti-VEGF agents as a class carry risks including intraocular inflammation, retinal vasculitis, retinal vascular occlusion, and endophthalmitis. Brolucizumab in particular has post-marketing safety signals relating to intraocular inflammation that are documented in international PI documents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic link between Brolucizumab's known pharmacology (VEGF-A inhibition via intravitreal injection) and mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies. All 10 top TxGNN predictions for this drug are classified as Evidence Level L5, with zero supporting clinical trials and no relevant literature for Brolucizumab in any of these conditions.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm Brolucizumab's ARTG registration status directly with TGA, as the current dataset shows 0 entries
- **Safety data retrieval:** Download and parse the TGA-approved Beovu® Product Information to populate warnings, contraindications, and precautions (particularly regarding intraocular inflammation and retinal vascular occlusion)
- **MOA documentation:** Retrieve formal mechanism of action data from DrugBank (DB14864) to enable mechanistic plausibility analysis
- **Knowledge graph audit:** Investigate why the four highest-scoring predictions (ranks 1–4) are biologically implausible non-ophthalmic conditions; assess whether rare disease node topology is inflating scores
- **Ophthalmic research questions:** Predictions at ranks 6–10 (pigmented paravenous retinochoroidal atrophy, familial flecked retinopathy, ectopia lentis-chorioretinal dystrophy-myopia syndrome, retinal dystrophy in lipidoses, senile reticular retinal degeneration) carry greater biological proximity to Brolucizumab's ophthalmic mechanism. If secondary choroidal neovascularisation (CNV) is a feature of any of these conditions, a targeted literature review and expert ophthalmological consultation would be appropriate before dismissing these as research questions
- **No clinical development investment** is warranted for this candidate at the current evidence stage

---

> ⚠️ **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application. This content is generated by the TxGNN AI model and has not been evaluated by the TGA or any clinical body.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

