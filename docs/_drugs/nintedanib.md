---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Original Indication (Data Pending) to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib is a triple angiokinase inhibitor (VEGFR1-3/PDGFRα,β/FGFR1-3); its originally licensed indication is not documented in this evidence pack (data gap DG002 — MOA/indication pending confirmation from DrugBank). The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, but this is currently supported by mechanistic rationale only, with **0 clinical trials** and **1 general review article** (not nintedanib-specific) identified to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — original indication and MOA are flagged as pending collection (data gaps DG001/DG002) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Australia Market Status | Not currently marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-indication and confirmed mechanism-of-action data for nintedanib are not available in this evidence pack (data gap DG002, High severity). Based on the mechanistic information captured in the TxGNN repurposing rationale, nintedanib is a triple angiokinase inhibitor that blocks VEGFR1-3, PDGFRα/β, and FGFR1-3.

Dermatofibrosarcoma protuberans is driven in the great majority of cases by the *COL1A1-PDGFB* fusion gene, which causes constitutive activation of PDGFRβ. Imatinib, a PDGFR-targeting agent, is already approved for DFSP on this same mechanistic basis. Because nintedanib also inhibits PDGFR (alongside VEGFR and FGFR), there is a plausible mechanistic rationale for activity in DFSP.

However, this rationale currently rests on drug-class reasoning rather than nintedanib-specific data: the only supporting literature is a general review of PDGFR inhibitors in neoplastic disease, which does not report on nintedanib in DFSP directly. No clinical trials of nintedanib in DFSP have been identified. This places the candidate at an early, hypothesis-generating stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | General review of small-molecule PDGFR inhibitors in neoplastic disease; discusses the role of PDGFR-targeted agents in tumours driven by PDGF signalling, but does not report nintedanib-specific data in DFSP. |

---

## Australia Market Information

Nintedanib has no ARTG entries and is not currently marketed in Australia based on the data available in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack — this is tracked as a **Blocking** data gap (DG001), meaning a formal safety assessment cannot proceed until TGA/TFDA-equivalent PI data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for nintedanib in DFSP is biologically plausible (shared PDGFR-driven pathway with imatinib, an approved DFSP therapy), but it is currently supported only by a non-drug-specific review article and no clinical trials — evidence level L4, decision stage S1 ("Research Question"). Safety data required for any S1 progression is also completely absent (Blocking gap DG001), and nintedanib is not currently marketed in Australia.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information — warnings, contraindications, DDI (Blocking gap DG001)
- Confirmed mechanism of action and original indication from DrugBank (High-severity gap DG002)
- Preclinical or case-level evidence specific to nintedanib (not just PDGFR-inhibitor class) in DFSP or PDGFB-fusion-driven tumours
- If pursued, confirmation of Australian regulatory pathway status given nintedanib is not currently registered

*Note: The prediction pipeline also generated 9 additional lower-confidence candidates for this drug (liposarcoma, fibrosarcoma subtypes, ALS-related conditions, and a skeletal dysplasia), all scored L5/Hold due to absence of clinical or literature evidence and, in several cases, suspected knowledge-graph noise (e.g. shared *NEK1* gene nodes). These are not detailed above as none met the threshold for a research-question-level candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

