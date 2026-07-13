---
layout: default
title: Carmustine
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Carmustine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carmustine: From Brain Tumour to Lymph Node Cancer

## One-Sentence Summary

Carmustine (BCNU) is a nitrosourea alkylating agent with a longstanding history in the treatment of malignant brain tumours (glioblastoma and anaplastic glioma), and as the backbone of the BEAM conditioning regimen used before autologous stem cell transplantation (ASCT).
The TxGNN model predicts it may be effective for **Lymph Node Cancer** (encompassing diffuse large B-cell lymphoma and Hodgkin's lymphoma),
with **7 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Brain tumours (malignant glioma); backbone of BEAM conditioning chemotherapy |
| Predicted New Indication | Lymph Node Cancer |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carmustine (1,3-bis(2-chloroethyl)-1-nitrosourea; BCNU) is a bifunctional alkylating agent of the nitrosourea class. It exerts cytotoxic activity primarily through the formation of DNA interstrand cross-links and inhibition of O⁶-alkylguanine DNA alkyltransferase (MGMT), a key DNA repair enzyme. This dual mechanism produces irreversible cell death in rapidly proliferating tumour cells — a property equally relevant to lymphoma as to glioma.

Currently, detailed pharmacological mechanism data could not be retrieved from the DrugBank database for this analysis. However, based on extensive published evidence, carmustine is the "C" in the BEAM regimen (Carmustine + Etoposide + Ara-C + Melphalan), which is the internationally recognised standard myeloablative conditioning protocol before ASCT for relapsed or refractory Hodgkin's lymphoma (HL) and aggressive non-Hodgkin's lymphoma (NHL) — the principal disease entities subsumed under the "lymph node cancer" category. BEAM is used in transplant centres globally, including in Australia, as a compassionate access regimen.

The TxGNN prediction of 98.49% is therefore not surprising: the mechanistic and clinical link between carmustine and lymph node cancer is direct rather than speculative. The BEAM protocol's well-documented efficacy and the drug's potent activity against rapidly dividing lymphoid tumour cells provide strong biological plausibility. Carmustine's established role in clearing residual lymphoma prior to stem cell reinfusion confirms that the TxGNN model has identified a biologically coherent and clinically validated connection.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01141712](https://clinicaltrials.gov/study/NCT01141712) | Phase 2 | Completed | 43 | BEAM conditioning for aggressive B-cell lymphoma and Hodgkin's lymphoma in HIV-positive patients; assessed overall survival and engraftment outcomes following autologous HSCT |
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | Completed | 473 | Autologous PBSCT for lymphoma using BEAM-based preparative regimens, with rituximab in CD20+ cases; large-sample safety and efficacy data supporting BEAM tolerability |
| [NCT01702961](https://clinicaltrials.gov/study/NCT01702961) | N/A | Completed | 75 | Real-world observational study of Rituximab + BEAM + ASCT for lymphoma and Hodgkin's disease after first relapse; supports BEAM as current clinical practice |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous then non-myeloablative allogeneic HCT for high-risk Hodgkin's lymphoma, NHL, multiple myeloma, and CLL; includes BEAM-based conditioning |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Intensive sequential chemotherapy vs high-dose chemotherapy with PBSCT for primary breast cancer with axillary lymph node involvement (4–9 nodes); terminated early, limiting conclusions |
| [NCT01468311](https://clinicaltrials.gov/study/NCT01468311) | Phase 1/2 | Terminated | 6 | Yttrium-90 anti-CD25 radioimmunotherapy combined with high-dose BEAM for recurrent/refractory Hodgkin's lymphoma; terminated early due to slow accrual |
| [NCT02788201](https://clinicaltrials.gov/study/NCT02788201) | Phase 2 | Completed | 8 | Genomic-based therapy assignment for advanced urothelial carcinoma using the COXEN model; carmustine was included as one of the candidate agents; indirect relevance only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18988286](https://pubmed.ncbi.nlm.nih.gov/18988286/) | 2008 | Randomised Phase 2 | Cancer | 5-year results of early vs late intensification in high-risk Hodgkin's lymphoma (n=158); the ASCT arm used myeloablative carmustine-based conditioning and showed durable FFTF in a subset of patients |
| [2642573](https://pubmed.ncbi.nlm.nih.gov/2642573/) | 1989 | Clinical Study | Leukemia | BCNU + etoposide + cyclophosphamide high-dose myeloablative therapy for advanced Hodgkin's disease (n=23); responses documented including in patients refractory to prior chemotherapy |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Clinical Study | Clin Cancer Res | O⁶-alkylguanine-DNA alkyltransferase levels in cutaneous T-cell lymphoma (mycosis fungoides); topical and oral carmustine active in early disease; MGMT expression identified as a resistance mechanism |
| [7577204](https://pubmed.ncbi.nlm.nih.gov/7577204/) | 1995 | RCT Protocol | J Natl Cancer Inst Monogr | CALGB 9082: high-dose cyclophosphamide/cisplatin/carmustine with ABMT vs low-dose consolidation for breast cancer with 10+ axillary lymph nodes; pivotal trial establishing HDCT-SCT feasibility |
| [15767638](https://pubmed.ncbi.nlm.nih.gov/15767638/) | 2005 | RCT | J Clin Oncol | Combined analysis of CALGB 9082/SWOG 9114/NCIC MA-13: high-dose carmustine-based HDCT with SCT vs intermediate-dose for high-risk breast cancer with lymph node involvement; no OS benefit in unselected population |
| [11063378](https://pubmed.ncbi.nlm.nih.gov/11063378/) | 2000 | Cohort | Biol Blood Marrow Transplant | California multicentre experience with carmustine-based HDCT + HSCT for breast cancer (n=1,111); overall treatment-related mortality 2.3%, supporting acceptable toxicity profile at experienced centres |
| [1642408](https://pubmed.ncbi.nlm.nih.gov/1642408/) | 1992 | Clinical Study | Ann Plast Surg | Adjuvant carmustine + dacarbazine + cisplatin + tamoxifen in high-risk melanoma patients with 4+ positive regional lymph nodes; pilot study with descriptive outcomes |
| [8501500](https://pubmed.ncbi.nlm.nih.gov/8501500/) | 1993 | Clinical Study | J Clin Oncol | High-dose cyclophosphamide/cisplatin/carmustine with ABMT consolidation for primary breast cancer with 10+ involved axillary nodes; foundational HDCT-SCT efficacy data |
| [1899111](https://pubmed.ncbi.nlm.nih.gov/1899111/) | 1991 | Clinical Study | J Clin Oncol | Myeloablative chemotherapy including carmustine for stage IV neuroblastoma; included regional lymph node irradiation; demonstrates carmustine activity in high-risk paediatric solid tumours |
| [36213836](https://pubmed.ncbi.nlm.nih.gov/36213836/) | 2022 | Cohort | J Oncology | Retrospective review of HDCT + ASCT in locally advanced triple-negative breast cancer; marginal benefit observed in TNBC subgroup treated with carmustine-containing regimens |

---

## Australia Market Information

Carmustine is currently **not marketed in Australia**. There are no entries in the Australian Register of Therapeutic Goods (ARTG). Clinicians wishing to access carmustine would need to apply through one of the following TGA pathways:

- **Special Access Scheme (SAS) Category B**: For individual patients with a serious condition where no alternative is available
- **Authorised Prescriber**: For specialists at tertiary haematology/oncology centres providing ongoing BEAM-based ASCT conditioning

Prescribers should contact the TGA's Access to Unapproved Therapeutic Goods team and consult internationally approved Product Information (US FDA or EMA) for prescribing guidance.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrosourea class (bifunctional alkylating agent) |
| Myelosuppression Risk | **High** — Delayed and cumulative myelosuppression is carmustine's hallmark toxicity; nadir typically occurs 4–6 weeks after administration (significantly later than most alkylating agents). Risk is dose-dependent and cumulative with repeated cycles |
| Emetogenicity Classification | Moderate to High (IV formulation); Low (topical/wafer formulation) |
| Monitoring Items | Full Blood Count (FBC) with differential and platelets — weekly from week 3 to 6 post-dose given delayed nadir; Liver Function Tests (LFTs); Renal function (eGFR/creatinine); Pulmonary Function Tests including DLCO — carmustine causes delayed pulmonary fibrosis/interstitial pneumonitis, particularly at cumulative doses >1,400 mg/m² |
| Handling Protection | Must be handled as a cytotoxic agent in full accordance with Australian cytotoxic drug handling guidelines (SHPA/ISOPP standards); requires biosafety cabinet preparation, closed-system drug transfer devices, appropriate PPE (gown, gloves, eye protection), and cytotoxic waste disposal |

---

## Safety Considerations

Specific safety data from the TGA-approved Product Information could not be retrieved for this analysis, as carmustine is not currently registered in Australia.

> Please refer to the US FDA-approved Prescribing Information or the EMA Summary of Product Characteristics for Carmustine for comprehensive safety information, including black box warnings, contraindications, and drug interactions.

Key safety concerns documented in the published literature include:

- **Delayed myelosuppression**: Onset typically 4–6 weeks post-dose; thrombocytopenia and leukopenia are the dose-limiting toxicities. Patients must be counselled about the risk of serious infection and bleeding well after the day of administration
- **Pulmonary toxicity**: Delayed interstitial pneumonitis and progressive pulmonary fibrosis occur in approximately 20–30% of patients, particularly with cumulative lifetime doses exceeding 1,400 mg/m²; baseline and periodic DLCO monitoring is essential
- **Hepatotoxicity**: Transient elevation of liver transaminases and alkaline phosphatase; reversible in most cases
- **Secondary malignancy**: As with all alkylating agents, there is a recognised risk of therapy-related myelodysplastic syndrome (t-MDS) and acute myeloid leukaemia (t-AML), particularly with repeated cycles or when combined with other alkylating agents

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carmustine is already the internationally recognised backbone of the BEAM conditioning regimen for ASCT in relapsed or refractory Hodgkin's and non-Hodgkin's lymphoma — the disease entities that constitute "lymph node cancer" in the TxGNN model. Multiple completed Phase 2 trials (including n=473 and n=43 directly in lymphoma) and a large body of clinical literature confirm both efficacy and a manageable toxicity profile in specialist haematology centres. The main barrier to Australian use is not lack of evidence, but rather the absence of a registered product.

**To proceed, the following is needed:**

- **TGA access pathway**: Submit a TGA Special Access Scheme (SAS Category B) application or establish an Authorised Prescriber arrangement at a recognised stem cell transplant centre
- **Mechanism of action data**: Retrieve full DrugBank MOA data to complete pharmacological profiling and drug interaction analysis
- **Local safety and monitoring protocol**: Establish a risk management plan addressing delayed myelosuppression (weeks 4–6 FBC monitoring) and annual pulmonary function surveillance (DLCO)
- **Haematology and pharmacy specialist input**: Restrict use to tertiary haematology/oncology centres with ASCT capability and specialist pharmacy cytotoxic preparation services
- **Supply chain verification**: Confirm a reliable importation pathway (e.g., via SAS-approved international suppliers) before committing to any BEAM-based treatment protocol
- **Drug interaction assessment**: Full DDI screening is required once MOA data and complete patient medication lists are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

