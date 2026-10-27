---
layout: default
title: Dostarlimab
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dostarlimab: predicted new indication X-linked intellectual disability-epilepsy syndrome (evidence level L5). Approved use: Not available in the data compiled for this report . Overseas…"
monitor_inn: "Dostarlimab"
predicted_indications: ["X-linked intellectual disability-epilepsy syndrome", "balanoposthitis", "acquired amyloid peripheral neuropathy", "peripheral neuropathy associated with monoclonal gammopathy", "systemic inflammatory disease associated with an acquired peripheral neuropathy", "polyradiculoneuropathy associated with IgG/IgA/IgM monoclonal gammopathy", "cutis laxa", "transient global amnesia (disease)", "cryopyrin-associated periodic syndrome", "optic pathway glioma"]
---

# Dostarlimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Dostarlimab: From Oncology Use (Original Indication Not Recorded) to X-linked Intellectual Disability-Epilepsy Syndrome
{: .text-alpha }

## One-Sentence Summary

Dostarlimab (Jemperli) is a PD-1 blocking antibody used in cancer immunotherapy. The data compiled for this report did not record an approved indication for the Australian product.
The TxGNN model's top-ranked prediction is **X-linked intellectual disability-epilepsy syndrome**, but the score is a neutral 0.5 and there are **0 clinical trials** and **0 publications** supporting it.
This prediction is not supported by evidence, and the same applies to all ten predictions reviewed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG indication text is empty). Overseas, dostarlimab is approved for mismatch repair deficient (dMMR) endometrial cancer and other dMMR solid tumours |
| Predicted New Indication | X-linked intellectual disability-epilepsy syndrome |
| TxGNN Prediction Score | 50.00% (neutral, uninformative) |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled drug record. From the pharmacology data, dostarlimab is an antibody that binds human PD-1 (PDCD1, CD279) with high affinity and blocks its interaction with both PD-L1 and PD-L2. This restores T-cell anti-tumour activity.

The prediction is **not mechanistically reasonable** on current information. X-linked intellectual disability-epilepsy syndrome is a monogenic neurodevelopmental disorder with no established immune checkpoint component. A TxGNN score of 0.5 carries no information, and no trials or literature support the link.

The other nine predictions reviewed (all also scored 0.5, all L5) fare no better:

| Rank | Predicted Disease | Assessment |
|------|------|------|
| 2 | Balanoposthitis | No plausible link; immune activation could worsen inflammation |
| 3 | Acquired amyloid peripheral neuropathy | PD-1 blockade does not affect amyloid; checkpoint inhibitors can cause neuropathy |
| 4 | Peripheral neuropathy with monoclonal gammopathy | Speculative link via plasma cell clone; limited efficacy of PD-1 blockade and risk of immune-mediated neuropathy |
| 5 | Systemic inflammatory disease with acquired peripheral neuropathy | Immunostimulation is opposite to what is needed |
| 6 | Polyradiculoneuropathy with monoclonal gammopathy | Checkpoint inhibitors are linked to Guillain-Barré-like events; harm likely exceeds benefit |
| 7 | Cutis laxa | No link to elastic fibre formation |
| 8 | Transient global amnesia | No plausible role |
| 9 | Cryopyrin-associated periodic syndrome | Driven by NLRP3/IL-1β; effective approved therapies exist; could worsen autoinflammation |
| 10 | Optic pathway glioma | Only loosely plausible oncology rationale, but low mutational burden, no MMR-deficiency rationale and risk of inflammatory optic pathway damage |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14109N | Jemperli | Solution concentrate for I.V. infusion 500 mg in 10 mL | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

Points from the mechanism-based review of the predictions:
- **Immune-related adverse events**: Checkpoint inhibitors can cause immune-mediated neuropathy, including Guillain-Barré-like polyradiculoneuropathy. This is particularly relevant to several predicted neurological indications.
- **Immune activation**: Enhanced immune activity could worsen inflammatory or autoinflammatory conditions.
- **Drug interactions**: The only interaction record is the pharmacological target (PD-1, PDCD1). No drug-drug interactions with a graded severity level were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions have a neutral TxGNN score of 0.5, no clinical trials, no literature and no credible mechanistic link. Several carry a plausible safety risk from immune activation.

**To proceed, the following is needed:**
- Retrieval of the Jemperli Product Information (warnings and contraindications), which is currently a blocking data gap
- Approved indication text for ARTG 14109N
- Detailed mechanism of action data from DrugBank
- New biological evidence for any specific candidate (optic pathway glioma is the only one with a loosely plausible oncology rationale) before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

