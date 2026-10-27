---
layout: default
title: Minocycline
parent: Model Prediction Only (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Minocycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections including urinary tract infection, bronchitis…"
monitor_inn: "Minocycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "neurotrophic keratopathy", "postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "post-infectious syndrome", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
---

# Minocycline
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

## Minocycline: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Minocycline is a tetracycline-class antibiotic, originally used for bacterial infections such as urinary tract infection, bronchitis, acne, gonorrhoea and periodontitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** were found to support this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections including urinary tract infection, bronchitis, acne, gonorrhoea and periodontitis (from the knowledge graph; the ARTG entry carries no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, minocycline belongs to the tetracycline class, its efficacy in bacterial infections and acne is established, and mechanistically it may be applicable to inflammatory conditions of the ocular surface.

The plausible link is the anti-inflammatory and matrix metalloproteinase (MMP) inhibiting activity attributed to tetracyclines, which could be relevant to ocular surface inflammation. This is a hypothesis from the prediction rationale only. No trials or literature were retrieved to confirm it, and the original indications are mainly systemic infections and acne rather than eye disease.

Other top-ranked predictions include exposure keratitis (99.20%), neurotrophic keratopathy (98.98%), otitis externa (98.70%), chronic rhinosinusitis (98.63%) and several non-specific post-infectious conditions. All are at L4 or L5 evidence, and none has controlled clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14483G | Akamin 50 | Tablet 50 mg (as hydrochloride) | Not stated in the data compiled for this report |

Only oral tablet forms are registered. No ophthalmic formulation was identified.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, pseudotumor cerebri, intracranial hypertension, pyoureter and oesophageal dyskinesia.
- **Drug Interactions:** 100 interactions were recorded; the first 20 returned include:
  - **Major:** isotretinoin and acitretin (retinoids; the combination is associated with raised intracranial pressure risk).
  - **Moderate:** ethinylestradiol, amoxicillin, ampicillin, aminolevulinic acid (topical), sodium citrate, asparaginase products, balsalazide, bismuth subcitrate potassium, calcium phosphate, calcium acetate, brentuximab vedotin, calaspargase pegol and cannabidiol.
  - **Minor:** acetazolamide, hydrochlorothiazide, amiloride and bumetanide.
- **Topical concern:** an in vitro study found tetracyclines cytotoxic to human tympanic membrane fibroblasts, although less so than quinolones. This suggests caution for any topical ear use.

Please also refer to the TGA-approved Product Information (PI) for full safety information, as label warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for punctate epithelial keratoconjunctivitis is supported only by a high model score (L5). No trials or publications were found, no ophthalmic route is registered in Australia, and label safety data were not available.

**To proceed, the following is needed:**
- Mechanism of action data for minocycline (for example from DrugBank) to test the link to ocular surface disease
- Systematic search for clinical or preclinical evidence of tetracyclines, including minocycline, in keratoconjunctivitis and related ocular surface conditions
- Retrieval of the TGA Product Information to complete warnings and contraindications screening
- Assessment of route feasibility, as only oral tablets are registered and an ophthalmic formulation would be needed
- Review of the other ranked predictions with some indirect evidence (such as otitis externa) only if a specific clinical question arises
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

