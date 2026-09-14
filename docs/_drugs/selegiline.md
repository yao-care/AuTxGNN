---
layout: default
title: Selegiline
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
---

# Selegiline
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

Using the evidence pack directly (no additional skill needed — this is a fully-specified report-writing task). One judgment call worth flagging: TxGNN's numerically top-ranked prediction (rank 1, "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis") has zero supporting evidence and the pack itself labels it a likely embedding-similarity artefact, not a mechanistic signal. Rank 2 (schizophrenia) is the highest-ranked prediction with actual clinical trial and literature support (L2, S2, "Proceed with Guardrails"), so I've used it as the reportable candidate and noted the rank-1 anomaly separately.

---

# Selegiline: From Parkinson's Disease/Depression to Schizophrenia (Negative Symptoms Augmentation)

## One-Sentence Summary

Selegiline is a selective monoamine oxidase-B (MAO-B) inhibitor with established use in Parkinson's disease (oral) and major depressive disorder (transdermal). The TxGNN model's highest evidence-backed prediction is that selegiline, used as an add-on to antipsychotic therapy, may help improve **negative symptoms of schizophrenia**, with **1 completed clinical trial** and **20 related publications** — including three double-blind RCTs — currently supporting this direction. Note: TxGNN's single highest-scoring candidate overall was an ultra-rare congenital brain malformation with no supporting evidence; the model's own annotation flags that hit as a probable knowledge-graph embedding artefact rather than a genuine mechanistic signal, so it is not the focus of this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (oral formulation); major depressive disorder (transdermal formulation) — per literature evidence; structured DrugBank indication field was not populated in this evidence pack |
| Predicted New Indication | Schizophrenia (negative symptom augmentation to antipsychotic therapy) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Selegiline is an irreversible, selective MAO-B inhibitor. At the low oral doses used in Parkinson's disease, it selectively spares MAO-A and increases synaptic dopamine availability. At oral doses ≥20 mg/day (or via other formulations), selectivity is lost and it behaves as a non-selective MAOI. This dose-dependent dopaminergic-enhancing action is the pharmacological basis for the schizophrenia hypothesis: antipsychotics work primarily by blocking dopamine D2 receptors, which controls positive symptoms but is also thought to contribute to negative symptoms (apathy, blunted affect, social withdrawal) through a secondary, iatrogenic dopamine-deficient state in some brain regions. Low-dose selegiline added on top of antipsychotic treatment could theoretically counteract this without reversing the D2 blockade needed to control positive symptoms.

This is not a novel hypothesis invented by the model — it has been directly tested in humans. Three double-blind, placebo-controlled trials (Bodkin 1996, Bodkin 2005, Amiri 2008) examined selegiline augmentation specifically for negative symptoms in chronic schizophrenia, and a 2023 systematic review/meta-analysis (Rossano et al.) evaluated selegiline's efficacy and safety across psychiatric conditions including schizophrenia. Results across these studies have been mixed rather than uniformly positive, which is consistent with the "Proceed with Guardrails" rating rather than a stronger "Go."

A structured mechanism-of-action record from DrugBank was not available in this evidence pack (flagged as data gap DG002); the MOA description above is derived from the literature evidence supplied alongside the schizophrenia prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomised, placebo-controlled trial of selegiline augmentation of antipsychotic medication for negative symptoms in inpatients with chronic schizophrenia. |

No ANZCTR (Australian New Zealand Clinical Trials Registry) entries were identified in this evidence pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | RCT | J Nerv Ment Dis | Pilot study of low-dose selegiline (5 mg BID) augmentation for negative symptoms in chronic schizophrenia/schizoaffective disorder, testing the dopamine-deficiency hypothesis. |
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT | Am J Psychiatry | Double-blind, placebo-controlled, multicentre trial of selegiline augmentation for negative symptoms in outpatients with schizophrenia. |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Hum Psychopharmacol | 8-week double-blind, randomised, placebo-controlled trial of selegiline add-on to risperidone for negative symptoms. |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biol Psychiatry | Placebo-controlled trial of selegiline for neuroleptic-induced tardive dyskinesia in patients on antipsychotics. |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Review/Meta-analysis | Eur Neuropsychopharmacol | Systematic review and meta-analysis of selegiline efficacy/safety (oral and transdermal) across psychiatric disorders, including schizophrenia. |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Review of selegiline's role in treating negative symptoms associated with schizophrenia. |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Review | Schizophr Res | Systematic review of pharmacological treatments for primary negative symptoms in schizophrenia. |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case series | Compr Psychiatry | Three schizophrenia patients showed improved negative symptoms and functioning after adding selegiline to antipsychotic regimen; no adverse effects reported. |
| [7901857](https://pubmed.ncbi.nlm.nih.gov/7901857/) | 1993 | Other | Pharmacopsychiatry | Selegiline evaluated for neuroleptic-induced parkinsonism. |
| [36561338](https://pubmed.ncbi.nlm.nih.gov/36561338/) | 2022 | Review | Front Pharmacol | Historical review of MAO inhibitors, including selegiline, in psychopharmacology. |

## Australia Market Information

No ARTG entries were identified for Selegiline in this evidence pack — market status is recorded as "not marketed" with 0 total licences.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: structured warnings, contraindications, and drug interaction data for Selegiline were not available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that currently prevents a formal safety pre-assessment (S1) for this candidate.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three double-blind RCTs and a 2023 systematic review directly test selegiline augmentation for schizophrenia negative symptoms, giving this candidate genuine (if mixed-result) L2 evidence — a meaningfully stronger basis than the model's raw top-ranked score, which corresponds to an implausible, evidence-free match. However, the drug-level safety data gap is severe enough (Blocking) that no guardrail-based rollout can proceed without it.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently a Blocking data gap
- Structured mechanism-of-action data from DrugBank
- A synthesis of the three existing RCTs' effect sizes/consistency, given their mixed results, before considering guardrailed clinical use
- Confirmation of registration pathway, since Selegiline currently has no ARTG entries in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

