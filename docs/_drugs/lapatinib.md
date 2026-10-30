---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Lapatinib"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Lapatinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Not recorded in the local data"
---

# Lapatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lapatinib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Lapatinib was originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but currently there are **no clinical trials** and **no publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lapatinib is a tyrosine kinase inhibitor that targets EGFR and HER2, and its efficacy in HER2-positive breast carcinoma is established. Whether this mechanism applies to DFSP is unproven.

DFSP is driven mainly by the COL1A1-PDGFB fusion and PDGFR signalling, which is not a canonical lapatinib target. Any link would be speculative and would rely on indirect crosstalk between receptor tyrosine kinase pathways. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions with some supporting literature were also reviewed (see "Other Predicted Indications" below), but the top-ranked prediction has no direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11251E | Tykerb | Tablet 250 mg (as ditosilate monohydrate) | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Liver function, cardiac function (including QT interval), electrolytes, and respiratory symptoms; see the PI for details |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, potassium deficiency disease, interstitial lung disease, drug-induced liver injury, and heart failure.
- **Drug Interactions**: 100 interactions were identified in total. Examples from the 20 reviewed:
  - **Major**: loperamide, clarithromycin
  - **Moderate**: acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexlansoprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aprepitant, pioglitazone, saxagliptin, and several laxatives or bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol)

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Other Predicted Indications

| Rank | Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|

**Malaria (rank 8)** is the only alternative with a plausible, distinct mechanism, and it is a research question rather than a clinical candidate:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32235391](https://pubmed.ncbi.nlm.nih.gov/32235391/) | 2020 | Preclinical (in vitro) | Molecules | Lapatinib, nilotinib and lomitapide inhibited haemozoin (β-haematin) formation in malaria parasites. |
| [42374402](https://pubmed.ncbi.nlm.nih.gov/42374402/) | 2026 | Systematic analysis | Malar J | Landscape analysis of the 51 most cited malaria drug repurposing studies. |
| [29301082](https://pubmed.ncbi.nlm.nih.gov/29301082/) | 2018 | Preclinical | ACS Infect Dis | Optimisation of lapatinib-derived 4-anilinoquinolines against *P. falciparum*. |
| [25685309](https://pubmed.ncbi.nlm.nih.gov/25685309/) | 2015 | Preclinical | MedChemComm | Kinase-inhibitor-derived thienopyrimidine scaffolds tested against trypanosomiasis, leishmaniasis and malaria parasites. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for DFSP rests only on a model score (L5). There are no clinical trials or publications, and the disease driver (PDGFB/PDGFR) is not a recognised lapatinib target. Safety signals from the knowledge graph (QT prolongation, hepatotoxicity, heart failure, interstitial lung disease) and major drug interactions also call for caution.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), for example from DrugBank
- Preclinical data on lapatinib in DFSP models, ideally compared with PDGFR-directed agents
- Parsed Product Information (PI) warnings and contraindications, which are required before safety screening
- For the malaria direction, evidence that antimalarial concentrations are achievable at tolerable doses, together with a safety assessment
- ARTG indication text to confirm the approved original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

