---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fludrocortisone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Fludrocortisone
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

# Fludrocortisone: From Mineralocorticoid Replacement to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Fludrocortisone is a synthetic corticosteroid with predominantly mineralocorticoid activity, registered in Australia as a 100 microgram oral tablet. The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, but **no clinical trials and no literature** specific to this indication were found. The prediction is currently model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, fludrocortisone is a corticosteroid with strong mineralocorticoid activity and some glucocorticoid activity. Corticosteroids play a general role in symptom control in cutaneous lymphoma, so a loose conceptual link exists.

However, the data compiled for this report show no specific link between fludrocortisone and this lymphoma. The high TxGNN score (0.996) is a graph-based prediction and should be treated as a hypothesis only. Related predictions in the same list, such as granulomatous slack skin disease (a rare cutaneous T-cell lymphoma variant), likely reflect graph proximity to this result rather than independent evidence.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Cystic teratoma | 99.20% | L5 | No plausible mechanism; likely graph artefact |
| 3 | Spinal cord dermoid cyst | 99.18% | L5 | No evidence |
| 4 | Dermoid cyst of ovary | 99.18% | L5 | No evidence |
| 5 | Disease of orbital part of eye adnexa | 99.17% | L5 | No evidence |
| 6 | Eye disease | 99.14% | L4 | Indirect preclinical and review literature only |
| 7 | Disease of orbital region | 99.13% | L5 | No evidence |
| 8 | Exostosis | 99.08% | L5 | No plausible mechanism |
| 9 | Granulomatous slack skin disease | 98.98% | L5 | Likely proximity to rank 1 |
| 10 | Optic papillitis | 98.95% | L5 | No evidence for fludrocortisone |

The only prediction with any supporting literature is "eye disease" (see the note under Literature Evidence). The term is too broad to define a specific therapeutic target.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary cutaneous T-cell lymphoma. No ANZCTR entries were identified either.

## Literature Evidence

Currently no related literature available for primary cutaneous T-cell lymphoma.

For context, the broader "eye disease" prediction (rank 6) retrieved some literature. The most relevant items are below. None provides direct evidence for the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclinical | Experimental Eye Research | Fludrocortisone showed anti-inflammatory and neuroprotective properties in retinal degeneration models |
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B | BMJ Open Ophthalmology | Safety and tolerability of a single intravitreal fludrocortisone acetate injection in geographic atrophy |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Clinical study | International Ophthalmology | Haemodynamic effects of fludrocortisone in glaucoma patients with systemic hypotension |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Review | Survey of Ophthalmology | Non-IOP-lowering glaucoma approaches, including fludrocortisone to avoid blood pressure dips |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Review | Klinische Monatsblätter für Augenheilkunde | Non-IOP-lowering glaucoma therapy, including fludrocortisone |
| [25354755](https://pubmed.ncbi.nlm.nih.gov/25354755/) | 2015 | Diagnostic study | Rheumatology (Oxford) | Furosemide plus fludrocortisone urinary acidification test for distal renal tubular acidosis in Sjögren's syndrome |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1433K | FLUDROCORTISONE MEDSURGE | Tablet containing fludrocortisone acetate 100 micrograms | Not listed in the data compiled for this report |

## Safety Considerations

Warning and contraindication text was not available. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction screen returned 100 entries. Most listed entries are of Moderate severity.

- **Major:** Bupropion
- **Moderate (examples):**
  - Antidiabetic agents: acarbose, alogliptin, pioglitazone, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin, linagliptin, albiglutide, dulaglutide
  - Amphotericin B (including lipid complex)
  - Aprepitant
  - Acetylsalicylic acid
  - Clarithromycin
  - Laxatives: bisacodyl, picosulfuric acid
  - Anabolic steroids: oxandrolone, oxymetholone

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction is supported only by a graph-based score, with no clinical trials or literature (evidence level L5). The prediction is not suitable for progression at this stage.

**To proceed, the following is needed:**
- Mechanism of action data to assess a plausible link to cutaneous T-cell lymphoma
- A targeted literature review of corticosteroid use in cutaneous lymphoma, and whether mineralocorticoid activity is relevant
- The approved indication from the ARTG entry, and the PI warnings and contraindications
- Preclinical or early clinical data for fludrocortisone in this disease
- If an alternative direction is wanted, clarification of the broad "eye disease" signal. Candidates are geographic atrophy (the Phase 1B intravitreal study) or glaucoma-related systemic hypotension. Either would be a separate research question, not a repurposing decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

