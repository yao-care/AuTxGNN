---
layout: default
title: Cabazitaxel
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cabazitaxel: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Cabazitaxel"
predicted_indications: ["female breast carcinoma", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "HIV infectious disease", "hyperthyroidism", "neuroblastoma", "rheumatoid arthritis"]
---

# Cabazitaxel
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

# Cabazitaxel: From Its Registered Use (Indication Not Stated in the Data) to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a taxane chemotherapy drug. The data compiled for this report do not state its approved indication in Australia, although it is widely known as a treatment for metastatic castration-resistant prostate cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**.
Currently there are **no registered clinical trials** in the compiled data, and the **20 publications** are mostly preclinical or review articles, plus one Phase II randomised trial (GENEVIEVE) and one Phase I/II study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (ARTG indication text is empty) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical and mechanism studies; no completed Phase 3 trials) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Cabazitaxel belongs to the taxane class, which stabilises microtubules and blocks cell division. Paclitaxel and docetaxel, which share this mechanism, are established treatments in breast cancer.

Cabazitaxel has a lower affinity for P-glycoprotein than the older taxanes. The literature suggests it may therefore keep some activity in taxane-resistant tumours. For example, a resistance study in MCF-7 breast cancer cell models found it was less cross-resistant than paclitaxel and docetaxel.

Most supporting publications are laboratory studies of nanoformulations (lipospheres, lipid carriers, nanoparticles, micelles) in breast cancer cell lines or xenografts. Two clinical studies are relevant: the GENEVIEVE Phase II trial, which compared cabazitaxel with paclitaxel in the neoadjuvant setting, and a Phase I/II study combining it with capecitabine in metastatic breast cancer. The evidence is therefore indirect and largely preclinical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the data compiled for this report.

Two published clinical studies are listed in the literature table below (GENEVIEVE and the cabazitaxel plus capecitabine Phase I/II study).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | Eur J Cancer | GENEVIEVE: cabazitaxel vs weekly paclitaxel as neoadjuvant treatment in HER2-negative (triple-negative or luminal B) breast cancer, comparing pathological complete response |
| [38663168](https://pubmed.ncbi.nlm.nih.gov/38663168/) | 2024 | Phase II RCT (long-term follow-up) | ESMO Open | Long-term outcomes of GENEVIEVE; the earlier report noted differences in pCR rates between arms |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | Eur J Cancer | Dose-escalation of cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline and taxane treatment |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review/preclinical | Mol Cancer Ther | Resistance mechanisms; cabazitaxel less cross-resistant than paclitaxel and docetaxel in resistant models, including MCF-7 variants |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs Today | Cabazitaxel's pharmacokinetic and safety profile; neutropenia and neuropathy are the main toxicities |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | J Immunother Cancer | Cabazitaxel's effect on macrophages improves CD47-targeted immunotherapy in triple-negative breast cancer models |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | J Control Release | Nanoparticle-encapsulated cabazitaxel gave complete remission in 6 of 8 patient-derived breast cancer xenograft tumours |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chem Phys Lipids | Cabazitaxel and thymoquinone co-loaded lipospheres for breast cancer |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclinical | Colloids Surf B | Cabazitaxel-loaded lipid carriers evaluated against breast cancer cell lines |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclinical | Acta Pharmacol Sin | Cabazitaxel-loaded polymeric micelles in breast cancer metastasis models |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4376H | Cabazitaxel Juno | Concentrated injection 60 mg in 1.5 mL, with diluent | Not stated in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule-stabilising) |
| Myelosuppression Risk | High (neutropenia is a leading toxicity in the literature; the knowledge graph also links the drug to leukopenia, thrombocytopenia and anaemia) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential, liver function and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, leukopenia, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome) and pyoureter. These come from a graph of drug-disease contraindications, so verify them against the approved label.
- **Drug Interactions:** 100 interactions were identified. Major-level ones in the displayed list include **deferiprone** and **samarium (153Sm) lexidronam**, both of which add to bone marrow suppression. Moderate-level ones include:
  - Aprepitant, clarithromycin, cobicistat and the azole antifungals (clotrimazole, miconazole), which may affect cytochrome P450 (CYP3A) metabolism
  - Metronidazole and tinidazole
  - Rosuvastatin and simvastatin
  - Ticagrelor
  - Deferasirox
  - Chloroquine
  - Disulfiram

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The breast cancer prediction is mechanistically plausible, since taxanes are established in this disease. However, the supporting evidence is mainly preclinical, with one Phase II neoadjuvant trial and one Phase I/II study. There is no completed Phase 3 evidence and no registered trials in the compiled data. This is a research question rather than a clinical recommendation.

**To proceed, the following is needed:**
- The approved indication text from the TGA Product Information, which is missing from the ARTG record
- The Product Information warnings and contraindications, which are required for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A review of the GENEVIEVE results (pCR and long-term outcomes) and an assessment of how they apply in Australian practice
- A search of ClinicalTrials.gov and ANZCTR for current cabazitaxel breast cancer trials
- A comparison with the established taxanes (paclitaxel, docetaxel) in breast cancer, including toxicity, cost and funding considerations

---

*Note: The other nine predictions in the data (for example sickle cell syndromes, HIV infection, hyperthyroidism, neuroblastoma and rheumatoid arthritis) have no trials or literature and no clear mechanistic rationale. They are all at Evidence Level L5 with a Hold recommendation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

