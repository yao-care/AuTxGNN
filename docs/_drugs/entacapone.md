---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease and related parkinsonian syndromes"
---

# Entacapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a peripheral COMT inhibitor, originally used as an adjunct to levodopa in Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration** (score 99.76%), but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian syndromes (per the knowledge graph; no approved indication text is recorded for the Australian entry) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entacapone is a peripheral COMT inhibitor. It prolongs the action of levodopa, and its efficacy as an adjunct in Parkinson disease is established.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. A plausible link therefore exists only for the parkinsonian and dopaminergic features. Entacapone would not address the underlying lipid metabolism and neuroaxonal pathology of the condition.

The TxGNN score is high, but it is a computational association. No trial or publication supports use of entacapone in this disease.

### Other Predicted Indications (Top 10)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | Plausible only for parkinsonian features |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | No clear mechanistic link |
| 3 | Myelitis | 99.63% | L5 | No established role for COMT inhibition |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L4 | Largely duplicates the existing Parkinson disease indication |
| 5 | Transaldolase deficiency | 99.43% | L5 | No mechanistic link |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | Theoretical mitochondrial concern, so caution is warranted |
| 7 | Lewy body dementia | 99.25% | L4 | Shared alpha-synuclein pathology; indirect, preclinical support only |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | No mechanistic link |
| 9 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.06% | L5 | Structural developmental disorder; no plausible role |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L4 | Indirect rationale; often poor levodopa response |

Of these, Lewy body dementia and progressive supranuclear palsy-corticobasal syndrome are the most biologically coherent research questions. Juvenile parkinsonism is largely a duplicate of the approved use.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (PLA2G6-associated neurodegeneration).

Trials found for other predicted indications are tangential and do not test entacapone as a treatment:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging in autonomic failure (relevant to Lewy body dementia). A diagnostic imaging study, not a therapeutic trial of entacapone |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Active, not recruiting | 120 | Non-interventional gait analysis in neurological disease, including parkinsonian disorders (relevant to PSP-corticobasal syndrome). It does not evaluate entacapone |

## Literature Evidence

Currently no related literature is available for the top-ranked prediction.

Literature found for Lewy body dementia is preclinical only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro study | J Neurosci Res | Examined the effects of antiparkinsonian agents on β-amyloid and α-synuclein oligomer formation |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC organoid) | Sci Adv | Modelled Lewy body disease with SNCA triplication cortical organoids and identified candidate therapeutic drugs |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 14542J | Comtan | Tablet 200 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are computational associations, not label text): multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, drug-induced dyskinesia, epilepsy, psychotic and other mental disorders, liver disease, kidney disease, gallbladder disease, peptic and gastric ulcer, open-angle and angle-closure glaucoma, diabetes mellitus, diabetic ketoacidosis, myocardial infarction, coronary thrombosis, heart conduction disease, sudden cardiac arrest, melanoma, hemoglobinopathy and diarrhoeal disease.
- **Drug interactions:** 82 interactions were identified. The main moderate-level interactions are with epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide and iron. Others are of unknown severity, including pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin and potassium chloride.
- **Theoretical concern:** entacapone has been associated with mitochondrial uncoupling in vitro, which argues for caution in mitochondrial disorders.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a model score, with no trials or literature. Entacapone would not address the underlying pathology of PLA2G6-associated neurodegeneration. Lewy body dementia and PSP-corticobasal syndrome are better candidates for further research, but their evidence is indirect or preclinical.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian entry (ARTG 14542J)
- Detailed mechanism of action data
- Targeted literature review of COMT inhibitors in PLA2G6-related dystonia-parkinsonism
- Preclinical or case-series evidence in Lewy body dementia or PSP-corticobasal syndrome before any trial planning
- Confirmation of route compatibility (oral tablet) with the target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

