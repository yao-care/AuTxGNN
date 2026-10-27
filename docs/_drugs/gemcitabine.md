---
layout: default
title: Gemcitabine
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gemcitabine: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Ovarian cancer"
monitor_inn: "Gemcitabine"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "endometrial mixed adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "mucin-rich endometrial endometrioid adenocarcinoma"]
---

# Gemcitabine
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

## Gemcitabine: From Ovarian Cancer to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Gemcitabine is a nucleoside analogue chemotherapy originally associated with ovarian cancer treatment.
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **40 clinical trials** and **20 publications** currently listed in the data compiled for this report, including a completed Phase 3 trial of gemcitabine plus paclitaxel in metastatic breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (the ARTG entry in the compiled data has no indication text; the original indication is taken from the knowledge-graph indication edges) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, gemcitabine is a nucleoside (pyrimidine) analogue that inhibits DNA synthesis and ribonucleotide reductase. This cytotoxic mechanism is not specific to one tumour type.

Its efficacy in ovarian cancer and other solid tumours is established, and mechanistically it may be applicable to breast carcinoma. The literature describes gemcitabine as an active agent in metastatic breast cancer. Single-agent response rates of 16% to 37% are reported, and higher response rates are reported in combination with platinum, taxanes, vinorelbine and anthracyclines.

Gemcitabine plus paclitaxel is already an established regimen in metastatic breast cancer. This is therefore less a speculative repurposing than a prediction supported by existing clinical use.

## Clinical Trial Evidence

The data list many trials. The table shows the 10 most relevant, prioritising those graded as directly relevant.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | Not reported | Randomised trial of gemcitabine plus paclitaxel versus paclitaxel in unresectable, locally recurrent or metastatic breast cancer |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | Completed | 4894 | Adjuvant trial in node-positive breast cancer comparing three regimens, one adding gemcitabine to dose-dense AC followed by paclitaxel |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial of adding capecitabine or gemcitabine to docetaxel before AC, with or without bevacizumab |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | Unknown | 800 | Neoadjuvant trial of epirubicin/cyclophosphamide then paclitaxel with or without gemcitabine in poor-risk early breast cancer |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Unknown | Not reported | tAnGo trial of adding gemcitabine to paclitaxel-containing, epirubicin-based adjuvant chemotherapy |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Phase 2 | Completed | 59 | Pemetrexed plus gemcitabine in metastatic breast cancer |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Nab-paclitaxel plus gemcitabine in metastatic breast cancer |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | Completed | 30 | Gemcitabine alone in metastatic breast cancer previously treated with doxorubicin and paclitaxel |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | Trilaciclib, pembrolizumab, gemcitabine and carboplatin in metastatic triple-negative breast cancer |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Phase 2 | Not yet recruiting | 750 | Gemcitabine versus paclitaxel in women of African ancestry with metastatic triple-negative breast cancer (planned start June 2027) |

**Note:** Only one Phase 3 trial (NCT00006459) is graded as directly relevant with completed status. No results data are included in the compiled data, so trial outcomes cannot be confirmed here. The L1 level assigned in the data, which normally requires at least two completed Phase 3 RCTs, should be verified against published results. NCT00093795 is also a completed Phase 3 trial.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine plus paclitaxel in metastatic breast cancer. About 52% response in phase II trials (114 of 221 patients), with phase III data |
| [12057042](https://pubmed.ncbi.nlm.nih.gov/12057042/) | 2002 | Review | Clin Breast Cancer | Gemcitabine plus cisplatin. Median response rate 43% in pretreated patients. Main toxicities were thrombocytopenia and neutropenia |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine and platinum compounds in metastatic breast cancer, with clinical benefit and response |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine plus docetaxel. Phase II data in metastatic breast cancer |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Gemcitabine, anthracycline and taxane combinations in advanced breast cancer |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Semin Oncol | Single-agent response rates of 16% to 37%. Higher rates in combinations |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Review | Clin Breast Cancer | Gemcitabine and trastuzumab in HER2-overexpressing metastatic breast cancer |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I trial | Breast Cancer Res Treat | Carboplatin, gemcitabine and mifepristone in advanced breast and recurrent epithelial ovarian cancer |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | Preclinical | Clin Breast Cancer | Gemcitabine with trastuzumab in breast and lung cancer cell lines |
| [28961673](https://pubmed.ncbi.nlm.nih.gov/28961673/) | 2017 | Case report | Retina | Gemcitabine-induced retinopathy (adverse event) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4439P | DBL Gemcitabine Injection | Solution for injection, 1 g (as hydrochloride) in 26.3 mL | Not stated in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside/pyrimidine analogue) |
| Myelosuppression Risk | Medium to high. Neutropenia and thrombocytopenia are the main toxicities reported in the literature |
| Emetogenicity Classification | Low to moderate, based on general drug class knowledge. Please refer to the Product Information (PI) |
| Monitoring Items | FBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, leukopenia, anaemia (including macrocytic anaemia), infectious disease, interstitial lung disease, haemolytic-uraemic syndrome (including typical form) and pyoureter.
- **Drug Interactions:** The data list 100 potential interactions. The main ones with an assigned severity are naltrexone (moderate) and levofloxacin (minor). The others shown (for example calcitriol, doxycycline, pantoprazole, metformin, morphine, prednisone, simvastatin and vancomycin) have unknown severity.
- **Reported adverse event:** A case report describes gemcitabine-induced retinopathy.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available in the compiled data. Please refer to the PI for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gemcitabine-containing regimens, including gemcitabine plus paclitaxel, have a completed Phase 3 trial in metastatic breast cancer and are supported by multiple reviews and Phase 2 studies. The product is marketed in Australia, but label safety data and results from the trials were not available.

**To proceed, the following is needed:**
- Review of the TGA-approved PI, including approved indications, warnings and contraindications (the ARTG entry has no indication text in the compiled data)
- Published outcome data from the Phase 3 trials (NCT00006459, NCT00093795) to confirm the evidence level
- Detailed mechanism of action data
- Confirmation of whether breast cancer is already an approved or guideline-supported use in Australia, including PBS listing criteria
- A safety monitoring plan covering myelosuppression, renal and hepatic function, and pulmonary toxicity

**Other predicted indications:** Rectum mucinous adenocarcinoma, colon mucinous adenocarcinoma, villoglandular endometrial endometrioid adenocarcinoma, rete ovarii adenocarcinoma and mucin-rich endometrial endometrioid adenocarcinoma have model prediction support only or unrelated literature (Hold). Endometrial mixed adenocarcinoma and endometrial mucinous adenocarcinoma have limited indirect supporting data (Research Question). Cervical mucinous adenocarcinoma and gallbladder mucinous adenocarcinoma have only indirect or case-report evidence (Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

