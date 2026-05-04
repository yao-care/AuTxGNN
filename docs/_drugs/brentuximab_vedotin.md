---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma to Follicular Lymphoma

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before therapeutic application.

---

## One-Sentence Summary

Brentuximab vedotin (BV; brand name Adcetris®) is an anti-CD30 antibody-drug conjugate globally approved for classical Hodgkin lymphoma (cHL) and systemic anaplastic large cell lymphoma (sALCL), but not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **follicular lymphoma (FL)**, supported by **1 actively recruiting Phase 2 clinical trial** and **20 publications**, primarily concentrated in CD30-positive or histologically transformed FL subgroups.
The overall evidence base is at **Level L3** (observational studies and case series), and patient selection by CD30 expression status is the critical gating requirement before any clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma (global approvals; no TGA registration in Australia) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, brentuximab vedotin is an antibody-drug conjugate (ADC) comprising an anti-CD30 monoclonal antibody (brentuximab) covalently linked to the potent microtubule-disrupting cytotoxin monomethyl auristatin E (MMAE) via a protease-cleavable linker. Upon binding CD30 on the surface of tumour cells, the ADC is internalised; lysosomal proteases cleave the linker, releasing MMAE intracellularly. Free MMAE disrupts tubulin polymerisation, arrests the cell cycle at G2/M, and triggers apoptosis. The global approval of BV in cHL and sALCL is founded on this CD30-selective mechanism of tumour killing.

Follicular lymphoma is typically a CD30-negative B-cell malignancy, which makes unselected FL an unlikely candidate for BV. However, a clinically important subset of FL — particularly those undergoing histological transformation towards anaplastic large cell lymphoma (ALCL) or high-grade B-cell lymphoma — can acquire robust CD30 surface expression. A published case report (PMID 32476657) documents a complete response in a patient whose Grade 1 FL transformed to CD30-positive, ALK1-negative ALCL, treated successfully with BV and high-dose methotrexate. Separately, folliculotropic mycosis fungoides — a variant of cutaneous T-cell lymphoma with marked involvement of hair follicles — has also demonstrated responsiveness to BV (PMID 41409526), supporting the concept of CD30 targeting within follicular lymphoid compartments.

The TxGNN prediction therefore reflects a biologically plausible **subset hypothesis**: BV is unlikely to benefit unselected FL patients, but may offer meaningful activity in the CD30-positive, transformed, or follicular T-helper cell-phenotype subpopulation. Prospective CD30 immunohistochemical screening is the essential gating criterion for any investigational use, and one actively recruiting Phase 2 trial (NCT04587687) is directly examining BV plus bendamustine in relapsed/refractory FL, providing the formal clinical framework to answer this question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|------------|------|--------|----------|------------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine for R/R follicular lymphoma. The only active FL-specific BV trial; targets CD30-positive FL. Results pending (expected completion December 2026). |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + bendamustine + rituximab for R/R CD30-positive B-cell NHL including FL. Withdrawn before enrolment commenced; no data generated. |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Risk-stratified sequential therapy with rituximab, BV, and bendamustine (RBvB) in newly diagnosed post-transplant lymphoproliferative disorders with CD20/CD30 co-expression. Withdrawn before enrolment; no data. |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline for CD30+ and/or EBV+ lymphomas (including FL). Terminated early. Non-FL-specific design, but establishes the CD30 selection framework relevant to FL investigation. |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomised R-bendamustine ± BV for R/R CD30-positive DLBCL. Terminated early; limited conclusions, but provides partial safety data for BV + bendamustine backbone used in the active FL trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf J Oncol | Grade 1 FL transformed to CD30+ ALK1-negative ALCL achieved complete response to BV + high-dose methotrexate — the most direct published evidence of BV efficacy in the FL transformation setting |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Case Report | Skin Appendage Disord | Extensive follicular mucinosis (folliculotropic MF/CTCL variant) with irreversible alopecia responded to BV; supports CD30-directed targeting within follicular lymphoid tissue |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leuk Res Rep | Immunotherapy in indolent NHL; covers FL treatment landscape including emerging CD30-directed and immunomodulatory strategies; contextualises BV's potential role |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2 Trial | Blood Adv | BV + gemcitabine (GBV) in R/R PTCL (CD30 ≥5% by IHC); primary endpoint ORR met with BV maintenance phase. Demonstrates clinically meaningful BV activity even in CD30-low lymphomas |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Real-World Study | Adv Ther | BV + cyclophosphamide/epirubicin/prednisone in untreated CD30+ PTCL subtypes (PTCL-TFH, ALCL, AITL) in Chinese patients; high short-term remission rates and manageable toxicity |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | Review | Hematol Oncol Clin N Am | Angioimmunoblastic T-cell lymphoma (AITL) — a follicular T-helper (Tfh)-derived neoplasm biologically related to FL; BV highlighted as an emerging therapeutic agent in this follicular-origin disease |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Updates BV + CHP frontline standard for CD30+ PTCLs; addresses CD30 expression threshold debate and patient selection principles directly transferable to FL subgroup design |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology ASH Educ | Comprehensive synthesis of BV incorporation into lymphoma management; discusses minimum CD30 thresholds, combination strategies, and future indications relevant to FL investigation |
| [29023638](https://pubmed.ncbi.nlm.nih.gov/29023638/) | 2018 | Review | Br J Dermatol | Optimal BV regimen for CD30+ cutaneous lymphomas — addresses dosing and scheduling considerations applicable to non-classical CD30+ lymphoid malignancies |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplant | Post-ASCT maintenance in lymphoma; BV maintenance established for high-risk HL; also covers FL maintenance context, relevant to consolidation strategies after FL response |

---

## Australia Market Information

Brentuximab vedotin is **not registered with the Therapeutic Goods Administration (TGA)** and has no ARTG entries. It is not commercially available through standard Australian supply channels.

**Access options for Australian clinicians:**

- **TGA Special Access Scheme (SAS) Category B:** Individual patient access for serious or life-threatening conditions where no alternative is available
- **Clinical Trial Enrolment:** Check ANZCTR (anzctr.org.au) for any Australian sites participating in BV studies
- **Managed Access Programmes:** Contact the Australian distributor/sponsor (Seagen/Pfizer) regarding any compassionate access pathways

Globally, Adcetris® (brentuximab vedotin) holds regulatory approval in the USA (FDA), EU (EMA), UK (MHRA), Japan (PMDA), and Taiwan (TFDA) for classical Hodgkin lymphoma, systemic ALCL, primary cutaneous ALCL, CD30+ peripheral T-cell lymphoma (BV-CHP regimen), and primary cutaneous CD30+ T-cell lymphoproliferative disorders.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic — Antibody-Drug Conjugate (ADC); payload MMAE is a potent synthetic auristatin-class antimitotic (microtubule inhibitor) |
| Myelosuppression Risk | Moderate to High — neutropenia is the most frequently reported Grade 3–4 adverse event (febrile neutropenia also documented); anaemia and thrombocytopenia occur at lower frequency |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Full blood count (FBC) with differential before each cycle; liver function tests (LFTs); renal function; neurological assessment for peripheral neuropathy (sensory and motor) at each visit; pregnancy test in women of childbearing potential prior to each cycle |
| Handling Protection | Must be prepared and administered under cytotoxic drug handling procedures — preparation in a biological safety cabinet by trained oncology pharmacy staff; appropriate personal protective equipment (gloves, gown, eye protection) required for all preparation and administration steps |

---

## Safety Considerations

No TGA-approved Australian Product Information exists. Please refer to the **FDA Prescribing Information for ADCETRIS®** or the **EMA Summary of Product Characteristics** for complete safety data. The following key safety signals are established from global post-marketing experience:

- **Peripheral neuropathy:** Progressive cumulative sensory and motor neuropathy requiring dose delay, reduction, or permanent discontinuation — the most clinically impactful chronic toxicity
- **Progressive Multifocal Leukoencephalopathy (PML):** JC virus reactivation leading to PML (including fatal cases) — carries a black-box warning; monitor for new or worsening neurological, cognitive, or behavioural symptoms
- **Pulmonary toxicity:** Non-infectious pneumonitis and interstitial lung disease — hold BV and investigate any new pulmonary symptoms
- **Serious infections:** Opportunistic infections including *Pneumocystis jirovecii* pneumonia and herpes zoster — PCP prophylaxis should be considered
- **Infusion-related reactions:** Including anaphylaxis — premedication and monitoring protocols required; administration must occur in a facility equipped for anaphylaxis management
- **Embryo-foetal toxicity:** Contraindicated in pregnancy; effective contraception required during and for 6 months after treatment for both male and female patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction has genuine biological plausibility for the CD30-positive or histologically transformed FL subgroup, supported by a mechanistically coherent framework (CD30-targeted MMAE delivery), a direct case report of complete response in transformed FL, and one actively recruiting Phase 2 trial. However, BV is not expected to benefit unselected, CD30-negative FL patients — the evidence base is L3, and the drug is not currently accessible in Australia through standard channels.

**To proceed, the following is needed:**

- **CD30 IHC screening protocol:** Define a minimum CD30 positivity threshold (e.g., ≥1%, ≥10%, or ≥20% tumour cells) as a mandatory inclusion criterion for any FL-BV investigation — this is the single most important gating step
- **TGA access pathway:** Clarify SAS Category B eligibility or identify Australian sites for international BV trials before initiating any patient-level discussion
- **Full safety documentation:** Obtain the current FDA Prescribing Information and EMA SmPC to enable complete Australian formulary risk-benefit assessment and institutional pharmacy approval
- **Histological transformation surveillance:** Develop a biopsy protocol for FL patients with clinical signs of transformation (rapid progression, elevated LDH, B symptoms) to prospectively identify the CD30+ subgroup most likely to benefit
- **Results of NCT04587687:** Await enrolment completion and preliminary efficacy data from the only active FL-specific BV trial before committing to broader institutional investigation
- **Multidisciplinary consultation:** Engage haematology, pharmacy, and ethics/governance prior to any SAS application given the absence of local regulatory approval and the investigational nature of this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

