---
layout: default
title: Selenium Sulfide
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Selenium Sulfide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Seborrheic dermatitis, pityriasis simplex, seborrheic keratosis…"
---

# Selenium Sulfide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Selenium Sulfide: From Seborrheic Dermatitis to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Selenium sulfide is a topical agent originally used for scalp and skin conditions such as seborrheic dermatitis and pityriasis versicolor.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Seborrheic dermatitis, pityriasis simplex, seborrheic keratosis, pityriasis versicolor (from the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 89.52% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, selenium sulfide is a topical antifungal, keratolytic and antiseborrheic agent. Its efficacy in scalp and skin conditions such as seborrheic dermatitis and pityriasis versicolor is established, and mechanistically it may be applicable to keratinising skin conditions.

A plausible link is its keratolytic and cytostatic action on epidermal keratinocytes, as in its use for seborrheic keratosis. Seborrheic keratosis and inverted follicular keratosis are both benign epidermal keratinising lesions, which may explain the model's prediction.

There are important limits. No trials or literature support this specific indication. The vulvar site also raises mucosal tolerability concerns, because selenium sulfide is intended for external scalp and skin use and can irritate.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Cutaneous candidiasis | 83.86% | L4 | Plausible through antifungal activity against *Malassezia*. Supported only by two narrative reviews. Established azoles and polyenes are likely better options. |
| 3 | Acne keloid | 79.87% | L5 | Indirect link only. No data. |
| 4 | Acrodermatitis chronica atrophicans | 79.63% | L5 | Bacterial (Borrelia) condition. No relevant mechanism. |
| 5 | Neonatal dermatomyositis | 78.70% | L5 | Immune-mediated. Neonatal percutaneous absorption is a concern. |
| 6 | Childhood secondary interstitial lung disease (connective tissue disease) | 77.38% | L5 | No plausible route for a topical agent. Likely a knowledge-graph artefact. |
| 7 | Amyopathic dermatomyositis | 77.10% | L5 | No mechanistic connection. |
| 8 | Hydroa vacciniforme, familial | 74.95% | L5 | No mechanistic connection. |
| 9 | Lichen planus, familial | 69.35% | L5 | Speculative. No immunomodulatory mechanism. |
| 10 | Acne | 65.49% | L5 | Weak rationale through keratolytic and antiseborrheic effects. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (vulvar inverted follicular keratosis).

For the second-ranked prediction, cutaneous candidiasis, two narrative reviews were found. They are not specific to selenium sulfide.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3459338](https://pubmed.ncbi.nlm.nih.gov/3459338/) | 1986 | Review | Acta Derm Venereol Suppl | Discusses treatment of cutaneous *Pityrosporum* and *Candida* infections. Both are opportunistic yeasts, and predisposing factors are key to treatment and recurrence. |
| [7501581](https://pubmed.ncbi.nlm.nih.gov/7501581/) | 1995 | Review | Postgrad Med | Approach to diagnosing and treating superficial fungal infections, including cutaneous candidiasis and tinea versicolor, with topical antifungals. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4452H | Selsun | Shampoo 25 mg per mL (2.5%), 125 mL | Not available in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signal**: dermatitis (from drug-disease contraindication edges, not label text).
- **Drug Interactions**: 79 potential interactions were recorded, all with an unclassified severity level. Examples include pantoprazole, metformin, omeprazole, triamcinolone, prednisone, warfarin, simvastatin and dexamethasone. Their clinical significance is unknown, and they are unlikely to be meaningful for a topical shampoo without a systemic absorption assessment.
- For the vulvar site and for neonatal use, mucosal irritation and percutaneous absorption need specific consideration.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-based only (L5), with no clinical trials or publications for vulvar inverted follicular keratosis. The vulvar mucosal site raises tolerability concerns for a product intended for scalp and skin use. Of the other predictions, only cutaneous candidiasis has any indirect support (L4), and established antifungals are likely better options.

**To proceed, the following is needed:**
- Product Information (PI) warnings and contraindications for the Australian product, which are currently unavailable and block safety screening
- Detailed mechanism of action data
- Approved indication text for the ARTG entry
- Clinical or case-based evidence for inverted follicular keratosis, including histopathological confirmation of the diagnosis
- Assessment of mucosal and vulvar tolerability and of systemic absorption
- If a repurposing direction is pursued, cutaneous candidiasis may be a more tractable research question, requiring comparison against standard topical azoles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

