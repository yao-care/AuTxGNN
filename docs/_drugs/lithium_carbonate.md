---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Mood Stabilisation to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate (DrugBank DB14509) is pharmacologically known for its mood-stabilising effects via GSK3β/IMPase inhibition, though this evidence pack contains no formal record of its original approved indication. The TxGNN model's top prediction is **Pseudoachondroplasia**, a rare skeletal dysplasia, but this is supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (`original_indications` empty). Lithium is pharmacologically known for mood stabilisation, referenced only indirectly in the model's own rationale text. |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lithium carbonate is not available in this evidence pack (flagged as a High-severity data gap). Based on the rationale supplied alongside the prediction, lithium is pharmacologically known to inhibit glycogen synthase kinase-3β (GSK3β) and inositol monophosphatase (IMPase), pathways linked to its established mood-stabilising effects.

Pseudoachondroplasia is caused by *COMP* gene mutations that lead to misfolded protein accumulation in the chondrocyte endoplasmic reticulum and subsequent chondrocyte apoptosis. The proposed link is that GSK3β inhibition activates Wnt/β-catenin signalling and autophagy, which in theory could influence chondrocyte survival.

However, this link is explicitly flagged as speculative even in the source rationale: there is no direct molecular or animal-model evidence that lithium affects clearance of misfolded COMP protein. The evidence pack itself notes the high TxGNN score more likely reflects the sparsity of connections around this rare-disease node in the knowledge graph (an embedding-level similarity) rather than a genuine pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

TFDA/PI warnings and contraindications for lithium carbonate could not be retrieved for this evidence pack — this is flagged as a **Blocking** data gap, meaning the safety profile cannot yet be assessed against the standard S1 safety screening stage. No drug interaction data was found (DDI query status: not found). Because the drug is not currently marketed in Australia (0 ARTG entries), no local Product Information exists to reference; safety data would need to be sourced from an approved overseas formulation before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials, literature, or mechanistic evidence specific to pseudoachondroplasia — and the source rationale itself cautions this is likely an artefact of sparse knowledge-graph connections around a rare-disease node rather than a real pharmacological signal. A Blocking safety data gap also prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/PI-sourced warnings, contraindications, and interaction data for lithium carbonate (currently Blocking)
- Confirmed mechanism-of-action data from DrugBank or primary literature
- Preclinical evidence (e.g., in vitro chondrocyte/COMP misfolding models) testing whether GSK3β inhibition affects pseudoachondroplasia-relevant pathology
- Given the complete absence of trial/literature evidence for this specific indication, this candidate is a poor use of limited review resources compared to alternatives in the same prediction set — notably rank 9 (WHIM syndrome, L4/S1, "Research Question"), which has a documented clinical basis (lithium's known leukocytosis effect) and may warrant separate evaluation instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

