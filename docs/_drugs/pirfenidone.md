---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an antifibrotic agent (its documented mechanism targets TGF-β signalling and fibroblast proliferation); this evidence pack does not contain a structured original-indication record, but pirfenidone is internationally recognised for idiopathic pulmonary fibrosis. The TxGNN model's top-ranked prediction for this drug is **Extracutaneous Mastocytoma**, but this signal is currently supported by **zero clinical trials** and **zero publications** — it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no ARTG licences or `original_indications` records returned). Pirfenidone is widely known as an antifibrotic used for idiopathic pulmonary fibrosis — noted here as general background, not sourced from this pack |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Australia Market Status | Not currently marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in this evidence pack (`original_moa` is a data gap). However, the model's own rationale text describes pirfenidone's known action as inhibition of TGF-β signalling and fibroblast proliferation — consistent with its established antifibrotic use.

Extracutaneous mastocytoma is pathologically driven by KIT-mutation-related mast cell proliferation, a mechanism that does not overlap with TGF-β/fibroblast pathways. The evidence pack's own mechanistic assessment for this candidate states there is "no known intersection" between pirfenidone's fibroblast-inhibitory action and mast-cell-driven pathology, and explicitly characterises the link as speculative with no supporting evidence. In other words, this is the highest-scoring candidate by TxGNN's topological similarity metric, but the model score is not corroborated by a plausible mechanism or by any external evidence.

For context, one lower-ranked candidate in this pack (fibroblastic neoplasm, rank 9) has a mechanistically more coherent rationale and six supporting publications — but that literature also contains case reports of pirfenidone-associated sarcoma development and dermatofibroma aggravation, a safety signal worth carrying forward regardless of which indication is pursued (see Safety Considerations below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries were returned for this drug in the evidence pack (`total_licenses = 0`, market status: not currently marketed). No product/dosage-form information is available to tabulate.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — this evidence pack's `key_warnings`, `contraindications`, and drug-interaction (DDI) fields are all unpopulated (DDI query status: not found).

**Additional signal from literature (not PI-sourced):** publications surfaced under a different candidate indication in this same evidence pack (fibroblastic neoplasm, rank 9) include two case reports of concern — multiple eruptive dermatofibromas aggravated by pirfenidone in a systemic sclerosis patient (PMID 32572469), and undifferentiated pleomorphic sarcoma following pirfenidone use (PMID 29702057). These suggest pirfenidone's effect on fibroblastic/mesenchymal tissue may be bidirectional rather than uniformly antiproliferative, and should be flagged for any mesenchymal-lineage repurposing pathway, including mastocytoma if pursued.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-only signal: no clinical trials, no literature, and the model's own mechanistic rationale finds no credible link between pirfenidone's known TGF-β/fibroblast pathway and the KIT-driven pathology of extracutaneous mastocytoma. Combined with the drug's non-marketed status in Australia and a blocking gap in TFDA/PI safety data (DG001), there is no basis to advance this candidate beyond a research hypothesis.

**To proceed, the following is needed:**
- TGA-approved Product Information for pirfenidone (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Preclinical or mechanistic studies directly linking pirfenidone to mast cell biology or KIT-pathway modulation
- If mesenchymal/fibroblastic-lineage indications are explored instead, dedicated review of the sarcoma-induction and dermatofibroma-aggravation case reports noted above before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

