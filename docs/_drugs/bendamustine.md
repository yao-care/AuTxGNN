---
layout: default
title: Bendamustine
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Bendamustine
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

# Bendamustine: From CLL / Indolent B-cell NHL to Mantle Cell Lymphoma

## One-Sentence Summary

Bendamustine is a bifunctional alkylating agent internationally approved for chronic lymphocytic leukaemia (CLL) and rituximab-refractory indolent B-cell non-Hodgkin lymphoma (NHL), although it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Mantle Cell Lymphoma (MCL)**,
with **50 clinical trials** and **20 publications** currently supporting this direction — including multiple completed and ongoing Phase 3 RCTs that directly validate bendamustine as a cornerstone of MCL therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not TGA-registered in Australia; globally approved for CLL and rituximab-refractory indolent B-cell NHL (US FDA, EMA) |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Bendamustine has a unique dual mechanism of action that distinguishes it from conventional alkylating agents. Its nitrogen mustard moiety forms inter- and intrastrand DNA crosslinks, causing irreparable DNA damage and triggering apoptosis, while its benzimidazole ring confers purine analogue properties that disrupt nucleic acid synthesis and inhibit DNA damage repair pathways. This hybrid mechanism produces only partial cross-resistance with other alkylating agents (e.g., cyclophosphamide, melphalan), meaning it retains activity in patients who have progressed on prior chemotherapy regimens.

Mantle cell lymphoma is driven by the t(11;14)(q13;q32) translocation, resulting in cyclin D1 overexpression and aberrant cell cycle progression. MCL cells characteristically have impaired DNA repair capacity — a vulnerability that makes them particularly sensitive to bendamustine's dual mode of DNA damage. Like CLL and indolent NHL, MCL is a B-cell malignancy that expresses CD20, allowing co-administration with rituximab (anti-CD20) to synergistically enhance B-cell clearance. The resulting bendamustine–rituximab (BR) regimen has become the internationally accepted backbone for MCL treatment, especially in transplant-ineligible patients.

This mechanistic rationale is strongly validated by robust clinical evidence. Two completed Phase 3 randomised controlled trials (NCT01456351 and NCT00991211) directly tested BR in MCL, establishing its efficacy as first-line and salvage therapy. The landmark SHINE trial (NEJM 2022), BRIGHT study (Lancet 2013), and ENRICH trial (Lancet 2025) further cement BR as the standard comparator arm against which all novel MCL regimens — including BTK inhibitor combinations — are benchmarked. The TxGNN prediction score of 99.63% is therefore well supported by the highest level of clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | Completed | 230 | Randomised comparison of BR vs fludarabine–rituximab (FR) for event-free survival in recurrent or progressive low-grade NHL and MCL; directly assessed bendamustine efficacy as salvage therapy |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Completed | 549 | BR vs R-CHOP as first-line treatment of low-grade NHL and MCL; evaluated non-inferiority for progression-free survival |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Active, not recruiting | 635 | Randomised, double-blind study of acalabrutinib + BR vs placebo + BR in previously untreated MCL; BR serves as the chemotherapy backbone |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Active, not recruiting | 510 | Zanubrutinib + rituximab vs BR in transplant-ineligible untreated MCL; BR is the active comparator representing current standard of care |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | Active, not recruiting | 373 | Four-arm randomised study in patients ≥60 years with previously untreated MCL; all arms incorporate BR ± bortezomib or lenalidomide consolidation |
| [NCT06854003](https://clinicaltrials.gov/study/NCT06854003) | Phase 2 | Recruiting | 60 | Randomised evaluation of BRAZAN induction (bendamustine + rituximab + cytarabine + zanubrutinib) followed by zanubrutinib/rituximab ± sonrotoclax maintenance in treatment-naive MCL |
| [NCT01437709](https://clinicaltrials.gov/study/NCT01437709) | Phase 2 | Completed | 30 | Ofatumumab with or without bendamustine in MCL patients ineligible for autologous stem cell transplant; specifically designed for transplant-ineligible MCL population |
| [NCT01457144](https://clinicaltrials.gov/study/NCT01457144) | Phase 2 | Completed | 76 | First-line RiBVD regimen (rituximab, bortezomib, bendamustine, dexamethasone) in patients aged ≥65 or younger patients refusing transplant with MCL |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | Completed | 57 | Age-adjusted R-BAC (rituximab 375 mg/m², bendamustine 70 mg/m², cytarabine 800 mg/m²) induction in older patients with MCL; evaluated safety and activity in a geriatric MCL population |
| [NCT02278796](https://clinicaltrials.gov/study/NCT02278796) | Phase 2 | Completed | 108 | Randomised comparison of BeEAM (bendamustine-containing) vs standard BEAM as high-dose conditioning prior to autologous stem cell transplantation in lymphoma patients including MCL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | Phase 3 RCT | N Engl J Med | SHINE trial: ibrutinib + BR vs placebo + BR in older patients with untreated MCL; demonstrated significantly prolonged PFS with ibrutinib addition, validating BR as the essential chemotherapy backbone |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | Phase 3 RCT | J Clin Oncol | Acalabrutinib + BR vs placebo + BR in untreated MCL; evaluated whether second-generation BTK inhibitor improves on the established BR backbone |
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | Phase 3 RCT | Lancet | BR vs R-CHOP as first-line treatment for indolent NHL and MCL; BR demonstrated superior PFS and significantly better tolerability (less alopecia, haematological toxicity) |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | Phase 3 RCT | Lancet | ENRICH trial: ibrutinib + rituximab vs immunochemotherapy (R-CHOP or BR) in MCL patients aged ≥60 years; BR used as standard-of-care comparator reflecting established practice |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Phase 3 RCT | J Clin Oncol | BRIGHT study 5-year follow-up: BR vs R-CHOP/R-CVP in treatment-naive indolent NHL and MCL; long-term durability of BR response confirmed with favourable survival outcomes |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | Phase 3 RCT | Blood | BRIGHT study primary results: BR non-inferior to R-CHOP/R-CVP for complete response rate in treatment-naive indolent NHL and MCL |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | Phase 3 RCT | Future Oncol | Study protocol for Phase 3 trial of zanubrutinib + rituximab vs BR in transplant-ineligible untreated MCL; highlights BR as the benchmark standard-of-care regimen |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Cohort Study | Blood Advances | Pooled analysis of rituximab–bendamustine / rituximab–cytarabine (RB/RC) alternating induction followed by ASCT in transplant-eligible MCL; achieved high complete response rates with acceptable toxicity |
| [36919283](https://pubmed.ncbi.nlm.nih.gov/36919283/) | 2023 | Network Meta-analysis | Eur J Haematol | Network meta-analysis of regimens in transplant-ineligible newly diagnosed MCL; ibrutinib + BR identified as superior; confirms BR as the central node in MCL treatment comparisons |
| [26755518](https://pubmed.ncbi.nlm.nih.gov/26755518/) | 2016 | Review | J Clin Oncol | Comprehensive review of MCL pathophysiology and clinical management; articulates the role of BR plus maintenance rituximab as standard of care for older patients |

---

## Australia Market Information

Bendamustine is **not currently registered with the Therapeutic Goods Administration (TGA)** and has no entries in the Australian Register of Therapeutic Goods (ARTG). There are no TGA-approved formulations, dosage forms, or approved indications available in Australia.

For reference, bendamustine is approved in other jurisdictions under the following brand names:

| Brand Name | Jurisdiction | Approved Indications |
|-----------|-------------|---------------------|
| Treanda® / Bendeka® | US FDA | CLL (first-line); indolent B-cell NHL progressing during or within 6 months of rituximab-containing therapy |
| Levact® | EMA | CLL (first-line, unfit for fludarabine); indolent NHL progressing after rituximab; multiple myeloma (in combination) |
| SyB L-0501 | Japan (PMDA) | Low-grade B-cell NHL; MCL |

Any use in Australia would require TGA registration via a standard application pathway, or access under the Special Access Scheme (SAS) or Authorised Prescriber scheme.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — bifunctional alkylating agent (nitrogen mustard derivative) with concurrent purine analogue activity; mechanistically distinct from pure alkylating agents such as cyclophosphamide |
| Myelosuppression Risk | High — neutropenia and lymphopenia are the predominant dose-limiting toxicities; T-cell lymphopenia is prolonged and clinically significant (increased infection risk for months post-treatment); thrombocytopenia and anaemia also reported |
| Emetogenicity Classification | Moderate (standard-dose IV regimen: 90–120 mg/m² on Days 1–2 of a 28-day cycle) |
| Monitoring Items | Full blood count with differential (prior to each cycle and at mid-cycle nadir), liver function tests, serum creatinine and eGFR, electrolytes, QTc interval (cardiac monitoring during infusion recommended) |
| Handling Protection | Must be prepared and administered in accordance with cytotoxic drug safety regulations; SHPA Guidelines for Hazardous Medicines and Safe Handling of Cytotoxics apply; closed-system drug transfer devices (CSTD) recommended for reconstitution |

---

## Safety Considerations

As bendamustine is not TGA-registered in Australia, no TGA-approved Product Information (PI) is available locally. Please refer to the product information from approved international markets for comprehensive safety guidance:

- **US FDA label (Treanda®/Bendeka®):** Available at [DailyMed](https://dailymed.nlm.nih.gov/) — covers myelosuppression, severe infection (including opportunistic infections such as PCP and herpes reactivation), anaphylaxis and infusion reactions, tumour lysis syndrome, skin reactions (including Stevens-Johnson syndrome), embryofoetal toxicity, and secondary malignancies
- **EMA SmPC (Levact®):** Available via [EMA product page](https://www.ema.europa.eu/) — includes additional guidance on use in hepatic and renal impairment

Drug interaction data was unavailable in this evidence pack. Clinically relevant interactions to review include: other myelosuppressive agents, live attenuated vaccines (contraindicated), allopurinol (may increase bendamustine skin toxicity), and CYP1A2 inhibitors/inducers.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (including SHINE, BRIGHT, and others) provide the highest level of evidence (L1) directly supporting bendamustine — as part of the BR regimen — for mantle cell lymphoma. BR is now the internationally accepted chemotherapy backbone against which novel MCL therapies are evaluated, making the mechanistic and clinical case for this indication exceptionally strong.

**To proceed, the following is needed:**

- **TGA registration pathway:** Initiate a TGA product registration application or access via Special Access Scheme (SAS Category B) for individual patients — the drug currently has no Australian market authorisation for any indication
- **Safety dossier completion:** Obtain the current US FDA Treanda®/Bendeka® package insert and EMA Levact® SmPC; document full warnings, contraindications, drug interaction profile, and special population guidance (hepatic/renal impairment, elderly)
- **Mechanism of action documentation:** Retrieve complete MOA data from DrugBank (DB06769) to support pharmacology section of any TGA submission
- **Australian clinical guideline alignment:** Confirm endorsement of BR-based regimens in Australian MCL guidelines (ALLG, Cancer Council Australia, Lymphoma Australia clinical practice frameworks)
- **Infection prophylaxis protocol:** Develop an Australian-context risk management plan for T-cell lymphopenia — including cotrimoxazole prophylaxis for PCP, antiviral prophylaxis for herpes/CMV reactivation, and vaccination scheduling — in line with COSA and SHPA standards
- **Pharmacy safety framework:** Establish cytotoxic handling, preparation, and disposal protocols compliant with Australian WHS legislation prior to any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

