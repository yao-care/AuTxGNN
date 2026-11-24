---
layout: default
title: Pertuzumab
parent: Model Prediction Only (L5)
nav_order: 564
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Pertuzumab"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab: predicted new indication Ectomesenchymoma (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Pertuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## One-Sentence Summary

Pertuzumab is a HER2-targeted monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
This is largely an extension within the existing HER2-positive indication rather than true new-disease repurposing, because the benefit depends on HER2 status, not progesterone receptor (PR) status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ectomesenchymoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 (as assigned in the data compiled for this report; see note below) |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The L1 rating is based on randomised Phase 3 and Phase 2 evidence. Only one completed Phase 3 trial is listed, and it is a biosimilar equivalence study. A strict reading of the rules (two or more completed Phase 3 RCTs) would be more conservative, so this rating should be read with caution.

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pertuzumab: "Pertuzumab targets the extracellular dimerization domain (Subdomain II) of the human epidermal growth factor receptor 2 protein (HER2) and, thereby, blocks ligand-dependent heterodimerization of HER2 with other HER family members, including EGFR, HER3, and HER4. As a result, pertuzumab inhibits ligand-initiated intracellular signaling through two major signal pathways, mitogen-activated protein (MAP) kinase, and phosphoinositide 3-kinase (PI3K)." ([DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff), label version 2026-04-30; accessed 2026-11-19.) Based on known pharmacology, pertuzumab binds HER2 subdomain II and blocks HER2/HER3 heterodimerisation. This inhibits PI3K/AKT and MAPK signalling in HER2-positive tumours.

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

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 10267J | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 10308M | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 10333W | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 10334X | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 15369X | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 15386T | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 15402P | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |
| 15411D | Perjeta | Pertuzumab | Solution for I.V. infusion 420 mg in 14 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

