---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 653
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is a selective alpha-1A adrenergic receptor antagonist used to relieve lower urinary tract symptoms associated with benign prostatic hyperplasia (BPH). The TxGNN model's top prediction for this drug is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth syndrome — but this prediction is currently supported by **zero clinical trials and zero publications**, and the model's own rationale flags no plausible biological mechanism connecting the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH) / lower urinary tract symptoms (inferred from drug class and co-therapy context; not separately confirmed in this evidence pack) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% (rank 140 overall) |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the model's own repurposing rationale, tamsulosin is a selective alpha-1A adrenergic receptor antagonist that relaxes smooth muscle in the prostate and bladder neck, and its established clinical role is managing BPH-related urinary symptoms (it is frequently co-prescribed with 5-alpha reductase inhibitors such as finasteride/dutasteride).

Ambras type hypertrichosis universalis congenita is a rare congenital disorder driven by chromosomal rearrangement and gene-regulatory abnormalities affecting hair follicle development — a pathway that has no known interaction with alpha-1 adrenergic signalling. The model's own mechanistic annotation for this candidate explicitly states there is no biological link between the two, and no clinical or literature evidence exists to support it.

Taken together, this candidate should be treated as a **low-confidence, likely spurious association** arising from graph-based pattern learning rather than a genuine pharmacological signal. It is presented here for completeness and transparency, not as a promising repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no supporting clinical trials, no supporting literature, and the model's own mechanistic annotation identifies no plausible biological link between tamsulosin's alpha-1 antagonism and this rare congenital hypertrichosis syndrome. This is an L5 (prediction-only) signal with no path to advancement as currently evidenced.

**To proceed, the following is needed:**
- TFDA/TGA-approved product information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank — currently a High-severity data gap (DG002)
- Independent mechanistic or preclinical rationale connecting alpha-1 adrenergic antagonism to hair follicle/keratin pathways, before any further evidence collection is warranted
- Consideration of lower-ranked candidates in this evidence pack (e.g. rank 9, "alopecia") if a hair-related indication is of interest, though that candidate also currently lacks direct drug-disease evidence and remains at Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

