---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From CD20+ B-Cell-Depleting Autoimmune Therapy to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody whose established pharmacological basis is B-cell depletion in autoimmune conditions (e.g. multiple sclerosis); confirmed Australian regulatory indication data is not available in this evidence pack. The TxGNN model predicts possible efficacy in **HER2 Positive Breast Carcinoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely model artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug not marketed in Australia; no ARTG-listed indication text on file. (Evidence pack notes MOA basis relates to CD20+ B-cell-driven autoimmune disease, e.g. multiple sclerosis) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap, DG002). Based on the reviewer notes accompanying this evidence pack, ocrelizumab is an anti-CD20 monoclonal antibody that depletes CD20+ B cells, with its established pharmacological application in autoimmune disease (e.g. multiple sclerosis) rather than oncology.

HER2 Positive Breast Carcinoma is driven by HER2/neu receptor overexpression and downstream PI3K/MAPK signalling — a pathway with no known mechanistic overlap with B-cell depletion. The evidence pack's own rationale for this prediction explicitly concludes that the TxGNN score (0.999) lacks an interpretable biological pathway, and that in the absence of any supporting trial or literature evidence, the score more likely reflects an embedding-space artefact than a true repurposing signal.

The same pattern holds across the other nine top-ranked candidates in this batch (hormone-receptor-driven breast cancer subtypes and several rare/paediatric neoplasms such as tongue and hypopharynx benign tumours, schwannoma, and neuroblastoma) — none show a plausible mechanistic link to CD20+ B-cell depletion, and none are supported by trial or literature evidence specific to ocrelizumab. This clustering of high scores with no discriminating evidence across mechanistically unrelated diseases is a recognised signature of low model discriminability on drugs with sparse training data, rather than a genuine repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*Note: A search for "Ocrelizumab" + "breast tumor luminal A or B" (a separate, lower-ranked candidate in this batch) returned 19 PubMed hits, but on review all were general B-cell biology/lymphoma/hepatitis-B-vaccine literature with no direct discussion of ocrelizumab in breast cancer — assessed as keyword-collision noise, not supporting evidence.*

---

## Australia Market Information

Ocrelizumab is not currently marketed in Australia under this evidence pack (0 ARTG entries on file).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence supports HER2 Positive Breast Carcinoma (or any of the other top-ranked candidates) as a repurposing indication for ocrelizumab, and the mechanistic link to the drug's known CD20+ B-cell-depleting activity is absent. Combined with a blocking data gap on TGA-approved warnings/contraindications (DG001), this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) for ocrelizumab, including warnings, contraindications, and monitoring requirements (resolves DG001)
- Structured mechanism of action data from DrugBank or equivalent source (resolves DG002)
- Independent mechanistic or preclinical rationale connecting CD20+ B-cell depletion to HER2-driven breast carcinoma, before any trial or literature evidence can be meaningfully evaluated
- Re-screening of this drug's full predicted-indication list against known pharmacology, given the current top-10 list shows no mechanistically coherent signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

