---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 698
evidence_level: L5
indication_count: 10
---

# Trastuzumab Emtansine
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate used internationally for HER2-positive breast cancer, though it is not currently marketed in Australia.
The TxGNN model's top-ranked prediction is **Normal Breast-Like Subtype of Breast Carcinoma**,
but this is currently supported by only **1 ongoing Phase 2 trial** and **no published literature**, with the mechanistic rationale still unconfirmed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (internationally established use; not a TGA-approved indication — drug not marketed in Australia) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this evidence pack (Data Gap DG002). Based on the supporting literature that is available (PMID 32583565, PMID 21510863), trastuzumab emtansine is an antibody-drug conjugate (ADC) combining the anti-HER2 monoclonal antibody trastuzumab with DM1 (emtansine/mertansine), a cytotoxic microtubule inhibitor. Trastuzumab delivers the cytotoxic payload specifically to HER2-overexpressing cells, and its efficacy in HER2-positive breast cancer is well established internationally.

The top-ranked predicted indication, "normal breast-like subtype," is a molecular subtype of breast carcinoma that is typically HER2-negative or low-expressing, rather than HER2-driven. The single supporting trial (NCT06348134) does not stratify by this subtype specifically — it evaluates anti-HER2 therapy broadly in HER2-positive Nigerian breast cancer patients — so the mechanistic link is conditional on individual tumour HER2 status rather than generally applicable to the subtype as a whole. The evidence pack's own rationale flags this as non-universal.

It is worth noting for context that other candidates in this same evidence pack — particularly progesterone-receptor positive and progesterone-receptor negative breast cancer (ranks 2–3) — are supported by a substantially larger body of completed Phase 2/3 RCTs and literature, largely because they sit within the already-established HER2-positive breast cancer population where T-DM1 has a genuine, well-documented mechanistic basis. The rank-1 candidate reported here has comparatively weaker direct evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Assessing optimal neoadjuvant-to-adjuvant anti-HER2-based therapy in Nigerian women with HER2+ breast cancer, evaluating efficacy and safety before/after surgery; no results yet, and not specifically stratified by normal breast-like subtype (relevance grade B — indirect) |

## Literature Evidence

Currently no related literature available for this specific predicted indication.

## Australia Market Information

Trastuzumab emtansine is not currently registered on the ARTG (Australian Register of Therapeutic Goods). The evidence pack records 0 licenses and a market status of "not marketed" in Australia.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate; anti-HER2 antibody linked to the cytotoxic microtubule inhibitor DM1) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Trastuzumab emtansine is not currently marketed in Australia, and no TGA-approved Product Information exists domestically. Warnings, contraindications, and drug interaction data in this evidence pack are incomplete and flagged as a **Blocking** data gap (DG001), meaning a formal safety (S1) evaluation cannot yet proceed. Overseas prescribing information (e.g. an equivalent regulator's approved PI) should be sourced and reviewed before any further assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is supported by only one ongoing, indirectly relevant Phase 2 trial (evidence level L3, relevance grade B) with no completed results and no literature, and the mechanistic link depends on individual tumour HER2 status rather than being generally applicable to the subtype. A Blocking safety data gap also prevents progression past decision stage S1.

**To proceed, the following is needed:**
- TGA-approved (or overseas equivalent) Product Information covering warnings and contraindications (resolves DG001)
- Confirmed DrugBank mechanism of action data (resolves DG002)
- HER2 status stratification data from trials enrolling the "normal breast-like" subtype specifically, to confirm or refute the mechanistic link
- Completion results from NCT06348134 (estimated completion 2036)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

