---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a nonsteroidal antiandrogen historically used for metastatic prostate cancer as part of combined androgen blockade. The TxGNN model's top-ranked prediction for this drug is **"prostate cancer/brain cancer susceptibility"**, a composite and non-standard disease label, with **no clinical trials** and **no supporting literature** currently identified for this specific pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed by this evidence pack's regulatory data (no Australian licenses on file). Based on established pharmacology, flutamide is a nonsteroidal antiandrogen used for metastatic prostate cancer as part of combined androgen blockade. |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, flutamide is a nonsteroidal antiandrogen that competitively blocks the androgen receptor, inhibiting testosterone/DHT signalling in androgen-sensitive tissue — the basis for its established role in prostate cancer treatment.

The predicted label "prostate cancer/brain cancer susceptibility" is a composite, non-standard diagnostic term rather than a single defined condition. The prostate cancer component is mechanistically consistent with flutamide's known antiandrogen action. The brain cancer susceptibility component, however, has no established link to androgen receptor blockade, and the evidence pack's own rationale for this candidate explicitly notes the mechanistic gap.

Critically, targeted searches against this exact predicted indication returned zero clinical trials and zero literature (query log entries 4–6), meaning the 99.98% score reflects the TxGNN knowledge-graph model only, with no corroborating real-world or published evidence. For context, other candidates in this evidence pack scored similarly by TxGNN but carry markedly different evidence profiles — e.g., "male reproductive organ cancer" (rank 6) has 50 clinical trials and 20 publications, though that indication substantially overlaps with flutamide's already-established prostate cancer use rather than representing a genuine new repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Flutamide currently holds no ARTG registration in Australia (market status: Not Marketed; 0 licenses on file). No product, dosage form, or approved indication data is available from this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (nonsteroidal antiandrogen; ATC class L02BB — not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the Product Information (PI) — no toxicity data available in this evidence pack |
| Emetogenicity Classification | Please refer to the Product Information (PI) — no toxicity data available in this evidence pack |
| Monitoring Items | Please refer to the Product Information (PI) — no toxicity data available in this evidence pack |
| Handling Protection | Please refer to the Product Information (PI) — no toxicity data available in this evidence pack |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Both the key warnings and contraindications fields, and the drug interaction (DDI) query, returned no usable data in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (Evidence Level L5) with zero corroborating clinical trials or literature, and the predicted indication itself is a non-standard composite label rather than a clearly defined disease. Combined with the absence of Australian market presence and a Blocking-severity gap in TGA-approved PI safety data, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TGA-approved Product Information (safety warnings, contraindications) — currently a Blocking data gap
- Detailed mechanism of action data from DrugBank — currently a High-severity data gap
- Clarification of the composite disease label into distinct, standard diagnostic terms so each component can be evaluated separately
- Preclinical or mechanistic evidence specifically linking androgen receptor blockade to brain cancer susceptibility
- If further prostate-cancer-specific repurposing is of interest, review rank-6 candidate ("male reproductive organ cancer", L1 evidence) separately, noting it reflects flutamide's established use rather than a novel indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

