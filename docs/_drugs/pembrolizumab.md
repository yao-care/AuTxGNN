---
layout: default
title: Pembrolizumab
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Pembrolizumab"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
description: "Pembrolizumab: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Not recorded in the local data"
---

# Pembrolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pembrolizumab: Fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor, originally used to treat non-small cell lung cancer and metastatic melanoma.
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 0.9940), but **no clinical trials and no publications** support this prediction.
The prediction is a computational signal only, and the other top-ranked predictions show similar gaps (see the note below the Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pembrolizumab is a monoclonal antibody that targets programmed cell death protein 1 (PD-1, CD279; gene PDCD1). It blocks PD-1 and so restores T-cell activity against tumour cells.

Its efficacy in lung cancer and melanoma is well established. However, gingival fibromatosis is a benign, fibroproliferative (often hereditary) condition. No mechanistic link between PD-1 blockade and this condition has been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature is available for gingival fibromatosis.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10424P | Keytruda | Solution concentrate for I.V. infusion, 100 mg in 4 mL | Not available in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; immune-related adverse events (for example thyroid, liver, endocrine and pulmonary effects) are the usual focus |
| Handling Protection | Please refer to the PI and local institutional policy |

---

## Safety Considerations

- **Drug Interactions** (13 entries, from the DDI screening):
  - **Major:** lenalidomide, pomalidomide, thalidomide.
  - **Moderate:** systemic and inhaled corticosteroids, including hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort.
  - The remaining entry is the pharmacological target record (PD-1), which is not an interaction.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism for a benign fibroproliferative condition. Immune-related adverse events also add a safety concern for a non-malignant indication.

**To proceed, the following is needed:**
- Mechanistic data showing a role for PD-1 in gingival fibromatosis
- Preclinical or case-level evidence of benefit
- Detailed mechanism of action data (MOA)
- Review of the TGA-approved PI for warnings and contraindications
- A risk-benefit assessment for a benign condition

**Note on other predictions:** The remaining top-ranked predictions are also weak. Most have no supporting evidence. Several are essentially the already-approved lung cancer indication (lung hilum carcinoma, lung benign neoplasm, pulmonary sulcus neoplasm), where the Phase 3 lung cancer evidence does not transfer to benign tumours. Lung germ cell tumour (L3) has only indirect trial data and is better treated as a research question than a repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

