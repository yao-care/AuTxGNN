---
layout: default
title: Zidovudine
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zidovudine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection and AIDS"
monitor_inn: "Zidovudine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "AIDS related complex", "congenital human immunodeficiency virus", "fibroma of prostate", "Brenner tumor", "female breast carcinoma", "benign reproductive system neoplasm"]
---

# Zidovudine
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

# Zidovudine: From HIV Infection and AIDS to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Zidovudine is an antiretroviral medicine originally used to treat HIV infection and AIDS in people.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV/FeLV-related disease in cats)**, a veterinary condition.
This is supported by **0 registered clinical trials** and **20 publications**, all animal studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (the ARTG approved-indication text is not available in the data compiled for this report) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 (veterinary clinical and cohort studies; the remainder is preclinical animal work) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Zidovudine is a nucleoside reverse transcriptase inhibitor (NRTI). Detailed mechanism-of-action data were not available in the data compiled for this report. Based on its drug class, it is converted inside cells to an active triphosphate form that blocks the reverse transcriptase enzyme, which retroviruses need to replicate.

Feline immunodeficiency virus (FIV) is a lentivirus closely related to HIV. It replicates through the same reverse transcriptase-dependent process, so the mechanism is directly conserved. This explains the very high model score, and zidovudine has long been used experimentally in cats.

The prediction is a veterinary indication, so it is of limited relevance to human drug repurposing. It largely reflects the drug's existing antiretroviral activity in a closely related animal model. The findings in the same-family simian immunodeficiency virus (SIV) model point the same way.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Veterinary clinical study | Viruses | Compared zidovudine alone and combined with interferon-α, lamivudine or valproic acid in naturally FIV-infected cats over one year, assessing viral load, CD4+/CD8+ ratio and neurological signs |
| [7495172](https://pubmed.ncbi.nlm.nih.gov/7495172/) | 1995 | Controlled veterinary study | Zentralbl Veterinarmed A | Long-term oral AZT (5 mg/kg three times daily) vs conventional symptomatic therapy in FIV-seropositive cats with clinical disease (n = 9 vs 5) |
| [1363008](https://pubmed.ncbi.nlm.nih.gov/1363008/) | 1992 | Veterinary clinical study | Vet Immunol Immunopathol | Assessed efficacy and side effects of AZT and PMEA in cats naturally infected with FIV or FeLV who had clinical symptoms |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Veterinary follow-up | J Feline Med Surg | Effects of 5-6 years of antiretroviral therapy, starting with AZT, in FIV-infected domestic cats |
| [21723621](https://pubmed.ncbi.nlm.nih.gov/21723621/) | 2011 | Veterinary cohort | Vet Immunol Immunopathol | Immune-endocrine interactions in 20 treated and untreated naturally FIV-infected cats followed for six months |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Experimental animal study | Arch Virol | In experimentally infected cats, zidovudine did not prevent infection but lowered plasma virus titres at 2 weeks |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Experimental animal study | J Acquir Immune Defic Syndr | Prophylactic zidovudine prevented early viraemia and lymphocyte decline but not primary FIV infection |
| [7749786](https://pubmed.ncbi.nlm.nih.gov/7749786/) | 1995 | Experimental animal study | J Acquir Immune Defic Syndr | Early suppression of viraemia did not alter the spread of FIV infection; CD4 counts were higher in treated cats |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Animal study (FeLV) | Antimicrob Agents Chemother | Interferon-α plus AZT vs AZT alone in presymptomatic cats with persistent FeLV-related immunodeficiency |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | Animal study (FeLV) | J Acquir Immune Defic Syndr | AZT inhibited FeLV-FAIDS replication in vitro, with added effect from interferon-α; oral dosing in cats reached measurable plasma levels |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| 10266H | Retrovir | Capsule 100 mg (oral) |

---

## Safety Considerations

Disease associations recorded for zidovudine in the knowledge graph used by the model (these are not label text) include:
- **Haematological:** neutropenia, agranulocytosis, anaemia (including macrocytic anaemia)
- **Hepatic and metabolic:** liver disease and failure, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis, hypertriglyceridaemia, pancreatitis, gallbladder disease
- **Muscle:** myopathy, myositis, dermatomyositis, skeletal muscle disease
- **Other:** kidney disease, obesity disorders

Drug interactions: 100 interactions were recorded. The main ones are:
- **Moderate:** amphotericin B (including lipid and cholesteryl sulfate formulations), corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), statins (rosuvastatin, simvastatin), naltrexone and orlistat
- **Minor:** cimetidine and clarithromycin

Trial literature also describes pharmacokinetic interactions with probenecid and acetaminophen.

For full warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a veterinary indication supported only by animal studies, with no human trials. It is of limited value for human drug repurposing in Australia. The model's high score mainly reflects zidovudine's known antiretroviral mechanism.

Two lower-ranked predictions have direct human evidence, but they fall within the existing HIV indication family rather than being true repurposing. They are:
- **AIDS-related complex:** a completed Phase 3 trial (NCT00001011, 538 participants), which is historical because current practice uses combination antiretroviral therapy.
- **Perinatal and congenital HIV:** Phase 3 trials (NCT00102960, NCT00001104) and guideline-level evidence.

These two could proceed with guardrails: haematological monitoring, myopathy and lactic acidosis surveillance, DDI review, and monitoring for congenital malformations and neonatal haematological toxicity in pregnancy use.

**To proceed, the following is needed:**
- A clear scope decision on whether veterinary indications are in scope for this assessment
- Detailed mechanism-of-action data
- TGA Product Information warnings and contraindications, and the approved indication text for the ARTG entry
- For the human-relevant predictions, comparison against current Australian antiretroviral guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

