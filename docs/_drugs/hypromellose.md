---
layout: default
title: Hypromellose
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hypromellose: predicted new indication Hepatic veno-occlusive disease-immunodeficiency syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Hypromellose"
predicted_indications: ["hepatic veno-occlusive disease-immunodeficiency syndrome", "pancytopenia due to IKZF1 mutations", "hepatic veno-occlusive disease", "combined immunodeficiency due to CRAC channel dysfunction", "absent thumb-short stature-immunodeficiency syndrome", "facial dysmorphism-immunodeficiency-livedo-short stature syndrome", "immuno-osseous dysplasia", "psoriasis", "autoinflammatory syndrome with pyogenic bacterial infection and amylopectinosis", "human herpesvirus 8-related tumor"]
---

# Hypromellose
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

## Hypromellose: From Ophthalmic Lubricant to Hepatic Veno-Occlusive Disease-Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Hypromellose is an inert, cellulose-derived polymer used as an ophthalmic lubricant (eye drops) and as a pharmaceutical excipient.
The TxGNN model predicts it may be effective for **hepatic veno-occlusive disease-immunodeficiency syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It appears to be a knowledge-graph artefact rather than a biologically grounded finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the single ARTG entry is an eye drop product with no indication text) |
| Predicted New Indication | Hepatic veno-occlusive disease-immunodeficiency syndrome |
| TxGNN Prediction Score | 98.30% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hypromellose is known to be a pharmacologically inert cellulose-derived polymer. It acts as a viscosity enhancer, film former and ophthalmic lubricant, with negligible systemic absorption.

The predicted disease is a rare genetic disorder (SP110 mutation) affecting the liver and immune system. Nothing in the data connects hypromellose to its pathophysiology, and a lubricant acting on the ocular surface has no plausible route to affect it. The high TxGNN score is most likely a knowledge-graph artefact and not a biologically grounded prediction.

For context, the other top-ranked predictions (all with L5 evidence, no trials and no literature) are also unsupported mechanistically:

| Rank | Predicted Disease | TxGNN Score | Mechanistic Assessment |
|------|------|------|------|
| 2 | Pancytopenia due to IKZF1 mutations | 98.15% | No plausible mechanism; genetic haematopoietic disorder |
| 3 | Hepatic veno-occlusive disease | 98.08% | No endothelial-protective or antithrombotic activity; approved therapy (defibrotide) works differently |
| 4 | Combined immunodeficiency due to CRAC channel dysfunction | 98.03% | No interaction with calcium channel signalling |
| 5 | Absent thumb-short stature-immunodeficiency syndrome | 97.94% | No biological rationale |
| 6 | Facial dysmorphism-immunodeficiency-livedo-short stature syndrome | 97.90% | No target engagement |
| 7 | Immuno-osseous dysplasia | 97.88% | No relevant pharmacology |
| 8 | Psoriasis | 97.86% | Weak, indirect rationale only (possible vehicle or film-forming role in topical products, not disease-modifying) |
| 9 | Autoinflammatory syndrome with pyogenic bacterial infection and amylopectinosis | 97.79% | No immunomodulatory activity |
| 10 | Human herpesvirus 8-related tumour | 97.78% | No antiviral or antineoplastic activity |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11625W | Revive Tears | Eye drops 3 mg per mL, 10 mL | Not stated |

The only registered product is an ophthalmic preparation, so the available route (ophthalmic) has not been shown to be compatible with any predicted indication.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5, model prediction only), and no mechanistic link exists between an inert, minimally absorbed ophthalmic polymer and the predicted disease. The high TxGNN score is not supported by biological plausibility.

**To proceed, the following is needed:**
- Any credible mechanistic hypothesis connecting hypromellose to the disease pathophysiology
- Preclinical or clinical evidence for the predicted indication
- Confirmation of the approved indication text for the ARTG entry
- Mechanism of action data and product information warnings and contraindications
- Evaluation of route compatibility, as the only registered product is an eye drop
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

