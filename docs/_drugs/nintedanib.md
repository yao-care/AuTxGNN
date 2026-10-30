---
layout: default
title: Nintedanib
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Nintedanib"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
description: "Nintedanib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Not recorded in the local data"
---

# Nintedanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nintedanib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Nintedanib is an oral triple angiokinase inhibitor, originally used for idiopathic pulmonary fibrosis and non-small cell lung cancer.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but currently there are **no registered clinical trials** and only **1 indirect review publication** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9915 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. Based on known pharmacology, nintedanib is a triple angiokinase inhibitor targeting PDGFR alpha/beta, FGFR 1-3 and VEGFR 1-3.

DFSP is driven by the COL1A1-PDGFB fusion, which causes constitutive PDGFR-beta signalling. Nintedanib inhibits this receptor family, so the prediction is mechanistically plausible. Its antifibrotic and antiproliferative effects on fibroblasts in pulmonary fibrosis also fit with DFSP, a fibroblast-derived tumour.

The one retrieved paper is a general review of PDGFR inhibitors in neoplastic disorders, which is indirect evidence. Imatinib is the established PDGFR-targeted therapy for DFSP, and no nintedanib-specific clinical data were available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders. It is indirect evidence and does not report nintedanib-specific data in DFSP. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11100F | Ofev | Capsule 100 mg (oral) | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; liver function and FBC monitoring are generally relevant for kinase inhibitors |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the DDI screen, and the first 20 returned are summarised here.
  - **Major**: Dexamethasone.
  - **Moderate, bleeding risk (anticoagulants, antiplatelets, thrombolytics)**: acetylsalicylic acid, abciximab, alteplase, antithrombin III human, apixaban, betrixaban, bivalirudin, cangrelor, caplacizumab, cilostazol, clopidogrel, dalteparin, defibrotide, desirudin, dipyridamole.
  - **Moderate, other**: clarithromycin, cobicistat, naltrexone, rolapitant.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9915) and the PDGFR-driven mechanism is plausible, but there are no clinical trials and only one indirect review. Imatinib is already the established targeted therapy for DFSP, so a nintedanib case would need to show added value.

**To proceed, the following is needed:**
- Nintedanib-specific preclinical data (for example DFSP cell lines or xenograft models with the COL1A1-PDGFB fusion)
- Case series or early-phase trial data in DFSP, ideally imatinib-resistant disease
- Detailed mechanism of action data
- TGA Product Information warnings and contraindications for a safety review
- Review of bleeding risk with anticoagulant and antiplatelet co-medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

