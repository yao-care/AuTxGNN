---
layout: default
title: Naltrexone
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Naltrexone
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

# Naltrexone: From Opioid/Alcohol Use Disorder to Hypervitaminosis

## One-Sentence Summary

Naltrexone is a mu-opioid receptor antagonist internationally used for opioid and alcohol use disorder; no Australia-specific approved indication is on file since the drug is not currently registered here. The TxGNN model predicts possible activity in **Hypervitaminosis**, but this candidate currently has **no supporting clinical trials** and **no supporting literature**, and a blocking safety data gap remains unresolved.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Australia (drug not registered locally); internationally used for opioid/alcohol use disorder |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap DG002, High severity). Naltrexone is widely known as a mu-opioid receptor antagonist, used internationally to treat opioid dependence and alcohol use disorder — this is general pharmacological knowledge, not confirmed via Australian regulatory sources here, since naltrexone has no ARTG entries.

The predicted new indication, hypervitaminosis (vitamin excess/toxicity), has no obvious pharmacological or clinical relationship to opioid receptor antagonism. The TxGNN score (98.66%, ranked 13,245 out of all drug–disease pairs in the model) reflects a statistical association from the model's knowledge-graph embeddings rather than a validated biological mechanism.

No clinical trials or published literature currently support a naltrexone–hypervitaminosis link. This is a pure model-generated hypothesis (Evidence Level L5) and should be treated as exploratory only until independent mechanistic or clinical evidence emerges.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

Naltrexone is not currently registered on the ARTG (0 entries) — no Australian market information is available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (DG001) means no TFDA/TGA-equivalent product information — warnings or contraindications — is available, so safety cannot be assessed.
- The top predicted indication, hypervitaminosis, has zero clinical trial or literature support (Evidence Level L5, model prediction only).
- Naltrexone is not currently registered in Australia (0 ARTG entries), so there is no local regulatory pathway or safety record to build on.

**To proceed, the following is needed:**
- TGA-equivalent Product Information: warnings, precautions, and contraindications (currently Blocking gap DG001)
- Confirmed mechanism of action data (DG002, High severity)
- A targeted literature/mechanistic search specifically testing naltrexone in hypervitaminosis, as none currently exists
- Consideration of other, more biologically plausible candidates in this batch — e.g., rank 5 "restless legs syndrome" (score 92.2%) returned 5 literature hits, though none directly evidence a naltrexone–RLS relationship and would need dedicated review before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

