---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-17
description: "Amoxicillin: predicted new indication polyclonal hyperviscosity syndrome (evidence level L5). In Australia: at least 20 PBS items"
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Amoxicillin: beta-lactam antibiotic (inhibits bacterial cell wall synthesis) → polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic that acts against susceptible bacteria. The TxGNN model predicts it may be relevant to **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** in the data compiled for this report support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for amoxicillin: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), label version 2026-11-13; accessed 2026-11-19.) Amoxicillin belongs to the beta-lactam class of antibiotics, which inhibit bacterial cell wall synthesis.

Polyclonal hyperviscosity syndrome is driven by excess immunoglobulins in the blood and has no antibacterial target. No plausible mechanistic link between amoxicillin and this condition was identified. The high score is a model prediction only and is not supported by any trial or publication. At this stage the prediction should be regarded as unsubstantiated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11947T | AMILOXYN | Capsule 500 mg (as trihydrate) | Not recorded in the local data |

## Safety Considerations

Contraindications and key warnings text was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for label safety information.

**Drug Interactions** (100 interacting drugs were recorded; selected examples):
- **Major:** Methotrexate; live cholera vaccine (Vibrio cholerae CVD 103-HgR strain)
- **Moderate:** Doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, mycophenolate mofetil, entecavir, balsalazide
- **Minor:** Allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no supporting trials or publications and no plausible mechanistic link between a beta-lactam antibiotic and a condition of immunoglobulin-driven hyperviscosity.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking amoxicillin to polyclonal hyperviscosity syndrome
- Any preclinical or clinical data directly studying this disease
- Product Information (PI) review for warnings and contraindications
- Detailed mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

