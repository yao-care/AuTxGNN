---
layout: default
title: Tenofovir Disoproxil
parent: Moderate Evidence (L3-L4)
nav_order: 659
evidence_level: L4
indication_count: 10
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tenofovir Disoproxil: From HIV-1 Infection / Chronic Hepatitis B to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor whose established human uses are HIV-1 treatment/PrEP and chronic hepatitis B.
> The TxGNN model's top-ranked prediction, **Simian Immunodeficiency Virus Infection**, is not a human disease — it is an animal-model ontology artefact,
> supported only by **2 low-relevance clinical trials** and **20 macaque-model publications**, none of which demonstrate a genuine new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory register supplied (no ARTG-equivalent license entries). Based on established pharmacology noted elsewhere in this evidence pack, tenofovir disoproxil's approved human uses are HIV-1 infection (treatment and PrEP) and chronic hepatitis B. |
| Predicted New Indication | Simian Immunodeficiency Virus Infection (an animal-model disease, not a human indication) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (marked as a blocking/high-severity data gap in the evidence pack). Based on known pharmacology, tenofovir disoproxil is a nucleotide analogue reverse transcriptase inhibitor that suppresses HIV-1 and hepatitis B virus polymerase — this is well-established, on-label activity, not a new mechanistic hypothesis.

The top-ranked TxGNN prediction, simian immunodeficiency virus (SIV) infection, is a veterinary/laboratory disease node used to model HIV in macaques. It sits immediately adjacent to "HIV infection" in the knowledge graph's disease ontology, so the model surfaces it as a near-identical match — but the evidence pack's own rationale explicitly flags this as prediction noise rather than a translatable human repurposing target. The supporting literature (below) is exclusively pre-clinical macaque/SHIV challenge-protection research, and the two associated clinical trials are human HIV studies with only incidental relevance (one withdrawn with zero enrolment).

For transparency: the two predicted indications in this pack with genuine clinical evidence (L1, hepatitis B virus infection and AIDS related complex — see the evidence pack's full prediction list) are not novel candidates either. Both are already-established uses of tenofovir disoproxil, so the model is essentially rediscovering the drug's own label rather than identifying a new opportunity. The remaining predictions (rare genetic neurodevelopmental disorder, obsolete hyperlipidemia term, prostate fibroma, Brenner tumor, benign reproductive neoplasms) have no clinical trial or literature support and no biologically plausible mechanistic link to an antiviral nucleotide analogue. Taken together, this evidence pack does not currently contain a credible, human-relevant new repurposing signal for tenofovir disoproxil.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab combined with ART for virological remission in HIV-infected subjects (human HIV study; not an SIV trial — graded low relevance) |
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | HIV RNA decay kinetics study referencing comparable SIV-macaque decay data; withdrawn before enrolment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Animal (macaque) | JCI Insight | Hypo-osmolar rectal tenofovir douche prevents SHIV acquisition in macaques |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal (macaque) | J Infect Dis | Oral TAF + emtricitabine protects macaques from rectal SHIV infection |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Animal (macaque) | J Virol | Vaginal 1% tenofovir gel gives durable protection against SHIV in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal (macaque) | J Infect Dis | FTC/TDF prevents vaginal SHIV infection in macaques co-infected with STIs |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal (macaque) | J Acquir Immune Defic Syndr | Oral TDF / topical tenofovir protects infant macaques from oral SIV challenge |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal (macaque) | J Infect Dis | TDF gives partial protection against SHIV in macaques with repeated challenge |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal (macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts give extended postexposure protection against SHIV in macaques |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal (macaque) | Nature Communications | SHIV remission in macaques with early ART initiation and long-acting antivirals |
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Review of systemic PrEP for human HIV infection (human, but tangential to SIV) |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal (macaque) | J Infect Dis | FTC/TDF prevents transmission of tenofovir-resistant (K65R) SHIV in macaques |

---

## Australia Market Information

Currently no ARTG entries are recorded for this drug in the evidence pack (0 licenses; market status: Not marketed).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (simian immunodeficiency virus infection) is an animal-model ontology artefact with no direct human clinical applicability — its own supporting evidence is exclusively pre-clinical macaque research. No indication in this evidence pack represents a genuine, evidence-supported *new* human indication: the two candidates with strong clinical evidence (hepatitis B, AIDS-related complex) are already-established uses of tenofovir disoproxil, and the remaining candidates have no clinical or mechanistic support.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (currently a data gap)
- TFDA/TGA-approved Product Information for safety warnings, contraindications and DDI data (currently blocking data gap)
- Re-run TxGNN candidate generation with animal/veterinary disease ontology nodes filtered out, to avoid noise like SIV/FIV
- If a genuine novel human indication is later identified, complete route-of-administration and similarity-to-original-indication analysis (currently marked "pending" throughout this evidence pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

