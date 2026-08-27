---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
---

# Oxybutynin
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

# Oxybutynin: From Overactive Bladder to Restless Legs Syndrome

## One-Sentence Summary

Oxybutynin is an antimuscarinic (anticholinergic) agent with a long history of use for overactive bladder and neurogenic bladder dysfunction. The TxGNN model predicts it may also be effective for **Restless Legs Syndrome**, but this is currently a pure computational signal — **no clinical trials** and **no published literature** were found supporting this specific drug–disease link. Given the absence of supporting evidence and an unclear mechanistic rationale, this candidate is not ready to advance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Australian licensing data reviewed. Oxybutynin is internationally established as an antimuscarinic for overactive bladder / urge urinary incontinence (see literature evidence in related predictions below) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on general pharmacological knowledge, oxybutynin is a muscarinic receptor antagonist (M2/M3) that relaxes detrusor smooth muscle, and its efficacy in overactive bladder and neurogenic bladder is well established. It is not currently approved or commonly used for any neurological movement disorder.

Restless Legs Syndrome (RLS) is a sensorimotor neurological condition, primarily attributed to central dopaminergic dysfunction and iron-handling abnormalities, with treatment centred on dopamine agonists, alpha-2-delta calcium channel ligands (e.g. gabapentinoids), and iron replacement. This is mechanistically distinct from oxybutynin's peripheral antimuscarinic action on bladder smooth muscle, and no established pharmacological pathway currently links the two.

A plausible (though speculative) explanation for the TxGNN association may be indirect: RLS and overactive bladder/nocturia frequently co-occur in the same patient populations (e.g. older adults, patients with sleep disruption), which could generate a knowledge-graph-level correlation without reflecting a true causal or therapeutic relationship. Because no clinical trial or literature evidence currently exists for this specific pairing, this prediction should be treated as an early-stage, unvalidated hypothesis rather than a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries were found for oxybutynin in the data reviewed for this report; the product is recorded as **not marketed** in Australia based on available data. This should be independently verified against the current TGA ARTG database before any further evaluation, as oxybutynin-containing products are marketed in other jurisdictions.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications, or drug interaction data were available in this evidence pack (drug interaction query returned "not found").

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting oxybutynin for restless legs syndrome, and no clear mechanistic link between its antimuscarinic action and RLS pathophysiology has been established. The evidence level is L5 — a model prediction only, without any corroborating studies.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or another authoritative source (currently a Blocking data gap, DG001/DG002)
- TGA-approved Product Information, including warnings, contraindications, and drug interaction data (currently unavailable — flagged as a Blocking gap)
- Verification of current ARTG registration status, as this pack records oxybutynin as not marketed in Australia
- A targeted literature and clinical trial search specifically for "oxybutynin AND restless legs syndrome" to confirm the absence of evidence is not a data-collection artefact
- Preclinical or mechanistic studies exploring any plausible pharmacological basis before further investment

**Note for reviewers:** other TxGNN-predicted indications for oxybutynin in this evidence pack — particularly *low compliance bladder* (rank 4, 2 clinical trials and 20 supporting publications) — carry a substantially stronger evidence base and may represent a more productive repurposing candidate to prioritise ahead of restless legs syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

