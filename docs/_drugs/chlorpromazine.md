---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

Using the report format specified in your prompt. Before drafting, I need to flag one judgment call I made based on the evidence pack itself.

**Note on indication selection:** The evidence pack ranks 9 of its 10 TxGNN candidates (including the #1-ranked "retinal dystrophy with or without extraocular anomalies") with **zero supporting evidence** and its own `repurposing_rationale` text explicitly labels them likely **hub-node embedding artifacts** ("非真實預測訊號" / not a real prediction signal — near-identical scores ~0.999x, no mechanistic plausibility, and for rank 1 the 15 "supporting" PubMed hits don't even mention chlorpromazine). Presenting one of those as the headline finding would produce a misleading clinical report. The only candidate with genuine mechanistic rationale, real evidence, and a non-"Hold" recommendation is **rank 10: early-onset schizophrenia** (L3, Proceed with Guardrails). I built the report around that candidate and added a short transparency note about the excluded artifacts rather than silently dropping them.

---

# Chlorpromazine: From Schizophrenia to Early-Onset Schizophrenia

## One-Sentence Summary

Chlorpromazine is a first-generation (typical) antipsychotic whose established mechanism — dopamine D2 receptor antagonism — underlies its long-standing use in schizophrenia. Of the ten candidate indications TxGNN produced for this drug, only **early-onset schizophrenia** is backed by a coherent pharmacological rationale and corroborating evidence, currently supported by **1 clinical trial** and **8 publications**; the remaining nine top-ranked candidates carry no supporting evidence and are assessed below as likely model artifacts.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (established pharmacological use; not recorded in the source registry entry for this record — see Data Gap note below) |
| Predicted New Indication | Early-onset schizophrenia |
| TxGNN Prediction Score | 99.47% (rank 6,160 of all drug–disease pairs) |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

**Data gap:** the `original_indications` field in this evidence pack is empty and `original_moa` is unrecorded (structured DrugBank MOA data not yet pulled). The mechanism discussed below is drawn from the prediction rationale rather than a structured MOA field, and should be independently confirmed against the TGA-approved Product Information before clinical use.

## Selection Note: Nine Candidates Excluded as Likely Artifacts

TxGNN ranked nine other diseases above early-onset schizophrenia for chlorpromazine — including retinal dystrophy, X-linked myopia variants, congenital glycosylation disorders, hydranencephaly, a polymicrogyria syndrome, and Charcot-Marie-Tooth disease type 1G. All nine returned **zero clinical trials and zero (or clearly irrelevant) literature**, cluster tightly around a score of ~0.999x, and have no plausible pharmacological link to a D2/H1/α1/muscarinic receptor antagonist. For the top-ranked candidate, the 15 PubMed hits retrieved were manually checked and none mention chlorpromazine at all — consistent with a keyword co-occurrence false match rather than genuine signal. These are flagged here for transparency and QA (the score clustering suggests a hub-node artifact in the underlying knowledge graph embedding), and none are carried forward into the sections below.

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this record (data gap — DrugBank query pending). Based on well-established pharmacology referenced in the prediction rationale, chlorpromazine acts primarily as a **dopamine D2 receptor antagonist**, with additional antagonism at histamine H1, alpha-1 adrenergic, and muscarinic receptors. D2 blockade is the classic mechanism underlying its efficacy against the positive symptoms of schizophrenia.

Early-onset schizophrenia (onset in childhood or adolescence) is generally regarded as part of the same disease spectrum as adult-onset schizophrenia, differing mainly in age of onset and, in some series, in treatment responsiveness. Because the underlying dopaminergic pathophysiology is considered continuous across the age spectrum, the same D2-antagonist mechanism is, in principle, applicable to the early-onset population.

This is therefore not a novel pharmacological hypothesis so much as an evidence question about **applying an already-understood mechanism to a specific, younger sub-population** — the available data below speaks mainly to treatment-resistance patterns and pharmacogenomic modifiers in this group rather than establishing a new indication from first principles.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06128408](https://clinicaltrials.gov/study/NCT06128408) | N/A (observational) | Unknown | 300 | Cohort study characterising treatment-resistant schizophrenia from illness onset (TRO). Reports that up to 30% of antipsychotic-naïve first-episode patients show poor treatment response, and that TRO patients make up ~80% of all treatment-resistant schizophrenia cases in long-term follow-up. This is a descriptive cohort, not a chlorpromazine intervention trial — classified as indirect (relevance grade B). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24854724](https://pubmed.ncbi.nlm.nih.gov/24854724/) | 2015 | Review | L'Encéphale | Reviews neurological soft signs in early-onset schizophrenia as evidence for a neurodevelopmental model of the disorder. |
| [10703271](https://pubmed.ncbi.nlm.nih.gov/10703271/) | 1999 | Retrospective Cohort | Soc Psychiatry Psychiatr Epidemiol | Examines whether age at onset of schizophrenia relates to typical neuroleptic dosage requirements in outpatients. |
| [18408624](https://pubmed.ncbi.nlm.nih.gov/18408624/) | 2008 | Cohort / genetic association | Pharmacogenetics and Genomics | BDNF gene variants identified as a schizophrenia risk factor and linked to **chlorpromazine-induced extrapyramidal syndrome** in a Chinese population — direct pharmacogenomic data on chlorpromazine tolerability. |
| [17915974](https://pubmed.ncbi.nlm.nih.gov/17915974/) | 2007 | Cohort / pharmacogenomics | J Clin Psychiatry | AKT1 gene polymorphisms associated with schizophrenia risk and with antipsychotic treatment response in a Chinese population. |
| [28976410](https://pubmed.ncbi.nlm.nih.gov/28976410/) | 2017 | Cross-sectional | Clinical Neuropharmacology | Describes clinical features of early-onset schizophrenia patients with comorbid obsessive-compulsive disorder. |
| [26916502](https://pubmed.ncbi.nlm.nih.gov/26916502/) | 2016 | Cross-sectional | Acta Neuropsychiatrica | Assesses Theory of Mind deficits in adolescents with early-onset schizophrenia and their correlation with executive function. |
| [22802957](https://pubmed.ncbi.nlm.nih.gov/22802957/) | 2012 | Imaging / cross-sectional | PLoS ONE | MRI study showing decreased temporal gyrus grey matter volume in first-episode, early-onset schizophrenia. |
| [24289465](https://pubmed.ncbi.nlm.nih.gov/24289465/) | 2013 | Comparative cohort | Psychogeriatrics | Compares clinical features of early-onset versus late-onset schizophrenia in a Japanese sample. |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for chlorpromazine safety information — no structured warnings, contraindications, or drug-interaction data were returned for this record (DDI query: not found).

For context, chlorpromazine is a typical (first-generation) antipsychotic with well-documented class-related risks, including extrapyramidal symptoms, sedation, anticholinergic effects, orthostatic hypotension, and QT prolongation; one of the publications above (PMID 18408624) specifically links a genetic marker to chlorpromazine-induced extrapyramidal syndrome. This general class knowledge does not substitute for the TGA PI and should not be used as a definitive safety reference on its own.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The D2-antagonist mechanism is pharmacologically well-established and plausibly extends to early-onset schizophrenia as part of the same disease spectrum as adult-onset disease. However, direct evidence is limited to one observational cohort study (status: unknown, no chlorpromazine intervention arm) and pharmacogenomic/cross-sectional literature rather than randomised controlled trials in this specific population — consistent with an L3 evidence level, not a level supporting unconditional adoption.

**To proceed, the following is needed:**
- TFDA/TGA-approved PI warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety screening)
- Structured mechanism-of-action data from DrugBank (High-priority data gap)
- Confirmation of chlorpromazine's registered original indication and Australian market/registration status (currently shows "Not marketed" with 0 ARTG entries — verify this is current)
- Drug–drug interaction data (current query returned "not found")
- Paediatric/adolescent-specific dosing, tolerability, and long-term safety data for the early-onset population
- Prospective controlled trial evidence specifically evaluating chlorpromazine (not just antipsychotics generally) in early-onset schizophrenia

**Separately:** the nine other TxGNN-ranked candidates for this drug (score ≥0.999) should be reviewed by the modelling team — the tight score clustering with zero evidence across all nine is a strong signal of a hub-node artifact in the knowledge graph embedding rather than genuine repurposing signal, and may warrant a broader audit of similarly-scored candidates for other drugs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

