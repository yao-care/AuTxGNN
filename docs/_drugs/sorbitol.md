---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 686
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Sorbitol: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not available"
monitor_inn: "sorbitol"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Sorbitol: From an Unspecified Original Indication to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Sorbitol is a sugar alcohol used as an osmotic laxative, and it is registered in Australia in a combination enema product (Micolette). No original indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text recorded for the registered product) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sorbitol is a sugar alcohol that acts as an osmotic laxative. It is also used as a sweetener and as an irrigating solution. In Australia it is present in a combination enema product, and its approved indication is not recorded in the data compiled for this report.

Malignant hyperthermia is a pharmacogenetic disorder of skeletal muscle calcium regulation, commonly involving *RYR1* or *CACNA1S* variants. It is triggered by volatile anaesthetics or succinylcholine. The standard treatment is dantrolene, which acts on the ryanodine receptor. No established pathway links sorbitol to this mechanism. Any connection, for example through osmotic or fluid-balance effects, would be speculative and is not supported by the available data.

The high TxGNN score (a model-based prediction only) should therefore be treated as a hypothesis-generating signal, not as evidence of likely efficacy.

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
| 14534Y | Micolette | Enemas 3.125 g-450 mg-45 mg in 5 mL, 12 | Not recorded |

---

## Safety Considerations

- **Contraindications (model signal, not label text)**: The TxGNN model (deep learning) flags a drug-disease contraindication link with **active peptic ulcer disease**; this reflects similarities the model learned between related diseases, not biological evidence.
- **Drug Interactions** (2 recorded):
  - **Tolevamer**: Major
  - **Lamivudine**: Moderate

Product-level warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). There are no registered trials or publications, no plausible mechanistic link to the pathophysiology of malignant hyperthermia, and the product-level safety information is incomplete. Malignant hyperthermia is a life-threatening condition with an established, specific treatment (dantrolene), so an unsupported prediction should not guide practice.

**To proceed, the following is needed:**
- Mechanism of action data for sorbitol, and a plausible, testable link to ryanodine receptor or skeletal muscle calcium regulation
- The approved indication and PI warnings and contraindications for Micolette
- A systematic literature search and preclinical evidence (for example, in vitro or animal models of malignant hyperthermia)
- Clarification of route compatibility, since the registered product is an enema and the predicted indication would likely need a different route and formulation
- A review of the knowledge-graph contraindication (active peptic ulcer disease) and the major interaction with tolevamer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

