---
layout: default
title: Lincomycin
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lincomycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Pneumococcal, staphylococcal and streptococcal infections"
monitor_inn: "Lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "urinary tract infection (disease)"]
---

# Lincomycin
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

# Lincomycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Lincomycin is a lincosamide antibiotic, originally used to treat pneumococcal, staphylococcal and streptococcal infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials** and **no relevant publications** currently support this direction.
The prediction is a graph-based score only and has no identified mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pneumococcal, staphylococcal and streptococcal infections (the ARTG entry carries no indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Lincomycin is known to be a lincosamide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in Gram-positive bacterial infections is established.

No plausible pathway links this antibacterial action to raised serum amylase. Hyperamylasemia is a laboratory finding that can arise from pancreatic or salivary gland disease or reduced clearance of amylase. It is not an infection that an antibacterial would treat directly. The high TxGNN score (rank 8,929) appears to reflect a pattern in the knowledge graph rather than a biological rationale, and it should be read with caution.

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
- A credible mechanistic hypothesis linking lincomycin to amylase elevation, or confirmation that the prediction is an artefact of the graph
- Detailed mechanism of action data
- The TGA Product Information, including warnings, contraindications and approved indications, so that safety screening can proceed
- Any clinical or observational data on lincomycin and serum amylase

## Other Predictions Noted (Not Recommended for Progression)

Two lower-ranked predictions have indirect evidence only and are better framed as research questions than as repurposing candidates:

- **Septicemic plague (score 98.11%, L4):** Two in vitro susceptibility surveys (PMIDs [1300928](https://pubmed.ncbi.nlm.nih.gov/1300928/) and [7259143](https://pubmed.ncbi.nlm.nih.gov/7259143/)) tested plague strains against lincomycin. Lincosamides are generally ineffective against Gram-negative bacilli such as *Yersinia pestis*, and guideline-recommended agents already exist. No clinical efficacy data.
- **Urinary tract infection (score 97.77%, L4):** The literature is mostly veterinary or microbiological. The only randomised trial ([PMID 1433889](https://pubmed.ncbi.nlm.nih.gov/1433889/), 1992, n=95) compared imipenem/cilastatin with aztreonam plus lincomycin in severe infections in patients with malignancy or haematological disease. Lincomycin was only a partner drug, so this does not show monotherapy efficacy. Most urinary tract infections are caused by Gram-negative organisms against which lincomycin is inactive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

