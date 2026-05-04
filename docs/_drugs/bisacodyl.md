---
layout: default
title: Bisacodyl
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Bisacodyl
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

# Bisacodyl: From Constipation/Bowel Preparation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Bisacodyl is a well-established stimulant laxative used for the management of constipation and pre-procedural bowel preparation. The TxGNN model predicts it may be effective for **Exercise-Induced Malignant Hyperthermia**, with **no clinical trials** and **no publications** currently supporting this direction — this represents a model-only prediction with no supporting empirical evidence. Bisacodyl is not currently registered in Australia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Constipation and pre-procedural bowel preparation (not currently registered in Australia) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 97.69% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Based on well-established pharmacological knowledge, Bisacodyl is a stimulant laxative that acts primarily on the large intestine — it stimulates enteric nerve endings in the colonic mucosa to increase peristaltic contractions and inhibits water and electrolyte reabsorption, resulting in accelerated colonic transit and defaecation. Its clinical utility is confined to the lower gastrointestinal tract.

Exercise-induced malignant hyperthermia (EIMH) is a rare skeletal muscle disorder caused by mutations in the *RYR1* or *CACNA1S* genes, which encode the ryanodine receptor and the voltage-gated calcium channel respectively. In susceptible individuals, physical exertion triggers uncontrolled release of calcium from the sarcoplasmic reticulum, leading to sustained skeletal muscle hypermetabolism, hyperthermia, and potentially life-threatening metabolic crisis. Current management centres on dantrolene — an agent that specifically antagonises RYR1 — along with supportive care.

There is no credible pharmacological link between Bisacodyl and EIMH. Bisacodyl's enteric neurostimulatory and electrolyte-transport-inhibiting actions in the colon share no known intersection with the RYR1/CACNA1S calcium channel dysregulation that underlies malignant hyperthermia. The high TxGNN prediction score most likely reflects proximity between disease nodes in the knowledge graph — specifically, shared clustering among ion channel disorders and metabolic disease groups — rather than any direct drug-target relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Bisacodyl is **not currently marketed in Australia** and has no ARTG entries on record. Any proposed clinical use in Australia would require assessment of an appropriate regulatory pathway (e.g., TGA Special Access Scheme or clinical trial authorisation) before proceeding.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for exercise-induced malignant hyperthermia is entirely unsupported by clinical trials or published literature, and there is no established pharmacological mechanism connecting Bisacodyl's gastrointestinal mode of action to the skeletal muscle calcium dysregulation underlying EIMH. Furthermore, Bisacodyl is not currently registered in Australia, adding a significant regulatory barrier to any clinical translation.

**To proceed, the following is needed:**
- Retrieval and review of Bisacodyl's complete mechanism of action data from DrugBank to confirm or refute any off-target activity relevant to calcium channel biology
- Independent pharmacological expert review to determine whether any plausible mechanistic hypothesis can be formulated
- Preclinical studies (in vitro or animal models of RYR1/CACNA1S dysfunction) to establish a biological basis before any clinical investigation is considered
- Assessment of the TGA regulatory pathway for Australian market entry or trial authorisation, should evidence emerge to warrant further investigation
- For the highest-quality repurposing candidate from this evidence pack, consider pivoting focus to **Dyspepsia** (rank 2, L4 evidence), which has at least a weak mechanistic hypothesis via lower gastrointestinal prokinetic effects and limited supporting data

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application in practice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

