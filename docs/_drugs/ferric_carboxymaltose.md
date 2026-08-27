---
layout: default
title: Ferric Carboxymaltose
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Ferric Carboxymaltose
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

# Ferric Carboxymaltose: From Iron Deficiency Anaemia to Bronchitis

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement therapy, established for treating iron deficiency anaemia. The TxGNN model predicts it may also be effective for **Bronchitis**, but this direction is currently supported by **no clinical trials and no published literature** — the signal comes from the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anaemia (general clinical knowledge; not documented in the evidence pack — `original_indications` is empty) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ferric carboxymaltose in this evidence pack. Based on general clinical knowledge, ferric carboxymaltose is an intravenous iron-carbohydrate complex used to correct iron deficiency anaemia across a range of settings (e.g. chronic kidney disease, heart failure, inflammatory bowel disease, heavy uterine bleeding). Its efficacy in replenishing iron stores and correcting anaemia is well established.

Bronchitis is an infectious/inflammatory airway condition with no established pharmacological link to iron repletion. The evidence pack's own repurposing rationale states explicitly: *"無已知機轉關聯，鐵劑補充與支氣管炎之病理生理無直接連結，僅為 TxGNN 高分預測，缺乏臨床或機轉證據支持"* (no known mechanistic link; iron supplementation has no direct connection to bronchitis pathophysiology; this is a high TxGNN score only, without clinical or mechanistic support).

This prediction should therefore be treated as a model-generated hypothesis rather than a mechanistically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (bronchitis) has an L5 evidence level — a high TxGNN score with no supporting clinical trials, literature, or plausible mechanistic link. There is insufficient basis to advance this indication beyond the model-prediction stage.

**To proceed, the following is needed:**
- TFDA/TGA product information (warnings, contraindications) — currently a **blocking** data gap (DG001); safety cannot be evaluated without it
- Mechanism of action data from DrugBank (DG002)
- Any preclinical or mechanistic studies linking iron repletion to airway/respiratory inflammation, should they emerge

**Note for reviewers:** Among this drug's other predicted indications, **rank 2 (thrombotic disease)** carries materially stronger preliminary support — an L4 evidence level with an animal-model mechanistic link (iron-deficiency-induced thrombocytosis) and a completed Phase 4 trial in a related population — and may be a more productive candidate for further evaluation than bronchitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

