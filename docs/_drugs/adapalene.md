---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
---

# Adapalene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Adapalene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical retinoid, originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are currently **no registered clinical trials** and **no publications** supporting this direction. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (the approved indication text for the Australian entry is not available; acne is taken from the TxGNN knowledge graph) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Adapalene is a topical retinoid that selectively binds retinoic acid receptors (RAR-beta and RAR-gamma). It modulates keratinocyte differentiation and inflammation, which is the basis for its use in acne. Detailed mechanism of action data was not available in the data compiled for this report.

No established mechanistic link connects adapalene to plasma zinc regulation. No known pathway involves zinc transporters (ZIP/ZnT), metallothionein, or dietary or renal zinc handling. Any connection would be speculative, for example an indirect retinoid-related effect on zinc-binding proteins or transporters.

The high score (0.995) is a graph-based prediction only. Elevated plasma zinc is also more a laboratory finding than a treatable disease, so the indication itself is questionable. Similarity to the original indication and route compatibility have not yet been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13363H | Epiduo | Gel 1 mg-25 mg per g, 30 g (topical) | Not available in the compiled data |

The data compiled for this report lists one valid single-ingredient entry and no cancelled entries. The listed dosage form is topical only.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** Drug-disease contraindication links were found for photoparoxysmal response, photosensitivity disease, exfoliative dermatitis and dermatitis.
- **Drug Interactions:** The interaction query returned 58 potential interactions, with severity levels all listed as "Unknown". Examples include doxycycline, minocycline, tetracycline, metronidazole, prednisone, triamcinolone, budesonide, fluconazole, clopidogrel, bupropion and ibuprofen. Their clinical significance has not been graded.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model support (L5), with no clinical trials or publications. No plausible mechanism links adapalene to plasma zinc, and elevated plasma zinc is a laboratory finding rather than a well-defined disease. Adapalene is also a topical product, so systemic effects on plasma zinc are unlikely.

**To proceed, the following is needed:**
- Confirmation that the indication is clinically meaningful and treatable
- Detailed mechanism of action data and a credible mechanistic hypothesis linking retinoid signalling to zinc handling
- Route compatibility assessment (topical product versus a systemic target)
- Label warnings and contraindications from the TGA-approved PI, as the safety screen cannot proceed without them
- Graded severity for the identified drug interactions
- A targeted literature and trial registry search (including ANZCTR) to confirm there is no supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

