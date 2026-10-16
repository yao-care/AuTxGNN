---
layout: default
title: Ponatinib
parent: Model Prediction Only (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ponatinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: Chronic myelogenous leukaemia, BCR-ABL1 positive"
monitor_inn: "Ponatinib"
predicted_indications: ["fibromatosis, gingival", "liposarcoma", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "ovarian myxoid liposarcoma", "hamartoma of lung", "fibroma of lung", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung benign neoplasm", "lung hilum carcinoma"]
---

# Ponatinib
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

# Ponatinib: From Chronic Myeloid Leukaemia to Gingival Fibromatosis

## One-Sentence Summary

Ponatinib is a multi-targeted tyrosine kinase inhibitor, originally used for BCR-ABL1-positive chronic myeloid leukaemia.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction.
This is a model-only prediction (L5), and the remaining nine ranked predictions have similarly little disease-specific support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukaemia, BCR-ABL1 positive (the Australian licence entry has no indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Ponatinib is a third-generation BCR-ABL tyrosine kinase inhibitor, and its efficacy in BCR-ABL1-positive chronic myeloid leukaemia is established. It is also known to inhibit other kinases, including FGFR, PDGFR, VEGFR, SRC, KIT and RET.

A link between these pathways and a fibroproliferative condition such as gingival fibromatosis is conceivable, because PDGFR and FGFR signalling are involved in fibroblast growth. However, this is speculative. No trials or publications in the compiled data connect ponatinib to this condition. The high TxGNN score is a computational prediction only.

### Other Ranked Predictions

The table below summarises the other nine predictions in the compiled data.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Liposarcoma | 99.00% | L4 | One 2017 preclinical kinase-profiling study; no ponatinib-specific efficacy shown |
| 3 | Inclusion body myopathy with early-onset Paget disease (with or without frontotemporal dementia) | 98.98% | L5 | No evidence; no mechanistic link identified |
| 4 | Ovarian myxoid liposarcoma | 98.93% | L5 | No direct evidence |
| 5 | Hamartoma of lung | 98.93% | L5 | Benign lesion; unfavourable risk-benefit given ponatinib's cardiovascular and thrombotic safety burden |
| 6 | Fibroma of lung | 98.87% | L5 | Benign neoplasm; no supporting evidence |
| 7 | Junctional epidermolysis bullosa | 98.86% | L5 | No plausible kinase-inhibitor mechanism evident |
| 8 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 98.83% | L5 | Retrieved literature is generic and not disease-specific |
| 9 | Lung benign neoplasm | 98.83% | L5 | Literature covers pharmacology and toxicity, nothing specific to this condition |
| 10 | Lung hilum carcinoma | 98.81% | L5 | No evidence; RET and FGFR inhibition is relevant to some lung cancers only |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis. No clinical trials are listed for any of the ten ranked predictions.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For context, publications retrieved for other predictions (liposarcoma, lung benign neoplasm, and the rare syndrome at rank 8) are largely general ponatinib, FGFR, PDGFR and RET literature, or toxicity reviews. They do not provide disease-specific efficacy evidence.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10520Q | Iclusig | Tablet 15 mg (as hydrochloride) | Not stated in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; the literature compiled for this report highlights cardiovascular toxicity, vascular occlusion and pulmonary complications as areas of concern |
| Handling Protection | Please refer to the PI and local handling policies |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. The first 20 listed include:
  - **Major**: acetylsalicylic acid (aspirin), clarithromycin
  - **Moderate**: loperamide, aprepitant, dexamethasone, naldemedine, naltrexone, metronidazole, miconazole
  - **Minor**: acid-suppressing agents (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), magnesium oxide, naloxegol
- **Literature-Reported Concerns**: Reviews in the compiled data describe cardiotoxicity, vascular events (peripheral artery disease and stroke), pulmonary complications and cutaneous reactions with ponatinib and related tyrosine kinase inhibitors.

Label warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gingival fibromatosis rests on a model score alone, with no trials, no literature and no established mechanistic link. Ponatinib also carries a significant cardiovascular and thrombotic safety burden, which makes a non-malignant indication hard to justify without supporting evidence.

**To proceed, the following is needed:**
- Mechanism of action data, to assess the plausibility of a PDGFR/FGFR-mediated fibroproliferative link
- Preclinical evidence (for example, in gingival fibroblast models) showing ponatinib activity
- TGA-approved PI warnings and contraindications for a formal safety screen
- Approved indication text for the Australian ARTG entry
- A risk-benefit framework for a non-malignant indication
- If a different indication is preferred, liposarcoma is the only one with any supporting literature (L4), though this is a single preclinical kinase-profiling study and not ponatinib-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

