---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer (lung cancer). The ARTG entry in the data…"
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib is an oral EGFR tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** were found for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (lung cancer). The ARTG entry in the data compiled for this report has no approved indication text. |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, gefitinib is a selective inhibitor of the epidermal growth factor receptor (EGFR) tyrosine kinase. Its efficacy in EGFR-mutant NSCLC is well established.

Gingival fibromatosis is a fibroproliferative condition of the gums. A speculative link is EGFR/ErbB signalling in fibroblast proliferation. However, nothing in the compiled data supports this link, and the similarity between the original and predicted indications has not been assessed. The high score most likely reflects the model's network patterns rather than a validated biological rationale.

Other top-ranked predictions were reviewed too. Most are also prediction-only (L5). The ones with literature are not gefitinib-specific:

- **Lung hilum carcinoma** and **pulmonary sulcus neoplasm** are essentially lung cancers, so the existing EGFR-TKI rationale could apply to EGFR-mutant cases. The evidence is limited to case reports and general reviews, so these are best treated as research questions rather than new indications.
- **Lung germ cell tumour** has one linked trial, which studied head and neck cancer and NSCLC rather than germ cell tumours.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11264W | Cipla Gefitinib | Tablet 250 mg | Not stated in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Liver function and respiratory symptoms are of particular interest (see Safety Considerations). Please refer to the PI for the full monitoring schedule. |
| Handling Protection | Please refer to the PI and local cytotoxic or hazardous drug handling policies |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis and post-inflammatory pulmonary fibrosis. Literature retrieved for other predictions also describes gefitinib-associated pneumonitis and interstitial lung disease, including a fatal case, QT prolongation (preclinical), and cutaneous toxicity (acneiform eruption, paronychia, xerosis).
- **Drug interactions**: 100 interactions were identified, and the main ones listed are Moderate or Unknown severity.
  - Acid-suppressing agents (H2 blockers and PPIs): famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole.
  - Other moderate-level interactions: clarithromycin, aprepitant, dexamethasone, naltrexone, miconazole, clotrimazole, troglitazone.
  - Unknown-level interactions: calcitriol, glimepiride.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label text was not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gingival fibromatosis is supported only by a model score, with no clinical trials, no literature and no established mechanistic link. A skin and mucosal toxicity profile for gefitinib is also a potential concern in fibroproliferative or epithelial conditions.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a documented rationale for EGFR/ErbB involvement in gingival fibroblast proliferation
- Preclinical studies (for example fibroblast models) and a literature search specific to gingival fibromatosis
- The TGA Product Information, including warnings, contraindications and the approved indication text, to enable safety screening
- Assessment of route and dosing suitability, since only an oral 250 mg tablet is registered
- Separately, consider whether the lung hilum carcinoma and pulmonary sulcus neoplasm predictions merit a research question, since they fall within the existing lung cancer setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

