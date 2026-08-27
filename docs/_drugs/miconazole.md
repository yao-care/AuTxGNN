---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Miconazole
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

# Miconazole: From Superficial Fungal Infections to Acne

## One-Sentence Summary

Miconazole is a long-established imidazole antifungal, historically used to treat superficial fungal infections such as dermatophytosis and candidiasis. The TxGNN model predicts it may also be effective for **acne (disease)**, but this direction is currently supported by only **1 clinical trial (unrelated drug combination, suspended)** and **4 publications**, none of which directly test miconazole against acne.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial fungal infections (dermatophytosis, candidiasis) — a well-established antifungal use noted in the supporting literature; no ARTG-registered indication text is available because the drug is not currently marketed |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% (rank 5637 among all predictions) |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for miconazole is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, miconazole is a member of the imidazole antifungal class, and its established efficacy in superficial fungal infections comes from inhibiting fungal cytochrome P450 14α-demethylase (lanosterol demethylase), which blocks ergosterol synthesis in the fungal cell membrane.

The proposed link to acne is indirect rather than mechanistically direct. Acne lesions can be complicated by *Malassezia* (*Pityrosporum*) folliculitis, a fungal condition that is frequently misdiagnosed as acne vulgaris, and in vitro data show azole antifungals have activity against *Propionibacterium* (*Cutibacterium*) *acnes*. This means the TxGNN association is likely picking up an "antimicrobial/antifungal" signal rather than hitting the classic acne pathophysiology pathways (sebaceous gland activity, androgen signalling, inflammatory cascades).

Given this, the prediction is biologically plausible as a research hypothesis — particularly for acne-mimicking fungal folliculitis — but it should not be read as evidence that miconazole treats acne vulgaris itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1% topical combination (not miconazole) in patients with contaminated dermatosis/"acne"; trial was suspended and does not test miconazole directly (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Reviews miconazole's broader effects on skin disorders beyond classic antifungal indications |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series (Pityrosporum folliculitis) | Clinical and Experimental Dermatology | 62 patients with *Pityrosporum* folliculitis — a condition frequently misdiagnosed as acne vulgaris — evaluated for antifungal treatment response |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biological & Pharmaceutical Bulletin | Azole antifungal agents, including miconazole's class, show in vitro activity against *Propionibacterium acnes* isolated from acne vulgaris patients |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohort/split-face study | Skin Research and Technology | Split-face study of catamenial (menstrual-related) acne; abstract does not mention miconazole specifically and its relevance to this drug is unclear |

---

## Australia Market Information

Miconazole currently has no ARTG entries on record and is not marketed in Australia per this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: the underlying evidence pack flags TFDA label warnings/contraindications as a **Blocking** data gap — this must be resolved before any formal safety (S1) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 (mechanistic/preclinical only), the single associated clinical trial does not test miconazole and was suspended, and the supporting literature links to acne only indirectly (via fungal folliculitis mimicking acne, and in vitro anti-*P. acnes* activity) rather than to acne vulgaris itself. This is a research hypothesis, not a substantiated repurposing candidate.

**To proceed, the following is needed:**
- TFDA/TGA product information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action documentation from DrugBank
- A dedicated literature/trial search distinguishing acne vulgaris from fungal folliculitis mimics, to clarify which population (if any) miconazole could plausibly benefit
- Route-of-administration and formulation compatibility data (currently unassessed/"pending")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

