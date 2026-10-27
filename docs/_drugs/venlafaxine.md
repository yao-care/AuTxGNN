---
layout: default
title: Venlafaxine
parent: Model Prediction Only (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Venlafaxine: predicted new indication Top TxGNN rank: Ohdo syndrome and variants . Best-supported: Dysthymi… (evidence level L5). Approved use: Not stated in the ARTG data compiled for this report. T…"
monitor_inn: "Venlafaxine"
predicted_indications: ["Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy", "dysthymic disorder", "melancholia", "childhood apraxia of speech", "obsessive-compulsive disorder", "agoraphobia"]
---

# Venlafaxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Venlafaxine: From Depressive and Anxiety Disorders to Dysthymic Disorder
{: .text-alpha }

## One-Sentence Summary

Venlafaxine is a serotonin-noradrenaline reuptake inhibitor, originally used for depression (including major depressive disorder) and anxiety-related conditions such as social phobia.
The TxGNN model ranks **Ohdo syndrome and variants** highest, but this prediction has no supporting evidence. The best-supported prediction is **Dysthymic Disorder**, with **4 clinical trials** and **20 publications** currently supporting this direction.
Evidence for the top-ranked prediction is model-only (L5), so this report also reviews the better-supported candidates below it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report. The knowledge graph lists unipolar depression, major depressive disorder, anxiety disorder and social phobia |
| Predicted New Indication | Top TxGNN rank: Ohdo syndrome and variants (no evidence, Hold). Best-supported: Dysthymic disorder |
| TxGNN Prediction Score | Ohdo syndrome and variants: 95.86%. Dysthymic disorder: 89.14% |
| Evidence Level | Ohdo syndrome: L5. Dysthymic disorder: L2 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Ohdo syndrome: Hold. Dysthymic disorder: Proceed with Guardrails (research question) |

**Overview of all ranked predictions**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Ohdo syndrome and variants | 95.86% | L5 | Hold. No mechanistic link, likely a knowledge-graph artefact |
| 2 | Ligneous conjunctivitis | 93.99% | L5 | Hold. Plasminogen deficiency, unrelated to monoamine reuptake |
| 3 | Blepharophimosis-intellectual disability syndrome, Ohdo type | 93.79% | L5 | Hold. Same entity as rank 1 |
| 4 | Benign paroxysmal torticollis of infancy | 89.73% | L5 | Hold. Speculative link, infant safety concerns |
| 5 | Dysthymic disorder | 89.14% | L2 | Research question. Closest to an indication extension |
| 6 | Melancholia | 88.81% | L2 | Research question. Subtype of an established indication |
| 7 | Childhood apraxia of speech | 88.32% | L5 | Hold. No plausible mechanism |
| 8 | Neurotic depression | 88.31% | L2 | Research question. Outdated term, overlaps depression and dysthymia |
| 9 | Obsessive-compulsive disorder | 87.34% | L2 | Proceed with Guardrails |
| 10 | Agoraphobia | 85.25% | L3 | Research question. Usually co-occurs with panic disorder |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Venlafaxine is generally known as a serotonin-noradrenaline reuptake inhibitor (SNRI). Its efficacy in depressive and anxiety disorders is established, and mechanistically it may be applicable to related conditions.

**Top-ranked predictions (ranks 1-4, 7).** There is no credible link for the highest-scoring predictions. Ohdo syndrome (KAT6B-related chromatin disorder), ligneous conjunctivitis (plasminogen deficiency) and childhood apraxia of speech (neurodevelopmental) are not addressed by monoamine reuptake inhibition. Benign paroxysmal torticollis of infancy has a weak, speculative link through migraine-spectrum biology, but paediatric use raises significant safety concerns. The high scores are most likely knowledge-graph artefacts.

**Better-supported predictions.** The predictions with real support sit within the depression and anxiety spectrum:
- **Dysthymic disorder** is a chronic depressive disorder on the same spectrum as the approved depression indications. This is closer to an indication extension than true repurposing.
- **Melancholia** and **neurotic depression** are a severe subtype and an historical term, respectively, of depression. The evidence returned concerns general major depression rather than these specific labels.
- **Obsessive-compulsive disorder** shares the serotonergic mechanism of first-line therapy (SSRIs/clomipramine). Evidence is mixed. A double-blind comparison with paroxetine found comparable efficacy, while other work is open-label or in treatment-resistant patients. Guideline-level reviews place venlafaxine as a second-line or augmentation option.
- **Agoraphobia** usually occurs with panic disorder, for which SSRIs and SNRIs are established treatments. No agoraphobia-specific trials are registered.

---

## Clinical Trial Evidence

The trials below are for the best-supported predictions. The four highest-ranked predictions (ranks 1 to 3, plus ranks 4 and 7) have no registered trials, nor does neurotic depression or agoraphobia.

**Dysthymic disorder**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00592384](https://clinicaltrials.gov/study/NCT00592384) | Phase 4 | Completed | 133 | Placebo-controlled trial of venlafaxine XR for major depression or dysthymia after spinal cord injury. Directly tests venlafaxine but in a specific comorbid population |
| [NCT00584974](https://clinicaltrials.gov/study/NCT00584974) | Phase 2 | Completed | 523 | Placebo-controlled study of SEP-225289 (a different compound) in major depressive disorder. Indirect relevance |
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | Treatments for depressed adolescents who attempted suicide. Not dysthymia-specific |
| [NCT01658228](https://clinicaltrials.gov/study/NCT01658228) | Phase 4 | Completed | 86 | Pilot combination treatment in mild cognitive impairment with depression. Limited relevance |

**Melancholia**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Phase 4 | Completed | 53 | Treatment effects on decision-making in major depression. Cognitive rather than efficacy endpoints |

**Obsessive-compulsive disorder**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04539951](https://clinicaltrials.gov/study/NCT04539951) | Phase 2 | Recruiting | 1600 | Pragmatic trial of switching or augmentation strategies after unsatisfactory initial OCD treatment. May provide direct comparative evidence when complete |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Cognitive behavioural therapy added to SRI treatment in paediatric OCD. Does not test venlafaxine directly |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8800 | Individual patient data meta-analysis of antidepressant efficacy in anxiety disorders. Indirect relevance |

No ANZCTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Dysthymic disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Antidepressant efficacy in dysthymia from placebo-controlled RCTs (class-level, not venlafaxine-specific) |
| [25607727](https://pubmed.ncbi.nlm.nih.gov/25607727/) | 2015 | RCT | JAMA Psychiatry | Venlafaxine extended-release for depression after spinal cord injury |
| [10836286](https://pubmed.ncbi.nlm.nih.gov/10836286/) | 2000 | Randomised trial | Int Clin Psychopharmacol | 24-week double-blind comparison of venlafaxine and paroxetine in major depression or dysthymia |
| [9448655](https://pubmed.ncbi.nlm.nih.gov/9448655/) | 1997 | Clinical study | J Clin Psychiatry | Venlafaxine in dysthymic disorder |
| [15533993](https://pubmed.ncbi.nlm.nih.gov/15533993/) | 2004 | Open-label trial | J Geriatr Psychiatry Neurol | Elderly dysthymia: 60.9% responders (intent-to-treat), 47.8% remission |
| [11098413](https://pubmed.ncbi.nlm.nih.gov/11098413/) | 2000 | Review | Depress Anxiety | Venlafaxine may be effective in dysthymia, with more limited data than in major depression |

**Neurotic depression**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19165525](https://pubmed.ncbi.nlm.nih.gov/19165525/) | 2009 | Meta-analysis | Eur Arch Psychiatry Clin Neurosci | Venlafaxine versus other antidepressants and placebo in major depression |
| [23953038](https://pubmed.ncbi.nlm.nih.gov/23953038/) | 2014 | Meta-regression | Int J Neuropsychopharmacol | Moderators of response to venlafaxine and sertraline in major depression |
| [40633778](https://pubmed.ncbi.nlm.nih.gov/40633778/) | 2025 | RCT | J Affect Disord | Cognitive effects of augmentation versus switching to venlafaxine XR/duloxetine in treatment-resistant depression |

**Melancholia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7559370](https://pubmed.ncbi.nlm.nih.gov/7559370/) | 1995 | Placebo-controlled study | J Clin Psychiatry | Venlafaxine versus placebo in hospitalised patients with major depression and melancholia |

**Obsessive-compulsive disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | J Clin Psychopharmacol | Double-blind venlafaxine versus paroxetine in OCD (150 patients) |
| [14744166](https://pubmed.ncbi.nlm.nih.gov/14744166/) | 2004 | RCT | J Clin Psychiatry | Double-blind switch study of paroxetine and venlafaxine in OCD |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | Guideline | World J Biol Psychiatry | WFSBP guidelines for OCD and PTSD |
| [29278206](https://pubmed.ncbi.nlm.nih.gov/29278206/) | 2018 | Systematic review | Curr Med Chem | Strategies for OCD resistant to first-line pharmacotherapy |
| [12755657](https://pubmed.ncbi.nlm.nih.gov/12755657/) | 2003 | Open-label study | J Clin Psychiatry | Venlafaxine in treatment-resistant OCD |
| [15585743](https://pubmed.ncbi.nlm.nih.gov/15585743/) | 2005 | Review | Ann Pharmacother | Published literature on venlafaxine in OCD |

**Agoraphobia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Pharmacological treatments in panic disorder (not venlafaxine-specific) |
| [16894619](https://pubmed.ncbi.nlm.nih.gov/16894619/) | 2007 | Double-blind RCT | Depress Anxiety | Venlafaxine ER, paroxetine and placebo in panic disorder (664 patients) |
| [19358784](https://pubmed.ncbi.nlm.nih.gov/19358784/) | 2009 | Double-blind RCT | J Clin Psychiatry | Venlafaxine ER in adult outpatients with panic disorder |
| [17696574](https://pubmed.ncbi.nlm.nih.gov/17696574/) | 2007 | Review | CNS Drugs | Diagnosis and treatment of agoraphobia with panic disorder |

Currently no related literature is available for ranks 1 to 4 and 7 (Ohdo syndrome and variants, ligneous conjunctivitis, benign paroxysmal torticollis of infancy, childhood apraxia of speech).

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14402B | Efexor-XR | Capsule (modified release) 150 mg (as hydrochloride) | Not stated in the data compiled for this report |

Only one ARTG entry (single-ingredient, valid, oral) was found.

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text).** The knowledge graph links venlafaxine to the following conditions as contraindications. These should be checked against the TGA-approved Product Information:
- Cardiovascular: hypertension, long QT syndrome, cardiovascular and heart disease, cerebrovascular disorder
- Hepatic and renal: liver failure, liver disease, cirrhosis, gallbladder disease, impaired renal function
- Neurological and psychiatric: epilepsy, bipolar disorder and major affective disorder, substance-related disorder and drug dependence, neuroleptic malignant syndrome
- Other: angle-closure glaucoma and ocular hypertension, blood coagulation disease, hypertriglyceridaemia, hyperthyroidism (including Graves disease), inappropriate ADH syndrome, interstitial lung disease

**Drug Interactions.** 100 interactions were identified. Major-level examples in the compiled data are bupropion, lorcaserin, diethylpropion, dolasetron, palonosetron and phentermine. Moderate-level examples include aspirin, morphine, epinephrine, clarithromycin, aprepitant and famotidine.

**Literature-reported safety signals.** Withdrawal and discontinuation syndrome, cardiovascular toxicity, hyponatraemia, mania, delirium, ecchymosis and bleeding events. Use in children and adolescents carries a suicidality warning.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label text was not available.

---

## Conclusion and Next Steps

**Decision: Hold for ranks 1 to 4 and 7. Proceed with Guardrails for OCD. Research Question for dysthymic disorder, melancholia, neurotic depression and agoraphobia.**

**Rationale:**
- The highest-scoring predictions (Ohdo syndrome, ligneous conjunctivitis, childhood apraxia of speech) have no mechanistic link or evidence and should not be pursued.
- Dysthymic disorder, melancholia and neurotic depression sit within the depression spectrum already served by venlafaxine, so they are indication extensions rather than novel repurposing. Dysthymia has the strongest direct evidence (L2), though it comes mainly from open-label and class-level studies.
- OCD has double-blind comparative data, but the only Phase 3 trial listed is a paediatric trial that does not test venlafaxine, so L1 is not supported.

**To proceed, the following is needed:**
- Mechanism of action data and TGA Product Information warnings and contraindications (both are data gaps)
- The approved indication text for ARTG 14402B, to confirm which conditions are already covered
- Venlafaxine-specific placebo-controlled RCTs in dysthymia
- Results of NCT04539951 for OCD
- A cardiovascular, hepatic and interaction monitoring plan, given the safety signals above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

