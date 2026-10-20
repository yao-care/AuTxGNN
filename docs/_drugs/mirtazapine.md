---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mirtazapine: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy", "ligneous conjunctivitis", "childhood apraxia of speech", "dysthymic disorder", "agoraphobia", "phobic disorder", "melancholia"]
---

# Mirtazapine
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

# Mirtazapine: From Depression to Dysthymic Disorder

## One-Sentence Summary

Mirtazapine is an antidepressant originally used for major depressive disorder and anxiety disorders.
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (persistent depressive disorder), with **1 registered clinical trial (indirect relevance only)** and **10 publications** currently supporting this direction.
Many of the other top-ranked predictions have no supporting evidence at all, so this report focuses on the best-supported prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (knowledge graph indications; the ARTG indication text is not available) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L3 (observational and open-label data plus a class-level meta-analysis; no mirtazapine-specific Phase 3 RCT. The data compiled for this report assigned L2, but that is not supported by the trial data.) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked predictions:** The highest-scoring predictions (Ohdo syndrome and variants, 99.42%; blepharophimosis-intellectual disability syndrome, Ohdo type, 99.11%; benign paroxysmal torticollis of infancy, 99.11%; ligneous conjunctivitis, 98.94%; childhood apraxia of speech, 98.70%) have no trials or publications and no identifiable mechanistic link. They are Level L5 and should be put on **Hold**. Dysthymic disorder is the best-supported prediction and is the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mirtazapine is a noradrenergic and specific serotonergic antidepressant (alpha-2 antagonism, 5-HT2/5-HT3 blockade, H1 antagonism). Its efficacy in major depressive disorder is established, and mechanistically it may be applicable to dysthymia.

Dysthymic disorder is a chronic, lower-grade form of depression on the same clinical spectrum as major depression. The pharmacology that treats major depression is therefore directly relevant. The literature includes a dedicated mirtazapine-in-dysthymia study, a placebo-controlled meta-analysis of antidepressants in dysthymia, and treatment algorithms for chronic depression.

An important caveat: the meta-analysis covers the antidepressant class rather than mirtazapine specifically. The mirtazapine-specific dysthymia study is a small open-label series of 15 patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | Compared three treatments for depressed teenagers who had attempted suicide (TASA). The population and endpoint (suicidality) differ from dysthymia, and mirtazapine is not clearly tested, so relevance is indirect. |

No ANZCTR trials were identified in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Efficacy of antidepressants in dysthymia from placebo-controlled randomised trials (class-level, not mirtazapine-specific) |
| [36999619](https://pubmed.ncbi.nlm.nih.gov/36999619/) | 2023 | Systematic review | Cochrane Database Syst Rev | Antidepressants for depression in people with cancer |
| [10569129](https://pubmed.ncbi.nlm.nih.gov/10569129/) | 1999 | Open-label case series | Depress Anxiety | Mirtazapine 15 to 45 mg in patients with dysthymic disorder |
| [11310816](https://pubmed.ncbi.nlm.nih.gov/11310816/) | 2001 | Review/algorithm | J Clin Psychiatry | Treatment algorithm for chronic depression, including dysthymia |
| [10446741](https://pubmed.ncbi.nlm.nih.gov/10446741/) | 1999 | Review | J Clin Psychiatry | Mirtazapine in indications beyond depression |
| [18833439](https://pubmed.ncbi.nlm.nih.gov/18833439/) | 2008 | Case report | Rev Bras Psiquiatr | Venlafaxine plus mirtazapine for "double depression" (major depression with dysthymia) |
| [9671349](https://pubmed.ncbi.nlm.nih.gov/9671349/) | 1998 | Case report | J Clin Psychiatry | Hypomania with mirtazapine augmentation of sertraline (safety signal) |
| [21057250](https://pubmed.ncbi.nlm.nih.gov/21057250/) | 2010 | Case report | J Clin Psychopharmacol | Delayed-onset mirtazapine-related leukopenia and rechallenge (safety signal) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14369G | MIRTANZA ODT | Tablet 15 mg (orally disintegrating) | Not available in the compiled data |

---

## Safety Considerations

Safety label text (warnings and contraindications) was not available. Please refer to the TGA-approved Product Information (PI) for safety information.

Supplementary information from the data compiled for this report:

- **Knowledge-graph contraindication signals** (not label text): epilepsy, manic bipolar affective disorder, liver disease, impaired renal function, neutropenia, agranulocytosis, hypotension and orthostatic hypotension, serotonin syndrome, drug-induced akathisia, cerebrovascular disease and stroke, myocardial infarction, and obesity-related conditions. These should be verified against the PI.
- **Drug interactions:** 100 interactions were identified. Those classified as **Major** among the 20 listed are bupropion, lorcaserin, dolasetron and palonosetron. Moderate interactions include cimetidine, clarithromycin, morphine, dexamethasone, levofloxacin and aprepitant, among others.
- **Literature safety signals:** reports of leukopenia, hypomania with augmentation, pancreatitis and arthralgia.
- **Paediatric use:** antidepressants carry suicidality warnings in young people, which is relevant given that the only listed trial involves adolescents.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dysthymia sits on the same spectrum as mirtazapine's established indication, and there is dedicated literature, though it is small-scale and mostly open-label or class-level. There is no mirtazapine-specific Phase 3 RCT, so the evidence is moderate rather than confirmatory.

**To proceed, the following is needed:**
- A randomised, placebo-controlled trial of mirtazapine specifically in dysthymia or persistent depressive disorder
- Mechanism of action data and the ARTG indication text and PI safety information (the compiled data has gaps here)
- A safety monitoring plan covering haematological monitoring (leukopenia and agranulocytosis), hypomania or mania screening, and the major drug interactions
- Clarification of whether this use is already covered by the existing depression indication, since related predictions (melancholia, neurotic depression) are essentially on-label and are not true repurposing opportunities

**Other predictions in this dataset:**
- Phobic disorder (social anxiety): two small randomised placebo-controlled studies exist, but confirmatory Phase 3 evidence is lacking. Treat as a research question.
- Agoraphobia: only open-label and pilot data in panic disorder. Treat as a research question.
- Melancholia and neurotic depression: effectively on-label. Hold.
- Ohdo syndrome (both entries), benign paroxysmal torticollis of infancy, ligneous conjunctivitis and childhood apraxia of speech: no evidence or mechanistic link. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

