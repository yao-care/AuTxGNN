---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 769
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis, staphylococcal infections…"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis and Gram-Positive Infections to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but **no clinical trials** and only **1 unrelated case report** support this prediction, and the data compiled for this report found no plausible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridium difficile* colitis, staphylococcal infections, endocarditis, bacterial arthritis, staphylococcal pneumonia (approved indication text for the ARTG entry is not available) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, vancomycin is a glycopeptide antibiotic that inhibits bacterial cell wall synthesis, and its efficacy in Gram-positive infections is well established.

Diffuse scleroderma is an autoimmune, fibrotic disease. Vancomycin has no known immunomodulatory or antifibrotic action, so no plausible mechanistic link to this condition was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The only retrieved paper is a case report of erythroderma with sepsis and eosinophilia, which does not address scleroderma.

**Other predictions reviewed (all lower priority):**

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Paratyphoid fever | 0.9985 | L5 | Gram-negative pathogen; vancomycin cannot cross the outer membrane. Only an antibiogram survey was found. |
| Salmonellosis | 0.9981 | L5 | Intrinsic resistance. Literature is resistance surveillance and reviews. Oral vancomycin may disrupt colonisation resistance and worsen enteric infection. |
| Congenital analbuminemia | 0.9979 | L5 | No mechanistic link, no literature. |
| Polyclonal hyperviscosity syndrome | 0.9979 | L5 | No mechanistic link, no literature. |
| Hyperamylasemia | 0.9979 | L5 | A laboratory finding, not a treatable target. |
| Typhoid fever | 0.9975 | L5 | Gram-negative; only case reports and general reviews, none showing vancomycin efficacy. |
| Blood group incompatibility | 0.9963 | L5 | Unrelated; one irrelevant microbiology paper. |
| Streptococcal pneumonia | 0.9960 | L4 | Biologically plausible (Gram-positive, reserve option for resistant pneumococci), but largely overlaps existing Gram-positive indications. Evidence is reviews and surveillance only. |
| Premalignant haematological system disease | 0.9954 | L5 | No mechanistic link, no literature. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | Case of diffuse exfoliative rash (erythroderma) with sepsis and eosinophilia in a 56-year-old man. It does not address scleroderma or vancomycin efficacy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14696L | Vancomycin Viatris | Powder for injection 500 mg (500,000 I.U.) (as hydrochloride) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications and warnings from the knowledge graph (not label text):** the TxGNN knowledge graph links vancomycin to the following conditions as contraindications or cautions:
- Kidney disease
- Pyoureter
- Neutropenia
- Agranulocytosis
- Hearing disorder and auditory system disease

**Drug interactions:** The interaction query returned 100 interactions in total. Examples from the 20 listed include:
- **Major:** human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, and live *Vibrio cholerae* CVD 103-HgR vaccine.
- **Moderate:**
  - Nephrotoxic or ototoxic combinations: amikacin, amphotericin B (including lipid complex), bacitracin, capreomycin, carboplatin.
  - NSAIDs: ketorolac, ibuprofen, diclofenac, celecoxib.
  - Others: metformin, estradiol, ethinylestradiol, mesalazine, balsalazide, ibandronate, cholestyramine.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, the single paper is unrelated, and vancomycin has no recognised antifibrotic or immunomodulatory mechanism for diffuse scleroderma. None of the other nine predicted indications showed meaningful new evidence. Streptococcal pneumonia is plausible but largely duplicates existing Gram-positive use.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to enable mechanistic-link analysis
- TGA Product Information, including approved indications, warnings and contraindications for ARTG 14696L
- Any preclinical or clinical rationale linking vancomycin to scleroderma pathophysiology (none identified so far)
- If a new direction is pursued, streptococcal pneumonia is a better candidate for a focused literature review, although it mostly overlaps existing indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

