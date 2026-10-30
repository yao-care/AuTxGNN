---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 5
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
last_modified_at: 2026-10-30
description: "Ciclesonide: predicted new indication atopic eczema (evidence level L5). Approved use: Not recorded in the local data"
---

# Ciclesonide
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

## Ciclesonide: inhaled corticosteroid prodrug → atopic eczema
{: .text-alpha }

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid prodrug that is activated to des-ciclesonide in the body. The TxGNN model predicts it may be effective for **atopic eczema**, but the data compiled for this report contain **no clinical trials and no publications** on this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atopic eczema |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ciclesonide is an inhaled corticosteroid prodrug activated by esterases to des-ciclesonide, which acts through the glucocorticoid receptor.

Glucocorticoid receptor-mediated anti-inflammatory activity is plausibly relevant to atopic eczema, for which topical corticosteroids are standard care. This is a mechanistic argument only. The formulation, activation in skin and local safety of ciclesonide for this use are not established.

Other predictions in the data (for example, the closely related term "dermatitis, atopic") are likely redundant ontology entries for the same condition. They should be merged during review and are not treated here as separate findings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14312G | Alvesco 80 | Pressurised inhalation 80 micrograms per dose, 120 doses (CFC-free formulation) | Not recorded in the local data |

The only listed product is an inhaled formulation. No topical presentation is recorded, so route compatibility with atopic eczema is unresolved.

## Safety Considerations

- **Drug Interactions**: 63 interactions were recorded. Examples include:
  - Major: cladribine.
  - Moderate: clarithromycin, miconazole, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, conivaptan, fostamatinib, inhaled rapid-acting insulin, topical abametapir.
  - Minor: formoterol, salbutamol, arformoterol.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9996), but there are no trials or publications on atopic eczema, so evidence is limited to model output (L5). Only an inhaled product is marketed in Australia, and skin delivery and local safety are not established.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of ciclesonide in atopic eczema or other eczematous skin disease
- Route and formulation feasibility assessment, since only an inhaled product is registered
- Full mechanism of action data
- Warnings and contraindications from the TGA Product Information
- Review of the major and moderate drug interactions for any proposed population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

