---
layout: default
title: Mebeverine
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Mebeverine
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

# Mebeverine: From an Unspecified Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Mebeverine's original indication and mechanism of action are not specified in the current evidence pack. The TxGNN model predicts potential relevance to **Cauda Equina Syndrome**, with a prediction score of **98.01%**, but there are currently **no clinical trials and no published literature** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (no ARTG record, no `original_indications` data) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 98.01% (model rank 18,606) |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mebeverine is not available in this evidence pack, and no original indication is recorded either — the drug is not registered in Australia (0 ARTG entries), so there is no local approved-indication text to compare against.

Without a documented MOA or a confirmed original indication, a mechanistic rationale linking mebeverine to Cauda Equina Syndrome cannot be constructed from the data provided. Cauda Equina Syndrome is a neurosurgical emergency caused by compression of the lumbosacral nerve roots, and it is not a condition typically addressed through pharmacotherapy alone — this makes the prediction clinically unusual on its face, and it is worth flagging that plausibility could not be assessed against known pharmacology here.

This prediction should therefore be treated as a hypothesis generated purely by the TxGNN knowledge-graph model, not as one corroborated by mechanistic or clinical reasoning at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: a single unrelated-topic PubMed record (PMID 19334485, on gastroesophageal reflux disease) was returned for a lower-ranked prediction, "gastroduodenitis" (rank 8, score 81.1%) — not for the top-ranked Cauda Equina Syndrome prediction above.)*

---

## Australia Market Information

Mebeverine currently has no ARTG entries and is not marketed in Australia.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) were returned by the queried sources. Mebeverine holds no ARTG registration in Australia, so no TGA-approved Product Information is available locally. Clinicians should consult overseas regulatory sources (e.g. UK MHRA SmPC, EU EMA labelling) for interim safety guidance until local data can be obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Cauda Equina Syndrome) has no clinical trial or literature support (L5 — model prediction only), no MOA data to establish mechanistic plausibility, and the drug is not currently marketed in Australia. This does not meet the bar to proceed.

**To proceed, the following is needed:**
- Mechanism of action data (DG002, High severity) via DrugBank API
- TFDA/overseas PI warnings and contraindications (DG001, Blocking — currently prevents any S1 safety screening)
- Independent literature/clinical evidence specifically linking mebeverine to Cauda Equina Syndrome, or reconsideration of a lower-ranked candidate with at least partial evidence (e.g. rank 8, gastroduodenitis, which returned one PubMed record)
- Confirmation of mebeverine's original approved indication, since this is currently absent from the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

