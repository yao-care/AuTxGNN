---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "Malan overgrowth syndrome"]
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Clozapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Clozapine: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic with a broad receptor-blocking profile and is currently marketed in Australia.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, particularly treatment-resistant mania.
This direction is supported by **1 completed Phase 2 double-blind trial** and a **2020 systematic review and meta-analysis** of clozapine in bipolar disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The literature describes clozapine as antagonising dopamine D2/D4, serotonin 5-HT2A, muscarinic, histamine and adrenergic receptors. This broad profile is consistent with antimanic and mood-stabilising effects in treatment-resistant mania.

Many people with mania do not respond adequately to conventional treatment or cannot tolerate effective doses. The Phase 2 trial protocol describes clozapine as a possible alternative for this group. The very high TxGNN score (0.9995) points in the same direction. It is a model output, not clinical proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of the safety and efficacy of clozapine in treatment-resistant mania (2002–2005). Results are not provided in the compiled data, and the sample is small. |

No ANZCTR identifiers were found in the compiled data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic review / meta-analysis | J Psychiatr Res | Assesses the clinical efficacy and adverse effect profile of clozapine in bipolar disorder |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disord | Evaluates the efficacy and safety of clozapine in treatment-resistant bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort / effectiveness study | Lancet Psychiatry | Nationwide and meta-analytic comparison of clozapine's effectiveness and safety across psychiatric disorders, including affective disorders |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disord | Summarises current knowledge on clozapine in bipolar disorder and future research needs |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based options for managing a manic episode, including mood stabiliser and antipsychotic choice |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Mol Psychiatry | Inadequate response in acute mania and maintenance treatment remains a problem, which frames the case for further options |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bull Menninger Clin | Treatment-resistant bipolar disorder. Most newer options rest on case reports and case series |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Dosing / DDI modelling study | Drug Des Devel Ther | Clozapine drug interactions and individualised dosing in bipolar disorder |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series / review | Clin Neuropharmacol | 36 patients given combined ECT and clozapine. 67% benefited, and adverse reactions occurred in 16.6% |
| [9448668](https://pubmed.ncbi.nlm.nih.gov/9448668/) | 1998 | Review | J Clin Psychiatry | Reviews the role of antipsychotics, including clozapine, in bipolar disorder |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10288L | Clopine 200 | Tablet 200 mg | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. The major-level interactions in the first 20 listed are **bupropion**, **morphine** and **potassium citrate**. Many moderate-level interactions are also listed, for example with metformin, pioglitazone, other antidiabetic agents, atropine, hyoscyamine, glycopyrronium, loperamide, omeprazole, cimetidine, famotidine and epinephrine.
- **Points raised in the compiled literature**: the literature on clozapine and the guardrails noted for this indication point to agranulocytosis (absolute neutrophil count monitoring), metabolic effects, cardiac toxicity including myocarditis, and seizure risk.

No label warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind trial and a 2020 systematic review and meta-analysis directly address clozapine in bipolar disorder and mania. The trial is small, its results are not available in the compiled data, and clozapine carries serious known risks.

**To proceed, the following is needed:**
- Published results of NCT00029458 and critical appraisal of the 2020 meta-analysis
- Larger, adequately powered randomised trials in adult mania
- Detailed mechanism of action data
- Label warnings and contraindications from the current TGA-approved PI
- A monitoring plan covering neutrophil counts, metabolic and cardiac risk, seizure risk and interacting medicines

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

