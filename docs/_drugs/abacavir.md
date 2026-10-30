---
layout: default
title: Abacavir
parent: Model Prediction Only (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Abacavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Abacavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Abacavir
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

## Abacavir: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but the support is limited to **0 clinical trials** and **1 in vitro susceptibility review** (2004).
This is an animal-virus model rather than a true human repurposing opportunity, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the ARTG entry has no approved indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) with proven activity against HIV-1. Simian immunodeficiency virus (SIV) is a closely related lentivirus with a similar reverse transcriptase, so activity is biologically plausible.

The only supporting evidence is a 2004 in vitro review of the susceptibility of HIV-2, SIV and SHIV to anti-HIV-1 compounds. SIV infection occurs in non-human primates and has no human clinical use case. It is therefore not a true repurposing indication for patients.

For context, the model's other predictions with some evidence are mostly extensions of the existing HIV indication. These include congenital HIV (a Phase 3 trial of antiretroviral strategies in infants, with abacavir's role to be verified) and AIDS related complex (an early symptomatic stage of HIV disease). They are not novel repurposing targets. The prediction for a rare neurodevelopmental disorder comes from the TxGNN model (deep learning) alone and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for simian immunodeficiency virus infection.

For reference, trials linked to the related HIV-spectrum predictions are:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Compared antiretroviral courses of different lengths in infants infected with HIV at birth. Abacavir's role needs verification. |
| [NCT00002364](https://clinicaltrials.gov/study/NCT00002364) | Phase 2 | Completed | 40 | Exploratory study of abacavir (1592U89) activity combined with other NRTIs in NRTI-experienced patients. |
| [NCT04340388](https://clinicaltrials.gov/study/NCT04340388) | Phase 4 | Completed | 10 | Dolutegravir and obesity/cardiovascular outcomes. It does not address abacavir efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro review | Antiviral Therapy | Activity of 16 approved antiretrovirals and one experimental drug against HIV-2, SIV and SHIV strains. |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Animal study | Antiviral Research | Zidovudine, lamivudine and abacavir combination suppressed feline immunodeficiency virus replication in vitro. This is a veterinary setting, and abacavir's effect cannot be separated from the combination. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10294T | Ziagen | Tablet 300 mg (as sulfate) | Not listed in the data compiled for this report |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, lactic acidosis, neutropenia, agranulocytosis, anaemia, hypertriglyceridaemia, obesity disorders, and muscle disorders (myopathy, myositis, dermatomyositis, familial periodic paralysis).
- **Drug interactions:** 93 interactions were identified. Moderate-level interactions include naltrexone and orlistat. Many others (for example metformin, morphine, omeprazole, pantoprazole, prednisone and vancomycin) have no severity grade assigned.
- **Related literature signals:** HLA-B*57:01-associated hypersensitivity, cardiovascular and heart failure risk signals in HIV cohorts, adverse pregnancy outcomes, and a paediatric myositis case report.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications, as label data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single 2004 in vitro review in an animal virus model, with no trials and no human use case. It is not a meaningful repurposing opportunity. The model's more credible HIV-related predictions (congenital HIV, AIDS related complex) are extensions of the existing indication rather than new uses.

**To proceed, the following is needed:**
- Confirmation of whether any human-relevant indication warrants pursuit (for example, safety and dosing in pregnancy and paediatrics for congenital HIV, with HLA-B*57:01 screening)
- Mechanism of action data (MOA)
- TGA Product Information warnings and contraindications, and ARTG approved indication text
- Verification of abacavir's role in NCT00102960
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

