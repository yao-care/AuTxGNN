---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 100
evidence_level: L5
indication_count: 6
monitor_inn: "Bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-10-28
description: "Bleomycin: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Bleomycin: DNA strand-scission cytotoxic glycopeptide → cauda equina neoplasm
{: .text-alpha }

## One-Sentence Summary

Bleomycin is a cytotoxic antibiotic that cleaves DNA strands and is used in cancer chemotherapy. The TxGNN model predicts it may be relevant to **cauda equina neoplasm**, with a score of 0.9930. The data compiled for this report contain **no clinical trials** and **1 publication** for this disease, and that publication does not study it, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Bleomycin is known as a DNA strand-scission cytotoxic agent, and this is the only mechanistic basis available for the prediction.

The one linked publication (PMID 9440744) describes radiation therapy for relapsed CNS germinoma after chemotherapy that included carboplatin, etoposide and bleomycin. It does not study cauda equina neoplasm or test bleomycin in that setting. The high score is therefore a model output without clinical support, and the mechanistic link to this tumour type is speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort (retrospective) | Journal of Clinical Oncology | Radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy (carboplatin, etoposide, bleomycin). It does not address cauda equina neoplasm. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4433H | DBL Bleomycin Sulfate | Powder for injection containing bleomycin sulfate 15,000 I.U. | Not recorded in the local data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA strand-scission antibiotic) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Pulmonary function and clinical lung assessment (interstitial pneumonitis is a recognised risk); also refer to the PI |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Key Warnings**: Interstitial pneumonitis and pulmonary toxicity are recognised risks of bleomycin therapy. Reported hyperpyrexic reactions after bleomycin have also been described in the literature compiled for the other predictions.
- **Drug Interactions**: The interaction screen returned 100 entries. The ones listed in the data are mostly of unknown severity (for example pantoprazole, omeprazole, morphine, prednisone, vancomycin, ondansetron). Levofloxacin is graded Minor. Refer to the PI for clinically significant interactions.

For other warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial and no publication directly studies bleomycin in cauda equina neoplasm. The evidence level is therefore L5, and the high TxGNN score is not supported by clinical data. Pulmonary toxicity is a further concern.

**To proceed, the following is needed:**
- Literature or case series showing bleomycin activity in spinal or cauda equina tumours
- Mechanism of action data and a rationale for drug delivery to the spinal canal
- Review of the TGA Product Information for warnings and contraindications
- Assessment of the suitability of the available injectable formulation for this tumour type
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

