---
layout: default
title: Zopiclone
parent: Model Prediction Only (L5)
nav_order: 797
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zopiclone: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
monitor_inn: "Zopiclone"
predicted_indications: ["acute encephalopathy with biphasic seizures and late reduced diffusion", "benign paroxysmal torticollis of infancy", "agoraphobia", "inherited prion disease", "Wernicke-Korsakoff syndrome", "epilepsy, childhood absence, susceptibility to", "restless legs syndrome", "mitral valve prolapse, myxomatous", "hyperparathyroidism, primary, caused by water clear cell hyperplasia"]
---

# Zopiclone
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

## Zopiclone: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)
{: .text-alpha }

## One-Sentence Summary

Zopiclone is a Z-drug hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, but this is essentially the same as its existing indication rather than a true repurposing.
Currently there are **no registered clinical trials** but **20 publications** (including several systematic reviews, network meta-analyses and clinical guidelines) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (from the TxGNN knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 98.83% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* No clinical trials are registered in the data compiled for this report. The L1 level reflects the strength of the published systematic reviews, network meta-analyses and guidelines, not completed Phase 3 trials specific to this prediction. It should be read as supportive of the existing insomnia indication only.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, zopiclone is a cyclopyrrolone Z-drug that acts as a positive allosteric modulator of the GABA-A receptor. This enhances inhibitory neurotransmission and promotes sleep onset and maintenance.

"Sleep disorder, initiating and maintaining sleep" is effectively the same condition as insomnia, which is zopiclone's established use. The high TxGNN score therefore mostly reflects recovery of a known indication rather than a new discovery. The published literature supports zopiclone's role in insomnia, while also highlighting limits such as dependence, abuse potential and next-day impairment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic review / network meta-analysis | Lancet | Compares pharmacological treatments for acute and long-term management of adult insomnia disorder |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Systematic review / network meta-analysis | Drugs | Network meta-analysis of 153 randomised trials on the effectiveness, safety and tolerability of insomnia drugs |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Compares lemborexant with other insomnia treatments (zopiclone is among the comparators) |
| [34023645](https://pubmed.ncbi.nlm.nih.gov/34023645/) | 2021 | Systematic review | Eur Neuropsychopharmacol | Reviews efficacy and safety of zopiclone for insomnia in older adults |
| [41187937](https://pubmed.ncbi.nlm.nih.gov/41187937/) | 2025 | Clinical guideline | Arq Neuropsiquiatr | Brazilian guideline on Z-drug abuse and dependence; use recommended for no longer than four weeks |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Clinical guideline | Sleep Med | European consensus on switching or deprescribing hypnotics for chronic insomnia |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs have a strong evidence base for insomnia but carry cognitive impairment, tolerance, rebound insomnia, falls and dependence risks |
| [38551874](https://pubmed.ncbi.nlm.nih.gov/38551874/) | 2024 | Review | Rev Prat | Z-drugs (zolpidem, zopiclone) promote sleep initiation with fewer harmful effects than long-acting benzodiazepines when used at the right time and dose |
| [20945020](https://pubmed.ncbi.nlm.nih.gov/20945020/) | 2010 | Review | Rev Bras Psiquiatr | Z-drugs are GABA-A modulators selective for α1 subunits |
| [34533440](https://pubmed.ncbi.nlm.nih.gov/34533440/) | 2022 | Review | Curr Pharm Des | Pharmacology and misuse potential of benzodiazepines and Z-drugs |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13307J | Imovane | Tablet 7.5 mg (oral) | Approved indication text not available in the data compiled for this report |

---

## Safety Considerations

**Contraindication-related conditions (from drug–disease knowledge graph data, not label text):** liver failure, anxiety disorder, neurotic disorder, dysthymic disorder.

**Drug Interactions:** 100 potential interactions were identified, but none has a severity grading (all are recorded as "Unknown"). Examples include morphine, scopolamine, metformin, glimepiride, pantoprazole, omeprazole and prednisone. Clinical significance cannot be determined from this data, particularly for additive CNS depression with opioids.

**Literature-derived cautions:** dependence and abuse potential, rebound insomnia on discontinuation, next-day cognitive impairment, falls and car accidents (especially in older adults). Short-term use only (generally up to four weeks) is recommended.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is effectively the same as zopiclone's established use in insomnia, and is supported by systematic reviews, network meta-analyses and recent guidelines. It is not a true repurposing, and safety concerns around dependence and next-day impairment require guardrails.

**To proceed, the following is needed:**
- The approved indication text and PI warnings and contraindications for the ARTG entry (Imovane)
- Detailed mechanism of action data
- Clarification of the severity of the 100 listed drug interactions, especially with other CNS depressants
- A deprescribing and short-term-use plan consistent with the 2025 Z-drug guidance
- Special-population precautions (older adults, hepatic impairment, anxiety and mood disorders)

---

### Other Predictions (Not Recommended for Progression)

For completeness, the other nine predicted indications have no clinical trial evidence and are rated Hold, except restless legs syndrome:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Acute encephalopathy with biphasic seizures and late reduced diffusion | 90.43% | L5 | Hold |
| 3 | Benign paroxysmal torticollis of infancy | 81.96% | L5 | Hold |
| 4 | Agoraphobia | 81.16% | L5 | Hold |
| 5 | Inherited prion disease | 74.13% | L5 | Hold |
| 6 | Wernicke-Korsakoff syndrome | 70.14% | L5 | Hold |
| 7 | Childhood absence epilepsy, susceptibility to | 68.56% | L5 | Hold (GABA-A enhancement may aggravate absence seizures) |
| 8 | Restless legs syndrome | 64.91% | L4 | Research question (indirect support only; may help secondary insomnia, not core RLS pathophysiology) |
| 9 | Mitral valve prolapse, myxomatous | 64.74% | L5 | Hold |
| 10 | Primary hyperparathyroidism due to water clear cell hyperplasia | 64.04% | L5 | Hold |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

