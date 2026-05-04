---
layout: default
title: Bimekizumab
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: From Plaque Psoriasis to Diabetic Cataract

## One-Sentence Summary

Bimekizumab is a dual IL-17A and IL-17F inhibitor approved in multiple countries for inflammatory conditions including plaque psoriasis and psoriatic arthritis.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, with a prediction score of 98.23%.
However, with **0 clinical trials** and **0 publications** supporting this direction, evidence is limited to model prediction only (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory data (globally approved for plaque psoriasis and related inflammatory conditions) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bimekizumab is a humanised monoclonal antibody that uniquely inhibits both IL-17A and IL-17F — two cytokines that share the IL-17RA/IL-17RC receptor complex and act synergistically to drive chronic inflammatory cascades. By blocking both isoforms simultaneously, Bimekizumab provides broader suppression of the IL-17 signalling axis compared with IL-17A-only inhibitors (such as secukinumab or ixekizumab). Its approved indications — plaque psoriasis, psoriatic arthritis, and axial spondyloarthritis — all share a common pathological thread of dysregulated IL-17-driven tissue inflammation.

The theoretical link to diabetic cataract is mechanistically indirect. IL-17A and IL-17F are upregulated in the diabetic inflammatory milieu, and via NF-κB activation they may theoretically contribute to oxidative stress that could influence lens transparency. However, this connection is highly speculative for several reasons: (1) diabetic cataract is primarily driven by hyperglycaemia-induced lens protein glycation and polyol pathway activation, not by IL-17-mediated inflammation; (2) no preclinical or clinical data exist exploring anti-IL-17 therapy in cataract prevention or treatment; and (3) the definitive treatment for cataract remains surgical lens extraction, leaving an extremely narrow window for pharmacological intervention.

Importantly, a notable pattern in this Evidence Pack warrants caution: nine of the top ten TxGNN predictions are cataract subtypes (ranks 16,888–18,469). This clustering strongly suggests the model is generalising from disease-ontology adjacency — cataract subtypes sharing a large knowledge graph node — rather than reflecting a true biological signal. The one non-cataract prediction (antithrombin deficiency type 2) is similarly without plausible mechanistic rationale. Overall mechanistic plausibility for this repurposing direction is assessed as low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are currently on file for Bimekizumab.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No entries found | — | — |

> **Note for clinicians:** Bimekizumab (brand name Bimzelx) has received regulatory approvals in the EU, UK, USA, Canada, and Japan for plaque psoriasis and related inflammatory conditions. Clinicians should verify the current TGA registration status directly via the ARTG online search at [www.tga.gov.au](https://www.tga.gov.au), as registration status may have changed after the data cutoff date of 5 April 2026.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Bimekizumab in diabetic cataract is supported only by model output with no clinical trials, no peer-reviewed literature, and a mechanistically weak biological rationale. The clustering of nine cataract subtypes within the top ten predictions is a strong indicator of a model artefact (ontology-adjacency false positive) rather than a genuine drug repurposing signal — this prediction should not progress to clinical development planning at this stage.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or in vivo) demonstrating a functional role for IL-17A/F in lens protein aggregation, lens epithelial cell apoptosis, or cataractogenesis
- Published literature linking any anti-IL-17 biologic to ocular inflammatory or degenerative endpoints
- Verification of current TGA/ARTG registration status for Bimekizumab in Australia
- Full safety and contraindication profile from the approved Product Information (PI), including immunosuppression risks relevant to ophthalmic use
- A mechanistic hypothesis that moves beyond disease-ontology adjacency before any further investment in this indication is considered

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

