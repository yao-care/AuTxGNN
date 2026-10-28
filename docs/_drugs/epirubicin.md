---
layout: default
title: Epirubicin
parent: Moderate Evidence (L3-L4)
nav_order: 259
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Epirubicin"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
description: "Epirubicin: predicted new indication Primary pulmonary lymphoma (evidence level L4). Approved use: Not recorded in the local data"
---

# Epirubicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Epirubicin: Primary pulmonary lymphoma
{: .text-alpha }

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy agent, originally used to treat breast carcinoma.
The TxGNN model's top-ranked prediction is **primary pulmonary lymphoma**, but this is supported by **no registered clinical trials** and only **6 publications** (mostly case reports, small retrospective series and a drug review).
The strongest evidence in the data compiled for this report is for a lower-ranked prediction, **small cell lung carcinoma**, which has **5 clinical trials** (3 Phase 3) and **21 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L4 (for the top-ranked prediction; small cell lung carcinoma reaches L1) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold (primary pulmonary lymphoma); Proceed with Guardrails as a research question for small cell lung carcinoma |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, epirubicin is an anthracycline (a 4' epimer of doxorubicin) that inhibits topoisomerase II and intercalates into DNA. Its efficacy in breast cancer is established, and mechanistically it may be applicable to other rapidly proliferating, chemosensitive tumours.

**Primary pulmonary lymphoma:** Anthracyclines are core components of lymphoma regimens, and epirubicin appears in regimens such as CEOP and VEBEP. However, the evidence does not isolate epirubicin's contribution in pulmonary lymphoma. Doxorubicin-based R-CHOP remains the standard anthracycline backbone, so this prediction is plausible but unproven for epirubicin specifically.

**Other predictions in the ranked list:**
- **Small cell lung carcinoma (rank 3):** a chemosensitive tumour with direct Phase 3 evidence, but epirubicin has not become standard of care. Platinum/etoposide plus immunotherapy is the current standard, and the benefit of adding epirubicin was not clearly favourable.
- **Upper aerodigestive tract neoplasm (rank 7):** epirubicin-containing ECF/EOX regimens are established in gastroesophageal adenocarcinoma. This is largely an existing use rather than novel repurposing, and newer regimens (e.g. FLOT, immunotherapy combinations) have partly displaced it.
- **Myeloid leukaemia (rank 6):** a mechanistic fit, but daunorubicin and idarubicin are preferred, and several papers describe epirubicin as a cause of secondary AML/MDS, which is a safety signal.
- **Breast-related predictions (ranks 8-10) and several lung subtypes (ranks 2, 5):** model prediction only, with no trials or literature. The benign breast conditions (papillomatosis, leiomyoma) are not appropriate targets for cytotoxic chemotherapy.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (primary pulmonary lymphoma). The trials below relate to the best-supported prediction, **small cell lung carcinoma**. Trial titles in the data are partly truncated, so outcomes cannot be confirmed.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003606](https://clinicaltrials.gov/study/NCT00003606) | Phase 3 | Completed | 216 | Cisplatin/etoposide with or without epirubicin and cyclophosphamide in extensive-stage SCLC; directly tests the epirubicin-containing arm (results not provided) |
| [NCT00011921](https://clinicaltrials.gov/study/NCT00011921) | Phase 3 | Unknown | 430 | Sequential high-dose chemotherapy versus standard chemotherapy in SCLC; epirubicin contribution not isolated |
| [NCT00658580](https://clinicaltrials.gov/study/NCT00658580) | Phase 3 | Completed | 361 | Cisplatin/etoposide versus etoposide regimen without platinum in extensive SCLC; epirubicin role unclear |
| [NCT03755115](https://clinicaltrials.gov/study/NCT03755115) | Phase 2 | Unknown | 40 | PD-1 antibody SHR-1210 plus epirubicin in extensive SCLC after first-line failure; no results available |
| [NCT00154739](https://clinicaltrials.gov/study/NCT00154739) | Phase 2 | Completed | 86 | Gemcitabine/cisplatin versus gemcitabine/epirubicin in stage IIIB/IV lung cancer; histology (small cell vs non-small cell) uncertain |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

**Primary pulmonary lymphoma (top-ranked prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Epirubicin pharmacology and use in cancer chemotherapy; equivalent response rates to doxorubicin-containing regimens in several malignancies |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Primary extranodal DLBCL in the rituximab era (indirect) |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Retrospective cohort | Annals of Hematology | Pola-R-CHP in 117 DLBCL patients (anthracycline regimen, indirect) |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | Cancer Journal | VEBEP plus radiotherapy in advanced Hodgkin's disease (indirect) |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Rev Invest Clin | Primary non-Hodgkin's lymphoma of the lung |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Transl Cancer Res | Pleural MALT lymphoma, misdiagnosis (indirect) |

**Selected publications for small cell lung carcinoma (best-supported prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12488411](https://pubmed.ncbi.nlm.nih.gov/12488411/) | 2002 | Randomised Phase 3 | J Clin Oncol | Cisplatin/etoposide superior to cyclophosphamide/epirubicin/vincristine in SCLC (5-year follow-up) |
| [21831476](https://pubmed.ncbi.nlm.nih.gov/21831476/) | 2012 | Phase 2 | Lung Cancer | Epirubicin plus ifosfamide in relapsed or refractory SCLC |
| [36000584](https://pubmed.ncbi.nlm.nih.gov/36000584/) | 2023 | Real-world cohort | Cancer Med | EpiTax: second-line epirubicin-paclitaxel in relapsed SCLC |
| [7812705](https://pubmed.ncbi.nlm.nih.gov/7812705/) | 1994 | Clinical trial | Lung Cancer | Cyclophosphamide/epirubicin/etoposide in 136 patients: 31% complete and 49% partial responses |
| [1317199](https://pubmed.ncbi.nlm.nih.gov/1317199/) | 1992 | Clinical trial | Eur J Cancer | VEC regimen with epirubicin dose escalation in limited-stage SCLC |
| [12847592](https://pubmed.ncbi.nlm.nih.gov/12847592/) | 2003 | Clinical trial | Saudi Med J | Alternating EP and ifosfamide/vincristine/epirubicin regimen in SCLC |
| [2165738](https://pubmed.ncbi.nlm.nih.gov/2165738/) | 1990 | Phase 2 | Am J Clin Oncol | High-dose epirubicin in untreated SCLC: 33% overall response rate |
| [11576714](https://pubmed.ncbi.nlm.nih.gov/11576714/) | 2001 | Review | Lung Cancer | Chemotherapy for primary and recurrent SCLC; epirubicin among active agents |
| [33209466](https://pubmed.ncbi.nlm.nih.gov/33209466/) | 2020 | Review | J Thorac Dis | Systemic therapy for limited-stage SCLC; cisplatin/etoposide remains the standard |

**Other relevant items:** The perioperative MAGIC Phase 3 RCT of ECF in gastroesophageal cancer ([16822992](https://pubmed.ncbi.nlm.nih.gov/16822992/), 2006, N Engl J Med) supports the upper aerodigestive tract prediction, though this is largely an existing use.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4375G | Epirubicin Accord | Solution for injection containing epirubicin hydrochloride 200 mg in 100 mL | Not stated in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor and DNA intercalator) |
| Myelosuppression Risk | High (the knowledge graph lists neutropenia, thrombocytopenia and agranulocytosis as contraindication-related conditions) |
| Emetogenicity Classification | Moderate (general class knowledge; please confirm against the Product Information) |
| Monitoring Items | Full blood count with differential, liver and renal function, cardiac function (LVEF) before and during treatment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, other myocardial disorders, hemoglobinopathy, pyoureter and stomatitis.
- **Drug Interactions:** 100 interactions were identified. Examples of Major interactions are **cimetidine** and **dolasetron**. Moderate interactions include clarithromycin, bupropion, levofloxacin, loperamide, naltrexone, pioglitazone, famotidine, palonosetron, minocycline and eliglustat. One Minor interaction is metronidazole.
- **Secondary malignancy:** The literature reports secondary AML/MDS after epirubicin-based chemotherapy, and anthracycline cardiotoxicity is a recognised class concern.

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold (primary pulmonary lymphoma, the top-ranked prediction). Small cell lung carcinoma may proceed with guardrails as a research question only.**

**Rationale:**
- The top-ranked prediction has no registered trials and only case reports, small retrospective series and a review. These do not isolate epirubicin's contribution, and doxorubicin-based R-CHOP is already the standard.
- Small cell lung carcinoma has direct Phase 3 evidence (L1), but this reflects that trials exist, not proven benefit. The randomised comparison in PMID 12488411 favoured cisplatin/etoposide over an epirubicin-containing regimen, and epirubicin is not part of current standard care.

**To proceed, the following is needed:**
- Mechanism of action data and TGA Product Information warnings and contraindications, both of which are missing and block safety screening
- Published outcomes from NCT00003606 and NCT00011921 to determine the incremental benefit and toxicity of adding epirubicin
- For pulmonary lymphoma, comparative data against standard doxorubicin-based regimens
- A cardiac and haematological safety monitoring plan, including cumulative anthracycline dose limits
- Confirmation of the approved indications for the ARTG entry (4375G)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

