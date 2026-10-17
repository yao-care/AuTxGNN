---
layout: default
title: Bortezomib
parent: Model Prediction Only (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bortezomib: predicted new indication Vertebral anomalies and variable endocrine and T-cell dysfunction (evidence level L5). Approved use: Plasma cell myeloma, mantle cell lymphoma, B-cell neoplasm…"
monitor_inn: "Bortezomib"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "neuroblastoma", "myeloid leukemia", "colon adenocarcinoma", "lymph node cancer", "dermatofibrosarcoma protuberans"]
---

# Bortezomib
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

# Bortezomib: From Plasma Cell Myeloma to Non-Hodgkin Lymphoma (Familial) and Related Haematological Malignancies

## One-Sentence Summary

Bortezomib is a proteasome inhibitor, originally used to treat plasma cell myeloma, mantle cell lymphoma, B-cell neoplasms and lymphosarcoma.
The TxGNN model's top-ranked prediction is a rare syndromic condition (**vertebral anomalies and variable endocrine and T-cell dysfunction**) with no supporting studies. The best-supported predictions are **Hodgkin lymphoma**, **non-Hodgkin lymphoma (familial)**, **myeloid leukaemia** and **neuroblastoma**.
Evidence ranges from **no studies** (rank 1) to **dozens of registered clinical trials** (ranks 5 to 7). This report presents the rank 1 prediction in the overview, then discusses the better-evidenced candidates.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma, mantle cell lymphoma, B-cell neoplasm, lymphosarcoma (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication (rank 1) | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score (rank 1) | 96.10% |
| Evidence Level (rank 1) | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision (rank 1) | Hold |

**Summary of leading predictions**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 96.10% | L5 | Hold |
| 2 | Ganglioneuroblastoma | 96.01% | L5 | Hold |
| 3 | Retroperitoneal neoplasm | 95.64% | L4 | Hold |
| 4 | Neuroblastoma | 95.11% | L3 | Research Question |
| 5 | Hodgkin lymphoma | 85.09% | L2 | Research Question |
| 6 | Myeloid leukaemia | 83.77% | L2 | Research Question |
| 7 | Lymphoma, non-Hodgkin, familial | 83.59% | L2 | Proceed with Guardrails |
| 8 | Colon adenocarcinoma | 79.12% | L3 | Hold |
| 9 | Lymph node cancer | 77.96% | L3 | Research Question |
| 10 | Dermatofibrosarcoma protuberans | 77.01% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Bortezomib is known to be a reversible inhibitor of the 26S proteasome. Proteasome inhibition suppresses NF-kB signalling, triggers endoplasmic reticulum stress and promotes apoptosis in cancer cells. Its efficacy in plasma cell myeloma and mantle cell lymphoma is established.

**The top-ranked prediction is probably not meaningful.** The rank 1 condition is a rare syndrome with no trials or literature, and no mechanistic rationale can be built from the data compiled for this report. It is most likely a network-proximity artefact of the model.

**The better-supported predictions are mechanistically coherent:**
- **Non-Hodgkin lymphoma (familial):** Bortezomib is already used in mantle cell lymphoma and has activity in plasmablastic lymphoma and other B-cell lymphomas. The evidence applies to NHL broadly, and nothing is specific to a familial form, so extrapolation needs caution.
- **Hodgkin lymphoma:** Hodgkin Reed-Sternberg cells depend on constitutive NF-kB activity, which proteasome inhibition suppresses.
- **Myeloid leukaemia:** Leukaemic blasts show proteasome and NF-kB dependence, and bortezomib may sensitise cells to chemotherapy and epigenetic agents. Single-agent activity has been modest.
- **Neuroblastoma:** Preclinical models show apoptosis, ER stress and anti-angiogenic effects, and bortezomib overcame chemoresistance. Resistance has been linked to Nrf2/HO-1/GSH.
- **Colon adenocarcinoma:** Preclinical activity exists, but clinical results are unfavourable and proteasome inhibitors have had limited single-agent activity in solid tumours.

---

## Clinical Trial Evidence

The rank 1 prediction has no registered trials. Currently no related clinical trials registered for it. The table below shows the most relevant trials for the best-supported candidates. No ANZCTR identifiers were available in the data compiled for this report.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Completed | 135 | Randomised: ofatumumab + bendamustine ± bortezomib in untreated follicular lymphoma (NHL) |
| [NCT00312845](https://clinicaltrials.gov/study/NCT00312845) | Phase 3 | Completed | 676 | Bortezomib + rituximab vs rituximab alone in relapsed/refractory follicular B-cell NHL (progression-free survival primary endpoint) |
| [NCT00636311](https://clinicaltrials.gov/study/NCT00636311) | Phase 2 | Completed | 13 | IGEV ± bortezomib induction in relapsed/refractory Hodgkin lymphoma |
| [NCT00262860](https://clinicaltrials.gov/study/NCT00262860) | Phase 2 | Completed | 18 | Bortezomib + gemcitabine in relapsed/refractory Hodgkin lymphoma |
| [NCT04173585](https://clinicaltrials.gov/study/NCT04173585) | Phase 2 | Completed | 50 | TEAM trial: bortezomib in AML with epigenetic therapy resistance |
| [NCT01371981](https://clinicaltrials.gov/study/NCT01371981) | Phase 3 | Completed | 1645 | Bortezomib and sorafenib with chemotherapy in de novo AML with high allelic ratio FLT3/ITD |
| [NCT00666588](https://clinicaltrials.gov/study/NCT00666588) | Phase 2 | Completed | 52 | Bortezomib with re-induction chemotherapy in children and young adults with relapsed/refractory AML |
| [NCT02139397](https://clinicaltrials.gov/study/NCT02139397) | Phase 1/2 | Completed | 16 | DFMO + bortezomib in relapsed/refractory neuroblastoma |
| [NCT00644696](https://clinicaltrials.gov/study/NCT00644696) | Phase 1 | Completed | 18 | Irinotecan + bortezomib in children with recurrent/refractory high-risk neuroblastoma |
| [NCT00052507](https://clinicaltrials.gov/study/NCT00052507) | Phase 2 | Completed | Not reported | PS-341 in metastatic colorectal cancer; no positive signal reported |

---

## Literature Evidence

The rank 1 prediction has no related literature. Currently no related literature available for it. Selected publications for the better-supported candidates are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18504251](https://pubmed.ncbi.nlm.nih.gov/18504251/) | 2008 | Phase 2 clinical study | Ann Oncol | Bortezomib + gemcitabine in relapsed/refractory Hodgkin lymphoma, based on NF-kB rationale |
| [29303024](https://pubmed.ncbi.nlm.nih.gov/29303024/) | 2018 | Retrospective analysis | Leuk Lymphoma | Bortezomib + DA-EPOCH associated with long-term survival in plasmablastic lymphoma |
| [29527667](https://pubmed.ncbi.nlm.nih.gov/29527667/) | 2019 | Clinical study | Br J Haematol | Bortezomib + EPOCH effective as frontline treatment in plasmablastic lymphoma |
| [25263936](https://pubmed.ncbi.nlm.nih.gov/25263936/) | 2014 | Review | Expert Opin Pharmacother | Bortezomib for non-Hodgkin lymphoma |
| [22566605](https://pubmed.ncbi.nlm.nih.gov/22566605/) | 2012 | Phase 1 trial | Blood | Clinical and pharmacodynamic activity of bortezomib + decitabine in AML |
| [26784138](https://pubmed.ncbi.nlm.nih.gov/26784138/) | 2016 | Phase 1 trial | Leuk Lymphoma | Midostaurin, bortezomib and MEC in relapsed/refractory AML |
| [27911437](https://pubmed.ncbi.nlm.nih.gov/27911437/) | 2016 | Review | Blood Cancer J | Role of the proteasome in AML |
| [16912267](https://pubmed.ncbi.nlm.nih.gov/16912267/) | 2006 | Preclinical (in vitro) | J Natl Cancer Inst | Bortezomib inhibits growth, induces apoptosis and reduces angiogenesis in neuroblastoma cells |
| [17689684](https://pubmed.ncbi.nlm.nih.gov/17689684/) | 2007 | Preclinical (murine) | Surgery | Bortezomib inhibits angiogenesis and reduces tumour burden in a neuroblastoma model |
| [22552540](https://pubmed.ncbi.nlm.nih.gov/22552540/) | 2012 | Preclinical (in vitro) | Int J Oncol | Bortezomib induces G2-M arrest in colon cancer cells; clinical CRC results largely inconclusive |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12219D | DBL Bortezomib | Powder for injection 3 mg | Not available in the data compiled for this report |

---

## Cytotoxicity

Bortezomib is an antineoplastic drug. Detailed toxicity data were not available in the data compiled for this report, so please refer to the Product Information (PI) warnings and precautions. The following is general guidance only.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Thrombocytopenia and neutropenia are flagged in the knowledge graph contraindication data. Please refer to the PI |
| Emetogenicity Classification | Please refer to the PI |
| Monitoring Items | Full blood count (with platelets and differential), liver function, assessment for peripheral neuropathy |
| Handling Protection | Follow local cytotoxic drug handling procedures and refer to the PI |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text) include:
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Neurological: peripheral neuropathy, peripheral nervous system disease, posterior leukoencephalopathy syndrome
- Cardiovascular: cardiovascular disease, heart disease, long QT syndrome, hypotensive disorders, orthostatic hypotension, pulmonary hypertension
- Respiratory: interstitial lung disease, pneumonia, acute respiratory distress syndrome
- Gastrointestinal and hepatic: ileus, intestinal obstruction, liver disease, gallbladder disease
- Metabolic: diabetes mellitus, diabetic ketoacidosis

**Drug interactions:** The interaction query returned 100 interactions. The first 20 reviewed were mostly Moderate, with a few Minor:
- **Antidiabetic agents (Moderate):** acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, ertugliflozin, exenatide. Glycaemic monitoring is advisable.
- **Other Moderate:** aprepitant, ascorbic acid, metronidazole, clarithromycin, clotrimazole.
- **Minor:** dexamethasone, esomeprazole.

---

## Conclusion and Next Steps

**Decision: Hold** (for the rank 1 prediction)

**Rationale:**
- The top-ranked prediction has a high model score but no trials, no literature and no plausible mechanistic link, so it is likely a network artefact. Ranks 2 and 3 are also weak (no trials; one case report).
- Among the other candidates, only non-Hodgkin lymphoma has enough support to be considered **Proceed with Guardrails** (L2, with a randomised Phase 2 and a Phase 3 trial in follicular lymphoma). Note that the label is "familial", and the evidence is not specific to that form. Hodgkin lymphoma, myeloid leukaemia, neuroblastoma and lymph node cancer are **Research Questions**. Colon adenocarcinoma and dermatofibrosarcoma protuberans are **Hold**.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable) to support mechanistic analysis
- The TGA Product Information, including warnings, contraindications and approved indications for ARTG 12219D (the safety data gap is Blocking for safety screening)
- Review of the trial results (outcomes, not just registration records) for NCT01286272 and NCT00312845 before any NHL claims
- Clarification of whether the "familial NHL" label is clinically meaningful, or whether NHL should be assessed as a broader indication
- A safety monitoring plan covering peripheral neuropathy, cytopenias and cardiopulmonary risk, with interaction checks for patients on antidiabetic therapy
- Route and formulation compatibility assessment (currently pending; only an injectable form is registered in Australia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

