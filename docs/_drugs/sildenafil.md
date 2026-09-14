---
layout: default
title: Sildenafil
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From Erectile Dysfunction to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Sildenafil is a phosphodiesterase type 5 (PDE5) inhibitor best known for erectile dysfunction and pulmonary arterial hypertension. The TxGNN model's top-ranked prediction for this drug is **Ambras type hypertrichosis universalis congenita**, an extremely rare congenital hypertrichosis syndrome, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a knowledge-graph embedding signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction / pulmonary arterial hypertension (general knowledge — not present as sourced data in this evidence pack) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a data gap, DG002). Based on general knowledge, sildenafil inhibits PDE5, raising intracellular cGMP and causing vascular smooth muscle relaxation; this mechanism is well established for erectile dysfunction and pulmonary arterial hypertension.

Ambras type hypertrichosis universalis congenita is an extremely rare congenital genetic disorder characterised by generalised excessive hair growth from birth, typically linked to chromosomal rearrangements near the *TRPS1*/*EXT1* region rather than vascular or cGMP signalling pathways. There is no known pharmacological or pathophysiological link between PDE5 inhibition and this condition.

Per the model output's own rationale, this candidate reflects "only a high TxGNN knowledge-graph embedding similarity score, with no clinical trial or literature support, and no known mechanism connecting sildenafil to this very rare congenital syndrome." It should be treated as a low-confidence signal rather than a biologically grounded hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for sildenafil in this evidence pack (total_licenses = 0; market_status = not marketed).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 (model-prediction-only) candidate with no clinical trial or literature evidence, and no plausible mechanistic link between PDE5 inhibition and this rare congenital syndrome. There is insufficient basis to advance it beyond hypothesis generation.

**To proceed, the following is needed:**
- TGA-approved Product Information / warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism of action data for sildenafil (DG002)
- Any preclinical or case-level evidence specifically linking PDE5 inhibition to hypertrichosis-type congenital syndromes, before this candidate can move beyond S0
- Consider instead prioritising other candidates in this drug's prediction set with stronger evidence — notably rank 9, "genetic alopecia" (L3, decision stage S2, "Research Question"), which is supported by two clinical trials (including a completed RCT, NCT06527729) and direct mechanistic literature (PMID 30292404) on sildenafil and hair growth
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

