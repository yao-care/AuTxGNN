---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Ruxolitinib
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib is an oral JAK1/2 inhibitor, originally used for myeloproliferative neoplasms such as myelofibrosis and polycythaemia vera.
The TxGNN model predicts it may be effective for **uterine corpus PEComa**, but this is a **model prediction only**, with **no clinical trials** and **no publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ruxolitinib is known as a JAK1/2 inhibitor, and its efficacy in myeloproliferative neoplasms is established through dysregulated JAK/STAT signalling.

The mechanistic case for uterine PEComa is weak. PEComa is driven mainly by mTOR pathway activation (loss of TSC1/TSC2), and no link to JAK/STAT inhibition is established in the available data. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Related predictions (benign PEComa, lymphangiomyoma, lymphangioleiomyomatosis, lung PEComa) share the same limitation. Lymphangioleiomyomatosis, for example, is treated mainly by mTOR inhibition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10614P | Jakavi | Tablet 5 mg (oral) | Not listed in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for these.

**Drug Interactions:** The interaction screen returned 100 interacting drugs. Only the first 20 were available for review. Of these, the following are rated **Major**:
- Clarithromycin
- Cobicistat
- Deferasirox
- Deferiprone
- Ibritumomab tiuxetan
- Tositumomab and Tositumomab (I-131)
- Samarium (153Sm) lexidronam

**Moderate** interactions include dexamethasone, rosuvastatin, fenfluramine, dexfenfluramine, sibutramine, troglitazone, palifermin and strontium chloride Sr-89. The remaining reviewed interactions (aprepitant, cimetidine, miconazole, clotrimazole) are rated Minor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no publications and no established mechanistic link to JAK/STAT inhibition. The disease is driven mainly by mTOR signalling.

**To proceed, the following is needed:**
- Preclinical or clinical evidence linking JAK/STAT signalling to PEComa
- Detailed mechanism of action data
- Product Information warnings and contraindications for the Australian product
- Review of the other predicted indications in the same output, which have more supporting data:
  - Hemophagocytic lymphohistiocytosis (HLH), with L3 evidence (mostly non-randomised clinical reports; no registered trials were identified)
  - Myxoid liposarcoma (preclinical JAK-STAT data only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

