---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Atazanavir
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

# Atazanavir: From HIV-1 Infection to Congenital Human Immunodeficiency Virus

---

## One-Sentence Summary

Atazanavir (ATV) is a selective HIV-1 protease inhibitor, internationally approved for treatment of HIV-1 infection in adults and paediatric patients, though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Congenital Human Immunodeficiency Virus** (HIV acquired through mother-to-child vertical transmission),
supported by **multiple completed Phase 3 RCTs** and **7 publications** — including dedicated paediatric trials (PRINCE I & II) and pregnancy pharmacokinetic studies, placing overall evidence at **L1**.

> **Note on TxGNN ranking:** The highest-scoring TxGNN predictions for this drug include veterinary or animal-model diseases (feline AIDS, SIV infection) and clinically obsolete terms, all assessed as Hold (L5). This report focuses on **Congenital Human Immunodeficiency Virus** (TxGNN Rank #5), which is the highest-ranked human disease indication with substantive clinical evidence and a Proceed with Guardrails recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (internationally approved; not registered in Australia) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atazanavir is a highly selective inhibitor of HIV-1 aspartyl protease — an enzyme that cleaves viral polyproteins into functional structural components during the final stage of HIV replication. Without functional protease activity, HIV produces immature, non-infectious viral particles. ATV is typically co-administered with a pharmacokinetic booster (ritonavir or cobicistat) to achieve adequate and sustained plasma concentrations. While detailed mechanism of action data was not available in this Evidence Pack, ATV's role as an HIV-1 protease inhibitor is extensively documented in international literature and regulatory submissions.

Congenital HIV refers to HIV-1 infection acquired through mother-to-child transmission (MTCT) — occurring in utero, perinatally during delivery, or postnatally through breastfeeding. The mechanistic case is direct: the HIV-1 protease targeted by ATV is identical regardless of whether the patient is an adult, a neonate, or a child with vertically acquired infection. Suppressing maternal viral load through effective antiretroviral therapy (ART) is the cornerstone of MTCT prevention, placing ATV squarely within this clinical pathway. Additionally, once a child acquires HIV congenitally, treatment with protease inhibitor-containing regimens follows the same virological principles as adult therapy.

The evidence base specifically supporting ATV in this population is notably robust. The PRINCE I (NCT01099579) and PRINCE II (NCT01335698) paediatric trials evaluated ATV powder plus ritonavir in children as young as 3 months, providing both safety and pharmacokinetic data for neonatal and infant populations. Dedicated pregnancy PK studies (NCT00326716; the large IMPAACT P1026s cohort, NCT00042289) characterise drug exposure across gestational trimesters, and SMARTT prospective cohort data (PMID 27242802) assess safety across multiple developmental domains in over 3,500 HIV-exposed uninfected infants. The TxGNN prediction reflects genuine mechanistic and clinical alignment between ATV's established antiviral activity and the congenital HIV disease context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | 96-week head-to-head comparison of ATV/r vs LPV/r, each with TDF/FTC, in treatment-naïve HIV-1 subjects; established non-inferiority and confirmed ATV/r as a standard-of-care first-line regimen |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II: safety, efficacy, and pharmacokinetics of ATV oral powder + ritonavir in HIV-infected children aged 3 months to under 11 years; directly informs paediatric/congenital HIV dosing |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: safety, tolerability, and PK of ATV oral powder + ritonavir in HIV-infected paediatric patients aged 3 months to under 6 years, including the youngest age cohort relevant to congenital HIV |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | Prospective safety evaluation of ATV capsule + ritonavir in HIV-infected adolescents aged 6–18 years (≥15 kg); confirmed safety profile across the paediatric weight spectrum |
| [NCT00326716](https://clinicaltrials.gov/study/NCT00326716) | Phase 1 | Completed | 69 | PK of ATV/r as part of HAART in HIV-1-infected pregnant women across trimesters; established dose adjustment guidance to ensure adequate foetal and maternal drug exposure |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A | Completed | 1,578 | IMPAACT P1026s: large prospective PK study of ARV drugs (including ATV) in pregnant women and their infants across multiple sites; the most comprehensive ARV pregnancy PK dataset available |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | DTG/ABC/3TC vs ATV+RTV+TDF/FTC in HIV-1-infected ART-naïve women; ATV/r arm provides 48-week efficacy and safety data specifically in women of childbearing age |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | Phase 3 RCT evaluating switch from PI-based regimen (including ATV/r) to dolutegravir + rilpivirine; validates ATV/r as the established PI comparator backbone for virological suppression |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | D/C/F/TAF vs boosted PI + FTC/TDF (boosted PI class includes ATV/r) in virologically suppressed HIV-1 adults; largest switch trial contextualising ATV/r within current PI-based therapy |
| [NCT02227238](https://clinicaltrials.gov/study/NCT02227238) | Phase 3b | Completed | 627 | Dolutegravir vs LPV/r (with ATV/r as permitted active comparator) in treatment-failure HIV-1 adults on first-line therapy; reinforces ATV/r as an established second-line standard |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective cohort | Frontiers in Immunology | PHACS SMARTT study: comprehensive safety assessment of in utero ARV exposure (including ATV) across metabolic, cardiac, neurological, and neurodevelopmental domains in >3,500 HIV-exposed uninfected infants at 22 US sites |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Congenital anomalies and prenatal ARV exposure in HIV-exposed uninfected infants; provides reassuring safety data for most antiretrovirals including ATV when used during pregnancy |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case-control | European Journal of Clinical Pharmacology | Most recent European congenital anomaly registry analysis of fetal ARV exposure; evaluates teratogenicity signals using population-level surveillance data |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort/PK study | Antiviral Therapy | ATV exposure remains therapeutically adequate during pregnancy irrespective of concurrent tenofovir use; supports current standard dosing recommendations in pregnant women |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cross-sectional | Journal of AIDS and Immune Research | Newborn hearing screening outcomes in HIV-exposed uninfected infants from the SMARTT cohort; evaluates auditory safety of in utero ARV exposures |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In vitro/mechanistic | Reproductive Toxicology | ATV and ritonavir interactions with placental efflux transporters (ABCB1, ABCG2, ABCC2) in rats; first mechanistic study characterising transplacental transfer and foetal ATV exposure |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance/Review | Clinical Infectious Diseases | Pharmacovigilance database analysis of ARV safety in pregnancy; contextualises ATV within the broader landscape of antiretroviral teratogenicity and adverse event reporting |

---

## Australia Market Information

Atazanavir is not currently registered on the Australian Register of Therapeutic Goods (ARTG) and has no commercial availability in Australia.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|-------------|-------------|---------------------|
| — | Not registered | — | No ARTG entries exist for atazanavir |

Clinicians in Australia requiring access to atazanavir may apply through the TGA Special Access Scheme (SAS Category B for individual patients, or Category C for unapproved use in clinical contexts). International product information — including the FDA-approved Reyataz® label and the EMA-approved summary of product characteristics — serves as the primary reference for dosing, safety, and monitoring guidance.

---

## Safety Considerations

No specific safety data (key warnings, contraindications, or drug interaction records) were available in this Evidence Pack.

Please refer to the international Product Information (PI) for Atazanavir/Reyataz® (FDA or EMA-approved) for comprehensive safety information, and consult the TGA Special Access Scheme requirements for unapproved therapeutic goods.

**Important clinical note for Australian prescribers:** Atazanavir is internationally recognised to carry significant drug–drug interaction potential, including with proton pump inhibitors (PPIs; may reduce ATV absorption substantially), H₂-receptor antagonists (require dose separation and timing adjustments), antacids, and medications metabolised by CYP3A4 or UGT1A1. ATV also commonly causes asymptomatic unconjugated hyperbilirubinaemia (indirect bilirubin elevation), which is generally benign but can lead to jaundice. These interactions are particularly relevant in the congenital/neonatal setting given the polypharmacy frequently encountered in HIV-positive mothers and in co-managed paediatric patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — including the dedicated PRINCE I and PRINCE II paediatric trials, large-scale pregnancy pharmacokinetic studies, and head-to-head adult trials establishing ATV/r as a standard-of-care regimen — provide L1 evidence directly relevant to the congenital HIV clinical context. The mechanistic link is unambiguous: ATV's HIV-1 protease inhibition addresses the same viral pathway in vertically acquired infection as in adult disease.

**To proceed, the following is needed:**
- TGA Special Access Scheme (SAS) application to access atazanavir for individual patients in Australia
- Full international prescribing information (FDA Reyataz® PI or EMA SmPC) to substitute for unavailable TGA-approved PI
- Comprehensive drug–drug interaction assessment for the patient's concurrent medications, with particular attention to acid-suppressing agents (PPIs, H₂ blockers), rifamycins, and CYP3A4-active drugs
- Weight-band and age-appropriate paediatric dosing confirmation using PRINCE I/II pharmacokinetic data
- Baseline and on-treatment monitoring plan: HIV-1 RNA viral load, CD4+ T-cell count, liver function tests (ALT, AST), total and unconjugated bilirubin, serum creatinine, and urinalysis
- For pregnant patients: trimester-specific PK guidance per IMPAACT P1026s and NCT00326716 data to ensure adequate maternal plasma levels
- Specialist infectious diseases consultation (or paediatric HIV service referral) prior to initiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

