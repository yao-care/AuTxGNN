---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Insulin Lispro
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

# Insulin lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue originally used to manage blood glucose in patients with diabetes mellitus (type 1 and type 2).
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**,
however **no clinical trials** and **no published literature** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes mellitus (type 1 and type 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this dataset. Based on established pharmacology, insulin lispro is a rapid-acting insulin analogue in which lysine and proline at positions B28 and B29 are transposed, reducing self-aggregation and accelerating subcutaneous absorption relative to human insulin. It acts primarily via the insulin receptor to promote peripheral glucose uptake and suppress hepatic glucose production.

Autoimmune oophoritis is a rare inflammatory condition in which immune-mediated attack on ovarian tissue leads to granulosa cell destruction and premature ovarian insufficiency. The proposed biological connection lies in the fact that insulin receptors are expressed on ovarian granulosa and theca cells, and insulin signalling is known to modulate steroidogenesis and the local ovarian immune microenvironment. TxGNN likely captured this relationship through the shared comorbidity network of polycystic ovary syndrome (PCOS) → insulin resistance → ovarian inflammation, rather than through a direct therapeutic pathway.

There is, however, no direct pathophysiological evidence that insulin lispro can attenuate the underlying autoimmune mechanism of oophoritis. The predicted link appears to be a network-level co-occurrence rather than a tractable clinical mechanism. This prediction should be interpreted with significant caution and is best regarded as a hypothesis-generating signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Insulin lispro is not currently recorded in the Australian Register of Therapeutic Goods (ARTG) within this dataset (data cutoff: 22 June 2026). No ARTG entries were returned by the evidence collection pipeline.

> **Note:** This may reflect a data gap in the pipeline rather than a genuine absence from the Australian market. Clinicians should verify current ARTG registration status directly via the [TGA website](https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.78%), the mechanistic link between insulin lispro and autoimmune oophoritis is indirect and entirely network-driven, with no supporting clinical trials or published literature (Evidence Level L5). There is no plausible direct therapeutic mechanism by which insulin lispro would modulate the autoimmune pathology underlying oophoritis.

**To proceed, the following is needed:**
- Verification of ARTG registration status via the TGA website
- Retrieval of TGA-approved Product Information (PI) for full safety, warnings, and contraindication data
- Detailed mechanism of action data (MOA) from DrugBank or primary pharmacology literature
- Preclinical evidence (in vitro or animal model) demonstrating that insulin receptor signalling in granulosa cells directly influences autoimmune inflammation
- Clarification of whether TxGNN prediction score reflects a therapeutically meaningful edge or a structural artefact of the PCOS–insulin resistance comorbidity cluster in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

