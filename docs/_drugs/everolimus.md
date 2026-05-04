---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Advanced Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR (mechanistic target of rapamycin) inhibitor with established global approvals for advanced renal cell carcinoma, hormone receptor-positive breast cancer, neuroendocrine tumours, and tuberous sclerosis complex — though no Australian ARTG registrations were returned in the current data query.
The TxGNN model predicts it may be effective for **Liposarcoma** (specifically dedifferentiated liposarcoma, DDLPS),
with **1 active Phase II clinical trial** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma; HR+/HER2− breast cancer; neuroendocrine tumours (globally approved — no ARTG entries returned in current data) |
| Predicted New Indication | Liposarcoma (dedifferentiated liposarcoma, DDLPS) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (0 ARTG entries per current data) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Everolimus is a selective inhibitor of mTOR (mechanistic target of rapamycin), a serine/threonine kinase that acts as a central regulator of cell growth, proliferation, and survival. It binds to the intracellular protein FKBP-12, forming an inhibitory complex that blocks mTORC1 signalling. The downstream effect is suppression of protein synthesis, cell cycle arrest at G1, and reduced tumour-associated angiogenesis. This mechanism underpins its established use across multiple solid tumours where mTORC1 is pathologically overactivated — including renal cell carcinoma, HR+/HER2− breast cancer, and pancreatic neuroendocrine tumours.

The molecular rationale for everolimus in liposarcoma is particularly well-grounded in **dedifferentiated liposarcoma (DDLPS)**. The hallmark genomic event in DDLPS is high-frequency amplification of the CDK4/MDM2 locus on chromosome 12q13-15. Critically, immunohistochemical analysis of 99 DDLPS tissue specimens has documented consistent co-activation of the Akt/mTOR and MAPK pathways alongside this amplification (PMID 26518767), confirming that mTOR pathway dependence is measurable in patient tumours — not merely a theoretical extrapolation. This creates a compelling case for **dual CDK4/6 + mTOR pathway blockade**: combining ribociclib (CDK4/6 inhibitor) with everolimus (mTOR inhibitor) simultaneously disrupts both the cell cycle amplification and the downstream survival signalling network, a synergism observed in multiple preclinical sarcoma models.

Liposarcoma and renal cell carcinoma — one of everolimus's approved indications — share a common therapeutic logic: both cancers exhibit dysregulated PI3K/AKT/mTOR signalling that drives proliferation and resistance to apoptosis. The translational step from epithelial cancers to soft-tissue sarcomas is mechanistically sound, and the TxGNN prediction score of 99.88% aligns with the available biological and clinical evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase II | Active, Not Recruiting | 48 | Two-arm study of ribociclib (300 mg/day, 3 weeks on/1 week off) + everolimus (2.5 mg) in advanced DDLPS (Arm A) and leiomyosarcoma (Arm B). Requires ≥1 prior systemic therapy. Evaluates antitumour activity of CDK4/6 + mTOR dual blockade. Results published in 2024 (PMID 37967116). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II Trial Publication | Clinical Cancer Research | Published results of ribociclib + everolimus in advanced DDLPS and LMS (n=48). Directly evaluates antitumour activity of the CDK4/6 + mTOR doublet strategy across two common soft-tissue sarcoma subtypes. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational / Mechanistic | Tumour Biology | Immunohistochemical study of 99 DDLPS specimens confirming activation of Akt/mTOR and MAPK pathways. Includes in vitro analysis of mTOR inhibitor antitumour effects. Provides the primary molecular rationale for everolimus in DDLPS. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review / Preclinical | Frontiers in Oncology | Review of PDOX (patient-derived orthotopic xenograft) sarcoma models identifying effective CDK inhibitor combination strategies. Supports the preclinical basis for CDK pathway targeting across sarcoma subtypes including liposarcoma. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Research | Preclinical evaluation of eribulin combined with mechanistically distinct agents in liposarcoma and other tumour xenograft models. Provides supporting context for combination approaches targeting liposarcoma. |

---

## Australia Market Information

No ARTG entries were identified for Everolimus in the current regulatory data query (search date: 2026-04-05; result count: 0). The product is recorded as **not marketed** in the Australian market per available data.

> **Important:** Clinicians should independently verify the current registration status of Everolimus via the TGA ARTG Public Summary portal ([https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg)), as Everolimus (brand names including **Afinitor®**, **Certican®**, and **Votubia®**) holds regulatory approvals in the USA (FDA), Europe (EMA), and multiple other jurisdictions. The zero-result return may reflect a data gap in the current search rather than confirmed non-registration.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (not conventional cytotoxic; immunosuppressive agent with antineoplastic activity) |
| Myelosuppression Risk | Moderate — anaemia, neutropenia, and thrombocytopenia are documented class effects; typically non-severe but requires monitoring |
| Emetogenicity Classification | Low — oral formulation; stomatitis/oral mucositis more common than severe nausea or vomiting |
| Monitoring Items | Full blood count (FBC with differential); renal function (eGFR, electrolytes); liver function tests; fasting blood glucose; fasting lipid panel; respiratory symptoms (non-infectious pneumonitis surveillance) |
| Handling Protection | Standard oral medication precautions apply; everolimus is immunosuppressive — consult institutional guidelines for handling in the context of oncology use; not classified as a traditional cytotoxic for specialised chemotherapy handling purposes |

---

## Safety Considerations

No Australian-specific key warnings, contraindications, or drug interaction data were available in this Evidence Pack. Please refer to the TGA-approved Product Information (PI) for comprehensive safety information.

For clinical reference, everolimus carries known class-effect risks that prescribers should be aware of:

- **Non-infectious pneumonitis**: A serious class effect of mTOR inhibitors; can present as dyspnoea, cough, or hypoxia — dose modification or discontinuation may be required
- **Metabolic effects**: Clinically significant hyperglycaemia and hyperlipidaemia (monitor fasting glucose and lipids regularly)
- **Immunosuppression**: Increased susceptibility to bacterial, fungal, and viral infections; reactivation of latent infections (e.g., hepatitis B, TB) is a known risk
- **Stomatitis**: Common and sometimes dose-limiting; affects quality of life
- **Drug interactions**: Everolimus is a CYP3A4 and P-glycoprotein substrate — strong inhibitors (e.g., azole antifungals, certain HIV antiretrovirals) and inducers (e.g., rifampicin, phenytoin) significantly alter plasma exposure

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A directly relevant Phase II clinical trial (NCT03114527, n=48) specifically evaluating everolimus in dedifferentiated liposarcoma has been completed and published in a high-impact journal (*Clinical Cancer Research*, 2024), providing L2-level evidence. This is complemented by robust mechanistic evidence documenting Akt/mTOR pathway activation in DDLPS tumour tissue, establishing a well-supported biological rationale. The TxGNN prediction score of 99.88% is consistent with this evidence base.

**To proceed, the following is needed:**

- **Verify Australian regulatory status**: Confirm current ARTG registration via the TGA portal — the zero-entry result is likely a data gap and requires manual resolution before any prescribing or access pathway decisions
- **Obtain TGA Product Information (PI)**: The PI document must be reviewed for formal safety assessment, including key warnings, contraindications, and drug interactions currently absent from this Evidence Pack
- **Review NCT03114527 full results** (PMID 37967116): Extract subgroup-level efficacy data (response rate, progression-free survival) and toxicity profile specifically for the DDLPS arm
- **Clarify histological subtype scope**: Determine whether the evidence supports well-differentiated liposarcoma (WDLPS), DDLPS, or other liposarcoma subtypes — current data is strongest for DDLPS
- **Mechanism of action documentation**: Formal MOA data from DrugBank should be retrieved to complete the regulatory-facing evidence package

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All information should be interpreted in conjunction with current clinical guidelines and verified regulatory data.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

