---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: From Topical Antistaphylococcal Use to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Mupirocin is a topical antibacterial agent whose literature base centres on Staphylococcus aureus skin infection and nasal MRSA decolonisation. Among the 10 disease candidates TxGNN generated, the one with the strongest independent supporting evidence is **Staphylococcal Scalded Skin Syndrome (SSSS)**, backed by **14 publications** (including a comparative cohort study of mupirocin ointment as adjunct therapy) but **no dedicated clinical trials**. TxGNN's single highest-scoring candidate (pleural empyema, 99.5%) was reviewed and found to have no clinical or mechanistic support and a route-of-administration mismatch (mupirocin has no systemic bioavailability), so it is not carried forward as the headline candidate — see rationale below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (no ARTG-listed indication; Mupirocin is not currently registered in Australia). Literature in this pack consistently describes it as a topical antistaphylococcal ointment used for skin infection/decolonisation. |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 95.57% (rank 9 of the candidate set; selected for evidence strength, not raw score — see below) |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (`original_moa`) is not available for Mupirocin in this evidence pack. However, the underlying evidence does contain mechanistic detail: mupirocin inhibits bacterial isoleucyl-tRNA synthetase, blocking protein synthesis in susceptible Gram-positive organisms — most notably *Staphylococcus aureus*. This is consistent with its well-documented role as a topical antistaphylococcal agent, used for conditions such as impetigo and MRSA nasal decolonisation, as reflected repeatedly across the literature retrieved for this pack.

SSSS is caused by exfoliative-toxin-producing strains of *S. aureus*. Since mupirocin's established target is *S. aureus* itself, extending its use to SSSS is a same-pathogen, different-clinical-presentation extension rather than a mechanistically novel leap — several of the retrieved publications directly discuss mupirocin in the context of staphylococcal skin/soft-tissue disease control, and one (PMID 37404367) specifically evaluates 2% mupirocin ointment combined with intravenous antibiotics in paediatric SSSS.

It is worth noting that TxGNN's top-ranked candidate by raw score was pleural empyema (99.5%), followed by several ocular and vaginal conditions. On review, these carry no supporting clinical trials or literature, and in several cases the proposed indication is physiologically incompatible with mupirocin's topical-only route (no systemic bioavailability) or pathophysiologically unrelated to bacterial infection (e.g., neurotrophic keratopathy, vaginal leukoplakia). One candidate ("non-human animal disease") is a non-clinical knowledge-graph artefact. These are therefore not presented as the headline finding; SSSS, despite a lower raw TxGNN score, is the only candidate reaching an evidence level (L3) and decision stage (S2) beyond pure model prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mupirocin in Staphylococcal Scalded Skin Syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Cohort | Clinical, Cosmetic and Investigational Dermatology | Compares treatment duration, cost and outcomes of different IV antibiotics combined with 2% mupirocin ointment in paediatric SSSS — the only study directly evaluating mupirocin as adjunct therapy in this indication. |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Review of Anti-infective Therapy | Reviews treatment of bullous impetigo and SSSS in infants, both caused by staphylococcal exfoliative toxins. |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatologic Clinics | Discusses control of staphylococcal skin disease, naming topical mupirocin as a valuable addition to antistaphylococcal management. |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case Series | Advances in Neonatal Care | Case series on SSSS identification and wound care in neonates with MSSA infection. |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Cohort (outbreak investigation) | Journal of Hospital Infection | Nosocomial SSSS outbreak in 13 neonates; epidemiological and case-control investigation of transmission and control. |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Cohort | The Pediatric Infectious Disease Journal | Molecular epidemiology of *S. aureus* strains (ST121) causing rising SSSS cases in Houston, Texas. |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | Cohort | The Pediatric Infectious Disease Journal | Molecular epidemiology of SSSS in premature infants; describes infection-control strategies to prevent NICU outbreaks. |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Case Report | Journal of Medical Microbiology | Emergence of a mupirocin- and fusidic acid-resistant *S. aureus* clone causing SSSS — relevant to resistance risk when using mupirocin in this population. |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Case Report | Journal of Clinical Microbiology | Emergence of a mupirocin-resistant *S. aureus* clone causing mainly skin infections, over a 43-month surveillance period. |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case Report | Dermatopathology (Basel) | SSSS in an adult on chemotherapy — an atypical adult presentation of a normally paediatric disease. |

*4 additional records (PMIDs 18306677, 35358031, 16218885, 19000857) were retrieved but not yet fully classified by study type; available on request.*

---

## Australia Market Information

Mupirocin has **no ARTG entries** and is **not currently marketed in Australia** according to this evidence pack. No product, dosage form, or approved-indication data is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data for Mupirocin were not available in this evidence pack (a blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety data (warnings, contraindications, DDI) is entirely unavailable, which blocks even an initial (S1) safety assessment.
- Mupirocin is not registered in Australia (0 ARTG entries), so there is no local regulatory or PI baseline to build on.
- The best-supported candidate indication (SSSS) reaches only L3 evidence and a "Research Question" stage — hypothesis-generating observational and case-report data, not confirmatory trial evidence. No candidate in this pack reaches L1/L2.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information — warnings, contraindications, DDI (blocking gap, DG001)
- Formal mechanism-of-action documentation (DG002)
- Prospective comparative or controlled evidence evaluating topical mupirocin specifically as adjunct therapy in SSSS (the existing cohort study, PMID 37404367, is the only direct data point)
- A resistance-risk assessment given documented emergence of mupirocin-resistant *S. aureus* clones in skin infection settings (PMIDs 30418106, 28592549)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

