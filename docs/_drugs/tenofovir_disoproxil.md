---
layout: default
title: Tenofovir Disoproxil
parent: Model Prediction Only (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Tenofovir Disoproxil
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

# Tenofovir disoproxil: From Chronic Hepatitis B and HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is an oral antiviral originally used for chronic hepatitis B virus infection and HIV infection (including AIDS).
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, which is a primate counterpart of HIV rather than a new human disease.
Support is limited to **0 registered clinical trials** and **animal-model and review publications** (mostly macaque studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infection; AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical studies only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tenofovir is known to be a nucleotide reverse transcriptase inhibitor. Its efficacy in HIV and hepatitis B is established, and mechanistically it may be applicable to SIV.

SIV is the primate lentivirus counterpart of HIV-1 and also relies on reverse transcriptase. A nucleotide reverse transcriptase inhibitor is therefore expected to inhibit SIV replication. The retrieved literature is consistent with this. It consists mainly of macaque studies of pre-exposure prophylaxis (PrEP), prophylaxis in infant macaques, and antiretroviral therapy.

**Important caveat:** SIV infection in macaques is an animal model of an already-approved human indication (HIV). The evidence supports mechanism and dosing but is not a distinct human indication. The model's other high-scoring predictions are also not new human opportunities:
- Hepatitis B virus infection is already an approved indication.
- AIDS related complex is a historical term overlapping with the approved HIV indication.
- Feline AIDS is a veterinary indication.
- Several rare tumour and genetic disorder predictions have no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for SIV infection. No ANZCTR identifiers were found.

---

## Literature Evidence

All studies below are preclinical (animal) work, reviews, or one human pharmacokinetic trial. None is a human efficacy RCT for this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal study | J Infect Dis | Weekly tenofovir disoproxil fumarate (TDF) gave partial protection against repeated rectal SHIV challenges in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study | J Infect Dis | Emtricitabine/TDF prevented vaginal SHIV infection in macaques coinfected with Chlamydia and Trichomonas |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study | J Infect Dis | Emtricitabine/TDF PrEP was tested against a tenofovir-resistant SHIV (K65R mutation) in macaques |
| [24043812](https://pubmed.ncbi.nlm.nih.gov/24043812/) | 2013 | Animal study | PNAS | A TDF-eluting intravaginal ring protected macaques from multiple vaginal SHIV challenges |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal study | J Acquir Immune Defic Syndr | Oral TDF and topical tenofovir GS-7340 were evaluated against repeated oral SIV challenges in infant macaques |
| [12404171](https://pubmed.ncbi.nlm.nih.gov/12404171/) | 2002 | Animal study | J Infect Dis | Low-dose topical (oral) TDF was tested for protecting infant macaques from repeated low-dose oral SIV exposure |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study | AIDS Res Hum Retroviruses | Combining a virus-like particle HIV vaccine with partially protective oral PrEP prevented SHIV infection in macaques |
| [22964889](https://pubmed.ncbi.nlm.nih.gov/22964889/) | 2012 | Review | Curr Opin HIV AIDS | Reviews lessons from animal models of antiretroviral PrEP and next steps in preclinical research |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Review | Clin Microbiol Rev | Reviews acyclic nucleoside phosphonates (cidofovir, adefovir, tenofovir) against DNA virus and retrovirus infections |
| [21896911](https://pubmed.ncbi.nlm.nih.gov/21896911/) | 2011 | Human PK trial | Antimicrob Agents Chemother | Single-dose TDF and TDF-emtricitabine pharmacokinetics and safety in HIV-infected pregnant women and their infants |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10310P | Tenofovir Sandoz | Tablet containing tenofovir disoproxil fumarate 300 mg (oral) | Indication text not specified in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals (not label text):** The TxGNN knowledge graph links tenofovir disoproxil to the following conditions. These are model-derived associations and should be verified against the approved label.
  - Renal and hepatic: kidney disease, liver disease, liver failure, fatty liver disease and non-alcoholic steatohepatitis, lactic acidosis, Fanconi renotubular syndrome.
  - Bone and metabolic: hypophosphatemia, osteomalacia, rickets, hypertriglyceridemia, obesity disorder.
  - Cardiac and neuropsychiatric: long QT syndrome and torsades de pointes, epilepsy, anxiety and related disorders, delusional disorder, paranoid schizophrenia.
  - Other: gallbladder disease, hepatitis C virus infection.
- **Drug Interactions:** No interaction records were found in the data compiled.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings, contraindications and interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is preclinical only (L4). There are no registered clinical trials for SIV infection, and the indication is an animal model of the already-approved HIV indication, not a distinct human indication.
- The model score is very high (99.95%), but it does not translate into a new clinical opportunity.

**To proceed, the following is needed:**
- Confirmation of whether any human indication is being pursued. For SIV, the practical value is as a preclinical model to support dosing and prophylaxis research, not a new patient indication.
- Detailed mechanism of action data (MOA).
- The approved indication text and safety information (warnings, contraindications) from the TGA Product Information for ARTG 10310P.
- Review of the model's human-relevant predictions separately. Hepatitis B is already approved, and a Phase 3 RCT (NCT01745822, perinatal HBV transmission) supports that use. Any such review should include monitoring of renal function and bone density.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

