---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 796
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Zonisamide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the Australian registration data (zonisamide is general…"
monitor_inn: "Zonisamide"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
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

## Zonisamide: From Epilepsy to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Zonisamide is an antiseizure medicine marketed in Australia as an oral capsule (the approved indication text was not available in the data compiled for this report).
The TxGNN model predicts it may be effective for **Tourette syndrome**, but **no clinical trials and no publications** currently support this prediction.
The prediction is model-based only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data (zonisamide is generally used as an antiseizure medicine) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, zonisamide acts on voltage-gated sodium and T-type calcium channels and may modulate dopaminergic and serotonergic transmission. These pathways could plausibly relate to the neural circuits involved in tics, but this link is speculative.

Its efficacy in epilepsy is established, and mechanistically it may be applicable to other neurological and neuropsychiatric conditions. However, no direct data link zonisamide to Tourette syndrome.

There is also a possible safety signal. A pragmatic review (PMID 36005856) reports antiseizure medication-induced tic disorder, which raises concern rather than offering support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tourette syndrome.

---

## Literature Evidence

Currently no related literature available for Tourette syndrome. The only relevant item identified, [36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/) (2022, Review, *Expert Rev Neurother*), discusses antiseizure medication-induced obsessive-compulsive disorder and tic disorder, which is a safety signal rather than evidence of benefit.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13853D | Zonegran | Capsule 25 mg | Not stated in the data compiled |

---

## Safety Considerations

- **Drug Interactions** (100 interactions were identified; examples below):
  - **Major**: anticholinergic agents (methscopolamine, hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, propantheline) and metformin.
  - **Moderate**: aprepitant, morphine, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole.
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): kidney disease and nephrolithiasis, liver disease, gallbladder disease, metabolic acidosis, neutropenia and agranulocytosis, and psychiatric disorders (anxiety, psychotic, schizoaffective and other mental disorders).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label text was not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests on the model score alone, with no trials or literature, and a related review flags possible tic induction by antiseizure medicines.

**To proceed, the following is needed:**
- Retrieve the TGA Product Information, including the approved indication, warnings and contraindications
- Obtain detailed mechanism of action data (for example from DrugBank)
- A systematic literature search and trial registry search (including ANZCTR) specific to Tourette syndrome
- Preclinical or small exploratory clinical evidence, with attention to tic-exacerbation risk

---

## Other Predicted Indications (Context)

Other predictions were also reviewed, but none is stronger than L4 evidence:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Manic bipolar affective disorder | 0.9935 | L5 | One open-label report in bipolar depression ([17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/)) and a case report of zonisamide-induced mania ([2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/)). |
| Fibromyalgia | 0.9920 | L5 | One Phase 4 trial ([NCT00259636](https://clinicaltrials.gov/study/NCT00259636)) was withdrawn with 0 enrolled. |
| Trichotillomania, Prinzmetal angina, conjunctivitis | 99.16–0.9978 | L5 | Prediction only. |
| Methemoglobinemia (three entries) | 0.9953–0.9964 | L5 | No credible mechanism. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Zonisamide is a sulfonamide, so safety concerns outweigh any benefit signal. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

