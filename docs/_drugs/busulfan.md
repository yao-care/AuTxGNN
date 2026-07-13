---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myelogenous Leukaemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically approved for chronic myelogenous leukaemia (CML), and now widely established as a cornerstone myeloablative and reduced-intensity conditioning (MAC/RIC) agent prior to allogeneic haematopoietic stem cell transplantation (allo-HSCT).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
with **50+ clinical trials** and **20 publications** — including multiple completed Phase 3 RCTs — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myelogenous leukaemia (CML; historical Myleran indication) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Busulfan is a bifunctional alkylating agent that forms DNA interstrand cross-links, causing cell death in rapidly proliferating haematopoietic progenitor cells. This mechanism underpins its role as the benchmark drug in myeloablative conditioning (MAC) and reduced-intensity conditioning (RIC) regimens prior to allo-HSCT — a use that evolved directly from its original CML indication.

Both CML and MDS arise from clonal haematopoietic stem cell dysfunction, and the therapeutic rationale for busulfan in MDS is mechanistically identical to its original use: eliminating the abnormal haematopoietic clone and creating engraftment space for donor stem cells to reconstitute normal haematopoiesis. In MDS, where clonal cytopenias and risk of leukaemic transformation drive treatment decisions, busulfan's myeloablative capacity is precisely what is required before allo-HSCT — the only currently curative approach for higher-risk MDS.

Multiple landmark Phase 3 RCTs have explicitly used busulfan-based regimens as the comparator arm standard of care for MDS allo-HSCT, confirming its entrenched clinical position. The MC-FludT.14/L trial (NCT00822393, n=570, *Lancet Haematology* 2020) was specifically designed with busulfan/fludarabine RIC as the reference arm, reflecting international consensus that busulfan is the conditioning benchmark for this population — spanning both adult and paediatric MDS cohorts globally.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | Completed | 570 | Landmark RCT (MC-FludT.14/L) comparing treosulfan-based conditioning vs busulfan/fludarabine RIC for allo-HSCT in adult AML/MDS ineligible for standard conditioning; busulfan/fludarabine serves as the reference standard arm |
| [NCT00002798](https://clinicaltrials.gov/study/NCT00002798) | Phase 3 | Completed | 880 | Paediatric AML/MDS Phase 3 RCT comparing chemotherapy regimens ± bone marrow transplantation; busulfan is a core preparative component across arms |
| [NCT00582933](https://clinicaltrials.gov/study/NCT00582933) | Phase 2 | Completed | 96 | IV Busulfan + Melphalan + Fludarabine triple myeloablative regimen before T-cell depleted allo-HSCT for haematological disorders including MDS; demonstrates feasibility of busulfan-based conditioning without total body irradiation |
| [NCT01985061](https://clinicaltrials.gov/study/NCT01985061) | Phase 2 | Active, not recruiting | 177 | Prospective multicentre dose-finding study of 3 IV busulfan dose levels combined with fludarabine and thymoglobulin prior to matched related/unrelated donor allo-HSCT in poor-prognosis myeloid malignancies including MDS |
| [NCT04098653](https://clinicaltrials.gov/study/NCT04098653) | Phase 2/3 | Unknown | 196 | Randomised comparison of Decitabine + BuCy vs BuCy alone as myeloablative conditioning for AML and MDS undergoing allo-HSCT; evaluates whether adding epigenetic priming to busulfan reduces relapse |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | Single-arm prospective study evaluating FLU-BU-MEL conditioning for allo-HSCT specifically in MDS-EB or IPSS-R intermediate-high/very-high-risk MDS |
| [NCT00003662](https://clinicaltrials.gov/study/NCT00003662) | Phase 2 | Completed | 90 | Umbilical cord blood transplantation in adults and children with bone marrow failure syndromes and haematological cancers including MDS; busulfan included in preparative conditioning |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Intensity-modulated total marrow irradiation (IM-TMI 9 Gy) added to standard myeloablative FluBu4 with post-transplant cyclophosphamide for high-risk AML, CML and MDS allo-HSCT |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax combined with timed sequential busulfan, cladribine and fludarabine before allo-HSCT for AML and MDS; evaluates BCL-2 inhibition added to busulfan backbone |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | Completed | 64 | Busulfan + Melphalan + Fludarabine with peri-transplant palifermin (mucosal protectant) followed by T-cell depleted allo-HSCT from matched/mismatched donors for advanced MDS and AML |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Phase 3 RCT | Am J Hematol | Final analysis of MC-FludT.14/L (n=476): treosulfan non-inferior to busulfan/fludarabine RIC for event-free survival in older/comorbid AML/MDS patients undergoing allo-HCT; validates busulfan/fludarabine as the established comparator standard |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | Lancet Haematol | Confirmatory interim Phase 3 non-inferiority RCT (n=570): treosulfan+fludarabine vs busulfan+fludarabine in older/comorbid AML/MDS before allo-HSCT; busulfan regimen serves as benchmark reference arm |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase 3 RCT | J Clin Oncol | BMT CTN 0901 Phase 3 RCT (n=272): myeloablative vs reduced-intensity conditioning in AML/MDS; busulfan-based MAC and RIC regimens evaluated; demonstrates comparable overall survival with different toxicity/relapse trade-offs |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | Lancet Haematol | Multicentre open-label Phase 3 RCT: G-CSF + decitabine + BuCy vs BuCy alone for MDS-RAEB or secondary AML post-MDS allo-HSCT; confirms busulfan-cyclophosphamide as the current standard conditioning backbone |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic review & meta-analysis | Front Oncol | Meta-analysis of treosulfan vs busulfan conditioning for MDS and AML allo-HCT long-term outcomes; synthesises comparative safety and efficacy data from multiple RCTs and cohort studies |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Contemporary Review | Am J Hematol | Current comprehensive review of allo-HCT for MDS and myelofibrosis; addresses genomic profiling-guided patient selection, busulfan-based conditioning intensity, and emerging targeted approaches |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Propensity score-matched cohort | Transplant Cell Ther | Single-centre retrospective study (n=138, Princess Margaret Hospital Toronto): treosulfan vs busulfan conditioning in MDS/CMML allo-HCT; comparable outcomes provide real-world validation of busulfan's role in MDS |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Phase 2 Prospective | Transplant Cell Ther | Myeloablative busulfan+fludarabine with in vivo T-cell depletion (alemtuzumab) for AML/MDS: safe and effective even in patients beyond traditional 55-year age cutoff, extending busulfan-based MAC to broader populations |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Propensity score-matched analysis | Bone Marrow Transplant | Nationwide Japanese registry analysis (2006–2018) comparing Flu/Bu4 vs Bu4/Cy for MDS allo-HSCT; Flu/Bu4 demonstrates comparable transplant outcomes with a potentially improved toxicity profile |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Retrospective cohort | Cancer | Fractionated IV busulfan myeloablative conditioning in older AML/MDS patients: dose fractionation preserves myeloablative efficacy while controlling non-relapse mortality, supporting busulfan's expanded use in older recipients |

---

## Australia Market Information

Busulfan is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this product at this time.

Clinicians wishing to access busulfan in Australia would need to apply through one of the following pathways:
- **TGA Special Access Scheme Category B (SAS-B)** — for individual patient access via prescriber notification
- **Authorised Prescriber Scheme** — for clinicians in accredited transplant centres prescribing to multiple eligible patients
- **Hospital exemption** — for compounding or importation under institutional therapeutic goods exemption arrangements

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Bifunctional alkylating agent (nitrogen mustard analogue) |
| Myelosuppression Risk | **High** — myeloablation is the therapeutic intent; profound and prolonged pancytopenia (neutropenia, thrombocytopenia, anaemia) expected following conditioning doses; G-CSF support and transfusion protocols mandatory |
| Emetogenicity Classification | Low to moderate (intravenous formulation); risk increases with high-dose regimens |
| Monitoring Items | Full blood count (FBC) with differential daily; liver function tests (LFTs) including bilirubin for sinusoidal obstruction syndrome (SOS/VOD) detection; renal function; busulfan plasma AUC (therapeutic drug monitoring mandatory for IV formulation to achieve target AUC 900–1,350 µmol·min/L); seizure monitoring — busulfan crosses the blood–brain barrier and prophylactic anticonvulsants are required |
| Handling Protection | Must be handled in strict accordance with cytotoxic handling guidelines (SHPA and ACSOM standards); IV formulation requires preparation in a biological safety cabinet by trained pharmacy staff; personal protective equipment (PPE) including chemotherapy-rated gloves and gown mandatory; cytotoxic waste disposal protocols apply |

---

## Safety Considerations

Please refer to the relevant Product Information (PI) for complete safety information. As busulfan is not registered on the ARTG, Australian prescribers should consult international product information (e.g., Busulfex® IV prescribing information) and institutional protocols.

Key safety areas that require proactive management in the transplant setting include hepatic sinusoidal obstruction syndrome (SOS/VOD), which may require defibrotide access planning; seizure prophylaxis with prophylactic anticonvulsants (levetiracetam preferred due to fewer drug interactions); and pulmonary toxicity with chronic busulfan use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning for MDS allo-HSCT is supported by multiple completed Phase 3 RCTs and is internationally recognised as a standard of care; the TxGNN prediction score of 99.62% aligns with this strong established evidence base. However, the absence of any Australian ARTG registration (0 entries) means regulatory access pathways must be established before clinical use.

**To proceed, the following is needed:**

- **Regulatory access:** Obtain TGA SAS-B authorisation or Authorised Prescriber status for use in accredited bone marrow transplant centres; engage a TGA-registered sponsor to explore formal ARTG listing
- **Mechanism of action documentation:** Retrieve complete DrugBank and international PI data for full MOA, pharmacokinetic parameters, and safety profile to support institutional credentialling and risk assessment
- **Therapeutic drug monitoring (TDM) protocol:** Establish access to busulfan plasma AUC monitoring (HPLC-based assay) — this is mandatory for IV formulation and requires laboratory infrastructure at or near the transplant centre
- **Seizure prophylaxis and VOD prevention protocols:** Confirm institutional protocols for anticonvulsant prophylaxis and defibrotide access (via TGA SAS) for sinusoidal obstruction syndrome management
- **Restriction to specialist centres:** Use must be limited to accredited allogeneic stem cell transplant programmes with intensive supportive care capability, haematology intensivists, and 24-hour pharmacy coverage
- **Paediatric dosing expertise:** For paediatric MDS cases, ensure access to weight-based and body surface area-adjusted dosing guidance and dedicated paediatric transplant team involvement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

