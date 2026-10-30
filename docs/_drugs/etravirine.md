---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 278
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Etravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
description: "Etravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Etravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Etravirine: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Etravirine is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only prediction and should be treated as a low-confidence hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, etravirine is an NNRTI that inhibits HIV-1 reverse transcriptase, including in some strains resistant to first-generation NNRTIs. Its efficacy in HIV infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, which is the likely basis for the prediction. However, FIV reverse transcriptase is generally considered intrinsically less susceptible to NNRTIs, so activity is not expected. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is also a veterinary condition, so any human-health repurposing pathway is unclear.

Other predictions from the model give similar signals:
- **Simian immunodeficiency virus infection** (score 0.9998, L4): SIV is a standard animal model, but SIV (especially SIVmac) is naturally resistant to many NNRTIs. The single linked paper is indirect.
- Remaining predictions (neurodevelopmental disorder, prostate fibroma, Brenner tumour, benign reproductive neoplasms, obsolete familial combined hyperlipidaemia) have no plausible mechanism and appear to be computational artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For context, the closest related predictions have the following indirect literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Cohort/Case series | Antiviral Therapy | Two cases of darunavir and etravirine (with or without raltegravir) use in pregnancy in highly treatment-experienced HIV patients (relevant to congenital HIV) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Risk factors for gastrointestinal adverse events in HIV treated and untreated patients (relevant to AIDS related complex) |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | In vitro/resistance study | AIDS Research and Human Retroviruses | Novel mutations L228I and Y232H cause NNRTI resistance in a combined pattern (relevant to AIDS related complex) |
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical/in vitro | Molecular Pharmaceutics | Nanoparticle-based antiretroviral combinations for synergistic inhibition of HIV transmission (relevant to SIV infection) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10301E | Intelence | Tablet 200 mg | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived associations, not label text): chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease, and peripheral neuropathy.
- **Drug Interactions**: 100 interactions were recorded. The first 20 retrieved are mostly Moderate, with one Minor (ranitidine). Moderate interactions include:
  - Acid suppressants: rabeprazole, omeprazole, cimetidine
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Antidiabetics: pioglitazone, saxagliptin, linagliptin, glimepiride, chlorpropamide
  - Others: aprepitant, clarithromycin, metronidazole, dronabinol, eliglustat, naldemedine, naloxegol

Please refer to the TGA-approved Product Information (PI) for warnings, contraindications and full interaction guidance.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. Biological plausibility is low because FIV and SIV reverse transcriptases are generally less susceptible to NNRTIs. The related predictions are either already covered by the HIV indication or have no plausible mechanism.

**To proceed, the following is needed:**
- In vitro activity data of etravirine against FIV reverse transcriptase and FIV replication
- Mechanism of action data
- Clarification of whether a veterinary indication falls within the scope of this evaluation
- Product Information warnings and contraindications for Intelence
- If a human-relevant direction is wanted, a focused review of the congenital HIV (perinatal) use of etravirine, including paediatric and neonatal dosing and safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

