---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Mesalazine"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
description: "Mesalazine: predicted new indication Congenital hypotrichosis with juvenile macular dystrophy (evidence level L5). In Australia: at least 20 PBS items"
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Mesalazine: Congenital hypotrichosis with juvenile macular dystrophy
{: .text-alpha }

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) was originally used to treat ulcerative colitis and other inflammatory bowel conditions.
The TxGNN model predicts it may be effective for **congenital hypotrichosis with juvenile macular dystrophy**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so the evidence rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mesalazine: "The mechanism of action of mesalamine is not fully understood, but it appears to have a topical anti-inflammatory effect on the colonic epithelial cells. Mucosal production of arachidonic acid metabolites, both through the cyclooxygenase and lipoxygenase pathways, is increased in patients with ulcerative colitis, and it is possible that mesalamine diminishes inflammation by blocking cyclooxygenase and inhibiting prostaglandin production in the colon." ([DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7), label version 2026-10-26; accessed 2026-11-19.) Based on known information, mesalazine is an aminosalicylate anti-inflammatory agent, its efficacy in ulcerative colitis is established, but a mechanistic link to the predicted indication has not been identified.

Congenital hypotrichosis with juvenile macular dystrophy is an ultra-rare hereditary disorder caused by CDH3 mutation. No inflammatory pathway that mesalazine could plausibly modulate has been identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the ranked list were also reviewed. Rheumatoid arthritis (indirect evidence via sulfasalazine, which is metabolised to mesalazine) and osteoarthritis (a loose anti-inflammatory rationale) have somewhat more plausible rationales. Both are still at the "Hold" stage and do not alter the decision for the lead prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 10254Q | Pentasa | Mesalazine | Sachet containing prolonged release granules, 4 g per sachet | Valid |
| 10257W | Salofalk | Mesalazine | Sachet containing granules, 3 g per sachet | Valid |
| 11210B | Asacol | Mesalazine | Tablet 800 mg (enteric coated) | Valid |
| 11554D | Salofalk | Mesalazine | Tablet 1 g (enteric coated) | Valid |
| 12198B | Pentasa | Mesalazine | Suppository 1 g | Valid |
| 12203G | Pentasa | Mesalazine | Sachet containing prolonged release granules, 1 g per sachet | Valid |
| 12463Y | Asacol | Mesalazine | Tablet 1.6 g (enteric coated) | Valid |
| 13247F | MESALZ | Mesalazine | Tablet 1.2 g (prolonged release) | Valid |
| 13355X | Pentasa | Mesalazine | Sachet containing prolonged release granules, 1 g per sachet | Valid |
| 13356Y | MESALZ | Mesalazine | Tablet 1.2 g (prolonged release) | Valid |
| 13361F | Salofalk | Mesalazine | Sachet containing granules, 500 mg per sachet | Valid |
| 13362G | Salofalk | Mesalazine | Tablet 500 mg (enteric coated) | Valid |
| 13394Y | Salofalk | Mesalazine | Tablet 1 g (enteric coated) | Valid |
| 13395B | Asacol | Mesalazine | Tablet 1.6 g (enteric coated) | Valid |
| 13396C | Pentasa | Mesalazine | Tablet 500 mg (prolonged release) | Valid |
| 13397D | Pentasa | Mesalazine | Sachet containing prolonged release granules, 2 g per sachet | Valid |
| 13398E | Salofalk | Mesalazine | Sachet containing granules, 1 g per sachet | Valid |
| 13422K | Asacol | Mesalazine | Tablet 800 mg (enteric coated) | Valid |
| 13423L | Mesasal | Mesalazine | Tablet 250 mg (enteric coated) | Valid |
| 13456F | Pentasa | Mesalazine | Sachet containing prolonged release granules, 4 g per sachet | Valid |

The table shows 20 of 44 PBS items for this ingredient in these data (items on the current PBS Schedule first).

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph-derived associations, not product label text): kidney disease, pyoureter, liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pyloric stenosis, lipoid nephrosis and interstitial nephritis.
- **Drug Interactions**: 100 interactions were identified. Those listed include:
  - **Major**: cidofovir; human botulinum neurotoxin A/B immune globulin.
  - **Moderate** (examples): NSAIDs (ketorolac, ibuprofen, celecoxib, bromfenac), azathioprine, aminoglycosides (amikacin), amphotericin B formulations, acyclovir, cisplatin, bacitracin, capreomycin, and sulfonylureas (acetohexamide, chlorpropamide).
  - Many of these relate to additive nephrotoxicity, so renal function monitoring is relevant.

For full safety information, including warnings, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and no plausible mechanistic link to this ultra-rare genetic disorder. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data showing that mesalazine can act on CDH3-related pathology
- Preclinical evidence (for example, in vitro or animal models) in the predicted condition
- Mechanism of action data for mesalazine
- Approved indication text and PI warnings and contraindications for the Australian product
- Consideration of better-supported candidates from the ranked list, such as rheumatoid arthritis or osteoarthritis, which still lack direct mesalazine evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

