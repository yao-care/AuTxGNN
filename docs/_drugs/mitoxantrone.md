---
layout: default
title: Mitoxantrone
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Mitoxantrone: predicted new indication Upper aerodigestive tract neoplasm (evidence level L5). Approved use: Acute myeloid leukaemia and related myeloid leukaemias"
monitor_inn: "mitoxantrone"
predicted_indications: ["upper aerodigestive tract neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "head and neck cancer", "bladder exstrophy-epispadias-cloacal exstrophy complex"]
---

# Mitoxantrone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Mitoxantrone: From Acute Myeloid Leukaemia to Head and Neck Cancer

## One-Sentence Summary

Mitoxantrone is a cytotoxic anthracenedione chemotherapy, originally used for acute myeloid leukaemia (AML) and related myeloid leukaemias.
The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm** (top-ranked prediction), but the best-supported related prediction in the data compiled for this report is **head and neck cancer**, which has **6 registered clinical trials** and **20 publications**, mostly phase II or earlier, with a phase III trial registered but not yet recruiting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukaemia and related myeloid leukaemias (the ARTG entry does not list indication text) |
| Predicted New Indication | Upper aerodigestive tract neoplasm (rank 1); head and neck cancer (rank 7) is the best-evidenced prediction and is used for the evidence sections below |
| TxGNN Prediction Score | 99.78% (upper aerodigestive tract neoplasm); 99.31% (head and neck cancer) |
| Evidence Level | L3 (upper aerodigestive tract neoplasm); L1 (head and neck cancer, as scored in the data compiled for this report) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (head and neck cancer); Hold for other predictions |

Note: the L1 grade for head and neck cancer is generous. It rests on a completed phase Ib study and older phase II studies, not on completed phase 3 RCTs as the standard L1 definition requires. I would treat it as closer to L2-L3 in practice.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mitoxantrone is a topoisomerase II inhibitor and DNA intercalator, structurally similar to the anthracyclines. It is established in AML and other haematological malignancies, and its cytotoxic mechanism could plausibly apply to rapidly dividing squamous and glandular tumour cells.

Older single-agent phase II trials in head and neck squamous cell carcinoma showed modest or minimal activity (for example, one partial response among 22 evaluable patients in a Southwest Oncology Group study). More recent work focuses on a liposomal formulation of mitoxantrone, particularly in nasopharyngeal carcinoma, where several trials are underway.

The model's other predictions have weaker support. Small cell lung carcinoma has only indirect or preclinical evidence. Primary pulmonary lymphoma has small retrospective data, which is plausible because mitoxantrone is used in lymphoma regimens. BCR-ABL positive chronic myeloid leukaemia is plausible only for blast crisis, since TKIs have largely replaced chemotherapy in chronic phase. Well-differentiated fetal adenocarcinoma of the lung and pulmonary blastoma have no trials or literature. The bladder exstrophy-epispadias-cloacal exstrophy complex is a congenital malformation with no plausible mechanistic link, and the score is likely a prediction artefact.

## Clinical Trial Evidence

Trials below are for head and neck cancer (the best-supported prediction). The top-ranked upper aerodigestive tract neoplasm prediction has no registered trials.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04902027](https://clinicaltrials.gov/study/NCT04902027) | Phase 1b | Completed | 45 | Single-arm study of mitoxantrone liposome injection in recurrent/metastatic head and neck cancer; safety and preliminary efficacy |
| [NCT05717764](https://clinicaltrials.gov/study/NCT05717764) | Phase 3 | Not yet recruiting | 500 | Randomised trial of liposomal mitoxantrone plus capecitabine vs capecitabine alone in platinum-refractory recurrent/metastatic nasopharyngeal carcinoma |
| [NCT06472713](https://clinicaltrials.gov/study/NCT06472713) | Phase 2 | Recruiting | 32 | Single-arm study of liposomal mitoxantrone plus PD-1 blockade in previously treated nasopharyngeal carcinoma |
| [NCT06892431](https://clinicaltrials.gov/study/NCT06892431) | Phase 2 | Not yet recruiting | 150 | JMT101 plus liposomal mitoxantrone in nasopharyngeal cancer after at least two prior lines |
| [NCT07070479](https://clinicaltrials.gov/study/NCT07070479) | Phase 2 | Recruiting | 208 | Bayesian adaptive trial of four regimens in PD-1-resistant nasopharyngeal carcinoma, including liposomal mitoxantrone plus anti-PD-1 (mitoxantrone is one arm of several) |
| [NCT07354698](https://clinicaltrials.gov/study/NCT07354698) | Phase 4 | Not yet recruiting | 114 | Mitoxantrone used for lymphatic tracing in transoral robotic thyroid cancer surgery (imaging use, not antitumour therapy) |

No ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Phase 1b | Oral Oncology | Liposomal mitoxantrone in recurrent/metastatic head and neck squamous cell carcinoma |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II | Ann Oncol | EORTC phase II study of mitoxantrone in adenoid cystic carcinoma of the head and neck |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II | Anti-Cancer Drugs | Ifosfamide plus mitoxantrone in recurrent/metastatic squamous cell carcinoma of the head and neck (22 patients) |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II | Anti-Cancer Drugs | Mitoxantrone plus cisplatin in salivary gland malignancies (14 patients) |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Phase II | Am J Clin Oncol | Single-agent mitoxantrone in 19 patients with head and neck carcinoma |
| [6511239](https://pubmed.ncbi.nlm.nih.gov/6511239/) | 1984 | Phase II | Invest New Drugs | Phase II trial of mitoxantrone in advanced head and neck cancer |
| [6511243](https://pubmed.ncbi.nlm.nih.gov/6511243/) | 1984 | Phase II | Invest New Drugs | Southwest Oncology Group study: one partial response in 22 evaluable patients; no significant activity; leukopenia and thrombocytopenia were the main toxicities |
| [8418245](https://pubmed.ncbi.nlm.nih.gov/8418245/) | 1993 | Phase II | J Clin Oncol | Multicentre phase II trial in advanced nasopharyngeal carcinoma in Southeast Asia |
| [34659878](https://pubmed.ncbi.nlm.nih.gov/34659878/) | 2021 | Review | Am J Cancer Res | Systemic therapies for salivary gland adenoid cystic carcinoma |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Systematic review | Bull Cancer | Systemic treatments for recurrent/metastatic adenoid cystic carcinoma of the head and neck |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4514N | Mitozantrone Ebewe | Injection 20 mg (as hydrochloride) in 10 mL | Not listed in the data compiled for this report |

The available product is the conventional (non-liposomal) injection. The recent head and neck trials use a liposomal formulation, which is not among the ARTG entries listed here.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracenedione, topoisomerase II inhibitor) |
| Myelosuppression Risk | High (leukopenia and thrombocytopenia were the main toxicities in the head and neck phase II studies) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential, liver function, cardiac function (cardiotoxicity is a recognised risk), and other parameters per the Product Information |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the Product Information (PI) warnings and precautions for definitive guidance.

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph associations, not label text):** liver failure, liver disease, gallbladder disease, epilepsy, heart failure, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic anaemia), infectious disease, fungal infectious disease and dermatophytosis. Several reflect the drug's myelosuppressive effect.
- **Drug Interactions:** 355 interactions were identified. Main ones:
  - Major: dolasetron
  - Moderate: clarithromycin, eliglustat, rolapitant
  - Minor: levofloxacin
  - Many others, such as metformin, amphotericin B and omeprazole, are of unknown severity.
- **Cardiotoxicity:** noted in the literature compiled for this report and should be managed with monitoring.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (head and neck cancer only; Hold for the other predictions)

**Rationale:**
- Head and neck cancer, particularly nasopharyngeal carcinoma, has an active liposomal mitoxantrone programme with a completed phase Ib study and a registered phase III trial. However, the phase III has not started recruiting, historical single-agent phase II results were modest, and the product available in Australia is the conventional formulation. Evidence is promising but not yet confirmatory.
- Small cell lung carcinoma, well-differentiated fetal adenocarcinoma of the lung, pulmonary blastoma and bladder exstrophy complex should be held. Primary pulmonary lymphoma and BCR-ABL positive CML are better treated as research questions.

**To proceed, the following is needed:**
- Results from the NCT05717764 phase III and the ongoing phase II studies
- Clarity on whether a liposomal formulation is available or registrable in Australia, since the current ARTG entry is the conventional injection
- Detailed mechanism of action data
- Label-based warnings and contraindications from the TGA Product Information
- A cardiac and haematological monitoring plan
- Registration of any Australian trial on ANZCTR if local studies are planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

