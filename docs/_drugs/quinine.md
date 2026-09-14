---
layout: default
title: Quinine
parent: 僅模型預測 (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
---

# Quinine
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

# Quinine: From Malaria to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Quinine is a long-established antimalarial agent (haemozoin/haematin polymerisation inhibitor with Na⁺/Ca²⁺ channel–modulating activity); structured original-indication and MOA fields are not on file for this evidence pack, but this pharmacology is described in the prediction rationale itself. The TxGNN model's top-ranked prediction is **Smouldering Systemic Mastocytosis** (score 96.90%), but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment flags it as likely model noise rather than a genuine signal — quinine's best-known interaction with the immune/haematological system (drug-dependent antibody–mediated thrombocytopenia) runs counter to, not in support of, a therapeutic role in a mast-cell proliferative disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (antimalarial) — inferred from rationale text; no structured `original_indications`/TGA licence data on file |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 96.90% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form for this pack (`original_moa`: Data Gap). Based on the rationale text supplied with the prediction, quinine's known pharmacology is antimalarial — inhibition of haem/haematin polymerisation in *Plasmodium* — together with non-specific Na⁺/Ca²⁺ channel modulation. Smouldering systemic mastocytosis, by contrast, is driven by activating **KIT** mutations causing clonal mast-cell proliferation.

There is no known overlap between quinine's mechanism and the KIT signalling pathway, and the evidence pack explicitly notes that quinine is better known clinically for **inducing** immune-mediated thrombocytopenia and other drug-dependent antibody reactions — an adverse, pro-inflammatory association rather than a therapeutic one in mast-cell disease. The assessment concludes this ranking most likely reflects embedding-space proximity noise in the knowledge graph rather than a real pharmacological signal, and this is corroborated by the complete absence of any supporting trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries are currently on file for quinine in this evidence pack (market status: Not marketed; 0 total licences).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this evidence pack; a DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no supporting clinical trial or literature evidence (Evidence Level L5), and the mechanistic rationale itself argues against biological plausibility — quinine's principal known interaction with immune/haematological pathways is adverse (drug-induced thrombocytopenia), not therapeutic. Proceeding to any safety-relevant evaluation stage (S1+) is not currently supportable.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Structured mechanism-of-action data from DrugBank — currently a High-severity data gap (DG002)
- Quinine-specific (not disease-background) preclinical or clinical evidence directly addressing KIT-driven mast-cell pathology, should this candidate be pursued further

**Note on other candidates in this pack:** all 10 TxGNN-ranked predictions for quinine resulted in a Hold recommendation. The strongest evidence level reached was **L4** (rank 6, polycystic kidney/liver disease), based on an indirect ion-channel mechanistic argument (quinine's non-specific blockade of polycystin-2/Ca²⁺-activated Cl⁻ currents), but the associated literature consists of general ADPKD/PLD reviews and guidelines rather than quinine-specific studies, and should not be read as direct drug evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

