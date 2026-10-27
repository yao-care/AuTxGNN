---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 87
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Benzoyl Peroxide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Acne"
monitor_inn: "benzoyl peroxide"
predicted_indications: ["vulvar inverted follicular keratosis", "2-hydroxyethyl methacrylate sensitization", "acrodermatitis chronica atrophicans", "acne keloid"]
---

# Benzoyl Peroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Benzoyl Peroxide: From Acne to Vulvar Inverted Follicular Keratosis
{: .text-alpha }

## One-Sentence Summary

Benzoyl peroxide is a topical agent originally used for acne and a range of inflammatory skin conditions, including dermatitis and seborrheic keratosis.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (the approved indication text is not available in the data compiled for this report; the knowledge graph lists acne, atopic dermatitis, contact dermatitis, seborrheic dermatitis, seborrheic keratosis and others) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, benzoyl peroxide is a topical oxidising agent with keratolytic and antimicrobial actions. Its efficacy in acne is established, and it may be mechanistically applicable to follicular and keratinocyte-related skin conditions.

Inverted follicular keratosis is a benign lesion related to seborrheic keratosis, which is one of the drug's original indications in the knowledge graph. This offers a plausible but unverified link through keratinocyte or follicular pathology. However, benzoyl peroxide's keratolytic and antimicrobial actions have no demonstrated relevance to this vulvar lesion. Applying an irritant oxidising agent to vulvar skin or mucosa also raises tolerability concerns.

The high score is a model prediction only and should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the fourth-ranked prediction (acne keloid) has one indirect publication: [39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/) (2024, retrospective chart review, Dermatology Online Journal). It describes acne vulgaris presentation and treatment patterns in 77 Black paediatric patients and does not address acne keloidalis directly.

## Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | 2-hydroxyethyl methacrylate sensitisation | 99.43% | L5 | Likely reflects shared allergen or exposure context. Benzoyl peroxide is a known contact sensitiser, so this is a safety signal rather than an opportunity. |
| 3 | Acrodermatitis chronica atrophicans | 99.17% | L5 | A late Borrelia infection treated with systemic antibiotics. There is no evidence of activity against Borrelia, and topical use would not reach the disease. |
| 4 | Acne keloid | 99.06% | L4 | Related to acne through follicular inflammation. It may help the inflammatory component but would not reverse established fibrotic scarring. Recommendation: Research Question. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13363H | Epiduo | Gel 1 mg-25 mg per g, 30 g (topical) | Not available |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease network edges, not product label text): photosensitivity disease, skin atrophy, exfoliative dermatitis, dermatitis, telangiectasis (including hereditary haemorrhagic telangiectasia), anogenital human papillomavirus infection, common wart, kidney disease, diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency (Addison disease), inflammatory bowel disease (Crohn disease, ulcerative colitis, Crohn's colitis), Clostridium difficile colitis, perinatal necrotising enterocolitis, and peripheral vascular or arterial disease. These should be interpreted with caution, as many appear unrelated to topical use.
- **Contact sensitisation**: benzoyl peroxide is a known contact sensitiser, and irritation is a particular concern on vulvar skin.

No drug interaction data were found. Please refer to the TGA-approved Product Information (PI) for definitive warnings, contraindications and interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for vulvar inverted follicular keratosis is supported only by a model score. There are no clinical trials or publications, the mechanistic link is weak, and irritation risk on vulvar skin is a concern.

**To proceed, the following is needed:**
- Mechanism of action data for benzoyl peroxide
- A literature and case-report search specific to inverted follicular keratosis and its treatment
- The approved indication text and PI safety information (warnings and contraindications) for the ARTG entry
- Assessment of tolerability and sensitisation risk for application to vulvar skin
- Of the other predictions, acne keloid is the only one worth considering as a research question, with a focused review of benzoyl peroxide in inflammatory folliculitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

