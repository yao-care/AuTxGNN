---
layout: default
title: Pazopanib
parent: Model Prediction Only (L5)
nav_order: 550
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Pazopanib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
description: "Pazopanib: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Pazopanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Pazopanib: Liposarcoma
{: .text-alpha }

*Note: The report follows the first-ranked prediction (Xp11.2/TFE3 translocation RCC), which has no supporting evidence. The most evidence-supported predictions are summarised below. Unclassified renal cell carcinoma (rank 3) is the best-supported renal prediction, and liposarcoma (rank 4) and dermatofibrosarcoma protuberans (rank 10) are the best-supported sarcoma predictions.*

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor originally used for renal cell carcinoma and soft tissue sarcoma.
The TxGNN model ranks **liposarcoma** first (score 0.9959), but this prediction has **no clinical trials and no publications**.
The best-supported predictions are **liposarcoma** (6 clinical trials, 20 publications) and **unclassified renal cell carcinoma** (6 publications, no registered trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 (rank 1). Rank 3 (unclassified RCC): L3. Rank 4 (liposarcoma): L2. Rank 10 (DFSP): L2 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold (rank 1). Proceed with Guardrails for liposarcoma; Research Question for unclassified RCC, fibroblastic neoplasm and DFSP |

### Summary of the Top Ten Predictions

| Rank | Predicted Indication | Score | Trials | Publications | Evidence Level | Recommendation |
|---|---|---|---|---|---|---|
| 4 | Liposarcoma | 0.9959 | 6 | 20 | L2 | Proceed with Guardrails |
| 6 | Ovarian myxoid liposarcoma | 0.9951 | 0 | 0 | L5 | Hold |
| 7 | Heart fibrosarcoma | 0.9937 | 0 | 0 | L5 | Hold |
| 8 | Fibroblastic neoplasm | 0.9935 | 2 | 20 | L5 | Research Question |
| 9 | Kidney fibrosarcoma | 0.9933 | 0 | 0 | L5 | Hold |
| 10 | Dermatofibrosarcoma protuberans | 0.9929 | 4 | 13 | L2 | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pazopanib is a multi-target inhibitor of VEGFR1-3, PDGFR and c-KIT. It is already used in renal cell carcinoma and soft tissue sarcoma, and it may be mechanistically applicable to related tumours that depend on angiogenesis and PDGFR signalling.

For the top-ranked predictions, the high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They are not backed by trial or publication data.

Predictions with more support follow the same angiogenesis and PDGFR logic:
- **Unclassified RCC:** non-clear-cell histologies share some VEGF-pathway dependence, though less than clear-cell disease. Retrospective series, real-world data and a single-arm Phase 2 study suggest activity.
- **Liposarcoma:** this subtype was excluded from the pivotal soft tissue sarcoma approval because of lack of benefit in the adipocytic group, and dedicated Phase 2 studies showed modest results.
- **Dermatofibrosarcoma protuberans (DFSP):** the COL1A1-PDGFB fusion drives constitutive PDGFRB activation, which pazopanib inhibits. It is most relevant after imatinib resistance.
- **Fibroblastic neoplasms:** there is plausibility from solitary fibrous tumour data, but the evidence is heterogeneous.

## Clinical Trial Evidence

**Rank 1 (Xp11.2/TFE3 translocation RCC):** Currently no related clinical trials registered.

**Rank 3 (unclassified RCC):** Currently no related clinical trials registered.

**Rank 4 (liposarcoma):**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable or metastatic liposarcoma (direct evidence) |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Activity and tolerability in advanced or metastatic liposarcoma after standard therapies |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomised, double-blind gemcitabine with or without pazopanib in refractory soft tissue sarcoma (mixed population) |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib plus oral topotecan in metastatic soft tissue and bone sarcomas (mixed population) |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Completed | 140 | Neoadjuvant radiation or chemoradiation with or without pazopanib in non-rhabdomyosarcoma soft tissue sarcoma (indirect relevance) |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Risk-adapted regimen with maintenance pazopanib in non-rhabdomyosarcoma soft tissue sarcoma (limited relevance) |

**Rank 10 (DFSP):**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Phase 2 | Terminated | 23 | Pazopanib in unresectable locally advanced DFSP (direct but underpowered) |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | Phase 1/2 | Terminated | 151 | MLN0128 versus pazopanib in advanced sarcoma (pazopanib as comparator) |

**Rank 8 (fibroblastic neoplasm):** [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) is a Phase 2 single-agent study (n=96, completed) in solitary fibrous tumour and extraskeletal myxoid chondrosarcoma.

No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

**Rank 3 (unclassified RCC):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 (single-arm) | Cancer Res Treat | Efficacy and safety of pazopanib in non-clear-cell RCC |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | PANORAMA: first-line pazopanib in non-clear-cell RCC (Italy) |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Outcomes of metastatic non-clear-cell RCC treated with pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world study | Ecancermedicalscience | Sunitinib versus pazopanib in non-clear-cell and sarcomatoid RCC |

**Rank 4 (liposarcoma), selected:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 report/review | Expert Opin Investig Drugs | Pazopanib in intermediate- or high-grade advanced liposarcoma |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Commentary | Lancet Oncol | Pazopanib for advanced liposarcoma |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | Established and experimental systemic options for advanced liposarcoma |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Curr Treat Options Oncol | Systemic therapy for dedifferentiated liposarcoma |

**Rank 10 (DFSP), selected:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Phase 2 | J Invest Dermatol | Multicentre Phase 2 of pazopanib in unresectable DFSP |
| [34066400](https://pubmed.ncbi.nlm.nih.gov/34066400/) | 2021 | Retrospective | Cancers | Neoadjuvant imatinib or pazopanib followed by surgery in locally advanced DFSP |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Preclinical | Cancer Sci | Pazopanib identified as a potential inhibitor of the COL1A1-PDGFB fusion |

**Rank 8 (fibroblastic neoplasm), selected:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25269954](https://pubmed.ncbi.nlm.nih.gov/25269954/) | 2014 | Preclinical and clinical | Eur J Cancer | Activity of pazopanib in solitary fibrous tumour |
| [38759389](https://pubmed.ncbi.nlm.nih.gov/38759389/) | 2024 | Real-world | Eur J Cancer | Pazopanib and sorafenib in desmoid tumours (CanSaRCC) |

**Rank 1:** Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 10041L | Votrient | Tablet 400 mg (as hydrochloride) | Not available in the data compiled for this report |

The data compiled for this report did not include an ARTG number in the standard format, so the licence number is shown as supplied.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions |
| Monitoring Items | Please refer to the PI; liver function, blood pressure and haematological parameters are generally monitored |
| Handling Protection | Please refer to the PI and local institutional policy |

## Safety Considerations

**Contraindication signals (knowledge graph, not label text):** The knowledge graph links pazopanib with the following conditions:
- Cardiovascular: hypertension, long QT syndrome, torsades de pointes, myocardial infarction
- Hepatic: liver failure, drug-induced liver injury, hyperbilirubinaemia, Gilbert syndrome
- Gastrointestinal: active peptic ulcer disease, pancreatitis, diarrhoeal disease
- Other: intracerebral haemorrhage, proteinuria, hypothyroidism, electrolyte disturbances (potassium, calcium, phosphorus)

These are not confirmed label contraindications.

**Drug Interactions:** 100 interactions were recorded. Those listed include:
- **Major:** acid-suppressing agents (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), clarithromycin and dolasetron
- **Moderate:** pioglitazone, loperamide, aprepitant, dexamethasone, budesonide, bisacodyl, magnesium oxide, saxagliptin, eliglustat and polyethylene glycol

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (Xp11.2/TFE3 RCC). Proceed with Guardrails for liposarcoma.**

**Rationale:**
- The top-ranked renal predictions have no trials or publications, so the high TxGNN scores reflect only proximity to the approved RCC indication.
- Liposarcoma has several completed Phase 2 trials but modest efficacy. Unclassified RCC, fibroblastic neoplasm and DFSP are research questions supported by small or mixed-population studies.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- The approved indication text and TGA Product Information safety content (warnings, contraindications)
- Targeted literature review for Xp11.2/TFE3 translocation RCC
- Prospective or larger studies in non-clear-cell RCC and DFSP, with results from the dedicated liposarcoma trials reviewed in full
- Safety monitoring plan for the hepatic, cardiovascular (QT, hypertension) and interaction risks noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

