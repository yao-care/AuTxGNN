---
layout: default
title: Cisplatin
parent: Model Prediction Only (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Cisplatin
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

# Cisplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cisplatin is a platinum-based chemotherapy drug, originally used for ovarian cancer and related ovarian tumours.
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **20 clinical trials** and **20 publications** retrieved in the data compiled for this report. Only a few of the trials directly test cisplatin in breast cancer, and the literature is mostly preclinical or review material.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (the Australian ARTG entry carries no indication text; the original indication is taken from the knowledge-graph indication list) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 97.39% |
| Evidence Level | L1 (as assigned in the compiled data; see the note in the conclusion) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, cisplatin forms DNA intrastrand crosslinks that trigger apoptosis in rapidly dividing cells. Its efficacy in ovarian cancer is established, and mechanistically it may be applicable to breast cancer.

Breast tumours with homologous recombination deficiency (for example BRCA1/2 mutation carriers and triple-negative breast cancer) are thought to be especially sensitive to DNA-damaging platinum agents. Ovarian cancer also depends on DNA-damage sensitivity, which links the original and predicted indications. Supporting this, an older review reports that cisplatin has single-agent, front-line activity in metastatic breast cancer, and a small 1989 study of cisplatin plus etoposide reported responses in refractory disease.

Other high-scoring predictions in the same analysis are ovarian choriocarcinoma, gonadal germ cell tumour, adult germ cell tumour and ovarian primitive germ cell tumour. Cisplatin-based BEP chemotherapy (bleomycin, etoposide, cisplatin) is already the established standard in germ cell tumours. Those predictions are therefore better supported than breast carcinoma on clinical grounds, and they are summarised at the end of this report.

## Clinical Trial Evidence

Of the 20 trials retrieved for breast carcinoma, the most relevant are listed below. Many of the remainder are phase 1 studies of other investigational agents in which cisplatin is not the focus.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01670500](https://clinicaltrials.gov/study/NCT01670500) | Phase 2 | Completed | 118 | Randomised comparison of neoadjuvant cisplatin versus doxorubicin/cyclophosphamide in newly diagnosed breast cancer with germline BRCA mutations. Direct comparison of cisplatin in the target disease; results are not summarised in the data compiled. |
| [NCT03201861](https://clinicaltrials.gov/study/NCT03201861) | Phase 3 | Recruiting | 762 | Weekly paclitaxel plus cisplatin as adjuvant chemotherapy in high-risk, HER2-negative early breast cancer. No efficacy results yet. |
| [NCT00003032](https://clinicaltrials.gov/study/NCT00003032) | Phase 3 | Completed | 224 | High-dose chemotherapy with autologous stem cell support versus standard therapy in metastatic breast cancer. The regimen is largely obsolete and cisplatin's individual contribution cannot be isolated. |
| [NCT02365805](https://clinicaltrials.gov/study/NCT02365805) | Phase 2 | Completed | 30 | BERNAQ: neoadjuvant chemotherapy tailored to BRCA1 levels in HER2-negative breast cancer. Small study. |
| [NCT00535509](https://clinicaltrials.gov/study/NCT00535509) | Not applicable (described as phase 2) | Completed | 285 | Neoadjuvant FEC100/cisplatin-docetaxel with or without trastuzumab in HER2-positive locally advanced breast cancer. |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Intensive sequential chemotherapy versus high-dose chemotherapy with stem cell support in primary breast cancer with 4-9 involved nodes. |
| [NCT00002836](https://clinicaltrials.gov/study/NCT00002836) | Phase 3 | Completed | 184 | High-dose chemotherapy plus G-CSF versus G-CSF alone for stem cell mobilisation in breast cancer. |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Pilot of sequential high-dose cisplatin-containing cycles with stem cell support in advanced cancer. Historical regimen. |
| [NCT00004900](https://clinicaltrials.gov/study/NCT00004900) | Phase 2 | Completed | Not reported | Sequential high-dose chemotherapy with stem cell support in metastatic breast cancer. |
| [NCT02897375](https://clinicaltrials.gov/study/NCT02897375) | Phase 1 | Completed | 71 | Palbociclib combined with cisplatin or carboplatin in advanced solid tumours (dose-finding). |

No ANZCTR identifiers were included in the data compiled for this report.

## Literature Evidence

No randomised trial publication was retrieved for breast carcinoma. The items below are mostly reviews and preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1411630](https://pubmed.ncbi.nlm.nih.gov/1411630/) | 1992 | Review | Semin Oncol | Cisplatin has significant single-agent, front-line activity in metastatic breast cancer; in combination (for example with etoposide or 5-FU) response rates are similar to other first-line combinations. |
| [2643295](https://pubmed.ncbi.nlm.nih.gov/2643295/) | 1989 | Clinical study | Am J Clin Oncol | Cisplatin plus etoposide in 31 patients with refractory metastatic breast cancer: 3 complete and 8 partial responses among 29 evaluable patients. |
| [39216513](https://pubmed.ncbi.nlm.nih.gov/39216513/) | 2024 | Review | Mutat Res Rev Mutat Res | Molecular determinants of cisplatin response and resistance in breast tumours, and nanotechnology-based approaches. |
| [39536542](https://pubmed.ncbi.nlm.nih.gov/39536542/) | 2024 | Review | Pathol Res Pract | Role of long non-coding RNAs in cisplatin response and resistance in breast cancer. |
| [27448297](https://pubmed.ncbi.nlm.nih.gov/27448297/) | 2016 | Review | Tumour Biol | miRNA-mediated cisplatin resistance in breast cancer. |
| [34998857](https://pubmed.ncbi.nlm.nih.gov/34998857/) | 2022 | Preclinical | Toxicol Appl Pharmacol | Timed (chronotherapy) cisplatin in a mouse model of triple-negative mammary carcinoma. |
| [41053085](https://pubmed.ncbi.nlm.nih.gov/41053085/) | 2025 | Preclinical | Cell Death Dis | USP9X and WWP1 regulate IGF2BP2 ubiquitination, TNBC progression and cisplatin sensitivity. |
| [37067747](https://pubmed.ncbi.nlm.nih.gov/37067747/) | 2023 | Preclinical | Cell Oncol | Gallium maltolate shows synergism with cisplatin in breast carcinoma cells. |
| [37914960](https://pubmed.ncbi.nlm.nih.gov/37914960/) | 2024 | Preclinical | Breast Cancer | SLC38A5 promotes glutamine metabolism and reduces cisplatin chemosensitivity. |
| [8400329](https://pubmed.ncbi.nlm.nih.gov/8400329/) | 1993 | Pharmacokinetic study | Breast Cancer Res Treat | Pharmacokinetic and pharmacodynamic interactions of intensive cyclophosphamide, cisplatin and BCNU in breast cancer. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4319H | Cisplatin Accord | I.V. injection 50 mg in 50 mL | Not recorded in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum-based alkylating-like agent; forms DNA crosslinks) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions (cisplatin is generally regarded as highly emetogenic) |
| Monitoring Items | Please refer to the PI; typically FBC, renal function, electrolytes, and hearing assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Safety label data (warnings and contraindications) were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** An interaction screen returned 100 potential interactions. Most of those listed are of moderate severity, with one minor. Examples include:
- Aminoglycoside antibiotics (for example kanamycin) and amphotericin B formulations (conventional, lipid complex, cholesteryl sulfate, liposomal)
- Proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole)
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone)
- Mesalazine, balsalazide, metronidazole, exenatide
- Ascorbic acid (minor)

The data compiled do not describe the mechanism or clinical consequence of each interaction, so these should be checked against the PI and a current interaction reference.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cisplatin is already marketed in Australia and has a plausible DNA-damage mechanism in BRCA-mutated and triple-negative breast cancer. Direct support is limited to one completed randomised phase 2 trial (NCT01670500) with no results in the compiled data, one recruiting phase 3 trial (NCT03201861), and older small studies. The "L1" evidence level assigned in the compiled data appears generous: the completed phase 3 trial that was retrieved tested high-dose chemotherapy with stem cell support, in which cisplatin's contribution cannot be isolated, and no completed phase 3 trial testing cisplatin directly in breast cancer was identified. Evidence is better regarded as L2 or lower for this specific indication.

**To proceed, the following is needed:**
- Published results from NCT01670500 and, when available, NCT03201861
- Detailed mechanism of action data (MOA) and the approved indication text from the TGA Product Information
- Warnings, contraindications and a safety monitoring plan from the PI (the safety screen was blocked by missing label data)
- Clarification of the target population (for example BRCA-mutated or triple-negative disease) and confirmation of any off-label use pathway in Australia
- Review of the interaction list, particularly nephrotoxic and ototoxic combinations (aminoglycosides, amphotericin B)

## Other Predicted Indications (Summary)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|------|
| 2 | Choriocarcinoma of ovary | 95.68% | L2 | Proceed with Guardrails | Evidence is indirect, drawn from germ cell tumour trials (for example NCT00470366, a phase 2 trial in germ cell tumours; NCT03067181, a recruiting phase 3 trial of carboplatin versus cisplatin). Published ovarian choriocarcinoma literature is mainly case reports. |
| 3 | Gonadal germ cell tumour | 95.65% | L1 | Proceed with Guardrails | Multiple completed phase 3 trials of cisplatin-based regimens in germ cell tumours, including NCT00002566, NCT00324298 and NCT00003941. NCT02429687 is a recruiting phase 3 trial comparing paclitaxel plus carboplatin or cisplatin with BEP in malignant ovarian germ cell tumours. A 2025 meta-analysis (PMID 39924670) compares carboplatin-based and cisplatin-based chemotherapy. Most trials enrolled men with testicular disease. |
| 4 | Adult germ cell tumour | 95.49% | L1 | Proceed with Guardrails | Cisplatin-based BEP and EP are long-established; PMID 9552027 is a randomised comparison of BEP and VIP. Cisplatin is already standard care here. |
| 5 | Ovarian primitive germ cell tumour | 95.46% | L2 | Proceed with Guardrails | Only early-phase trials and reviews specific to this indication; evidence is extrapolated from testicular germ cell tumours. |
| 6-8, 10 | Enteric, reticular, hepatoid and papillary patterns of testicular yolk sac tumour | 95.02% | L5 | Hold | No trials or literature specific to these subtypes. |
| 9 | Testicular yolk sac tumour, endodermal sinus pattern | 95.02% | L4 | Research Question | A single cohort study (PMID 11061887) describes clinical behaviour in stage I disease, not cisplatin efficacy. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

