---
layout: default
title: Tolnaftate
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 10
---

# Tolnaftate
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

# Tolnaftate: From Superficial Fungal Skin Infections to Majocchi Granuloma

## One-Sentence Summary

> Tolnaftate is a topical antifungal originally used to treat superficial dermatophyte (tinea) infections of the skin.
> The TxGNN model predicts it may also be effective for **Majocchi granuloma**, a deep follicular dermatophyte infection,
> but this prediction is currently supported by **no clinical trials** and **no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial fungal skin infections (dermatophytosis / tinea) — inferred from evidence pack rationale text; not formally recorded in this dataset |
| Predicted New Indication | Majocchi granuloma |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for tolnaftate is not available in this evidence pack (flagged as a data gap). However, supporting rationale text elsewhere in the pack indicates tolnaftate acts as a **squalene epoxidase inhibitor**, blocking ergosterol synthesis in dermatophyte fungi — the same mechanism underlying its established use in superficial tinea infections.

Majocchi granuloma is a **deep, follicular** dermatophyte infection, caused by the same class of fungal pathogens (dermatophytes) that tolnaftate is known to act against in superficial skin layers. On this basis, the mechanistic rationale for extending tolnaftate's antifungal spectrum to Majocchi granuloma is biologically plausible.

However, the prediction has an important pharmacokinetic limitation: Majocchi granuloma involves **deep follicular and perifollicular** fungal invasion, and topical tolnaftate formulations are not established to penetrate to this depth. The evidence pack itself flags this as a concern — "the ability of a topical formulation to penetrate deep follicular infection is questionable" — meaning the mechanistic plausibility does not translate into confirmed clinical efficacy without further evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Tolnaftate is currently **not marketed** in Australia, and there are **no ARTG entries** recorded in this dataset (0 licenses).

---

## Safety Considerations

Safety data for this candidate is currently incomplete. The following data gaps have been flagged in this evidence pack:

- **TFDA/PI warnings and contraindications**: Not yet available (classified as a *Blocking* gap — this prevents the candidate from entering initial safety assessment, S1).
- **Mechanism of action detail**: Not yet available (classified as a *High* severity gap — this limits confidence in the mechanistic rationale above).
- **Drug–drug interactions**: No interaction data found (query returned no results).

Please refer to the TGA-approved Product Information (PI) for authoritative safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Majocchi granuloma) is supported only by mechanistic plausibility (L5 evidence) with no clinical trials or literature directly addressing this use. A blocking data gap also exists around TFDA-equivalent safety labelling (warnings/contraindications), which prevents progression into initial safety assessment (S1).

**To proceed, the following is needed:**
- TFDA/PI-equivalent warnings, contraindications, and precautions (blocking gap — required before any safety evaluation)
- Detailed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Preclinical or clinical evidence specifically evaluating topical/systemic tolnaftate penetration and efficacy in deep follicular (Majocchi granuloma) infections
- Confirmation of appropriate dosage form/route for deep tissue penetration, given topical formulations may be pharmacokinetically unsuited to this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

