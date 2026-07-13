---
layout: default
title: Carbamide Peroxide
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Carbamide Peroxide
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

# Carbamide Peroxide: From Cerumen Removal to Sinusitis

## One-Sentence Summary

Carbamide peroxide is a topical oxygen-releasing compound, best known as an OTC earwax (cerumen) softening agent and dental bleaching ingredient. The TxGNN model predicts it may be effective for **Sinusitis** with a prediction score of **94.21%**; however, there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cerumen (earwax) removal; dental bleaching (OTC use) |
| Predicted New Indication | Sinusitis |
| TxGNN Prediction Score | 94.21% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on established pharmacology, carbamide peroxide (urea hydrogen peroxide) is an adduct of hydrogen peroxide (H₂O₂) and urea. On contact with body fluids, it decomposes to release nascent oxygen and free H₂O₂, providing local antimicrobial activity and effervescent mechanical cleansing. The urea component additionally acts as a mucolytic, softening protein-rich debris and viscous secretions. These properties underpin its approved OTC uses for earwax removal and oral antisepsis.

The mechanistic rationale for sinusitis is biologically plausible at a theoretical level: if delivered via nasal irrigation, H₂O₂ could contact the sinus mucosa and exert broad-spectrum bactericidal activity against common sinusitis pathogens, while urea may help solubilise thickened mucus and promote drainage. Of the ten predictions in this Evidence Pack, the sinusitis cluster (ranks 1, 4, 5) represents the group with the strongest mechanistic connection to carbamide peroxide's known properties. Notably, rank 10 (infectious otitis media) shares the highest plausibility because the drug already has FDA-approved use in the external ear canal — the same anatomical neighbourhood.

However, the mechanistic link remains entirely unvalidated. No in vitro, animal, or clinical studies have examined carbamide peroxide for sinusitis. The TxGNN model most likely identified a generalised "antimicrobial activity" node in the knowledge graph rather than indication-specific evidence. Several other predictions in this pack (paratyphoid fever, relapsing fever, meningococcal infection) involve systemic infections where a topical, non-absorbable local agent has no pharmacological reach, suggesting significant noise in the model output for this drug. Clinical investment should not proceed without first establishing basic preclinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Carbamide peroxide is **not registered** with the Therapeutic Goods Administration (TGA) and has no entries in the Australian Register of Therapeutic Goods (ARTG). Any clinical research or therapeutic use pathway in Australia would require a TGA application from the outset.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Local safety data and contraindications were not retrievable in the current Evidence Pack (Data Gap DG001 — Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Carbamide peroxide has no Australian regulatory presence and the highest-ranked predicted indication (sinusitis) is supported by model prediction alone (Evidence Level L5), with no clinical trials, no relevant publications, no established sinus delivery formulation, and absent safety data — making any research commitment premature.

**To proceed, the following is needed:**
- Resolve Data Gap DG001 (Blocking): Obtain and review full Product Information for warnings, contraindications, and concentration safety thresholds
- Resolve Data Gap DG002 (High): Retrieve complete MOA data from DrugBank to support mechanistic rationale documentation
- Commission preclinical in vitro studies to establish bactericidal activity of carbamide peroxide against primary sinusitis pathogens (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*) at nasal-safe concentrations
- Conduct a focused literature review on H₂O₂-based nasal irrigation (not restricted to carbamide peroxide formulations) to assess translational precedent
- Assess formulation feasibility: appropriate concentration, pH, and tolerability for nasal/sinus irrigation use
- If preclinical data is supportive, evaluate TGA registration pathway requirements before any first-in-human study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

