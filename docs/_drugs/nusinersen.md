---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

# Nusinersen: From Spinal Muscular Atrophy to Fallopian Tube Serous Adenofibroma

## One-Sentence Summary

Nusinersen is an antisense oligonucleotide approved for spinal muscular atrophy (SMA), acting by modulating SMN2 pre-mRNA splicing. The TxGNN model's top-ranked prediction for this drug is **Fallopian Tube Serous Adenofibroma**, but the score sits at the model's near-random baseline (0.5) and is supported by **zero clinical trials** and **zero publications**. This is not a credible repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) |
| Predicted New Indication | Fallopian Tube Serous Adenofibroma |
| TxGNN Prediction Score | 50.00% (rank 929,877 of all drug-disease pairs) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable in this evidence pull (DrugBank query flagged as a data gap). Based on general knowledge captured in the evidence pack's own annotations, nusinersen is an antisense oligonucleotide that targets SMN2 pre-mRNA splicing to increase functional SMN protein production, and its proven efficacy is in spinal muscular atrophy — a neuromuscular disease.

Fallopian tube serous adenofibroma is a rare benign/borderline gynaecological tumour with no known pathophysiological connection to SMN protein deficiency or splicing regulation. There is no shared gene, pathway, or tissue biology linking the two conditions, and this holds true for the other nine top-ranked candidates in this evidence pack as well (which span oncology, thrombosis, infection, and unrelated tumour types).

Notably, all ten top-ranked predictions carry the identical TxGNN score of 0.5, which is the model's near-random baseline rather than a meaningful confidence signal. This pattern, combined with the complete absence of clinical trials, registry entries, or literature across all ten candidates, indicates this particular drug-indication cluster does not currently represent a credible repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

Nusinersen is not currently marketed in Australia under this evidence pack's data — no ARTG entries were found.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this and all other top-ranked candidates sits at the model's near-random baseline (0.5), with no clinical trials, registry entries, or literature to support any of them, and no plausible mechanistic link between nusinersen's SMN2-splicing activity and fallopian tube serous adenofibroma. There is currently no basis to advance this candidate beyond model output.

**To proceed, the following is needed:**
- Confirmed MOA data from DrugBank/TGA-approved PI (currently a data gap)
- TGA/TFDA product information for warnings and contraindications (currently a blocking data gap)
- An independent (non-automated) literature and trial search, since all ten automated queries returned zero results
- Re-examination of whether TxGNN candidates with meaningfully higher scores exist for this drug beyond this near-baseline cluster, before committing further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

