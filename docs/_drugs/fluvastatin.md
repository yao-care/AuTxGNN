---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 6
monitor_inn: "Fluvastatin"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "fibroma of prostate"]
last_modified_at: 2026-10-23
description: "Fluvastatin: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Fluvastatin: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Fluvastatin is a statin (HMG-CoA reductase inhibitor).
The TxGNN model predicts it may be relevant to **HIV infectious disease**, but the 13 publications compiled for this report mainly concern lipid management and drug interactions in people with HIV, not treatment of HIV itself. No clinical trials are registered in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

**Evidence level note:** Several publications study fluvastatin in people with HIV, but they address dyslipidaemia, drug interactions or HCV co-infection. None of them studies fluvastatin as a treatment for HIV infection itself. Under the evidence rules, the level is therefore L5.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Fluvastatin is known as a statin that inhibits HMG-CoA reductase and lowers LDL cholesterol.

Fluvastatin is not an antiviral. The link to HIV is indirect. Statins may reduce inflammation and immune activation in treated HIV, and fluvastatin has been studied for dyslipidaemia in people on protease inhibitors. It is metabolised mainly by CYP2C9 rather than CYP3A4, so it is less likely to interact with antiretroviral protease inhibitors than some other statins. One preclinical study reported a protective effect on podocytes in a mouse model of HIV-associated nephropathy.

These data support lipid management and possible adjunctive benefits in people with HIV. They do not show that fluvastatin treats HIV infection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | Open-label randomised controlled study | J Antimicrob Chemother | Fluvastatin as an adjuvant to pegylated interferon and ribavirin in HIV/HCV genotype 1 co-infection |
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | Clinical study | AIDS | Efficacy and safety of fluvastatin in hyperlipidaemic, protease inhibitor-treated HIV patients |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | Clinical study | Infection | Fluvastatin and pravastatin for lipid lowering in HIV patients on antiretroviral therapy, including interaction with indinavir |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | Pilot study | J Viral Hepat | Pilot study of whether fluvastatin favours HCV replication in HIV-HCV co-infected patients |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | Randomised clinical study | AIDS | In 20 HIV patients, ezetimibe lowered LDL-C by 20% and fluvastatin 80 mg/day by 24%, with no significant difference between groups |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | Cohort/clinical study | AIDS Res Hum Retroviruses | Statin use and inflammation and immune activation biomarkers in HIV patients on effective antiretroviral therapy (statins in general, not fluvastatin specifically) |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Review | Clin Pharmacokinet | Drug interactions between statins and antiviral protease inhibitors |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Review | AIDS | Statins and fibrates for hyperlipidaemia in HIV-infected patients on HAART |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | Preclinical (mouse) | Nephrol Dial Transplant | Fluvastatin prevented podocyte injury in a murine model of HIV-associated nephropathy |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | Randomised trial | AIDS | Rosuvastatin versus pravastatin in dyslipidaemic HIV patients on protease inhibitors (not fluvastatin, so indirect evidence) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13558N | Lescol XL | Tablet (prolonged release) 80 mg (as sodium) | Not stated in the data compiled for this report |

## Safety Considerations

- **Conditions recorded as contraindications in the knowledge graph (not label text):** liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury.
- **Drug interactions:** The interaction query returned 100 records. Moderate-level interactions include other statins (rosuvastatin, simvastatin), aprepitant, metronidazole, tinidazole, oxandrolone, naltrexone, nateglinide, nitisinone, glyburide and pectin. Several others, such as cimetidine, famotidine, pantoprazole, doxycycline and aspirin, have an unknown severity level.
- **Antiretroviral combinations:** The publications suggest fluvastatin is less affected by protease inhibitors than some other statins, but the interaction literature should be reviewed before any combined use.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high prediction score is not backed by any study of fluvastatin as a treatment for HIV infection. The existing literature concerns lipid control, drug interactions and HCV co-infection in people with HIV. The other predicted diseases (CETP deficiency, a rare neurodevelopmental disorder, feline and simian immunodeficiency viruses, and prostate fibroma) have no supporting trials or publications and appear to reflect network associations only.

**To proceed, the following is needed:**
- Mechanism of action data and a defined hypothesis for any HIV-related benefit (for example, immune activation or inflammation endpoints)
- Clinical studies of fluvastatin that directly assess an HIV-related outcome rather than lipid lowering
- The TGA-approved PI, including approved indications, warnings and contraindications for Lescol XL
- A review of interactions with common antiretroviral regimens, and monitoring for muscle and liver adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

