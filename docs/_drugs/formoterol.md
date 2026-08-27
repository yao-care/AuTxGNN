---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Formoterol
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

# Formoterol: From Long-Acting Bronchodilator Therapy to Obstructive Lung Disease (COPD)

## One-Sentence Summary

> Formoterol is a long-acting beta2-adrenergic agonist (LABA) bronchodilator already used worldwide in asthma and COPD combination inhalers, though no formal original-indication record was returned for this jurisdiction in the evidence pack.
> Among the ten TxGNN-predicted indications reviewed, **Obstructive Lung Disease (COPD)** carries by far the strongest supporting evidence, with **50 clinical trials** and **20 publications** identified, including multiple landmark Phase 3 mortality/exacerbation trials (ETHOS, KRONOS, FULFIL).
> Note: TxGNN's single highest-scoring raw prediction, "respiratory malformation," was reviewed and excluded from this report — the evidence pack's own analysis flags it as a knowledge-graph node-matching artefact, since the underlying trials and literature are entirely about asthma/COPD, not structural airway malformation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (Data Gap); formoterol is a well-established LABA bronchodilator for asthma/COPD based on the trial and literature evidence contained in this pack |
| Predicted New Indication | Obstructive Lung Disease (COPD) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed (0 ARTG entries recorded) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from the source query for this evidence pack (Data Gap). Based on the extensive trial and literature evidence it does contain, formoterol is a long-acting beta2-adrenergic agonist (LABA) that activates β2 receptors on airway smooth muscle, raising cAMP/PKA signalling to produce rapid-onset, long-duration (12+ hour) bronchodilation. It is a core component of numerous fixed-dose combination inhalers (e.g., budesonide/formoterol, beclometasone/formoterol, glycopyrronium/formoterol, aclidinium/formoterol) used globally in obstructive airway disease.

Obstructive Lung Disease (a category that principally captures COPD) shares the same underlying pathophysiology that formoterol's LABA mechanism directly targets — airflow limitation from bronchial smooth-muscle tone and airway remodelling. This is reflected in landmark completed Phase 3 trials such as ETHOS, KRONOS and FULFIL, which evaluated formoterol-containing triple/dual therapies against hard clinical endpoints (FEV1, exacerbation rate, and — notably in ETHOS — all-cause mortality).

By contrast, the model's single top-ranked raw output, "respiratory malformation," has no mechanistic plausibility: it is a structural congenital anomaly, not a functional airway-tone disorder, and every trial/publication returned for it is actually about asthma, COPD or Symbicort — confirming this is very likely an ontology-adjacency artefact in the knowledge graph rather than a genuine signal. The other TxGNN-ranked candidates with no supporting trials or literature (Rienhoff syndrome, interstitial emphysema, hyperlucent lung, compensatory emphysema, asthma-related genetic susceptibility) are model-score-only predictions with no clinical or mechanistic basis and are not carried forward in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06744374](https://clinicaltrials.gov/study/NCT06744374) | N/A (observational) | Completed | 22,369 | Real-world mortality/cardiopulmonary event comparison, single-inhaler (BGF) vs multiple-inhaler triple therapy in COPD |
| [NCT00206154](https://clinicaltrials.gov/study/NCT00206154) | Phase 3 | Completed | 1,500 | Symbicort pMDI vs formoterol, budesonide, combination and placebo in COPD maintenance |
| [NCT07069829](https://clinicaltrials.gov/study/NCT07069829) | N/A (observational) | Recruiting | 1,400 | Real-world clinical/patient-reported outcomes, Breztri/Trixeo triple therapy in moderate-severe COPD |
| [NCT00793624](https://clinicaltrials.gov/study/NCT00793624) | Phase 3 | Completed | 906 | 48-week long-term efficacy/safety of once-daily BI 1744 CL vs twice-daily Foradil (formoterol) in COPD |
| [NCT03662711](https://clinicaltrials.gov/study/NCT03662711) | Phase 4 | Terminated | 843 | 1-year LABD ± ICS effect on re-hospitalisation/death in elderly COPD patients (graded directly relevant) |
| [NCT03963167](https://clinicaltrials.gov/study/NCT03963167) | N/A (observational) | Completed | 661 | 12-month real-world health status and adherence with Trimbow (BDP/FF/G) in COPD |
| [NCT05311306](https://clinicaltrials.gov/study/NCT05311306) | N/A (observational) | Completed | 475 | Real-world change in clinical/patient-reported outcomes with TRIXEO (budesonide/glycopyrronium/formoterol) in COPD |
| [NCT00421122](https://clinicaltrials.gov/study/NCT00421122) | Phase 3 | Completed | 315 | Symbicort Turbuhaler vs Pulmicort Turbuhaler + Bricasol pMDI in Chinese COPD patients |
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | Completed | 340 | Symbicort Turbuhaler vs Pulmicort Turbuhaler + Theolong tablet, Japanese patients (graded directly relevant) |
| [NCT02347072](https://clinicaltrials.gov/study/NCT02347072) | Phase 3 | Completed | 80 | 24-hour lung function profile of PT003 vs Spiriva Respimat vs placebo in moderate-to-very-severe COPD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33252985](https://pubmed.ncbi.nlm.nih.gov/33252985/) | 2021 | RCT | Am J Respir Crit Care Med | ETHOS trial: budesonide/glycopyrrolate/formoterol reduced all-cause mortality vs dual therapy in COPD |
| [30232048](https://pubmed.ncbi.nlm.nih.gov/30232048/) | 2018 | RCT | Lancet Respir Med | KRONOS trial: triple therapy (BGF) vs dual therapies in moderate-to-very-severe COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy vs dual ICS/LABA in COPD |
| [39213002](https://pubmed.ncbi.nlm.nih.gov/39213002/) | 2025 | Cohort | Am J Respir Crit Care Med | Post hoc ETHOS analysis: effect of triple therapy on cardiovascular/severe cardiopulmonary events |
| [33273813](https://pubmed.ncbi.nlm.nih.gov/33273813/) | 2020 | Review | Int J Chron Obstruct Pulmon Dis | Overview of formoterol pharmacology and efficacy in COPD |
| [35512458](https://pubmed.ncbi.nlm.nih.gov/35512458/) | 2022 | Analysis | Respir Med | ETHOS sub-analysis: prior ICS use and benefits of BGF on exacerbations, symptoms, QoL and lung function |
| [39420338](https://pubmed.ncbi.nlm.nih.gov/39420338/) | 2024 | RCT | Respir Res | TRIFORCE trial: BDP/FF/G effects on lung hyperinflation and exercise endurance in COPD |
| [40619503](https://pubmed.ncbi.nlm.nih.gov/40619503/) | 2025 | Comparative effectiveness | Adv Ther | FF/UMEC/VI vs BUD/GLY/FORM in COPD patients stepping up from dual therapy |
| [31951778](https://pubmed.ncbi.nlm.nih.gov/31951778/) | 2020 | Review | Expert Rev Clin Pharmacol | Aclidinium bromide/formoterol fumarate for maintenance treatment of COPD |
| [26049917](https://pubmed.ncbi.nlm.nih.gov/26049917/) | 2015 | Review | Eur J Intern Med | Extensive review of long-acting bronchodilators formoterol and salmeterol in COPD |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-interaction data were returned for formoterol in this evidence pack (source query status: not found), and no ARTG-registered Australian product record was located to cross-check against.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (ETHOS, KRONOS, FULFIL) plus a large real-world evidence base directly support formoterol-containing regimens in obstructive lung disease/COPD, giving this candidate the highest evidence level (L1) and most mature decision stage (S3) of all ten TxGNN outputs reviewed. However, formoterol currently has no ARTG-registered product recorded in this dataset and no TFDA-equivalent safety/warning data was retrievable, so this should be treated as evidence-supported guidance pending local regulatory confirmation rather than a ready-to-implement recommendation.

**To proceed, the following is needed:**
- Confirmation of current Australian ARTG registration status and product listings for formoterol (0 entries returned here appears to be a data-gap rather than a true absence of marketed product)
- Product Information (PI) warnings, contraindications and drug-interaction data
- Formal mechanism-of-action record from DrugBank/equivalent source
- Clarification of why TxGNN's top-ranked output ("respiratory malformation") is a knowledge-graph artefact, to avoid this recurring in automated triage of future candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

