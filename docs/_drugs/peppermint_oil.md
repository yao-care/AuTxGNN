---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: Ten TxGNN-Predicted Indications — Cardiovascular Disease as the Only Evidence-Backed Candidate

## One-Sentence Summary

Peppermint oil (DrugBank DB11198) has no recorded original indication in this evidence pack and is not currently marketed in Australia (0 ARTG entries). TxGNN generated 10 candidate new indications, but the **highest-scoring** prediction (leprosy, 99.8%) has **zero** supporting trials or literature, while the only candidate with real-world evidence — **cardiovascular disease** (rank 9, 99.1%) — is backed by **3 clinical trials** and **8 publications**, though all are small pilot studies rather than confirmatory RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication recorded (drug not marketed in Australia) |
| Highest-Scoring Prediction | Leprosy (TxGNN score 99.80%), but **no clinical trials or literature support it** — likely model noise |
| Best-Evidenced Prediction | Cardiovascular Disease (TxGNN score 99.13%) — 3 trials, 8 publications |
| Evidence Level (Cardiovascular Disease) | L3 |
| Evidence Level (other 9 candidates) | L5 (model prediction only) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## All 10 Predicted Indications (Ranked by TxGNN Score)

| Rank | Predicted Indication | TxGNN Score | Evidence | Evidence Level | Recommendation |
|------|----------------------|-------------|----------|-----------------|-----------------|
| 1 | Leprosy | 99.80% | None | L5 | Hold — no known mechanism, judged model noise |
| 2 | Pneumocystosis | 99.58% | None | L5 | Hold — no known antifungal mechanism |
| 3 | Coronary Artery Disease | 99.35% | None | L5 | Hold — mechanism purely inferential |
| 4 | Myocardial Ischemia | 99.26% | None | L5 | Hold — no preclinical/clinical validation |
| 5 | Echinococcus granulosus Infection | 99.25% | None | L5 | Hold — no specific antiparasitic mechanism |
| 6 | Polyp of Vocal Cord | 99.14% | None | L5 | Hold — no known mechanism |
| 7 | Uterine Polyp | 99.14% | None | L5 | Hold — no known mechanism |
| 8 | Polyp of Middle Ear | 99.14% | None | L5 | Hold — no known mechanism |
| **9** | **Cardiovascular Disease** | **99.13%** | **3 trials, 8 papers** | **L3** | **Hold — research question, not yet actionable** |
| 10 | Polyp of Frontal Sinus | 99.12% | None | L5 | Hold — sensory/decongestant effect only, not curative |

The disconnect between TxGNN rank and evidence availability is notable: the model's single highest-confidence prediction (leprosy) has no supporting data at all, while the only candidate with real trials and literature ranks 9th. This pattern is consistent with the mechanistic rationale text for each candidate, most of which explicitly flag "no known mechanism" or "model noise."

---

## Why is This Prediction Reasonable? (Cardiovascular Disease)

Detailed mechanism of action data for peppermint oil as a whole is not available in this evidence pack (marked as Data Gap). However, the evidence pack's own mechanistic rationale for the cardiovascular disease candidate is informative: peppermint oil's major constituent, **menthol**, is a known TRPM8 receptor agonist with calcium-channel-blocking activity. Menthol has documented effects on vagal (parasympathetic) tone, heart rate, and vascular smooth muscle, which provides a plausible physiological link to cardiovascular/cardiometabolic parameters such as blood pressure and heart rate variability.

This mechanism does not, however, establish disease-specific efficacy against "cardiovascular disease" as a clinical endpoint — it supports a narrower, symptomatic/parameter-level effect (e.g. blood pressure, autonomic tone) rather than a disease-modifying one. The related predictions for coronary artery disease and myocardial ischemia (ranks 3 and 4) rely on the same theoretical extrapolation but currently have **no supporting trials or literature at all**, so they should be treated as unproven hypotheses rather than corroborating evidence.

---

## Clinical Trial Evidence (Cardiovascular Disease)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05071833](https://clinicaltrials.gov/study/NCT05071833) | N/A (dietary intervention) | Completed | 36 | Small exploratory study of oral peppermint supplementation on cardiometabolic parameters; direct relevance but weak statistical power. |
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | N/A (dietary intervention) | Completed | 40 | Peppermint oil effects on cardiometabolic outcomes in mild-to-moderate hypertension; follows on from an earlier RCT showing improved systolic BP and lipids in healthy individuals. |

One additional trial, [NCT04966546](https://clinicaltrials.gov/study/NCT04966546) (subdural hematoma post-operative monitoring), was excluded from the table above — it was withdrawn (0 enrolled) and is mechanistically unrelated to peppermint oil or cardiovascular disease; it appears to be a search false-positive.

Neither remaining trial is a randomised, placebo-controlled Phase 2/3 trial with a formal phase designation — both are small, unblinded/exploratory dietary intervention studies.

---

## Literature Evidence (Cardiovascular Disease)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT (protocol) | PLoS One | Protocol for a placebo-controlled RCT of peppermint oil in pre-hypertension/stage 1 hypertension, citing menthol/flavonoid content as the rationale — trial not yet reporting results. |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Cohort | Experimental Physiology | Gastric cooling and menthol increase cardiac parasympathetic (vagal) activity and reduce heart rate in healthy volunteers — supports the autonomic mechanism cited above. |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Review | Explore (NY) | Brief review mentioning peppermint oil primarily for irritable bowel syndrome, not cardiovascular disease — low direct relevance. |
| [19198983](https://pubmed.ncbi.nlm.nih.gov/19198983/) | 2009 | Review | Internal and Emergency Medicine | General internal/cardiovascular medicine update; no abstract available, relevance unclear. |
| [17577363](https://pubmed.ncbi.nlm.nih.gov/17577363/) | 2007 | Case Report | Contact Dermatitis | Allergic contact dermatitis from peppermint foot spray — a safety signal, not an efficacy finding. |

Three further records returned by the literature search — PMID [39139335](https://pubmed.ncbi.nlm.nih.gov/39139335/) (lercanidipine nanoemulsion), [28889028](https://pubmed.ncbi.nlm.nih.gov/28889028/) (candesartan nanoemulsion), and [27277875](https://pubmed.ncbi.nlm.nih.gov/27277875/) (exhaled-breath menthol detection) — do not discuss peppermint oil's cardiovascular effects and appear to be keyword-search false positives; they are excluded from the table above but flagged here for transparency rather than silently dropped.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction, contraindication, or warning data are currently available in this evidence pack, and drug–drug interaction lookups returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Peppermint oil is not currently marketed in Australia, has no recorded original indication, and no TGA PI safety data — this alone is a blocking gap for any safety assessment. Of the 10 TxGNN-predicted indications, 9 have no supporting evidence whatsoever, and the one with genuine data (cardiovascular disease) is supported only by two small, non-randomised or protocol-stage studies (n=36–40), not a completed confirmatory RCT.

**To proceed, the following is needed:**
- TGA Product Information (warnings, contraindications) — currently blocking (Severity: Blocking)
- Original mechanism of action data from DrugBank (Severity: High)
- Results from the ongoing/protocol-stage RCT (PMID 40333716) once completed
- A larger, adequately powered RCT specifically testing cardiovascular disease outcomes before this indication can move beyond "Research Question" status
- Re-verification of the leprosy and other L5 candidates against updated TxGNN model versions, given the complete absence of corroborating mechanism or evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

