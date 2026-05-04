---
layout: default
title: Dornase Alfa
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase Alfa: From Cystic Fibrosis to Ovarian Melanoma

## One-Sentence Summary

Dornase alfa is a recombinant human DNase I enzyme approved internationally for cystic fibrosis (CF), where it reduces airway mucus viscosity by degrading extracellular DNA.
The TxGNN model places **Ovarian Melanoma** as its top predicted new indication; however, the prediction score sits precisely at the minimum threshold of **50.00%** (rank 1,128,519 of all drug–disease pairs), indicating the model found no meaningful discriminative signal for this drug.
Currently **no clinical trials** and **no publications** directly support this predicted direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cystic fibrosis-associated lung disease |
| Predicted New Indication | Ovarian Melanoma |
| TxGNN Prediction Score | 50.00% *(at minimum prediction threshold — no meaningful signal)* |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established clinical knowledge, Dornase alfa is a recombinant human deoxyribonuclease I (rhDNase) that selectively cleaves extracellular DNA (eDNA). In cystic fibrosis, neutrophil-derived eDNA accumulates in airway secretions and forms a dense scaffold that dramatically increases sputum viscosity; by degrading this scaffold, dornase alfa reduces mucus viscosity, improves mucociliary clearance, and lowers the risk of pulmonary exacerbations. This mechanism is highly specific to conditions characterised by pathological eDNA accumulation.

Ovarian melanoma is an exceptionally rare tumour entity — so rare that it may represent a disease classification artefact or noise in the knowledge graph rather than a well-defined clinical condition. While there is emerging preclinical interest in the role of neutrophil extracellular traps (NETs) and eDNA within tumour microenvironments as potential mediators of immune evasion, this remains highly speculative. No mechanistic evidence, preclinical data, or clinical signal connects dornase alfa's DNase activity to ovarian melanoma in particular.

Critically, the TxGNN score of 0.5 represents the model's minimum prediction threshold, and the rank of 1,128,519 places this prediction at the extreme low-confidence end of all possible drug–disease pairs. This should be treated as predictive noise rather than a genuine repurposing candidate, and no further investigation is recommended on this specific indication without a compelling new biological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for ovarian melanoma.

---

## Australia Market Information

Dornase alfa currently has **no ARTG registration** and is not commercially available in Australia as of the data cut-off (4 April 2026).

> **Note for clinicians:** Dornase alfa (Pulmozyme®, Roche) is approved in the United States (FDA, 1993) and the European Union (EMA) for the management of cystic fibrosis in patients aged 5 years and older. Healthcare professionals in Australia wishing to access this product would need to apply through the TGA's **Special Access Scheme (SAS Category B)** or seek **Authorised Prescriber** status. The FDA and EMA prescribing information should be used as reference documents in the absence of a TGA-approved Australian PI.

---

## Safety Considerations

As dornase alfa is not registered in Australia, no TGA-approved Product Information (PI) is available. Please refer to the **FDA-approved US prescribing information** or **EMA Summary of Product Characteristics (SmPC)** for full safety, contraindication, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score of 50.00% at rank 1,128,519 represents the absolute minimum confidence level in the TxGNN model — there is no meaningful predictive signal linking dornase alfa to ovarian melanoma. Combined with the absence of any supporting clinical or preclinical literature, and the questionable status of "ovarian melanoma" as a well-defined disease entity in the knowledge graph, this candidate does not meet the threshold for further evaluation at this time.

**Broader context from this prediction set:**
Of the 10 top-ranked predictions returned for this drug, all share the same minimum score (0.5) and similar high rank numbers, suggesting the TxGNN model has difficulty generating high-confidence novel predictions for dornase alfa beyond its established indication. The most biologically plausible candidate in this set is **Ethmoid Sinusitis (rank 3)**, where dornase alfa's mucolytic mechanism has a credible mechanistic rationale in CF-associated chronic rhinosinusitis, supported by one indirect review publication ([PMID 27393775](https://pubmed.ncbi.nlm.nih.gov/27393775/)). This direction warrants a separate focused evidence review.

**To proceed with any further evaluation, the following would be needed:**

- Confirmation that "ovarian melanoma" is a well-characterised, clinically recognised disease entity (not a knowledge graph artefact)
- Preclinical evidence establishing a biological link between the eDNA/DNase pathway and ovarian melanoma pathophysiology
- A coherent mechanistic hypothesis grounded in published tumour biology or immunology literature
- TGA Special Access Scheme approval and a treating specialist willing to act as Authorised Prescriber, should clinical use ever be contemplated
- Full safety and drug interaction review against a validated prescribing information document (FDA or EMA)

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application. This report reflects data available as of 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

