---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist, used internationally for the symptomatic treatment of Benign Prostatic Hyperplasia (BPH), though it is currently not registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may have potential for **Ambras Type Hypertrichosis Universalis Congenita**, a rare genetic hair disorder characterised by excessive whole-body hair growth.
However, **no clinical trials or published literature** currently support this predicted direction, and all ten model-predicted indications are at Evidence Level L5 — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; known internationally for Benign Prostatic Hyperplasia (BPH) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on widely available pharmacological information, Alfuzosin is a selective post-synaptic alpha-1 adrenergic receptor (α1R) antagonist. It relaxes smooth muscle in the prostate and bladder neck, reducing urinary outflow resistance — the basis of its international use in BPH. Hair follicle dermal papilla cells are known to express alpha-adrenergic receptors, which provides the structural basis for the TxGNN knowledge graph to construct a prediction pathway: Drug → α1R blockade → Hair Follicle → Hair Growth modulation.

Ambras Type Hypertrichosis Universalis Congenita, however, is a rare genetic condition primarily associated with chromosomal rearrangements in the 8q24 region near the *TRPS1* gene. This disrupts transcriptional regulation of hair follicle development during embryogenesis. The pathological mechanism is a congenital gene-level developmental defect — not a receptor-mediated or pharmacologically reversible process. There is no preclinical or clinical evidence to support the hypothesis that alpha-1 receptor blockade can reverse the excess hair growth caused by this underlying genetic defect.

The prediction is most likely a false positive arising from high-connectivity hub nodes within the knowledge graph. While the α1R node links broadly to smooth muscle and hair follicle biology, the directionality of the proposed mechanism (α1 blockade reducing hypertrichosis) and the disease phenotype remain entirely unverified. This candidate is not considered biologically plausible at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 3 indication:** A PubMed query for the rank 3 prediction ("malformation syndrome with odontal and/or periodontal component") returned 20 publications. Upon review, all retrieved articles relate to general periodontitis pathophysiology, surgical techniques, and periodontal management — none examine Alfuzosin in this context. These publications are considered non-informative false positive retrievals and are not listed here.

---

## Safety Considerations

Alfuzosin is currently not registered on the Australian Register of Therapeutic Goods (ARTG) and therefore has no TGA-approved Product Information (PI). No drug interaction data was identified in the evidence query. Please refer to the FDA-approved prescribing information (US brand: Uroxatral®) and standard international pharmacological references for safety information pending Australian registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Alfuzosin are at Evidence Level L5, supported solely by knowledge graph model prediction with no clinical trials or human literature specific to any of the predicted conditions. The top-ranked prediction — Ambras Type Hypertrichosis Universalis Congenita — has a mechanistically implausible link given that the condition is driven by a congenital genetic developmental defect that is unlikely to be reversible through alpha-1 adrenergic receptor blockade. Furthermore, Alfuzosin is not currently registered in Australia, limiting any immediate clinical pathway.

**To proceed, the following is needed:**
- Retrieval of Alfuzosin's full mechanism of action and pharmacological profile from DrugBank (DG002 data gap remediation)
- Download and review of international product information (e.g., FDA prescribing information) for comprehensive safety and contraindication assessment (DG001 equivalent)
- Preclinical studies specifically examining the role of alpha-1 adrenergic receptor signalling in hair follicle biology and hypertrichosis models before any repurposing pathway can be considered viable
- Biological plausibility re-assessment across all 10 predicted indications to identify whether any candidate has a stronger mechanistic rationale warranting escalation beyond L5
- Consideration of whether Alfuzosin's well-established international BPH indication warrants exploring an Australian ARTG submission as a prerequisite to any repurposing programme

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application. Healthcare professionals should refer to current TGA guidelines and registered product information for clinical decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

