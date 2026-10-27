---
layout: default
title: Nusinersen
parent: Model Prediction Only (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nusinersen: predicted new indication Fallopian tube serous adenofibroma (evidence level L5). Approved use: Spinal muscular atrophy"
monitor_inn: "Nusinersen"
predicted_indications: ["fallopian tube serous adenofibroma", "pancreatic vasoactive intestinal peptide producing tumor", "salpingitis", "external ear squamous cell carcinoma", "isolated mesenteric vein thrombosis", "isolated splenic vein thrombosis", "epithelioid cell synovial sarcoma", "cellular ependymoma", "biphasic synovial sarcoma", "thymus squamous cell carcinoma"]
---

# Nusinersen
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

## Nusinersen: From Spinal Muscular Atrophy to Fallopian Tube Serous Adenofibroma
{: .text-alpha }

## One-Sentence Summary

Nusinersen is an antisense oligonucleotide originally used to treat spinal muscular atrophy (SMA).
The TxGNN model's top-ranked prediction is **fallopian tube serous adenofibroma**, but the score is neutral (50%), and there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model output without supporting evidence and should not be treated as a meaningful repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (the ARTG entry has no approved indication text; the indication is taken from the knowledge-graph data compiled for this report) |
| Predicted New Indication | Fallopian tube serous adenofibroma |
| TxGNN Prediction Score | 50.00% (neutral midpoint, uninformative) |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, nusinersen is an antisense oligonucleotide that modulates SMN2 pre-mRNA splicing to increase functional SMN protein, which is the basis for its use in SMA.

No mechanistic link to fallopian tube serous adenofibroma (a benign tumour) has been identified. There is no known SMN-dependent pathology in this condition. The TxGNN score of 0.5 sits at the neutral midpoint and carries no predictive information. Similarity to the original indication has not been assessed.

The other nine predictions in the top ten are also at a neutral score of 0.5, with no trials or literature and no plausible mechanistic link:

- Pancreatic VIP-producing tumour
- Salpingitis
- External ear squamous cell carcinoma
- Isolated mesenteric vein thrombosis
- Isolated splenic vein thrombosis
- Epithelioid cell synovial sarcoma
- Cellular ependymoma
- Biphasic synovial sarcoma
- Thymus squamous cell carcinoma

The thrombosis predictions are of particular concern. Coagulation-related warnings are recognised with nusinersen, which argues against, rather than for, its use in thrombotic conditions. For ependymoma, central nervous system delivery (intrathecal administration) alone is not a rationale, as the tumour biology is unrelated to SMN protein restoration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11363C | Spinraza | Solution for injection 12 mg in 5 mL | Not available in the data compiled for this report |

The only available route is injectable. The required route for the predicted indication has not been assessed.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

The data compiled for this report did not include warnings, contraindications or drug interaction findings, so the absence of listed items should not be read as an absence of risk. Coagulation abnormalities and thrombocytopenia are recognised concerns with nusinersen and are relevant to any proposed use in thrombotic conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions score a neutral 0.5, have no clinical trials or literature, and have no plausible mechanistic link to nusinersen's SMN2 splice-modulating action. Evidence is at L5 (model prediction only), and there is no basis to advance any of them.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Product Information warnings and contraindications for the Australian product (currently a blocking gap for safety screening)
- A credible biological rationale for the predicted indication, ideally supported by preclinical or observational evidence
- A re-run or independent validation of the prediction, since a score of 0.5 carries no information
- Assessment of route compatibility and similarity to the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

