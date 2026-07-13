---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Cefazolin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cefazolin: From Surgical Infection Prophylaxis to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic widely used in clinical practice for surgical site infection prophylaxis and treatment of susceptible bacterial infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **1 clinical trial** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Surgical prophylaxis and susceptible bacterial infections (no ARTG registration data available) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Australia Market Status | Not registered (0 ARTG entries returned) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Cefazolin is a first-generation cephalosporin that exerts bactericidal activity by inhibiting bacterial cell wall synthesis through irreversible binding to penicillin-binding proteins (PBPs). It demonstrates strong activity against *Staphylococcus aureus* (MSSA), *Streptococcus pyogenes*, and partial activity against *Streptococcus pneumoniae*, with limited coverage of Gram-negative organisms.

Acute infectious otitis media (AOM) is commonly caused by *S. pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Cefazolin's activity against *S. pneumoniae* and *S. aureus* provides partial pathogen coverage, supporting the mechanistic basis for the TxGNN prediction. In scenarios where *S. aureus* is the implicated pathogen — such as otitis media arising as a complication of post-surgical ear infections or furunculosis — Cefazolin's antimicrobial spectrum is well-suited to the clinical need.

The key limitation is that Cefazolin lacks meaningful activity against *H. influenzae* and *M. catarrhalis*, which together account for approximately 40–50% of bacterial AOM in children. This constrains its utility as empiric monotherapy for infectious otitis media and restricts any potential role to pathogen-confirmed or procedure-related contexts. The overall mechanistic fit is therefore rated as moderate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicentre double-blind RCT in children aged 6–23 months comparing 5-day (reduced-duration) versus 10-day (standard-duration) antibiotic therapy for AOM. Trial was terminated prior to completion; reason not specified in available records. Results should be interpreted with caution. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | South Med J | Narrative review of cephalosporin antibiotics in paediatric infections including otitis media; discusses antimicrobial spectrum, safety profile, and clinical utility of first-generation cephalosporins in children |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Series | Ann Otol Rhinol Laryngol | Describes empiric ceftazidime–Cefazolin combination therapy in paediatric Gradenigo Syndrome (petrous apicitis as an AOM complication); illustrates direct clinical application of Cefazolin in an otitis media-related condition |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Series | Clin Pharm | Case report of Stevens-Johnson syndrome in a child receiving sequential antibiotic therapy for otitis media; peripheral relevance to Cefazolin use in the AOM treatment pathway |

---

## Australia Market Information

No ARTG entries for Cefazolin were identified in the TGA database query. Clinicians should verify current registration status directly via the [TGA ARTG public search](https://www.tga.gov.au/resources/artg), as injectable Cefazolin formulations may be registered under different trade names or sponsor listings not captured by this query.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.44%) for infectious otitis media, the supporting clinical evidence base is limited — the sole registered clinical trial was terminated before completion, and available literature consists of older narrative reviews and case reports with only indirect relevance to Cefazolin as a treatment for AOM. The significant antimicrobial spectrum gap against *H. influenzae* and *M. catarrhalis* further constrains Cefazolin's applicability as empiric therapy for standard infectious otitis media.

**To proceed, the following is needed:**
- Investigation of the reason for early termination of NCT01511107 (efficacy failure, safety signal, or operational factors) to determine whether the hypothesis remains viable
- Identification of specific AOM subpopulations where Cefazolin's spectrum aligns with likely pathogens (e.g., confirmed MSSA or *S. pneumoniae* otitis media; post-operative middle ear infections)
- Verification of current TGA/ARTG registration status for Cefazolin products available in Australia
- Retrieval of full TGA Product Information including contraindications, warnings, and drug interactions to complete the safety profile
- **Higher-priority repurposing opportunity:** The Urinary Tract Infection indication (Rank #10, TxGNN score 98.91%, Evidence Level L3, Decision: **Proceed with Guardrails**) presents a substantially stronger repurposing case — 11 registered clinical trials, 20 publications including a completed RCT directly comparing Cefazolin versus ceftriaxone for complicated UTI (PMID [40033251](https://pubmed.ncbi.nlm.nih.gov/40033251/)) and a systematic review supporting first-generation cephalosporins for uncomplicated UTI (PMID [32659466](https://pubmed.ncbi.nlm.nih.gov/32659466/)). A dedicated report for this indication is recommended as the priority next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

