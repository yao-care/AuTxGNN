---
layout: default
title: Ocrelizumab
parent: Model Prediction Only (L5)
nav_order: 517
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ocrelizumab: predicted new indication HER2-positive breast carcinoma (evidence level L5). Approved use: Progressive multiple sclerosis"
monitor_inn: "Ocrelizumab"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer", "benign neoplasm of tongue", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "schwannoma of jugular foramen", "benign neoplasm of buccal mucosa"]
---

# Ocrelizumab
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

# Ocrelizumab: From Progressive Multiple Sclerosis to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody originally used to treat progressive multiple sclerosis.
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**,
but there are currently **0 registered clinical trials** and **0 publications** directly supporting this indication. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Progressive multiple sclerosis (per the knowledge graph; no approved indication text is available from the ARTG entry) |
| Predicted New Indication | HER2-positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ocrelizumab is known to be a humanised anti-CD20 monoclonal antibody that selectively depletes CD20-expressing B cells. Its efficacy in multiple sclerosis is well established.

No mechanistic link between CD20-directed B-cell depletion and HER2-positive breast carcinoma is supported by the data compiled. The high TxGNN score (0.999) reflects a graph-based model signal, not independent evidence. Other breast cancer subtypes (progesterone-receptor positive and negative, luminal A or B, normal breast-like) received near-identical scores. This suggests a shared graph signal across the breast cancer cluster rather than disease-specific evidence.

Other top-ranked predictions include benign head and neck neoplasms, cervical neuroblastoma and jugular foramen schwannoma. None has a supported rationale, and for benign lesions the risk-benefit balance of an immunosuppressive biologic is unfavourable.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

## Literature Evidence

Currently no related literature available for HER2-positive breast carcinoma.

For context, 18 records were retrieved for the related prediction "breast tumour luminal A or B". The ten listed all concern multiple sclerosis or other autoimmune and B-cell topics, and none addresses breast cancer. Examples are the pivotal ocrelizumab trials in primary progressive MS (PMID 28002688) and relapsing MS (PMID 28002679). This match appears to be an artefact of drug-name retrieval and should not be read as support for any oncology indication.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11237K | Ocrevus | Solution concentrate for I.V. infusion, 300 mg in 10 mL | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 entries. The main ones shown are:
  - **Moderate**: corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone), radiopharmaceuticals (iobenguane I-131, ibritumomab tiuxetan, tositumomab, samarium-153 lexidronam), and albendazole, pentamidine and levamisole.
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride).

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on the TxGNN model score. There are no clinical trials, no relevant literature, and no supported mechanistic link between CD20 B-cell depletion and HER2-positive breast carcinoma. Established HER2-directed therapies already exist for this disease.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a defined biological hypothesis linking CD20 or B cells to HER2-positive breast cancer
- Preclinical or translational evidence, then registered clinical studies
- The TGA-approved PI (warnings, contraindications, approved indications) to complete safety screening
- Review of the immunosuppression and infection risks in a cancer population, including interactions with chemotherapy and corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

