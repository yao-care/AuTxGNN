---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Antineoplastic Chemotherapy to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is a classic anthracycline cytotoxic agent and one of the most widely used chemotherapy backbones in oncology worldwide, employed across multiple malignancy types including lymphomas, sarcomas, and solid tumours. The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **multiple completed Phase 3 RCTs** and over **20 publications** currently supporting this direction. Notably, the evidence base places this at **Evidence Level L1** — the highest tier — meaning this is not a speculative prediction but rather a well-supported use case with robust clinical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication registered in Australia (no ARTG listing) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Doxorubicin is an anthracycline antibiotic that exerts its antineoplastic effect through two complementary mechanisms: **intercalation into the DNA double helix** and **inhibition of topoisomerase II**, an enzyme essential for DNA replication and transcription. The resulting DNA double-strand breaks are particularly lethal to rapidly proliferating cells, making doxorubicin highly cytotoxic against tumours with high mitotic indices.

Ewing sarcoma is driven by the **EWSR1-FLI1 fusion gene** (present in approximately 85% of cases), which causes widespread transcriptional dysregulation and maintains cells in a highly proliferative state. This biological profile makes Ewing sarcoma cells exquisitely sensitive to DNA-damaging agents such as doxorubicin. The drug is already the **backbone of the international standard VDC/IE regimen** (Vincristine–Doxorubicin–Cyclophosphamide alternating with Ifosfamide–Etoposide), which has been validated across multiple Phase 3 trials in North America and Europe.

Given this mechanistic alignment and the depth of existing clinical evidence, the TxGNN model's high prediction score reflects an already well-established clinical reality rather than a novel hypothesis. The practical question for Australian healthcare settings is not *whether* doxorubicin works for Ewing sarcoma, but rather **how to establish access pathways** given the absence of an ARTG registration in Australia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomised Phase 3 RCT comparing standard vs dose-intensified treatment in non-metastatic Ewing sarcoma; doxorubicin-containing regimen evaluated — highest-grade direct evidence |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Evaluates adding vincristine–topotecan–cyclophosphamide to standard VDC/IE (containing doxorubicin) in non-metastatic Ewing sarcoma; large multicentre trial |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Randomised trial of chemotherapy intensification through interval compression in Ewing's sarcoma; doxorubicin-containing regimen; supports standard dosing strategy |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1,200 | EURO-E.W.I.N.G.99 — landmark European cooperative trial studying combination chemotherapy with or without consolidation in Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Randomised Phase 3 trial of ganitumab (IGF-1R antibody) added to interval-compressed VDC/IE for newly diagnosed metastatic Ewing sarcoma |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 437 | Compares VIrR (vincristine–irinotecan–regorafenib) + VDC/IE versus standard VDC/IE alone in newly diagnosed metastatic Ewing sarcoma |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | CombinaiR3 — French study of doxorubicin-based first-line treatment in Ewing tumours with primary extrapulmonary metastatic dissemination; direct indication relevance |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Pediatric Oncology Group study of intensive chemotherapy with growth factor support in newly diagnosed metastatic Ewing's tumour; doxorubicin-containing regimen |
| [NCT03277924](https://clinicaltrials.gov/study/NCT03277924) | Phase 1/2 | Completed | 197 | Multicentre international trial of sunitinib and/or nivolumab added to doxorubicin-containing chemotherapy in soft tissue and bone sarcomas including Ewing sarcoma |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not reported | EICESS 92 — European Intergroup Cooperative Ewing's Sarcoma Study; randomised comparison of combination chemotherapy regimens including doxorubicin |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | *The Lancet* | EE2012 Phase 3 RCT directly comparing European (vincristine–ifosfamide–doxorubicin–etoposide) vs North American (VDC/IE) regimens in newly diagnosed Ewing sarcoma; demonstrates comparable outcomes with both doxorubicin-containing regimens |
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | *NEJM* | Landmark RCT demonstrating that adding ifosfamide and etoposide to standard doxorubicin-containing regimen significantly improves event-free survival in newly diagnosed Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT | *Trials* | EURO EWING 2012 — international RCT protocol comparing two induction/consolidation regimens for Ewing sarcoma family of tumours; establishes doxorubicin-based therapy as standard |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | *J Clin Oncol* | COG trial AEWS1221 — Phase 3 RCT of ganitumab added to interval-compressed doxorubicin-based chemotherapy in metastatic Ewing sarcoma; defines the current standard for metastatic disease |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | *J Clin Oncol* | Comprehensive review of Ewing sarcoma management; outlines the evidence base for risk-adapted, doxorubicin-containing multimodal treatment strategies |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | *Lancet Oncol* | Seminal review documenting the improvement in Ewing sarcoma survival from ~10% (pre-chemotherapy era) to ~75% (localised disease today) largely attributable to anthracycline-based regimens |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | Clinical Trial | *J Clin Oncol* | COG study AEWS0031 — demonstrates that interval compression of VDC/IE (doxorubicin-containing) chemotherapy improves event-free survival in localised Ewing sarcoma |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Follow-up Report | *J Clin Oncol* | Long-term outcome update from AEWS0031 confirming durable survival benefit of interval-compressed doxorubicin-based chemotherapy in localised Ewing sarcoma |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Analysis | *JNCI* | Dose-intensity analysis establishing that doxorubicin dose intensity is most strongly associated with favourable outcomes in Ewing's sarcoma trials |
| [28710342](https://pubmed.ncbi.nlm.nih.gov/28710342/) | 2017 | Clinical Study | *The Oncologist* | Reports efficacy of vincristine–ifosfamide–doxorubicin (VID) regimen in adults with Ewing sarcoma; five-year event-free survival data from MD Anderson Cancer Center |

---

## Australia Market Information

Doxorubicin currently has **no ARTG registrations** and is classified as **not marketed** in Australia. Despite this, doxorubicin-containing regimens are in active clinical use for Ewing sarcoma and related paediatric sarcomas at Australian specialist centres, typically accessed through hospital-level procurement, compassionate access schemes, or through clinical trial enrolment.

Healthcare professionals seeking to use doxorubicin for Ewing sarcoma in Australia should consider:
- TGA Special Access Scheme (SAS) Category B pathway for unregistered therapeutic goods
- Clinical trial enrolment (several active international trials are open)
- Engagement with the Children's Oncology Group (COG) and European paediatric sarcoma networks for protocol access

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalator and topoisomerase II inhibitor) |
| Myelosuppression Risk | **High** — dose-limiting neutropenia and thrombocytopenia are expected; febrile neutropenia rates are significant in standard VDC dosing schedules |
| Emetogenicity Classification | **Moderate to High** — doxorubicin is classified as a moderately to highly emetogenic agent depending on dose and combination regimen; prophylactic antiemetics are required |
| Monitoring Items | Full blood count with differential (prior to each cycle), cardiac function (LVEF via echocardiogram or MUGA at baseline, at cumulative dose thresholds, and at treatment completion), liver function tests, renal function, serum electrolytes |
| Cumulative Dose Threshold | Cardiotoxicity risk rises significantly above cumulative doses of **450–550 mg/m²**; paediatric Ewing sarcoma protocols typically remain below this threshold with careful planning |
| Handling Protection | Must be prepared and administered in accordance with Australian cytotoxic drug handling standards (refer to SHPA *Guidelines for the Safe Handling of Cytotoxics*); closed-system transfer devices recommended during preparation |

---

## Safety Considerations

Detailed safety information including warnings, contraindications, and drug interactions is not available in this evidence pack. Please refer to the **TGA-approved Product Information (PI)** for any doxorubicin formulation and to current **Australian paediatric oncology protocols** (e.g., COG AEWS protocols, EpSSG/EuroEwing guidelines) for regimen-specific toxicity management guidance.

Key clinically important safety considerations known from the literature and general oncology practice include:
- **Cardiotoxicity** (dose-related cardiomyopathy; acute and chronic forms) — requires baseline and serial cardiac function monitoring
- **Myelosuppression** — dose-limiting; growth factor support (G-CSF) is standard of care in interval-compressed schedules
- **Vesicant properties** — extravasation can cause severe tissue necrosis; central venous access is strongly preferred
- **Secondary leukaemia risk** — therapy-related AML/MDS associated with topoisomerase II inhibitors (low but not negligible long-term risk)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for doxorubicin in Ewing sarcoma is among the strongest of any drug repurposing scenario — multiple completed Phase 3 RCTs, large enrolment numbers across international cooperative groups, and doxorubicin's established role as the backbone of the globally accepted VDC/IE standard regimen all place this at Evidence Level L1. The primary practical barrier in Australia is the absence of an ARTG registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Access pathway establishment** — Identify the most appropriate TGA access mechanism (SAS Category B, authorised prescriber, or clinical trial) for Australian patients requiring doxorubicin for Ewing sarcoma
- **Formal cardiac monitoring protocol** — Document baseline LVEF measurement and define dose thresholds for repeat assessments (standard practice at 250 mg/m² and 450 mg/m² cumulative dose)
- **Multidisciplinary team (MDT) input** — Engage paediatric/adolescent oncology, cardiology, and pharmacy prior to initiating treatment, particularly for paediatric patients
- **Regimen selection** — Confirm which VDC/IE protocol version (COG AEWS, EpSSG, or Ewing 2008 framework) is most appropriate based on patient risk stratification (localised vs metastatic, age, tumour site)
- **G-CSF prophylaxis plan** — Primary prophylaxis with pegfilgrastim or filgrastim should be pre-planned given the high-grade myelosuppression expected with interval-compressed dosing
- **Long-term follow-up plan** — Given the paediatric population typically affected, establish a cardiac surveillance schedule extending beyond completion of therapy

> **YMYL Disclaimer:** This report is intended for research and clinical decision-support purposes only. It does not constitute medical advice, prescribing guidance, or a recommendation for individual patient treatment. All drug repurposing candidates require thorough clinical assessment, multidisciplinary review, and, where appropriate, regulatory approval prior to clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

