---
layout: default
title: Gabapentin
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Gabapentin
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

# Gabapentin: From Anticonvulsant Use to Acne (disease)

## One-Sentence Summary

Gabapentin is a gabapentinoid anticonvulsant with well-established international use for partial seizures and neuropathic pain, though no ARTG-registered product was found for it in this evidence pack (Australian market status: Not Marketed). The TxGNN model's top-ranked prediction for gabapentin is **Acne (disease)**, but this is currently supported only by a single, apparently mismatched case report and **no clinical trials** — an evidence level of **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack (DrugBank original indications and MOA are both data gaps). Literature returned elsewhere in this pack describes gabapentin as an anticonvulsant used for partial/tonic-clonic seizures and neuropathic pain. |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 98.46% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for gabapentin is not available in this evidence pack (flagged as a High-severity data gap). From literature returned elsewhere in this pack, gabapentin is known to bind the α2δ subunit of voltage-gated calcium channels, reducing glutamate/substance P release — a mechanism well established for its anticonvulsant and neuropathic-pain uses, but with no known relevance to acne pathophysiology (sebum production, comedogenesis, or *Cutibacterium acnes* activity).

For this specific top-ranked prediction, no mechanistic pathway linking gabapentin to acne is provided anywhere in the evidence pack, and no clinical trials were returned. The single literature record retrieved (PMID 22278969) is a case report titled "Unusual case of a swollen painful toe in a young man" — a topic unrelated to both acne and gabapentin's known pharmacology, and most plausibly a literature-search mismatch rather than genuine supporting evidence.

Given this, the prediction should be treated as a pure knowledge-graph association (TxGNN rank 14,906 of the model's output) rather than a clinically or mechanistically grounded hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22278969](https://pubmed.ncbi.nlm.nih.gov/22278969/) | 2012 | Case report (unrelated topic) | Arthritis care & research | Describes a swollen, painful toe in a young man; no abstract available, and the content does not relate to acne or gabapentin — likely a literature-search mismatch rather than supporting evidence. |

---

## Australia Market Information

No ARTG entries were returned for gabapentin in this evidence pack (market status: Not Marketed, total ARTG entries: 0).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There are no clinical trials and no credible literature supporting gabapentin for acne — the sole literature match appears to be an indexing/retrieval error, not genuine evidence.
- Evidence level is L5 (model prediction only, decision stage S0); the mechanistic case is unestablished.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for gabapentin (currently a data gap)
- TGA-approved Product Information / warnings and contraindications (currently a Blocking-severity data gap, required before any S1 safety screening)
- A manual check of whether the acne literature match reflects a genuine record or a search/indexing error, and re-query of PubMed/ClinicalTrials.gov specifically for "gabapentin AND acne"
- Any real preclinical or clinical rationale connecting α2δ calcium-channel modulation to acne pathophysiology before further investment

**Note:** within this same evidence pack, other candidate indications for gabapentin — notably *epilepsy with generalized tonic-clonic seizures* and *myofascial pain syndrome* (both L2, with completed Phase 2/3 trials) — have substantially stronger supporting evidence and may warrant separate evaluation ahead of this acne signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

