---
layout: default
title: Pyrantel
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pyrantel: predicted new indication Toxocariasis (the highest-scoring prediction… (evidence level L5). Approved use: Enterobiasis, ascaridiasis"
---

# Pyrantel
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

# Pyrantel: From Enterobiasis and Ascaridiasis to Toxocariasis

## One-Sentence Summary

Pyrantel is an anthelmintic originally used to treat enterobiasis (pinworm) and ascaridiasis (roundworm).
The TxGNN model predicts it may be effective for **toxocariasis** (score 95.5%), but **no clinical trials** and no human studies are available.
The 20 publications retrieved are almost entirely veterinary or laboratory studies, so the evidence is **model prediction plus indirect animal data**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Enterobiasis, ascaridiasis (from the TxGNN knowledge graph; no approved indication text is recorded for the Australian listing) |
| Predicted New Indication | Toxocariasis (the highest-scoring prediction, papillary conjunctivitis, has no mechanistic support, so toxocariasis is the most credible candidate and is reported here) |
| TxGNN Prediction Score | 95.5% (papillary conjunctivitis, the top-ranked prediction: 98.0%) |
| Evidence Level | L4 (toxocariasis); L5 for papillary conjunctivitis |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (as a research question only) |

**Note:** The top-ranked TxGNN prediction by score is papillary conjunctivitis (98.0%). It has no clinical, literature or mechanistic support and is likely a graph artefact. This report therefore focuses on toxocariasis (rank 2), which has a plausible mechanism and some indirect evidence.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pyrantel is generally understood to be a nicotinic acetylcholine receptor agonist that acts as a depolarising neuromuscular blocker in nematodes, causing spastic paralysis so the worms are expelled from the gut.

Its established uses, enterobiasis and ascaridiasis, involve intestinal roundworms. *Toxocara* species (*T. canis*, *T. cati*) are also ascarid nematodes, so the mechanism is biologically plausible. Veterinary studies show pyrantel-containing products clear adult intestinal *Toxocara* in dogs and cats.

There is an important limitation. Human toxocariasis is mainly visceral or ocular larva migrans, caused by larvae migrating through tissues. Pyrantel is poorly absorbed from the gut and is unlikely to reach these larvae. The veterinary data therefore speak to adult intestinal worms, not the human disease. No human trials were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 20 publications retrieved for toxocariasis, none is a human clinical study of pyrantel in toxocariasis. A selection of the most relevant is shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [955553](https://pubmed.ncbi.nlm.nih.gov/955553/) | 1976 | Review | Fortschritte der Medizin | Overview of worm diseases; pyrantel noted as a useful drug for ascaridiasis and enterobiasis |
| [2048286](https://pubmed.ncbi.nlm.nih.gov/2048286/) | 1991 | Veterinary efficacy study (cats) | Vet Res Commun | Pyrantel pamoate 20 mg/kg tested against *Toxocara cati* and hookworm in cats (paste vs granule) |
| [2368952](https://pubmed.ncbi.nlm.nih.gov/2368952/) | 1990 | Veterinary controlled trial (cats) | Am J Vet Res | Paste formulation reduced *T. cati* egg counts by 96.4% |
| [1057855](https://pubmed.ncbi.nlm.nih.gov/1057855/) | 1975 | Veterinary evaluation (dogs) | Am J Vet Res | About 96% efficacy against *Toxocara* and 93% against *Toxascaris* in dogs |
| [1763481](https://pubmed.ncbi.nlm.nih.gov/1763481/) | 1991 | Veterinary study (dogs) | Vet Parasitol | Beef-based chewable pyrantel tested against *T. canis* and other ascarids and hookworms in dogs |
| [1586021](https://pubmed.ncbi.nlm.nih.gov/1586021/) | 1992 | Veterinary study (combination) | Am J Vet Res | Ivermectin plus pyrantel chewable effective against heartworm, hookworm and ascarids in dogs |
| [10384907](https://pubmed.ncbi.nlm.nih.gov/10384907/) | 1999 | Veterinary efficacy study (greyhounds) | Vet Parasitol | Fenbendazole and pyrantel pamoate compared against *T. canis* in contaminated runs |
| [12684883](https://pubmed.ncbi.nlm.nih.gov/12684883/) | 2003 | In vitro study | Parasitol Res | Pyrantel plus fenbendazole acted synergistically on adult *T. canis* (morphological damage) |
| [40836259](https://pubmed.ncbi.nlm.nih.gov/40836259/) | 2025 | Veterinary study (combination) | Parasit Vectors | Four-drug chewable containing pyrantel effective against *T. canis* and *T. leonina* in dogs; efficacy cannot be attributed to pyrantel alone |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 3047J | Anthel 125 | Tablet 125 mg (as embonate), oral | Not recorded in the data compiled for this report |

## Cytotoxicity

Not applicable. Pyrantel is not an antineoplastic drug.

## Safety Considerations

- **Knowledge-graph contraindication signals:** liver disease and gallbladder disease (derived from drug-disease graph edges, not from label text; verify against the Product Information).
- **Drug Interactions (2 moderate, from DDInter):**
  - Iodide I-131 (Moderate)
  - Iodide I-123 (Moderate)

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Toxocariasis is mechanistically plausible but supported only by veterinary and in vitro data on adult intestinal worms. Human disease is largely tissue-dwelling larval infection that poorly absorbed pyrantel is unlikely to reach. The top-scoring prediction (papillary conjunctivitis) and several others (allergic urticaria, atopic conjunctivitis, Sorsby's fundus dystrophy, rosacea conjunctivitis) have no mechanistic or literature support. Other parasitic predictions (toxascariasis, anisakiasis, cutaneous larva migrans, capillariasis) have only indirect evidence, and established drugs such as albendazole or ivermectin are preferred for them. This should be treated as a research question, not a basis for clinical use.

**To proceed, the following is needed:**
- Detailed mechanism of action data and tissue-penetration data to test whether pyrantel can reach migrating larvae
- Human clinical data on pyrantel in toxocariasis (none currently exist)
- Comparison against current standard therapy (e.g. albendazole)
- Approved indication text, warnings and contraindications from the TGA Product Information for Anthel 125, as these are missing from the data compiled for this report and block formal safety screening
- Review of the liver and gallbladder disease signals and the iodine radioisotope interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

