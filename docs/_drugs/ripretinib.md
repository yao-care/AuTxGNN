---
layout: default
title: Ripretinib
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ripretinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not stated in the ARTG data compiled for this report. The literature…"
---

# Ripretinib
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

# Ripretinib: From Its Approved Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib is an oral switch-control tyrosine kinase inhibitor that targets KIT and PDGFRA. It is marketed in Australia as Qinlock, and the published literature links it to advanced gastrointestinal stromal tumour (GIST).
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **no clinical trials and no publications** currently support this prediction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report. The literature describes ripretinib as used in advanced GIST. |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, ripretinib is a switch-control kinase inhibitor that blocks both primary and secondary activating mutations of KIT and PDGFRA. These mutations drive GIST progression.

No link to multiple endocrine neoplasia (MEN) has been established. MEN syndromes are mainly driven by other genes, such as RET and MEN1, and no RET-directed activity of ripretinib is documented. The high TxGNN score (0.988) reflects graph-based proximity only. The prediction should be regarded as a hypothesis, not as evidence of benefit.

Other high-ranking TxGNN predictions for this drug include HER2-positive breast carcinoma, several breast cancer subtypes, cytomegalovirus infection, amenorrhoea, and two veterinary diseases (infectious bovine rhinotracheitis and malignant catarrh). None has supporting trials or a plausible mechanistic rationale, and the veterinary entries are probably knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

The publications retrieved for ripretinib in other predicted indications (breast cancer subtypes) all concern its existing use in GIST, pharmacokinetics or general kinase inhibitor reviews. They do not support a repurposing indication. Examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38182785](https://pubmed.ncbi.nlm.nih.gov/38182785/) | 2024 | Phase 3 RCT biomarker analysis | Nature Medicine | INTRIGUE trial ctDNA analysis in GIST. Ripretinib was not superior to sunitinib for progression-free survival in the primary analysis. |
| [34313371](https://pubmed.ncbi.nlm.nih.gov/34313371/) | 2021 | Post-hoc trial analysis | The Oncologist | INVICTUS study: clinical benefit of ripretinib dose escalation after progression in advanced GIST. |
| [38473346](https://pubmed.ncbi.nlm.nih.gov/38473346/) | 2024 | Cohort study | Cancers | UK expanded access programme: efficacy and safety of ripretinib in advanced GIST. |
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | Overview of FDA-approved small molecule kinase inhibitors. Contains no breast cancer efficacy data for ripretinib. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12764T | Qinlock | Tablet 50 mg | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions, and local cytotoxic drug handling policy |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Drug Interactions:** The interaction screen identified 90 potential interactions. Those flagged as **Major** among the first 20 entries reviewed are:
- Clarithromycin
- Cobicistat

Moderate-level interactions include pioglitazone, aprepitant, dexamethasone, canagliflozin, cimetidine, eliglustat, metreleptin, miconazole, repaglinide, clotrimazole, fidaxomicin, glycerol phenylbutyrate, rolapitant, rosiglitazone, troglitazone, deferasirox, fostamatinib and selexipag. Pharmacokinetic studies in the literature (verapamil in rats, and a physiologically-based pharmacokinetic model) also indicate that CYP3A4 and P-glycoprotein modulators can alter ripretinib exposure.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for multiple endocrine neoplasia is supported by model output only (L5). There are no trials, no relevant publications and no documented mechanistic link. The same applies to the other top-ranked predictions.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and an analysis of any plausible link to MEN-related pathways such as RET
- Preclinical evidence (in vitro or in vivo) in MEN-relevant models
- The TGA-approved Product Information, to confirm the approved indication and obtain warnings and contraindications
- Review of the full 90-item interaction list, with attention to CYP3A4 modulators
- Expert review of whether the prediction is clinically meaningful, given the rarity and genetic basis of MEN syndromes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

