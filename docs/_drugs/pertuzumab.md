---
layout: default
title: Pertuzumab
parent: Model Prediction Only (L5)
nav_order: 564
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pertuzumab: predicted new indication Progesterone-receptor positive breast cancer (evidence level L5). Approved use: HER2-positive breast carcinoma"
monitor_inn: "Pertuzumab"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Pertuzumab
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

## Pertuzumab: From HER2-Positive Breast Carcinoma to Progesterone-Receptor Positive Breast Cancer
{: .text-alpha }

## One-Sentence Summary

Pertuzumab is a HER2-targeted monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, with **1 completed Phase 3 clinical trial** and **20 publications** currently supporting this direction.
This is largely an extension within the existing HER2-positive indication rather than true new-disease repurposing, because the benefit depends on HER2 status, not progesterone receptor (PR) status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The L1 rating is based on randomised Phase 3 and Phase 2 evidence. Only one completed Phase 3 trial is listed, and it is a biosimilar equivalence study. A strict reading of the rules (two or more completed Phase 3 RCTs) would be more conservative, so this rating should be read with caution.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pertuzumab binds HER2 subdomain II and blocks HER2/HER3 heterodimerisation. This inhibits PI3K/AKT and MAPK signalling in HER2-positive tumours.

Hormone receptor-positive/HER2-positive breast cancer is a molecular subset of the already approved HER2-positive breast cancer indication, so the mechanism applies directly. The effect depends on HER2 status rather than PR status. Cross-talk between the HER2 and hormone receptor pathways is described in the literature, which is why combinations with endocrine therapy are of interest.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Randomised, double-blind trial of the pertuzumab biosimilar QL1209 vs reference pertuzumab, each with trastuzumab and docetaxel, in early or locally advanced HER2-positive, ER/PR-negative breast cancer. This is a biosimilar equivalence comparison, not a test of a new indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | J Clin Oncol | Survival analysis of WSG TP-II: neoadjuvant trastuzumab + pertuzumab with endocrine therapy vs weekly paclitaxel in HR-positive/HER2-positive early breast cancer |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: endocrine therapy plus dual HER2 blockade vs de-escalated chemotherapy in HR-positive/HER2-positive early breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (Phase 2) | Lancet Oncol | NeoSphere 5-year analysis: progression-free and disease-free survival and safety of neoadjuvant pertuzumab plus trastuzumab |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 weeks of dual blockade with or without weekly paclitaxel |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | Br J Cancer | Phase 3 equivalence of pertuzumab biosimilar QL1209 vs reference pertuzumab in HER2-positive, ER/PR-negative disease |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | RCT | ESMO Open | Phase 3 equivalence of pertuzumab biosimilar TQB2440 vs reference pertuzumab |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | Review of HR-positive/HER2-positive breast cancer, including pathway cross-talk |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | Cohort | Breast | Retrospective study of ovarian function suppression plus aromatase inhibitors in premenopausal HR+/HER2+ patients |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer | Signalling pathway interactions and clinical translation in HR+/HER2+ breast cancer |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10267J | Perjeta | Solution for I.V. infusion 420 mg in 14 mL | Approved indication text not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody) |
| Myelosuppression Risk | Low as a single agent; haematological toxicity is mainly driven by the combined chemotherapy (e.g. docetaxel) |
| Emetogenicity Classification | Low |
| Monitoring Items | Left ventricular ejection fraction (cardiac function) before and during treatment; FBC, liver and renal function as required by the combined chemotherapy |
| Handling Protection | Please refer to the Product Information (PI) and local institutional policy |

---

## Safety Considerations

- **Drug Interactions**: A moderate interaction with idelalisib is recorded. The other interaction entry describes pertuzumab's pharmacological target (ERBB2/HER2), not a drug-drug interaction.
- **Cardiac safety**: Cardiac safety studies of pertuzumab, trastuzumab and chemotherapy (TRYPHAENA, BERENICE) are available in the literature. Cardiac monitoring is advised.
- **Pregnancy**: Reports of use during pregnancy are limited, so this requires specialist advice.

For key warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pertuzumab is already registered in Australia, and randomised evidence supports its use in HER2-positive breast cancer, including HR-positive subsets. The predicted indication falls within the existing HER2-positive indication, so the real question is HER2 status and treatment combination, not a new disease.

**To proceed, the following is needed:**
- Confirmation of HER2 positivity before treatment
- Cardiac function monitoring plan
- Review of endocrine therapy combinations for HR-positive/HER2-positive disease
- Confirmation of the approved indication wording from the ARTG entry and the TGA Product Information
- Mechanism of action data and PI-based warnings and contraindications, which are not yet available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

