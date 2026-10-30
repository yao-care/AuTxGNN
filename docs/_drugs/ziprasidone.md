---
layout: default
title: Ziprasidone
parent: Model Prediction Only (L5)
nav_order: 793
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Ziprasidone: predicted new indication Trichotillomania (evidence level L2). Approved use: Manic bipolar affective disorder, bipolar disorder, schizophrenia"
monitor_inn: "Ziprasidone"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "major affective disorder", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
---

# Ziprasidone
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

## Ziprasidone: From Bipolar Disorder and Schizophrenia to Trichotillomania
{: .text-alpha }

## One-Sentence Summary

Ziprasidone is an atypical antipsychotic originally used for schizophrenia and manic episodes of bipolar disorder.
The TxGNN model predicts it may be effective for **major affective disorder** (the depression-focused indication that is the strongest-supported prediction among its top candidates), with **7 clinical trials** and **20 publications** currently supporting this direction.

Note: the top-ranked TxGNN prediction (trichotillomania, score 0.9983) has no supporting trials or literature. This report therefore focuses on the best-evidenced candidate, major affective disorder (rank 3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Manic bipolar affective disorder, bipolar disorder, schizophrenia (the ARTG entry carries no indication text) |
| Predicted New Indication | Major affective disorder (rank 3; rank 1 was trichotillomania, with no evidence) |
| TxGNN Prediction Score | 0.9966 (rank 1 trichotillomania: 0.9983) |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ziprasidone antagonises D2 and 5-HT2A receptors, acts as a 5-HT1A agonist, and inhibits serotonin and noradrenaline reuptake. This profile gives a plausible rationale for mood effects.

Ziprasidone is already used for bipolar mania and mixed episodes, so mood disorders are a natural extension. Several placebo-controlled Phase 2 trials have tested it in depressive and mixed states and as an adjunct to SSRIs in major depressive disorder. Systematic reviews and network meta-analyses also examine antipsychotic augmentation in treatment-resistant depression.

Caveats: the indication overlaps with the existing bipolar labelling, so the novel element is mainly unipolar or adjunctive depression. Results of the Phase 2 trials are not summarised in the data compiled, so efficacy conclusions remain unverified.

Other predictions with some support: **Tourette syndrome** (rank 7, score 0.9963, evidence level L3) has a small paediatric pilot study (PMID 10714048) and reviews, and D2 antagonism is the established basis for tic suppression. The remaining top-10 predictions (e.g. hydranencephaly, glycosylation disorders, X-linked myopias, retinal dystrophy, polymicrogyria) have no identifiable mechanistic link or clinical evidence; their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00633399](https://clinicaltrials.gov/study/NCT00633399) | Phase 2 | Completed | 458 | Three-phase study of ziprasidone added to an SSRI in MDD with inadequate SSRI response; no results summarised |
| [NCT00555997](https://clinicaltrials.gov/study/NCT00555997) | Phase 2 | Completed | 120 | 12-week randomised, double-blind, placebo-controlled trial of ziprasidone in MDD, with HAM-D-17 as the outcome |
| [NCT00490542](https://clinicaltrials.gov/study/NCT00490542) | Phase 2 | Completed | 73 | Double-blind, placebo-controlled trial in depressive mixed state |
| [NCT00340379](https://clinicaltrials.gov/study/NCT00340379) | Phase 2/3 | Completed | 72 | Ziprasidone monotherapy vs sertraline plus haloperidol in psychotic major depression |
| [NCT01168674](https://clinicaltrials.gov/study/NCT01168674) | Phase 4 | Completed | 49 | 13-week double-blind, placebo-controlled crossover study of predictors of response to ziprasidone augmentation in MDD |
| [NCT00237666](https://clinicaltrials.gov/study/NCT00237666) | Phase 4 | Completed | 30 | Open-label, flexible-dose trial in bipolar II major depression |
| [NCT00421954](https://clinicaltrials.gov/study/NCT00421954) | Phase 3 | Completed | 8 | Open-label feasibility study in adolescents with psychotic disorder; too small to support efficacy |

No ANZCTR identifiers were available in the data compiled.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic review/NMA | J Affect Disord | Compares augmentation agents for treatment-resistant depression |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic review/meta-analysis | Psychol Med | Efficacy and tolerability of antipsychotics as monotherapy and adjunct in adult MDD |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematic review/meta-analysis | J Psychopharmacol | Antidepressants plus second-generation antipsychotics vs esketamine vs lithium in major depression |
| [40808264](https://pubmed.ncbi.nlm.nih.gov/40808264/) | 2025 | Systematic review | Bipolar Disord | Pharmacological treatments for MDD and bipolar depression with mixed features |
| [27835715](https://pubmed.ncbi.nlm.nih.gov/27835715/) | 2017 | Randomised controlled trial (RCT) | J Clin Psychiatry | Cardiac, endocrine, metabolic and motor effects of ziprasidone added to escitalopram in MDD |
| [27306192](https://pubmed.ncbi.nlm.nih.gov/27306192/) | 2016 | Post-hoc analysis of RCT | Int Clin Psychopharmacol | Ziprasidone augmentation showed an anxiolytic effect in anxious depression |
| [26619770](https://pubmed.ncbi.nlm.nih.gov/26619770/) | 2015 | Review | Am J Psychiatry | Adjunctive ziprasidone in major depression and the status of adjunctive atypical antipsychotics |
| [19040553](https://pubmed.ncbi.nlm.nih.gov/19040553/) | 2008 | Review | CNS Neurosci Ther | Ziprasidone in affective disorders; limited metabolic side effects reported |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia Pac Psychiatry | Antipsychotics as antidepressants, effective at sub-antipsychotic doses |
| [32512768](https://pubmed.ncbi.nlm.nih.gov/32512768/) | 2020 | Review | Pharmaceuticals (Basel) | Pharmacological options for treatment-resistant depression |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9070J | ZIPROX | Capsule 20 mg (as hydrochloride), oral | Not recorded in the data compiled |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for full safety information.

The following come from a knowledge graph and drug-interaction database, not from label text:

- **Knowledge-graph contraindication signals** include: long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, orthostatic hypotension, neutropenia, agranulocytosis, epilepsy, liver failure, kidney disease, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, obesity, potassium deficiency, and breast carcinoma.
- **Drug interactions:** 100 interactions were identified. Those rated **Major** among the first 20 listed include hydrocortisone, amphotericin B (including the lipid complex), bupropion and morphine. Many Moderate interactions were also listed, including with metformin, pioglitazone, famotidine, epinephrine, atropine and loperamide.
- **Literature-flagged concerns:** QT prolongation (particularly in children and adolescents, PMID 39549076), somnolence and metabolic effects.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for major affective disorder). Tourette syndrome is a research question only, and all other predictions should be held.

**Rationale:**
- Several randomised, placebo-controlled Phase 2 trials, including a large one (n=458), and multiple systematic reviews support ziprasidone in depressive and mixed states. However, the trial results are not summarised in the data compiled, and the indication overlaps with the existing bipolar use. Cardiac (QT) risk requires careful controls.

**To proceed, the following is needed:**
- Published results of NCT00633399, NCT00555997 and NCT00490542 to verify efficacy
- Mechanism of action data and PI warnings and contraindications (both are data gaps)
- A baseline and follow-up ECG and electrolyte monitoring plan, and screening against the contraindication signals above
- Review of interacting medicines, particularly QT-prolonging agents and those rated Major
- Confirmation of the ARTG-approved indication wording for ZIPROX (it is blank in the data compiled)
- Paediatric cardiac safety assessment before considering any Tourette syndrome use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

