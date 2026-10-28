---
layout: default
title: Efavirenz
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Efavirenz: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "efavirenz"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Efavirenz
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Efavirenz: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Efavirenz is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition.
Support is thin: **0 clinical trials** and **1 in vitro publication**, so this prediction rests mainly on model output.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Efavirenz inhibits HIV-1 reverse transcriptase (RT). Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, efavirenz is an NNRTI with proven efficacy in HIV infection and AIDS, and it may mechanistically be applicable to related lentiviruses.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV and causes an AIDS-like syndrome in cats. A 2023 biochemical and structural study compared NNRTIs, including efavirenz, against FIV and HIV reverse transcriptases. However, the available data do not show efavirenz activity against FIV RT. NNRTIs are generally expected to have weak activity against FIV RT because the NNRTI binding pocket differs between the two viruses. This is an inference from the general NNRTI class and should be checked against the full paper.

The evidence is in vitro biochemical/structural only, with no animal efficacy data and no clinical trials. Feline AIDS is a veterinary indication, so its relevance to human drug repurposing is limited.

Two other predictions were also reviewed:
- **Simian immunodeficiency virus infection (score 0.9980, L4, Hold):** Wild-type SIV is intrinsically resistant to NNRTIs. Efavirenz-containing regimens suppress RT-SHIV (an SIV carrying HIV-1 RT) in macaques, but this validates the known anti-HIV-1 mechanism in an animal model. It adds no new human indication, since SIV infection is not a human disease.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (score 0.9977, L5, Hold):** There is no clinical trial, no literature and no established mechanistic link. Efavirenz's effect on CYP46A1 is speculative here and not supported by the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | Journal of Veterinary Science | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus RTs to assess NNRTI potential for FIV infection. No effective treatment currently exists for infected cats. The available abstract does not report efavirenz activity. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11732L | Tenofovir Disoproxil Emtricitabine Efavirenz Viatris 300/200/600 | Tablet (tenofovir disoproxil maleate 300 mg, emtricitabine 200 mg, efavirenz 600 mg) | Not listed in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, Fanconi renotubular syndrome, lactic acidosis, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, delusional disorder, paranoid schizophrenia, chronic hepatitis B and C virus infection, hypertriglyceridemia, obesity, hypophosphatemia, osteomalacia, rickets and gallbladder disease.
- **Drug Interactions:** 330 interactions were identified. Examples include the **major** interaction with dolasetron, and **moderate** interactions with clarithromycin, bupropion, aprepitant, pioglitazone, saxagliptin, loperamide, dexamethasone, hydrocortisone, betamethasone, triamcinolone, famotidine, rabeprazole, acarbose, dronabinol and minocycline.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for the lead prediction is a single in vitro study of a veterinary condition that does not show efavirenz activity, and there are no clinical trials. The high TxGNN score alone does not justify progression. The SIV prediction reflects a chimeric animal model, and the neurodevelopmental prediction has no supporting data.

**To proceed, the following is needed:**
- Full-text review of PMID 38031646 to confirm whether efavirenz inhibits FIV RT
- Animal efficacy data in FIV-infected cats, if the veterinary indication is pursued
- Detailed mechanism of action data
- Label warnings and contraindications from the TGA Product Information
- Confirmation of the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

