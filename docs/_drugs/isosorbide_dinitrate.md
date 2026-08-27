---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina Pectoris to Alopecia

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is a classic organic nitrate vasodilator used internationally for the prevention and treatment of angina pectoris and congestive heart failure, though it is currently not registered with the TGA in Australia.
The TxGNN model assigns its highest prediction score to **Alopecia** (99.99%), however there are currently **no clinical trials and no publications** specifically supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris / Congestive heart failure (global use; not TGA-registered in Australia) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ISDN is not available in this evidence pack. Based on established pharmacology, ISDN is an organic nitrate that releases nitric oxide (NO) in vivo. NO activates soluble guanylate cyclase (sGC), which elevates intracellular cyclic GMP (cGMP) levels, ultimately relaxing vascular smooth muscle to produce venodilation and arterial dilation — reducing both cardiac preload and afterload. This mechanism underpins its established use in angina pectoris and heart failure.

The proposed connection between ISDN and alopecia is speculative. The repurposing rationale suggests that NO-mediated vasodilation *may* improve microvascular perfusion around hair follicles, theoretically supporting follicular health. It is worth noting that Minoxidil — another vasodilator — is an established treatment for androgenetic alopecia, which lends some broad biological plausibility to the vasodilator–hair loss axis. However, Minoxidil acts via K_ATP channel opening, which is pharmacologically distinct from the NO/cGMP pathway. There is currently no published biological evidence that NO-mediated signalling directly influences hair follicle cycling or regeneration.

The high TxGNN prediction score most likely reflects shared neighbourhood topology between alopecia-associated nodes and vascular disease nodes in the knowledge graph, rather than a direct pharmacological signal. For context, other ISDN predictions in this analysis carry far stronger evidence: **Vascular Disease** (rank 6) is an L1-level prediction with a "Proceed with Guardrails" recommendation supported by dozens of clinical trials, and **Pulmonary Hypertension** (rank 4) carries L3-level observational and haemodynamic study support — both far more consistent with ISDN's established cardiovascular mechanism.

---

## Safety Considerations

Isosorbide dinitrate is not registered with the TGA in Australia. Please refer to the Product Information (PI) from a country where ISDN is currently approved (e.g., the United Kingdom, Japan, or the European Union) for complete safety information, including contraindications, adverse effects, and monitoring requirements.

Key drug-class safety consideration for clinical awareness:

- **Absolute contraindication with PDE5 inhibitors** (e.g., sildenafil, tadalafil, vardenafil): both drug classes act on the NO/cGMP pathway, and concurrent use can cause severe, potentially life-threatening hypotension.
- **Hypotension risk**: particularly pronounced on first dose, in volume-depleted patients, or when combined with other antihypertensives.
- **Nitrate tolerance**: continuous use can lead to haemodynamic tolerance within 24 hours; nitrate-free intervals are required in clinical dosing schedules.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score, the alopecia indication has no supporting clinical trial or literature evidence whatsoever (L5). The score is most likely an artefact of knowledge graph topology shared between alopecia and vascular disease nodes rather than a genuine pharmacological signal. Furthermore, ISDN is not currently registered with the TGA in Australia, presenting a significant regulatory barrier to any clinical application.

**To proceed, the following is needed:**
- Preclinical mechanistic studies establishing whether NO/cGMP-mediated signalling influences hair follicle biology, perifollicular microcirculation, or the hair growth cycle
- Comparative mechanistic studies versus Minoxidil to determine whether NO-pathway vasodilation provides any distinct or additive follicular benefit
- TGA registration (ARTG listing) in Australia before clinical use can be considered
- Full MOA documentation and Product Information for complete safety assessment (currently unavailable in this evidence pack)

> **Note for reviewers:** If the purpose of this pipeline is to identify actionable repurposing candidates for ISDN, the **Vascular Disease** (rank 6, L1) and **Pulmonary Hypertension** (rank 4, L3) predictions are substantially more promising and merit dedicated evaluation reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

