---
layout: default
title: Timolol
parent: 僅模型預測 (L5)
nav_order: 676
evidence_level: L5
indication_count: 10
---

# Timolol
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

Using this task's own detailed formatting spec directly (no additional skill applies — this is a self-contained report-generation instruction, not a coding/debugging/brainstorming task).

# Timolol: From Established Glaucoma Therapy to Primary Hereditary Glaucoma

## One-Sentence Summary

Timolol is a non-selective beta-blocker best known for lowering intraocular pressure, though this evidence pack does not contain a documented original approved indication (the drug currently holds **no ARTG registration in Australia**). The TxGNN model predicts a **98.64%** likelihood of relevance to **Primary Hereditary Glaucoma**, but the only clinical trial identified for this specific prediction is unrelated to the indication, and **no supporting literature** was found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Timolol has no current ARTG registration in Australia) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Timolol is not available in this evidence pack (flagged as data gap DG002, High severity). However, mechanistic rationale accompanying the predicted indications describes Timolol as a **non-selective beta-adrenergic receptor blocker** that inhibits β2 receptors in the ciliary body epithelium, reducing aqueous humour production and lowering intraocular pressure (IOP) — the pharmacological basis for its well-established role across multiple glaucoma subtypes.

Primary hereditary glaucoma is a genetically driven subtype in which elevated IOP remains a central pathological feature. On that basis, an IOP-lowering agent such as Timolol is mechanistically plausible for this population, consistent with its known use in other glaucoma subtypes represented elsewhere in this evidence pack.

However, the only clinical trial evidence supplied for this specific ranked indication (NCT02484716) does not actually test Timolol in glaucoma at all — it evaluates a nasal spray formulation for epistaxis in Hereditary Haemorrhagic Telangiectasia (HHT), an unrelated condition. This was graded "C" relevance in the source evidence and appears to reflect a data-linkage error rather than genuine supporting evidence. No literature was identified to support Timolol specifically in primary hereditary glaucoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02484716](https://clinicaltrials.gov/study/NCT02484716) | Phase 2 | Completed | 58 | Randomised trial of a topical nasal Timolol spray for epistaxis in Hereditary Haemorrhagic Telangiectasia (HHT) — **not** a study of primary hereditary glaucoma; flagged as low relevance (Grade C) and likely a data-matching artefact |

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Timolol currently holds **no ARTG registration** in Australia (0 licenses on file). No approved product information or indication text is available from the Australian regulatory record for this evidence pack.

---

## Safety Considerations

Timolol is not currently registered on the ARTG, so no TGA-approved Product Information is available for this evidence pack. Key warnings, contraindications, and drug–drug interaction data are all flagged as data gaps (DG001, Blocking severity) and could not be sourced. Safety evaluation should draw on Product Information from a jurisdiction where Timolol is currently registered before any further clinical assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no valid clinical trial or literature evidence directly supporting Timolol's use in primary hereditary glaucoma — the single trial identified addresses an unrelated condition (HHT-related epistaxis). Combined with blocking-level gaps in safety data (DG001) and MOA verification (DG002), this candidate does not meet the bar to proceed past initial screening.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) for Timolol (DG001 — Blocking)
- Verified mechanism-of-action data from DrugBank (DG002 — High)
- Correctly matched clinical trials or literature specifically studying Timolol in primary hereditary glaucoma populations
- Confirmation of Timolol's regulatory status, since it currently has zero ARTG entries in Australia

**Note:** This evidence pack contains substantially stronger candidates for the same drug — notably **closed-angle glaucoma**, **open-angle glaucoma**, and **angle-closure glaucoma** (all rated L1, "Proceed with Guardrails," with multiple Phase 3 RCTs and 15–20+ supporting publications each). These may represent a more actionable repurposing pathway than the top-ranked prediction evaluated in this report and warrant a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

