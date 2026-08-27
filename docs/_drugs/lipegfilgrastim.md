---
layout: default
title: Lipegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Lipegfilgrastim
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

# Lipegfilgrastim: From Chemotherapy-Induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Lipegfilgrastim is a PEGylated granulocyte-colony stimulating factor (G-CSF) analogue, generally used to reduce the duration of chemotherapy-induced neutropenia — this original-use context is background pharmacological knowledge, since no Australian regulatory (ARTG) record was returned in this evidence pack. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with a prediction score of **99.93%**, but currently **no clinical trials or literature** support this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack — no ARTG licence on file (general background: chemotherapy-induced neutropenia) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (no ARTG entry) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lipegfilgrastim is not available in this evidence pack (data gap DG002), and no original indication is recorded in the supplied regulatory data — the product currently holds no ARTG entry. Based on general pharmacological knowledge, lipegfilgrastim is a PEGylated recombinant human G-CSF analogue, most commonly used to stimulate neutrophil production and shorten the duration of chemotherapy-induced neutropenia.

The TxGNN model's top prediction, "primary release disorder of platelets", sits alongside several related predictions further down the ranked list (pseudo-von Willebrand disease, Glanzmann thrombasthenia, hemorrhagic disorder due to constitutional thrombocytopenia, thrombocytopenia due to immune destruction, Scott syndrome) — together suggesting the model has picked up a platelet-production/function theme. This is mechanistically plausible in a loose sense, since G-CSF-class growth factors act on shared bone-marrow progenitor pathways that also influence megakaryocyte and platelet lineages, but a direct pharmacological link to platelet-release disorders is not established for this drug's approved use.

Because both the original-indication and MOA fields are flagged as data gaps in this evidence pack, and no clinical trial or literature evidence exists for this specific predicted indication, the rationale above should be treated as a model-generated hypothesis rather than a confirmed pharmacological pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries are currently registered for this product in Australia.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no supporting clinical trial or literature evidence, and both the drug's mechanism of action and its original indication are unverified in this evidence pack. The product also has no current ARTG registration in Australia, and safety data (warnings, contraindications, DDI) could not be sourced — this is flagged as a **Blocking** gap (DG001) that prevents any initial safety assessment.

**To proceed, the following is needed:**
- TFDA/TGA-sourced Product Information (warnings and contraindications) — DG001
- Confirmed mechanism of action data from DrugBank — DG002
- Drug-drug interaction data (current query returned not_found)
- Clinical trial or literature evidence specific to "primary release disorder of platelets" or related platelet-function indications
- Confirmation of the drug's original approved indication(s) and regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

