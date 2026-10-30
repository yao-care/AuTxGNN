---
layout: default
title: Etoposide
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Etoposide"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
description: "Etoposide: predicted new indication Well-differentiated fetal adenocarcinoma of the lung (evidence level L5). Approved use: Not recorded in the local data"
---

# Etoposide
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

## Etoposide: Well-differentiated fetal adenocarcinoma of the lung
{: .text-alpha }

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor chemotherapy originally used for small cell lung carcinoma and testicular germ cell tumours (including seminoma, teratoma and yolk sac tumour).
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **34 registered clinical trials** and **20 publications** linked to this prediction, including several randomised phase 3 trials.
Etoposide with ifosfamide is already part of standard Ewing sarcoma regimens internationally, so this prediction largely validates existing practice rather than identifying a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Etoposide is well known as a topoisomerase II inhibitor, which causes DNA strand breaks and cell death in rapidly dividing cells. This is consistent with its established activity in small cell lung carcinoma and germ cell tumours.

Ewing sarcoma is an aggressive bone and soft tissue cancer of children, adolescents and young adults. Published work notes that it is highly sensitive to genotoxic agents such as etoposide. Ifosfamide plus etoposide is a long-established part of Ewing sarcoma chemotherapy, typically alternating with vincristine, doxorubicin and cyclophosphamide (VDC/IE). A randomised trial in the *New England Journal of Medicine* (2003) showed that adding ifosfamide and etoposide to standard chemotherapy improved outcomes in newly diagnosed disease.

Other lower-ranked predictions in the data (for example pulmonary blastoma and various rhabdomyosarcoma subtypes) are also plausible but rest on far weaker evidence. Rhabdomyosarcoma (rank 6) also has an L1 evidence label, but etoposide's contribution cannot be separated from combination regimens. This report focuses on the top-evidence candidate, Ewing sarcoma.

---

## Clinical Trial Evidence

Many registered trials include etoposide-containing regimens. The most relevant are listed below. In nearly all of them, etoposide is one component of a multi-drug regimen, so its individual contribution cannot be isolated.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: randomised chemotherapy, radiotherapy and stem cell transplant strategies in Ewing sarcoma |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Chemotherapy intensification through interval compression in Ewing sarcoma and related tumours |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to standard five-drug chemotherapy (including etoposide) in non-metastatic disease |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy (including etoposide) in metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification versus standard treatment in non-metastatic Ewing sarcoma |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not reported | EICESS 92: randomised comparison of combination chemotherapy regimens plus surgery and radiotherapy |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and consolidation in metastatic Ewing sarcoma |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | Active, not recruiting | 83 | Irinotecan and temozolomide added to high-dose alkylator-based therapy in newly diagnosed Ewing sarcoma |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not reported | Cyclophosphamide, doxorubicin, vincristine, etoposide and ifosfamide followed by resection and radiotherapy |
| [NCT00014313](https://clinicaltrials.gov/study/NCT00014313) | Phase 2 | Terminated | 3 | Weekly cisplatin with oral etoposide in metastatic Ewing sarcoma/PNET; terminated early |

Trial counts and details are drawn from the data compiled for this report; several additional smaller or terminated trials are not listed here.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012: comparison of two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (alternating VDC and ifosfamide-etoposide) in localised Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | Euro Ewing 2012 international randomised trial protocol |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board consensus recommendations |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospective analysis | Sarcoma | Oral etoposide in 33 adolescent and adult patients with relapsed or refractory Ewing sarcoma at Peter MacCallum Cancer Centre (Australia) |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management of Ewing sarcoma and future collaborative approaches |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Overview of Ewing sarcoma treatment and outcomes |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Preclinical | Nature | EWS-FLI1 causes R-loops and blocks BRCA1 repair, helping explain Ewing sarcoma's sensitivity to etoposide |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1389D | Vepesid | Capsule 100 mg | Not available in the data compiled for this report |

Only one ARTG entry (oral capsule) was identified. Intravenous etoposide products were not captured in the data, so availability of other formulations should be checked against the ARTG.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor, epipodophyllotoxin class) |
| Myelosuppression Risk | High. Neutropenia, leukopenia, thrombocytopenia and anaemia are listed as contraindicated or high-risk conditions in the knowledge graph |
| Emetogenicity Classification | Low to moderate (oral and intravenous administration may differ; check the Product Information) |
| Monitoring Items | Full blood count with differential, liver and renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the Product Information (PI) warnings and precautions for definitive guidance.

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for formal safety information.

- **Knowledge-graph contraindication signals** (not label text): thrombocytopenia, neutropenia, agranulocytosis, anaemia, leukopenia, interstitial lung disease, pulmonary fibrosis, impaired renal function, acidosis and metabolic acidosis, and drug-induced liver injury.
- **Secondary malignancy**: the evidence compiled notes a risk of secondary leukaemia with epipodophyllotoxins.
- **Drug interactions**: 100 interactions were identified. Those rated Moderate include aprepitant, rolapitant, metronidazole, tinidazole, eliglustat, rosuvastatin and simvastatin. Levofloxacin is rated Minor. Others (for example cimetidine, doxycycline, amphotericin B, morphine and pantoprazole) have no assigned severity. The full list should be reviewed for each patient.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomised phase 3 trials and publications support etoposide-containing regimens (with ifosfamide) in Ewing sarcoma, and this use is already recognised in consensus guidelines. It is better viewed as validation of existing practice than as a novel repurposing. Etoposide's effect cannot be isolated from the combination regimens, and it carries significant myelosuppression and secondary malignancy risks.

**To proceed, the following is needed:**
- Confirmation of the Australian approved indications, as the ARTG indication text for Vepesid was not available and the Ewing sarcoma use may be off-label
- Review of intravenous etoposide products on the ARTG, since only an oral capsule was identified
- Mechanism of action data and Product Information warnings and contraindications (both are data gaps)
- A myelosuppression and secondary malignancy monitoring plan, plus interaction management
- Review against local paediatric and adolescent/young adult sarcoma protocols and Australian practice data, such as the Peter MacCallum oral etoposide series

**Other predictions:** All other predicted indications in the data (pulmonary blastoma, primary pulmonary lymphoma, and rhabdomyosarcoma subtypes) should be treated as **Hold** or research questions. Evidence for them is limited to case reports, indirect literature or model scores alone. Rhabdomyosarcoma overall has trial support but is also confounded by combination regimens.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

