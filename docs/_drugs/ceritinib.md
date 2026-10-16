---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceritinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer"
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK inhibitor originally used to treat non-small cell lung cancer (NSCLC) and lung cancer.
The TxGNN model predicts it may be effective for **hereditary gingival fibromatosis**, but this is a purely computational prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer; lung cancer (approved indication text for the ARTG entry is not available) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ceritinib is known from the literature to inhibit ALK, ROS1 and IGF-1R, and its efficacy in ALK-rearranged NSCLC has been established.

No established role for these targets in hereditary gingival fibromatosis was found in the data compiled. Gingival fibromatosis is a benign overgrowth of gum tissue and is biologically unrelated to ALK-driven lung cancer. The high TxGNN score (99.86%) therefore reflects a knowledge-graph pattern rather than a demonstrated mechanistic link, and the prediction should be treated as speculative.

### Other Predictions Reviewed

The other top-ranked predictions are also supported only weakly:

- **Lung hilum carcinoma and pulmonary sulcus neoplasm:** These would be relevant only if the tumour is ALK-positive, which falls within the existing approved indication rather than being a new one.
- **Lung benign neoplasm:** The 20 publications retrieved concern ALK biology and ceritinib in malignant ALK-rearranged NSCLC. None shows efficacy in benign lung tumours.
- **Lung germ cell tumour:** The publications concern other ALK-altered tumours (neuroblastoma, glioblastoma, pulmonary carcinoid). This evidence is indirect.
- **Fibroma of lung, hamartoma of lung, inclusion body myopathy, leukomelanoderma syndrome and junctional epidermolysis bullosa:** No supporting mechanism or evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For context, the publications retrieved for the lower-ranked prediction "lung benign neoplasm" mostly describe the approved NSCLC use. The key example is below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28126333](https://pubmed.ncbi.nlm.nih.gov/28126333/) | 2017 | RCT | Lancet | ASCEND-4: first-line ceritinib versus platinum-based chemotherapy in advanced ALK-rearranged NSCLC (Phase 3) |

This trial concerns the approved malignant indication, not a new one.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11056X | Zykadia | Capsule 150 mg (oral) | Not available in the data compiled; please refer to the TGA Product Information |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. The literature raises cardiac (QT prolongation), renal and hypersensitivity concerns with ALK inhibitors and related TKIs. |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interactions, with 20 shown in the data compiled. Two are rated **Major**: triamcinolone and budesonide. Most others are rated Moderate, including:
  - acid-suppressing drugs (famotidine, ranitidine, omeprazole, rabeprazole);
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone);
  - antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide);
  - loperamide, aprepitant and bisacodyl.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials or publications for gingival fibromatosis, and no plausible mechanism links ALK/ROS1/IGF-1R inhibition to this condition. Ceritinib is also a cytotoxic-class oncology agent with significant safety considerations, which makes a benign, non-life-threatening condition a poor benefit-risk fit without supporting data.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and any biological evidence linking ALK, ROS1 or IGF-1R signalling to gingival fibroblast overgrowth
- Preclinical evidence in relevant models
- Safety information (warnings and contraindications) from the TGA Product Information
- The approved indication text for the ARTG entry
- A benefit-risk assessment for a benign condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

