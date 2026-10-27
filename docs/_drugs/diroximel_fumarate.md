---
layout: default
title: Diroximel Fumarate
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diroximel Fumarate: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Diroximel fumarate"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "tetanic cataract", "mature cataract", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "immature cataract", "craniostenosis cataract"]
---

# Diroximel Fumarate
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

## Diroximel Fumarate: From an Unspecified Original Indication to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Diroximel fumarate is an oral prodrug of monomethyl fumarate and is marketed in Australia as Vumerity, but the data compiled for this report do not record its approved indication.
The TxGNN model predicts it may be effective for **diabetic cataract**, although there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is therefore model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Diroximel fumarate is a prodrug of monomethyl fumarate (MMF), which is generally understood to activate the Nrf2 antioxidant pathway and to have anti-inflammatory activity. This is background knowledge rather than a sourced finding in this dataset.

The original indication was not captured, so the relationship between it and diabetic cataract cannot be assessed directly. The proposed link is that oxidative stress and polyol-pathway damage contribute to lens opacification in diabetes, so Nrf2 activation is a plausible but unvalidated protective mechanism. Systemic drug exposure reaching the lens is unverified.

The same model also ranks several other eye conditions highly: diabetic retinopathy, severe nonproliferative diabetic retinopathy, and multiple cataract subtypes. Many of these scores are almost identical (about 99.999%), which suggests they may reflect shared connections between related disease nodes in the knowledge graph rather than independent evidence. Some predictions, such as tetanic cataract and craniostenosis cataract, have no evident mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13059H | Vumerity | Capsule (enteric) 231 mg | Not recorded in the data compiled for this report |

The route of administration is oral.

## Safety Considerations

- **Drug Interactions**: The interaction screen was completed and returned 100 interactions. The 20 reviewed here were all rated Moderate. They include:
  - Corticosteroids: hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone and prednisone
  - Naltrexone and ethanol
  - Immunomodulating or myelosuppressive agents: mercaptopurine, levamisole, trimetrexate, dexrazoxane, roflumilast and dupilumab
  - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, iobenguane (I-131), tositumomab and tositumomab (I-131)

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no registered trials or publications. The high scores across closely related cataract and retinopathy entries suggest graph similarity rather than independent evidence. Warnings, contraindications and the original indication are also missing from the data compiled for this report.

**To proceed, the following is needed:**
- Confirmation of the approved indication and the full safety profile (warnings and contraindications) from the TGA-approved PI
- Mechanism of action data from DrugBank
- Preclinical evidence that Nrf2 activation protects against diabetic lens or retinal injury, including evidence that systemic dosing reaches ocular tissue
- A literature and trial registry search (including ANZCTR) specific to diabetic cataract and diabetic retinopathy
- A review of the diabetic retinopathy prediction as a possible alternative lead, since the data suggest a more plausible mechanism there than for several of the cataract subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

