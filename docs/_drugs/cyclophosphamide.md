---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Cyclophosphamide
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

# Cyclophosphamide: From Established Alkylating Chemotherapy to Myeloid Leukaemia

## One-Sentence Summary

Cyclophosphamide is a well-established alkylating agent with a long history of use across haematological malignancies, solid tumours, and autoimmune conditions — though no ARTG registration was identified in this dataset query. The TxGNN model predicts it may be effective for **Myeloid Leukaemia**, with **10+ clinical trials** (including multiple Phase 2/3 RCTs) and **20 publications** currently supporting this direction. The evidence base is robust, reflecting cyclophosphamide's central role in myeloablative conditioning and post-transplant immunosuppression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no ARTG registration identified in this dataset) |
| Predicted New Indication | Myeloid Leukaemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (0 ARTG entries identified) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cyclophosphamide is a nitrogen mustard alkylating agent. Formal mechanism of action data was not captured in this Evidence Pack; however, based on widely accepted pharmacology, cyclophosphamide is metabolised hepatically to its active metabolite phosphoramide mustard, which forms covalent crosslinks between and within DNA strands. This disrupts DNA replication and RNA transcription, causing apoptosis preferentially in rapidly proliferating cells. This mechanism provides the biological rationale for activity against leukaemic blasts.

In myeloid leukaemia, cyclophosphamide serves two distinct therapeutic roles. First, as part of **myeloablative conditioning regimens** — most notably the BuCy regimen (busulfan plus cyclophosphamide) — it eradicates residual leukaemic clones and creates haematopoietic space to facilitate engraftment of donor stem cells prior to allogeneic haematopoietic stem cell transplantation (allo-HSCT). Second, as **post-transplant cyclophosphamide (PTCy)**, administered at lower doses on Days +3 and +4 after transplant, it selectively eliminates proliferating alloreactive T cells, thereby preventing graft-versus-host disease (GVHD) while preserving the beneficial graft-versus-leukaemia (GVL) effect. This dual mechanism — direct cytotoxicity and targeted immune modulation — makes cyclophosphamide uniquely suited to the complex treatment landscape of myeloid leukaemia.

The TxGNN prediction score of 99.47% reflects a well-established biological and clinical relationship, supported by decades of published evidence and international guideline endorsement. The prediction should be interpreted as strong model validation of an existing clinical paradigm rather than a truly novel repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002549](https://clinicaltrials.gov/study/NCT00002549) | Phase 3 | Unknown | 1,520 | Randomised comparison of cyclophosphamide-containing induction regimens (ICE vs MICE vs DCE) followed by intensive consolidation and bone marrow transplantation in AML; landmark large-scale trial establishing the role of cyclophosphamide in AML induction |
| [NCT03007147](https://clinicaltrials.gov/study/NCT03007147) | Phase 3 | Active, not recruiting | 475 | International RCT evaluating imatinib with two different cyclophosphamide-based chemotherapy backbones in newly diagnosed Ph+ALL; cyclophosphamide-containing arm under direct comparison |
| [NCT02208037](https://clinicaltrials.gov/study/NCT02208037) | Phase 2 | Completed | 279 | BMT CTN #1203 (Progress I): multicentre randomised trial comparing novel GVHD prophylaxis approaches — including post-transplant cyclophosphamide — against contemporary standards after allo-HSCT for haematologic malignancies |
| [NCT05598593](https://clinicaltrials.gov/study/NCT05598593) | Phase 2 | Unknown | 70 | Modified TBF conditioning regimen (including cyclophosphamide) prior to allo-HCT for T-ALL/lymphoblastic lymphoma; directly assesses cyclophosphamide's role in transplant conditioning for lymphoid blast disease |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Venetoclax + azacytidine bridging followed by modified BUCY (busulfan-cyclophosphamide) conditioning for high-risk MDS and R/R AML undergoing allo-HSCT; evaluates cyclophosphamide as the backbone of a modern combined strategy |
| [NCT05126849](https://clinicaltrials.gov/study/NCT05126849) | Phase 2 | Recruiting | 31 | Nationwide study of post-transplant cyclophosphamide in haploidentical allo-HSCT for acquired refractory aplastic anaemia and MDS; directly measures PTCy safety and engraftment outcomes |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | Multicentre study of HLA-mismatched unrelated donor bone marrow transplantation with PTCy, sirolimus, and MMF for GVHD prophylaxis in patients with haematologic malignancies including AML |
| [NCT00005892](https://clinicaltrials.gov/study/NCT00005892) | Observational | Completed | N/A | Completed study of moderate-dose cyclophosphamide plus radiotherapy before allo-BMT in patients with MDS and acute leukaemia related to Fanconi's anaemia; evaluates survival and morbidity outcomes in a directly relevant population |
| [NCT00602693](https://clinicaltrials.gov/study/NCT00602693) | Phase 1 | Completed | 41 | Fludarabine and cyclophosphamide non-myeloablative conditioning before UCB transplant, with subsequent T-regulatory cell infusion; demonstrates cyclophosphamide's immune-modulating role in the transplant platform |
| [NCT06786533](https://clinicaltrials.gov/study/NCT06786533) | Phase 1 | Recruiting | 18 | Dose-escalation safety study of anti-FLT3 CAR-T cells (HG-CT-1) in R/R AML with cyclophosphamide as lymphodepleting preconditioning; represents cyclophosphamide's emerging role supporting next-generation cell therapies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | RCT | Future Oncology | Head-to-head comparison of BuCy (busulfan-cyclophosphamide) vs FluBu (fludarabine-busulfan) myeloablative conditioning for allo-HSCT in AML; BuCy remains a standard reference regimen |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Phase 2 Trial | Transplant Immunology | Cladribine + BuCy as intensified conditioning prior to allo-HSCT in R/R AML; demonstrates that cyclophosphamide-containing intensified regimens are feasible and clinically active in refractory disease |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | Analysis of 217 AML patients in complete remission undergoing HCT with myeloablative conditioning + PTCy-based GVHD prophylaxis; 2-year overall survival 77%, event-free survival 72% |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Cohort | Bone Marrow Transplantation | Retrospective analysis of 1,823 AML patients receiving PTCy-based HSCT; examines the impact of conditioning intensity stratified by cytogenetic and molecular risk classification |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohort | European Journal of Haematology | Comparison of myeloablative vs reduced-intensity conditioning in AML patients under 65 years receiving ATG and post-transplant cyclophosphamide GVHD prophylaxis; informs intensity selection in younger patients |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Retrospective Cohort | International Journal of Molecular Sciences | First published data on PTCy-based GVHD prophylaxis after matched sibling and unrelated donor HSCT in paediatric AML; demonstrates safety and efficacy in a younger population |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Retrospective Cohort | Cytotherapy | Prognostic factors in haploidentical HCT with PTCy for AML; supports PTCy as an effective and increasingly used GVHD prophylaxis strategy across donor types |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Retrospective | Haematology/Oncology and Stem Cell Therapy | Comparative effectiveness of BuCy vs BuFlu myeloablative conditioning for allo-HCT in AML and MDS; quality of life outcomes included alongside traditional survival endpoints |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Retrospective | American Journal of Hematology | Cyclophosphamide/fludarabine non-myeloablative allo-HSCT vs myeloablative transplant for 165 AML patients; comparable event-free and overall survival at 61-month median follow-up |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Retrospective | Leukaemia & Lymphoma | High-dose cyclophosphamide (60 mg/kg) for cytoreduction in 27 AML patients presenting with hyperleukocytosis or leukostasis; provides data on cyclophosphamide as acute cytoreductive therapy beyond conditioning |

---

## Australia Market Information

No ARTG registrations for cyclophosphamide were identified in this dataset query. The drug is recorded as not currently marketed in Australia, with zero ARTG entries returned.

> **Important Data Limitation:** This finding may reflect a gap in the data collection process rather than a true absence of Australian registration. Cyclophosphamide is a decades-old medicine that may be registered under multiple formulations or brand names not captured by this query. Clinicians and pharmacists should verify current ARTG status directly via the [TGA ARTG public database](https://www.tga.gov.au/resources/artg) before making any supply or prescribing decisions.

---

## Cytotoxicity

Cyclophosphamide meets the criteria for antineoplastic classification as a conventional alkylating cytotoxic agent. This section is included accordingly.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (nitrogen mustard class) |
| Myelosuppression Risk | **High** — Neutropenia and thrombocytopenia are dose-limiting toxicities; nadir typically occurs around Day 10–14 post-dose with recovery by Day 21–28; risk is particularly pronounced at myeloablative doses used in HSCT conditioning |
| Emetogenicity Classification | **Moderate to high** — Highly emetogenic at doses ≥1,500 mg/m² (as used in conditioning regimens); moderate emetogenic risk at standard chemotherapy doses; prophylactic antiemetic regimens are required |
| Monitoring Items | Full blood count with differential (FBC), renal function (eGFR/serum creatinine), liver function tests (LFTs), urinalysis for haematuria (haemorrhagic cystitis monitoring), serum electrolytes, cardiac function assessment at high cumulative doses |
| Handling Protection | Must be handled according to Australian cytotoxic drug handling regulations — appropriate PPE (gloves, gown, eye protection), use of closed-system drug transfer devices (CSTDs), dedicated cytotoxic preparation area, and cytotoxic waste disposal protocols are mandatory |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for comprehensive safety information.

> **Note for clinicians:** No safety data (warnings, contraindications, or drug interaction information) was available in this Evidence Pack. Cyclophosphamide has a well-characterised toxicity profile including haemorrhagic cystitis (mitigated by mesna co-administration and hydration), myelosuppression, cardiotoxicity at high doses, secondary malignancy risk (particularly therapy-related MDS/AML), gonadal toxicity, and teratogenicity. Comprehensive prescribing information must be reviewed prior to use, and institutional oncology pharmacy consultation is strongly recommended.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide has extensive Level 1 evidence — including multiple completed and ongoing Phase 2/3 randomised controlled trials with thousands of enrolled patients — establishing its efficacy and safety in myeloid leukaemia treatment. Its role is primarily in myeloablative conditioning (BuCy regimen) and as post-transplant cyclophosphamide (PTCy) for GVHD prevention in the allo-HSCT setting. This is a globally standard practice rather than a novel repurposing concept; the TxGNN prediction effectively confirms a well-validated clinical application.

**To proceed, the following is needed:**

- **Verify Australian registration status**: The ARTG query returned 0 entries — this is a critical data gap that must be resolved before any clinical use. Confirm via the TGA ARTG public database whether cyclophosphamide products (e.g., powder for injection) are currently registered; if not, investigate TGA Special Access Scheme (SAS) or Authorised Prescriber pathways.
- **Obtain TGA-approved Product Information**: No safety data was captured in this Evidence Pack. Full PI review covering warnings, contraindications, dosing, and monitoring requirements is essential for Australian prescribing.
- **Clarify the specific clinical sub-indication**: The evidence varies substantially by indication context — AML induction chemotherapy, myeloablative HSCT conditioning (BuCy), reduced-intensity conditioning, or PTCy GVHD prophylaxis each have distinct dose regimens, patient selection criteria, and toxicity profiles.
- **Supplement mechanism of action data**: DrugBank MOA data was listed as a data gap; retrieving this will complete the mechanistic evidence package and support clinical rationale documentation.
- **Confirm institutional HSCT protocols**: Cyclophosphamide use in AML is predominantly within structured haematology/transplant service protocols; alignment with Australian bone marrow transplant unit guidelines is required prior to implementation.

---

*This report is generated for research purposes only. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in conjunction with TGA-approved prescribing information and current clinical guidelines. This report does not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

