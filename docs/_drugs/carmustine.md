---
layout: default
title: Carmustine
parent: Model Prediction Only (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Carmustine
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

# Carmustine: From Lymphoma and Brain Tumours to Lymph Node Cancer

## One-Sentence Summary

Carmustine is a DNA-alkylating nitrosourea chemotherapy drug, used for lymphomas, glioblastoma and multiple myeloma.
The TxGNN model predicts it may be effective for **lymph node cancer**, with a high score of 98.5%.
Direct evidence for this label is weak: **1 clinical trial** (terminated, and mainly a breast cancer study) and **20 publications** (mostly breast cancer with nodal involvement) are linked to it.
Carmustine is already used in lymphoma, so this is closer to a confirmation of existing use than a true repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lymphomas (Hodgkin and non-Hodgkin, including mantle cell lymphoma), brain glioblastoma, plasma cell myeloma. The Australian licence record has no indication text, so this list comes from the knowledge graph used by TxGNN |
| Predicted New Indication | Lymph node cancer |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L3 (randomised and observational studies exist, but in related settings, not lymph node cancer itself) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Carmustine is known as a DNA-alkylating nitrosourea that crosslinks DNA and crosses the blood-brain barrier. Its efficacy in lymphoma is established, mainly as part of high-dose conditioning regimens (BEAM, CBV) before autologous stem cell transplant. Mechanistically it is plausible for malignancies of the lymph nodes.

"Lymph node cancer" is a broad label. In the evidence retrieved, it was matched mostly to breast cancer with many involved axillary nodes, where high-dose cyclophosphamide, cisplatin and carmustine with stem cell support was studied. One Hodgkin lymphoma intensification study was also retrieved. These are not studies of primary lymph node cancer, and carmustine's specific contribution is hard to separate from the combination regimens.

Because lymphoma is already among carmustine's original indications, the high score likely reflects existing use. It does not point to a new therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Randomised comparison of intensive sequential chemotherapy (doxorubicin, paclitaxel, cyclophosphamide) with high-dose chemotherapy and autologous stem cell support in primary breast cancer with 4-9 involved axillary lymph nodes. Carmustine's role is not clearly established. |

No ANZCTR trials were identified. This is the only trial linked to the predicted indication, and it was terminated before completion.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7577204](https://pubmed.ncbi.nlm.nih.gov/7577204/) | 1995 | RCT | J Natl Cancer Inst Monogr | CALGB 9082: high-dose versus low-dose cyclophosphamide, cisplatin and carmustine as consolidation in breast cancer with 10 or more involved nodes |
| [15767638](https://pubmed.ncbi.nlm.nih.gov/15767638/) | 2005 | Randomised trial report | J Clin Oncol | Prospective randomised comparison of high-dose chemotherapy with stem cell support versus intermediate-dose chemotherapy in high-risk primary breast cancer (CALGB 9082, SWOG 9114, NCIC MA-13) |
| [16118805](https://pubmed.ncbi.nlm.nih.gov/16118805/) | 2005 | Randomised trial (quality of life) | Cancer | Quality of life after high-dose versus intermediate-dose chemotherapy in stage II/III breast carcinoma with multiple positive nodes (CALGB 9066) |
| [18988286](https://pubmed.ncbi.nlm.nih.gov/18988286/) | 2008 | Randomised phase 2 | Cancer | Early versus late intensification in high-risk Hodgkin lymphoma, 158 patients, five-year results (GOELAMS) |
| [15505610](https://pubmed.ncbi.nlm.nih.gov/15505610/) | 2004 | Cohort | Biol Blood Marrow Transplant | Five-year results of high-dose cyclophosphamide, carmustine and thiotepa with autologous transplant in high-risk breast cancer |
| [12523579](https://pubmed.ncbi.nlm.nih.gov/12523579/) | 2002 | Phase 2 study | Biol Blood Marrow Transplant | High-dose chemotherapy with haematopoietic support in breast cancer with 4-9 involved nodes (61 patients) |
| [11895898](https://pubmed.ncbi.nlm.nih.gov/11895898/) | 2002 | Cohort | Clin Cancer Res | Pharmacokinetics of high-dose cyclophosphamide, cisplatin and carmustine in relation to survival and toxicity (85 women) |
| [8501500](https://pubmed.ncbi.nlm.nih.gov/8501500/) | 1993 | Clinical study | J Clin Oncol | High-dose cyclophosphamide, cisplatin and carmustine with autologous marrow support as consolidation in breast cancer with 10 or more nodes |
| [2642573](https://pubmed.ncbi.nlm.nih.gov/2642573/) | 1989 | Clinical study | Leukemia | BCNU, etoposide and cyclophosphamide with autologous marrow transplant in 23 patients with advanced Hodgkin's disease |
| [8484641](https://pubmed.ncbi.nlm.nih.gov/8484641/) | 1993 | Clinical study | Am Rev Respir Dis | Pulmonary drug toxicity in 23 of 59 patients (39%) given high-dose combination alkylator chemotherapy with marrow transplant |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8898H | Gliadel | Implants 7.7 mg, 8 | Indication text not listed in the record |

Only the Gliadel implant (a local wafer for brain tumours) appears in the Australian records compiled. No intravenous carmustine product, the form used in BEAM and CBV conditioning, was identified. Route compatibility for lymphoma or lymph node cancer is therefore unconfirmed.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrosourea class) |
| Myelosuppression Risk | High. Delayed and cumulative myelosuppression is expected with systemic or high-dose use |
| Emetogenicity Classification | High for intravenous use; the implant is local |
| Monitoring Items | FBC with differential, liver and renal function, and pulmonary function. Pulmonary toxicity was prominent in the retrieved high-dose studies |
| Handling Protection | Follow cytotoxic drug handling regulations |

This is a class-based summary. Please refer to the Product Information (PI) warnings and precautions for product-specific details.

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindication signals (knowledge graph, not label text)**: Associations include bone marrow and blood conditions (anaemia, leukopenia, thrombocytopenia, acute leukaemias), lung disease including pulmonary fibrosis, liver, kidney and gallbladder disease, infections (including fungal infection and meningitis), brain oedema, hydrocephalus, intracranial abscess and epilepsy.
- **Drug interactions**: 100 interactions were recorded. Of those shown, cimetidine is rated **Major**, naltrexone **Moderate** and levofloxacin **Minor**. Most others have an unspecified severity, including proton pump inhibitors, H2 blockers, corticosteroids, ondansetron, aprepitant, morphine and vancomycin.
- **Literature signals**: Pulmonary toxicity was common in high-dose regimens (39% in one series). Therapy-related acute leukaemia has also been reported after alkylator treatment of glioma.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence directly tied to "lymph node cancer" is one terminated, mainly breast cancer trial and breast cancer literature, which does not support a new indication.
- Carmustine's real value in lymphoma is already established through existing use in conditioning regimens, so the prediction adds little as a repurposing candidate.

**To proceed, the following is needed:**
- A precise disease definition for "lymph node cancer", for example the specific lymphoma subtype or nodal metastasis setting
- Trial or real-world data in which carmustine's own contribution is isolated
- Confirmation of the availability and registration status of intravenous carmustine in Australia
- Detailed mechanism of action data
- Label-based safety information (warnings, contraindications) from the TGA-approved PI, with a monitoring plan covering myelosuppression and pulmonary toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

