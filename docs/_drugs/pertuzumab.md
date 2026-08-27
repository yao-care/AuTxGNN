---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Pertuzumab (DrugBank DB06366) is an anti-HER2 monoclonal antibody whose established use is in HER2-positive breast cancer.
> The TxGNN model's top-ranked prediction — **progesterone-receptor positive breast cancer** — is best understood as a receptor-status refinement within pertuzumab's existing HER2-positive breast cancer population rather than a genuinely new disease target,
> with **10 clinical trials** (including 2 completed Phase 3 RCTs) and **20 publications** currently supporting the mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer *(inferred from repurposing rationale text; not separately confirmed via ARTG licence data — see note below)* |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed *(0 ARTG entries recorded in this evidence pack)* |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data was not returned by the DrugBank query for this evidence pack. However, the underlying repurposing analysis for this candidate explicitly documents pertuzumab's mechanism: it is a HER2-targeted monoclonal antibody that blocks heterodimerisation of HER2 with HER1/HER3/HER4, interrupting downstream HER2 signalling. This mechanism is already well established as the basis for pertuzumab's approved use in HER2-positive breast cancer.

Progesterone-receptor (PR) status is a hormone-receptor stratification variable measured alongside HER2 status in breast cancer, not a distinct disease entity. A tumour that is "PR-positive breast cancer" and HER2-positive sits squarely within the population pertuzumab already targets — the predicted indication therefore represents an extension/refinement of an existing approved-use population rather than a mechanistically novel repurposing candidate. This explains both the very high TxGNN score and the unusually strong evidence base (multiple completed Phase 3 trials) for what is nominally a "new" indication.

Because of this overlap, the clinical trial and literature evidence below should be read as supporting pertuzumab's activity in HER2-positive/PR-positive disease specifically (as a biomarker-defined subgroup), rather than as evidence for a mechanistically unrelated new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Randomised, double-blind biosimilar (QL1209) vs pertuzumab, both with trastuzumab + docetaxel, in HER2-positive/ER/PR-negative early-stage breast cancer. |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050 — atezolizumab vs placebo added to neoadjuvant anthracycline/taxane + trastuzumab + pertuzumab in early HER2-positive breast cancer. |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant comparison of Herceptin ± docetaxel ± pertuzumab in locally advanced/inflammatory/early HER2-positive breast cancer; pathological complete response endpoint. |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Biosimilar (BCD-178) vs Perjeta as neoadjuvant therapy for HER2-positive breast cancer without ER/PR expression. |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab preoperative therapy, studying impact of HER2 heterogeneity on treatment response. |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023 — neoadjuvant lapatinib + trastuzumab with/without endocrine therapy, 12 vs 24 weeks, in HER2-overexpressing breast cancer. |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO — de-escalated neoadjuvant chemotherapy plus SC pertuzumab/trastuzumab in HER2-positive, ER-negative, node-negative early breast cancer. |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective multicentre study of HER2-low prevalence and treatment patterns in HER2-negative metastatic breast cancer (indirect relevance). |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | NEOADAPT — chemotherapy-free neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab in HR-positive (incl. PR+), HER2-positive early breast cancer. |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Single-arm neoadjuvant paclitaxel response-rate study in Nigerian women with breast cancer (pertuzumab not central). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II — endocrine therapy + trastuzumab/pertuzumab vs de-escalated chemotherapy in HR-positive/HER2-positive early breast cancer. |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT | Future Oncology | DECRESCENDO — de-escalating chemotherapy in HER2-positive, hormone receptor-negative, node-negative early breast cancer. |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2) | J Clin Oncol | PERTAIN — trastuzumab + aromatase inhibitor ± pertuzumab in HER2-positive and hormone receptor-positive metastatic/locally advanced breast cancer. |
| [37723497](https://pubmed.ncbi.nlm.nih.gov/37723497/) | 2023 | Cohort | World J Surg Oncol | Real-world retrospective study (China) finding PR status a more decisive factor than ER status for pertuzumab benefit in HER2-positive, node-positive breast cancer. |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer. |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort | Lancet Oncology | NeoSphere 5-year follow-up — neoadjuvant pertuzumab + trastuzumab in HER2-positive breast cancer. |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | Phase 3 equivalence trial | British J Cancer | QL1209 (pertuzumab biosimilar) vs reference pertuzumab, both + trastuzumab + docetaxel, in HER2-positive, ER/PR-negative breast cancer. |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 trial | Annals of Oncology | WSG-ADAPT HER2+/HR- — 12-week neoadjuvant dual HER2 blockade ± paclitaxel. |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | Systematic Review | Int J Mol Sciences | Pertuzumab + trastuzumab + docetaxel as adjuvant doublet therapy for HER2-positive breast cancer. |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Review | Southern Medical Journal | Overview of neoadjuvant and adjuvant therapies across breast cancer molecular subtypes, including HER2-enriched disease. |

---

## Australia Market Information

This evidence pack records **no ARTG entries** and a market status of **Not Marketed** for pertuzumab. No product name, dosage form, or approved-indication text was retrievable from the regulatory data source used to build this pack. This should be treated as a data gap requiring verification rather than a confirmed regulatory finding, since pertuzumab-containing products are marketed in a number of jurisdictions internationally — the current TGA/ARTG registration status should be confirmed directly against the TGA product database before any decision is finalised.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were returned for pertuzumab in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is met on the strength of two completed Phase 3 RCTs (NCT04629846, NCT03726879) directly evaluating pertuzumab-based regimens in this receptor-defined population, supported by a further eight trials and ten relevant publications, including one real-world study specifically addressing PR status as a predictor of pertuzumab benefit (PMID 37723497). However, because PR-positive status sits within pertuzumab's existing HER2-positive breast cancer population rather than representing a mechanistically distinct disease, this candidate should be framed as a biomarker-defined subgroup confirmation rather than novel repurposing.

**To proceed, the following is needed:**
- TGA-approved Product Information — warnings/precautions and contraindications (flagged as a **Blocking** data gap; required before any S1 safety assessment can proceed)
- Confirmed, structured mechanism-of-action data from DrugBank (High-priority gap; current MOA description was reconstructed from rationale text, not a primary source field)
- Verification of actual TGA/ARTG registration status for pertuzumab in Australia, given the "Not Marketed / 0 ARTG entries" result is inconsistent with pertuzumab's known international marketing status and should be checked directly against the TGA database
- Confirmation of drug interaction data (currently returned as not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

