---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol: From Hypertension/Angina to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a selective beta-1 adrenergic blocker generally used to manage hypertension, angina and related cardiovascular conditions. The TxGNN model's top-ranked prediction is that it may be effective for **Malignant Renovascular Hypertension**, but this direction is currently supported by **0 clinical trials** and only **2 tangentially related publications** (neither of which studies metoprolol directly in this condition).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (data gap — original indication text and TFDA label not yet retrieved) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, metoprolol is a cardioselective beta-1 adrenergic receptor antagonist. Beta-1 blockade reduces renin release, heart rate, and cardiac output — mechanisms that are theoretically applicable to controlling severe/malignant forms of hypertension, including malignant renovascular hypertension, which is driven substantially by renin-angiotensin system activation.

However, the theoretical mechanistic link is not currently backed by direct evidence. Malignant renovascular hypertension is a renin-driven, often surgically- or ACE-inhibitor/ARB-managed condition, and beta-blockers are typically adjunctive rather than first-line in this specific presentation. The TxGNN score is high, but this reflects a knowledge-graph relationship prediction rather than confirmed clinical benefit.

The two retrieved publications are only topically adjacent — one is a case report on hypertensive optic neuropathy from Takayasu's arteritis-related renal artery stenosis, and the other evaluates a diagnostic biomarker (chromogranin A) for pheochromocytoma. Neither studies metoprolol's efficacy or safety in this indication, so the mechanistic rationale should be regarded as plausible but essentially unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15231398](https://pubmed.ncbi.nlm.nih.gov/15231398/) | 2004 | Case report | Survey of Ophthalmology | Case of hypertensive optic neuropathy from renal artery stenosis (Takayasu's arteritis); does not evaluate metoprolol treatment |
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Diagnostic study | Medicine | Evaluates chromogranin A vs. plasma catecholamines for diagnosing pheochromocytoma in hypertension work-up; not a metoprolol efficacy study |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials and no literature directly evaluating metoprolol in malignant renovascular hypertension — the two retrieved papers are only topically related. Combined with the outstanding blocking data gap on TFDA warnings/contraindications, there is insufficient evidence to progress this candidate.

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action data from DrugBank
- Original indication/regulatory history for metoprolol in this market
- Dedicated clinical or preclinical studies of metoprolol specifically in malignant renovascular hypertension

**Note:** A lower-ranked candidate in this evidence pack, **chronic pulmonary heart disease** (rank 9, score 99.05%), has substantially stronger support — 15 clinical trials (including several Phase 4 RCTs with n>1,700) and 20 publications — with a scoring of L2/Proceed with Guardrails. This may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

