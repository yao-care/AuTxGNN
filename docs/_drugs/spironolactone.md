---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Spironolactone
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

# Spironolactone: From Hypertension/Heart Failure to Androgenetic Alopecia

## One-Sentence Summary

Spironolactone is a mineralocorticoid (aldosterone) receptor antagonist historically used for hypertension, heart failure, and oedema. The TxGNN model, cross-checked against real-world evidence, points most credibly to **Alopecia (Androgenetic Alopecia)** as a repurposing candidate — not the model's top-ranked disease label, which lacks any supporting evidence. This alopecia indication is backed by **2 clinical trials** and **10+ relevant publications**, including one completed Phase 2 RCT and multiple systematic reviews.

> **Note on candidate selection**: This evidence pack scored 10 TxGNN-predicted indications for spironolactone. The single highest-scoring label ("hypotrichosis simplex of the scalp," 99.26%) has **zero** supporting trials or literature and its own rationale states no mechanistic link exists — it is treated as noise, not a lead. This report is built around the best-*evidenced* candidate instead. A summary of all 10 candidates is provided at the end for transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, heart failure, and oedema (per literature within this evidence pack, PMID 35138351); no Australian TGA-approved indication text is available in this dataset |
| Predicted New Indication | Alopecia (Androgenetic Alopecia / Female Pattern Hair Loss) |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

DrugBank-sourced mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, literature captured within this pack consistently characterises spironolactone as a synthetic aldosterone receptor antagonist that also exhibits anti-androgenic activity — it competitively blocks androgen receptors and reduces testosterone synthesis (PMID 35038224, PMID 36923692).

Androgenetic alopecia is driven by follicular sensitivity to androgens (dihydrotestosterone), causing progressive miniaturisation of scalp hair follicles. Spironolactone's anti-androgenic action is mechanistically well matched to this pathophysiology, which is why it has been used off-label by dermatologists for decades, particularly in women who cannot use finasteride.

Importantly, the evidence pack also shows the model producing several unrelated or mismatched labels for the same drug (e.g. "diffuse alopecia areata," an autoimmune condition with a distinct mechanism, and several disease labels tied only to generic "hypoxia" literature with no real pharmacological link). This underscores that TxGNN's raw ranking should not be read at face value — the alopecia (androgenetic) signal is credible because it is corroborated by real trial and literature evidence, not because of its score alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175617](https://clinicaltrials.gov/study/NCT00175617) | Phase 2 | Completed | 40 | RCT comparing oral spironolactone versus topical minoxidil for female pattern hair loss; directly relevant, completed with outcome data. |
| [NCT02483195](https://clinicaltrials.gov/study/NCT02483195) | Phase 4 | Withdrawn | 0 | Planned head-to-head of finasteride vs. spironolactone+minoxidil in postmenopausal androgenetic alopecia; withdrawn before enrolment, no data generated. |

No ANZCTR-registered trials were identified in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34352345](https://pubmed.ncbi.nlm.nih.gov/34352345/) | 2022 | Systematic Review | J Am Acad Dermatol | Efficacy and safety profile of oral spironolactone for androgenic alopecia. |
| [36923692](https://pubmed.ncbi.nlm.nih.gov/36923692/) | 2023 | Systematic Review | Clin Cosmet Investig Dermatol | Oral and topical spironolactone stimulate hair growth and are widely used by dermatologists for AGA. |
| [37650533](https://pubmed.ncbi.nlm.nih.gov/37650533/) | 2024 | RCT/Comparative | J Cosmet Dermatol | Blinded RCT: topical minoxidil + oral spironolactone vs. topical minoxidil + oral finasteride in women with AGA/female pattern hair loss. |
| [27225981](https://pubmed.ncbi.nlm.nih.gov/27225981/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Review of interventions for female pattern hair loss, including antiandrogens such as spironolactone. |
| [38852607](https://pubmed.ncbi.nlm.nih.gov/38852607/) | 2024 | Systematic Review | J Cosmet Laser Ther | Systematic review of 141 studies on oral, topical, and procedural treatments for androgenic alopecia. |
| [37284568](https://pubmed.ncbi.nlm.nih.gov/37284568/) | 2023 | Review | Clin Cosmet Investig Dermatol | Current guidance and unmet needs in AGA treatment, including antiandrogen therapy. |
| [37823040](https://pubmed.ncbi.nlm.nih.gov/37823040/) | 2023 | Review | JAAD Int | Update on AGA pathophysiology mediated by androgen sensitivity of scalp follicles. |
| [39893632](https://pubmed.ncbi.nlm.nih.gov/39893632/) | 2025 | Review | Expert Opin Drug Metab Toxicol | Comprehensive review of efficacy, safety, and tolerability of alopecia drugs, including spironolactone. |
| [38540126](https://pubmed.ncbi.nlm.nih.gov/38540126/) | 2024 | Review | Biomedicines | Hormonal background of non-scarring alopecias, covering androgen-mediated pathways targeted by spironolactone. |
| [35038224](https://pubmed.ncbi.nlm.nih.gov/35038224/) | 2022 | Review | Dermatol Ther | Overview of spironolactone's anti-androgenic mechanism and dermatological uses. |

---

## Australia Market Information

This evidence pack records **0 ARTG entries** for spironolactone (market status: not marketed). No product listings are available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable at the time of this evidence pull — this is flagged as a **Blocking** data gap (DG001: TFDA/TGA PI warnings and contraindications), meaning a formal Stage 1 safety assessment cannot yet proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The androgenetic alopecia indication is supported by L2-level evidence (one completed Phase 2 RCT plus multiple systematic reviews) and a coherent, literature-corroborated mechanistic rationale, consistent with its long-established off-label dermatological use. However, the drug is not currently marketed in Australia under this dataset and formal safety documentation is missing, so guardrails are required before any clinical or regulatory action.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) — currently a Blocking gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Verification of current Australian marketing/ARTG status, since this pack shows 0 entries
- A larger, dedicated RCT in androgenetic alopecia to move evidence from L2 toward L1
- Formal safety monitoring plan (electrolytes/potassium, renal function) given spironolactone's known anti-mineralocorticoid class effects

---

## Appendix: Other Candidate Indications Screened

For transparency, all 10 TxGNN-predicted indications in this evidence pack are listed below. Most of the highest-scoring labels have no supporting trial or literature evidence and are not actionable.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------|------|------|------|------|
| 1 | Hypotrichosis simplex of the scalp | 99.26% | L5 | S0 | Hold | Rare genetic disorder (APCDD1); no mechanistic link, no evidence |
| 2 | Congenital hypotrichosis milia | 99.04% | L5 | S0 | Hold | Rare congenital syndrome; no known pathway link, no evidence |
| 3 | Diffuse alopecia areata | 98.41% | L4 | S0 | Hold | Only literature found is about a different condition (androgenetic, not autoimmune, alopecia) — label mismatch |
| 4 | **Alopecia (Androgenetic)** | 97.83% | **L2** | **S2** | **Proceed with Guardrails** | Featured indication in this report |
| 5 | Malignant hypertensive renal disease | 97.54% | L5 | S0 | Hold | Theoretical mechanism only, no evidence |
| 6 | Malignant renovascular hypertension | 97.54% | L3 | S1 | Research Question | Mechanistically on-label (aldosterone antagonism) but only review-level literature, no dedicated trials |
| 7 | Pulmonary hypertension owing to lung disease/hypoxia | 97.33% | L5 | S0 | Hold | Literature retrieved is generic hypoxia biology, not drug-specific — likely term co-occurrence artefact |
| 8 | Pulmonary hypertension, unclear multifactorial mechanism | 97.33% | L5 | S0 | Hold | No trials, no literature |
| 9 | Braddock (CHOPS) syndrome | 96.64% | L5 | S0 | Hold | Rare genetic syndrome, no known pathway link |
| 10 | Chronic pulmonary heart disease (cor pulmonale) | 95.55% | L2 | S2 | Research Question | Second-best evidenced candidate — a completed Phase 4 trial in chronic right heart failure (n=15) plus mechanistic literature on MRA in pulmonary hypertension models; worth a separate evaluation |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

