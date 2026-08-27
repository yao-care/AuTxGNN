---
layout: default
title: Penicillamine
parent: 僅模型預測 (L5)
nav_order: 521
evidence_level: L5
indication_count: 10
---

# Penicillamine
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

# Penicillamine (DB00859): Original Indication Not on Record — Evaluating TxGNN's Strongest-Evidence Prediction (Disease of Transporter Activity)

## One-Sentence Summary

This evidence pack does not document Penicillamine's original approved indication or mechanism of action (both flagged as data gaps), and the drug is **not currently marketed in Australia** (0 ARTG entries). Among 10 TxGNN-predicted indications, the model's single highest-scoring prediction (megaloblastic anaemia, 98.0%) has **zero supporting trials or literature**, but a lower-ranked prediction — **"disease of transporter activity"** (93.0%, rank 3) — is backed by **20 PubMed records including one completed Phase 3 RCT**, and the supporting literature itself identifies penicillamine as the established copper-chelation therapy for Wilson's disease. This is the only candidate in the pack with evidence strong enough to act on.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `original_indications` on file; MOA also a data gap) |
| Predicted New Indication (headline) | Disease of transporter activity (rank 3 of 10 — selected for evidence strength, not raw TxGNN score; see note below) |
| TxGNN Prediction Score | 93.02% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (research-question stage only — see Conclusion for why overall status is Hold) |

**Note on candidate selection:** This evidence pack scores 10 predicted indications for Penicillamine, not one. The raw top-ranked prediction (megaloblastic anaemia, 98.0%) has no clinical trials, no literature, and a scoring recommendation of "Hold" (L5). Rather than headline an unsupported prediction, this report leads with the candidate carrying the strongest evidence. All 10 candidates are tabulated below for transparency.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Megaloblastic anaemia | 98.02% | L5 | Hold |
| 2 | Tricarboxylic acid cycle disorder | 93.46% | L4 | Research Question |
| 3 | Disease of transporter activity | 93.02% | L2 | Proceed with Guardrails |
| 4 | Neurodevelopmental disorder (ataxic gait/absent speech) | 93.01% | L5 | Hold |
| 5 | Glycogen storage disease (branching enzyme, congenital) | 92.88% | L5 | Hold |
| 6 | Glycogen storage disease (branching enzyme, perinatal) | 92.88% | L5 | Hold |
| 7 | Adult polyglucosan body disease | 92.49% | L5 | Hold |
| 8 | Chronic granulomatous disease, X-linked | 92.48% | L4 | Hold (evidence mismatch — see below) |
| 9 | Pyruvate metabolism disorder | 91.54% | L4 | Research Question |
| 10 | Haemolytic anaemia due to G6PD deficiency | 90.26% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Penicillamine is not available in this evidence pack. Based on the literature retrieved for the top candidates, Penicillamine functions as a **copper-chelating agent**, forming soluble complexes that promote urinary copper excretion — this is documented across multiple sources supporting rank 3 ("disease of transporter activity") and rank 2 ("tricarboxylic acid cycle disorder").

"Disease of transporter activity" is a broad disease-ontology grouping. The literature retrieved under this label converges heavily on **Wilson's disease** (an inherited defect in the copper-transporter gene ATP7B) and **cystinuria** (a defect in a renal amino-acid transporter). One of the retrieved records is a completed Phase 3 RCT (PMID 36183738, the CHELATE trial) comparing trientine tetrahydrochloride against penicillamine as maintenance therapy for Wilson's disease — confirming penicillamine is already established therapy in this space rather than a novel repurposing hypothesis. Several reviews (PMID 29625923, PMID 18568852) corroborate this established use.

The rank 2 candidate ("tricarboxylic acid cycle disorder") is linked more speculatively: copper chelation may inhibit *cuproptosis*, a copper-dependent cell death pathway involving TCA-cycle lipoylated proteins, but no clinical or preclinical evidence directly tests penicillamine against a TCA-cycle disorder itself — this remains mechanism-only (L4).

Rank 8 (chronic granulomatous disease) deserves a caution flag: the retrieved literature is dominated by primary biliary cirrhosis and neutrophil/nitric-oxide biology, which does not map cleanly onto the core NADPH-oxidase defect of chronic granulomatous disease. This looks like a TxGNN high score paired with a literature-search mismatch rather than genuine mechanistic support, and should not be advanced without a targeted re-search.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (all `clinical_trials` and `ictrp_trials` arrays are empty across all 10 predicted indications, including the headline candidate).

---

## Literature Evidence

### Disease of transporter activity (headline candidate, 20 records retrieved — top entries shown)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36183738](https://pubmed.ncbi.nlm.nih.gov/36183738/) | 2022 | RCT (Phase 3) | Lancet Gastroenterol Hepatol | CHELATE trial: trientine tetrahydrochloride non-inferior to penicillamine for Wilson's disease maintenance therapy |
| [29625923](https://pubmed.ncbi.nlm.nih.gov/29625923/) | 2018 | Review | Clin Res Hepatol Gastroenterol | 2017 update on Wilson's disease diagnosis and lifelong copper-chelation treatment |
| [18568852](https://pubmed.ncbi.nlm.nih.gov/18568852/) | 2008 | Review | Crit Rev Clin Lab Sci | Comprehensive review of Wilson's disease diagnosis (autosomal recessive ATP7B copper-transport disorder) |
| [3077031](https://pubmed.ncbi.nlm.nih.gov/3077031/) | 1988 | Review | Crit Rev Clin Lab Sci | Cystinuria: inherited renal transporter defect causing cystine stones |
| [39420162](https://pubmed.ncbi.nlm.nih.gov/39420162/) | 2024 | Review | Drugs | Trientine tetrahydrochloride development history, positioned against D-penicillamine intolerance |
| [32996699](https://pubmed.ncbi.nlm.nih.gov/32996699/) | 2020 | Cohort | Liver Int | mtDNA depletion-like syndrome observed in Wilson's disease patients |
| [33300046](https://pubmed.ncbi.nlm.nih.gov/33300046/) | 2021 | Preclinical | Biosci Rep | Combination of traditional formula with penicillamine in a Wilson's disease mouse model |
| [39589160](https://pubmed.ncbi.nlm.nih.gov/39589160/) | 2025 | Review | Neural Regen Res | Copper homeostasis and neurodegenerative disease overview |
| [21709497](https://pubmed.ncbi.nlm.nih.gov/21709497/) | 2011 | Preclinical | Health Phys | D-penicillamine (Cuprimine) evaluated for radioisotope decorporation |
| [41406573](https://pubmed.ncbi.nlm.nih.gov/41406573/) | 2026 | Preclinical | Redox Biol | Melatonin explored as adjunct/alternative for Wilson's disease copper overload |

### Tricarboxylic acid cycle disorder (rank 2, mechanism-only support)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37150036](https://pubmed.ncbi.nlm.nih.gov/37150036/) | 2023 | Review | Biomed Pharmacother | Molecular mechanisms of cuproptosis and relevance to cardiovascular disease |
| [39031346](https://pubmed.ncbi.nlm.nih.gov/39031346/) | 2024 | Review | Clin Hemorheol Microcirc | Cuproptosis and physical training overview |
| [27001865](https://pubmed.ncbi.nlm.nih.gov/27001865/) | 2016 | Preclinical | Biochem J | Triethylenetetramine (a related copper chelator) modulates polyamine/energy metabolism, inhibits cancer cell proliferation |

### Pyruvate metabolism disorder (rank 9, indirect support)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39147330](https://pubmed.ncbi.nlm.nih.gov/39147330/) | 2024 | Preclinical | Biochem Pharmacol | Melatonin plus penicillamine/zinc gluconate combination studied in copper-laden rats (Wilson's disease model) |
| [5644093](https://pubmed.ncbi.nlm.nih.gov/5644093/) | 1968 | Cohort | Am J Med | D-penicillamine and dietary treatment effects on plasma cystine/cysteine in cystinosis |

---

## Australia Market Information

Penicillamine has **no ARTG entries** and is **not currently marketed in Australia** — this candidate pack contains no product listings to summarise.

---

## Safety Considerations

Safety data for this candidate is incomplete: TFDA-equivalent warning and contraindication data was not retrieved (flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet pass an initial safety screen), and no drug–drug interaction records were found. Please refer to the TGA-approved Product Information (PI) for safety information before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold** (at the overall candidate-package level)

**Rationale:**
Although the "disease of transporter activity" candidate (Wilson's disease/cystinuria mechanism) has genuine L2-grade evidence including a Phase 3 RCT and would individually merit "Proceed with Guardrails" as a research question, the drug is not marketed in Australia (0 ARTG entries) and carries a **Blocking** safety data gap (no TFDA-equivalent warnings/contraindications on file). Both must be resolved before this moves past a research question. The other 9 predicted indications lack sufficient evidence (L4–L5) to act on at all, and the chronic granulomatous disease candidate (rank 8) shows signs of a literature-search mismatch rather than genuine support.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications, DDI) to clear the blocking safety gap
- Confirmed mechanism-of-action documentation (currently absent)
- Confirmation of any Australian regulatory pathway, given the drug is currently unmarketed
- A targeted re-search of literature for the chronic granulomatous disease candidate to confirm or rule out the apparent mismatch
- If pursuing the transporter-activity/Wilson's disease angle further: clarification of whether this represents a genuinely new indication for this market or simply documentation of an already-established use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

