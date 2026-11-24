---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
monitor_inn: "Azithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-11-24
description: "Azithromycin: predicted new indication hyperamylasemia (evidence level L5). In Australia: 5 PBS items (5 currently listed)"
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
| Australia Market Status | Listed on the PBS Schedule (5 of 5 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for azithromycin: "Azithromycin is a macrolide antibacterial drug. […] Azithromycin acts by binding to the 23S rRNA of the 50S ribosomal subunit of susceptible microorganisms inhibiting bacterial protein synthesis and impeding the assembly of the 50S ribosomal subunit." ([DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a), label version 2026-09-09; accessed 2026-11-19.) Azithromycin is a macrolide antibiotic, a class that generally acts by inhibiting the bacterial 50S ribosomal subunit.

Hyperamylasemia is a laboratory finding with many possible causes (pancreatic, salivary and renal), not a disease with a defined drug target. No identifiable mechanistic link between a macrolide antibiotic and this finding was found. The high TxGNN score should be treated as a model-generated signal only, with no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4115N | Zithromax | Azithromycin | Tablet 500 mg (as dihydrate) | Valid |
| 5616N | Zithromax | Azithromycin | Tablet 600 mg (as dihydrate) | Valid |
| 6221K | Zithromax | Azithromycin | Tablet 600 mg (as dihydrate) | Valid |
| 8201P | Zithromax | Azithromycin | Powder for oral suspension 200 mg (as dihydrate) per 5 mL, 15 mL | Valid |
| 8336R | Zithromax | Azithromycin | Tablet 500 mg (as dihydrate) | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

