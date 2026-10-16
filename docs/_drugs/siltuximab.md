---
layout: default
title: Siltuximab
parent: Model Prediction Only (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Siltuximab: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Castleman disease"
---

# Siltuximab
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

# Siltuximab: From Castleman Disease to Extracutaneous Mastocytoma

## One-Sentence Summary

Siltuximab is an anti-interleukin-6 (IL-6) antibody, originally used to treat Castleman disease.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Castleman disease (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, siltuximab is a monoclonal antibody that neutralises IL-6. Its efficacy in Castleman disease, a disorder driven by dysregulated IL-6 production, has been demonstrated.

IL-6 can contribute to mast cell biology, so a mechanistic link to mast cell tumours is conceivable. However, this link is speculative. No trial or literature was identified to test it, and the prediction rests only on the TxGNN score.

**Other predictions worth noting.** The model also ranked other diseases for siltuximab. Two have more supporting evidence than the top-ranked prediction:
- **TAFRO syndrome** (score 98.79%, evidence level L4): a variant of idiopathic multicentric Castleman disease with cytokine-storm features, which supports biological plausibility. Direct evidence is limited to case reports and consensus guidance. The pivotal Phase 2 RCT was in multicentric Castleman disease, not TAFRO, and TAFRO patients often respond poorly to siltuximab.
- **Kaposi's sarcoma** (score 99.28%, evidence level L4): KSHV encodes a viral IL-6 homologue, and KSHV-associated multicentric Castleman disease is closely related. The only retrieved paper is a general Castleman review, so there is no direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for extracutaneous mastocytoma.

## Literature Evidence

Currently no related literature available for extracutaneous mastocytoma.

For context, the literature retrieved for the related Castleman disease and TAFRO syndrome predictions includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25042199](https://pubmed.ncbi.nlm.nih.gov/25042199/) | 2014 | RCT | Lancet Oncol | Randomised, double-blind, placebo-controlled Phase 2 trial of siltuximab in HIV-negative multicentric Castleman disease |
| [30181172](https://pubmed.ncbi.nlm.nih.gov/30181172/) | 2018 | Guideline/Consensus | Blood | International evidence-based consensus treatment guidelines for idiopathic multicentric Castleman disease |
| [35793409](https://pubmed.ncbi.nlm.nih.gov/35793409/) | 2022 | Post hoc analysis of RCT | Blood Adv | Siltuximab associated with improved progression-free survival in idiopathic multicentric Castleman disease |
| [35770616](https://pubmed.ncbi.nlm.nih.gov/35770616/) | 2022 | Systematic review | Eur J Haematol | Efficacy and safety of regimens for multicentric Castleman disease; siltuximab response rate below 50% |
| [36652167](https://pubmed.ncbi.nlm.nih.gov/36652167/) | 2023 | Case report/Review | J Nephrol | Siltuximab monotherapy in TAFRO syndrome |
| [32564425](https://pubmed.ncbi.nlm.nih.gov/32564425/) | 2020 | Case report | Eur J Haematol | Frontline siltuximab and rituximab in TAFRO syndrome |
| [38927484](https://pubmed.ncbi.nlm.nih.gov/38927484/) | 2024 | Review/Guidance | Biomedicines | Guidance for managing TAFRO syndrome |
| [38087716](https://pubmed.ncbi.nlm.nih.gov/38087716/) | 2024 | Review | Blood Rev | Update on diagnosis and treatment of idiopathic multicentric Castleman disease, including approval of siltuximab |
| [36433996](https://pubmed.ncbi.nlm.nih.gov/36433996/) | 2022 | Biomarker study | Nat Commun | CXCL13 as a predictive biomarker; siltuximab is not effective in all iMCD patients |
| [39970477](https://pubmed.ncbi.nlm.nih.gov/39970477/) | 2024 | Review | AIDS Rev | Castleman disease subtypes and aetiologies (relevant to the Kaposi's sarcoma link) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12916T | Sylvant | Powder for injection 100 mg | Not specified in the data compiled for this report |

## Safety Considerations

**Drug Interactions** (100 interactions recorded; the main ones are listed below):
- **Major:** deferiprone
- **Moderate:** simvastatin, apixaban, warfarin, rivaroxaban, dicoumarol, lidocaine, hydrocodone, fentanyl, theophylline, aminophylline, oxtriphylline, roflumilast, tacrolimus, nifedipine, tetanus toxoid vaccine
- **Minor:** zinc salts (sulfate, acetate, gluconate, chloride)

Many of the moderate interactions involve drugs metabolised by cytochrome P450 enzymes, which IL-6 blockade may affect. Review each combination against the Product Information (PI).

For warnings and contraindications, please refer to the TGA-approved Product Information (PI). In immunodeficient patients, IL-6 inhibition could add infection risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The extracutaneous mastocytoma prediction is supported only by a model score, with no trials or literature (evidence level L5). Mast cell disease biology is mainly driven by other pathways, so the link to IL-6 blockade is speculative.

**To proceed, the following is needed:**
- Preclinical or mechanistic studies linking IL-6 signalling to mast cell tumours
- Detailed mechanism of action data and TGA Product Information (warnings and contraindications)
- Confirmation of the approved indication wording for the ARTG entry
- If a repurposing target is pursued, consider TAFRO syndrome or Kaposi's sarcoma first, since both have a clearer IL-6 rationale and some supporting literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

