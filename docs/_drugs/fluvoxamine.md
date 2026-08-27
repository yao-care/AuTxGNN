---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamine: From Obsessive-Compulsive Disorder to Paranoid Personality Disorder

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) historically used to treat obsessive-compulsive disorder and depression. The TxGNN model's top-ranked prediction for this candidate is **Paranoid Personality Disorder**, but this direction is currently supported by **0 clinical trials** and only **2 tangentially related publications**, neither of which studied fluvoxamine's efficacy in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obsessive-Compulsive Disorder / Depression (general pharmacological knowledge — not present in the supplied evidence pack; no ARTG license record available) |
| Predicted New Indication | Paranoid Personality Disorder |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on general pharmacological knowledge, fluvoxamine is an SSRI that inhibits serotonin reuptake and also acts as a sigma-1 receptor agonist; its established efficacy is in obsessive-compulsive disorder and depressive/anxiety disorders.

There is no mechanistic hypothesis in the evidence pack connecting fluvoxamine's serotonergic activity to paranoid personality disorder specifically. The two supporting publications are not treatment studies of this condition: one is a cross-sectional study of personality traits in body dysmorphic disorder patients (only tangentially involving fluvoxamine-treated subjects), and the other is a review of psychiatric side effects caused by interferon-alpha therapy, unrelated to fluvoxamine.

Given the absence of both a mechanistic rationale and any direct clinical evidence, this prediction should be treated as a candidate requiring substantial further validation rather than an actionable repurposing signal — it may reflect a false-positive association in the underlying knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cross-sectional | Comprehensive Psychiatry | Assessed personality traits/disorders in 148 body dysmorphic disorder patients (26 in a fluvoxamine treatment study); does not evaluate fluvoxamine for paranoid PD. |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encéphale | Reviews psychiatric complications (including personality disorders) induced by interferon-alpha therapy; unrelated to fluvoxamine treatment. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that fluvoxamine currently has no ARTG entries and is not marketed in Australia, so no locally approved PI exists to reference at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic hypothesis and no clinical or trial evidence supporting fluvoxamine's use in paranoid personality disorder — only 2 indirectly related publications exist. This is a pure model-prediction-only (L5) candidate and should not proceed further without new supporting data.

**To proceed, the following is needed:**
- A pharmacological rationale linking SSRI/sigma-1 receptor activity to paranoid personality disorder symptomatology
- Preclinical or observational evidence specific to this indication
- Mechanism of action (MOA) data for fluvoxamine (currently a data gap)
- TFDA/TGA warnings, contraindications and drug interaction data (currently a data gap)
- Confirmation of current Australian registration status, given 0 ARTG entries recorded

**Note:** this evidence pack contains other TxGNN-predicted indications for fluvoxamine with substantially stronger evidence — notably **anxiety disorder** (L1, Proceed with Guardrails) and **agoraphobia** (L2, Proceed with Guardrails) — which warrant separate, prioritised evaluation ahead of this candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

