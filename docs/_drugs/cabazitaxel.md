---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a next-generation taxane approved internationally for metastatic castration-resistant prostate cancer (mCRPC), acting as a microtubule-stabilising agent with a notably low susceptibility to P-glycoprotein–mediated drug resistance.
The TxGNN model predicts it may be effective for **female breast carcinoma**, supported by **no ClinicalTrials.gov-registered trials** retrieved in this query but **20 publications** — including at least two clinical trial reports — currently underpinning this direction.
Evidence quality is rated **L2**, reflecting at least one published Phase II randomised controlled trial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel is a semi-synthetic taxane derived from 10-deacetylbaccatin III that binds to and stabilises β-tubulin subunits within polymerised microtubules, preventing depolymerisation and thereby arresting dividing cancer cells in the G2/M phase. What distinguishes it from earlier taxanes is its markedly lower affinity for P-glycoprotein (Pgp) — the ATP-dependent efflux pump that underlies multidrug resistance in many solid tumours. This property allows cabazitaxel to retain activity in paclitaxel- and docetaxel-refractory cell lines and patient populations, a characteristic that was the basis of its original registration for docetaxel-pretreated mCRPC.

The mechanistic rationale for breast cancer is direct and well-supported. Taxanes are already standard-of-care in breast oncology, but tumour-associated taxane resistance — driven by Pgp overexpression or high levels of the βIII-tubulin isotype — limits durability. Preclinical evidence demonstrates that cabazitaxel is substantially less cross-resistant than paclitaxel or docetaxel in MDR cell models, including the MCF-7 breast cancer line (PMID 25416788), and that βIII-tubulin overexpression specifically enhances cabazitaxel's efficacy relative to docetaxel (PMID 28567478). For triple-negative breast cancer (TNBC) — a subtype with no targeted therapy and high relapse rates on standard taxanes — these properties are particularly compelling.

Beyond direct cytotoxicity, emerging data suggest a secondary immunomodulatory mechanism: cabazitaxel reprogrammes tumour-associated macrophages from an immunosuppressive M2 phenotype towards tumouricidal activity, synergising with CD47-targeted immunotherapy in TNBC preclinical models (PMID 33753567). Direct clinical trial evidence already exists in breast cancer, including the GENEVIEVE Phase II randomised trial comparing cabazitaxel versus weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer (PMID 28768217), and a Phase I/II dose-finding study in taxane- and anthracycline-pretreated metastatic breast cancer (PMID 21339064), providing a clinically actionable precedent.

---

## Clinical Trial Evidence

No trials were retrieved from the ClinicalTrials.gov or ICTRP registries for the cabazitaxel / female breast carcinoma query at the time of evidence collection. However, the following trials have been published in the peer-reviewed literature and are relevant to this evaluation:

| Published Trial | Phase | Design & Population | Key Findings |
|----------------|-------|---------------------|--------------|
| GENEVIEVE (PMID 28768217, 2017) | Phase II RCT | Cabazitaxel vs weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer (TNBC and luminal B/HER2-negative subtypes) | Directly compared pathological complete response (pCR) rates between arms; provides head-to-head evidence of cabazitaxel activity in breast cancer |
| Villanueva et al. (PMID 21339064, 2011) | Phase I/II | Multicentre dose-escalation of cabazitaxel + capecitabine in MBC progressing after anthracycline and taxane treatment | Established MTD, characterised safety profile (neutropenia, fatigue), and demonstrated preliminary antitumour activity in heavily pre-treated MBC |
| NCT01934894 (PMID 29678476, 2018) | Phase II | Cabazitaxel + lapatinib in HER2+ metastatic breast cancer with intracranial metastases | Exploited cabazitaxel's blood-brain barrier penetration alongside lapatinib's CNS activity; assessed CNS-specific outcomes |

> **Note:** Clinicians should search ClinicalTrials.gov and ANZCTR directly for currently active or recently completed registered trials, as the registry query conducted on 9 March 2026 may not reflect newly registered studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | European Journal of Cancer | GENEVIEVE trial: directly compared cabazitaxel vs weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer; primary endpoint was pathological complete response rate in TNBC and luminal B subtypes |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | European Journal of Cancer | Cabazitaxel + capecitabine dose-escalation in MBC pre-treated with taxanes and anthracyclines; determined MTD, pharmacokinetics, and early efficacy in a refractory population |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | Clinical Breast Cancer | Cabazitaxel + lapatinib in HER2+ MBC with CNS metastases (NCT01934894); evaluated the combination's activity against intracranial disease using both drugs' blood-brain barrier penetrating properties |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Mechanistic | Molecular Cancer Therapeutics | Characterised cabazitaxel resistance in MCF-7 breast cancer cell models; demonstrated substantially lower cross-resistance (9-fold) compared with paclitaxel (60-fold) and docetaxel in MDR variants |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Mechanistic | Cancer Chemotherapy and Pharmacology | βIII-tubulin isotype overexpression — a marker of taxane resistance and tumour aggressivity — differentially enhances cabazitaxel's binding and efficacy relative to docetaxel |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | Journal for Immunotherapy of Cancer | Cabazitaxel reprogrammes tumour-associated macrophages to enhance Programmed Cell Removal (PrCR) activity, synergising with CD47-targeted immunotherapy in TNBC models |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | PACA nanoparticle-encapsulated cabazitaxel demonstrated efficacy in patient-derived triple-negative breast cancer xenografts and was associated with reduction in immunosuppressive M2 macrophages |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | PEBCA nanoparticle-encapsulated cabazitaxel achieved complete remission in 6/8 patient-derived basal-like breast cancer xenografts, compared with 1/8 for equivalent free-drug dose |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs of Today | Comprehensive overview of cabazitaxel's pharmacokinetics, safety profile, Pgp resistance avoidance, and broad antitumour activity demonstrated across multiple cancer cell lines including breast |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | TDM-based dose individualisation for taxanes including cabazitaxel; reviews PK-PD relationships and pharmacological personalisation considerations relevant to optimal dosing in breast cancer populations |

---

## Australia Market Information

Cabazitaxel is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG) and has no approved product entries. It is not commercially marketed in Australia.

> Clinicians seeking access to cabazitaxel in Australia should consider the TGA Special Access Scheme (SAS Category B) for individual patients or apply through the TGA Clinical Trial Notification (CTN) scheme for investigational use.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (semi-synthetic taxane derivative; microtubule-stabilising mechanism) |
| Myelosuppression Risk | **High** — Grade 3/4 neutropenia reported in >50% of patients in pivotal prostate cancer trials; febrile neutropenia is a potentially fatal complication; G-CSF prophylaxis and dose modification protocols are routinely required |
| Emetogenicity Classification | Low to moderate (consistent with taxane class; IV infusion-related nausea more common than severe vomiting) |
| Monitoring Items | Full blood count with differential (mandatory prior to each treatment cycle, with absolute neutrophil count threshold); liver function tests; renal function (serum creatinine, eGFR); peripheral neurological assessment for neuropathy; hypersensitivity monitoring during infusion |
| Handling Protection | Preparation and administration must comply with cytotoxic drug handling regulations (SHPA Guidelines and ISOPP Standards); requires Class II biological safety cabinet; staff require full cytotoxic PPE (double gloves, chemotherapy-rated gown, eye/face protection); dedicated cytotoxic waste disposal |

---

## Safety Considerations

As cabazitaxel is not registered in Australia, no TGA-approved Product Information is available. Please refer to the **FDA-approved Prescribing Information (Jevtana®)** or the **EMA Summary of Product Characteristics** for comprehensive safety information, including myelosuppression management, hypersensitivity reactions, hepatic impairment precautions, and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least one Phase II randomised controlled trial (GENEVIEVE) has directly compared cabazitaxel against a standard-of-care taxane in HER2-negative breast cancer, and Phase I/II evidence exists for taxane- and anthracycline-refractory metastatic breast cancer, placing this at evidence level L2. The mechanistic rationale is well-established: Pgp resistance avoidance and βIII-tubulin advantage both directly address the primary chemotherapy resistance challenge in TNBC and luminal B subtypes. The complete absence of ARTG registration requires a formal access pathway before any clinical application in Australia.

**To proceed, the following is needed:**
- Initiation of a TGA Special Access Scheme (Category B) application or Clinical Trial Notification (CTN) to enable access in Australia
- Retrieval and review of the full FDA Prescribing Information (Jevtana®) or EMA SmPC to complete safety profiling — myelosuppression management protocols, contraindications, and drug interaction data are currently unavailable in this pack
- Clarification of the target breast cancer subtype population most likely to benefit (TNBC vs HER2+ with CNS involvement vs luminal B) based on subgroup data from GENEVIEVE and NCT01934894
- Development of a haematological monitoring and G-CSF prophylaxis protocol appropriate for the Australian clinical setting
- Assessment of whether any currently active Australian or New Zealand clinical trials (ANZCTR) are recruiting for cabazitaxel in breast cancer, to consider enrolment pathways ahead of standalone compassionate use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

