---
layout: default
title: Doxycycline
parent: Model Prediction Only (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "Doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
description: "Doxycycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In Australia: at least 20 PBS items"
---

# Doxycycline
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

## Doxycycline: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Doxycycline is a tetracycline antibiotic used for bacterial infections such as bronchitis, bacterial pneumonia, gonorrhoea, anthrax and acne.
The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**, but there are **no registered clinical trials** and only **1 publication** (a 1992 case report), so the evidence is weak and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxycycline: "Doxycycline inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit. Doxycycline has bacteriostatic activity against a broad range of Gram-positive and Gram-negative bacteria." ([DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8), label version 2026-07-09; accessed 2026-11-19.) Based on known information, doxycycline is a broad-spectrum tetracycline antibiotic with proven efficacy in several bacterial infections, including *Chlamydia trachomatis*. Mechanistically it may be applicable to ocular surface disease.

The prediction rests on two plausible links:

- **Antimicrobial activity:** Chlamydial conjunctivitis can be followed by punctate epithelial keratitis. Doxycycline is an established treatment for the chlamydial infection that often precedes it.
- **Anti-inflammatory activity:** Doxycycline is known to inhibit matrix metalloproteinases (MMPs) and reduce inflammation, which could help with ocular surface inflammation.

This is indirect reasoning. The one available paper relates to treating the preceding infection, not to a repurposing signal for the keratitis itself. Notably, in that report the keratitis persisted after the infection was treated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and their follicles resolved. Both then developed recurrent, bilateral punctate corneal epithelial lesions. This describes persistent keratitis after treatment, not a benefit from doxycycline. |

---

## Australia Market Information

| Licence Number | Product Name | Dosage Form |
|---------|------|------|
| 10176N | Doxylin 100 | Tablet 100 mg (as hyclate), oral |

The approved indication text was not available in the licence data compiled for this report. Only oral tablets are listed, and no ocular or topical formulation was identified.

---

## Safety Considerations

**Contraindications flagged by the knowledge graph** (these are drug-disease links, not product label text):
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis
- Dyskinesia of the oesophagus

**Drug interactions:** 100 interactions were identified. The 20 reviewed include:
- **Major:** isotretinoin, acitretin, aminolevulinic acid
- **Moderate:** aluminium hydroxide, aminophylline, amoxicillin, ampicillin, bedaquiline and others
- **Minor:** acetazolamide, amiloride, bendroflumethiazide

Please refer to the TGA-approved Product Information (PI) for full warnings, contraindications and interaction management.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but the supporting evidence is a single 1992 case report that does not show a benefit from doxycycline. There are no clinical trials, and no mechanism of action data is available for this assessment.

**To proceed, the following is needed:**
- Controlled clinical studies of doxycycline (oral or topical ocular) in punctate epithelial keratoconjunctivitis
- Detailed mechanism of action data
- Approved indication text and PI safety information for the Australian product
- Ophthalmic formulation and route feasibility, since only an oral tablet is currently registered

**Note:** Among the other predictions for this drug, chronic gingivitis/periodontitis has substantially stronger support (L2, with multiple clinical studies of subantimicrobial-dose and locally delivered doxycycline). It may be a better candidate to prioritise.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

