---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: From Gastrointestinal Stromal Tumour (GIST) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib (marketed overseas as Qinlock) is a tyrosine kinase inhibitor whose approved use targets advanced gastrointestinal stromal tumour (GIST); this specific indication is not recorded in the structured regulatory data of this evidence pack. The TxGNN model's top prediction for this drug is **Multiple Endocrine Neoplasia**, but this candidate is currently supported by **zero clinical trials** and **zero relevant publications** — the prediction is a knowledge-graph signal only, and the pack's own mechanistic review argues against biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no ARTG entries, `original_indications` empty). Ripretinib's known overseas-approved use is advanced gastrointestinal stromal tumour (GIST). |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ripretinib is a data gap in this evidence pack. Based on the drug's known profile (referenced within the evidence pack's own rationale text), Ripretinib is a switch-control tyrosine kinase inhibitor targeting KIT and PDGFRA, approved overseas for advanced GIST after prior therapy failure.

Multiple endocrine neoplasia (particularly MEN2) is driven primarily by mutations in the RET proto-oncogene — a different receptor tyrosine kinase target to KIT/PDGFRA. The evidence pack's own mechanistic assessment states explicitly that there is **no direct inhibitory evidence or clinical data supporting cross-target activity** between Ripretinib and RET-driven disease.

While KIT/PDGFRA and RET both belong to the receptor tyrosine kinase family, shared family membership alone is not pharmacological justification. This prediction should be treated as a knowledge-graph-derived association rather than a mechanistically substantiated hypothesis. Notably, none of the top 10 TxGNN predictions for this drug (including HER2-positive breast carcinoma, several other breast cancer subtypes, and two veterinary/bovine conditions) carry supporting clinical or literature evidence — one apparent "hit" (rank 10, breast tumour luminal A/B, 19 PubMed results) is a string-matching artefact, where the abbreviation "B" matched B-cell biology and hepatitis B literature rather than breast cancer.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

*(Ripretinib is an antineoplastic tyrosine kinase inhibitor, approved overseas for GIST; this section is included on that basis, though the drug is a targeted agent rather than a conventional cytotoxic.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (switch-control KIT/PDGFRA tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high (98.84%) but is unsupported by any clinical trial or literature evidence, and the evidence pack's own mechanistic review indicates the biological target driving multiple endocrine neoplasia (RET) is not one Ripretinib is known to inhibit (KIT/PDGFRA). Missing PI/regulatory warning data also currently blocks entry into initial safety screening.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) for Ripretinib — currently missing and blocks safety pre-screening
- Confirmed mechanism-of-action data for Ripretinib
- Direct experimental or clinical evidence of activity against RET-driven disease, if this specific indication is to be pursued further
- If exploring alternatives, note that all top 10 TxGNN-predicted indications for this drug are evidence level L5 (no trials, negligible or noise-only literature) — none currently warrant progression past model-prediction stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

