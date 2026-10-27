---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Topiramate: predicted new indication Trigeminal neuralgia (evidence level L5). Approved use: Epilepsy with generalised tonic-clonic seizures, partial epilepsy…"
monitor_inn: "Topiramate"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Topiramate
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

## Topiramate: From Epilepsy to Trigeminal Neuralgia
{: .text-alpha }

## One-Sentence Summary

Topiramate is an antiseizure medication originally used for generalised tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction, trigeminal nerve neoplasm, is most likely a graph-proximity artefact, so this report focuses on the best-supported prediction, **Trigeminal Neuralgia** (score 98.92%).
That prediction is currently supported by **0 registered clinical trials** and **20 publications**, including a small randomised crossover pilot study and a meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy with generalised tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome (from knowledge graph indication data; the ARTG entry has no indication text) |
| Predicted New Indication | Trigeminal neuralgia (best-supported prediction; the top-ranked prediction, trigeminal nerve neoplasm, scored 99.70% but is considered implausible) |
| TxGNN Prediction Score | 98.92% (trigeminal neuralgia); 99.70% (trigeminal nerve neoplasm) |
| Evidence Level | L2 (trigeminal neuralgia) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (trigeminal neuralgia) |

**Note on the ranking:** The highest-scoring prediction, trigeminal nerve neoplasm, has no trials or literature and no plausible antineoplastic mechanism, so it is rated L5 and Hold. Most other top predictions are rare reflex epilepsies (visual, startle, orgasm-induced, eating, audiogenic, thinking, micturition-induced and reading seizures), which fall within topiramate's existing antiseizure spectrum. Their evidence is indirect (L4/L5), so none is recommended for progression beyond a research question or Hold. Trigeminal neuralgia is the only prediction with direct clinical evidence.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From published pharmacology, topiramate is a broad-spectrum antiseizure drug that blocks voltage-gated sodium channels, enhances GABA-A activity, antagonises AMPA/kainate glutamate receptors and weakly inhibits carbonic anhydrase.

Trigeminal neuralgia is a neuropathic pain syndrome driven by ectopic, hyperexcitable firing of trigeminal nerve fibres, often after neurovascular compression and focal demyelination. Carbamazepine, a sodium channel blocker, is first-line therapy. Topiramate's sodium channel blockade and dampening of excitatory transmission parallel carbamazepine's action, which makes the prediction mechanistically plausible. This also explains why the knowledge graph links the drug to this nerve.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal neuralgia. No ANZCTR identifiers were available either.

---

## Literature Evidence

Selected publications for trigeminal neuralgia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11307048](https://pubmed.ncbi.nlm.nih.gov/11307048/) | 2001 | RCT (pilot, placebo-controlled crossover) | Clin Neuropharmacol | Three patients; topiramate reduced pain by 31%, 42% and 64% (p = 0.04) |
| [21936587](https://pubmed.ncbi.nlm.nih.gov/21936587/) | 2011 | Meta-analysis | CNS Drugs | Topiramate compared with carbamazepine in classical trigeminal neuralgia |
| [19471799](https://pubmed.ncbi.nlm.nih.gov/19471799/) | 2004 | Systematic review/Meta-analysis | Rev Bras Anestesiol | Efficacy, safety and tolerability of pharmacological treatments for trigeminal neuralgia |
| [41718164](https://pubmed.ncbi.nlm.nih.gov/41718164/) | 2026 | Systematic review | Medicines (Basel) | Anticonvulsants in trigeminal neuralgia, stratified by mechanism of action |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences (Riyadh) | Update on pharmacological and surgical options for trigeminal neuralgia |
| [17952282](https://pubmed.ncbi.nlm.nih.gov/17952282/) | 2007 | Case series | Arq Neuropsiquiatr | Eight patients on 50-100 mg/day: 3 complete remissions, 3 moderate improvements, 2 non-responders; dizziness, somnolence and weight loss were common |
| [11398791](https://pubmed.ncbi.nlm.nih.gov/11398791/) | 2001 | Clinical report | J Pain Symptom Manage | Topiramate relieved idiopathic and symptomatic trigeminal neuralgia |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in cluster headache and trigeminal neuralgia |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian J Neurosurg | General review of trigeminal neuralgia |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clin Evid | General review of trigeminal neuralgia |

The RCT is very small (three patients), so it provides only preliminary support.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13878K | Topamax Sprinkle | Capsule 50 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Contraindications (from knowledge graph drug-disease edges, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, diarrhoeal disease, ocular hypertension, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, acidosis disorder, metabolic acidosis, amnestic disorder, retrograde amnesia.
- **Drug interactions:** The interaction screen returned 100 interactions. The main ones listed are:
  - **Major:** metformin, and the anticholinergic agents hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline and trospium.
  - **Moderate:** pioglitazone, glyburide, morphine, dronabinol, nabilone, phentermine, metoclopramide, phenylbutyric acid and glycerol phenylbutyrate.
- **Reported adverse effects in the literature:** dizziness, somnolence, weight loss, cognitive impairment, metabolic acidosis, renal stones, and psychiatric effects (case reports of psychotic exacerbation and mania).

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (trigeminal neuralgia only)**

**Rationale:**
- Trigeminal neuralgia has a plausible mechanism and direct clinical evidence: a small placebo-controlled crossover pilot, a topiramate-versus-carbamazepine meta-analysis and case series. This supports topiramate as an alternative or add-on for patients who are intolerant of, or refractory to, carbamazepine or oxcarbazepine. The evidence base is small and no registered Phase 3 trial exists.
- Trigeminal nerve neoplasm should be placed on **Hold**. It is likely a model artefact with no supporting evidence.
- The reflex epilepsy predictions are **Hold** or **Research Question** only. Their evidence is general epilepsy or preclinical data, with nothing specific to the conditions.

**To proceed, the following is needed:**
- Adequately powered randomised controlled trials of topiramate in trigeminal neuralgia, ideally compared with carbamazepine or oxcarbazepine
- Review of the TGA-approved PI for warnings and contraindications, which was not available in the data compiled for this report
- Detailed mechanism of action data from DrugBank
- Monitoring plan for cognitive and other CNS adverse effects, metabolic acidosis, renal stones, and the major interactions (notably metformin and anticholinergics)
- Confirmation of the approved indications and available formulations for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

