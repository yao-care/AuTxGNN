---
layout: default
title: Ipilimumab
parent: Model Prediction Only (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ipilimumab: predicted new indication Non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "Ipilimumab"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
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

## Ipilimumab: From Metastatic Melanoma to Non-Cutaneous Melanoma
{: .text-alpha }

## One-Sentence Summary

Ipilimumab is a CTLA-4 checkpoint-blocking antibody, originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (mucosal, uveal and conjunctival subtypes), with **22 registered clinical trials** and **6 publications** retrieved for this indication. Most of this evidence comes from mixed melanoma populations or combination regimens rather than ipilimumab alone, so this is better described as an extension within the melanoma family than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (the ARTG indication text is not available in the data compiled for this report) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L1 as assigned by the automated scoring; a manual reading suggests L2 (see below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked prediction:** The highest-scoring prediction is choroideremia (99.06%). It has no supporting trials or literature, and no plausible link to CTLA-4 blockade. It is a monogenic retinal degeneration, and immune activation could be harmful. It is treated here as a graph-based artefact and was not selected. The report focuses on non-cutaneous melanoma, the highest-ranked prediction with substantive supporting evidence.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ipilimumab blocks CTLA-4, a negative regulator of T-cell activation. Blocking it enhances T-cell priming and anti-tumour immunity, which underlies its efficacy in cutaneous metastatic melanoma.

Non-cutaneous melanomas (mucosal, uveal and conjunctival) share a melanocytic origin with cutaneous melanoma, so CTLA-4 blockade is mechanistically plausible. These subtypes generally have a lower tumour mutational burden and typically lower response rates, so benefit may be more modest.

The Phase 3 trial labelled in the data (NCT02278887) does not test ipilimumab as the investigational agent. It compares tumour-infiltrating lymphocyte (TIL) cell therapy against ipilimumab. The L1 rating is therefore generous and should be confirmed manually. Direct support comes mainly from a completed Phase 2 trial of nivolumab plus ipilimumab in uveal melanoma (NCT02626962) and retrospective ipilimumab series, including an Australian one.

## Clinical Trial Evidence

The 22 trials returned for this indication are mostly early-phase or combination studies. The most relevant are listed below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02626962](https://clinicaltrials.gov/study/NCT02626962) | Phase 2 | Completed | 52 | Single-arm nivolumab plus ipilimumab in previously untreated metastatic uveal melanoma; most directly relevant trial |
| [NCT02278887](https://clinicaltrials.gov/study/NCT02278887) | Phase 3 | Completed | 168 | TIL cell therapy with lymphodepletion and IL-2 versus ipilimumab in stage IV melanoma; ipilimumab is the comparator |
| [NCT02506153](https://clinicaltrials.gov/study/NCT02506153) | Phase 3 | Active, not recruiting | 1301 | Pembrolizumab versus high-dose interferon or ipilimumab in high-risk resected melanoma |
| [NCT05598853](https://clinicaltrials.gov/study/NCT05598853) | Phase 1 | Active, not recruiting | 26 | Intrathecal plus systemic anti-PD1/anti-CTLA-4 in leptomeningeal metastases from NSCLC or melanoma |
| [NCT02983045](https://clinicaltrials.gov/study/NCT02983045) | Phase 1/2 | Completed | 557 | NKTR-214 with nivolumab, including a triplet with ipilimumab, in solid tumours |
| [NCT03241173](https://clinicaltrials.gov/study/NCT03241173) | Phase 1/2 | Completed | 52 | INCAGN01949 combined with immune therapies in advanced malignancies |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | Encorafenib/binimetinib followed by ipilimumab/nivolumab versus immunotherapy alone in BRAF V600 melanoma |
| [NCT04250246](https://clinicaltrials.gov/study/NCT04250246) | Phase 2 | Unknown | 184 | Nivolumab plus ipilimumab with or without guadecitabine in anti-PD-1-resistant melanoma and NSCLC |
| [NCT04940299](https://clinicaltrials.gov/study/NCT04940299) | Phase 2 | Active, not recruiting | 35 | Tocilizumab with ipilimumab and nivolumab in advanced melanoma, NSCLC or urothelial carcinoma |
| [NCT01769222](https://clinicaltrials.gov/study/NCT01769222) | Phase 1 | Terminated | 3 | Intratumoral ipilimumab with local radiation; terminated, little data |

Several other listed trials (for example NCT06047379 and NCT04136470) are only loosely related to ipilimumab. No ANZCTR identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Curr Oncol | Real-world comparison of anti-PD-1 alone versus with ipilimumab in younger versus older adults with advanced melanoma |
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort | Med J Aust | Australian experience of ipilimumab in pretreated cutaneous, uveal and mucosal melanoma; efficacy and immune-related adverse events |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Curr Cancer Drug Targets | Systematic review of adjuvant treatment of melanoma, noting that non-cutaneous melanoma is only about 5% of cases |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discov Med | Update on anti-PD-1 antibodies, alone or with ipilimumab, as frontline therapy in advanced melanoma |
| [42178946](https://pubmed.ncbi.nlm.nih.gov/42178946/) | 2026 | Cohort | Pigment Cell Melanoma Res | Poliosis as a side effect of immunotherapy in cutaneous and non-cutaneous melanoma |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case report | Cureus | Rare melanoma metastasis to the transverse colon; notes the risk of gastrointestinal perforation with immunotherapy |

For related subtypes, the mucosal melanoma literature includes a dedicated ipilimumab 3 mg/kg expanded access analysis ([24100024](https://pubmed.ncbi.nlm.nih.gov/24100024/)) and a pooled nivolumab with or without ipilimumab analysis ([28056206](https://pubmed.ncbi.nlm.nih.gov/28056206/)).

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 15230N | Yervoy | Injection concentrate for I.V. infusion, 200 mg in 40 mL | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Not a typical feature; please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions |
| Monitoring Items | Immune-related adverse events: liver function, thyroid function, and bowel, skin and endocrine symptoms. Confirm against the PI |
| Handling Protection | Please refer to the PI and local institutional policy |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Drug Interactions:** 100 interactions were identified. Examples include:
  - **Major:** anticoagulants (apixaban, edoxaban, betrixaban, dalteparin, argatroban, bivalirudin, desirudin, danaparoid)
  - **Moderate:** corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone), metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin
  - Corticosteroids are also used to manage immune-related adverse events, so their use should be planned deliberately.
- **Safety signals in the retrieved literature:** Case reports describe fatal myocarditis with rhabdomyolysis, encephalitis, colitis and pneumonitis with ipilimumab-containing regimens.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ipilimumab is already marketed in Australia for melanoma. CTLA-4 blockade is mechanistically plausible in non-cutaneous melanoma, and there is a completed Phase 2 trial in uveal melanoma plus retrospective mucosal melanoma data. However, the automated L1 rating is not well supported, because the Phase 3 trial does not test ipilimumab directly. A manual rating of about L2 is more defensible. Response rates are expected to be lower than in cutaneous melanoma.

**To proceed, the following is needed:**
- Manual confirmation of the evidence level, and review of the published results of NCT02626962
- ARTG approved indication text and TGA Product Information, including warnings and contraindications
- Mechanism of action data from DrugBank
- A safety monitoring plan for immune-related adverse events, including cardiac, neurological and gastrointestinal events
- A review of interactions with anticoagulants and corticosteroids
- Subtype-specific efficacy data for mucosal, uveal and conjunctival melanoma, ideally including Australian data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

