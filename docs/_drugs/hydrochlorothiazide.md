---
layout: default
title: Hydrochlorothiazide
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydrochlorothiazide (HCTZ) is a well-established thiazide diuretic, clinically proven for the management of hypertension and oedema across decades of global use.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction score of **98.42%**; however, **no clinical trials** and **no supporting publications** specific to this indication were identified, placing the evidence at model-prediction level only.
The high score most likely reflects generalisation from HCTZ's broad antihypertensive role rather than a targeted mechanistic advantage in this severe renal subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, oedema |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L5 |
| Australia Market Status | Not registered in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established pharmacology, Hydrochlorothiazide is a thiazide diuretic that inhibits the sodium-chloride cotransporter (NCC) in the distal convoluted tubule of the kidney, promoting natriuresis and diuresis, reducing circulating plasma volume, and consequently lowering systemic blood pressure.

Malignant hypertensive renal disease is a life-threatening emergency characterised by severely elevated blood pressure coupled with rapid-onset renal injury (thrombotic microangiopathy, fibrinoid necrosis of arterioles). The knowledge graph likely generated this association by extending HCTZ's well-documented hypertension relationship to this extreme renal subtype.

However, a critical mechanistic limitation exists: as GFR falls sharply in malignant hypertensive nephropathy, tubular delivery of thiazides diminishes markedly, substantially reducing diuretic efficacy. Current clinical guidelines favour intravenous antihypertensives (e.g., labetalol, nicardipine, sodium nitroprusside) and loop diuretics for acute management, not thiazides. The high TxGNN score is therefore most likely a knowledge-graph artefact of broad hypertension–HCTZ co-occurrence rather than evidence of a genuine therapeutic role in this severe subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Hydrochlorothiazide (as a stand-alone active ingredient) is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. No individual product entries were identified.

> **Note for clinicians:** HCTZ is widely available globally and may exist in Australia as a component of fixed-dose combination antihypertensive products (e.g., combined with an ACE inhibitor or ARB). A comprehensive ARTG search including combination formulations is recommended before assuming unavailability.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (98.42%), the mechanistic fit for malignant hypertensive renal disease is poor — thiazide diuretic efficacy is substantially curtailed in the setting of acute GFR reduction, and no clinical trial or literature evidence supports HCTZ in this specific indication. Proceeding without supporting evidence in a condition associated with high short-term mortality would not be appropriate.

**To proceed, the following is needed:**

- Conduct a full ARTG search including fixed-dose combination products containing HCTZ to confirm Australian availability
- Obtain TGA Product Information for complete safety, contraindication, and drug interaction review
- Retrieve HCTZ mechanism of action data from DrugBank (DB00999) to enable formal mechanistic linkage analysis
- Commission a targeted literature review on HCTZ use in patients with chronic kidney disease and hypertensive emergency
- Consider prioritising evaluation of better-evidenced TxGNN predictions in this report set — notably **Rank 7 (Acute Pulmonary Heart Disease, L3 evidence)** and **Rank 6 (Chronic Pulmonary Heart Disease, L4 evidence)**, both of which have supporting clinical trial or diuretic class-level RCT data (CLOROTIC trial, PMID 38215973) and may represent more actionable repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

