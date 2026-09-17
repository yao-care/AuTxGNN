---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic with established use against Gram-positive bacterial infections (per literature evidence in this pack; specific TFDA/TGA-approved indication text is not available). The TxGNN model's top-ranked prediction is **Diffuse Scleroderma**, but this evidence pack itself flags the finding as a likely **false positive** — there is no mechanistic rationale and only a single, unrelated case report. Of the 10 candidate indications screened in this pack, only one (**Streptococcal Pneumonia**, ranked 9th by score) has credible mechanistic and clinical support and is worth further consideration — see the summary table below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (0 ARTG entries; Vancomycin is a glycopeptide antibiotic with established use in Gram-positive infections per literature evidence) |
| Predicted New Indication (Top TxGNN Score) | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Note:** This pack screened 10 TxGNN-predicted indications for Vancomycin. Nine of ten — including the top-scored Diffuse Scleroderma — lack mechanistic plausibility or supporting evidence. See "All Candidates Screened" below for the full picture, including the one candidate (Streptococcal Pneumonia) with genuine clinical support.

---

## All Candidates Screened (This Evidence Pack)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|---|---|---|---|---|---|---|
| 1 | Diffuse Scleroderma | 99.92% | L5 | S0 | Hold | Autoimmune fibrotic disease — no mechanistic link; likely false positive |
| 2 | Paratyphoid Fever | 99.85% | L4 | S0 | Hold | Gram-negative pathogen — vancomycin cannot penetrate outer membrane |
| 3 | Salmonellosis | 99.81% | L4 | S0 | Hold | Gram-negative pathogen — same limitation as above |
| 4 | Congenital Analbuminemia | 99.79% | L5 | S0 | Hold | No mechanistic link; no supporting evidence |
| 5 | Polyclonal Hyperviscosity Syndrome | 99.79% | L5 | S0 | Hold | No mechanistic link; no supporting evidence |
| 6 | Hyperamylasemia | 99.79% | L5 | S0 | Hold | Lab abnormality, not a disease entity; no mechanistic link |
| 7 | Typhoid Fever | 99.75% | L4 | S0 | Hold | Gram-negative pathogen — same limitation as #2/#3 |
| 8 | Blood Group Incompatibility | 99.63% | L5 | S0 | Hold | Immune haemolytic mechanism unrelated to antimicrobial action |
| **9** | **Streptococcal Pneumonia** | 99.60% | **L2** | **S3** | **Proceed with Guardrails** | Mechanistically sound; consistent with existing guideline-supported use in resistant *S. pneumoniae* |
| 10 | Premalignant Haematological Disease | 99.54% | L5 | S0 | Hold | Oncologic entity — no mechanistic link; no evidence |

The remainder of this report addresses the top TxGNN-ranked candidate (Diffuse Scleroderma) as required, followed by a dedicated summary of the clinically credible candidate (Streptococcal Pneumonia).

---

## Why is This Prediction Reasonable? (Diffuse Scleroderma)

Currently, detailed mechanism of action data for Vancomycin is not available in this evidence pack. Based on information within the pack, Vancomycin is a **glycopeptide antibiotic** that inhibits bacterial cell wall (peptidoglycan) synthesis by binding to the D-Ala-D-Ala terminus of cell wall precursors — a mechanism specific to susceptible bacterial pathogens.

Diffuse scleroderma is an **autoimmune fibrotic disease**, not an infectious condition, and has no established pathological connection to bacterial cell wall synthesis inhibition. The only supporting literature is a single case report describing erythroderma with sepsis and eosinophilia — a differential-diagnosis discussion, not a study of vancomycin treating scleroderma.

**Assessment:** This prediction is judged to have a high likelihood of being a false positive from the knowledge-graph model, with no mechanistic rationale and no direct supporting evidence.

---

## Clinical Trial Evidence (Diffuse Scleroderma)

Currently no related clinical trials registered.

---

## Literature Evidence (Diffuse Scleroderma)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a case of diffuse exfoliative erythroderma with sepsis and eosinophilia in a patient with prior streptococcal cellulitis; discusses differential diagnosis of erythroderma. Does not evaluate vancomycin for scleroderma. |

---

## Australia Market Information

No ARTG entries are recorded in this evidence pack (total_licenses = 0; market status = Not marketed). Vancomycin's marketed formulations and approved indications in Australia should be confirmed directly via the TGA ARTG database and current Product Information.

---

## Notable Alternative Candidate: Streptococcal Pneumonia (Rank 9)

Although not the top-scored prediction, this candidate is the only one in the pack with a sound mechanistic basis and meaningful clinical evidence, and warrants separate attention.

**Mechanistic rationale:** Vancomycin inhibits cell wall peptidoglycan synthesis in Gram-positive organisms. *Streptococcus pneumoniae* is a Gram-positive coccus within vancomycin's intrinsic spectrum. Clinically, vancomycin is already guideline-recommended for penicillin-resistant/multidrug-resistant *S. pneumoniae* infections (particularly meningitis) — this is less a novel indication than a reinforcement of existing clinical practice.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05395520](https://clinicaltrials.gov/study/NCT05395520) | N/A | Unknown | 146 | Evaluates whether AUC-based vancomycin monitoring is appropriate beyond serious MRSA infections, relevant to dosing safety in resistant Gram-positive infections |
| [NCT04464291](https://clinicaltrials.gov/study/NCT04464291) | N/A | Completed | 500 | Epidemiological survey of circulating *S. pneumoniae* serotypes in Russia — background/context only |
| [NCT02538211](https://clinicaltrials.gov/study/NCT02538211) | N/A | Completed | 63 | Intestinal microbiome and vaccine immune response — background only, not directly relevant |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10712318](https://pubmed.ncbi.nlm.nih.gov/10712318/) | 2000 | RCT | Am J Respir Crit Care Med | Prospective randomised comparison of quinupristin/dalfopristin vs. vancomycin in gram-positive nosocomial pneumonia (n=298) |
| [36028454](https://pubmed.ncbi.nlm.nih.gov/36028454/) | 2022 | Cohort/Surveillance | Indian J Med Microbiol | Antibiotic resistance rates and penicillin MIC distribution in streptococcal pneumonia, 2013–2019 |
| [10501315](https://pubmed.ncbi.nlm.nih.gov/10501315/) | 1999 | Review | Seminars in Respiratory Infections | Treatment of pneumococcal pneumonia amid rising penicillin/macrolide resistance |
| [16735146](https://pubmed.ncbi.nlm.nih.gov/16735146/) | 2006 | Review | Am J Medicine | Antimicrobial resistance in Gram-positive bacteria, including pneumococcal resistance trends |
| [9404765](https://pubmed.ncbi.nlm.nih.gov/9404765/) | 1997 | Review | Chest | Penicillin dosing for pneumococcal pneumonia; discusses emergence of resistant pneumococci and vancomycin use |
| [27929242](https://pubmed.ncbi.nlm.nih.gov/27929242/) | 2016 | Review (guideline-based) | American Family Physician | Diagnosis and management of community-acquired pneumonia in adults |
| [21661712](https://pubmed.ncbi.nlm.nih.gov/21661712/) | 2011 | Review | American Family Physician | Diagnosis and management of community-acquired pneumonia, including antibiotic selection |
| [35794077](https://pubmed.ncbi.nlm.nih.gov/35794077/) | 2022 | Practice Evaluation | J Perinatal Medicine | Evaluates appropriate vancomycin prescribing per updated ACOG guidelines for penicillin-allergic patients at risk of resistant GBS |

**Evidence Level:** L2 | **Decision Stage:** S3 | **Recommendation:** Proceed with Guardrails

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision (Top-ranked prediction — Diffuse Scleroderma): Hold**

**Rationale:**
The top TxGNN-scored prediction lacks any mechanistic plausibility (an antibacterial agent proposed for an autoimmune fibrotic disease) and is supported only by a single, unrelated case report. Evidence level is L5 (model prediction only), and the evidence pack itself flags this as a probable false positive.

**To proceed (if pursued at all), the following is needed:**
- Preclinical/mechanistic studies establishing any plausible biological link between glycopeptide antibiotics and fibrotic autoimmune disease
- Independent confirmation that this is not a knowledge-graph artefact before any further investment

**Separately — Streptococcal Pneumonia (Rank 9): Proceed with Guardrails**

**Rationale:**
This is mechanistically sound and consistent with existing clinical guidance for vancomycin use in resistant *S. pneumoniae* infections, supported by L2 evidence including a randomised comparative trial.

**To proceed, the following is needed:**
- Confirmation this reflects extension/reinforcement of an existing indication rather than a genuinely novel use
- Vancomycin MOA and TFDA/TGA-approved indication text (currently data gaps — DG001, DG002 in this pack)
- Formal safety review (PI-based) before any guardrail protocol is finalised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

