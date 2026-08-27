---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a well-established osmotic diuretic, though no original indication or Australian registration record is present in this dataset. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but currently only **1 tangentially related publication** and **no clinical trials** support this direction — the evidence is preliminary at best.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No formal indication data on file (osmotic diuretic use — e.g. cerebral oedema, raised intracranial/intraocular pressure, oliguric states — is general pharmacological knowledge, not sourced from this evidence pack) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, mannitol is an osmotic agent that promotes water and electrolyte excretion via the renal tubule; its clinical use for reducing intracranial/intraocular pressure and inducing diuresis is well established.

NSIAD is a rare, genetically-driven condition caused by a gain-of-function mutation in the vasopressin V2 receptor, leading to inappropriate free-water retention independent of ADH levels. Standard management relies on fluid restriction, urea, or vaptan-class V2 receptor antagonists. The theoretical link to mannitol is that its osmotic diuretic action could promote free-water excretion, which would be mechanistically relevant to a condition defined by water retention.

However, this link is currently speculative rather than evidence-based. The single supporting publication is a general review on pitfalls in evaluating hyponatraemia, which likely references mannitol only in the context of differential diagnosis of osmotic states — not as an evaluated treatment for NSIAD. No clinical trial has tested mannitol in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Reviews ten common pitfalls in evaluating hyponatraemic patients; does not evaluate mannitol as a treatment for NSIAD — relevance is limited to shared osmotic/electrolyte concepts in differential diagnosis |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is one review article that does not directly evaluate mannitol for NSIAD, with no clinical trials and no mechanism-of-action data confirmed. This is a knowledge-graph-derived hypothesis rather than an evidence-backed repurposing candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank query currently unresolved — flagged as a High-severity data gap, DG002)
- TFDA/TGA-approved Product Information for warnings and contraindications (flagged as a Blocking data gap, DG001 — required before any S1 safety evaluation can proceed)
- Verification of current Australian ARTG registration status (dataset shows "not marketed," which should be confirmed against TGA records given mannitol's known global availability)
- Dedicated pharmacological or case-level evidence directly linking mannitol to NSIAD, beyond the current tangential review reference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

