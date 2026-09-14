---
layout: default
title: Venlafaxine
parent: 僅模型預測 (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
---

# Venlafaxine
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

# Venlafaxine: From Major Depressive Disorder to a Portfolio of Mood/Anxiety Spectrum Extensions

## One-Sentence Summary

> Venlafaxine (DB00285) is a serotonin–norepinephrine reuptake inhibitor (SNRI); its established core indication (referenced throughout this evidence pack's rationale fields) is **Major Depressive Disorder**. This evidence pack evaluates **10 TxGNN-predicted indications** as a portfolio: 4 candidates (dysthymic disorder, melancholia, neurotic depression, agoraphobia) are supported by **multiple RCTs and 10+ publications each** and are recommended **Proceed with Guardrails**, 1 candidate (OCD) is a **Research Question** supported by open-label/switch trials, and the remaining 5 highest-TxGNN-score candidates (Ohdo syndrome, ligneous conjunctivitis, blepharophimosis-ID Ohdo type, benign paroxysmal torticollis, childhood apraxia of speech) have **no supporting trials or literature** and are correctly flagged **Hold** as probable false positives.

⚠️ **Note on ranking:** In this pack, TxGNN's raw prediction score does **not** track evidence quality — the four highest-scoring predictions (rank 1–4) are mechanistically implausible and evidence-free, while the best-supported candidates (dysthymia, melancholia, neurotic depression, OCD, agoraphobia) sit lower in TxGNN rank but have substantial clinical/literature backing. This report is organised by evidence strength, not raw TxGNN rank.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated as structured data in this pack (`original_indications` empty, `original_moa` = Data Gap). Repurposing-rationale text across all 10 candidates consistently identifies venlafaxine's established core indication as **Major Depressive Disorder** (SNRI class) |
| Candidates Evaluated | 10 predicted indications (TxGNN rank 33,987–101,625) |
| Best-Supported Candidate | Agoraphobia (with panic disorder) |
| TxGNN Prediction Score (Agoraphobia) | 85.25% |
| Evidence Level (best candidates) | L2 (dysthymia, melancholia, neurotic depression, agoraphobia); L3 (OCD) |
| Evidence Level (worst candidates) | L5 (Ohdo syndrome, ligneous conjunctivitis, blepharophimosis-ID Ohdo type, benign paroxysmal torticollis, childhood apraxia) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Proceed with Guardrails** for 4 candidates · **Research Question** for 1 candidate · **Hold** for 5 candidates |

---

## Why Are These Predictions Reasonable?

Venlafaxine is described throughout this evidence pack's `repurposing_rationale` fields as an SNRI that inhibits reuptake of both serotonin and norepinephrine, producing an antidepressant/anxiolytic effect. The mechanistic logic for the 5 credible candidates below is that they all sit on the **depression/anxiety spectrum** venlafaxine already treats — these are not novel-mechanism repurposing hypotheses but **label-extension/sub-phenotype extensions** of its known pharmacology:

- **Dysthymic disorder, melancholia, neurotic depression** — all are depressive-spectrum diagnoses (chronic mild depression, endogenous/melancholic MDD subtype, and an older nosological term for anxious-depressive states respectively). The rationale text explicitly states these are "同類適應症延伸" (same-class indication extensions), not cross-mechanism repurposing.
- **Obsessive-compulsive disorder** — serotonergic reuptake inhibition is the established first-line OCD mechanism (SRIs); venlafaxine's noradrenergic component's contribution is described as "角色不明" (role unclear), so this is flagged as a plausible but unconfirmed hypothesis (Research Question, not yet Proceed).
- **Agoraphobia (with panic disorder)** — venlafaxine ER modulates amygdala/limbic serotonergic and noradrenergic signalling to reduce panic frequency; this is described as an existing core-indication sub-type extension, consistent with venlafaxine ER's approved panic-disorder indication in several overseas markets.

By contrast, the 5 highest-TxGNN-score candidates (Ohdo syndrome and variants, ligneous conjunctivitis, blepharophimosis-intellectual disability syndrome Ohdo type, benign paroxysmal torticollis of infancy, childhood apraxia of speech) are rare genetic/developmental/structural disorders with **no known relationship** to monoamine reuptake inhibition. The evidence pack's own rationale text labels these "疑似假陽性" (suspected false positives) and "無機轉合理性" (no mechanistic plausibility) — pure knowledge-graph artefacts with zero clinical trial or literature support.

---

## Candidate 1: Dysthymic Disorder (Persistent Depressive Disorder)

**TxGNN score:** 89.14% (rank 77,662) · **Evidence Level:** L2 · **Decision Stage:** S2 · **Recommendation:** Proceed with Guardrails

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00592384](https://clinicaltrials.gov/study/NCT00592384) | Phase 4 | Completed | 133 | Multi-site double-blind placebo-controlled RCT of venlafaxine XR in adults with spinal cord injury and MDD or dysthymia |
| [NCT01852383](https://clinicaltrials.gov/study/NCT01852383) | Phase 4 | Completed | 30 | Open-label duloxetine (not venlafaxine) trial in elderly dysthymia — disease-relevant only |
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | TASA trial comparing treatments in depressed adolescent suicide attempters — low specificity to dysthymia |
| [NCT04437485](https://clinicaltrials.gov/study/NCT04437485) | Phase 2 | Completed | 46 | Pilot RCT: collaborative depression care reducing diabetes risk in comorbid depression/prediabetes |
| [NCT01658228](https://clinicaltrials.gov/study/NCT01658228) | Phase 4 | Completed | 86 | Pilot combination treatment trial in mild cognitive impairment with depression |
| [NCT00584974](https://clinicaltrials.gov/study/NCT00584974) | Phase 2 | Completed | 523 | Double-blind placebo-controlled MDD trial (drug code SEP-225289, not confirmed venlafaxine) |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis (Tier 1) | J Clin Psychiatry | Meta-analysis of placebo-controlled RCTs confirming antidepressant efficacy in dysthymia |
| [25607727](https://pubmed.ncbi.nlm.nih.gov/25607727/) | 2015 | RCT | JAMA Psychiatry | Placebo-controlled RCT of venlafaxine XR for depression (incl. dysthymia) following spinal cord injury |
| [10836286](https://pubmed.ncbi.nlm.nih.gov/10836286/) | 2000 | RCT (Tier 2) | Int Clin Psychopharmacol | 24-week double-blind RCT: venlafaxine vs paroxetine in depressive disorder/dysthymia |
| [9846033](https://pubmed.ncbi.nlm.nih.gov/9846033/) | 1998 | Open-label pilot | J Psychiatry Neurosci | First efficacy/tolerability data for venlafaxine in primary dysthymia without concurrent MDD |
| [10665631](https://pubmed.ncbi.nlm.nih.gov/10665631/) | 1999 | Open-label | J Clin Psychiatry | Open-label study supporting venlafaxine tolerability/effectiveness in dysthymia |
| [9448655](https://pubmed.ncbi.nlm.nih.gov/9448655/) | 1997 | Open-label (Tier 2) | J Clin Psychiatry | Earliest report of venlafaxine in dysthymic disorder |
| [15533993](https://pubmed.ncbi.nlm.nih.gov/15533993/) | 2004 | Open-label, elderly (Tier 2) | J Geriatr Psychiatry Neurol | 60.9% response, 47.8% remission in elderly dysthymia (12-week flexible dose up to 300mg/d) |
| [12422062](https://pubmed.ncbi.nlm.nih.gov/12422062/) | 2002 | Open-label | Neuropsychobiology | SR-venlafaxine effective in GAD with comorbid MD or dysthymia |
| [11098413](https://pubmed.ncbi.nlm.nih.gov/11098413/) | 2000 | Review | Depress Anxiety | Notes venlafaxine "may also be effective" in dysthymia and bipolar II depression, though data more limited than for MDD |
| [10086481](https://pubmed.ncbi.nlm.nih.gov/10086481/) | 1999 | Review | J Clin Psychiatry | SSRIs/SNRIs broad-spectrum efficacy including dysthymia |

---

## Candidate 2: Melancholia

**TxGNN score:** 88.81% (rank 79,700) · **Evidence Level:** L2 · **Decision Stage:** S2 · **Recommendation:** Proceed with Guardrails

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Phase 4 | Completed | 53 | Effects of treatment (untreated MDD, incl. melancholic features) on decision-making — mechanistic, not melancholia-specific |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10757255](https://pubmed.ncbi.nlm.nih.gov/10757255/) | 2000 | Double-blind RCT (Tier 1) | J Psychopharmacol | Venlafaxine vs amitriptyline in outpatients with/without melancholia, 8-week multicentre RCT |
| [10836283](https://pubmed.ncbi.nlm.nih.gov/10836283/) | 2000 | RCT | Int Clin Psychopharmacol | Higher remission rates with venlafaxine vs fluoxetine in hospitalized MDD with melancholia |
| [7559370](https://pubmed.ncbi.nlm.nih.gov/7559370/) | 1995 | Comparative cohort (Tier 2) | J Clin Psychiatry | Venlafaxine effective and safe in hospitalized patients with major depression and melancholia vs placebo |
| [39440379](https://pubmed.ncbi.nlm.nih.gov/39440379/) | 2024 | Systematic review + TSA (Tier 2) | Epidemiol Psychiatr Sci | Adverse event risks with venlafaxine in adult MDD, systematic review with meta-analysis |
| [35947166](https://pubmed.ncbi.nlm.nih.gov/35947166/) | 2022 | Review (Tier 3) | Psychopharmacology | Psychopharmacological properties and therapeutic profile of venlafaxine |
| [11098415](https://pubmed.ncbi.nlm.nih.gov/11098415/) | 2000 | Review | Depress Anxiety | Venlafaxine and treatment-resistant depression |
| [38685594](https://pubmed.ncbi.nlm.nih.gov/38685594/) | 2024 | Post-hoc pooled analysis | CNS Spectrums | Venlafaxine XR effect on anhedonia/amotivation in MDD |
| [23953038](https://pubmed.ncbi.nlm.nih.gov/23953038/) | 2014 | Meta-regression | Int J Neuropsychopharmacol | Specificity profile of venlafaxine vs sertraline in major depression |
| [34958348](https://pubmed.ncbi.nlm.nih.gov/34958348/) | 2022 | Pharmacological study | Int J Neuropsychopharmacol | Differential potency of venlafaxine, paroxetine, atomoxetine on serotonin/norepinephrine reuptake |
| [24964257](https://pubmed.ncbi.nlm.nih.gov/24964257/) | 2015 | Review | Drug Metab Pers Ther | Clinical drug-drug interaction profile of venlafaxine |

---

## Candidate 3: Neurotic Depression

**TxGNN score:** 88.31% (rank 82,790) · **Evidence Level:** L2 · **Decision Stage:** S2 · **Recommendation:** Proceed with Guardrails

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completed | 370,212 | Large real-world retrospective claims-database cohort comparing antidepressants (incl. venlafaxine) for utilization patterns and adverse outcomes |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23953038](https://pubmed.ncbi.nlm.nih.gov/23953038/) | 2014 | Meta-regression (Tier 1) | Int J Neuropsychopharmacol | Double-blind RCTs comparing venlafaxine and sertraline in major depression |
| [12135535](https://pubmed.ncbi.nlm.nih.gov/12135535/) | 2002 | Double-blind RCT | Int J Neuropsychopharmacol | Venlafaxine vs fluoxetine in depression with concomitant anxiety (N=146) |
| [8071246](https://pubmed.ncbi.nlm.nih.gov/8071246/) | 1994 | RCT | J Clin Psychiatry | Venlafaxine vs imipramine in acute treatment of major depression, outpatients |
| [9133767](https://pubmed.ncbi.nlm.nih.gov/9133767/) | 1997 | Double-blind placebo-controlled RCT | Psychopharmacol Bull | Venlafaxine in children/adolescents (age 8–17) with major depression |
| [40801757](https://pubmed.ncbi.nlm.nih.gov/40801757/) | 2025 | Effectiveness trial | J Clin Psychiatry | ASCERTAIN-TRD: augmentation vs switching to venlafaxine XR/duloxetine in treatment-resistant depression |
| [17272528](https://pubmed.ncbi.nlm.nih.gov/17272528/) | 2007 | Review (Tier 3) | BMJ | Editorial review: venlafaxine for major depression |
| [12492770](https://pubmed.ncbi.nlm.nih.gov/12492770/) | 2002 | Literature review (Tier 3) | Acta Psychiatr Scand Suppl | Achieving remission with venlafaxine vs SSRIs |
| [25257248](https://pubmed.ncbi.nlm.nih.gov/25257248/) | 2015 | PK cohort study (Tier 2) | J Neural Transm | Steady-state venlafaxine serum concentrations in late-life depression by age/sex/BMI |
| [11983797](https://pubmed.ncbi.nlm.nih.gov/11983797/) | 2002 | Case series | J Neuropsychiatry Clin Neurosci | Venlafaxine-ECT combination in treatment-resistant depression |
| [26005260](https://pubmed.ncbi.nlm.nih.gov/26005260/) | 2015 | Comparative study | Med Arch | Tolerance comparison of venlafaxine, paroxetine, and amitriptyline |

---

## Candidate 4: Obsessive-Compulsive Disorder (OCD)

**TxGNN score:** 87.34% (rank 88,617) · **Evidence Level:** L3 · **Decision Stage:** S1 · **Recommendation:** Research Question

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04539951](https://clinicaltrials.gov/study/NCT04539951) | Phase 2 | Recruiting | 1,600 | Pragmatic trial of switching/augmentation strategies after unsatisfactory initial OCD treatment |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT + SRI augmentation in paediatric OCD partial responders |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Individual patient data meta-analysis of antidepressant efficacy in anxiety disorders incl. OCD |
| [NCT00211809](https://clinicaltrials.gov/study/NCT00211809) | Phase 4 | Terminated | 17 | CBT as adjunct to SRI pharmacotherapy in body dysmorphic disorder |
| [NCT04708834](https://clinicaltrials.gov/study/NCT04708834) | Phase 3 | Terminated | 772 | Long-term safety of adjunctive troriluzole in OCD (not venlafaxine) |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Adjunctive troriluzole RCT in OCD patients with inadequate response to SSRI/clomipramine/**venlafaxine**/desvenlafaxine |
| [NCT06659094](https://clinicaltrials.gov/study/NCT06659094) | N/A | Completed | 95 | Stepped-care internet CBT for OCD — no pharmacotherapy arm |
| [NCT01944657](https://clinicaltrials.gov/study/NCT01944657) | N/A | Withdrawn | 0 | Withdrawn, 0 enrolled |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | Double-blind RCT | J Clin Psychopharmacol | First randomized double-blind SNRI comparison: venlafaxine vs paroxetine in OCD (N=150) |
| [12444814](https://pubmed.ncbi.nlm.nih.gov/12444814/) | 2002 | Single-blind controlled study | J Clin Psychiatry | 12-week venlafaxine vs clomipramine in OCD |
| [14744166](https://pubmed.ncbi.nlm.nih.gov/14744166/) | 2004 | Double-blind switch study | J Clin Psychiatry | First controlled switch study of paroxetine to venlafaxine in OCD |
| [12755657](https://pubmed.ncbi.nlm.nih.gov/12755657/) | 2003 | Open-label (Tier 2) | J Clin Psychiatry | Venlafaxine effective in treatment-resistant OCD, incl. SSRI non-responders |
| [30516575](https://pubmed.ncbi.nlm.nih.gov/30516575/) | 2019 | Real-world cohort | J Clin Psychopharmacol | Real-world effectiveness of venlafaxine in SSRI-resistant OCD (India specialty clinic) |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | Clinical guideline (Tier 2) | World J Biol Psychiatry | WFSBP guideline for pharmacological treatment of OCD and PTSD |
| [29278206](https://pubmed.ncbi.nlm.nih.gov/29278206/) | 2018 | Systematic review (Tier 2) | Curr Med Chem | Evidence-based strategies for treatment-resistant OCD |
| [15585743](https://pubmed.ncbi.nlm.nih.gov/15585743/) | 2005 | Review (Tier 3) | Ann Pharmacother | Evaluation of published literature on venlafaxine in OCD |
| [25093787](https://pubmed.ncbi.nlm.nih.gov/25093787/) | 2014 | Case series (Tier 3) | J Neuropsychiatry Clin Neurosci | Venlafaxine in treatment-resistant OCD |
| [8599411](https://pubmed.ncbi.nlm.nih.gov/8599411/) | 1996 | Early case report | Am J Psychiatry | Treatment of OCD with venlafaxine |

**Caveat:** Clinical guidelines consistently position venlafaxine as a **second-line/alternative** OCD agent, not first-line. Evidence base is dominated by small open-label and treatment-resistant case series rather than large confirmatory RCTs — hence "Research Question" rather than "Proceed."

---

## Candidate 5: Agoraphobia (with Panic Disorder)

**TxGNN score:** 85.25% (rank 101,625) · **Evidence Level:** L2 · **Decision Stage:** S3 (most advanced) · **Recommendation:** Proceed with Guardrails

### Clinical Trial Evidence

Currently no clinical trials directly registered against this indication in the evidence pack (supporting RCT evidence is captured in literature below).

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Cochrane network meta-analysis (Tier 1) | Cochrane Database Syst Rev | Network meta-analysis of pharmacological treatments for panic disorder |
| [16894619](https://pubmed.ncbi.nlm.nih.gov/16894619/) | 2007 | Double-blind RCT | Depress Anxiety | Venlafaxine ER vs paroxetine vs placebo in panic disorder with/without agoraphobia (N=664) |
| [17589833](https://pubmed.ncbi.nlm.nih.gov/17589833/) | 2007 | RCT (Tier 1) | Psychopharmacology | Venlafaxine ER vs paroxetine in outpatients with panic disorder |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Integrative systematic review (Tier 2) | Psychother Psychosom | Pharmacological, psychotherapeutic and neurostimulatory options in treatment-resistant anxiety disorders |
| [17696574](https://pubmed.ncbi.nlm.nih.gov/17696574/) | 2007 | Review (Tier 3) | CNS Drugs | Diagnosis and treatment of agoraphobia with panic disorder |
| [9641002](https://pubmed.ncbi.nlm.nih.gov/9641002/) | 1998 | Open-label trial | Psychopharmacol Bull | Low-dose venlafaxine in panic disorder with/without agoraphobia |
| [18330461](https://pubmed.ncbi.nlm.nih.gov/18330461/) | 2008 | Commentary/review | J Psychiatry Neurosci | Combined antidepressants and CBT for panic disorder with agoraphobia |
| [15448584](https://pubmed.ncbi.nlm.nih.gov/15448584/) | 2004 | Review | CNS Spectrums | Treatment-resistant panic disorder and agoraphobia |
| [36573969](https://pubmed.ncbi.nlm.nih.gov/36573969/) | 2022 | Review | JAMA | Anxiety disorders overview, including panic disorder/agoraphobia treatment |
| [16765030](https://pubmed.ncbi.nlm.nih.gov/16765030/) | 2006 | Review | Eur Neuropsychopharmacol | Notes venlafaxine efficacy comparable to benzodiazepines in anxiety spectrum |

**Note:** Venlafaxine ER holds approved panic-disorder-with-agoraphobia indications in several overseas jurisdictions; this candidate represents the most mature (S3) and best-precedented of the portfolio, despite carrying a mid-tier TxGNN score.

---

## Candidates Recommended for Hold (No Supporting Evidence)

The following 5 candidates have **zero clinical trials and zero literature** in this evidence pack, despite the highest raw TxGNN scores. Each is flagged internally as mechanistically implausible:

| Disease | TxGNN Score | Rationale Summary |
|---------|------|------|
| Ohdo syndrome and variants | 95.86% | Chromatin-regulatory gene (KAT6B/BRPF1) developmental disorder — no known relation to SNRI mechanism; suspected false positive |
| Ligneous conjunctivitis | 93.99% | Plasminogen-deficiency fibrin deposition disorder — unrelated to monoamine reuptake |
| Blepharophimosis-intellectual disability syndrome, Ohdo type | 93.79% | Same chromatin-disorder family as above; no monoamine-system relevance |
| Benign paroxysmal torticollis of infancy | 89.73% | Theoretical migraine-precursor link possible, but no clinical/literature support and SNRI safety in infants is unestablished — risk/evidence ratio is poor |
| Childhood apraxia of speech | 88.32% | Neurodevelopmental motor-planning disorder — no mechanistic link; paediatric SNRI safety concerns unaddressed |

---

## Australia Market Information

No ARTG entries are recorded for this product in the evidence pack (`total_licenses = 0`, `market_status = Not marketed`). No dosage-form or route data is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains no structured key warnings, contraindications, or drug-drug interaction data (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for dysthymic disorder, melancholia, neurotic depression, agoraphobia) · **Research Question** (OCD) · **Hold** (Ohdo syndrome and variants, ligneous conjunctivitis, blepharophimosis-ID Ohdo type, benign paroxysmal torticollis, childhood apraxia of speech)

**Rationale:**
- Four candidates sit on venlafaxine's already-established depression/anxiety pharmacology and are backed by multiple RCTs, comparative trials, and 10+ publications each — reasonable to progress with standard psychiatric-drug guardrails.
- OCD has a real but second-line evidence base (small open-label/switch trials; guidelines position it as an alternative, not first-line) — warrants a defined research question rather than immediate progression.
- The five highest-TxGNN-score candidates are unsupported knowledge-graph artefacts with no plausible mechanism and should not consume further evaluation resources.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) for formal warnings, contraindications, and DDI data (currently all Data Gap)
- Confirmed drug-level MOA data from DrugBank (currently Data Gap; MOA description above is reconstructed from rationale text, not a primary source)
- Australian regulatory pathway assessment given zero current ARTG entries (product is not currently marketed in Australia)
- For OCD: a defined comparative RCT (venlafaxine vs standard SRI) before advancing beyond Research Question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

