---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
monitor_inn: "Azithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-10-30
description: "Azithromycin: predicted new indication hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Azithromycin
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

## Azithromycin: macrolide antibiotic (50S ribosomal inhibitor) → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Azithromycin is a macrolide antibiotic that is marketed in Australia as an oral tablet.
The TxGNN model predicts it may be associated with **hyperamylasemia**, but **no clinical trials and no publications** were found for this prediction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Azithromycin is a macrolide antibiotic, a class that generally acts by inhibiting the bacterial 50S ribosomal subunit.

Hyperamylasemia is a laboratory finding with many possible causes (pancreatic, salivary and renal), not a disease with a defined drug target. No identifiable mechanistic link between a macrolide antibiotic and this finding was found. The high TxGNN score should be treated as a model-generated signal only, with no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4115N | Zithromax | Tablet 500 mg (as dihydrate) | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in total. Examples from the listed entries:
  - **Major**: cisapride, dolasetron
  - **Moderate**: famotidine, loperamide, clarithromycin, levofloxacin, granisetron, aluminium hydroxide, magnesium hydroxide, several laxatives
  - **Minor**: amoxicillin, metronidazole

Further safety information should be taken from the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications and no plausible mechanistic link. Hyperamylasemia is a laboratory finding rather than a treatable disease, so the evidence level is L5.

**To proceed, the following is needed:**
- A clear clinical definition of the target condition (the cause of the raised amylase) and a biologically plausible mechanism
- Mechanism of action data for azithromycin
- Studies that directly examine azithromycin in this condition
- Warnings and contraindications from the TGA-approved PI, with a review of the major interactions (cisapride, dolasetron)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

