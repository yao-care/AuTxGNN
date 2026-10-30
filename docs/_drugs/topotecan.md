---
layout: default
title: Topotecan
parent: Model Prediction Only (L5)
nav_order: 739
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Topotecan"
predicted_indications: ["female breast carcinoma", "adult germ cell tumor"]
description: "Topotecan: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Topotecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Topotecan: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Topotecan is a topoisomerase I inhibitor chemotherapy originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but the supporting evidence is thin: **3 registered clinical trials** (all early-phase or terminated, none breast-specific in design) and a literature set dominated by reviews and preclinical work, including one older Phase 2 study reporting no evidence of increased efficacy in advanced breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. Based on established pharmacology, topotecan inhibits topoisomerase I, causing DNA strand breaks and replication-associated cell death in rapidly dividing tumour cells.

Both ovarian and breast cancers are gynaecological-axis malignancies, and topoisomerase I inhibition is mechanistically plausible in breast cancer. A 2023 study (PMID 37987734) reported that TOP1 inhibition in MYC-driven cancer promotes aberrant R-loop accumulation and synthetic lethality, which may be relevant to MYC-amplified or triple-negative breast cancer. Topotecan is also a substrate of the BCRP/ABCG2 efflux transporter, which is expressed in breast cancer and may contribute to resistance.

Clinical support is limited, however. The listed trials are Phase 1 or terminated Phase 2 combination studies, and older literature on continuous infusional topotecan reports no evidence of increased efficacy in advanced breast cancer. The high TxGNN score should be read as a hypothesis, not as confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | Not reported | Intensive-dose topotecan, ifosfamide/mesna and etoposide (TIME) followed by autologous stem cell rescue in metastatic breast cancer; terminated, and the multi-drug design cannot isolate topotecan's contribution |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with several standard chemotherapies (topotecan among them) in advanced malignancies; combination safety data only |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Phase 1 | Recruiting | 426 | First-in-human study of PHST001 alone or with anticancer therapies in advanced solid tumours; topotecan's role and breast cancer relevance unconfirmed, no efficacy data yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase 2 trial | Br J Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot study | Onkologie | Topotecan as primary chemotherapy for brain metastases in metastatic breast cancer |
| [9425961](https://pubmed.ncbi.nlm.nih.gov/9425961/) | 1997 | Review | Semin Oncol | Potential role of topotecan in advanced breast cancer |
| [25236865](https://pubmed.ncbi.nlm.nih.gov/25236865/) | 2015 | Review | AAPS J | BCRP/ABCG2 efflux transporter; topotecan is a substrate, a possible resistance mechanism |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical | Cancer Res | TOP1 inhibition in MYC-driven breast cancer models induces R-loop accumulation and synthetic lethality |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | Preclinical | Biochem Pharmacol | BCRP/MXR/ABCP expression in topotecan-resistant breast carcinoma cells |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical | Anticancer Res | Xenograft comparison of doxorubicin, cisplatin, irinotecan and topotecan in colon, lung and breast tumours |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Preclinical | J Surg Res | Quercetin combined with topotecan in MCF-7 and MDA-MB-231 breast cancer cells |
| [39657238](https://pubmed.ncbi.nlm.nih.gov/39657238/) | 2024 | Preclinical | ACS Appl Mater Interfaces | Topotecan-loaded drug-gene nanoparticles for metastatic breast cancer |
| [27084985](https://pubmed.ncbi.nlm.nih.gov/27084985/) | 2016 | Review/Commentary | Aging | Metronomic chemotherapy for triple-negative breast cancer |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4617B | Hycamtin | Powder for I.V. infusion 4 mg (as hydrochloride) | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor, camptothecin class) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | FBC with differential, renal function, liver function; monitor for diarrhoea and respiratory symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the Product Information (PI) warnings and precautions for formal guidance.

## Safety Considerations

Formal warnings and contraindications from the approved Product Information were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

**Knowledge graph contraindication signals** (these come from a research knowledge graph, not label text): thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), interstitial lung disease, diarrhoeal disease, impaired renal function, pulmonary fibrosis and post-inflammatory pulmonary fibrosis.

**Drug interactions:** 100 interactions were identified; the sample reviewed included:
- **Major:** deferiprone, samarium (153Sm) lexidronam
- **Moderate:** eliglustat, rolapitant, iobenguane (I-131), palifermin, strontium chloride Sr-89, ibritumomab tiuxetan
- **Minor:** levofloxacin, caffeine
- **Severity not classified:** morphine, omeprazole, lansoprazole, prednisolone, ranitidine, ondansetron, famotidine, palonosetron, metoclopramide, dexamethasone

Combining topotecan with other myelosuppressive agents or radiopharmaceuticals warrants particular caution.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9992), but the trials are early-phase or terminated combination studies, and the only dedicated Phase 2 breast cancer study of topotecan found no evidence of increased efficacy. Evidence is at most L3 and does not yet justify clinical development in breast cancer. Topotecan is already marketed in Australia (one ARTG entry), so the barrier is evidence of benefit, not availability.

**To proceed, the following is needed:**
- Prospective breast cancer-specific efficacy data, ideally in biomarker-defined groups (for example MYC-amplified or triple-negative disease)
- A review of the full Hycamtin Product Information, including approved indications, warnings and contraindications
- Detailed mechanism of action data
- Evaluation of BCRP/ABCG2-mediated resistance as a limiting factor
- A safety and monitoring plan covering myelosuppression, diarrhoea, lung toxicity and renal impairment, with attention to drug interactions

**Other predicted indications:** The data also list adult germ cell tumour (score 0.9957, evidence level L2, though the retrieved studies are mostly paediatric neuroblastoma, glioma and retinoblastoma, with a single small Phase 2 combination trial, NCT00002814, n=20, needing verification). This is not assessed further here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

