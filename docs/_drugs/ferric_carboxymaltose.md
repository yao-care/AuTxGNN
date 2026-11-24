---
layout: default
title: Ferric Carboxymaltose
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Ferric carboxymaltose"
predicted_indications: ["bronchitis"]
description: "Ferric Carboxymaltose: predicted new indication Bronchitis (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Ferric Carboxymaltose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ferric Carboxymaltose: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement product, marketed in Australia as Ferinject.
The TxGNN model predicts it may be effective for **bronchitis** (the top-ranked prediction), but there are **no registered clinical trials** and **no publications** supporting this direction.
The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9900 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ferric carboxymaltose: "Ferric carboxymaltose is a colloidal iron (III) hydroxide in complex with carboxymaltose, a carbohydrate polymer that releases iron." ([DailyMed: ferric carboxymaltose prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8e8e95f4-8d3a-4658-9f6c-09edf2210341), label version 2026-09-16; accessed 2026-11-19.) Based on known information, ferric carboxymaltose is an intravenous iron replacement product. Its role is to correct iron deficiency and iron deficiency anaemia.

No mechanistic link to bronchitis was identified. The drug has no known anti-infective or airway anti-inflammatory activity. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not supported by trials or literature.

Other top-ranked predictions were also reviewed. Most have no plausible therapeutic link either:

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for bronchitis.

For context, literature was retrieved for other predicted indications, none of which supports a repurposing claim:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36282723](https://pubmed.ncbi.nlm.nih.gov/36282723/) | 2023 | Review | Eur Heart J | Iron deficiency is common in cardiovascular disease (thrombotic disease prediction) |
| [41912474](https://pubmed.ncbi.nlm.nih.gov/41912474/) | 2026 | Cohort | Renal Failure | In 41 non-dialysis CKD patients with iron deficiency, IV ferric carboxymaltose was examined for effects on platelet counts and transferrin, with potential thrombogenicity implications |
| [32079699](https://pubmed.ncbi.nlm.nih.gov/32079699/) | 2021 | Preclinical (rat) | Haematologica | Iron deficiency-induced thrombocytosis increased thrombotic tendency; ferric carboxymaltose was used to reverse deficiency |
| [31855154](https://pubmed.ncbi.nlm.nih.gov/31855154/) | 2020 | Cohort | Blood Transfus | IV ferric carboxymaltose was effective and safe for iron deficiency anaemia in inflammatory rheumatic diseases |
| [42785516](https://pubmed.ncbi.nlm.nih.gov/42785516/) | 2026 | Cohort/Review | J Pediatr | Compared effectiveness and safety of IV iron formulations in children with iron deficiency |
| [39304237](https://pubmed.ncbi.nlm.nih.gov/39304237/) | 2024 | RCT | Lancet Glob Health | IV ferric carboxymaltose vs oral ferrous sulphate for anaemia in pregnancy in Nigeria (not relevant to the predicted indications) |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 10104T | Ferinject | Ferric carboxymaltose | Injection 500 mg (iron) in 10 mL | Valid |
| 11702X | Ferinject | Ferric carboxymaltose | Injection 1000 mg (iron) in 20 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions** (5 recorded in the interaction database):
  - **Major:** Dimercaprol
  - **Moderate:** Iron, ferrous fumarate, ferrous gluconate, chloramphenicol
- **Bone-related signal:** Ferric carboxymaltose can cause hypophosphatemia and, with prolonged use, osteomalacia.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction of bronchitis has no clinical trials, no literature and no plausible mechanism, so it rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence (Evidence Level L5).

**To proceed, the following is needed:**
- Mechanism of action data
- Approved indication text and PI warnings and contraindications for the Australian entry
- A plausible mechanistic or clinical rationale for any predicted indication, followed by registered trials or controlled studies
- Route compatibility and similarity-to-original-indication assessments

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ferric carboxymaltose prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8e8e95f4-8d3a-4658-9f6c-09edf2210341) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

