---
layout: default
title: Moxonidine
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# Moxonidine: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Moxonidine is a centrally-acting antihypertensive — a selective imidazoline I1-receptor agonist used to treat essential hypertension (per the repurposing rationale in this evidence pack; formal indication data is not recorded separately).
The TxGNN model's top-ranked prediction is **Hypotrichosis Simplex of the Scalp**, a hereditary hair-follicle disorder, with a prediction score of **99.95%**.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, and the evidence pack itself notes no known mechanistic link — this is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in formal registration data (drug not marketed in Australia); referenced as hypertension in the prediction rationale narrative |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for moxonidine (flagged as a data gap in this evidence pack). Based on the narrative accompanying other candidate predictions in this pack, moxonidine is described as a selective imidazoline I1-receptor agonist acting on the rostral ventrolateral medulla (RVLM) to suppress sympathetic outflow, and is used clinically to lower blood pressure in essential hypertension.

Hypotrichosis simplex of the scalp is a hereditary disorder of hair-follicle development, unrelated to blood pressure regulation. The evidence pack's own assessment for this prediction states explicitly that there is **no known mechanistic link** between moxonidine's sympatholytic, antihypertensive action and this condition. No clinical trials or literature were found connecting the two.

In short, this is a high-scoring but mechanistically unsupported model output — the score reflects a pattern learned by TxGNN across the knowledge graph, not a validated biological hypothesis. Readers should treat this as a candidate for further research screening only, not as a signal with independent clinical or scientific corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Australia Market Information

Moxonidine has no ARTG entries and is not currently marketed in Australia (0 licenses on record in this evidence pack).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Note: this evidence pack flags TGA/PI warning and contraindication data as a blocking data gap — DG001 — so safety cannot be independently assessed from the data provided here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hypotrichosis simplex of the scalp) has no supporting clinical trials, no literature, and no plausible mechanistic link per the pack's own assessment — it is an L5, model-score-only signal (rank 1108 among all TxGNN predictions for this drug).

**To proceed, the following is needed:**
- Moxonidine's mechanism of action (MOA) data (DG002, High severity)
- TGA-approved Product Information — warnings and contraindications (DG001, Blocking severity)
- Independent mechanistic or preclinical rationale connecting moxonidine to hair-follicle biology before this candidate can move beyond S0

**Note for reviewers:** this evidence pack also contains lower-scoring but more mechanistically coherent candidates for moxonidine — e.g. malignant hypertensive renal disease, malignant renovascular hypertension, and primary hereditary glaucoma (all L4, S1, "Research Question") — where the rationale draws on plausible class-effect or downstream-pathology reasoning, though these likewise lack direct trials or literature. If the goal is identifying a scientifically defensible repurposing hypothesis rather than the single highest TxGNN score, those candidates may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

