---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). Approved use: Schizophrenia, bipolar disorder (manic)…"
monitor_inn: "Risperidone"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder", "Tourette syndrome", "intellectual disability", "autism, susceptibility to", "chromosome 15q11.2 deletion syndrome"]
---

# Risperidone
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

# Risperidone: From Schizophrenia and Bipolar Disorder to Gaze Palsy, Familial Horizontal, with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an atypical antipsychotic originally used for schizophrenia, bipolar disorder and autism-related symptoms.
The TxGNN model's top-ranked prediction is **familial horizontal gaze palsy with progressive scoliosis**, an ultra-rare genetic disorder, but there are **0 clinical trials** and **0 publications** supporting this prediction.
Stronger evidence exists for other predicted indications, notably adjunctive use in **major affective disorder** (treatment-resistant depression) and **Tourette syndrome**, which are covered below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, bipolar disorder (manic), autism spectrum disorder (irritability) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis (top-ranked prediction) |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (top-ranked prediction); L1 for major affective disorder and intellectual disability; L2 for Tourette syndrome |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails for better-supported predictions |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, risperidone is an atypical antipsychotic that blocks dopamine D2 and serotonin 5-HT2A receptors. Its efficacy in schizophrenia and bipolar mania is established.

**For the top-ranked prediction (familial horizontal gaze palsy with progressive scoliosis):** the condition is caused by ROBO3 mutations affecting axon guidance. No plausible link to D2/5-HT2A antagonism has been identified. The high score reflects network proximity in the knowledge graph rather than a biological rationale, and it should be treated as a computational artefact until proven otherwise.

**For the better-supported predictions:**
- **Major affective disorder (adjunctive use in treatment-resistant depression):** 5-HT2A/D2 antagonism supports augmentation of antidepressants. Bipolar use is already on-label, so the net new signal is adjunctive use in unipolar depression.
- **Tourette syndrome:** D2 blockade reduces tics, consistent with the established dopaminergic hypothesis.
- **Intellectual disability:** risperidone reduces aggression and disruptive behaviour via the same receptor actions. It does not treat core cognitive impairment.

## Clinical Trial Evidence

There are no clinical trials for the top-ranked prediction. The table below lists the most relevant trials for the better-supported predictions.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Adjunctive risperidone vs placebo in major depressive disorder not responding to standard therapy |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI in treatment-resistant unipolar depression, with maintenance phase |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Risperidone augmentation in patients who failed or partly responded to an antidepressant |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Risperidone monotherapy vs placebo in bipolar disorder with anxiety (already an approved indication) |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | ECT plus risperidone vs ECT alone in treatment-resistant depression; limited interpretability |
| [NCT00004393](https://clinicaltrials.gov/study/NCT00004393) | Phase 2 | Completed | 50 | Double-blind placebo-controlled risperidone in Tourette syndrome |
| [NCT00250354](https://clinicaltrials.gov/study/NCT00250354) | Phase 3 | Completed | 110 | Risperidone vs placebo for conduct disorder in children with mild to borderline intellectual disability |
| [NCT00266552](https://clinicaltrials.gov/study/NCT00266552) | Phase 3 | Completed | 118 | Risperidone oral solution vs placebo for conduct disorder in children with intellectual disability |
| [NCT00261508](https://clinicaltrials.gov/study/NCT00261508) | Phase 3 | Completed | 80 | Risperidone vs placebo for behavioural symptoms in children with autistic disorder and other pervasive developmental disorders |
| [NCT00065273](https://clinicaltrials.gov/study/NCT00065273) | Phase 3 | Completed | 50 | Behavioural effects of atypical antipsychotics in people with intellectual disability and severe aberrant behaviour |

No ANZCTR trial identifiers were available in the data compiled for this report.

## Literature Evidence

There is no literature for the top-ranked prediction. The table below lists key publications for the better-supported predictions (systematic reviews and RCTs prioritised).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic review / network meta-analysis | J Affect Disord | Compared augmentation agents in treatment-resistant major depression |
| [35993319](https://pubmed.ncbi.nlm.nih.gov/35993319/) | 2022 | Systematic review / network meta-analysis | Psychol Med | Efficacy and acceptability of second-generation antipsychotics added to antidepressants in unipolar depression |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | 17 trials (3,807 participants) on augmenting antidepressants with atypical antipsychotics |
| [12682319](https://pubmed.ncbi.nlm.nih.gov/12682319/) | 2003 | RCT | Neurology | Placebo-controlled trial of risperidone in Tourette syndrome |
| [11799340](https://pubmed.ncbi.nlm.nih.gov/11799340/) | 2002 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled trial in 48 adolescents and adults with Tourette syndrome |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network meta-analysis | Lancet Child Adolesc Health | Comparative efficacy and tolerability of drugs for Tourette's syndrome in young people |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical guideline | Eur Child Adolesc Psychiatry | European guidelines (pharmacological treatment) for Tourette syndrome and tic disorders |
| [39690490](https://pubmed.ncbi.nlm.nih.gov/39690490/) | 2025 | Network meta-analysis | J Psychopharmacol | Pharmacotherapies for agitation in autism or intellectual disability |
| [40396498](https://pubmed.ncbi.nlm.nih.gov/40396498/) | 2025 | Network meta-analysis | Cochrane Database Syst Rev | Atypical antipsychotics for autism spectrum disorder |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case series | J Child Adolesc Psychopharmacol | Risperidone added to SRIs in three patients with SRI-refractory trichotillomania |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11869Q | APO-Risperidone | Tablet 0.5 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindicated or cautioned conditions (from knowledge graph associations, not label text):**
- Cardiovascular and cerebrovascular: myocardial infarction, stroke, cerebral infarction, heart conduction disease, sudden cardiac arrest, heart disease, orthostatic hypotension and other hypotensive disorders, postural orthostatic tachycardia syndrome, multiple system atrophy
- Metabolic: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hyperlipidaemia, obesity
- Haematological: neutropenia, agranulocytosis, haemoglobinopathy
- Hepatic and other: liver disease, liver failure, gallbladder disease, epilepsy, female breast carcinoma

**Drug interactions** (100 recorded; main examples):
- **Major:** bupropion, morphine
- **Moderate:** metformin, alogliptin, albiglutide, canagliflozin, acarbose (possible effects on glucose control); epinephrine, hydrocortisone; famotidine; amphotericin B; anticholinergics such as atropine, hyoscyamine, glycopyrronium and clidinium; loperamide, bisacodyl, lorcaserin
- **Minor:** ranitidine

**Guardrails noted for the better-supported predictions:** metabolic monitoring and weight gain, hyperprolactinaemia, and extrapyramidal symptoms, particularly in children.

## Conclusion and Next Steps

**Decision: Hold (top-ranked prediction, familial horizontal gaze palsy with progressive scoliosis)**

**Rationale:**
- The prediction has no clinical or literature support and no plausible mechanism (ROBO3-related axon guidance disorder). The high score reflects network proximity only.
- Other predicted indications are better supported: major affective disorder (adjunctive use in treatment-resistant depression; L1, two completed Phase 3 trials plus meta-analyses), intellectual disability (behavioural symptoms; L1) and Tourette syndrome (L2) are **Proceed with Guardrails**. Trichotillomania and Phelan-McDermid syndrome are research questions (L4, case reports and preclinical data only). Asperger syndrome, autism susceptibility, amelocerebrohypohidrotic syndrome and 15q11.2 deletion syndrome are Hold, since they either duplicate existing use or have no evidence.

**To proceed, the following is needed:**
- TGA Product Information (warnings, contraindications and approved indications) for risperidone products
- Detailed mechanism of action data
- For adjunctive use in depression: confirmation of the regulatory position in Australia and comparison with approved augmentation options
- For Tourette syndrome and intellectual disability: positioning against guideline-recommended first-line treatments, plus a metabolic, prolactin and extrapyramidal symptom monitoring plan for paediatric patients
- For the top-ranked prediction: no further work is recommended unless independent mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

