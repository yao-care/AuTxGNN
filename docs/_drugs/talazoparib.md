---
layout: default
title: Talazoparib
parent: Model Prediction Only (L5)
nav_order: 698
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Talazoparib: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Not stated in the ARTG data compiled for this report (the indication…"
monitor_inn: "Talazoparib"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "primary release disorder of platelets", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Talazoparib
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

# Talazoparib: From Breast Cancer (Germline BRCA-Mutated, HER2-Negative) to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Talazoparib is an oral PARP inhibitor registered in Australia as Talzenna and, according to the data compiled for this report, is used in germline BRCA-mutated, HER2-negative breast cancer. The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, with **6 registered clinical trials** and **14 publications** retrieved. None of these studies directly tests talazoparib in HER2-positive disease, so the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (the indication text is blank). The published approved use is germline BRCA-mutated, HER2-negative locally advanced or metastatic breast cancer. |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L5 under the rules in this report (no completed Phase 3 RCT, observational study or systematic review specific to this indication). The upstream scoring recorded L2, but the trials listed are small Phase 1/2 studies in other breast cancer subtypes. |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, talazoparib is a PARP inhibitor with strong PARP-trapping activity. It exploits homologous recombination deficiency, such as germline BRCA1/2 mutations, through synthetic lethality.

Its benefit in breast cancer is tied to BRCA/HRD status rather than HER2 status. The approved use is in HER2-negative disease, so the original and predicted indications are both breast cancer but are biologically distinct subtypes. Any benefit in HER2-positive disease would most likely be limited to patients with BRCA-mutated or HRD-positive tumours. Combination strategies, for example with the PI3K/mTOR inhibitor gedatolisib, may extend the rationale, but these have been tested only in HER2-negative disease.

The high TxGNN score likely reflects general similarity between breast cancer subtypes in the knowledge graph, rather than HER2-specific evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | ctDNA-guided early treatment switch in metastatic breast cancer. Talazoparib's role is unclear and no HER2-positive link is established. |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Active, not recruiting | 29 | Pharmacodynamics-driven talazoparib trial in advanced solid tumours with DNA damage response gene aberrations. Not HER2-positive specific. |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY neoadjuvant platform trial across multiple arms and breast cancer subtypes. Talazoparib-specific HER2-positive evidence is indirect. |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib plus talazoparib in triple-negative or BRCA1/2-positive, HER2-negative breast cancer. Supports the PARP mechanism in breast cancer, not HER2-positive disease. |
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | Single-arm neoadjuvant talazoparib in germline BRCA1/2 HER2-negative early breast cancer. Terminated, so data are limited. |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 plus talazoparib in triple-negative or hormone-resistant, HER2-negative metastatic breast cancer. Supports safety and feasibility only. |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | Meta-analysis | Breast | GRADE recommendations for PARP inhibitors (olaparib, talazoparib) in BRCA1/2-related advanced HER2-negative breast cancer, based on the OlympiAd and EMBRACA trials. |
| [36202026](https://pubmed.ncbi.nlm.nih.gov/36202026/) | 2022 | Meta-analysis | Cancer Treat Rev | Bayesian network meta-analyses to establish treatment sequencing in metastatic triple-negative breast cancer. |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase I/II trial | Breast Cancer Res Treat | Gedatolisib plus talazoparib in advanced triple-negative or BRCA1/2-positive, HER2-negative breast cancer. |
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | Cohort (retrospective) | Front Immunol | Titled as a comparison of talazoparib with conventional chemotherapy in HER2-positive breast cancer. The available abstract text refers to HER2-negative advanced breast cancer, so its relevance and findings should be verified against the full paper. |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | Cohort (real-world) | Oncologist | Real-world characteristics and outcomes of talazoparib-treated patients with gBRCA-mutated, HER2-negative advanced breast cancer. |
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | Review (guideline) | J Clin Oncol | ASCO guideline update for HR-positive, HER2-negative metastatic breast cancer. |
| [35343197](https://pubmed.ncbi.nlm.nih.gov/35343197/) | 2022 | Review | Indian J Cancer | Role of PARP inhibitors in HER2-negative metastatic breast cancer. |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | Review | Oncology (Williston Park) | Immunotherapy and antibody-drug conjugates in metastatic triple-negative breast cancer. |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | Cohort | Mol Diagn Ther | Clinical actionability of molecular targets, including PARP inhibitors, in multi-ethnic breast cancer patients. |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | Real-world cohort | Clin Breast Cancer | Mayo Clinic real-world outcomes, toxicities and prescribing patterns of PARP inhibitors in metastatic breast cancer. |

Most of this literature concerns HER2-negative or triple-negative disease. None provides prospective evidence for talazoparib in HER2-positive breast cancer.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14683T | Talzenna | Capsule 500 micrograms (as tosilate) | Not recorded in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor with PARP-trapping activity) |
| Myelosuppression Risk | Please refer to the Product Information (PI). Thrombocytopenia and other cytopenias are recognised concerns with this drug class. |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Full blood count, and liver and renal function. Confirm the schedule against the PI. |
| Handling Protection | Please refer to the Product Information (PI) and local cytotoxic drug handling guidance |

---

## Safety Considerations

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction query returned 100 entries. The first 20 reviewed include:
- **Major:** clarithromycin, deferiprone, samarium (153Sm) lexidronam
- **Moderate:** eliglustat, eluxadoline, rolapitant, simvastatin, fidaxomicin, cobicistat, palifermin, strontium chloride Sr-89, eltrombopag, fostamatinib, ticagrelor, quinine, ivacaftor, roflumilast, chloramphenicol (including ophthalmic), erythromycin

The full list should be reviewed against the PI before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HER2-positive prediction rests on a high model score and a sound PARP/BRCA mechanism, but no trial or publication tests talazoparib in HER2-positive disease. The existing evidence is in HER2-negative, BRCA-mutated or triple-negative disease. The more credible near-term research question is use in BRCA-mutated or HRD-positive tumours regardless of HER2 status.

**To proceed, the following is needed:**
- Verification of the HER2-positive retrospective study (PMID 36045677), whose abstract appears to refer to HER2-negative disease
- Preclinical or early-phase data in HER2-positive, BRCA-mutated or HRD-positive populations
- The approved indication text and safety sections from the TGA-approved PI
- Mechanism of action data from DrugBank
- A review of the interaction list, particularly the major interactions, and a haematological monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

