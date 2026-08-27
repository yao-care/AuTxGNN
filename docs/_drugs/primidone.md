---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Epilepsy/Essential Tremor to Reflex Epilepsy Syndromes (Audiogenic Seizures)

## One-Sentence Summary

Primidone is a barbiturate-derived anticonvulsant, established for epilepsy and essential tremor. TxGNN generated **ten** candidate new indications for this drug, all clustered around reflex/stimulus-triggered seizure syndromes and two unrelated outliers; the model's single top-ranked hit (**trigeminal nerve neoplasm**) is almost certainly a name-collision artefact rather than a genuine signal. The most defensible candidate is **audiogenic (sound-triggered) seizures**, supported only by decades-old preclinical/animal pharmacology — **zero clinical trials** exist for any of the ten candidates.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (tonic-clonic/partial seizures) and essential tremor — formal indication text unavailable; Primidone is not currently registered in Australia |
| Predicted New Indication | Audiogenic seizures (a reflex epilepsy subtype); trigeminal neuralgia and startle epilepsy are secondary candidates in the same cluster |
| TxGNN Prediction Score | 99.99% (audiogenic seizures, model rank 471 of output) |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Note on the model's top hit:** TxGNN's #1-ranked prediction for this drug was *trigeminal nerve neoplasm* (score 99.99%, rank 189). The evidence pack's own mechanistic review flags this as a very likely false positive — Primidone has an anticonvulsant/GABAergic mechanism with no known link to tumour biology, and the prediction has zero supporting trials or literature. It most likely reflects the knowledge-graph embedding confusing "trigeminal nerve neoplasm" with the unrelated term "trigeminal neuralgia." This report focuses instead on the candidates with genuine mechanistic and literature support.

---

## Why is This Prediction Reasonable?

Primidone is a barbiturate derivative metabolised to phenobarbital and phenylethylmalonamide (PEMA). Its mechanism combines GABA-A receptor potentiation with voltage-gated sodium-channel blockade — a broad-spectrum anticonvulsant/anti-tremor profile that has kept it in use for generalised and partial epilepsy and for essential tremor.

Reflex epilepsies (audiogenic, startle, reading, thinking, micturition-induced, and orgasm-induced seizures) are seizure subtypes triggered by specific sensory or cognitive stimuli rather than distinct diseases with separate pathophysiology. Because broad-spectrum GABAergic/sodium-channel-blocking anticonvulsants are mechanistically applicable across seizure types, it is biologically plausible — though not clinically proven — that Primidone could be effective in these stimulus-triggered subtypes, similar to how it is already used off-label in cortical/stimulus-sensitive myoclonus.

The strongest direct evidence is a 1964 animal study that tested pyramidone (a primidone-related compound) against audiogenic convulsions, and a 1976 mouse study examining primidone's effect on brain enzyme activity in audiogenic epilepsy. Both are direct pharmacological tests in a relevant disease model, but both are more than 45 years old, small in scale, and pre-date modern trial standards. No human clinical evidence exists for any of the reflex epilepsy candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — for any of the ten TxGNN-predicted indications for Primidone (query log confirms 0 ClinicalTrials.gov and 0 ICTRP results across all ten disease queries).

---

## Literature Evidence

| PMID | Year | Type | Journal | Target Indication | Key Findings |
|------|-----|------|------|------|---------|
| [3925335](https://pubmed.ncbi.nlm.nih.gov/3925335/) | 1985 | RCT (general epilepsy) | New England Journal of Medicine | General/micturition-induced seizures | 10-centre RCT (n=622) comparing carbamazepine, phenobarbital, phenytoin, and primidone in partial/secondary generalised tonic-clonic seizures; establishes primidone's general anticonvulsant efficacy but not specific to any reflex subtype |
| [14249886](https://pubmed.ncbi.nlm.nih.gov/14249886/) | 1964 | Animal Study | Biulleten' eksperimental'noi biologii i meditsiny | Audiogenic seizures | Direct preclinical test of pyramidone (primidone-related compound) against audiogenic convulsions in animals |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Animal Study | Neurologie et psychiatrie | Audiogenic seizures | Effect of phenobarbital, diphenylhydantoin and primidone on brain enzyme activity in mice with audiogenic epilepsy |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case Report | Chinese Medical Journal (Free China ed) | Startle epilepsy | Case of startle epilepsy presenting as atonic drop attacks; describes clinical phenotype, not primidone-specific treatment data |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clinical Neuroscience | Audiogenic/reading seizures (stimulus-sensitive myoclonus) | Reviews primidone (500–1000 mg/day) among agents used for cortical/stimulus-sensitive myoclonus |
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disorders | Trigeminal neuralgia | Reviews antiepileptic drug use outside epilepsy; evidence for such uses generally limited to case series/small trials |
| [9068876](https://pubmed.ncbi.nlm.nih.gov/9068876/) | 1996 | Review | Bailliere's Clinical Neurology | Micturition-induced seizures | Lists primidone among established antiepileptic drugs for partial and generalised seizures |
| [11096777](https://pubmed.ncbi.nlm.nih.gov/11096777/) | 2000 | Review | Current Treatment Options in Neurology | Micturition-induced seizures | Primidone/phenobarbital noted as later-line options in primary generalised epilepsies |
| [19054416](https://pubmed.ncbi.nlm.nih.gov/19054416/) | 2009 | Cohort | Epilepsia | Thinking seizures | Studies race/setting effects on initial AED choice in newly diagnosed geriatric epilepsy; general epidemiology, not disease-specific |
| [3092407](https://pubmed.ncbi.nlm.nih.gov/3092407/) | 1986 | Review | Therapeutic Drug Monitoring | Trigeminal neuralgia | Discusses carbamazepine-primidone pharmacokinetic interactions in the context of trigeminal neuralgia treatment |

---

## Australia Market Information

Primidone has no ARTG entries and is not currently marketed in Australia (0 licences on file).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist for any of the ten TxGNN-predicted indications, the best-supported candidate (audiogenic seizures) rests on animal pharmacology from the 1960s–70s, and Primidone is not currently marketed in Australia. The model's own top-ranked hit (trigeminal nerve neoplasm) is very likely a false positive, underscoring the need for mechanistic screening before acting on TxGNN rank alone.

**To proceed, the following is needed:**
- TGA-approved Product Information / PI warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action data from DrugBank (currently a data gap)
- A targeted literature search specifically on primidone in reflex/stimulus-triggered epilepsy syndromes, to update the 1960s–70s preclinical evidence base
- Consideration of whether audiogenic/startle/reading seizure phenotypes warrant a pilot case series before any trial planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

