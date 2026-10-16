---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vitamin A: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Vitamin A deficiency (vitamin deficiency disorder). This comes from t…"
---

# Vitamin A
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

# Vitamin A: From Vitamin A Deficiency to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A is a fat-soluble vitamin, originally used to treat and prevent vitamin A deficiency.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials and no publications** were found to support this prediction.
The very high model score is a graph-based signal only, and the biological rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin A deficiency (vitamin deficiency disorder). This comes from the TxGNN knowledge graph, as the Australian licence records compiled for this report contain no indication text. |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, vitamin A is an essential nutrient. Its role in vitamin A deficiency is well established, and it acts through retinoid signalling to support vision, epithelial integrity and immune function.

The link to congenital prothrombin deficiency is not convincing. Prothrombin (factor II) synthesis depends on vitamin K-dependent gamma-carboxylation, and vitamin A has no established role in that pathway. A congenital factor II defect is not expected to respond to vitamin A. The prediction therefore appears to reflect a graph-based association (both conditions sit near vitamin-related nodes) rather than a plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG / Licence Number | Product Name | Dosage Form |
|---------|------|------|
| 14426G | Tearsagain | Eye spray 10 mg per mL, 10 mL |
| 12191P | Renastep | Oral liquid 125 mL, 24 (Renastep) |

Both entries are valid single-ingredient products. Approved indication text was not available in the data compiled for this report.

---

## Safety Considerations

Product Information (PI) warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for label safety information. The following items come from other sources.

- **Knowledge-graph contraindication signals (not label text)**: The graph links vitamin A to caution in the following conditions.
  - Renal and urinary: kidney disease, nephrolithiasis, nephrocalcinosis, primary hyperoxaluria
  - Hepatic and gastrointestinal: liver disease, gallbladder disease, peptic ulcer disease, inflammatory bowel disease
  - Metabolic and mineral: hypercalcaemia, hyperphosphataemia, hypervitaminosis, iron metabolism disorders, Wilson disease
  - Other: sarcoidosis, sickle cell anaemia, haemolytic anaemia, arteriosclerosis obliterans
- **Drug Interactions** (68 interactions found; main ones shown):
  - **Major**:
    - Retinoids: isotretinoin, acitretin, tretinoin
    - Tetracyclines: doxycycline, minocycline, tetracycline, oxytetracycline, demeclocycline, omadacycline, eravacycline, sarecycline
  - **Moderate**: bexarotene, cholestyramine, colesevelam, colestipol, sevelamer, selpercatinib
  - **Minor**: orlistat

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for congenital prothrombin deficiency has no supporting trials or publications, and it has no plausible mechanism, because prothrombin synthesis depends on vitamin K rather than vitamin A.
- Of the lower-ranked predictions in the same analysis, the most developed evidence is for perinatal disease, specifically bronchopulmonary dysplasia in very low birth weight infants. That evidence is supported by repeated Cochrane reviews, and it is graded L1 for proceeding with guardrails.
- That evidence is specific to preterm infants, the benefit is modest, and the usual route is intramuscular injection. The Australian products identified here are an eye spray and an oral liquid, so they do not match that use.

**To proceed, the following is needed:**
- Mechanism of action data for vitamin A
- Product Information warnings and contraindications for the Australian products
- A biologically plausible mechanism, followed by preclinical or clinical evidence, if congenital prothrombin deficiency is to be pursued
- A separate evaluation of the neonatal bronchopulmonary dysplasia indication, including route and formulation compatibility with the Australian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

