---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic conventionally used to treat bacterial infections. The TxGNN model's highest-ranked prediction for this drug is **Polyclonal Hyperviscosity Syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests solely on the model's score, with no corroborating mechanistic, clinical, or literature evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no ARTG entries or `original_indications` recorded). Elsewhere in this same evidence pack, Ofloxacin is described as a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase/topoisomerase IV, used for bacterial infections |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ofloxacin (`original_moa` is a data gap). Elsewhere in this evidence pack, Ofloxacin is consistently described as a fluoroquinolone-class antibiotic acting via inhibition of bacterial DNA gyrase and topoisomerase IV — a mechanism relevant to treating bacterial infections, not plasma protein disorders.

Polyclonal hyperviscosity syndrome is a disorder of excess circulating immunoglobulins (a blood/immune pathology), not an infectious process. The evidence pack's own rationale for this candidate states explicitly that there is **no identifiable mechanistic link** between an antibacterial agent and the pathophysiology of hyperviscosity syndrome, and that the prediction is a TxGNN model score with no supporting clinical or literature evidence.

In short, this is a case where the model's statistical score is not mechanistically or clinically substantiated. It should be treated as a low-confidence, exploratory signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Ofloxacin is not currently marketed in Australia (no ARTG entries), so no TGA-approved Product Information exists for this drug. Key warnings, contraindications, and drug-interaction data are all unavailable in this evidence pack (DDI query status: not found). Please refer to the Product Information/label approved by the drug's registering regulatory authority (e.g. FDA, EMA, or country of origin) for safety information, and obtain the TFDA label and DrugBank MOA data (flagged as outstanding data gaps, see below) before any safety assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has Evidence Level L5 — a model prediction only, with no clinical trials, no literature, and no plausible mechanistic rationale connecting an antibacterial agent to an immunoglobulin/plasma-viscosity disorder. There is insufficient basis to advance this specific indication.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings/contraindications for Ofloxacin (currently a Blocking data gap — required before any safety screening)
- Mechanism of action data via DrugBank API (currently a High-priority data gap)
- Documented original indication(s) and Australian regulatory/market status confirmation
- Any future clinical or preclinical evidence directly linking Ofloxacin to hyperviscosity/immunoglobulin pathology, should it emerge

**Note on other candidates in this evidence pack:** two other TxGNN predictions for Ofloxacin show materially stronger evidence and may warrant separate evaluation — *monoclonal gammopathy* (rank 6, Evidence Level L2, supported by a Phase 3 RCT of levofloxacin infection prophylaxis in myeloma, recommendation "Research Question") and *septicemic plague* (rank 7, Evidence Level L3, supported by multiple animal-model studies and FDA Animal Rule approval of the fluoroquinolone class, recommendation "Proceed with Guardrails"). These are not covered by this report, which is scoped to the top-ranked prediction only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

