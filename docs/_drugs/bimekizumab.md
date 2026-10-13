---
layout: default
title: Bimekizumab
parent: Model Prediction Only (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: From Immune-Mediated Inflammatory Disease to Diabetic Cataract

## One-Sentence Summary

Bimekizumab is a monoclonal antibody that neutralises IL-17A, IL-17F and IL-17AF. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on its known drug class, bimekizumab neutralises the cytokines IL-17A, IL-17F and IL-17AF, which drive inflammatory signalling.

Chronic low-grade inflammation and oxidative stress have been proposed as contributors to diabetic lens damage, and IL-17 signalling has been implicated in some diabetic complications. However, there is no established role for IL-17A/F in cataract formation. Hyperglycaemia-driven polyol pathway activity and oxidative stress are the main recognised drivers of diabetic lens damage.

The mechanistic link is therefore **speculative**. The high score is a graph-based prediction, and several other cataract subtypes share near-identical scores (about 98.1%), which suggests the result reflects similarity between cataract-related nodes in the knowledge graph rather than a biological rationale.

Other top-ranked predictions are similarly weak:
- Cataract subtypes (mature, immature, tetanic, craniostenosis, nuclear senile, cortical, senile, and type 2 diabetes-associated cataract): no plausible link between IL-17A/F inhibition and lens opacity. Established mature cataract is treated surgically.
- Antithrombin deficiency type 2: a hereditary SERPINC1 variant disorder that IL-17A/F neutralisation would not correct.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13644D | Bimzelx | Injection 160 mg in 1 mL single use pre-filled pen | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interaction records were found in the data compiled for this report, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a computational score, with no clinical trials or literature (Evidence Level L5). The mechanistic link between IL-17A/F inhibition and diabetic cataract is speculative, and safety data for this drug are incomplete.

**To proceed, the following is needed:**
- The approved indication text and Product Information (warnings and contraindications) for Bimzelx, which are currently missing and block safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic evidence for IL-17A/F involvement in diabetic lens damage
- A systematic literature search to confirm whether any relevant studies exist
- Route compatibility assessment (bimekizumab is a subcutaneous injection, whereas ocular disease may need different delivery considerations)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

