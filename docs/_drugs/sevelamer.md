---
layout: default
title: Sevelamer
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sevelamer: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not stated in the data compiled for this report (sevelamer is a phosp…"
---

# Sevelamer
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

# Sevelamer: From Hyperphosphataemia Management to Breast Fibrocystic Disease

## One-Sentence Summary

Sevelamer is a non-absorbed phosphate-binding polymer, marketed in Australia as sevelamer carbonate tablets. The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but **no clinical trials and no publications** support this prediction. The only candidate in the top ten with a plausible research direction is **HIV infection** (3 publications, mixed results), and it should be treated as a separate research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (sevelamer is a phosphate binder; the approved indication text for the Australian product was not available) |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 92.46% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, sevelamer is a non-absorbed polymer that binds dietary phosphate in the gut. It is used in patients with chronic kidney disease who have hyperphosphataemia.

For **breast fibrocystic disease**, no plausible mechanistic link is evident. The high score appears to come from the knowledge-graph structure rather than from biological or clinical evidence. The next three predictions (blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) share the same benign breast disease cluster and are not independent signals. Several other predictions (breast abscess, fat necrosis of breast, a rare neurodevelopmental disorder) also lack any supporting evidence.

The most biologically interesting prediction is **HIV infection / AIDS** (scores 87.16% and 86.40%). The hypothesis is that sevelamer binds bacterial endotoxin (lipopolysaccharide) in the gut. This could reduce microbial translocation and chronic immune activation. An SIV macaque study supports the idea. However, a small human study did not confirm a reduction in the key markers, so the mechanism remains unproven in people.

## Clinical Trial Evidence

Currently no related clinical trials registered for breast fibrocystic disease, or for any of the other top-ten predicted indications.

## Literature Evidence

Currently no related literature available for breast fibrocystic disease.

For reference, the following publications relate to the HIV/AIDS predictions (ranks 5 and 6), the only candidates with a literature signal of possible therapeutic relevance:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24864123](https://pubmed.ncbi.nlm.nih.gov/24864123/) | 2014 | Single-arm clinical study (36 people with untreated HIV, 8 weeks) | J Infect Dis | Sevelamer did not significantly change lipopolysaccharide or soluble CD14 (markers of microbial translocation). It did reduce soluble tissue factor, LDL cholesterol and oxidised LDL cholesterol. |
| [24837437](https://pubmed.ncbi.nlm.nih.gov/24837437/) | 2014 | Preclinical (SIV macaque model) | J Clin Invest | Early blockade of microbial translocation with sevelamer reduced SIV-related inflammation and viral replication. |
| [42371456](https://pubmed.ncbi.nlm.nih.gov/42371456/) | 2026 | Case report | Cureus | Recurrent calciphylaxis in a patient with HIV-associated end-stage renal disease. It has no bearing on antiviral or immunomodulatory efficacy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11838C | Sevelamer Lupin | Tablet containing sevelamer carbonate 800 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety warnings and contraindications.

- **Knowledge-graph contraindication signals** (from drug-disease relationships in a knowledge graph, not from label text): vitamin D deficiency, osteomalacia, rickets, hypophosphataemia and gastroparesis. These should be verified against the PI.
- **Drug Interactions** (DDInter, 100 interactions recorded). The moderate-level interactions include:
  - Cholecalciferol
  - Calcifediol
  - Calcitriol
  - Dihydrotachysterol
  - Ergocalciferol
  - Levofloxacin
  - Vitamin A

  Other recorded interactions have an unclassified severity, including pantoprazole, omeprazole, lansoprazole, cimetidine, vancomycin, morphine, prednisone and acarbose. Co-administration timing with other oral medicines should be checked against the PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (breast fibrocystic disease) is supported only by a graph-based score. There are no trials or publications, and no plausible mechanism. The HIV/AIDS predictions are better framed as a single, separate research question (L4), because the animal data are encouraging but the human biomarker study was largely negative.

**To proceed, the following is needed:**
- The approved indication text and the PI warnings and contraindications for the Australian product (ARTG 11838C)
- Mechanism of action data for sevelamer
- Any biological rationale linking a non-absorbed phosphate binder to benign breast disease. Without one, this prediction should not advance.
- For the HIV research question, a review of the full text of the human study design and a controlled trial with clinically relevant endpoints
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

