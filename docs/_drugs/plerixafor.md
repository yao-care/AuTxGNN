---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
---

# Plerixafor
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

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist historically used to mobilise peripheral blood stem cells (in combination with G-CSF) in patients with multiple myeloma or lymphoma undergoing autologous transplant. The TxGNN model predicts it may be effective for **indolent plasma cell myeloma** as a direct treatment, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in this evidence pack. Rationale notes describe historical use for peripheral blood stem cell mobilisation (with G-CSF) in multiple myeloma/lymphoma patients undergoing transplant — this drug is not registered as a direct cancer treatment. |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Plerixafor was not returned by the structured DrugBank query in this pack (data gap, remediation pending). However, other parts of this evidence pack consistently describe Plerixafor as a **CXCR4 antagonist**, blocking the CXCR4–CXCL12 (SDF‑1) axis that anchors haematopoietic and malignant plasma cells within the bone marrow niche.

The mechanistic rationale for this specific prediction is that Plerixafor's approved use is stem cell **mobilisation** in multiple myeloma patients (disrupting the same CXCR4–SDF‑1 interaction that plasma cells use to stay protected within marrow niches) — giving it a plausible pharmacological connection to plasma cell disease biology.

That said, this is a mobilisation/supportive-care mechanism, not a demonstrated anti-myeloma treatment mechanism. There is no direct treatment trial, preclinical study, or publication in this pack testing Plerixafor as therapy for indolent plasma cell myeloma. The connection is inferred from disease-class proximity, not from tested evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Safety data (key warnings, contraindications, drug interactions) were not available in this evidence pack, and Plerixafor currently has no approved Australian Product Information (not marketed / 0 ARTG entries). Prescribers and reviewers should consult overseas regulatory PI (e.g. US FDA, EMA) pending any TGA registration or PI acquisition.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 — no clinical trials or literature test Plerixafor specifically for indolent plasma cell myeloma. The mechanistic link relies on the drug's mobilisation role in myeloma care rather than a tested anti-myeloma effect, which is insufficient to progress past initial screening.

**To proceed, the following is needed:**
- Confirmed MOA and original indication data from DrugBank (DG002)
- TGA/overseas Product Information — warnings, contraindications, interactions (DG001, Blocking)
- Preclinical or mechanistic studies testing Plerixafor's direct anti-plasma-cell-myeloma activity (not just mobilisation)
- At minimum a case series or observational signal before this candidate can move beyond S0

**Note for reviewers:** within the same evidence pack, a different predicted indication for Plerixafor — **myeloid leukemia** (rank 7, score 99.02%) — has materially stronger support (L2, 30 clinical trials including completed Phase 1/2 studies, 20 publications on CXCR4-mediated chemosensitisation in AML). If the goal is to identify the most actionable repurposing candidate for Plerixafor rather than strictly the top-ranked disease, that entry warrants separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

