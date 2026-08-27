---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Larotrectinib
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

# Larotrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is a highly selective pan-TRK (TRKA/B/C) inhibitor originally granted a tissue-agnostic approval for solid tumours harbouring an NTRK gene fusion. The TxGNN model predicts a possible signal for **Multiple Endocrine Neoplasia (MEN)**, but this is currently supported by only **1 indirectly relevant clinical trial** and **2 contextual publications**, none of which studied larotrectinib in MEN directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTRK gene fusion-positive solid tumours (tissue-agnostic indication) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Australia Market Status | Not currently marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, larotrectinib is a selective inhibitor of the TRK receptor family (TRKA/B/C), and its efficacy in NTRK fusion-positive solid tumours is well established and forms the basis of its tissue-agnostic approval.

Multiple Endocrine Neoplasia — particularly MEN2 — is driven predominantly by **RET** proto-oncogene mutations, not NTRK fusions. RET and TRK are related receptor tyrosine kinases that sit in adjacent signalling space within the knowledge graph, which likely explains why TxGNN assigned a high similarity score. However, this is a mechanistic proximity rather than a direct pharmacological link: larotrectinib does not target RET.

The one relevant trial identified (MATCH) is a large genomically-driven basket study in which larotrectinib is used only in the NTRK-fusion-positive subgroup, and the study was not designed around MEN. Taken together, the prediction is biologically plausible as a hypothesis-generating signal but is not yet supported by direct mechanistic or clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | Large genomically-driven basket trial (MATCH) across advanced/refractory solid tumours, lymphomas and myeloma; larotrectinib is used only in the NTRK-fusion-positive subgroup and was not designed for MEN specifically (Grade C relevance – indirect). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Reviews kinase inhibitors (including mutation-specific TRK-targeted agents) in advanced thyroid cancer; contextual background only, not MEN-specific. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Cohort/Mechanistic | NPJ Precision Oncology | Describes RET-driven resistance mechanisms to RET inhibitors in medullary thyroid carcinoma; provides mechanistic context distinguishing RET from TRK signalling but does not study larotrectinib in MEN. |

---

## Australia Market Information

No ARTG entries are currently registered for larotrectinib in Australia — the drug is not marketed locally.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between larotrectinib (a TRK inhibitor) and MEN (a RET-driven disease) is weak, and the only identified trial evidence is indirect (a basket trial not designed for this indication). No literature directly studies larotrectinib in MEN. Evidence level L4 does not support progression at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action and DrugBank category data (currently a data gap, DG002)
- TGA/local Product Information warnings and contraindications (currently a data gap, DG001 — blocking for safety assessment)
- Direct pre-clinical or clinical evidence evaluating larotrectinib activity in MEN or RET-associated disease
- Clarification of whether the TxGNN signal reflects genuine cross-pathway relevance (RET–TRK proximity) or knowledge-graph noise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

