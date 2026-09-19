---
layout: default
title: Talazoparib
parent: Moderate Evidence (L3-L4)
nav_order: 651
evidence_level: L3
indication_count: 10
---

# Talazoparib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Talazoparib: From BRCA-Mutated HER2-Negative Breast Cancer to HER2-Positive Breast Cancer

## One-line Summary

Talazoparib (Talzenna) is a PARP inhibitor with an internationally approved indication for germline BRCA1/2 mutations, **HER2-negative** locally advanced or metastatic breast cancer. The TxGNN model predicts its highest-ranked new indication as **HER2-positive breast cancer** at evidence level **L3**; however, upon manual review, the supporting evidence (10 clinical trials, 14 literature reports) almost uniformly points to HER2 **negative** populations, directly contradicting the predicted label itself. Special attention is needed when interpreting this data quality concern.

> ⚠️ **Important Reminder**: The disease label of this candidate indication (HER2-positive) is inconsistent with the trial populations in its evidence database (nearly all HER2-negative), likely due to an ontology mapping error rather than representing a true therapeutic signal of the drug's efficacy in HER2-positive breast cancer.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original indication | Germline BRCA1/2 mutations, HER2-negative metastatic breast cancer (per literature PMID 36952230, not local drug registration data) |
| Predicted new indication | HER2 Positive Breast Carcinoma |
| TxGNN prediction score | 98.98% (rank 10415) |
| Evidence level | L3 |
| Australian market status | Not marketed |
| ARTG registrations | 0 |
| Recommended decision | Hold |

---

## Why Does This Prediction Appear Reasonable?

Currently, there is no detailed mechanism of action (MOA) structured data; however, based on multiple clinical trial abstracts in the evidence package, talazoparib is an oral **PARP (poly ADP-ribose polymerase) inhibitor** that blocks single-strand DNA repair enzymes and induces "synthetic lethality" in tumour cells with BRCA1/2 or homologous recombination repair (HRR) defects, thereby exerting anti-tumour effects.

From a mechanistic standpoint, PARP inhibitor efficacy theoretically depends on the tumour's BRCA/HRD (homologous recombination deficiency) status and has no direct causal relationship with HER2 expression. However, talazoparib's currently approved and primary clinical development populations are almost entirely restricted to **HER2-negative** breast cancer (e.g., NCT06735742's title explicitly states "HER2-Negative"; PMID 36952230's abstract also clearly defines the approved population as "HER2-negative"). Therefore, this TxGNN prediction of "HER2-positive breast cancer" may well be a data labelling or ontology mapping error rather than a true signal of new therapeutic efficacy in that population. To rigorously assess this candidate indication, the disease label should first be manually verified to determine if it should be corrected to HER2-negative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Summary |
|---|---|---|---|---|
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | Talazoparib monotherapy as neoadjuvant treatment for germline BRCA1/2 mutation carriers with **HER2-negative** early-stage breast cancer |
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | ctDNA-guided treatment switching study in HR+ advanced breast cancer (translational research, not talazoparib-specific) |
| [NCT06735742](https://clinicaltrials.gov/study/NCT06735742) | N/A | Active, not recruiting | 3 | TALZENNA post-marketing safety surveillance with population of BRCA-mutant, **HER2-negative** breast cancer (Japan)—title contradicts this indication label |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 combined with talazoparib in triple-negative/HER2-negative metastatic breast cancer |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Recruiting | 36 | Talazoparib in advanced solid tumours with DNA repair gene aberrations |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib + talazoparib in triple-negative/BRCA1/2-positive, **HER2-negative** breast cancer—population contradicts this indication |
| [NCT02401347](https://clinicaltrials.gov/study/NCT02401347) | Phase 2 | Completed | 21 | Talazoparib in BRCA wild-type triple-negative breast cancer or HRR-mutant solid tumours—not HER2-positive-specific research |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY2 adaptive platform trial covering multiple breast cancer subtypes including HER2+, but not talazoparib-specific analysis |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH biomarker-directed basket trial of approved drugs; terminated with small sample size |
| [NCT04508803](https://clinicaltrials.gov/study/NCT04508803) | Phase 2 | Completed | 37 | HX008 combined with niraparib in germline mutation carriers with metastatic breast cancer—investigational drug is not talazoparib |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Summary |
|------|------|------|---------|---|
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | Comparative study | Frontiers in Immunology | Retrospective comparison of talazoparib with conventional chemotherapy; abstract describes population as HER2-**negative** advanced breast cancer, inconsistent with title "HER2-positive" |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | Real-world cohort study | The Oncologist | Real-world US characteristics and outcomes of talazoparib treatment in germline BRCA-mutant, HER2-negative advanced breast cancer (EMBRACA-approved population) |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | Real-world cohort study | Clinical Breast Cancer | Mayo Clinic real-world patterns of prescribing and outcomes of PARP inhibitors in metastatic breast cancer |
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | Meta-analysis (GRADE) | Breast (Edinburgh) | Meta-analysis of PARP inhibitors (olaparib/talazoparib) in BRCA1/2-associated **HER2-negative** advanced breast cancer (Italian Society of Medical Oncology) |
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | Guideline review | J Clin Oncol | ASCO guideline update: endocrine and targeted therapy for HR-positive, **HER2-negative** metastatic breast cancer |
| [35343197](https://pubmed.ncbi.nlm.nih.gov/35343197/) | 2022 | Review | Indian J Cancer | Review of the role of PARP inhibitors in the treatment of **HER2-negative** metastatic breast cancer |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | Review | Oncology (Williston Park) | Review of new treatments for metastatic triple-negative breast cancer, including immunotherapy and antibody-drug conjugates |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | Review | Mol Diagn Ther | Review of molecular targeted therapy feasibility in multiethnic breast cancer patients, covering approved populations of PARP inhibitors (olaparib/talazoparib) |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase 1/2 trial report | Breast Cancer Res Treat | Gedatolisib + talazoparib in advanced triple-negative/BRCA1/2-positive, **HER2-negative** breast cancer |
| [32869930](https://pubmed.ncbi.nlm.nih.gov/32869930/) | 2020 | Genomic landscape study | The Oncologist | Integrated genomic landscape and PD-L1 biomarker analysis in 312 breast cancer patients |

---

## Australian Market Information

Talazoparib is currently **not marketed in Australia** and has no ARTG registration; therefore, approved indications, formulations, and product information cannot be listed.

---

## Cytotoxicity Information

| Item | Content |
|------|---------|
| Cytotoxicity classification | Targeted therapy—PARP inhibitor selectively acting on BRCA/HRD-deficient tumour cells via synthetic lethality mechanism, not traditional broad-spectrum cytotoxic chemotherapy |
| Myelosuppression risk | Moderate (based on risk assessments noted in the evidence package for other indications; talazoparib is known to have common adverse reactions including myelosuppression-induced thrombocytopenia) |
| Emetogenicity classification | Refer to TGA-approved product information (PI) for warnings and precautions |
| Monitoring parameters | Full blood count (FBC, including differential), with platelet and haemoglobin monitoring as per myelosuppression risk |
| Handling precautions | Refer to TGA-approved product information (PI) for warnings and precautions |

---

## Safety Considerations

Refer to TGA-approved product information (PI) for comprehensive safety information. Currently, no drug-drug interaction (DDI) data is available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (HER2-positive breast cancer) directly contradicts its own supporting trial/literature populations (almost entirely HER2-negative); the evidence package itself has flagged this as a suspected labelling error, which must be clarified before reliable assessment is possible.
- The drug is not marketed in Australia, and TGA product information warnings and contraindications represent "Blocking"-level data gaps (DG001), preventing completion of S1 safety triage.

**If advancement is to be pursued, the following must be supplemented:**
- Manual verification of whether the "HER2 positive breast carcinoma" label should be corrected to HER2-negative (or reclassified as a candidate for exclusion)
- Obtain TGA-approved product information (PI) for warnings, contraindications, and DDI data
- Obtain complete mechanism of action (MOA) structured data
- Recommend separate evaluation of **progesterone-receptor negative breast cancer** ranked 3rd in the same dataset (evidence level L2, decision stage S2, recommendation Proceed with Guardrails), whose trial populations align better with talazoparib's known approved mechanism, providing a relatively more robust evidence base

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

