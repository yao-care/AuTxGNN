---
layout: default
title: Nicotine
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Nicotine
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

# Nicotine: From No TFDA-Registered Indication to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Nicotine has no TFDA-registered indication in this data set (0 licences, market status "not marketed"), and its original mechanism of action is not yet documented. The TxGNN model's top-ranked prediction links nicotine to **Exercise-Induced Malignant Hyperthermia**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known biological connection between nicotine's mechanism and this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indications or regulatory licences are recorded for this drug |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 83.91% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for nicotine is not currently available in this evidence pack. What is documented is that nicotine acts as a nicotinic acetylcholine receptor (nAChR) agonist.

However, according to the model's own repurposing rationale, there is **no known mechanistic connection** between nAChR agonism and the core pathophysiology of exercise-induced malignant hyperthermia, which centres on RYR1-related dysfunction of the skeletal muscle calcium channel. This prediction reflects a statistical association from the TxGNN knowledge graph (rank 110,584 out of the model's full output) rather than a biologically grounded hypothesis, and the evidence pack explicitly flags it as lacking biological plausibility.

Because both the original indication and the mechanism of action are undocumented for this drug, there is no basis in the available data to argue that nicotine's known pharmacology would transfer to this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Nicotine is currently **not marketed** under the regulatory dataset used for this report, with **0 registered licences/ARTG entries** on file. No product-level information (brand name, dosage form, approved indication) is available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction records were found in the queried database (query status: not found).

Note: mechanism-of-action data and TFDA label warnings/contraindications for this drug are currently missing from the evidence base — the label warnings gap is flagged as a **blocking** issue that prevents any safety pre-assessment (S1) from being conducted.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no supporting clinical trials or literature, the model's own rationale states there is no known biological plausibility for the mechanism-disease link, and critical safety data (product warnings/contraindications) is a blocking gap that prevents any safety review. There is currently no basis to advance this indication.

**To proceed, the following is needed:**
- TFDA product label warnings and contraindications (blocking gap — required before any S1 safety pre-assessment)
- Mechanism of action data via DrugBank API
- Confirmation of nicotine's original approved indication(s), since none are currently on file

**For reference:** among nicotine's other TxGNN-predicted indications in this same evidence pack, **migraine disorder** (rank 4, L3/S1, "Research Question") and **blepharospasm** (rank 5, L3/S1) have meaningfully stronger evidence bases — including direct pilot clinical studies for blepharospasm (though with negative results) — and may be more productive candidates for further review than exercise-induced malignant hyperthermia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

