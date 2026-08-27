---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (PPAR-γ agonist) established as an insulin-sensitising treatment for type 2 diabetes mellitus, though it does not currently hold an Australian market authorisation in this evidence pack. The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this is supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (T2DM) — inferred from drug class/literature; no formal Australian approved-indication text is available in this pack |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for Pioglitazone is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology reflected in the source literature, Pioglitazone is a thiazolidinedione that acts as a PPAR-γ agonist and insulin sensitiser, an efficacy that is well established for type 2 diabetes.

For the top-ranked candidate, Opsismodysplasia, the evidence pack's own mechanistic review is explicit that no meaningful pathway overlap exists: this condition is a skeletal dysplasia caused by *INPPL1* (SHIP2) mutations, and there is no known relationship between that pathway and PPAR-γ/insulin-sensitising signalling. The assessment attributes the high TxGNN score to statistical proximity within the knowledge graph (a metabolic–skeletal node adjacency) rather than genuine mechanistic evidence.

None of the ten ranked candidates in this pack currently have direct supporting evidence: eight (including Opsismodysplasia) have zero clinical trials and zero literature, and the one candidate with literature hits (pancreatic agenesis, rank 9) was assessed as a likely keyword false-match (general T2DM/insulin-resistance reviews surfaced by co-occurring terms "diabetes"/"insulin," not disease-specific studies). Two lipodystrophy-related candidates (ranks 5 and 8) have a plausible biological rationale — PPAR-γ is a core regulator of adipocyte differentiation, and TZDs have literature precedent in some lipodystrophies — but no trial or publication evidence exists for them in this pack either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high TxGNN model score (L5, S0) with zero clinical trials or literature, and the evidence pack's own mechanistic review found no credible pathway linking Pioglitazone's insulin-sensitising action to Opsismodysplasia's skeletal dysplasia pathogenesis — the score is assessed as a knowledge-graph artefact rather than a genuine signal.

**To proceed, the following is needed:**
- TFDA/TGA Product Information warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed, structured mechanism-of-action documentation for Pioglitazone (currently a High-severity data gap)
- Independent preclinical or mechanistic studies directly linking Pioglitazone to Opsismodysplasia, or reconsideration of candidates with stronger biological plausibility (e.g., the lipodystrophy-related predictions, ranks 5 and 8, where PPAR-γ's role in adipocyte biology offers a more defensible rationale, though these also currently lack trial/literature support)
- Australian market/regulatory data, since Pioglitazone is not currently marketed in Australia (0 ARTG entries)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

