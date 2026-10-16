---
layout: default
title: Trastuzumab
parent: Moderate Evidence (L3-L4)
nav_order: 748
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Trastuzumab: predicted new indication Normal breast-like subtype of breast carcinoma (evidence level L4). Approved use: HER2-positive breast carcinoma"
monitor_inn: "Trastuzumab"
predicted_indications: ["normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Trastuzumab: From HER2-Positive Breast Carcinoma to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab is a HER2-targeted monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for the **normal breast-like subtype of breast carcinoma**, but the supporting evidence is very thin: **1 clinical trial** (not yet recruiting, and testing a different molecule) and **1 publication** (a morphology study with no treatment data).
The model's other predictions for related breast cancer subtypes (progesterone-receptor positive and negative disease) have far stronger support and are summarised below for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, trastuzumab binds the extracellular domain of HER2, inhibiting HER2 signalling and mediating antibody-dependent cellular cytotoxicity (ADCC). Its efficacy in HER2-positive breast cancer is well established.

The normal breast-like subtype is an intrinsic breast cancer subtype that is typically HER2-negative, with variable hormone receptor status. The direct mechanistic link to trastuzumab is therefore weak. The high TxGNN score appears to reflect a graph-based association with breast carcinoma in general rather than subtype-specific support. The prediction should be treated as a hypothesis only.

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
- **Progesterone-receptor positive breast cancer** (score 99.90%, L1, Proceed with Guardrails): supported by the completed Phase 3 adjuvant trial NCT01275677 (n=3270). This is largely a subpopulation of the already approved HER2-positive indication. Guardrails: confirm HER2 status and monitor LVEF.
- **Progesterone-receptor negative breast cancer** (score 99.90%, L1, Proceed with Guardrails): supported by NCT01275677 and the Phase 3 study NCT05985187 (status unknown). Use is limited to HER2-positive disease, and it should not be extrapolated to triple-negative or HER2-zero disease.
- **Luminal A or B breast tumour** (score 99.90%, L2, Proceed with Guardrails): literature support only, including the NeoSphere trial and the adjuvant trastuzumab trial. Use is limited to HER2-positive luminal B disease.
- **Rarer tumours** (for example ectomesenchymoma and HHV-8-related tumours, scores of about 99%, L5, Hold): prediction only, with no trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

