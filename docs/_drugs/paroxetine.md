---
layout: default
title: Paroxetine
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Paroxetine: predicted new indication Top-ranked: Ohdo syndrome and variants . Best-supported: Agoraphobia (evidence level L5). Approved use: Not stated in the Australian licence data. The knowledge g…"
---

# Paroxetine
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

# Paroxetine: From Major Depressive Disorder and Anxiety Disorders to Agoraphobia

## One-Sentence Summary

Paroxetine is a selective serotonin reuptake inhibitor (SSRI) originally used for depression and anxiety-related disorders, including major depressive disorder, obsessive-compulsive disorder, social phobia and post-traumatic stress disorder.
The TxGNN model's top-ranked prediction is **Ohdo syndrome and variants**, which has no supporting evidence. The best-supported prediction is **Agoraphobia**, with **2 clinical trials** and **19 publications** behind it.
This report covers the top-ranked prediction in the Quick Overview, then focuses on agoraphobia, the most clinically credible candidate. The depression-related predictions (melancholia, neurotic depression) are near-label rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence data. The knowledge graph lists anxiety disorder, dysthymic disorder, major depressive disorder, PTSD, social phobia, OCD and others |
| Predicted New Indication | Top-ranked: Ohdo syndrome and variants (rank 1). Best-supported: Agoraphobia (rank 6) |
| TxGNN Prediction Score | Ohdo syndrome and variants: 99.11%; Agoraphobia: 97.76% |
| Evidence Level | Ohdo syndrome: L5; Agoraphobia: L1 (the grade rests largely on panic disorder evidence) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Ohdo syndrome: Hold; Agoraphobia: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, paroxetine is a potent and selective inhibitor of presynaptic serotonin reuptake, and its efficacy in depression and anxiety disorders is well established.

**Agoraphobia:** It commonly co-occurs with panic disorder, and paroxetine is already approved for panic disorder and other anxiety disorders. Serotonergic modulation of fear and anxiety circuits (amygdala, prefrontal cortex) provides a plausible mechanism. The evidence is mostly in panic disorder with or without agoraphobia rather than agoraphobia alone, so this is a near-label use rather than a true repurposing.

**Ohdo syndrome and variants (rank 1 and rank 3):** No mechanistic link has been established. This is a rare genetic disorder (KAT6B-related), and the high score is a graph-based prediction only, with no trials or literature. It should not be pursued on current evidence.

**Other predictions:** Melancholia and neurotic depression are subtypes or relatives of already-approved depressive indications. The remaining predictions (benign paroxysmal torticollis of infancy and the paranoid, schizotypal, histrionic and schizoid personality disorders) have no or very weak evidence and are held.

---

## Clinical Trial Evidence

Trials for agoraphobia (rank 6):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000368](https://clinicaltrials.gov/study/NCT00000368) | Phase 3 | Completed | 379 | Long-term strategies for panic disorder, including maintenance cognitive behaviour therapy (CBT) and medication for non-responders. Paroxetine-specific arms are not confirmed in the data |
| [NCT02852577](https://clinicaltrials.gov/study/NCT02852577) | Phase 4 | Completed | 120 | Open, naturalistic randomised trial of clonazepam versus paroxetine in panic disorder with or without agoraphobia |

For melancholia (rank 2), one Phase 4 completed trial exists: [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) (n=53), which examined decision-making in major depression. It is not an efficacy trial in melancholia.

No clinical trials are registered for Ohdo syndrome, neurotic depression or the other predictions. No ANZCTR identifiers were available in the compiled data.

---

## Literature Evidence

Selected publications for agoraphobia (rank 6), prioritising RCTs, then reviews:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine and cognitive therapy in panic disorder with or without agoraphobia |
| [19958308](https://pubmed.ncbi.nlm.nih.gov/19958308/) | 2010 | RCT | Acta Psychiatr Scand | Paroxetine and CBT for late-life panic disorder with or without agoraphobia |
| [21344132](https://pubmed.ncbi.nlm.nih.gov/21344132/) | 2011 | Randomised trial | Braz J Med Biol Res | 8-week open-label comparison of clonazepam and paroxetine in panic disorder |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Pharmacological treatments for panic disorder in adults |
| [37676054](https://pubmed.ncbi.nlm.nih.gov/37676054/) | 2023 | Systematic review | Expert Rev Neurother | Pharmacological management of panic disorder in older patients |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Paroxetine was the first SSRI approved for panic disorder with or without agoraphobia; more effective than placebo in reducing panic attacks |
| [9707160](https://pubmed.ncbi.nlm.nih.gov/9707160/) | 1998 | Review | J Clin Psychiatry | Differential efficacy of tricyclics, paroxetine and benzodiazepines in panic disorder |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | SSRIs, including paroxetine, were superior to placebo in panic disorder and agoraphobia |
| [19698676](https://pubmed.ncbi.nlm.nih.gov/19698676/) | 1998 | Article | Eur Psychiatry | Panic disorder in Australia; paroxetine was the first SSRI used for it |
| [40357765](https://pubmed.ncbi.nlm.nih.gov/40357765/) | 2025 | Systematic review | Epidemiol Psychiatr Sci | Post-acute withdrawal syndrome after stopping antidepressants |

For melancholia, a worldwide paroxetine database meta-analysis ([1487627](https://pubmed.ncbi.nlm.nih.gov/1487627/), 1992) found paroxetine significantly superior to placebo (178 treated, 66 placebo patients). For neurotic depression, a meta-analysis of 39 randomised trials ([11354239](https://pubmed.ncbi.nlm.nih.gov/11354239/), 2001) found paroxetine comparable to tricyclic antidepressants in major depression.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14367E | Aropax | Tablet 20 mg (as hydrochloride) | Not available in the compiled data |

---

## Cytotoxicity

Not applicable. Paroxetine is not an antineoplastic drug, so this section is omitted.

---

## Safety Considerations

Warnings and contraindications from the product label were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Contraindication-related conditions (knowledge graph, not label text):** epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, syndrome of inappropriate ADH secretion (including the nephrogenic form), serotonin syndrome and drug-induced akathisia.

**Drug interactions:** 100 interactions were identified. Those listed in the compiled data (partial list) include:
- **Major:** bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron, phentermine
- **Moderate:** morphine, acetylsalicylic acid (aspirin), chlorpropamide, cimetidine, clarithromycin, glimepiride, repaglinide, dronabinol, eluxadoline, and several bowel preparations
- **Minor:** aprepitant

**Literature-reported safety signals:** antidepressant discontinuation or withdrawal symptoms, sweating, galactorrhoea and hypersensitivity skin reactions (case reports).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (agoraphobia); Hold (Ohdo syndrome and variants)**

**Rationale:**
- Agoraphobia is supported by one completed Phase 3 trial, one completed Phase 4 randomised trial, RCTs and a Cochrane network meta-analysis, mostly in panic disorder with or without agoraphobia. It is a near-label use. Only one Phase 3 trial is listed and its paroxetine-specific arms are unconfirmed, so L1 is a generous grade.
- The top-ranked Ohdo syndrome prediction has a high model score but no trials, no literature and no plausible mechanism, so it is held.

**To proceed, the following is needed:**
- Product label warnings and contraindications (a blocking data gap), obtained from the TGA-approved PI
- Approved indication text for the Australian ARTG entry, to confirm how much of this use is already on-label
- Detailed mechanism of action data
- Confirmation of paroxetine-specific arms in NCT00000368
- A discontinuation and withdrawal management plan, plus interaction screening for serotonergic and CYP2D6-interacting drugs
- Review of the knowledge graph contraindications (for example bipolar disorder and bleeding disorders) before prescribing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

