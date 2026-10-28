---
layout: default
title: Trastuzumab
parent: Model Prediction Only (L5)
nav_order: 748
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
monitor_inn: "Trastuzumab"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: predicted new indication Malignant cutaneous granular cell skin tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## One-Sentence Summary

Trastuzumab is a HER2-targeted monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
The model's other predictions for related breast cancer subtypes (progesterone-receptor positive and negative disease) have far stronger support and are summarised below for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant cutaneous granular cell skin tumor |
| TxGNN Prediction Score | 0.9948 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, trastuzumab binds the extracellular domain of HER2, inhibiting HER2 signalling and mediating antibody-dependent cellular cytotoxicity (ADCC). Its efficacy in HER2-positive breast cancer is well established.


---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07669610](https://clinicaltrials.gov/study/NCT07669610) | Phase 3 | Not yet recruiting | 140 | Open-label randomised study of trastuzumab rezetecan (a different HER2-directed ADC) with or without bevacizumab in basal-like, immune-suppressed triple-negative breast cancer. No results, and no direct evidence for trastuzumab. |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Cohort | Breast Cancer (Tokyo) | Morphological and cytopathological features of basal-like breast carcinoma. Descriptive only, with no treatment evidence. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10383L | Ogivri | Powder for I.V. infusion 150 mg | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody) |
| Myelosuppression Risk | Low as monotherapy; may add to myelosuppression when combined with chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (LVEF) before and during treatment, FBC when combined with chemotherapy, infusion-related reactions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 94 interactions are recorded. Major-level examples include deferiprone, samarium (153Sm) lexidronam, adalimumab and baricitinib. Moderate-level examples include warfarin, paclitaxel, zidovudine, azathioprine, alemtuzumab and chloramphenicol.
- **Cardiac toxicity**: The literature retrieved for the related predictions discusses trastuzumab-related cardiotoxicity. Cardiac monitoring is a standard guardrail.

For other safety information, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The normal breast-like subtype is typically HER2-negative, and the only linked trial tests a different molecule and has not started recruiting. The single paper provides no treatment evidence. The high TxGNN score is not backed by subtype-specific data.

**To proceed, the following is needed:**
- Evidence that normal-like tumours carry HER2 amplification or overexpression, or clinical data in this subtype
- Mechanism of action data (MOA)
- Package insert warnings and contraindications for the Australian product, and the approved indication text for ARTG 10383L

**Context from other predictions:**
- **Rarer tumours** (for example ectomesenchymoma, score 0.9948, and HHV-8-related tumours, score 0.9946, L5, Hold): prediction only, with no trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

