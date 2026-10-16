---
layout: default
title: Lactose
parent: Model Prediction Only (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lactose: predicted new indication Esophageal varices with bleeding (evidence level L5). Approved use: Lactose intolerance"
monitor_inn: "lactose"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding", "varicose disease", "Steel syndrome", "cystinosis", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Immunoerythromyeloid hypoplasia", "familial apolipoprotein C-II deficiency", "hypophosphatasia"]
---

# Lactose
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

# Lactose: From Lactose Intolerance to Esophageal Varices with Bleeding

## One-Sentence Summary

Lactose is a disaccharide sugar, originally used in products for managing lactose intolerance.
The TxGNN model predicts it may be effective for **esophageal varices with bleeding**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lactose intolerance |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lactose is a dietary disaccharide and a common pharmaceutical excipient. No mechanistic link to esophageal varices with bleeding has been identified.

The high prediction score appears to be a knowledge-graph artefact rather than an independent biological signal. One possible source of confusion is lactulose, a different compound used in hepatic encephalopathy (a complication of liver disease), which may be conflated with lactose in graph embeddings. The same-score prediction for esophageal varices without bleeding supports the view that these are neighbouring-node effects.

Other top-ranked predictions (varicose disease, Steel syndrome, cystinosis, hypophosphatasia and others) likewise have no identified mechanism and no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8587Y | Kindergen | Oral powder 400 g | Not available |
| ARTG 2870C | Renastart | Oral powder 400 g, 6 | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanism. It is most likely a knowledge-graph artefact, so it does not currently justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data for lactose and a credible biological rationale for esophageal varices
- Confirmation that the prediction is not driven by confusion with lactulose or other related compounds
- Any preclinical or clinical evidence supporting the proposed indication
- Approved indication text and safety information from the Product Information for the registered products
- Assessment of route compatibility and a safety screen before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

