---
layout: default
title: Lincomycin
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-17
monitor_inn: "Lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
description: "Lincomycin: predicted new indication Hyperamylasemia (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Lincomycin
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

## Lincomycin: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Lincomycin is a lincosamide antibiotic, originally used to treat pneumococcal, staphylococcal and streptococcal infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials** and **no relevant publications** currently support this direction.
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No mechanistic basis has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lincomycin: "Lincomycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the bacterial ribosome. Lincomycin is predominantly bacteriostatic in vitro." ([DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263), label version 2025-03-10; accessed 2026-11-19.) Lincomycin is known to be a lincosamide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in Gram-positive bacterial infections is established.

No plausible pathway links this antibacterial action to raised serum amylase. Hyperamylasemia is a laboratory finding that can arise from pancreatic or salivary gland disease or reduced clearance of amylase. It is not an infection that an antibacterial would treat directly. The high TxGNN score (rank 8,929) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it should be read with caution.

Other top-ranked predictions for lincomycin (for example polyclonal hyperviscosity syndrome, congenital analbuminemia and blood group incompatibility) also have no mechanistic link and no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11366F | LINCOMYCIN SXP | Injection 600 mg (as hydrochloride monohydrate) in 2 mL | Not stated in the data compiled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the TxGNN graph, not from label text): liver failure, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, colitis, digestive system disease and intestinal disease. The *C. difficile* and colitis signals are consistent with the well-known risk of antibiotic-associated colitis with lincosamides.
- **Drug Interactions**: 21 interactions were recorded in the DDInter database, 5 of them rated Moderate.
  - Moderate: balsalazide, picosulfuric acid, attapulgite, kaolin, erythromycin, ethinylestradiol.
  - The remaining interactions have no severity rating. They include clotrimazole, cimetidine, morphine, metformin, omeprazole, lactulose, triamcinolone, simvastatin, ranitidine, warfarin, lidocaine, cetirizine, montelukast and salmeterol.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature and no plausible mechanism, so it is a model output only (Evidence Level L5). Lincomycin also carries a significant gastrointestinal safety signal (antibiotic-associated colitis), which would need to be justified by a clear benefit.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking lincomycin to amylase elevation, or confirmation that the score reflects only similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence
- Detailed mechanism of action data
- The TGA Product Information, including warnings, contraindications and approved indications, so that safety screening can proceed
- Any clinical or observational data on lincomycin and serum amylase

## Other Predictions Noted (Not Recommended for Progression)

Two lower-ranked predictions have indirect evidence only and are better framed as research questions than as repurposing candidates:

- Lincosamides are generally ineffective against Gram-negative bacilli such as *Yersinia pestis*, and guideline-recommended agents already exist. No clinical efficacy data.
- The only randomised trial ([PMID 1433889](https://pubmed.ncbi.nlm.nih.gov/1433889/), 1992, n=95) compared imipenem/cilastatin with aztreonam plus lincomycin in severe infections in patients with malignancy or haematological disease. Lincomycin was only a partner drug, so this does not show monotherapy efficacy. Most urinary tract infections are caused by Gram-negative organisms against which lincomycin is inactive.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

