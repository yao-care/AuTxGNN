---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib (Rozlytrek®) is a multi-kinase inhibitor targeting NTRK1/2/3, ROS1, and ALK, internationally approved for NTRK fusion-positive solid tumours and ROS1-positive non-small cell lung cancer, but not currently registered in Australia.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)** (Prediction Score: 98.58%), though retrieved evidence — **2 clinical trials** and **1 publication** — has no direct relevance to MEN itself.
Notably, a separate TxGNN prediction for **Female Breast Carcinoma** (Rank 8) carries substantially stronger evidence at Level L2, with 5 clinical trials and 7 publications directly evaluating Entrectinib in NTRK- and ROS1-driven breast cancer subtypes; this is highlighted in the Conclusion as the higher-priority repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NTRK fusion-positive solid tumours; ROS1-positive NSCLC (FDA/EMA approved; not TGA-registered in Australia) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published literature, Entrectinib is a selective tyrosine kinase inhibitor (TKI) that binds to and inhibits TrkA (NTRK1), TrkB (NTRK2), TrkC (NTRK3), ROS1, and ALK. Its antitumour effect depends on the presence of oncogenic gene fusions involving these targets — it blocks constitutively active kinase signalling that drives uncontrolled cell proliferation. This is a tumour-agnostic mechanism: it targets the molecular alteration regardless of the tissue of origin.

Multiple Endocrine Neoplasia encompasses two main genetic syndromes. MEN1 is caused by loss-of-function mutations in the *MEN1* tumour suppressor gene, giving rise to parathyroid, pituitary, and pancreatic neuroendocrine tumours. MEN2 is driven by activating mutations in the *RET* proto-oncogene, primarily causing medullary thyroid carcinoma and phaeochromocytoma. The mechanistic link between Entrectinib and MEN is indirect at best: Entrectinib's established primary targets (NTRK/ROS1) are not the principal oncogenic drivers in MEN. While MEN1-associated pancreatic neuroendocrine tumours (pNETs) have occasionally been reported to harbour NTRK fusions, the prevalence is not well established. The sole retrieved publication (PMID 38438731) concerns resistance mechanisms to selective RET inhibitors in medullary thyroid carcinoma — relevant to MEN2 biology but not directly evaluating Entrectinib or NTRK/ROS1 pathways in this context.

The TxGNN model's prediction likely reflects knowledge graph proximity between neuroendocrine tumour biology and Entrectinib's NTRK target network. However, mechanistic validation in MEN-specific tumour models is needed before this prediction can be considered actionable.

---

## Clinical Trial Evidence

> **Important caveat:** Neither retrieved trial directly investigates Entrectinib in Multiple Endocrine Neoplasia. These results reflect cross-retrieval during evidence collection and are presented for transparency only.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, Not Recruiting | 65 | Neoadjuvant Entrectinib (ROS1 inhibition) plus endocrine therapy in invasive lobular breast carcinoma — not a MEN study; retrieved due to data integration overlap |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Precision medicine basket study terminated early after enrolment of only 2 participants — no usable data for any indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Translational/Basic Science | NPJ Precision Oncology | Describes adaptive off-target resistance mechanisms emerging under selective RET inhibitor therapy (selpercatinib/pralsetinib) in RET-driven cancers including medullary thyroid carcinoma — suggests alternative oncogene activation may play a role in treatment resistance, but does not evaluate Entrectinib or directly implicate NTRK/ROS1 pathways in MEN |

---

## Australia Market Information

Entrectinib is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no TGA-approved products for this drug in Australia.

> Entrectinib (Rozlytrek®) holds regulatory approval from the US FDA (2019) and the European Medicines Agency (EMA) for NTRK fusion-positive solid tumours and ROS1-positive NSCLC. Australian clinicians seeking access should explore the TGA Special Access Scheme (SAS Category B) or clinical trial pathways. TGA registration status should be verified directly at [www.tga.gov.au](https://www.tga.gov.au).

---

## Cytotoxicity

Entrectinib is an antineoplastic agent (targeted tyrosine kinase inhibitor) and the following considerations apply:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-kinase inhibitor (NTRK1/2/3, ROS1, ALK); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — neutropenia and anaemia are reported adverse events; thrombocytopenia is a recognised toxicity signal in clinical use (see Safety Considerations) |
| Emetogenicity Classification | Low to moderate — nausea reported in approximately 30% of patients in registration trials; vomiting also reported |
| Monitoring Items | Full blood count (FBC) with differential, liver function tests (LFTs), renal function, ECG (QTc interval), neurological and cognitive assessment, weight and BMI, bone health in long-term use and paediatric patients |
| Handling Protection | Follow standard cytotoxic handling precautions consistent with institutional guidelines for oral targeted cancer therapies |

---

## Safety Considerations

No TGA Product Information is currently available for Entrectinib in Australia. Clinicians should refer to the FDA Prescribing Information (Rozlytrek®) or EMA Summary of Product Characteristics as the primary safety reference.

Key safety signals identified from available literature include:

- **CNS adverse effects**: Dizziness, cognitive impairment, mood changes, and sleep disturbance are common, reflecting CNS penetration — a property that distinguishes Entrectinib from some other TKIs
- **Cardiac**: QTc interval prolongation has been reported; baseline and periodic ECG monitoring is warranted
- **Hepatotoxicity**: Elevated liver enzymes reported; monitor LFTs regularly
- **Bone and musculoskeletal**: Fractures reported, particularly in paediatric patients; evaluate bone health in long-term use
- **Thrombocytopenia**: A known adverse event across multiple clinical cohorts — this is a safety monitoring priority, **not** a therapeutic target (see Conclusion)

---

## Conclusion and Next Steps

**Decision: Hold (Research Question) — for Multiple Endocrine Neoplasia**

**Rationale:**
Despite a high TxGNN prediction score (98.58%), no clinical trial directly investigates Entrectinib in MEN, neither retrieved trial is relevant to the indication, and the sole publication addresses RET-pathway resistance without directly implicating NTRK or ROS1 in MEN biology. The mechanistic basis is speculative, and a preclinical proof-of-concept is needed before clinical translation can be considered.

---

### ⭐ Higher-Priority Repurposing Signal: Female Breast Carcinoma (Rank 8, Evidence Level L2)

This analysis has identified a substantially stronger repurposing opportunity within the same Evidence Pack. **Female Breast Carcinoma**, specifically:

- **Secretory carcinoma of the breast** with ETV6–NTRK3 gene fusion — a molecularly defined, directly targetable subtype (TrkC is Entrectinib's primary kinase target)
- **Invasive lobular carcinoma (ILC)** with ROS1 fusion — the subject of the ongoing Phase 2 ROSALINE trial (NCT04551495, n=65, ACTIVE_NOT_RECRUITING)

Supporting evidence includes the STARTRK-2 Basket Study (NCT02568267, Phase 2, n=534, ACTIVE_NOT_RECRUITING) which includes patients with NTRK fusion-positive breast cancer, plus 7 publications including a Phase 2 trial protocol (PMID 35695563) and preclinical data (PMID 38852701).

**Recommended decision for Female Breast Carcinoma: Proceed with Guardrails**

---

**To proceed with MEN (Research Question), the following is needed:**
- Systematic survey of NTRK fusion prevalence in MEN1-associated pancreatic neuroendocrine tumours (pNETs)
- Preclinical efficacy data in MEN1 and MEN2 tumour models
- Collaboration with endocrine oncology groups to identify potential biomarker-selected patient cohorts

**To proceed with Female Breast Carcinoma (recommended priority), the following is needed:**
- Await and review results from NCT04551495 (ROSALINE, Phase 2) expected completion January 2025 — follow up on publication
- Implement validated molecular screening (FISH, NGS) for NTRK3/ETV6 fusion (secretory carcinoma) and ROS1 fusion (ILC) in eligible patients
- Explore access via TGA Special Access Scheme (SAS Category B) for NTRK fusion-positive patients while formal TGA registration is pursued
- Establish safety monitoring plan including FBC, LFTs, QTc, and neurological assessment protocols aligned with international prescribing information
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

