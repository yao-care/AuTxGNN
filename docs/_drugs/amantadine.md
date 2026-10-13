---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Amantadine
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

# Amantadine: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is an oral agent originally used for Parkinson disease and related parkinsonian and movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis** (score 99.48%), but **no clinical trials and no publications** currently support this prediction.
Among the other top-ranked predictions, **myelitis** (post-polio fatigue) and **Lewy body dementia** have the most literature, though it is largely indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian and movement disorders (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, amantadine is an uncompetitive NMDA receptor antagonist with dopaminergic effects, and these properties underlie its use in parkinsonism and levodopa-induced dyskinesia.

For Rasmussen encephalitis, a plausible but unverified link is NMDA receptor antagonism, because glutamate-mediated excitotoxicity has been proposed in this condition. No trials or literature were supplied to support this link, so the prediction remains purely model-based.

Other predictions in the list show varying plausibility:

- **Myelitis:** The evidence relates to post-polio syndrome fatigue, which is indirect for myelitis in general.
- **PLA2G6-associated neurodegeneration:** The only paper concerns a different subtype (PKAN).
- **Lewy body dementia and progressive supranuclear palsy-corticobasal syndrome:** The evidence is indirect, and amantadine may worsen hallucinations and confusion in Lewy body dementia.
- **Metabolic disorders (transaldolase deficiency, fructose-1,6-bisphosphatase deficiency) and several X-linked intellectual disability syndromes:** No plausible mechanistic link was identified.

---

## Clinical Trial Evidence

For the top prediction (Rasmussen subacute encephalitis), currently no related clinical trials are registered.

For reference, the only trial in the top 10 predictions is listed below. It sits under the lower-ranked prediction, progressive supranuclear palsy-corticobasal syndrome, and is not an amantadine treatment trial.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Active, not recruiting | 120 | Observational gait pattern analysis in neurological disease, particularly parkinsonian disorders. It does not test amantadine, so it gives no direct treatment evidence. |

---

## Literature Evidence

For the top prediction (Rasmussen subacute encephalitis), currently no related literature is available.

The most relevant publications found across the other top-ranked predictions are listed below. They are indirect for the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7611638](https://pubmed.ncbi.nlm.nih.gov/7611638/) | 1995 | RCT | Ann N Y Acad Sci | Double-blind, placebo-controlled trial of amantadine for fatigue in post-polio syndrome; 23 patients completed six weeks of therapy (myelitis prediction, indirect). |
| [25984923](https://pubmed.ncbi.nlm.nih.gov/25984923/) | 2015 | Review | Cochrane Database Syst Rev | Treatment for post-polio syndrome; effectiveness of pharmacological treatment not yet established. |
| [21328301](https://pubmed.ncbi.nlm.nih.gov/21328301/) | 2011 | Review | Cochrane Database Syst Rev | Earlier version of the post-polio syndrome treatment review. |
| [16879288](https://pubmed.ncbi.nlm.nih.gov/16879288/) | 2006 | Guideline | Eur J Neurol | EFNS guideline on diagnosis and management of post-polio syndrome. |
| [2039376](https://pubmed.ncbi.nlm.nih.gov/2039376/) | 1991 | Case series | Arch Neurol | Post-polio fatigue treated with amantadine. |
| [26085043](https://pubmed.ncbi.nlm.nih.gov/26085043/) | 2015 | Systematic review/meta-analysis | Am J Psychiatry | Pharmacological management of Lewy body dementia; the conclusions on amantadine cannot be confirmed from the data compiled. |
| [18644910](https://pubmed.ncbi.nlm.nih.gov/18644910/) | 2008 | Review | Pract Neurol | Hallucinosis in Parkinson disease can be triggered by amantadine and anticholinergics. |
| [30051337](https://pubmed.ncbi.nlm.nih.gov/30051337/) | 2018 | Review | CNS Drugs | Therapeutic management of overlapping atypical parkinsonism syndromes (PSP, CBD, MSA). |
| [31366412](https://pubmed.ncbi.nlm.nih.gov/31366412/) | 2019 | Case report/small study | Can J Neurol Sci | Amantadine for gait dysfunction in PKAN (indirect for PLA2G6-associated neurodegeneration). |
| [10412804](https://pubmed.ncbi.nlm.nih.gov/10412804/) | 1999 | Preclinical safety study | Acta Neuropathol | Amantadine did not cause histopathological alterations in human brain tissue. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14486K | AMANTAMED | Capsule containing amantadine hydrochloride 100 mg (oral) | Not stated in the data compiled |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Knowledge-graph contraindication signals (not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, kidney disease, pyoureter, congestive heart failure, psychotic and related disorders (psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder), melanoma, angle-closure glaucoma, substance-related disorders, and atopic eczema/dermatitis. These need verification against the PI.
- **Drug interactions:** 93 interactions were identified.
  - **Major:** bupropion.
  - **Moderate:** anticholinergic and antimuscarinic agents (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium), metoclopramide, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate.
  - **Unknown severity:** calcitriol, pantoprazole, glimepiride, doxycycline and metformin.
  - Only the first 20 interactions were available for review.
- **Clinical note:** The literature reviewed notes that amantadine can trigger hallucinosis and psychosis, which is relevant for Lewy body dementia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction, Rasmussen subacute encephalitis, is supported only by a model score (L5), with no trials or publications. Evidence for the other top-ranked predictions is indirect: post-polio fatigue for myelitis, a different disease subtype for PLA2G6-associated neurodegeneration, and mostly case reports and reviews for Lewy body dementia. Myelitis and Lewy body dementia may be treated as research questions rather than candidates for clinical adoption.

**To proceed, the following is needed:**
- Mechanism of action data to assess the NMDA/glutamate hypothesis in Rasmussen encephalitis
- Targeted literature review of amantadine in Rasmussen encephalitis and in myelitis beyond post-polio syndrome
- Extraction of what the post-polio syndrome Cochrane reviews and the Lewy body dementia meta-analysis concluded about amantadine
- TGA Product Information warnings and contraindications, and the approved indication text for the ARTG entry
- Review of the knowledge-graph contraindication signals against the PI, especially psychosis, epilepsy, renal impairment and heart failure
- Route compatibility and disease similarity assessments, which are currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

