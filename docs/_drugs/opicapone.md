---
layout: default
title: Opicapone
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Opicapone
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

# Opicapone: From COMT Inhibition (Parkinson's Disease) to Rasmussen Subacute Encephalitis (Preliminary Model Prediction)

## One-Sentence Summary

Opicapone is a peripheral COMT (catechol-O-methyltransferase) inhibitor; internationally it is used as an add-on to levodopa in Parkinson's disease, though it is not currently marketed in Australia and formal indication data is unavailable in this evidence pack.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the connection as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed by local regulatory data (drug not marketed in Australia); internationally used as adjunct to levodopa in Parkinson's disease |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for opicapone is not available in this evidence pack. Based on what is known, opicapone is a peripheral COMT inhibitor belonging to the same pharmacological class used as adjunct therapy to levodopa in Parkinson's disease — this class use is referenced in the evidence pack's own rationale notes but has not been verified against Australian TGA-approved Product Information, since opicapone is not currently registered here.

Rasmussen subacute encephalitis is a paediatric autoimmune epilepsy syndrome driven by T-cell-mediated cortical inflammation. The evidence pack's mechanistic assessment for this candidate explicitly states there is no known pharmacological relationship between COMT/dopamine metabolism and this disease's underlying pathology, and suggests the high TxGNN score likely reflects indirect connectivity among neurological nodes in the knowledge graph rather than genuine pharmacological plausibility.

For context, of the 10 candidates generated for opicapone, only the rank-4 candidate ("Hunt's juvenile paralysis agitans," an early-onset Parkinsonism) shows a direct mechanistic overlap with opicapone's established pharmacology. The rank-1 candidate discussed in this report has the highest model score but the weakest mechanistic rationale among the top 10, and should be treated as a model-generated hypothesis requiring independent validation rather than a plausibility-ranked lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) is available in this evidence pack. Opicapone does not currently have TGA-approved Australian Product Information, as it is not marketed in Australia — safety information should be sourced from overseas regulatory documentation (e.g. EMA/FDA product information) pending local registration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero supporting clinical trials or literature (L5, model-only evidence), and the mechanistic rationale is explicitly assessed as weak/likely graph noise in the evidence pack itself. Combined with the drug's unregistered status in Australia and a blocking safety data gap, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TGA-equivalent Product Information / safety and contraindication data (blocking gap DG001)
- Confirmed mechanism of action data for opicapone (DG002)
- Independent preclinical or mechanistic evidence linking COMT inhibition to Rasmussen encephalitis pathology
- Consider re-scoping evaluation toward the rank-4 candidate (Hunt's juvenile Parkinsonism), which has stronger mechanistic overlap with opicapone's known pharmacology, though it is likewise currently unsupported by clinical or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

