---
layout: default
title: Dexpanthenol
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dexpanthenol: predicted new indication Anorectal stricture (evidence level L5). Approved use: Not stated in the Australian listing. The knowledge graph lists paral…"
monitor_inn: "Dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "punctate epithelial keratoconjunctivitis", "acute urate nephropathy", "indeterminate colitis", "diversion colitis"]
---

# Dexpanthenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Dexpanthenol: From Gastrointestinal Motility and Skin Conditions to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol is a precursor of pantothenic acid (vitamin B5), used for conditions such as paralytic ileus, gastroparesis, dermatitis and other skin diseases.
The TxGNN model's top prediction is **anorectal stricture**, but this rests on the model alone, with **no clinical trials** and **no publications** supporting it.
The only indication in the data compiled for this report with a clinical trial is **exanthem (rash)**, supported by **1 Phase 3 trial**, though its relevance is only partial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian listing. The knowledge graph lists paralytic ileus, intestinal obstruction, gastroparesis, atopic eczema, dermatitis, actinic keratosis and other skin diseases |
| Predicted New Indication | Anorectal stricture (top-ranked) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predicted indications (ranks 2-10):** imperforate anus (99.71%), anal polyp (99.62%), vulvar inverted follicular keratosis (99.60%), proctitis (99.60%), exanthem (99.60%), punctate epithelial keratoconjunctivitis (99.34%), acute urate nephropathy (98.99%), indeterminate colitis (98.87%) and diversion colitis (98.87%).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, dexpanthenol is converted in the body to pantothenic acid, a precursor of coenzyme A. This supports epithelial repair and wound healing, and mechanistically it may be applicable to conditions involving mucosal or skin damage.

For **anorectal stricture**, a role in mucosal healing is plausible, and dexpanthenol is also used for postoperative ileus, a related gut motility problem. However, no direct evidence supports this link.

Some other predictions are more plausible than others:
- **Proctitis, indeterminate colitis, diversion colitis:** a mucosal repair and anti-inflammatory rationale is conceivable but unproven.
- **Punctate epithelial keratoconjunctivitis:** dexpanthenol eye preparations are used in some regions for corneal healing and dry eye.
- **Imperforate anus, anal polyp, vulvar inverted follicular keratosis, acute urate nephropathy:** the mechanistic link is weak or absent. These scores probably reflect network proximity in the knowledge graph rather than a real biological connection.

---

## Clinical Trial Evidence

The only trial found relates to the exanthem prediction (rank 6). No trials were found for the other predicted indications.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Randomised, double-blind comparison of Bepanthen cream (containing dexpanthenol) versus cetomacrogol cream for preventing papulopustular eruption in patients receiving EGFR inhibitors. Results are not available in the data compiled for this report |

This trial concerns a drug-induced rash rather than exanthem in the strict sense, so its relevance is indirect.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4510J | SebiRinse | Cream 200 g | Not stated |

The only available form is topical (cream). Oral or other formulations would be needed for the gastrointestinal predictions, and route compatibility has not yet been assessed.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** haemophilia.
- **Drug Interactions:** no interactions were found in the data compiled for this report.

Please refer to the TGA-approved Product Information (PI) for full warnings and precautions, as label-based safety data were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions, including the top-ranked anorectal stricture, rest on model scores alone (L5) with no supporting trials or literature. The single Phase 3 trial relates to a different condition (drug-induced rash), and its relevance is only partial. Mechanistic plausibility is reasonable for mucosal and skin conditions (anorectal stricture, proctitis, exanthem) but weak or absent for others.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product (currently missing)
- Detailed mechanism of action data
- Confirmation of the population and outcomes of NCT01136005, and a literature search for the exanthem, proctitis and anorectal stricture predictions
- Assessment of route and formulation compatibility, since only a topical cream is registered in Australia
- Review of the knowledge-graph haemophilia contraindication against the product label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

