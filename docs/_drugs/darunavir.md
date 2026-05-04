---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Darunavir
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

# Darunavir: From HIV-1 Infection to Congenital HIV

## One-Sentence Summary

Darunavir is a second-generation HIV-1 protease inhibitor used to treat HIV-1 infection in adults and children, with a well-established role in combination antiretroviral therapy (cART) regimens globally. The TxGNN model predicts it may be effective for **Congenital HIV** (prevention of mother-to-child transmission and treatment of perinatally infected individuals), with **23 clinical trials** and **9 publications** currently supporting this direction.

> **Note on prediction ranking:** The highest-ranked TxGNN prediction (Rank 1: feline acquired immunodeficiency syndrome, 99.97%) is a veterinary condition with no direct clinical applicability to human patients — the sole trial retrieved was flagged as a data mapping error in the evidence review. This report therefore focuses on **Congenital HIV (Rank 5, 98.97%)**, which carries the strongest human clinical evidence (L1) and the highest actionability recommendation among all predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (treatment-experienced adults and children ≥3 years) |
| Predicted New Indication | Congenital HIV (Mother-to-Child Transmission Prevention and Paediatric Treatment) |
| TxGNN Prediction Score | 98.97% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not available in this Evidence Pack. Based on well-established medical literature, Darunavir is a nonpeptidic HIV-1 protease inhibitor (part of the second-generation protease inhibitor class) that binds with very high affinity to the active site of the HIV-1 protease enzyme. Its efficacy in HIV-1 infection has been extensively proven across numerous Phase 3 clinical trials, and it is approved by the US FDA, EMA, and WHO as an essential medicine. Mechanistically, darunavir prevents the cleavage of HIV Gag and Gag-Pol polyprotein precursors, blocking viral maturation and the production of infectious viral particles — and this mechanism is directly applicable to any HIV-1-related indication.

The connection between darunavir's established adult HIV-1 indication and congenital HIV is mechanistically direct: both involve the same pathogen (HIV-1). Congenital HIV refers to vertical (mother-to-child) transmission occurring in utero, during labour and delivery, or through breastfeeding. Darunavir's role in this context operates on two fronts: first, as part of the mother's Prevention of Mother-to-Child Transmission (PMTCT) regimen to maximally suppress maternal viral load before and during delivery; and second, as a component of treatment regimens for perinatally infected infants and children. The dedicated Phase 2 PMTCT trial NCT02738502 directly evaluated a darunavir/ritonavir-based strategy without NRTIs in pretreated pregnant women.

A clinically important consideration is that darunavir plasma concentrations are meaningfully reduced during pregnancy — particularly in the third trimester — compared with postpartum levels. Pharmacokinetic studies in HIV-positive pregnant women (PMID 25326090; NCT00855335; NCT00042289) have quantified this effect and provide the evidence base for dose adjustment guidance. The TxGNN prediction score of 98.97% aligns with this rich clinical evidence base and represents a clinically meaningful extension of the drug's known indication into the PMTCT and paediatric HIV treatment space.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02738502](https://clinicaltrials.gov/study/NCT02738502) | Phase 2 | Completed | 91 | Feasibility study of darunavir/ritonavir monotherapy as a PMTCT strategy without any NRTIs in pretreated pregnant women, combined with neonatal nevirapine prophylaxis; directly addresses congenital HIV prevention |
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | Characterised the pharmacokinetics of darunavir/ritonavir and darunavir/cobicistat in HIV-1 infected pregnant women; demonstrated reduced exposure in the third trimester, supporting the need for dose adjustment |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1,578 | Prospective PK evaluation of ARVs including darunavir in pregnant women and their infants (IMPAACT P1026s); the largest maternal ARV pharmacokinetic dataset available |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | Evaluated PK of ARV and anti-TB drugs during pregnancy and postpartum, including darunavir-containing regimens in co-infected women |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | Large RCT demonstrating non-inferiority of switching to D/C/F/TAF single-tablet regimen in virologically suppressed HIV-1 adults; establishes robust efficacy of the boosted darunavir backbone |
| [NCT02431247](https://clinicaltrials.gov/study/NCT02431247) | Phase 3 | Completed | 725 | D/C/F/TAF vs darunavir/cobicistat + FTC/TDF in ARV-naive adults; confirms the efficacy of darunavir as a foundation agent for treatment initiation |
| [NCT02275780](https://clinicaltrials.gov/study/NCT02275780) | Phase 3 | Completed | 769 | Double-blind RCT of doravirine vs darunavir/ritonavir in treatment-naive HIV-1 infection; darunavir/r served as active comparator, reinforcing its role as a benchmark first-line agent |
| [NCT01281813](https://clinicaltrials.gov/study/NCT01281813) | Phase 3 | Completed | 145 | Continued access to darunavir/ritonavir in adults and paediatric patients (≥3 years) in countries where darunavir was commercially unavailable; includes paediatric dosing and safety data |
| [NCT06747507](https://clinicaltrials.gov/study/NCT06747507) | Phase 3 | Recruiting | 392 | Randomised trial of maintaining dolutegravir vs switching to ritonavir-boosted darunavir in patients with DTG-associated resistance mutations; supports darunavir's role as a second-line and salvage option |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Non-inferiority RCT of DTG+RPV switch from PI-based regimens (including darunavir); reinforces the breadth of the evidence ecosystem supporting antiretroviral sequencing decisions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38788744](https://pubmed.ncbi.nlm.nih.gov/38788744/) | 2024 | RCT | The Lancet HIV | D2EFT trial: dolutegravir plus boosted darunavir demonstrated non-inferiority to standard second-line ART after NNRTI failure across diverse global settings; highest-tier evidence for darunavir in second-line use |
| [38864586](https://pubmed.ncbi.nlm.nih.gov/38864586/) | 2024 | Cohort | AIDS | US cohort characterising congenital anomaly rates following first-trimester exposure to newer ARVs including darunavir; key safety data for PMTCT regimen selection |
| [25326090](https://pubmed.ncbi.nlm.nih.gov/25326090/) | 2015 | PK Study | J Antimicrobial Chemotherapy | Total and unbound darunavir pharmacokinetics in HIV-infected pregnant women in the third trimester and postpartum; demonstrates significant reduction in exposure during pregnancy |
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Case Series | Antiviral Therapy | Two cases of darunavir (with etravirine and/or raltegravir) use in treatment-experienced pregnant women; earliest published evidence of darunavir feasibility in pregnancy |
| [35809963](https://pubmed.ncbi.nlm.nih.gov/35809963/) | 2022 | Case Report | Chest | 28-year-old man with congenital HIV presenting with bilateral pulmonary nodules; illustrates long-term clinical complexity in perinatally infected adults receiving ART throughout life |
| [34151853](https://pubmed.ncbi.nlm.nih.gov/34151853/) | 2021 | Case Report | J Neuromuscular Diseases | Inflammatory myositis secondary to ART in a 5-year-old child with congenital HIV on a darunavir-containing regimen; important paediatric safety signal for musculoskeletal monitoring |
| [33048878](https://pubmed.ncbi.nlm.nih.gov/33048878/) | 2021 | Cohort | AIDS | Risk of birth defects and adverse perinatal outcomes with integrase inhibitor exposure at conception; provides comparative safety context relevant to PMTCT regimen selection |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | Clinical Infectious Diseases | Pharmacovigilance database analysis of dolutegravir safety signals in pregnancy (neural tube defect concern); contextualises the clinical rationale for darunavir-based alternatives in PMTCT |
| [25172528](https://pubmed.ncbi.nlm.nih.gov/25172528/) | 2015 | Case Report | Arch Soc Esp Oftalmol | Retinal folds as a previously unreported adverse effect of darunavir in a 20-year-old HIV patient; highlights the importance of ophthalmological monitoring in young patients on long-term darunavir therapy |

---

## Australia Market Information

Darunavir has **no current ARTG entries** and is **not registered with the Therapeutic Goods Administration (TGA)** in Australia.

Use in Australian patients would require access through one of the following TGA pathways:

- **Special Access Scheme (SAS) – Category B**: For individual patients where a clinician determines the drug is appropriate. Application submitted to TGA.
- **Authorised Prescriber Scheme**: For clinicians treating a class of patients on a recurring basis.
- **Clinical Trial Import**: For research use under a Clinical Trial Notification or Approval.

Darunavir (brand name Prezista®; also available as Symtuza® as a fixed-dose combination with cobicistat/emtricitabine/tenofovir alafenamide) is approved in the United States (FDA), European Union (EMA), and is included on the WHO Model List of Essential Medicines. Clinicians seeking access should contact the TGA at **www.tga.gov.au** or the manufacturer (Janssen-Cilag Pty Ltd) for the current Australian access pathway.

---

## Safety Considerations

No safety data was available in this Evidence Pack for the Australian context. Please refer to the TGA-approved Product Information (PI) once registered, or consult the current FDA prescribing information (Prezista®) or EMA Summary of Product Characteristics for comprehensive safety data.

The following considerations are particularly relevant to the congenital HIV indication:

- **Pregnancy pharmacokinetics**: Darunavir plasma exposure is significantly reduced in the third trimester; dose adjustment (e.g., twice-daily dosing) may be required and should be guided by therapeutic drug monitoring
- **Paediatric use**: Weight-based dosing is required for children; minimum age and weight thresholds apply — consult current product labelling for specific paediatric dosing tables
- **Drug interactions**: Darunavir requires a pharmacokinetic booster (ritonavir 100 mg or cobicistat 150 mg); as a potent CYP3A4 inhibitor and substrate, it has numerous clinically significant interactions with other medications commonly used in pregnancy and paediatric care
- **Sulfonamide allergy**: Darunavir contains a sulfonamide moiety; use with caution in patients with known sulfonamide allergy

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 clinical trials — including a dedicated PMTCT study (NCT02738502, n=91) and large Phase 3 RCTs establishing the darunavir backbone (NCT02269917, n=1,149; NCT02275780, n=769) — combined with robust pharmacokinetic data in pregnant women, provide a strong foundation for darunavir's use in congenital HIV prevention and treatment. The TxGNN prediction score (98.97%) is consistent with this clinical evidence base. The principal barrier to use in Australia is the absence of TGA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- [ ] Submit a TGA Special Access Scheme (SAS Category B) application for darunavir, or explore the Authorised Prescriber pathway via an appropriate HIV specialist or clinical network
- [ ] Obtain the complete manufacturer Product Information (PI) for safety, contraindication, and paediatric dosing details
- [ ] Develop a pharmacokinetic monitoring plan for pregnant patients, including third-trimester dose adjustment protocols
- [ ] Establish a paediatric dosing and monitoring protocol for perinatally infected infants and children, aligned with current WHO and PENTA (Paediatric European Network for Treatment of AIDS) guidelines
- [ ] Consult ASHM (Australasian Society for HIV, Viral Hepatitis and Sexual Health Medicine) for local clinical pathway guidance and expert endorsement
- [ ] Confirm reliable supply chain access to cobicistat or ritonavir as required pharmacokinetic boosters
- [ ] Address the formal MOA data gap (DrugBank DB01264 query) to complete the mechanism of action documentation for regulatory submissions

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions should be interpreted in the context of individual patient assessment by qualified healthcare professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

