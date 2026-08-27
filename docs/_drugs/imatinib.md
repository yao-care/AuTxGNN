---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: From Chronic Myeloid Leukaemia to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally developed for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST). The TxGNN model predicts it may be effective for **heart fibrosarcoma**, but this direction is currently supported by **0 clinical trials** and only **1 non-specific literature review**, making it an early-stage research signal rather than an actionable clinical lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia (CML) / gastrointestinal stromal tumour (GIST) — well-established indications for imatinib; no TGA/ARTG-sourced indication text was available in this evidence pack |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (data gap DG002, High severity). Based on known information, imatinib is a small-molecule tyrosine kinase inhibitor targeting BCR-ABL, KIT and PDGFR, and its efficacy in CML and GIST is well established; mechanistically, PDGFR-driven signalling is also implicated in a range of fibroblastic/sarcomatous tumours.

The mechanistic link proposed here is an extrapolation from imatinib's proven activity in dermatofibrosarcoma protuberans (DFSP), a PDGFR-driven fibroblastic tumour, to the broader "fibrosarcoma" disease family in the knowledge graph — of which heart fibrosarcoma is one node. However, heart fibrosarcoma is an extremely rare tumour, and no cardiac-specific data exists: there are no registered clinical trials, and the single supporting publication is a 2008 general review of imatinib's expanding indications, not a study of cardiac or fibrosarcoma-specific activity.

Because the supporting evidence is mechanistic and generic rather than site-specific, this prediction should be treated as a research hypothesis. Notably, other TxGNN-predicted fibrosarcoma-family indications for imatinib in the same evidence pack (e.g. conventional fibrosarcoma/DFSP, which has a completed Phase 2 trial, and kidney fibrosarcoma, supported by a Phase 2 basket trial) carry stronger evidence and may be more productive avenues to pursue.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | General review of imatinib's expanding indications since its original approval for CML/GIST; notes new indications lack robust evidence and does not address heart fibrosarcoma specifically |

## Australia Market Information

Imatinib currently has **0 ARTG entries** and is recorded as **not marketed** in this evidence pack. No product listing, dosage form, or approved-indication data was available to tabulate.

## Cytotoxicity

Imatinib is an antineoplastic agent (tyrosine kinase inhibitor) used across multiple cancer indications, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL/KIT/PDGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — no drug-specific toxicity data was available in this evidence pack |
| Emetogenicity Classification | Low to moderate (typical for oral tyrosine kinase inhibitors as a class) |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests, renal function |
| Handling Protection | Oral antineoplastic agent — follow institutional cytotoxic/hazardous drug handling policy for oral chemotherapy agents |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that TGA-specific warnings and contraindications for imatinib were not retrievable in this evidence pack (data gap DG001, Blocking severity) — this is a prerequisite before any safety assessment (S1 stage) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (heart fibrosarcoma) has no clinical trial evidence and only one non-specific literature reference; combined with imatinib currently being unmarketed in Australia (0 ARTG entries), there is insufficient evidence to justify progressing beyond a research question at this time.

**To proceed, the following is needed:**
- TFDA/TGA Product Information — warnings, contraindications, and DDI data (blocking gap, DG001)
- Detailed mechanism of action (MOA) data confirming target expression relevance to heart fibrosarcoma (DG002)
- Cardiac/site-specific preclinical or case-level evidence for imatinib activity in fibrosarcoma
- Consider evaluating the better-evidenced fibrosarcoma-family predictions in this same evidence pack (conventional fibrosarcoma/DFSP — completed Phase 2 trial; kidney fibrosarcoma — Phase 2 basket trial) as higher-priority candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

