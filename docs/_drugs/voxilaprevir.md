---
layout: default
title: Voxilaprevir
parent: Model Prediction Only (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
---

# Voxilaprevir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Voxilaprevir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Voxilaprevir is an HCV NS3/4A protease inhibitor, originally used (as part of a fixed-dose combination with sofosbuvir and velpatasvir) to treat chronic hepatitis C virus infection.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but there are **no clinical trials** and **no publications** that actually test voxilaprevir against HBV, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (the ARTG entry holds no indication text; this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (the data compiled for this report assigns L4, but none of the retrieved publications tests voxilaprevir in HBV, so L5 is the more accurate level) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the compiled data. Based on known information, voxilaprevir is an HCV NS3/4A serine protease inhibitor, used in combination with sofosbuvir (an NS5B polymerase inhibitor) and velpatasvir (an NS5A inhibitor). Its efficacy in HCV, including retreatment after failure of other direct-acting antivirals, is well established.

A direct mechanistic link to HBV is **not supported**. HBV replicates through a reverse transcriptase/polymerase and a core-capsid-based process and has no NS3/4A-like protease. The very high TxGNN score most likely reflects network proximity within the viral hepatitis category rather than a pharmacological rationale. HBV matters for voxilaprevir mainly as a safety issue: HBV reactivation is a recognised risk during DAA therapy in HCV/HBV co-infected patients. That is not a therapeutic effect.

Other predictions (ranks 2–10) were also reviewed. Hepatitis A, hepatitis E, HIV and the animal-model conditions all lack a plausible direct mechanism, and none has trial or literature evidence of voxilaprevir activity. Omsk haemorrhagic fever and Kyasanur forest disease involve flaviviruses related to HCV, so NS3 protease homology offers a speculative rationale, but there is no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials are registered for hepatitis B virus infection.

## Literature Evidence

None of the nine retrieved publications tests voxilaprevir against HBV. They concern HCV and are listed only for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Single-arm trial (cohort) | Lancet Gastroenterol Hepatol | SOF/VEL/VOX retreatment of HCV after prior DAA failure in Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world SOF/VEL/VOX in Romanian genotype 1b patients who did not respond to earlier DAAs |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapy |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Preclinical/virology | Hepatology | Resistance patterns of HCV protease inhibitor escape variants |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA treatment failure in an HCV elimination programme |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | Summary of the International Conference on Viral Hepatitis 2017 |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Economic analysis | Ann Hepatol | International comparison of HBV and HCV drug prices |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Epidemiology | Vopr Virusol | Prevalence of HIV, HBV and HCV markers among dental patients |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11658N | Vosevi | Tablet containing 400 mg sofosbuvir with 100 mg velpatasvir and 100 mg voxilaprevir (oral) | Indication text not recorded in the data compiled for this report |

## Safety Considerations

- **Drug Interactions:** 19 interacting drugs were identified (Moderate and Major). The Major-level interactions are:
  - Rosuvastatin
  - Edoxaban
  - Cyclosporine

  Moderate-level interactions include:
  - Apixaban
  - Cobicistat
  - Ethinylestradiol
  - Eltrombopag
  - Obeticholic acid
  - Eluxadoline
  - Several oncology agents (afatinib, bosutinib, cobimetinib, idelalisib, lapatinib, lenvatinib, olaparib, pazopanib)
  - Artesunate
  - Teriflunomide
- **HBV reactivation:** In HCV/HBV co-infected patients, HBV reactivation is a recognised risk during DAA therapy. This is a safety consideration and does not indicate benefit against HBV.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. HBV has no NS3/4A-like protease target, no trial or publication tests voxilaprevir in HBV, and no other predicted indication has credible supporting evidence either.

**To proceed, the following is needed:**
- In vitro antiviral activity data for voxilaprevir against HBV
- Mechanism of action data (MOA) to test any plausible link
- TGA Product Information warnings and contraindications for safety screening
- A review of HBV reactivation risk and monitoring in HCV/HBV co-infected patients
- If any new indication is pursued, an interaction-management plan covering the Major-level interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

