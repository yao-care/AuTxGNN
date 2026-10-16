---
layout: default
title: Vemurafenib
parent: Model Prediction Only (L5)
nav_order: 773
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vemurafenib: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not available in the compiled data"
---

# Vemurafenib
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

# Vemurafenib: From Its Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Vemurafenib is an oral BRAF kinase inhibitor, and its original approved indication is not recorded in the data compiled for this report.
The TxGNN model's top-ranked prediction is HIV infectious disease, which has no supporting evidence. The only prediction with any supporting literature is **Female Breast Carcinoma** (rank 8), which has **1 withdrawn clinical trial (0 enrolled)** and **17 publications**, none of which show efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the ARTG entry has no indication text) |
| Predicted New Indication | HIV infectious disease (TxGNN rank 1); Female breast carcinoma (rank 8) is the only prediction with supporting material and is discussed below |
| TxGNN Prediction Score | HIV infectious disease: 97.65%; Female breast carcinoma: 95.15% |
| Evidence Level | L5 for HIV infectious disease; L4 for female breast carcinoma |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (overall); breast carcinoma is a research question only |

**Note on prediction selection:** Of the 10 predictions, 9 have no clinical trials or literature at all (L5, Hold). Because the top-ranked prediction has no evidence, this report focuses on female breast carcinoma, the only prediction with any evidence, while summarising the others.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Vemurafenib is generally known as a BRAF V600E kinase inhibitor, so any rationale rests on that background knowledge rather than on data supplied here.

**Breast carcinoma:** BRAF V600E mutations occur in a small subset of breast cancers, including rare triple-negative cases (a case report, PMID 34818649). BRAF/MAPK inhibition is therefore mechanistically plausible in a mutation-selected niche. However, the evidence is limited to case reports and reviews. One case report describes **vemurafenib-induced progression** of breast cancer (PMID 26264150), which raises a paradoxical MAPK activation concern in BRAF wild-type tumours.

**Other predictions:** No plausible link is evident for the remaining predictions.
- HIV infectious disease, feline acquired immunodeficiency syndrome and simian immunodeficiency virus infection: no BRAF-related link to viral pathophysiology is apparent. The veterinary and animal-model scores likely mirror the HIV prediction.
- Acute intermittent porphyria: vemurafenib is associated with phototoxicity, which argues for caution.
- Paratenonitis: the prediction may reflect known musculoskeletal side effects rather than therapeutic potential.
- Neurodevelopmental disorder, collagenopathy, calcific tendinitis and lymphocytic hypereosinophilic syndrome: predictions only, with no supporting data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05238831](https://clinicaltrials.gov/study/NCT05238831) | Early Phase 1 | Withdrawn | 0 | SMMART-ACT, a feasibility pilot of precision-medicine drug selection for individual cancers. Withdrawn with no participants, so it provides no efficacy or safety data. |

No ANZCTR trials were identified in the compiled data.

---

## Literature Evidence

Only the publications directly relevant to vemurafenib or breast cancer are listed. Several retrieved papers concern melanoma or are unrelated.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26264150](https://pubmed.ncbi.nlm.nih.gov/26264150/) | 2016 | Case report/Review | Targeted Oncology | A patient given vemurafenib for BRAF-mutant melanoma had progression of concurrent breast cancer, a paradoxical MAPK activation safety signal |
| [34818649](https://pubmed.ncbi.nlm.nih.gov/34818649/) | 2022 | Case report/Review | Oncology Research and Treatment | BRAF V600E mutation in triple-negative breast cancer; no evidence of vemurafenib efficacy in BRAF V600E-mutant breast cancer had been reported |
| [33896802](https://pubmed.ncbi.nlm.nih.gov/33896802/) | 2021 | Review | Breast Disease | Overview of FDA-approved drugs targeting the MAPK pathway in breast cancer |
| [40234093](https://pubmed.ncbi.nlm.nih.gov/40234093/) | 2025 | Clinical study | J Immunother Cancer | NeoACTIVATE: neoadjuvant cobimetinib and atezolizumab with or without vemurafenib in stage III **melanoma** (not breast) |
| [32103736](https://pubmed.ncbi.nlm.nih.gov/32103736/) | 2020 | Pooled trial analysis | BMC Cancer | Risk factors for severe rash with vemurafenib alone or with cobimetinib in melanoma |
| [32546073](https://pubmed.ncbi.nlm.nih.gov/32546073/) | 2021 | Retrospective case series | Ocul Immunol Inflamm | Uveitis induced by cancer biologics, including three vemurafenib-treated patients |
| [28614138](https://pubmed.ncbi.nlm.nih.gov/28614138/) | 2019 | Case report | Retin Cases Brief Rep | Exudative polymorphous vitelliform maculopathy during vemurafenib and pembrolizumab treatment |

There are no RCTs. No publication demonstrates efficacy of vemurafenib in breast cancer.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11076Y | Zelboraf | Tablet 240 mg (oral) | Not recorded in the compiled data |

---

## Cytotoxicity

Vemurafenib is an antineoplastic, targeted-therapy BRAF inhibitor rather than a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. The compiled data and literature point to dermatological and ocular monitoring (rash, uveitis) and ECG/electrolyte monitoring (QT-related). |
| Handling Protection | Please refer to the PI and local institutional policy |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (model-derived drug-disease links, not label text):
- Cardiac and electrolyte: long QT syndrome (including familial), torsades de pointes, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease
- Hepatic: hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome
- Ocular: uveitis, iris disease, ciliary body disease, panuveitis, iritis

The ocular signal is consistent with published reports of vemurafenib-associated uveitis (PMID 32546073).

**Drug interactions:** 100 interactions were identified. Those listed as Major:
- Clarithromycin
- Dolasetron
- Palonosetron

Moderate-level examples include famotidine, pioglitazone, dexamethasone, aprepitant, loperamide, sitagliptin, saxagliptin, linagliptin, naltrexone and several bowel-preparation agents. Many of the QT-relevant combinations are particularly relevant given the knowledge-graph QT signals.

**Disease-specific concern:** One case report describes vemurafenib-induced progression of breast cancer (PMID 26264150).

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Nine of the ten predictions have no clinical trials or literature (L5), and the top-ranked prediction (HIV) has no plausible mechanistic link.
- Female breast carcinoma (L4) has only case reports and reviews, a withdrawn trial with no enrolment, and a paradoxical-progression safety signal. It should be treated as a research question limited to biomarker-selected (BRAF V600E) disease.

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the TGA Product Information, and the approved indication text for the ARTG entry
- Mechanism of action data
- For breast cancer: prospective evidence in BRAF V600E-mutant breast cancer, with clear exclusion of BRAF wild-type disease because of paradoxical MAPK activation
- A cardiac (QT), ocular and dermatological safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

