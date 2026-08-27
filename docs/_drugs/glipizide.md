---
layout: default
title: Glipizide
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Glipizide
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

# Glipizide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

> Glipizide is a second-generation sulfonylurea used to manage type 2 diabetes mellitus by stimulating pancreatic β-cell insulin secretion.
> The TxGNN model predicts a possible association with **Opsismodysplasia**, a rare skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely embedding-space artefact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from mechanism-of-action references within the evidence pack; not provided as a structured field) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glipizide was not returned as a structured field in this evidence pack (flagged as a High-severity data gap). However, the evidence pack's own rationale text for related candidates consistently describes glipizide's known pharmacology as a sulfonylurea that acts on pancreatic β-cell KATP channels to stimulate insulin secretion — the standard mechanism for glucose control in type 2 diabetes.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in the *INO80D* gene, affecting chromatin remodelling during bone development. Based on the evidence pack's mechanistic assessment, there is **no identifiable biological pathway connecting glipizide's insulin-secretagogue action to INO80D-mediated skeletal development** — the two conditions do not share any known receptor, enzyme, or signalling pathway.

The evidence pack's own reviewer explicitly assesses this candidate as likely **high-score noise in the TxGNN embedding space** rather than a genuine repurposing signal. This assessment is consistent with the complete absence of clinical or literature evidence below, and is reinforced by the fact that several other top-ranked predictions for this drug (e.g. stiff person syndrome variants, lipodystrophy subtypes) were independently flagged with the same "no mechanistic pathway" conclusion — suggesting this cluster of high TxGNN scores may reflect a systematic embedding artefact rather than a disease-specific signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries were found — glipizide is not currently marketed in Australia under this evidence pack (0 licences on record).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack (TFDA/PI warning data is flagged as a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, literature, or plausible mechanistic evidence linking glipizide to opsismodysplasia — the drug's evidence pack itself assesses this top-ranked prediction as likely embedding-space noise rather than a genuine repurposing candidate. Combined with the drug's current non-marketed status in Australia, this candidate does not warrant progression at this time.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank — currently a High-severity data gap
- Independent biological rationale (e.g. genetic, cellular, or animal model data) connecting sulfonylurea pharmacology to *INO80D*-related skeletal development, before any further evidence collection is justified
- Given the pattern of similarly unsupported high-scoring predictions for this drug, consider a broader review of whether this TxGNN embedding cluster is reliable before investing further review effort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

