---
layout: default
title: Imatinib
parent: Moderate Evidence (L3-L4)
nav_order: 369
evidence_level: L4
indication_count: 10
---

# Imatinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imatinib: From Chronic Myelogenous Leukaemia and GIST to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used for BCR-ABL1-positive chronic myelogenous leukaemia, gastrointestinal stromal tumour (GIST), dermatofibrosarcoma protuberans and related disorders.
The TxGNN model's top-ranked prediction is **heart fibrosarcoma**, but this is supported by **no clinical trials** and only **1 publication**, a general commentary that itself describes the evidence as not robust.
Of the ten predictions reviewed, the better-supported ones are fibroblastic neoplasm (mostly DFSP literature) and liposarcoma (three Phase 1/2 or Phase 2 sarcoma trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence data compiled for this report. The knowledge graph lists systemic mastocytosis, GIST, BCR-ABL1-positive chronic myelogenous leukaemia, chronic eosinophilic leukaemia, dermatofibrosarcoma protuberans and hypereosinophilic syndrome |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predictions reviewed**

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|---|---|---|---|---|
| 2 | Fibroblastic neoplasm | 99.94% | L3 | Proceed with Guardrails |
| 3 | Conventional fibrosarcoma | 99.93% | L4 | Hold |
| 4 | Kidney fibrosarcoma | 99.93% | L4 | Hold |
| 5 | Low grade fibromyxoid sarcoma | 99.93% | L5 | Hold |
| 6 | Liposarcoma | 99.88% | L2 | Research question |
| 7 | Liver fibrosarcoma | 99.86% | L4 | Hold |
| 8 | Familial Mediterranean fever (autosomal recessive) | 99.86% | L5 | Hold |
| 9 | Ovarian myxoid liposarcoma | 99.85% | L5 | Hold |
| 10 | Familial rhabdoid tumour | 99.83% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Imatinib is known to be a small-molecule tyrosine kinase inhibitor that blocks BCR-ABL, KIT and PDGFR kinases. Its efficacy in its original indications is established, and the literature in this report describes this inhibition as the basis for its activity in KIT/PDGFRA-driven GIST and PDGFB-driven dermatofibrosarcoma protuberans (DFSP).

**Heart fibrosarcoma (rank 1):** No heart-specific data were found. The only literature item is a 2008 general commentary on new imatinib indications. Any link would be indirect, through PDGFRB inhibition in COL1A1-PDGFB-driven fibroblastic tumours, and this has not been established for cardiac fibrosarcoma.

**Fibroblastic neoplasm (rank 2):** This has the strongest rationale. Most of the literature concerns DFSP, in which the COL1A1-PDGFB fusion drives constitutive PDGFRB activation that imatinib inhibits. However, this applies to the DFSP subset rather than to fibroblastic neoplasms generally. Imatinib-resistant cases (for example, CDKN2A loss with CDK4 dependence) show that benefit is not universal, so any extension to other tumours needs molecular confirmation.

**Other predictions:** For conventional fibrosarcoma, the evidence is extrapolated from DFSP and a preclinical liposome study. Liposarcoma is mainly driven by MDM2/CDK4 amplification, so the KIT/PDGFR rationale is weak. Low grade fibromyxoid sarcoma, myxoid liposarcoma and rhabdoid tumours are driven by other alterations (FUS-CREB3L2, FUS-DDIT3 and SMARCB1 loss respectively). Familial Mediterranean fever is an inflammasome disorder for which colchicine and IL-1 blockade are standard. These predictions are computational only.

---

## Clinical Trial Evidence

No trials are registered against the top-ranked prediction (heart fibrosarcoma). The trials below were linked to the lower-ranked predictions of liposarcoma and kidney fibrosarcoma. None gives indication-specific results in the data provided.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | Not reported | Imatinib in metastatic or unresectable soft tissue and bone sarcoma. Likely includes liposarcoma, but subtype results are not available |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Exploratory basket study of imatinib in life-threatening rare malignancies. Not specific to liposarcoma or kidney fibrosarcoma |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | Dose-finding and efficacy study in recurrent or refractory soft tissue sarcoma. Gives safety and dosing information, with no liposarcoma-specific efficacy |

No ANZCTR trial identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Heart fibrosarcoma (top-ranked prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Commentary on new imatinib indications, concluding that the evidence is not robust. No heart-specific data |

**Most relevant publications for the better-supported predictions**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | European interdisciplinary guideline update on DFSP diagnosis and treatment |
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Phase 2 trial | J Clin Oncol | Multicentre Phase II trial of imatinib across 10 sarcoma subtypes, using a Bayesian hierarchical model |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Cohort | BMC Cancer | 153 Chinese DFSP patients: COL1A1::PDGFB fusion prevalence and outcomes of Mohs surgery with postoperative imatinib |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Preclinical | Mol Cancer Ther | CDKN2A/p16 loss implicates CDK4 as a target in imatinib-resistant DFSP |
| [40558511](https://pubmed.ncbi.nlm.nih.gov/40558511/) | 2025 | Preclinical | Cells | Patient-derived cell line profiling predicts imatinib sensitivity in DFSP |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Preclinical | Drug Dev Res | Imatinib plus dexketoprofen liposomes against fibrosarcoma in a preclinical model |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Review | J Surg Oncol | Surgical management of DFSP. Imatinib can be used in advanced or unresectable disease |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opin Drug Saf | Development and application of imatinib |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | 2003 | Report | Ann Oncol | Potential use of imatinib in ocular melanoma and liposarcoma expressing c-KIT |
| [30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/) | 2018 | Case report | Anti-Cancer Drugs | Imatinib-induced DRESS in a DFSP patient, managed with desensitisation |

The literature is dominated by DFSP, which is already an approved indication, rather than by the predicted new diseases.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10915L | IMATINIB-DRLA | Capsule 100 mg (as mesilate) | Not stated in the data compiled for this report |

This is the only licence listed (one single-ingredient product, valid). The oral capsule is the only route available. The licence number is given as it appears in the data and is not in a standard ARTG format, so check it against the ARTG before relying on it.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, anaemia and agranulocytosis as contraindicated conditions |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | Full blood count, liver and renal function, and fluid status. Confirm in the PI |
| Handling Protection | Please refer to the PI and local cytotoxic handling policy |

---

## Safety Considerations

The product-label warnings and contraindications were not available for this report, so the items below come from other sources.

- **Knowledge graph contraindication associations** (not label text): hypertension, liver failure and liver disease, kidney disease, congestive and other heart failure, coronary artery disease, heart valve disease, congenital heart disease, pericardial effusion, pulmonary oedema, brain oedema, thrombocytopenia, neutropenia, agranulocytosis, anaemia, diabetes mellitus, diabetic ketoacidosis, hyperbilirubinaemia (including Gilbert syndrome), active peptic ulcer disease, gallbladder disease, obesity, hypophosphataemia and pyoureter. These should be verified against the PI.
- **Drug interactions:** the interaction search returned 100 records, and the main ones are:
  - **Major:** eliglustat and naloxegol.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), clarithromycin, cimetidine, aprepitant, lansoprazole and dexlansoprazole, glimepiride, pioglitazone and saxagliptin, morphine, naltrexone and naldemedine, and metreleptin.
- **Case report:** imatinib-induced drug reaction with eosinophilia and systemic symptoms (DRESS) has been reported in a DFSP patient.

Please refer to the TGA-approved Product Information (PI) for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, heart fibrosarcoma)

**Rationale:**
- There are no trials and only one non-specific commentary for heart fibrosarcoma. The high TxGNN score (99.94%) is not backed by clinical data. Most other predictions are also on Hold, apart from fibroblastic neoplasm (Proceed with Guardrails, but largely DFSP, which is already approved) and liposarcoma (a research question).

**To proceed, the following is needed:**
- Product label warnings, contraindications and approved indication text, which are missing for the Australian product
- Detailed mechanism of action data
- Molecular confirmation of PDGFB rearrangement or KIT/PDGFR activation in any target tumour before extending use beyond DFSP
- Subtype-specific efficacy data from the soft tissue sarcoma trials, particularly for liposarcoma
- A clinical review of cardiac safety, because heart failure and pericardial effusion appear among the contraindication associations and the top-ranked indication is a cardiac tumour
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

