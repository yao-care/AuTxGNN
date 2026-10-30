---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 177
evidence_level: L5
indication_count: 3
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-10-30
description: "Clotrimazole: predicted new indication acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Clotrimazole: azole antifungal (CYP51 inhibitor) → acne (disease)
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is a topical azole antifungal that is marketed in Australia. The TxGNN model predicts it may be useful for **acne (disease)**. Evidence is very thin: **1 clinical trial** (a suspended combination-product study with no results) and **no publications** directly address this use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acne (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Clotrimazole belongs to the azole antifungal class. These drugs inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis and disrupts fungal membrane integrity. Clotrimazole is also reported to have some antibacterial and anti-inflammatory activity.

Malassezia yeasts and *Cutibacterium acnes* may contribute to acne-like lesions, so a topical antimicrobial effect is plausible. This link is speculative. The only trial is a fixed-dose combination of beclomethasone, gentamicin and clotrimazole. Clotrimazole's contribution cannot be separated from the corticosteroid and antibiotic components. The model score therefore reflects network-level similarity, not demonstrated efficacy in acne.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a topical combination cream (beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1%) in contaminated dermatosis with bilateral symmetrical lesions. No results are available. Clotrimazole's individual effect cannot be isolated, so this is indirect evidence only. |

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4004R | Pharmacy Action Anti-Fungal Cream | Cream 10 mg per g, 20 g | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: The interaction database lists 100 interacting drugs. Examples of those graded **Major** are fentanyl, alfentanil, hydrocodone and amiodarone. Many others are graded Moderate, including paclitaxel, abemaciclib, acalabrutinib, nifedipine, amlodipine, apixaban, alprazolam, estradiol, levonorgestrel and norethisterone. Some are Minor, including dolutegravir and amphotericin B. These grades come from a general interaction database and mainly reflect systemic exposure. Their relevance to a topical cream is likely lower and should be checked against the Product Information.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as none were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only related trial is a suspended study of a three-drug combination with no reported results. No publications support clotrimazole in acne. The prediction therefore rests on the model score alone and the evidence level is L5.

**To proceed, the following is needed:**
- Controlled studies of clotrimazole alone in acne, or a trial design that separates its effect from corticosteroid and antibiotic components
- Detailed mechanism of action data and a rationale for the antimicrobial or anti-inflammatory role in acne
- Warnings and contraindications from the TGA-approved Product Information
- A review of interaction relevance for topical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

