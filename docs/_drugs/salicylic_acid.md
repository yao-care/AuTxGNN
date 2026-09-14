---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Topical Keratolytic Use to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid (DrugBank DB00936) is a keratolytic agent, commonly used topically for dermatological conditions involving excess keratin (e.g. warts, acne, psoriasis). The TxGNN model predicts a possible new application in **papillary conjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a computational signal only, with no clinical or mechanistic validation to date.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `original_indications` recorded). Salicylic acid is generally classified as a keratolytic/dermatological agent. |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% (rank 2109) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for salicylic acid is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge referenced in the model's own rationale, salicylic acid is a keratolytic agent with weak anti-inflammatory activity via mild COX inhibition. There is no established precedent for its use on the ocular surface at any defined concentration or formulation.

Papillary conjunctivitis is predominantly an allergic or mechanically-induced inflammatory condition of the conjunctiva. The evidence pack's own rationale explicitly describes the mechanistic link to salicylic acid's keratolytic action as **weak and speculative**, noting that the two conditions do not share a clear pathophysiological pathway.

It is also worth noting that of the 10 TxGNN-predicted indications for this drug, most (e.g. brachydactyly-syndactyly syndrome, pseudoachondroplasia, acromesomelic dysplasia) are rare genetic skeletal/developmental disorders with no plausible mechanistic connection to salicylic acid — several are explicitly flagged in the model rationale as likely knowledge-graph noise. This context reinforces caution in interpreting the top-ranked prediction as well.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Salicylic acid currently has no ARTG entries and is not marketed in Australia (`market_status`: not marketed; `total_licenses`: 0). No approved indication text is available for reference.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — TFDA label data retrieval is flagged as a Blocking gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with no supporting clinical trials or literature, and the mechanistic rationale is explicitly assessed as weak/speculative in the source data. Combined with a Blocking data gap on TFDA warnings/contraindications, there is currently no basis to proceed to safety evaluation.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product label data (warnings and contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data for salicylic acid — currently High-severity gap (DG002)
- Preclinical or early clinical evidence specifically evaluating salicylic acid (or a defined ophthalmic formulation) in conjunctival inflammatory disease
- Re-evaluation of the remaining 9 predicted indications, most of which currently show no credible mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

