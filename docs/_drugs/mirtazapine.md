---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
---

# Mirtazapine
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

# Mirtazapine: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Mirtazapine is a noradrenergic and specific serotonergic antidepressant (NaSSA), internationally used for major depressive disorder. The TxGNN model's raw top-ranked outputs (e.g. Ohdo syndrome, ligneous conjunctivitis) were screened out as knowledge-graph noise with no plausible mechanistic link — the highest-ranked candidate with genuine supporting evidence is **Dysthymic Disorder (persistent depressive disorder)**, backed by **3 clinical trials** and **13 publications**, including a mirtazapine-specific open-label study and a dysthymia-specific antidepressant meta-analysis.

> **Note on prediction selection:** The Evidence Pack's top 5 ranked candidates by raw TxGNN score (Ohdo syndrome and its variants, benign paroxysmal torticollis of infancy, ligneous conjunctivitis, childhood apraxia of speech) each carry a "no evidence, no mechanistic plausibility" rationale in the source data itself and zero clinical trials or literature. Reporting on these as the lead candidate would be clinically misleading, so this report instead focuses on the highest-ranked candidate that has an evidentiary basis: dysthymic disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (per published literature; not captured in the structured `original_indications` field of this dataset — data gap) |
| Predicted New Indication | Dysthymic Disorder (Persistent Depressive Disorder) |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (no ARTG registration found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from the structured DrugBank query for this Evidence Pack (data gap). However, the accompanying literature and rationale data consistently identify mirtazapine as a NaSSA: it blocks presynaptic α2-adrenergic auto- and heteroreceptors (increasing noradrenaline and serotonin release) and antagonises postsynaptic 5-HT2A/2C and 5-HT3 receptors, with additional H1-antihistamine activity contributing to its sedative and appetite-stimulating effects.

Dysthymic disorder (persistent depressive disorder) is a chronic, low-grade form of depression that shares the same monoamine-based pathophysiology as major depressive disorder, mirtazapine's established indication. This is not a cross-mechanism extrapolation — it is a within-class extension of an already-validated pharmacological effect to a chronically milder presentation of the same disease spectrum.

This is supported directly by the evidence: an open-label study specifically testing mirtazapine 15–45 mg in dysthymic patients (PMID 10569129), and a placebo-controlled meta-analysis confirming antidepressant efficacy in dysthymia generally (PMID 21527126). The clinical trials identified are broader depression-treatment studies rather than dysthymia-specific mirtazapine trials, so they should be read as supportive context rather than direct proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | TASA trial — compared three depression treatments in adolescent suicide attempters; general depression treatment, not mirtazapine-specific or dysthymia-specific (indirect evidence) |
| [NCT04437485](https://clinicaltrials.gov/study/NCT04437485) | Phase 2 | Completed | 46 | eIMPACT-DM pilot RCT — collaborative depression care in patients with prediabetes; examined somatic symptoms (appetite, sleep) relevant to NaSSA pharmacology, but not mirtazapine-specific |
| [NCT02458690](https://clinicaltrials.gov/study/NCT02458690) | Phase 2 | Completed | 216 | eIMPACT trial — collaborative depression care in older primary-care patients to reduce cardiovascular risk; general depression treatment, not mirtazapine-specific |

*None of the above trials tested mirtazapine directly against dysthymia as the primary endpoint; they are included as broader supportive context (all graded "B" relevance in the source data).*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis (RCTs) | J Clin Psychiatry | Meta-analysis of placebo-controlled trials confirming antidepressant efficacy specifically in dysthymic disorder |
| [10569129](https://pubmed.ncbi.nlm.nih.gov/10569129/) | 1999 | Open-label cohort | Depress Anxiety | Mirtazapine 15–45 mg studied directly in 15 patients with dysthymic disorder |
| [36999619](https://pubmed.ncbi.nlm.nih.gov/36999619/) | 2023 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Review of antidepressants for depression in cancer patients, including mirtazapine class agents |
| [11310816](https://pubmed.ncbi.nlm.nih.gov/11310816/) | 2001 | Review | J Clin Psychiatry | Treatment algorithm for chronic depression, explicitly covering dysthymic disorder as a subtype |
| [18833439](https://pubmed.ncbi.nlm.nih.gov/18833439/) | 2008 | Case series | Rev Bras Psiquiatr | Venlafaxine + mirtazapine combination used for major depression with dysthymia ("double depression") |
| [26742677](https://pubmed.ncbi.nlm.nih.gov/26742677/) | 2015 | Retrospective cohort | Arch Ital Biol | Compared hypnotic efficacy of trazodone and mirtazapine in chronic insomnia (relevant to mirtazapine's sedative profile) |
| [31265070](https://pubmed.ncbi.nlm.nih.gov/31265070/) | 2019 | Cohort | J Clin Endocrinol Metab | Taiwan population-based cohort: antidepressant use, including mirtazapine, associated with reduced mortality in diabetic patients |
| [10446741](https://pubmed.ncbi.nlm.nih.gov/10446741/) | 1999 | Review | J Clin Psychiatry | Review of mirtazapine use beyond primary depression indication |
| [21057250](https://pubmed.ncbi.nlm.nih.gov/21057250/) | 2010 | Case report | J Clin Psychopharmacol | Delayed-onset leukopenia with mirtazapine and successful rechallenge (safety signal) |
| [17323021](https://pubmed.ncbi.nlm.nih.gov/17323021/) | 2007 | Review | Med Klin (Munich) | General review of depression management in family practice |

## Australia Market Information

No ARTG entries were found for mirtazapine in this dataset (0 licenses, market status: not marketed). Regulatory and product information should be confirmed directly with the TGA/ARTG database before any clinical use is considered.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications, or drug interaction data were returned for mirtazapine in this Evidence Pack (data gap), and TGA labelling data could not be retrieved.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mirtazapine's mechanism (NaSSA) is directly relevant to dysthymic disorder as a within-class extension of its approved antidepressant activity, supported by a dysthymia-specific open-label study and a dysthymia-specific efficacy meta-analysis — but no dysthymia-specific RCT of mirtazapine itself exists, and Australian regulatory/safety data are currently absent.

**To proceed, the following is needed:**
- TGA Product Information (PI) — warnings, contraindications, drug interactions (currently blocking data gap, DG001)
- Confirmed DrugBank/structured mechanism-of-action record (DG002)
- ARTG registration status confirmation, given "not marketed" status in this dataset
- A dysthymia-specific controlled trial of mirtazapine, ideally against placebo or an active comparator, to move beyond L2 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

