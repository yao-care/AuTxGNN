---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bevacizumab: predicted new indication Epiglottis neoplasm (evidence level L5). Approved use: Not stated in the Australian registration data. The drug knowledge gr…"
---

# Bevacizumab
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

# Bevacizumab: From Ovarian, Breast and Colorectal Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF monoclonal antibody, originally used for cancers such as ovarian, peritoneal, breast, colorectal and glioblastoma.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data. The drug knowledge graph lists peritoneal, ovarian, breast, colon (metastatic) and glioblastoma-related cancers |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bevacizumab is generally known as a monoclonal antibody that neutralises VEGF-A, a key driver of tumour angiogenesis. Its efficacy in several vascular, angiogenesis-dependent cancers is established.

Epiglottis neoplasms are head and neck tumours. Anti-VEGF therapy may plausibly affect tumour blood supply in such lesions. However, the prediction is based only on the TxGNN graph score (rank 1786 overall). No trials or publications specific to this indication were supplied, so the mechanistic link remains a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

For context, other predicted indications for bevacizumab have indirect head and neck trials (for example NCT00023959, a Phase 1 study in poor-prognosis head and neck cancer), but these were not linked to epiglottis neoplasm.

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 12479T | Mvasi | Solution for I.V. infusion, 100 mg in 4 mL | Not available in the data compiled |

The approved indication text for this product was not available, and the licence number format should be verified against the ARTG record.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Typical monitoring would include blood pressure, urinary protein, and full blood count |
| Handling Protection | Please refer to the PI and local institutional policy for handling of antineoplastic agents |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Drug Interactions**: 22 interactions were recorded in the DDI database (ddinter). Major-level interactions include:
- Deferiprone
- Samarium (153Sm) lexidronam
- Panitumumab
- Sunitinib
- Thalidomide

Moderate-level interactions include bisphosphonates (alendronic acid, risedronic acid, etidronic acid, ibandronate, pamidronic acid, tiludronic acid), colony-stimulating factors (filgrastim, pegfilgrastim, sargramostim), palifermin, strontium-89, idelalisib, radium-223, romosozumab and sodium phosphate P-32.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for epiglottis neoplasm is supported only by the TxGNN model score (Evidence Level L5). No trials or publications address this indication, and the safety data from the Australian label are missing.

**To proceed, the following is needed:**
- Indication-specific evidence (clinical trials or published studies in epiglottis or laryngeal neoplasms)
- Detailed mechanism of action data
- Approved indication text and safety information (warnings and contraindications) from the TGA Product Information for Mvasi
- A safety review of the major drug interactions listed above, particularly with other anticancer agents
- Assessment of whether the lesion type (benign or malignant) is clinically relevant to the proposed use

**Other candidates noted in the data:** Among the other predictions, "cystic neoplasm" has the strongest support (Evidence Level L1, including a Phase 3 RCT, NCT00565851, and a systematic review). However, that evidence largely reflects existing approved use in ovarian cancer rather than true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

