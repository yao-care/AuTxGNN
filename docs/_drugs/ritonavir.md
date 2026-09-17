---
layout: default
title: Ritonavir
parent: Moderate Evidence (L3-L4)
nav_order: 600
evidence_level: L3
indication_count: 10
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Ritonavir: From HIV Infection to Hepatitis B Virus Infection

> **Note on candidate selection**: This Evidence Pack contains 10 TxGNN-predicted indications for Ritonavir. The top 3 ranked candidates (simian immunodeficiency virus infection, feline acquired immunodeficiency syndrome, a rare paediatric neurodevelopmental disorder) are explicitly flagged in the pack's own `repurposing_rationale` as non-human disease models or knowledge-graph false positives with no clinical relevance. This report therefore focuses on **Hepatitis B virus infection** (rank 4), the highest-ranked candidate with a genuine, traceable mechanistic and clinical trial story.

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor that, in modern practice, is used almost exclusively as a low-dose pharmacokinetic booster (CYP3A4 inhibitor) within combination antiviral regimens rather than as a standalone antiviral. The TxGNN model predicts a possible link to **Hepatitis B virus infection**, with **50 clinical trials** and **16 publications** identified — though most of these trials actually studied hepatitis C or hepatitis D regimens, so the genuinely HBV-relevant evidence is a smaller, indirect subset (via ritonavir's booster role in hepatitis-delta and HBV capsid-modulator combinations).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (as a pharmacokinetic booster within combination antiretroviral therapy) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently not available for this candidate (data gap DG002). Based on known information, ritonavir is a component of standard combination antiretroviral therapy for HIV, and its dominant modern clinical role is as a potent CYP3A4 inhibitor used to "boost" the plasma concentration of co-administered antiviral drugs, rather than as a primary antiviral agent itself.

This booster property is mechanistically what links ritonavir to hepatitis B: ritonavir is combined with lonafarnib in the treatment of chronic hepatitis delta virus (HDV) infection — a disease that only occurs in patients already infected with HBV — and it is also combined with the investigational HBV capsid-assembly modulator GLS4 to raise its plasma exposure. In both cases ritonavir has no direct anti-HBV activity of its own; it works purely as a pharmacoenhancer for other agents that do.

Because of this indirect relationship, most of the clinical trials matched to "hepatitis B virus infection" in this Evidence Pack are, on inspection, hepatitis C direct-acting antiviral (DAA) studies (e.g. ombitasvir/paritaprevir/ritonavir/dasabuvir) that share drug names but not disease relevance. The genuinely informative evidence is a smaller set of HDV- and GLS4-specific studies, summarised below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03719313](https://clinicaltrials.gov/study/NCT03719313) | Phase 3 | Completed | 407 | D-LIVR: lonafarnib/ritonavir ± peginterferon alfa-2a vs peginterferon alone in chronic hepatitis delta (HBV+ patients maintained on nucleos(t)ide therapy) |
| [NCT03600714](https://clinicaltrials.gov/study/NCT03600714) | Phase 2 | Completed | 26 | Lonafarnib + ritonavir + lambda interferon for chronic delta hepatitis; ritonavir used to boost lonafarnib exposure |
| [NCT02511431](https://clinicaltrials.gov/study/NCT02511431) | Phase 2 | Completed | 22 | Lonafarnib and ritonavir combination for chronic hepatitis D safety/efficacy |
| [NCT05229991](https://clinicaltrials.gov/study/NCT05229991) | Phase 3 | Unknown | 30 | Once-daily lonafarnib 50mg + ritonavir 200mg over 48 weeks for chronic HDV infection |
| [NCT03638076](https://clinicaltrials.gov/study/NCT03638076) | Phase 2 | Completed | 20 | Morphothiadine mesilate (GLS4) capsules/ritonavir tablets in patients with chronic hepatitis B — safety, antiviral activity, PK |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Drug-drug interaction study of GLS4/ritonavir with entecavir or tenofovir disoproxil fumarate in healthy subjects |
| [NCT04551261](https://clinicaltrials.gov/study/NCT04551261) | Phase 1 | Completed | 28 | Pharmacokinetics of GLS4 combined with ritonavir or TAF, alone or in combination, in healthy subjects |
| [NCT06338826](https://clinicaltrials.gov/study/NCT06338826) | Phase 2 | Not yet recruiting | 140 | Antiviral treatment relief strategies in HIV-1/HBV coinfected patients, safety endpoint based on HBV virological control |
| [NCT02968641](https://clinicaltrials.gov/study/NCT02968641) | Phase 2b | Withdrawn | 0 | Lonafarnib with/without ritonavir for chronic HDV infection (LOWR-5) — withdrawn, no data generated |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39663120](https://pubmed.ncbi.nlm.nih.gov/39663120/) | 2025 | Review | Gut | Reviews antiviral therapy for chronic hepatitis delta, including lonafarnib/ritonavir regimens in HBV-coinfected patients |
| [37943548](https://pubmed.ncbi.nlm.nih.gov/37943548/) | 2023 | Review | JAMA | Overview of hepatitis D, which occurs only with concurrent HBV infection; context for ritonavir-boosted regimens |
| [26327754](https://pubmed.ncbi.nlm.nih.gov/26327754/) | 2015 | Review | World J Gastroenterol | Management of hepatitis delta and unmet need for novel therapeutic options |
| [32649736](https://pubmed.ncbi.nlm.nih.gov/32649736/) | 2021 | Clinical study | Clin Infect Dis | Antiviral activity and PK of HBV capsid modulator GLS4 in chronic HBV patients |
| [31636065](https://pubmed.ncbi.nlm.nih.gov/31636065/) | 2019 | First-in-human trial | Antimicrob Agents Chemother | GLS4 single/multiple-ascending-dose study with and without ritonavir boosting in healthy volunteers |
| [41480806](https://pubmed.ncbi.nlm.nih.gov/41480806/) | 2026 | Mechanistic study | J Med Virol | GLS4 activates interferon signalling during HBV infection |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | J Viral Hepat | Low incidence of HBV reactivation during direct-acting antiviral therapy |
| [18952618](https://pubmed.ncbi.nlm.nih.gov/18952618/) | 2009 | Cohort | J Antimicrob Chemother | Hepatic safety of tipranavir/ritonavir-based ART; effect of hepatitis virus coinfection and pre-existing fibrosis |
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | RCT (HCV, not HBV) | Lancet Gastroenterol Hepatol | GARNET trial of ombitasvir/paritaprevir/ritonavir + dasabuvir — hepatitis C, included for context only |
| [10632283](https://pubmed.ncbi.nlm.nih.gov/10632283/) | 2000 | Cohort | JAMA | Hepatotoxicity with protease-inhibitor-based ART, and the role of hepatitis B/C coinfection |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-interaction data were available in this Evidence Pack (data gap DG001, classified as **Blocking** severity — this must be resolved before any safety pre-assessment can proceed).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link to hepatitis B is real but indirect — ritonavir acts only as a pharmacokinetic booster for other HBV/HDV-targeted agents (lonafarnib, GLS4), not as a direct anti-HBV drug itself. The genuinely relevant trials are early-phase (mostly Phase 1–2, one Phase 3 in hepatitis delta specifically, not HBV monoinfection), and the majority of trials returned by the search were hepatitis C studies that share drug names but not disease relevance.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information — warnings, contraindications and precautions (blocking data gap, DG001)
- Verified mechanism of action documentation from DrugBank (DG002)
- Disambiguation of trial scope — confirm which studies target HBV monoinfection versus HDV coinfection versus HCV
- Efficacy data specific to chronic HBV (as opposed to hepatitis delta, where the booster role is already established)
- Confirmation of Australian ARTG registration status, since this drug currently shows no market presence in the data reviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

