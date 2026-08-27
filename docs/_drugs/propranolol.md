---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Propranolol: From Cardiovascular Disease to Breast Capillary Hemangioma

## One-Sentence Summary

Propranolol is a long-established non-selective beta-adrenergic antagonist historically used for cardiovascular conditions such as hypertension, angina and arrhythmia. Among **10 candidate indications** screened by the TxGNN model for this drug, **Breast Capillary Hemangioma** is the most evidence-supported repurposing direction, supported by **2 clinical trials** (including a 500-patient postmarketing surveillance study of the already-approved propranolol hemangioma formulation, Hemangiol) and **1 publication**. Most of the other TxGNN-ranked candidates (e.g. distal myopathy, congenital myopathy, chondroma, Maffucci syndrome) returned no supporting trials or literature and are flagged in this evidence pack as likely knowledge-graph artefacts rather than real pharmacological signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from this evidence pack (no ARTG-sourced text; `original_moa` and `original_indications` are data gaps). Propranolol is generally recognised as a non-selective beta-blocker for cardiovascular conditions (hypertension, angina, arrhythmia) — general pharmacological background, not sourced from this pack |
| Predicted New Indication | Breast Capillary Hemangioma |
| TxGNN Prediction Score | 98.90% (rank 11,085 of all candidate diseases; 10th of 10 candidates screened for this drug, but the highest-evidence one) |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack (`original_moa`: [Data Gap]). Based on general pharmacological knowledge, propranolol is a non-selective beta-adrenergic receptor antagonist. Its efficacy in **infantile hemangioma** — via suppression of VEGF/bFGF-driven angiogenesis and promotion of hemangioma stem cell apoptosis — is well proven and forms the basis of an already-approved product (Hemangiol). Breast capillary hemangioma is essentially the same histopathological entity (capillary/infantile hemangioma) presenting at a specific anatomical site, so the extrapolation risk from the approved indication is low.

This is reinforced by a large post-marketing surveillance study (NCT04105517, n=500) of Hemangiol specifically in proliferative infantile hemangiomas requiring systemic treatment, plus a supporting meta-analysis on beta-antagonist therapy for infantile hemangiomas. No trial or publication in this pack addresses the breast location specifically, so site-specific efficacy/safety data remains a gap.

For context, this evidence pack screened 10 TxGNN-predicted indications for propranolol overall. Two other candidates showed genuine, literature-recognised pharmacological plausibility — **cardiomyopathy** (long-standing off-label use in hypertrophic cardiomyopathy) and **intramuscular hemangioma** (same anti-angiogenic mechanism as the approved indication, but with a location-specific evidence gap) — both scored L2–L3 and were staged as "Research Question" or "Proceed with Guardrails." **Cirrhotic cardiomyopathy** returned mixed safety signals (blunted cardiovascular response, possible renal impairment) and is not yet a therapeutic opportunity. The remaining candidates (distal myopathy, congenital myopathy, chondroma, Maffucci syndrome) had no clinical trials or literature at all, and their own rationale notes explicitly flag them as probable false positives from knowledge-graph structural similarity rather than real drug–disease relationships.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04105517](https://clinicaltrials.gov/study/NCT04105517) | N/A (post-marketing surveillance) | Completed | 500 | Real-world prescription/surveillance study of Hemangiol (propranolol) in proliferative infantile hemangiomas requiring systemic treatment — directly supports the drug class in this disease entity |
| [NCT02732678](https://clinicaltrials.gov/study/NCT02732678) | Phase 1/2 | Unknown | 24 | Propranolol + metronomic cyclophosphamide dose-finding in locally advanced/metastatic angiosarcoma — a malignant vascular tumour, mechanistically distinct from benign capillary hemangioma; low relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32647928](https://pubmed.ncbi.nlm.nih.gov/32647928/) | 2020 | Meta-analysis/Cohort | Pediatric Surgery International | Efficacy and safety of adrenergic beta-antagonists (including propranolol) combined with laser therapy in infantile hemangiomas |

---

## Australia Market Information

No ARTG entries are recorded for propranolol in this evidence pack (`total_licenses`: 0, `market_status`: Not marketed). No product name, dosage form or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack could not retrieve key warnings, contraindications, or drug-interaction data for propranolol (all fields returned as data gaps; DDI query status: not found). Retrieving the TGA PI is flagged as a **Blocking** data gap (DG001) — safety review cannot proceed to initial screening (S1) without it.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast capillary hemangioma is mechanistically and histopathologically the same entity as infantile hemangioma, for which propranolol (Hemangiol) is an established, approved treatment; a 500-patient surveillance study supports the drug class in this disease. However, propranolol has no current ARTG registration in Australia and no site-specific (breast) trial or safety data exists, so guardrails are needed before clinical use.

**To proceed, the following is needed:**
- TGA-approved Product Information for propranolol (Blocking gap — required for safety screening)
- Formal mechanism-of-action documentation (e.g. DrugBank API record)
- Site-specific (breast) case series or trial data confirming efficacy/safety at this anatomical location
- Clarification of the regulatory pathway, given propranolol currently has zero ARTG entries in Australia
- Drug interaction and contraindication data before any clinical protocol design

*Note: This report focuses on the strongest of 10 TxGNN-predicted indications screened for propranolol in this evidence pack. Cardiomyopathy (general) and intramuscular hemangioma remain reasonable secondary research questions; distal myopathy (Tateyama type), congenital myopathy with excess of thin filaments, chondroma, and Maffucci syndrome had no supporting evidence and are not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

