---
layout: default
title: Rituximab
parent: 僅模型預測 (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Rituximab
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

# Rituximab: From B-Cell Non-Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

Rituximab is a chimeric anti-CD20 monoclonal antibody already established internationally for CD20-positive B-cell non-Hodgkin lymphoma and chronic lymphocytic leukaemia, though it does not currently hold an ARTG entry in Australia. The TxGNN model's top-ranked prediction is **Follicular Lymphoma**, backed by **50 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications**, with a prediction score of **96.08%**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Australian regulatory data (drug not registered); internationally, Rituximab is indicated for CD20-positive B-cell non-Hodgkin lymphoma and chronic lymphocytic leukaemia |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 96.08% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on well-established public information, Rituximab is a chimeric monoclonal antibody targeting CD20, a surface antigen expressed on mature B lymphocytes. It clears CD20-positive B cells through antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and induction of apoptosis.

Follicular lymphoma is itself a CD20-positive B-cell malignancy — arguably one of the closest possible matches to Rituximab's established mechanism, rather than a distant repurposing candidate. This is reflected in the depth of the evidence base: 50 registered clinical trials and 20 publications, including large completed Phase 3 randomised trials directly comparing Rituximab-containing regimens in this indication.

Because the mechanistic link (CD20 expression → antibody-mediated B-cell depletion) applies directly to follicular lymphoma, the strength of this prediction rests less on indirect inference and more on direct, confirmatory clinical evidence already accumulated for this drug-disease pairing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06097364](https://clinicaltrials.gov/study/NCT06097364) | Phase 3 | Active, not recruiting | 733 | OLYMPIA-2: odronextamab + chemotherapy vs Rituximab + chemotherapy in previously untreated follicular lymphoma |
| [NCT01476787](https://clinicaltrials.gov/study/NCT01476787) | Phase 3 | Completed | 1030 | RELEVANCE: Rituximab + lenalidomide vs Rituximab + chemotherapy in previously untreated follicular lymphoma |
| [NCT01650701](https://clinicaltrials.gov/study/NCT01650701) | Phase 3 | Completed | 1030 | RELEVANCE companion study confirming Rituximab + lenalidomide vs standard Rituximab-chemotherapy |
| [NCT05409066](https://clinicaltrials.gov/study/NCT05409066) | Phase 3 | Active, not recruiting | 549 | EPCORE FL-1: epcoritamab + Rituximab/lenalidomide vs Rituximab/lenalidomide alone in relapsed/refractory FL |
| [NCT04224493](https://clinicaltrials.gov/study/NCT04224493) | Phase 3 | Recruiting | 612 | Symphony-1: tazemetostat vs placebo added to Rituximab + lenalidomide in relapsed/refractory FL |
| [NCT01938001](https://clinicaltrials.gov/study/NCT01938001) | Phase 3 | Completed | 358 | Rituximab + lenalidomide vs Rituximab + placebo in relapsed/refractory indolent lymphoma |
| [NCT00006721](https://clinicaltrials.gov/study/NCT00006721) | Phase 3 | Active, not recruiting | 571 | CHOP + Rituximab vs CHOP + I-131 tositumomab in newly diagnosed follicular NHL |
| [NCT01701232](https://clinicaltrials.gov/study/NCT01701232) | Phase 3 | Completed | 174 | Rituximab biosimilar (BCD-020) vs reference MabThera monotherapy in indolent NHL |
| [NCT00460109](https://clinicaltrials.gov/study/NCT00460109) | Phase 2 | Completed | 24 | Denileukin diftitox + Rituximab in previously untreated follicular NHL |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Rituximab + bendamustine ± brentuximab vedotin in relapsed/refractory CD30+ DLBCL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40306831](https://pubmed.ncbi.nlm.nih.gov/40306831/) | 2025 | RCT | The Lancet Haematology | Long-term results: early Rituximab monotherapy vs watchful waiting in low tumour burden FL |
| [36255040](https://pubmed.ncbi.nlm.nih.gov/36255040/) | 2022 | Review | American Journal of Hematology | 2023 update on FL diagnosis and management |
| [31831752](https://pubmed.ncbi.nlm.nih.gov/31831752/) | 2019 | Review | Nature Reviews Disease Primers | Comprehensive review of FL biology and treatment |
| [33249059](https://pubmed.ncbi.nlm.nih.gov/33249059/) | 2021 | Review | Annals of Oncology | ESMO Clinical Practice Guidelines for FL diagnosis, treatment and follow-up |
| [28628883](https://pubmed.ncbi.nlm.nih.gov/28628883/) | 2017 | Review | Cancer Treatment Reviews | Pros and cons of Rituximab maintenance in FL |
| [29120553](https://pubmed.ncbi.nlm.nih.gov/29120553/) | 2017 | Review | Acta Clinica Croatica | Rituximab maintenance strategy in advanced FL |
| [35908982](https://pubmed.ncbi.nlm.nih.gov/35908982/) | 2023 | Review | Blood Reviews | Long-term treatment trajectory and biological understanding of FL |
| [37061956](https://pubmed.ncbi.nlm.nih.gov/37061956/) | 2023 | Review | Leukemia & Lymphoma | Update on FL biology and optimal therapy |
| [39374535](https://pubmed.ncbi.nlm.nih.gov/39374535/) | 2024 | Molecular study | Blood | Molecular subtyping of FL using RELEVANCE trial (Rituximab-chemo vs Rituximab-lenalidomide) samples |
| [36345167](https://pubmed.ncbi.nlm.nih.gov/36345167/) | 2022 | Systematic review/meta-analysis | Journal of Clinical Pharmacy and Therapeutics | Efficacy and safety of Rituximab biosimilars vs reference product as first-line therapy in low-tumour-burden FL |

---

## Australia Market Information

Rituximab does not currently hold an ARTG registration (Market Status: **Not Marketed**; 0 licence entries recorded). No product-level details (brand name, dosage form, approved indication text) are available from the regulatory data provided.

---

## Cytotoxicity

Rituximab is used in the treatment of B-cell malignancies (lymphoma/leukaemia) and is therefore included here for completeness, though as a monoclonal antibody it differs from conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications, or drug interaction data were available in this evidence pack (a TFDA/TGA labelling review is flagged as an outstanding, blocking data gap).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Follicular lymphoma has an L1 evidence level, underpinned by multiple completed Phase 3 RCTs (e.g. RELEVANCE, n=1030) directly testing Rituximab-containing regimens, plus a high TxGNN score (96.08%) and a mechanistically direct fit (CD20-positive B-cell malignancy). However, the drug is not currently registered in Australia and no formal safety labelling or MOA source data are yet available.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information for formal warnings, contraindications, and drug interaction review (S1 safety gate)
- DrugBank-sourced mechanism of action data to confirm and document the pharmacological rationale
- Confirmation of ARTG registration pathway/status, given the drug currently has zero Australian licence entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

