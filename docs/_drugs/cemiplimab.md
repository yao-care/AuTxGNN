---
layout: default
title: Cemiplimab
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cemiplimab: predicted new indication Gallbladder adenosquamous carcinoma (evidence level L5). Approved use: Squamous cell carcinoma"
monitor_inn: "Cemiplimab"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "external ear basal cell carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
---

# Cemiplimab
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

# Cemiplimab: From Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab (Libtayo) is an anti-PD-1 antibody originally used to treat squamous cell carcinoma, specifically cutaneous squamous cell carcinoma.
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Squamous cell carcinoma (per the knowledge graph; the ARTG indication text was not available in the data compiled for this report) |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Pharmacology data show that cemiplimab is a monoclonal antibody that targets human PD-1 (PDCD1, CD279). It blocks the PD-1/PD-L1 interaction with an IC50 below 1 nM in an ELISA. Blocking this checkpoint can restore T-cell activity against tumour cells. In clinical trials, about 50% of patients with advanced cutaneous squamous cell carcinoma responded to treatment.

The prediction most likely reflects the squamous histology link in the knowledge graph. The squamous component of adenosquamous carcinoma may share some PD-1/PD-L1 biology with cutaneous squamous cell carcinoma. However, biliary tract tumours are generally poorly immunogenic. No trial or literature evidence supports this link, so the prediction should be treated as a hypothesis only.

Other predicted indications were also reviewed. Most are squamous or adenosquamous tumours at other sites (head and neck, lung, anal-rectal transition zone, prostate, pancreas, urethra), and they also have no direct cemiplimab evidence. The one exception is external ear basal cell carcinoma (rank 4), which has a single case report (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered for gallbladder adenosquamous carcinoma.

## Literature Evidence

Currently no related literature available for gallbladder adenosquamous carcinoma.

For context, one publication was identified for a lower-ranked prediction, external ear basal cell carcinoma:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case report | Clin Exp Dermatol | Lasting response after discontinuation of cemiplimab in a patient with locally advanced basal cell carcinoma (abstract not available) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13135H | Libtayo | Solution concentrate for I.V. infusion, 350 mg in 7 mL | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Drug Interactions**: Ten interaction entries were found. Nine are Moderate-level interactions with corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort. The remaining entry is the drug's pharmacological target (PD-1), which is not a drug interaction.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available in the data compiled for this report. Please refer to the PI for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gallbladder adenosquamous carcinoma is supported only by the model score (L5), with no trials or publications. Biliary tract tumours are generally poorly immunogenic, so the link is speculative.

**To proceed, the following is needed:**
- Targeted literature and trial searches for cemiplimab or PD-1 blockade in adenosquamous biliary tumours
- Detailed mechanism of action data, and the ARTG approved indication text
- TGA Product Information warnings and contraindications for safety screening
- Review of the external ear basal cell carcinoma lead (rank 4) against the approved label and pivotal trial data, as a possible better-supported research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

