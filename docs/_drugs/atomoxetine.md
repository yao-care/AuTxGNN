---
layout: default
title: Atomoxetine
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Atomoxetine"
predicted_indications: ["specific developmental disorder", "faciodigitogenital syndrome", "chondromyxoid fibroma", "trichotillomania", "restless legs syndrome", "manic bipolar affective disorder", "Tourette syndrome", "transient tic disorder", "cerebellar ataxia", "autosomal dominant cerebellar ataxia"]
description: "Atomoxetine: predicted new indication Specific developmental disorder (evidence level L5). In Australia: 7 PBS items (7 currently listed)"
---

# Atomoxetine
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

## Atomoxetine: Specific developmental disorder
{: .text-alpha }

## One-Sentence Summary

Atomoxetine is a selective norepinephrine reuptake inhibitor marketed in Australia as an oral capsule. The TxGNN model predicts it may be useful for **specific developmental disorder**. No clinical trials and no studies directly testing this disease were found, so the evidence level is **L5 (model prediction only)**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (7 of 7 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Atomoxetine blocks the reuptake of norepinephrine. This description rests on the drug's known drug class. According to the Mechanism of Action section of the US FDA-approved prescribing information for atomoxetine: "The precise mechanism by which STRATTERA produces its therapeutic effects in ADHD is unknown, but is thought to be related to selective inhibition of the pre-synaptic norepinephrine transporter, as determined in ex vivo uptake and neurotransmitter depletion studies." ([DailyMed: Strattera (atomoxetine hydrochloride) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=309de576-c318-404a-bc15-660c2b1876fb), label version 2026-06-30; accessed 2026-11-19.)

Specific developmental disorders, such as learning disabilities, often occur alongside the neurodevelopmental condition for which atomoxetine is already used. Any benefit would most plausibly come from improved attention and executive function. It would not come from a direct effect on the underlying learning deficit.

The publications linked to this prediction study the drug's established use, including in children with autism. None of them tests atomoxetine in a specific developmental disorder. The high model score therefore reflects association patterns, not demonstrated efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below directly studies atomoxetine in specific developmental disorder. They concern the drug's established use and related comorbid conditions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Systematic review / network meta-analysis | The Lancet Psychiatry | Compared the benefits and harms of drug, psychological and neurostimulatory interventions in adults for the drug's established use |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Systematic review / meta-analysis | Autism Research | Three placebo-controlled RCTs (241 children) examined atomoxetine for attention-related symptoms in children with autism |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Review | Therapeutic Advances in Psychopharmacology | Reviewed atomoxetine efficacy in patients with common comorbid conditions across age groups |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohort (retrospective) | Neuropsychopharmacology Reports | Identified patient factors associated with atomoxetine response in adults |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Cohort | Clinical EEG and Neuroscience | Discussed quantitative EEG in childhood attention problems and learning disabilities; not a drug efficacy study |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 9092M | APO-Atomoxetine | Atomoxetine | Capsule 10 mg (as hydrochloride) | Valid |
| 9093N | APO-Atomoxetine | Atomoxetine | Capsule 18 mg (as hydrochloride) | Valid |
| 9094P | APO-Atomoxetine | Atomoxetine | Capsule 25 mg (as hydrochloride) | Valid |
| 9095Q | APO-Atomoxetine | Atomoxetine | Capsule 40 mg (as hydrochloride) | Valid |
| 9096R | APO-Atomoxetine | Atomoxetine | Capsule 60 mg (as hydrochloride) | Valid |
| 9289X | APO-Atomoxetine | Atomoxetine | Capsule 80 mg (as hydrochloride) | Valid |
| 9290Y | APO-Atomoxetine | Atomoxetine | Capsule 100 mg (as hydrochloride) | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

**Drug interactions** (100 interacting drugs recorded; main examples):
- **Major:** cisapride, dolasetron
- **Moderate:** bupropion, clarithromycin, cimetidine, famotidine, epinephrine, ephedrine, eliglustat, fenfluramine, granisetron, loperamide, isometheptene

For warnings, contraindications and other safety information, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but no clinical trial and no publication directly studies atomoxetine in specific developmental disorder. The evidence level is therefore L5. Any plausible benefit would be indirect, through attention and executive function, and has not been demonstrated.

**To proceed, the following is needed:**
- Studies that directly test atomoxetine in specific developmental disorder, with outcomes beyond attention symptoms
- Detailed mechanism-of-action data to support a mechanistic link
- Review of the TGA-approved Product Information (PI) for warnings, contraindications and interactions
- A defined target population and safety monitoring plan before any further evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description rests on the drug's known drug class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Strattera (atomoxetine hydrochloride) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=309de576-c318-404a-bc15-660c2b1876fb) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

