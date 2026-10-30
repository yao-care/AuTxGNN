---
layout: default
title: Fluvoxamine
parent: Model Prediction Only (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Fluvoxamine"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
description: "Fluvoxamine: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Fluvoxamine
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

## Fluvoxamine: Paranoid personality disorder
{: .text-alpha }

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) originally used for obsessive-compulsive disorder (OCD), social phobia and other phobic disorders.
The TxGNN model predicts it may be effective for **paranoid personality disorder** (highest-ranked prediction), but there are **no registered clinical trials** and only **2 indirect publications** supporting this prediction.
Better-supported predictions in the same report are **agoraphobia** (L1), **anxiety disorder** (L1) and **endogenous depression** (L2); these are reviewed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

**Other predictions evaluated**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Paranoid personality disorder | 1.0000 | L5 | Hold |
| 2 | Schizotypal personality disorder | 1.0000 | L5 | Hold |
| 3 | Schizoid personality disorder | 1.0000 | L5 | Hold |
| 4 | Histrionic personality disorder | 1.0000 | L5 | Hold |
| 5 | Anxiety disorder | 0.9997 | L1 | Proceed with Guardrails |
| 6 | Agoraphobia | 0.9997 | L1 | Proceed with Guardrails |
| 7 | Benign paroxysmal torticollis of infancy | 0.9997 | L5 | Hold |
| 8 | Dependent personality disorder | 0.9990 | L5 | Hold |
| 9 | Narcissistic personality disorder | 0.9989 | L5 | Hold |
| 10 | Endogenous depression | 0.9985 | L2 | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, fluvoxamine is an SSRI (with sigma-1 receptor agonist activity noted in the literature). Its efficacy in OCD and social anxiety disorder is established, and mechanistically serotonergic modulation may be applicable to other anxiety-spectrum and mood conditions.

**Paranoid personality disorder (top-ranked prediction).** The TxGNN score is very high, but the link is weak. The two retrieved papers concern personality traits in body dysmorphic disorder and psychiatric side effects of alpha-interferon. Neither tests fluvoxamine in paranoid personality disorder. Any serotonergic rationale is speculative, so this prediction should be treated as a hypothesis only.

**Better-supported predictions.**
- **Anxiety disorder and agoraphobia:** SSRIs are established for anxiety-spectrum disorders. Fluvoxamine has double-blind placebo-controlled trials in panic disorder with or without agoraphobia, and network meta-analyses cover panic disorder, social anxiety disorder and OCD. Caveat: OCD and social phobia are already original indications, so part of this is an extension within the existing label class. Generalised anxiety disorder and panic disorder are the true repurposing targets.
- **Endogenous (melancholic) depression:** Fluvoxamine inhibits serotonin reuptake, the shared mechanism of SSRIs in major depression. Network meta-analyses of antidepressants include fluvoxamine, but melancholia-specific evidence is limited to one Phase 2 trial with unknown status.
- **Other personality disorders and benign paroxysmal torticollis of infancy:** Evidence is absent or indirect (comorbidity reports, OCD augmentation studies, case reports). There is no plausible mechanistic basis for the infant condition, and SSRI use in infants raises safety concerns.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (paranoid personality disorder), or for schizotypal, schizoid, histrionic, dependent or narcissistic personality disorders, agoraphobia, or benign paroxysmal torticollis of infancy. Currently no related clinical trials registered for these.

Trials are available for **anxiety disorder** and **endogenous depression** (up to 10 most relevant shown; no ANZCTR identifiers were available).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01933919](https://clinicaltrials.gov/study/NCT01933919) | Phase 3 | Completed | 38 | Fluvoxamine vs placebo in paediatric/adolescent OCD (10-week efficacy, then long-term safety); OCD overlaps with the existing indication |
| [NCT00000389](https://clinicaltrials.gov/study/NCT00000389) | Phase 3 | Completed | Not reported | RUPP study of fluvoxamine in children with anxiety disorders (generalised anxiety, social phobia, separation anxiety) |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT added to serotonin reuptake inhibitor treatment in paediatric OCD partial responders; not fluvoxamine-specific |
| [NCT04160377](https://clinicaltrials.gov/study/NCT04160377) | Phase 2 | Unknown | 150 | Fluvoxamine for melancholia, with MRI, cytokine, gut flora and neuropsychological measures; no results available |
| [NCT00352768](https://clinicaltrials.gov/study/NCT00352768) | Phase 4 | Terminated | 20 | Post-marketing placebo-controlled study of fluvoxamine in paediatric OCD; terminated early, limited value |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Exposure and response prevention with SSRIs in OCD; not fluvoxamine-specific |
| [NCT00012584](https://clinicaltrials.gov/study/NCT00012584) | NA | Completed | 120 | Stimulant with or without fluvoxamine in youth with ADHD and anxiety disorders |
| [NCT02194075](https://clinicaltrials.gov/study/NCT02194075) | Phase 4 | Completed | 60 | Methylphenidate augmentation in OCD patients receiving fluvoxamine |
| [NCT04539951](https://clinicaltrials.gov/study/NCT04539951) | Phase 2 | Recruiting | 1600 | Pragmatic trial of switching and augmentation strategies after unsatisfactory initial OCD treatment |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | Completed | 43 | Gut microbiota in OCD before and after SSRI treatment; not an efficacy trial |

## Literature Evidence

**Paranoid personality disorder (top-ranked prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort | Comprehensive Psychiatry | Personality disorders and traits in 148 people with body dysmorphic disorder (26 in a fluvoxamine study); no treatment evidence for personality disorders |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encephale | Psychiatric complications of alpha-interferon; not related to fluvoxamine |

**Agoraphobia and anxiety disorder (strongest evidence)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Pharmacological treatments for panic disorder in adults |
| [7726307](https://pubmed.ncbi.nlm.nih.gov/7726307/) | 1995 | RCT | Am J Psychiatry | Fluvoxamine, placebo and psychological panic management combined with exposure in panic disorder with agoraphobia |
| [8927663](https://pubmed.ncbi.nlm.nih.gov/8927663/) | 1996 | RCT | Psychopharmacol Bull | Double-blind comparison of fluvoxamine, imipramine and placebo in panic disorder with or without agoraphobia (n=54) |
| [40143130](https://pubmed.ncbi.nlm.nih.gov/40143130/) | 2025 | Overview of systematic reviews | Pharmaceuticals (Basel) | Efficacy of fluvoxamine in anxiety disorders and OCD |
| [29995828](https://pubmed.ncbi.nlm.nih.gov/29995828/) | 2018 | Meta-analysis | Medicine | Efficacy and tolerability of fluvoxamine in adults with social anxiety disorder |
| [32039743](https://pubmed.ncbi.nlm.nih.gov/32039743/) | 2020 | Network meta-analysis | Acta Neuropsychiatrica | Pharmacological treatments for social anxiety disorder in adults |
| [27318812](https://pubmed.ncbi.nlm.nih.gov/27318812/) | 2016 | Systematic review / network meta-analysis | Lancet Psychiatry | Pharmacological and psychological interventions for adult OCD |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | SSRIs, including fluvoxamine, superior to placebo in panic disorder and agoraphobia |
| [8227490](https://pubmed.ncbi.nlm.nih.gov/8227490/) | 1993 | Clinical study | J Clin Psychopharmacol | Fluvoxamine vs placebo in 50 patients with panic disorder (8-week double-blind) |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guideline | Clin Pharmacol Ther | CPIC guideline on CYP2D6, CYP2C19, CYP2B6, SLC6A4 and HTR2A genotypes and SSRI dosing |

**Endogenous depression**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network meta-analysis | Lancet | Comparative efficacy and acceptability of 21 antidepressants in adult major depression |
| [18562407](https://pubmed.ncbi.nlm.nih.gov/18562407/) | 2009 | Meta-analysis | J Psychopharmacol | Efficacy, tolerability and side effects of fluvoxamine in major depression |
| [6215443](https://pubmed.ncbi.nlm.nih.gov/6215443/) | 1982 | Randomised double-blind study | J Affect Disord | Fluvoxamine vs chlorimipramine in endogenous depression (n=30); fluvoxamine numerically superior, not statistically significant |

**Schizotypal personality disorder (indirect evidence only)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1970224](https://pubmed.ncbi.nlm.nih.gov/1970224/) | 1990 | Cohort | Am J Psychiatry | Neuroleptic added to fluvoxamine-refractory OCD; response linked to comorbid tics or schizotypal personality disorder |
| [11063782](https://pubmed.ncbi.nlm.nih.gov/11063782/) | 2000 | Open-label trial | Psychiatry Research | Olanzapine augmentation in fluvoxamine-refractory OCD (12 weeks) |
| [14999178](https://pubmed.ncbi.nlm.nih.gov/14999178/) | 2004 | Case report | CNS Spectrums | Compulsive hoarding with schizotypal personality disorder treated with a multi-drug regimen including fluvoxamine |

Literature for schizoid and narcissistic personality disorders is limited to the same body dysmorphic disorder paper (PMID 10929788). For dependent personality disorder, one study (PMID 12496948, 2003) shows fluvoxamine reduced HPA-axis responsiveness in borderline personality disorder, which is not the predicted condition. There is no literature for histrionic personality disorder or benign paroxysmal torticollis of infancy.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14314J | Luvox | Tablet containing fluvoxamine maleate 100 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications / conditions of concern (not label text):** epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disorders, neuroleptic malignant syndrome, syndrome of inappropriate ADH secretion (including the nephrogenic form), and serotonin syndrome.

**Drug Interactions:** 100 interactions were identified. Examples include:
- **Major:** alosetron, bupropion, diethylpropion, dolasetron
- **Moderate:** rabeprazole, aprepitant, acetylsalicylic acid, clarithromycin, chlorpropamide, pioglitazone, morphine, eliglustat, eluxadoline, dronabinol, and several corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone, dexamethasone)

The literature also reports a fluvoxamine-methadone interaction with symptomatic methadone toxicity (PMID 10197892) and seizures with combined levomepromazine and fluvoxamine (PMID 8473723). Fluvoxamine inhibits CYP1A2 and CYP2C19, so the interaction burden is high.

Other points from the literature: suicidality monitoring (particularly in paediatric patients), sweating, gastrointestinal adverse effects, sexual dysfunction, and genotype-guided dosing (CPIC).

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold for paranoid personality disorder (top-ranked prediction); Proceed with Guardrails for agoraphobia, anxiety disorder and endogenous depression**

**Rationale:**
- The top-ranked prediction (paranoid personality disorder) rests on a computational score alone (L5), with no trials and no direct literature. The other personality disorder predictions and benign paroxysmal torticollis of infancy are likewise unsupported (L4/L5).
- Agoraphobia and anxiety disorder have L1 support from placebo-controlled trials and meta-analyses, though OCD and social phobia are already original indications. Endogenous depression is L2, with one unresolved Phase 2 trial.

**To proceed, the following is needed:**
- Mechanism of action data (not available in the data compiled for this report)
- The TGA Product Information, including the approved indication text, warnings and contraindications for Luvox (ARTG 14314J), and a check on the PBS listing
- For paranoid personality disorder, any direct clinical evidence before further consideration
- For agoraphobia and anxiety disorder, confirmation of the generalised anxiety and panic disorder evidence under current standards, as the pivotal trials are largely from the 1990s
- For endogenous depression, results of NCT04160377 or other melancholia-specific data
- A guardrail plan: low-dose initiation, suicidality monitoring (especially in children and adolescents), CYP1A2/CYP2C19 interaction screening, and pharmacogenetic dosing guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

