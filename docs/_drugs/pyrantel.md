---
layout: default
title: Pyrantel
parent: 僅模型預測 (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Pyrantel
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

# Pyrantel: From Intestinal Nematode Infections to Capillariasis

## One-Sentence Summary

Pyrantel is an anthelmintic historically used against common intestinal nematode infections (ascariasis, enterobiasis, hookworm), acting as a depolarising neuromuscular blocker on worm muscle. Of the 10 new indications flagged by the TxGNN model, most (7/10) have no supporting literature and are judged internally as prediction noise; the one candidate with meaningful supporting evidence is **capillariasis**, backed by **2 randomised controlled trials and several comparative clinical studies** in related intestinal nematode infections, though none testing *Capillaria philippinensis* directly. Overall evidence is indirect (L3) and a blocking safety data gap remains, so this is a research lead rather than a ready-to-use indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intestinal nematode infections (ascariasis, enterobiasis/pinworm, hookworm) — inferred from the evidence pack's own literature and mechanistic notes; not formally recorded in the drug record (`original_indications` is empty) |
| Predicted New Indication | Capillariasis (intestinal *Capillaria philippinensis* infection) |
| TxGNN Prediction Score | 89.08% (rank 9 of 10 by raw score, but highest-quality evidence of the set) |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Note on candidate selection:** The single highest raw TxGNN score (papillary conjunctivitis, 97.99%) has zero supporting trials or literature and is explicitly flagged in the evidence pack as prediction noise unrelated to pyrantel's pharmacology. We report capillariasis instead because it has the strongest evidence base (L3, decision stage S2) among all 10 candidates — see the portfolio table below.

## Why is This Prediction Reasonable?

*Mechanism note: the structured `original_moa` field is flagged as a data gap (DG002). However, the evidence pack's own mechanistic analysis describes pyrantel pamoate as a depolarising neuromuscular blocker that acts as an agonist at nicotinic acetylcholine receptors on nematode muscle, causing spastic paralysis and expulsion of the worm. This is consistent with pyrantel's established pharmacology as an anthelmintic.*

*Capillaria philippinensis*, the causative organism of capillariasis, is an intestinal nematode — the same broad parasite class (soil-transmitted/intestinal nematodes) as *Ascaris lumbricoides*, *Trichuris trichiura* and hookworm, against which pyrantel already has demonstrated clinical activity in multiple human trials. Mechanistically, the same neuromuscular target should be present in *C. philippinensis* adult worms, so the biological rationale for activity is sound.

However, the supporting literature identified for this candidate is entirely **indirect**: the RCTs and comparative studies below evaluate pyrantel against *Ascaris* and *Trichuris* infections, not capillariasis itself. No trial in the evidence pack tests pyrantel against *C. philippinensis* directly, and clinical practice for capillariasis (chronic diarrhoea, protein-losing enteropathy) currently relies on prolonged albendazole or mebendazole courses. The prediction is therefore a plausible research question, not an established efficacy signal.

### Predicted Indication Portfolio (all 10 TxGNN candidates)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------|------|------|------|
| 1 | Papillary conjunctivitis | 97.99% | L5 | S0 | Hold |
| 2 | Toxocariasis | 95.51% | L4 | S1 | Research Question |
| 3 | Toxascariasis | 94.86% | L4 | S0 | Hold |
| 4 | Anisakiasis | 94.79% | L5 | S0 | Hold |
| 5 | Allergic urticaria | 94.54% | L5 | S0 | Hold |
| 6 | Atopic conjunctivitis | 91.37% | L5 | S0 | Hold |
| 7 | Cutaneous larva migrans | 90.41% | L4 | S1 | Research Question |
| 8 | Sorsby's fundus dystrophy | 90.41% | L5 | S0 | Hold |
| 9 | **Capillariasis** | 89.08% | **L3** | **S2** | **Research Question** |
| 10 | Rosacea conjunctivitis | 88.32% | L5 | S0 | Hold |

Only candidates that fall within pyrantel's known anthelmintic mechanism (toxocariasis, cutaneous larva migrans, capillariasis) have any literature support; the remaining seven (mostly ocular/dermatological/allergic conditions with no mechanistic link and zero trials or publications) are held.

## Clinical Trial Evidence

Currently no related clinical trials registered for capillariasis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38563751](https://pubmed.ncbi.nlm.nih.gov/38563751/) | 2024 | RCT | Antimicrobial Agents and Chemotherapy | Assessor-blind RCT in school-aged children comparing albendazole alone vs combined with mebendazole or pyrantel for *Trichuris trichiura* infection |
| [9798586](https://pubmed.ncbi.nlm.nih.gov/9798586/) | 1998 | RCT | Lancet | Randomised trial of albendazole vs pyrantel in symptomless childhood trichuriasis, assessing growth outcomes |
| [657997](https://pubmed.ncbi.nlm.nih.gov/657997/) | 1978 | Comparative Clinical Study | Drugs | Oxantel-pyrantel suspension vs mebendazole in mixed *Ascaris*/*Trichuris* infections; both achieved 100% cure for *Ascaris* |
| [6287829](https://pubmed.ncbi.nlm.nih.gov/6287829/) | 1981 | Comparative Clinical Study | African Journal of Medicine and Medical Sciences | Pyrantel pamoate ~95% cure vs *Ascaris*, superior to piperazine/bephenium; neither regimen effective against *Trichuris* |
| [8893536](https://pubmed.ncbi.nlm.nih.gov/8893536/) | 1996 | Cohort | Parasitology | Single-dose pyrantel pamoate improved appetite and growth in *Ascaris*-infected schoolboys; little effect on concurrent *Trichuris* |
| [6466265](https://pubmed.ncbi.nlm.nih.gov/6466265/) | 1984 | Comparative Clinical Study | Bangladesh Medical Research Council Bulletin | Compared efficacy of pyrantel pamoate, levamisole and mebendazole in hospitalised patients with helminth infections |
| [7305501](https://pubmed.ncbi.nlm.nih.gov/7305501/) | 1981 | Comparative Clinical Study | Annals of Tropical Medicine and Parasitology | Anthelmintic effects of pyrantel, oxantel-pyrantel, levamisole and mebendazole on intestinal nematodes |
| [3895141](https://pubmed.ncbi.nlm.nih.gov/3895141/) | 1985 | Review | Pediatric Clinics of North America | Overview of intestinal nematode infections, including treatment approaches |
| [168337](https://pubmed.ncbi.nlm.nih.gov/168337/) | 1975 | Review | The Journal of Pediatrics | Overview of parasitic infections in children |
| [4809618](https://pubmed.ncbi.nlm.nih.gov/4809618/) | 1974 | Review | Clinical Pediatrics | Early clinical review of Antiminth (pyrantel pamoate) |

None of the above studies evaluate *Capillaria philippinensis* specifically; all evidence is extrapolated from pyrantel's activity against related intestinal nematodes.

## Australia Market Information

Pyrantel currently has no ARTG entries and is not marketed in Australia (0 licenses on record).

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No PI currently exists in this dataset because pyrantel is not marketed in Australia, and the TFDA-equivalent warnings/contraindications and DDI query returned no data (`DG001`, blocking severity). A drug-interaction search also returned no results (`not_found`).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and indirect clinical trial evidence (2 RCTs, several comparative studies) in related intestinal nematode infections make capillariasis a legitimate research question, but there is no direct evidence of efficacy against *Capillaria philippinensis*, and a blocking data gap (missing PI warnings/contraindications, DG001) prevents even an initial safety assessment. Pyrantel is also not currently registered in Australia.

**To proceed, the following is needed:**
- Resolve the blocking safety data gap: obtain TGA/PI warnings and contraindications for pyrantel
- Formal mechanism-of-action documentation (DG002)
- Dedicated efficacy data for pyrantel against *Capillaria philippinensis* specifically, rather than extrapolation from *Ascaris*/*Trichuris* studies
- Drug interaction (DDI) profile, currently unavailable
- Assessment of the ARTG registration pathway if repurposing is to be pursued in the Australian market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

