---
layout: default
title: Midostaurin
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
---

# Midostaurin
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

# Midostaurin: From FLT3-Mutated AML/Systemic Mastocytosis to Familial Thrombocytosis

*Note: The evidence pack contains no Australian regulatory record for midostaurin's original indication (ARTG entries = 0, market status = Not marketed). The original indication above is well-established public pharmacological information (Rydapt®, approved overseas for FLT3-mutated AML and aggressive systemic mastocytosis) and is **not** sourced from this Evidence Pack — flagged here for transparency rather than fabricated as pack data.*

## One-Sentence Summary

Midostaurin is a multikinase inhibitor (FLT3/KIT/PDGFR/VEGFR2/PKC) originally developed for FLT3-mutated acute myeloid leukaemia and systemic mastocytosis. The TxGNN model predicts it may be effective for **Familial Thrombocytosis**, but this prediction currently has **no supporting clinical trials and no supporting literature**, and the pack's own mechanistic review states the pathway driving familial thrombocytosis (MPL/THPO germline mutations) does not overlap with midostaurin's known targets.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack (drug not ARTG-registered in Australia) |
| Predicted New Indication | Familial Thrombocytosis |
| TxGNN Prediction Score | 98.92% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured MOA data is not available from DrugBank in this Evidence Pack (flagged as a High-severity data gap). However, literature captured elsewhere in this pack (PMID 16969355) independently describes midostaurin (PKC412A) as a multikinase inhibitor that potently inhibits protein kinase C alpha (PKCα), VEGFR2, KIT, PDGFR and FLT3 tyrosine kinases.

Familial thrombocytosis is a hereditary platelet disorder driven almost exclusively by germline mutations in *MPL* (thrombopoietin receptor) or *THPO* (thrombopoietin) — pathways that constitutively activate JAK-STAT signalling. This is a distinct mechanism from the FLT3/KIT/PKC axis that midostaurin targets.

The evidence pack's own repurposing rationale for this candidate is explicit on this point: the disease's causative pathway does not involve FLT3/KIT/PKC, so there is no direct mechanistic link to midostaurin's known pharmacology. The high TxGNN score most likely reflects node proximity within the knowledge graph (e.g. shared association with platelet/myeloid biology broadly) rather than a genuine, validated biological connection. This is consistent with the L5 evidence tier (model prediction only, no supporting studies) and the "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

No ARTG entries — midostaurin is not currently marketed in Australia according to this Evidence Pack.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this candidate has zero clinical trial or literature support, and the pack's own mechanistic analysis indicates the target disease pathway (MPL/THPO-driven) does not intersect with midostaurin's known kinase targets (FLT3/KIT/PKC). Evidence is insufficient to justify further evaluation at this time.

**To proceed, the following is needed:**
- Structured DrugBank MOA data (currently a Blocking/High data gap in this pack)
- TFDA/TGA Product Information warnings and contraindications (Blocking gap — required before any S1 safety screening)
- In vitro or preclinical validation of any interaction between midostaurin's targets and the MPL/THPO/JAK-STAT pathway, before this candidate can move beyond model prediction

*For context: among the other candidates in this pack, thrombocythemia (rank 5, evidence level L4, "Research Question") has a somewhat stronger — though still preclinical/indirect — mechanistic basis via FLT3-driven myeloproliferative neoplasm models, and metastatic melanoma (rank 3, L3) already has a negative Phase IIA clinical result. Neither is in scope of this report, which follows the pack's top-ranked candidate (familial thrombocytosis) per protocol.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

