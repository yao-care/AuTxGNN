---
layout: default
title: Alectinib
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Alectinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma"
monitor_inn: "Alectinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Alectinib
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

## Alectinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival
{: .text-alpha }

## One-Sentence Summary

Alectinib is an oral ALK inhibitor, originally used to treat non-small cell lung cancer (NSCLC) and lung cancer.
The TxGNN model (deep learning) predicts it may be effective for **Fibromatosis, Gingival** (score 0.9997), but **no clinical trials and no publications** currently support this prediction. It is a model-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma; lung cancer (approved indication text is not available in the ARTG data compiled for this report) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, alectinib is a selective anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor. Its efficacy in ALK-positive NSCLC is well established, but no mechanism has been identified that would link it to gingival fibromatosis.

Gingival fibromatosis is a benign overgrowth of gum tissue. It is not known to be driven by ALK signalling. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern. Most are benign or rare conditions with no ALK link. The exceptions are lung hilum carcinoma and pulmonary sulcus neoplasm, which are anatomically related to the approved indication. Lung germ cell tumour is the only prediction with a tumour-agnostic, ALK-fusion-driven rationale, based on case reports of ALK inhibitors in rare ALK-fusion tumours. That rationale is not specific to germ cell tumours.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for fibromatosis, gingival.

---

## Literature Evidence

Currently no related literature available for fibromatosis, gingival.

The strong Phase 3 evidence retrieved for alectinib (ALEX, J-ALEX and ALINA) relates to ALK-positive NSCLC, which is already the approved indication. It does not support this predicted indication.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11226W | Alecensa | Capsule 150 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Literature notes anaemia, usually mild, including a case of haemolytic anaemia. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Literature reports on alectinib suggest monitoring of full blood count, lipids, and cardiac parameters (heart rate, ECG) and weight. |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policy |

---

## Safety Considerations

- **Drug Interactions**: 92 potential interactions were identified in the DDI data. Examples include:
  - **Major**: aminolevulinic acid
  - **Moderate**: dolasetron, naltrexone, mefloquine, quinine, methoxsalen, atazanavir, bedaquiline, atenolol, acebutolol, bisoprolol, betaxolol, edrophonium and physostigmine
- **Adverse events reported in the literature (not from the label)**: hypertriglyceridaemia-induced pancreatitis, haemolytic anaemia, drug reaction with eosinophilia and systemic symptoms (DRESS), erythema multiforme, and serious weight gain.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available for this report. Please refer to the PI for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications, and no plausible ALK-related mechanism for gingival fibromatosis. Safety screening cannot proceed because the label warnings and contraindications were not available.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible biological link to gingival fibromatosis
- Preclinical or case-level evidence for alectinib in this condition
- The approved indication text and the Product Information (PI) warnings and contraindications for Alecensa
- A review of the other top-ranked predictions. The lung germ cell tumour prediction (rank 7) is a possible research question, using a biomarker-driven approach in ALK-fusion-positive tumours.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

