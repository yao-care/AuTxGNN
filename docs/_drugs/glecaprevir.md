---
layout: default
title: Glecaprevir
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-03
monitor_inn: "glecaprevir"
predicted_indications: ["HIV infectious disease", "hepatitis B virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Glecaprevir: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Glecaprevir
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

## Glecaprevir: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Glecaprevir is a hepatitis C virus (HCV) NS3/4A protease inhibitor, marketed in Australia in a fixed-dose tablet with pibrentasvir (Maviret).
The TxGNN model predicts it may be relevant to **HIV infectious disease**, but the studies retrieved treat hepatitis C in people who also have HIV, not HIV itself.
Evidence level is **L5**: **7 clinical trials** and **21 publications** were retrieved, but none directly studies HIV infection as the target disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Glecaprevir is known to inhibit the HCV NS3/4A protease, and it has no established direct anti-HIV activity.

The high TxGNN score most likely reflects the close relationship between HIV and HCV: the two infections share patient populations, and there are well-documented drug interactions between HCV antivirals and HIV antiretrovirals. The retrieved trials and papers involve HIV/HCV co-infection, where glecaprevir/pibrentasvir treats the hepatitis C component. This is better understood as use in a co-infected population than as true repurposing against HIV. The prediction should be treated as a research question, not a treatment signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: glecaprevir/pibrentasvir (ABT-493/ABT-530) in HCV genotype 1–6 with HIV-1 co-infection; the endpoint is HCV outcome |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Placebo-controlled study in non-cirrhotic Asian adults with HCV, with or without HIV co-infection |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | Open-label study in Asian adults with HCV and compensated cirrhosis, with or without HIV co-infection |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot of DAA regimens, including glecaprevir/pibrentasvir, in recently acquired HCV with or without HIV; the regimen is largely paritaprevir-based |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week glecaprevir/pibrentasvir in acute HCV, with or without HIV-1 co-infection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV eradication in HCV mono-infected and HIV/HCV co-infected people |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Recruiting | 30 | Pharmacokinetics and safety of glecaprevir/pibrentasvir started in pregnancy, with or without HIV |

All of these trials measure HCV or related outcomes. None tests glecaprevir as a treatment for HIV infection itself.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Real-world response to glecaprevir/pibrentasvir in HIV/HCV-coinfected patients |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Observational | Clin Exp Hepatol | Effectiveness of glecaprevir/pibrentasvir in HIV/HCV patients on bictegravir/emtricitabine/tenofovir alafenamide |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | Pharmacology | J Infect Dis | Drug interactions of glecaprevir/pibrentasvir with HIV antiretrovirals |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Meta-analysis | Int J Antimicrob Agents | Systematic review of 13 studies (3,082 patients); overall SVR12 97.8% in HCV |
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | Single-arm Phase IIIb | J Hepatol | 8-week glecaprevir/pibrentasvir in acute HCV |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Cohort | Adv Ther | Real-world 8-week regimen in treatment-naive patients with compensated cirrhosis |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapy |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | Overview of glecaprevir/pibrentasvir for chronic HCV |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Protease inhibitor therapy for HCV, noting HIV coinfection rates |
| [38367631](https://pubmed.ncbi.nlm.nih.gov/38367631/) | 2024 | Review | Lancet Gastroenterol Hepatol | Global registration and reimbursement of HCV direct-acting antivirals |

The literature concerns HCV treatment, including in people with HIV. It does not show anti-HIV activity.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11332K | Maviret | Tablet containing 100 mg glecaprevir with 40 mg pibrentasvir | Not stated in the data compiled for this report |

---

## Safety Considerations

**Drug Interactions** (57 interactions recorded; selected examples):
- **Major:** rosuvastatin, simvastatin, edoxaban
- **Moderate:** dexamethasone, esomeprazole, omeprazole, apixaban, betrixaban, cobicistat, deferasirox, metreleptin, naldemedine, troglitazone, lusutrombopag, revefenacin, griseofulvin
- **Minor:** fidaxomicin, naloxegol, prucalopride, indacaterol

Because HIV antiretrovirals are frequently co-prescribed, interaction checking is particularly important (see PMID 31504702). Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Glecaprevir has no established anti-HIV mechanism, and every trial and publication retrieved addresses hepatitis C, including in people with HIV co-infection, rather than HIV infection itself. The evidence level is therefore L5, and the high score most likely reflects the HIV–HCV relationship rather than an HIV-directed effect.

**To proceed, the following is needed:**
- In vitro evidence of anti-HIV activity, as no such data are currently available
- Detailed mechanism of action data
- Clarification of whether the intended value lies in treating HCV in co-infected people (an existing use) rather than in treating HIV
- Review of the PI for safety and antiretroviral interaction guidance

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

