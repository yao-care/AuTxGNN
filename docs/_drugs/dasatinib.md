---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Myeloid Leukaemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib (Sprycel®) is a multi-targeted tyrosine kinase inhibitor (TKI) with well-established use in chronic myeloid leukaemia (CML) and Philadelphia chromosome-positive (Ph+) acute lymphoblastic leukaemia, functioning by blocking BCR-ABL, Src family kinases, c-KIT, and PDGFR.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction.
The strongest clinical evidence comes from a completed Phase 2 trial in advanced sarcomas (NCT00464620, n=366), though Ewing sarcoma-specific subgroup data requires confirmation from the primary publication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukaemia (CML) and Ph+ Acute Lymphoblastic Leukaemia — inferred from clinical evidence; no Australian ARTG registration |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this data package. Based on published clinical and preclinical literature, dasatinib is an orally bioavailable small-molecule inhibitor of multiple tyrosine kinases — including BCR-ABL, Src family kinases (Lyn, Hck, Fyn), c-KIT, and PDGFR-α/β — and is approximately 325-fold more potent than imatinib against wild-type BCR-ABL in vitro. Its primary oncology role exploits BCR-ABL inhibition in CML, but its broad kinase profile makes it mechanistically relevant across other tumour types.

The mechanistic link to Ewing sarcoma centres on Src kinase signalling. Multiple independent in vitro studies (2007–2022) consistently show that microenvironmental stresses — such as hypoxia and mechanical pressure — persistently activate Src in Ewing sarcoma cells, driving invadopodia formation, cell migration, and invasion, which are key steps in metastatic progression (PMID 27566104, PMID 31521948). Dasatinib's inhibition of the Src/FAK complex directly disrupts this pathway, demonstrating antiproliferative and antimigratory activity in Ewing sarcoma cell lines (PMID 18202781, PMID 17363602). The extracellular matrix protein tenascin-C has been specifically identified as cooperating with Src in promoting invadopodia, reinforcing the specificity of this signalling axis in Ewing sarcoma biology.

While Ewing sarcoma and CML differ substantially, both are linked through Src kinase dependency. The completed Phase 2 trial NCT00464620 (n=366, advanced sarcomas) provides the most clinically relevant evidence to date, though it enrolled a mixed sarcoma population. The TxGNN prediction is well-grounded in this mechanistic framework, and the convergence of multiple independent preclinical datasets over 15 years supports the biological plausibility of this repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas (largest dedicated sarcoma dasatinib trial); evaluated response rate and 6-month progression-free survival. Enrolled a mixed sarcoma population including Ewing sarcoma. Ewing subgroup results require primary publication (Schuetze et al.) for formal confirmation. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib in combination with ifosfamide, carboplatin, and etoposide in paediatric solid tumours including Ewing sarcoma. Terminated early due to poor enrolment; provides preliminary paediatric safety signals only — no efficacy conclusions drawn. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy in children and young adults with relapsed or refractory solid tumours (B7-H3 positive), including Ewing sarcoma. Dasatinib's role in this context is as a CAR-T off-target toxicity management agent, not as a direct antitumour therapy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro preclinical | Cancer Research | Dasatinib inhibits migration and invasion across diverse human sarcoma cell lines; induces apoptosis in bone sarcoma cells (including Ewing) dependent on Src kinase for survival. Foundational preclinical study. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro preclinical | Oncology Reports | Dasatinib demonstrates antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines via c-KIT and PDGFR inhibition. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | In vitro | Neoplasia | Microenvironmental stress drives Src-dependent invadopodia formation and cell migration in Ewing sarcoma; identifies Src as a key metastatic driver and therapeutic target. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | In vitro | Neoplasia | Tenascin-C and Src cooperate to promote invadopodia in Ewing sarcoma under microenvironmental stress, reinforcing the disease-specific rationale for Src-targeted therapy. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | In vitro / Translational | Sarcoma | FAK-Src complex targeting in Ewing sarcoma, DSRCT, and rhabdomyosarcoma; dasatinib single-agent activity is limited but combination strategies with FAK inhibitors show preclinical promise. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signalling in sarcoma biology; discusses Src's role in proliferation, apoptosis, invasion, and metastasis, and its feasibility as a drug target in sarcoma. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | In vitro | Cell Communication and Signaling | CXCR4 antagonism with plerixafor paradoxically activates receptor tyrosine kinase signalling in Ewing sarcoma, highlighting the complexity of the signalling network and potential combination targeting opportunities. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Current Treatment Options in Oncology | Systemic therapy review for chondrosarcoma; contextual reference to Src/PDGFR inhibition in the broader sarcoma treatment landscape. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case Report | Case Reports in Oncology | Rare chromosomal abnormality in CML blast crisis treated with dasatinib; limited direct relevance to Ewing sarcoma but provides general dasatinib pharmacological context. |

---

## Cytotoxicity

Dasatinib is a targeted anticancer agent (tyrosine kinase inhibitor) indicated for malignant haematological conditions and with investigational use in solid tumours. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL / Src family kinase inhibitor (small-molecule TKI; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia are commonly reported in CML clinical trials; monitor closely in sarcoma patients who may have prior myelosuppressive treatment |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests (LFTs), renal function, electrolytes; pulmonary function and chest imaging (pleural effusion is a well-recognised dasatinib-associated adverse event); cardiac monitoring (QT interval) |
| Handling Protection | Standard institutional cytotoxic drug handling precautions apply; dasatinib is an oral tablet — PPE and safe handling per local cytotoxic guidelines are recommended |

---

## Safety Considerations

No TGA-approved Australian Product Information (PI) is available, as dasatinib is not currently registered on the ARTG. All formal warning and contraindication data fields are unavailable from this data package.

Please refer to the current **FDA-approved Prescribing Information** or **EMA Summary of Product Characteristics (SmPC)** for Sprycel® (dasatinib) for complete safety information, including contraindications, warnings, and drug interaction data.

Clinically important safety signals identified in the supporting literature include:
- **Pleural effusion**: A well-recognised and relatively common dasatinib-associated adverse event — reported in a substantial proportion of CML patients on long-term therapy
- **Chylothorax**: Rare lymphatic complication (PMID 36448074)
- **Interstitial pneumonitis**: Rare but serious pulmonary adverse event requiring monitoring and dose adjustment or cessation (PMID 36346055)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for dasatinib in Ewing sarcoma is coherent and supported by 15 years of convergent preclinical evidence targeting the Src/FAK axis, and the completed Phase 2 trial NCT00464620 (n=366) provides an initial clinical signal in advanced sarcomas. However, Ewing sarcoma–specific subgroup efficacy data has not been formally confirmed, and dasatinib is not registered in Australia — which introduces regulatory and access barriers for clinical use.

**To proceed, the following is needed:**

- **Primary publication review**: Obtain and critically appraise the Ewing sarcoma subgroup data from NCT00464620 (Schuetze et al.) to confirm clinical activity in this specific histology
- **Full safety profiling**: Access dasatinib PI from FDA or EMA to complete formal safety, contraindication, and drug interaction review
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB01254) to support mechanistic linkage analysis
- **Dedicated clinical evidence**: Consider whether a Ewing sarcoma–specific Phase 2 trial is feasible and warranted, given that existing evidence is largely from mixed-sarcoma populations
- **Australian regulatory pathway**: If pursuing use in Australia, explore the TGA Special Access Scheme (SAS) or Clinical Trial Notification (CTN) pathway, as no ARTG entry currently exists
- **Combination strategy evaluation**: Given that dasatinib single-agent activity in sarcomas appears limited (PMID 35655525), evaluate evidence for combination regimens (e.g., with FAK inhibitors or standard chemotherapy backbones) before proceeding to clinical use

---

> **⚠️ Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Any drug repurposing candidate requires rigorous clinical validation before therapeutic application. All clinical decisions should be made in accordance with applicable regulatory requirements and professional medical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

