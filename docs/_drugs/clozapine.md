---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not available in the data compiled for this report . Published litera…"
monitor_inn: "Clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "psychotic disorder", "Malan overgrowth syndrome"]
---

# Clozapine
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

## Clozapine: From Treatment-Resistant Schizophrenia to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic marketed in Australia as an oral tablet (Clopine 200). The TxGNN model predicts it may be effective for **manic bipolar affective disorder** (score 0.9995), with **1 directly relevant completed Phase 2 trial** and **a 2020 systematic review and meta-analysis** supporting this direction. Broader bipolar disorder evidence also includes a completed paediatric Phase 3 placebo-controlled trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text). Published literature describes clozapine as established for treatment-resistant schizophrenia |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 (one completed Phase 2 double-blind trial, n=42). For bipolar disorder more broadly, a completed Phase 3 paediatric trial supports L1 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on published literature, clozapine has a broad receptor profile: dopamine D2/D4, serotonin 5-HT2A, muscarinic, histaminergic and adrenergic antagonism. This profile is consistent with antimanic and mood-stabilising effects in treatment-resistant mania.

Clozapine is established for treatment-resistant schizophrenia, and bipolar mania with psychotic features or poor response to first-line agents shares overlapping dopaminergic and serotonergic pathology. Clinical reports and a completed double-blind Phase 2 trial in treatment-resistant mania support this link, and a 2020 systematic review and meta-analysis assessed clozapine's efficacy and adverse effects in bipolar disorder.

Note that the same prediction exercise ranked "psychotic disorder" and "schizophreniform disorder" highly. These are on-label or closely related uses, which suggests the original-indication field is a data gap rather than true repurposing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind efficacy and safety study of clozapine in treatment-resistant mania |
| [NCT00036582](https://clinicaltrials.gov/study/NCT00036582) | Phase 3 | Completed | 116 | Clozapine vs placebo in treatment-refractory bipolar disorder in children and adolescents (broader bipolar evidence) |
| [NCT02562287](https://clinicaltrials.gov/study/NCT02562287) | Phase 4 | Unknown | 54 | Clozapine vs olanzapine, quetiapine or risperidone in treatment-resistant bipolar disorder |
| [NCT04580134](https://clinicaltrials.gov/study/NCT04580134) | Phase 4 | Recruiting | 524 | Randomised double-blind clozapine response trial in a biotype-defined psychosis population |
| [NCT06011460](https://clinicaltrials.gov/study/NCT06011460) | N/A | Enrolling by invitation | 30 | Observational registry of adverse events with clozapine in bipolar disorder |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1254 | Intensified pharmacological treatment after first-line failure (includes bipolar depression); results pending |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic review/Meta-analysis | J Psychiatr Res | Clinical efficacy and adverse effect profile of clozapine in bipolar disorder |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disord | Efficacy and safety of clozapine in treatment-resistant bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort/Meta-analysis | Lancet Psychiatry | Transdiagnostic effectiveness and safety of clozapine versus other antipsychotics |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disord | What is known about clozapine in bipolar disorder and future directions |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based options for managing bipolar mania |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Mol Psychiatry | Treatment-resistant bipolar disorder |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Modelling study | Drug Des Devel Ther | Clozapine drug interactions and model-informed individualised dosing in bipolar disorder |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series/Review | Clin Neuropharmacol | 36 patients on combined ECT and clozapine; 67% benefited, adverse reactions in 16.6% |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10288L | Clopine 200 | Tablet 200 mg | Not stated in the data compiled for this report |

## Cytotoxicity

Not applicable. Clozapine is not an antineoplastic drug.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Disease associations flagged by the knowledge graph** (not label text): agranulocytosis, neutropenia and leukopenia; epilepsy; orthostatic and other hypotensive disorders; coronary artery disease, heart conduction disease and sudden cardiac arrest; stroke and cerebrovascular disorders; pulmonary embolism; respiratory failure; diabetes mellitus, hyperglycaemia and diabetic ketoacidosis; hyperlipidaemia and obesity; liver and gallbladder disease; benign prostatic hyperplasia; angle-closure glaucoma; paralytic ileus.
- **Drug interactions:** 100 interactions were identified. Major interactions in the sample reviewed include bupropion, morphine and potassium citrate. Moderate interactions include antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, chlorpropamide, albiglutide), anticholinergic agents (atropine, hyoscyamine, glycopyrronium), famotidine, cimetidine, omeprazole, epinephrine, loperamide, bisacodyl and lorcaserin.
- **Literature-reported risks:** myocarditis and cardiomyopathy, seizures, metabolic effects and weight gain, somnolence, and obsessive-compulsive symptoms.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind trial in treatment-resistant mania, a completed Phase 3 paediatric bipolar trial and a 2020 meta-analysis support the prediction, and clozapine is already marketed in Australia. The mania-specific trial is small (n=42), and the serious haematological, cardiac, seizure and metabolic risks require strict controls.

**To proceed, the following is needed:**
- The ARTG-approved indication and the PI warnings and contraindications (currently missing)
- Detailed mechanism of action data
- Larger, adult-focused randomised trials in bipolar mania, as published results are limited and the Phase 3 trial was paediatric
- A monitoring plan covering absolute neutrophil count, cardiac and metabolic surveillance, seizure risk and a review of concomitant medicines
- Restriction to treatment-resistant presentations, with specialist psychiatric oversight

### Other Predicted Indications (Summary)

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|---|---|---|---|
| Bipolar disorder | 0.9962 | L1 | Proceed with Guardrails |
| Psychotic disorder | 0.9912 | L1 | Proceed with Guardrails (on-label or established use) |
| Schizophreniform disorder | 0.9969 | L2 | Proceed with Guardrails |
| Major affective disorder | 0.9948 | L2 | Research question (unipolar depression not supported) |
| Tourette syndrome | 0.9991 | L4 | Hold (case reports only) |
| Trichotillomania | 0.9990 | L5 | Hold |
| ADHD (and inattentive type) | 0.9931 / 0.9921 | L5 | Hold |
| Malan overgrowth syndrome | 0.9902 | L5 | Hold (likely a network artefact) |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

