---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
---

# Verapamil
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

# Verapamil: From Cardiovascular Disease to Obsolete Bundle Branch Block

## One-Sentence Summary

> Verapamil is a non-dihydropyridine calcium channel blocker used in cardiovascular disease; the specific TGA-approved original indication is not captured in this evidence pack (flagged as a data gap).
> The TxGNN model predicts a possible association with **obsolete bundle branch block**, a disease term itself marked as obsolete in current nomenclature,
> with **0 clinical trials** and **0 publications** currently supporting this direction — this is a **model-prediction-only** signal that mechanistically appears to *contradict* rather than support therapeutic use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (see Data Gaps DG001/DG002) — verapamil is known from the pack's own rationale text as a non-dihydropyridine calcium channel blocker with negative dromotropic (AV-node–slowing) and antihypertensive effects |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for verapamil in this evidence pack (DG002 – High severity data gap). Based on the information that is present, verapamil is a non-dihydropyridine calcium channel blocker with a well-recognised negative dromotropic effect — it slows conduction through the atrioventricular (AV) node.

For the top-ranked predicted indication, "obsolete bundle branch block," the evidence pack's own mechanistic rationale flags a direct conflict: verapamil's AV-nodal conduction-slowing action would be expected to *worsen*, not improve, a conduction block. In addition, the disease term itself has been marked as an obsolete/deprecated classification, meaning it no longer represents a clinically actionable diagnostic target. Taken together, the high TxGNN similarity score (99.62%) reflects a strong knowledge-graph pattern match rather than a biologically plausible or clinically supported therapeutic direction — there is no clinical trial or literature evidence to corroborate it, and the mechanistic direction runs counter to the predicted use.

This is therefore best understood as a **model-prediction-only (L5)** hypothesis that does not currently warrant further clinical development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Australia Market Information

Verapamil is currently **not marketed** in Australia under this evidence pack, with **0 ARTG entries** recorded (`total_licenses: 0`). No product listings, dosage forms, or approved-indication text are therefore available for review.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Key warnings, contraindications, and drug interaction data are flagged as data gaps in this evidence pack — including a Blocking-severity gap, DG001, for TFDA/TGA-equivalent product label warnings and contraindications, which must be resolved before any safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is supported only by the TxGNN model score (L5, no clinical trials or literature), targets a disease term already classified as obsolete, and its own mechanistic rationale identifies a direct pharmacological conflict (AV-nodal conduction slowing vs. a conduction-block target). There is no basis to progress this candidate beyond model prediction.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TGA-equivalent Product Information for warnings/contraindications before any safety screening (S1) can occur
- Resolve DG002 (High): obtain verapamil's confirmed mechanism of action and TGA-approved original indication text
- Clinical/nosological review to confirm whether "obsolete bundle branch block" maps to any current, actionable ICD/SNOMED term
- Consider redirecting review effort toward higher-evidence candidates already at S1 in this same pack — notably **malignant renovascular hypertension** (rank 3, L4) and **arrhythmogenic right ventricular cardiomyopathy** (rank 9, L4), both flagged "Research Question" with supporting literature, unlike this rank-1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

