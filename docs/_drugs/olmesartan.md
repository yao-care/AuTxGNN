---
layout: default
title: Olmesartan
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Olmesartan
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

# Olmesartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker (ARB) used for blood pressure and cardiac afterload control. The TxGNN model's top-ranked prediction suggests potential efficacy for **Prinzmetal angina**, but this is currently a **pure model-based prediction with no supporting clinical trials or published literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Olmesartan is an ARB; this class is typically indicated for hypertension) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Olmesartan is not available in this evidence pack. Based on known pharmacology, Olmesartan is an angiotensin II receptor blocker that antagonises the AT1 receptor, regulating systemic blood pressure and cardiac afterload.

Prinzmetal (variant) angina is primarily driven by coronary artery vasospasm, for which calcium channel blockers are the established first-line treatment. ARB-mediated AT1 blockade has no established direct mechanistic link to coronary vasospasm control.

This prediction is generated purely from TxGNN knowledge-graph embedding similarity. The evidence pack itself notes no known mechanistic connection between AT1 receptor blockade and coronary vasospasm, so biological plausibility for this specific candidate is low. By contrast, other TxGNN-ranked candidates for this drug — migraine disorder (L2, one pilot RCT plus a systematic review) and pulmonary hypertension (L4, multiple preclinical models) — carry substantially more supporting evidence than this top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Olmesartan currently has no ARTG entries (Not Marketed status in Australia).

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) were available in this evidence pack. As Olmesartan is not currently marketed in Australia, no TGA-approved Product Information exists for local reference at this time; safety assessment would need to draw on overseas regulatory labelling (e.g. FDA, EMA) pending TGA registration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial or literature evidence for Prinzmetal angina, and the proposed mechanism lacks an established link to coronary vasospasm. Olmesartan is also not currently marketed in Australia (0 ARTG entries), and both MOA and product-label safety data are flagged as gaps in this evidence pack.

**To proceed, the following is needed:**
- Confirmed original approved indication/labelling text
- MOA detail from DrugBank (currently marked a High-severity data gap)
- TFDA/TGA product information — warnings and contraindications (currently marked a Blocking data gap)
- Preclinical or mechanistic studies directly linking AT1 blockade to coronary vasospasm
- If pursuing a repurposing candidate for this drug, consider prioritising **migraine disorder** (L2, Research Question) or **pulmonary hypertension** (L4, Research Question), which currently have stronger evidence bases than Prinzmetal angina
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

