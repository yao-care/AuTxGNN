---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Minocycline
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

# Minocycline: From Antibacterial Therapy to Otitis Externa

## One-Sentence Summary

Minocycline is a broad-spectrum tetracycline-class antibiotic; this evidence pack does not contain confirmed Australian registration or original-indication records (data gap). TxGNN's knowledge graph model returned **10 candidate indications** for Minocycline; the most actionable is **Otitis Externa**, which extends its existing antibacterial spectrum and is supported by **5 publications** (no dedicated clinical trials). Several other high-scoring candidates have zero supporting evidence, and one — postinfectious vasculitis — likely reflects a known adverse-effect signal rather than a genuine therapeutic opportunity (see Safety Considerations).

> **Note on indication selection**: Of the 10 TxGNN-predicted indications in this evidence pack, the top-ranked candidate by score alone (punctate epithelial keratoconjunctivitis, 99.63%) has zero supporting trials or literature (Evidence Level L5, Hold). This report instead headlines **Otitis Externa**, the candidate with the strongest and most clinically coherent evidence base. The full candidate list is provided below for transparency.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap). Minocycline is internationally established as a broad-spectrum tetracycline antibiotic for bacterial infections. |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 98.70% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed / not registered |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Minocycline is not available in this evidence pack (data gap, DG002). Based on known tetracycline-class pharmacology, Minocycline inhibits bacterial protein synthesis and has documented activity against Gram-positive organisms including methicillin-resistant *Staphylococcus aureus* (MRSA), alongside anti-matrix-metalloproteinase (MMP) and anti-inflammatory properties referenced across several of the model's rationale notes.

Otitis externa is predominantly a bacterial or polymicrobial infection of the external ear canal, commonly involving *Staphylococcus aureus* (including MRSA strains) and *Pseudomonas* species. Because this falls within Minocycline's known antimicrobial spectrum, this is not a novel pharmacological hypothesis but rather an extension of an already-established mechanism of action — supported by a 1972 report of minocycline dry syrup used for otorhinolaryngological infections and later bacteriology/resistance studies of discharging ears in Taiwan.

By contrast, most of the other 9 candidates (ophthalmic, sinus, and neoplastic indications) rest on theoretical MMP-inhibition or anti-inflammatory reasoning with no corroborating trials or publications, placing them at a substantially lower confidence tier than otitis externa.

## Clinical Trial Evidence

Currently no related clinical trials registered for Otitis Externa.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12542200](https://pubmed.ncbi.nlm.nih.gov/12542200/) | 2002 | Cohort | Acta Oto-Laryngologica | Documents community-acquired MRSA as an emerging pathogen in discharging ears, relevant to antibacterial coverage needs. |
| [12437801](https://pubmed.ncbi.nlm.nih.gov/12437801/) | 2002 | Cohort | The Journal of Laryngology and Otology | Bacteriological survey of 161 otorrhoea patients in Taiwan; *S. aureus* was the leading isolate (43.5%). |
| [34009720](https://pubmed.ncbi.nlm.nih.gov/34009720/) | 2021 | Cohort/Epidemiology | Veterinary Dermatology | Antimicrobial resistance patterns in *Staphylococcus pseudintermedius*, supporting stewardship considerations relevant to tetracycline use. |
| [4405139](https://pubmed.ncbi.nlm.nih.gov/4405139/) | 1972 | Cohort/Case series | The Japanese Journal of Antibiotics | Early clinical use of minocycline dry syrup for otorhinolaryngological infections. |
| [37026784](https://pubmed.ncbi.nlm.nih.gov/37026784/) | 2023 | In vitro/Basic science | Otology & Neurotology | Tetracyclines show lower cytotoxicity to tympanic membrane fibroblasts than quinolones — relevant to local tolerability if used intra-aurally. |

## Other Predicted Indications Considered

For transparency, all 10 TxGNN candidates from this evidence pack are summarised below:

| Rank | Disease | Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|-------|-----------------|-----------------|-----------------|------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.63% | L5 | S0 | Hold | No trials/literature; theoretical MMP-inhibition link only |
| 2 | Exposure keratitis | 99.20% | L5 | S0 | Hold | No trials/literature |
| 3 | Neurotrophic keratopathy | 98.98% | L5 | S0 | Hold | No trials/literature |
| 4 | Postinfectious vasculitis | 98.76% | L5 | S0 | Hold | **Safety signal, not efficacy signal** — Minocycline is a known cause of ANCA-associated vasculitis; the score likely reflects a drug-causes-disease association, not a treatment relationship |
| 5 | Post-bacterial disorder | 98.74% | L3 | S1 | Research Question | 16 trials retrieved, mostly unrelated to this diffuse label (rosacea, periodontitis, TB, stroke); needs a specific target indication before further evaluation |
| 6 | **Otitis externa** | 98.70% | L3 | S2 | **Proceed with Guardrails** | See main report above |
| 7 | Post-infectious syndrome | 98.68% | L2 | S1 | Research Question | Includes an ongoing Phase 3 platform trial (NCT07280572, RECLAIM, Long COVID) with a minocycline arm, and a terminated Phase 1/2 HIV-cognitive-impairment trial (NCT00855062) |
| 8 | Chronic ethmoidal sinusitis | 98.67% | L5 | S0 | Hold | No trials/literature |
| 9 | Chronic rhinosinusitis | 98.63% | L4 | S0 | Hold | Only 1 background (non-treatment) publication |
| 10 | Paranasal sinus neoplasm | 98.61% | L5 | S0 | Hold | No trials/literature; theoretical antitumour rationale only |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — key warnings, contraindications, and drug interaction data are not available in this evidence pack (data gap, DG001).

**Flagged safety signal**: Minocycline is a well-documented cause of drug-induced ANCA-associated vasculitis. The "postinfectious vasculitis" prediction (rank 4, above) most likely reflects this known adverse association in the knowledge graph rather than a therapeutic opportunity, and should not be pursued as a repurposing candidate without explicit safety review.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Otitis Externa specifically; all other 9 candidates remain Hold or Research Question)

**Rationale:**
Otitis externa is the only candidate where the predicted mechanism aligns with Minocycline's well-established antibacterial spectrum and is supported by real-world bacteriology and historical clinical-use literature, even though no dedicated clinical trial exists. All other candidates either lack any supporting evidence (L4–L5) or, in the case of postinfectious vasculitis, run counter to a known safety signal.

**To proceed, the following is needed:**
- TGA-approved Product Information (key warnings, contraindications, drug interactions) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank
- Australian ARTG registration status confirmation (currently shows 0 entries / not marketed)
- A dedicated clinical or in vitro efficacy study of Minocycline specifically for otitis externa (current literature is bacteriological/epidemiological background, not treatment-outcome data)
- Clarification of the "post-bacterial disorder" and "post-infectious syndrome" labels into specific target conditions before further evaluation
- Explicit exclusion review confirming postinfectious vasculitis is not advanced as a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

