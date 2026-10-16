---
layout: default
title: Dasatinib
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dasatinib: predicted new indication Ewing sarcoma (evidence level L5). Approved use: Chronic myelogenous leukaemia…"
---

# Dasatinib
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

# Dasatinib: From BCR-ABL1-Positive Chronic Myeloid Leukaemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral tyrosine kinase inhibitor, originally used to treat BCR-ABL1-positive chronic myeloid leukaemia (CML), including the blast phase.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, but the evidence is thin: **2 clinical trials** (one terminated with 7 patients, one sarcoma-wide Phase 2) and **10 publications**, mostly preclinical or review articles.
The supporting evidence is mostly mechanistic (Src inhibition), and the sarcoma-wide Phase 2 trial reportedly showed dasatinib failed as a single agent in Ewing sarcoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukaemia, BCR-ABL1 positive (including blast phase) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (as scored in the data compiled; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

*Note: The data compiled for this report scored this prediction L2, but the only Phase 2 trial is a sarcoma-wide study with no Ewing-specific results supplied. A conservative reading is L4 (preclinical and mechanistic support). I have therefore recommended Hold.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, dasatinib is a multi-targeted kinase inhibitor acting on BCR-ABL and Src-family kinases, and also on c-KIT, PDGFR and ephrin receptor kinases. Its efficacy in BCR-ABL1-positive CML is established.

The link to Ewing sarcoma is through Src-family kinase signalling. Preclinical studies show Src (including the FAK-Src complex) drives invasion, migration and invadopodia formation in Ewing sarcoma cells. Dasatinib reduced proliferation and migration in Ewing sarcoma and other sarcoma cell lines, and induced apoptosis in bone sarcoma cells that depend on Src.

The rationale is plausible but clinical benefit is not demonstrated. A review notes that dasatinib failed as a single agent in Ewing sarcoma and rhabdomyosarcoma in a Phase 2 sarcoma study. Interest has since shifted to combinations, such as the RIST regimen (rapamycin, irinotecan, dasatinib, temozolomide) in relapsed disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Paediatric trial of dasatinib with ifosfamide, carboplatin and etoposide. Terminated early, so little usable safety or efficacy information. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas, measuring response rate and 6-month progression-free survival. Sarcoma-wide; Ewing-specific results were not supplied. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Targeting the FAK-Src complex in DSRCT, Ewing sarcoma and rhabdomyosarcoma; single-agent dasatinib failed in the Phase 2 sarcoma study. |
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | Case series | J Pediatr Hematol Oncol | Single-centre descriptive experience with the RIST regimen (including dasatinib) in relapsed Ewing sarcoma. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncol Lett | Src signalling as a potential drug target in sarcoma. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Curr Treat Options Oncol | Systemic therapy for chondrosarcoma (limited direct relevance to Ewing sarcoma). |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncol Rep | Dasatinib showed antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Res | Dasatinib inhibited migration and invasion in sarcoma cell lines and induced apoptosis in Src-dependent bone sarcoma cells. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | In vitro | Neoplasia | Microenvironmental stress activates Src-dependent invadopodia and migration in Ewing sarcoma. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | In vitro | Neoplasia | Tenascin C and Src cooperate to promote invadopodia formation in Ewing sarcoma. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | In vitro | Cell Commun Signal | Plerixafor promoted proliferation of Ewing sarcoma cell lines (not directly about dasatinib). |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case report | Case Rep Oncol | Chromosome abnormality in CML blast crisis (not relevant to Ewing sarcoma). |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12842X | DASATINIB-TEVA | Tablet 100 mg (oral) | Not stated in the data compiled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, anaemia and agranulocytosis among contraindication-linked conditions. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential, liver function, and cardiac assessment (QT interval, signs of heart failure and pericardial effusion), per the PI |
| Handling Protection | Please refer to the PI and local cytotoxic or hazardous drug handling policies |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for definitive safety information.

- **Conditions linked to contraindications in a knowledge graph (not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia, congestive heart failure, myocardial infarction, coronary thrombosis, pericardial effusion, haemopericardium, intracerebral haemorrhage, active peptic ulcer disease and haemoglobinopathy. These should be verified against the PI.
- **Drug interactions:** 100 interactions were recorded; the first 20 are shown here.
  - **Major:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole (acid suppression), dexamethasone, acetylsalicylic acid, clarithromycin.
  - **Moderate:** hydrocortisone, budesonide, loperamide, aprepitant, bisacodyl, magnesium oxide, aluminium hydroxide, calcium carbonate, castor oil, polyethylene glycol, saxagliptin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Src-based mechanism is plausible and preclinical data are supportive, but the only clinical evidence is a sarcoma-wide Phase 2 trial in which single-agent dasatinib reportedly failed in Ewing sarcoma, and a trial terminated at 7 patients. There is no evidence of benefit in the new indication.

**To proceed, the following is needed:**
- Ewing-specific results from NCT00464620 and NCT00788125.
- Evidence for combination approaches (such as RIST) from prospective trials rather than a single-centre case series.
- Mechanism of action data and the TGA Product Information safety content (warnings and contraindications).
- Confirmation of the approved indication text for the Australian ARTG entry.

---

### Other Predicted Indications (for context)

- **Myeloid leukaemia (score 99.68%, evidence L1, Proceed with Guardrails):** most of the evidence (for example, DASISION and other Phase 3 CML trials) overlaps with the already approved CML indication, so it is not true repurposing. The genuinely new signal is acute myeloid leukaemia, particularly core-binding factor AML, where a 2026 Phase 3 trial of dasatinib added to chemotherapy has been published but its outcome was not stated in the data supplied.
- **Liposarcoma, dermatofibrosarcoma protuberans:** preclinical or review evidence only (L4, Hold).
- **Gingival fibromatosis, ovarian myxoid liposarcoma, ganglioneuroblastoma and others:** model prediction only (L5, Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

