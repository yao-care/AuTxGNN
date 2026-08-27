---
layout: default
title: Nifedipine
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Nifedipine
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

# Nifedipine: From Hypertension/Angina to Migraine with Brainstem Aura

## One-Sentence Summary

> Nifedipine is a dihydropyridine calcium channel blocker (CCB), a drug class established for treating hypertension and angina pectoris.
> The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
> but this signal is currently supported by **0 clinical trials** and only **2 publications** — one of which is a controlled study reporting nifedipine was *not* effective as abortive therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / Angina pectoris (general dihydropyridine CCB indication — no drug-specific record in this evidence pack) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 92.63% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nifedipine is not available in this evidence pack. Based on general pharmacological knowledge, nifedipine is a dihydropyridine calcium channel blocker; its efficacy in hypertension and angina is well established, and mechanistically calcium channel blockade could theoretically reduce vasospasm and cortical spreading depression (CSD)-related vascular events implicated in migraine pathophysiology.

However, the evidence pack's own rationale for this specific candidate flags an important limitation: the mechanistic link is drawn from *general* migraine pathophysiology, not from any mechanism study specific to the brainstem aura (basilar-type) subtype — the supporting evidence is extrapolated from broader migraine research rather than targeted studies.

Notably, a related but broader candidate in this pack — "migraine disorder" (rank 2, score 91.80%, evidence level L2) — has a much larger evidence base (2 clinical trials, 20+ publications, several RCTs). Even within that larger body of evidence, nifedipine's efficacy for migraine prophylaxis is inconsistent across studies and generally considered inferior to first-line agents such as flunarizine or beta-blockers. This broader context reinforces caution in interpreting the top-ranked, narrower "brainstem aura" prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1423566](https://pubmed.ncbi.nlm.nih.gov/1423566/) | 1992 | RCT | Cephalalgia | Double-blind study of nifedipine as abortive treatment for acute migraine-with-aura attacks; nifedipine **increased** headache intensity compared with vehicle — concluded **not useful** as abortive therapy |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathologie-biologie | Review of calcium antagonists (verapamil, diltiazem, nifedipine) for migraine prophylaxis; effectiveness of nifedipine **cannot be considered firmly demonstrated** given trial design limitations |

---

## Australia Market Information

Nifedipine currently has no ARTG entries recorded in this evidence pack (market status: Not Marketed, 0 licenses). No product-specific Australian market information is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (migraine with brainstem aura) is supported only by mechanism-level extrapolation (L4) and no dedicated clinical trials; the only directly relevant RCT identified reported nifedipine was **not effective** and worsened headache intensity.
- A blocking data gap exists for TFDA/TGA product warnings and contraindications (DG001), which prevents even an initial (S1) safety assessment.
- The drug is not currently marketed or registered in Australia (0 ARTG entries), adding regulatory uncertainty on top of the weak efficacy signal.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — required to clear the blocking safety gap before any further evaluation
- Drug-specific mechanism of action (MOA) data from DrugBank or equivalent source
- If pursuing the migraine indication further, consider redirecting research focus to the broader "migraine disorder" candidate (rank 2), which has a larger evidence base, while still weighing its documented inconsistent efficacy versus first-line prophylactic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

