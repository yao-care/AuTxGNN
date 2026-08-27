---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is a selective estrogen receptor degrader (SERD), used in the treatment of hormone receptor-positive (HR+), HER2-negative advanced/metastatic breast cancer. The TxGNN model predicts it may be effective for **HIV infectious disease**, but this direction is currently supported by **0 clinical trials** and only **1 publication**, and that publication does not actually discuss HIV or fulvestrant's mechanism against it — the evidence base for this specific prediction is essentially empty.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in ARTG (drug not marketed in Australia); based on trial/rationale text within this evidence pack, fulvestrant's established use is HR+/HER2- advanced breast cancer |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fulvestrant is flagged as a data gap in this evidence pack (DG002). Based on information embedded elsewhere in the pack (trial descriptions and rationale text for other candidate indications), fulvestrant is known to act as a selective estrogen receptor degrader (SERD) — it binds and degrades the estrogen receptor, and is used clinically for HR+/HER2- advanced or metastatic breast cancer, often in combination with CDK4/6 inhibitors (e.g. abemaciclib, ribociclib, palbociclib).

There is no established mechanistic pathway connecting estrogen receptor degradation to HIV viral replication, entry, or immune control. The single supporting publication (PMID 40343334) does not concern HIV at all — it is a multi-cohort omics analysis of **HTLV-1-associated myelopathy (HAM)**, a distinct retrovirus-driven neuroinflammatory condition. The overlap appears to be a literature indexing artefact (HTLV-1 vs HIV term confusion) rather than genuine biological evidence.

Because no clinical trials, case reports, or mechanistic studies specific to fulvestrant-HIV interaction exist in the current search, this prediction should be treated as a TxGNN statistical signal only, not a clinically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Review/Omics analysis | Research Square | Systems biology analysis of HTLV-1-associated myelopathy (HAM), a neuroinflammatory disorder distinct from HIV; does not address fulvestrant or HIV directly — likely an index-term mismatch (HTLV-1 vs HIV) rather than supporting evidence |

---

## Australia Market Information

Fulvestrant currently has no ARTG entries and is not marketed in Australia (0 licences on record in this evidence pack).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack (DG001: TGA PI data is a blocking gap for safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV infectious disease prediction has no clinical trial support and its sole literature reference is unrelated (concerns HTLV-1, not HIV) — this is consistent with an Evidence Level of L5 (model prediction only). Combined with the absence of TGA Product Information and MOA data, there is no basis to progress this candidate.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — currently blocking (DG001)
- Confirmed mechanism of action data via DrugBank or equivalent (DG002)
- A corrected literature search specifically for fulvestrant and HIV/retroviral mechanisms (the current single hit is a mismatch)
- If further exploration is warranted, note that **rheumatoid arthritis** (rank 6 in this evidence pack) has actual mechanistic literature and reached decision stage S1 ("Research Question") — it may be a more productive candidate to prioritise ahead of this one, though the estrogen-signalling literature on RA is itself directionally inconsistent and would need dedicated review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

