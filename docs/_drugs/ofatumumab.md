---
layout: default
title: Ofatumumab
parent: High Evidence (L1-L2)
nav_order: 485
evidence_level: L1
indication_count: 10
---

# Ofatumumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ofatumumab: From Not Yet Marketed in Australia to Predicted Use in Chronic Lymphocytic Leukaemia/Small Lymphocytic Lymphoma

## One-Sentence Summary

Ofatumumab (DrugBank: DB06650) is a fully human anti-CD20 monoclonal antibody, currently **not marketed in Australia** (ARTG listed count: 0), with local initial approved indication data not yet available.
The TxGNN model predicts it may be used for **chronic lymphocytic leukaemia/small lymphocytic lymphoma (CLL/SLL)**,
which represents an established international evidence-based use direction for ofatumumab, currently supported by **34 related clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications**.
A secondary direction—follicular lymphoma—is supported by multiple Phase 2 trials with the same mechanism, detailed below.

---

## Key Overview

| Item | Content |
|------|---------|
| Original Indication | No local (Australian) approved indication data available; drug not currently marketed in Australia |
| Predicted New Indication | Chronic lymphocytic leukaemia/small lymphocytic lymphoma (CLL/SLL) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Australian Market Status | Not marketed |
| ARTG Registration Count | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why This Prediction Is Reasonable

According to the mechanism-of-action information in the evidence package, ofatumumab is a fully human anti-CD20 monoclonal antibody that eliminates CD20-positive B lymphocytes through complement-dependent cytotoxicity (CDC) and antibody-dependent cellular cytotoxicity (ADCC). CLL/SLL is a CD20-positive B-cell malignancy with a mechanism directly corresponding to this target. This indication represents an approved use in some international markets; the "Not marketed" designation here reflects only the Australian regulatory registration status, not uncertainty regarding therapeutic efficacy.

The supporting evidence is substantial: completed Phase 3 RCTs include NCT00824265 (ofatumumab plus fludarabine-cyclophosphamide vs. FC alone, n=365, relapsed CLL), NCT02004522 (duvelisib vs. ofatumumab head-to-head, n=319), and NCT01578707 (ibrutinib vs. ofatumumab, RESONATE, n=391), meeting the L1 evidence threshold (≥2 completed Phase 3 RCTs).

Within the same drug evidence package, a secondary direction—"follicular lymphoma" (TxGNN score 99.70%, evidence level L2)—shares the same mechanism (CD20+ B-cell lymphoma) and is supported by multiple Phase 2 trials (e.g., NCT01190449, NCT01294579) demonstrating efficacy in treatment-naive populations, suitable for future tracking. Other predicted indications—sebaceous carcinoma, Langerhans cell histiocytosis, histiocytic/dendritic cell tumours, and childhood mediastinal neurogenic tumours—carry evidence level L5 and decision stage S0. Lacking any trial or literature support and unrelated to CD20 expression by cell origin, the evidence package itself has flagged these as model noise; they are recommended for exclusion and not included in the primary scope of this report.

Note: Detailed MOA data (DrugBank query) and TFDA/PI product information warnings remain gaps (DG001, DG002), with DG001 classified as Blocking level. This affects progression to safety assessment (S1); even though efficacy evidence reaches L1, final decision awaits closure of this gap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolled | Primary Finding |
|----------|-------|--------|----------|-----------------|
| [NCT00824265](https://clinicaltrials.gov/study/NCT00824265) | Phase 3 | Completed | 365 | Ofatumumab plus fludarabine-cyclophosphamide vs. FC alone, evaluating safety and efficacy in relapsed CLL |
| [NCT02004522](https://clinicaltrials.gov/study/NCT02004522) | Phase 3 | Completed | 319 | DUO trial: duvelisib vs. ofatumumab head-to-head comparison, relapsed/refractory CLL/SLL |
| [NCT01578707](https://clinicaltrials.gov/study/NCT01578707) | Phase 3 | Completed | 391 | RESONATE trial: ibrutinib vs. ofatumumab, evaluating PFS in relapsed/refractory CLL/SLL |
| [NCT01313689](https://clinicaltrials.gov/study/NCT01313689) | Phase 3 | Completed | 122 | Ofatumumab vs. physician's choice of treatment in bulky fludarabine-refractory CLL confirmatory trial |
| [NCT01039376](https://clinicaltrials.gov/study/NCT01039376) | Phase 3 | Terminated | 480 | Ofatumumab maintenance vs. observation in relapsed CLL patients responsive to induction therapy |
| [NCT01217749](https://clinicaltrials.gov/study/NCT01217749) | Phase 1b/2 | Completed | 71 | BTK inhibitor (PCI-32765) combined with ofatumumab, relapsed/refractory CLL/SLL |
| [NCT02049515](https://clinicaltrials.gov/study/NCT02049515) | Phase 3 | Completed | 99 | Duvelisib or ofatumumab monotherapy in patients with prior progression from early-phase studies (extension trial) |
| [NCT01453062](https://clinicaltrials.gov/study/NCT01453062) | N/A | Completed | 1 | European real-world observational study, CLL patients receiving ofatumumab treatment |
| [NCT01520922](https://clinicaltrials.gov/study/NCT01520922) | Phase 2 | Completed | 99 | Ofatumumab combined with bendamustine, treatment-naive or relapsed CLL |
| [NCT01024010](https://clinicaltrials.gov/study/NCT01024010) | Phase 2 | Completed | 82 | Ofatumumab combined with pentostatin and cyclophosphamide, treatment-naive CLL/SLL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Finding |
|------|------|------|---------|------------|
| [31512258](https://pubmed.ncbi.nlm.nih.gov/31512258/) | 2019 | RCT (long-term follow-up) | American Journal of Hematology | RESONATE trial final analysis, ibrutinib vs. ofatumumab in previously treated CLL/SLL, 6-year follow-up results |
| [37138022](https://pubmed.ncbi.nlm.nih.gov/37138022/) | 2023 | Meta-analysis | Annals of Hematology | Systematic review assessing overall efficacy of ofatumumab in treating CLL |
| [25828085](https://pubmed.ncbi.nlm.nih.gov/25828085/) | 2015 | Review | Haematologica | Review of ofatumumab's role in immunotherapy for CLL |
| [20481657](https://pubmed.ncbi.nlm.nih.gov/20481657/) | 2010 | Review | Drugs | Pharmacological characteristics review of ofatumumab, including key fludarabine/alemtuzumab-refractory CLL studies |
| [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/) | 2015 | Review (safety) | Expert Opinion on Drug Safety | Safety analysis of ofatumumab in CLL treatment |
| [25736010](https://pubmed.ncbi.nlm.nih.gov/25736010/) | 2015 | Guideline | Journal of the National Comprehensive Cancer Network | CLL/SLL treatment guidelines including ofatumumab as approved monoclonal antibody option |
| [20068404](https://pubmed.ncbi.nlm.nih.gov/20068404/) | 2009 | Review | mAbs | Drug overview of ofatumumab, including CLL approval application background |
| [28782884](https://pubmed.ncbi.nlm.nih.gov/28782884/) | 2017 | Review | American Journal of Hematology | CLL diagnosis, risk stratification and treatment updates |
| [29212732](https://pubmed.ncbi.nlm.nih.gov/29212732/) | 2018 | Review | The Oncologist | Role of anti-CD20 monoclonal antibodies (including ofatumumab) in CLL treatment and biosimilar considerations |
| [24947256](https://pubmed.ncbi.nlm.nih.gov/24947256/) | 2014 | Review | Future Oncology | Discussion of ofatumumab positioning as first-line therapy in treatment-naive CLL |

---

## Australian Market Information

Ofatumumab is currently **not registered in the Australian Register of Therapeutic Goods (ARTG)**, with no approved formulations or indications on record.

---

## Cytotoxicity Information

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted/immunotherapy (anti-CD20 monoclonal antibody, not conventional chemotherapy) |
| Myelosuppression Risk | Refer to approved product information (PI) warnings and precautions |
| Emetogenic Classification | Refer to approved product information (PI) warnings and precautions |
| Monitoring Parameters | Refer to approved product information (PI) warnings and precautions |
| Handling and Protection | Refer to approved product information (PI) warnings and precautions |

---

## Safety Considerations

No warnings, contraindications, or drug interaction data are currently available. Please refer to the TGA-approved product information (PI) for safety information.

---

## Conclusions and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CLL/SLL indication direction is supported by multiple completed Phase 3 RCTs (meeting L1 evidence level), with clear mechanism and approved use in some markets; however, detailed TFDA/PI product information warnings and mechanism-of-action data remain gaps (product information warnings classified as Blocking-level gap). Complete safety assessment (S1) has not yet been performed; until this gap is closed, listing as Go is not recommended.

**Supplementary Requirements for Progression:**
- Obtain TFDA (or corresponding TGA) product information warnings and contraindications to complete S1 safety assessment
- Close MOA data gaps from DrugBank to strengthen mechanism-of-action analysis
- If considering progression to the secondary direction of follicular lymphoma, separately evaluate whether its evidence level (currently L2) is sufficient to support subsequent decision stages

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

