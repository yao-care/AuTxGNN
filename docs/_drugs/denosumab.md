---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 2
monitor_inn: "Denosumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
last_modified_at: 2026-11-17
description: "Denosumab: predicted new indication severe nonproliferative diabetic retinopathy (evidence level L5). In Australia: 5 PBS items (5 currently listed)"
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Denosumab: RANKL inhibitor (monoclonal antibody) → severe nonproliferative diabetic retinopathy
{: .text-alpha }

## One-Sentence Summary

Denosumab is a monoclonal antibody that inhibits RANKL and is marketed in Australia as an injectable product.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but **no clinical trials and no publications** directly studying this disease are currently available, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (5 of 5 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for denosumab: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), label version 2026-11-04; accessed 2026-11-19.) Denosumab is a monoclonal antibody directed against RANKL, a signalling molecule in the RANK pathway, and it is known as a bone-targeted therapy.

A plausible but unproven link is that RANKL/RANK signalling is involved in inflammation and vascular biology, which could in principle touch on retinal microvascular disease. No direct data support an effect of denosumab on the retina. The high TxGNN score (0.9963) is a model-based prediction only and should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10061M | Wyost | Injection 120 mg in 1.7 mL | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. The ones listed here are all rated Moderate:
  - Corticosteroids: hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone
  - Immunosuppressants and immune-modulating agents: tacrolimus, dupilumab, levamisole, corticotropin, tetracosactide
  - Antimetabolites and radiopharmaceutical agents: mercaptopurine, trimetrexate, ibritumomab tiuxetan, iobenguane (I-131), tositumomab and tositumomab (I-131)

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials or publications that directly study severe nonproliferative diabetic retinopathy, so the evidence level is L5. The only related papers address denosumab in type 2 diabetes and do not show any retinal benefit.

**To proceed, the following is needed:**
- Preclinical or mechanistic studies of RANKL/RANK signalling in diabetic retinal disease
- Observational or registry data on retinopathy outcomes in people taking denosumab
- Product Information warnings and contraindications for safety review
- Detailed mechanism of action data
- An Australian-relevant safety and dosing plan if a trial in this population is considered

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

