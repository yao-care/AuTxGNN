---
layout: default
title: Melatonin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Melatonin: predicted new indication Migraine disorder (evidence level L5). Approved use: Insomnia"
monitor_inn: "Melatonin"
predicted_indications: ["migraine with brainstem aura", "obesity disorder", "restless legs syndrome", "migraine disorder", "hypervitaminosis", "obsolete hypertelorism (disease)", "monogenic obesity", "frontorhiny", "proximal 16p11.2 microdeletion syndrome", "acute encephalopathy with biphasic seizures and late reduced diffusion"]
---

# Melatonin
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

# Melatonin: From Insomnia to Migraine Disorder

## One-Sentence Summary

Melatonin was originally used to treat insomnia and sleep disorders.
The TxGNN model predicts it may be effective for **migraine disorder**, the best-supported of its top 10 predictions,
with **6 clinical trials** and **19 publications** currently supporting this direction, including a completed Phase 3 randomised controlled trial (RCT) and a meta-analysis.

*Note: the highest-scoring prediction was migraine with brainstem aura (87.9%), but no trials or literature specific to that subtype were found. This report therefore focuses on the broader prediction, migraine disorder (rank 4), which has the strongest evidence.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia; sleep disorder (initiating and maintaining sleep). Approved indication text is not available in the ARTG data compiled for this report. |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 85.5% |
| Evidence Level | L1 (see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note: the strict L1 rule requires at least two completed Phase 3 RCTs. Only one completed Phase 3 RCT (NCT01357031) was found, but it is supported by multiple completed Phase 2 RCTs and a meta-analysis of adult prophylaxis studies. The L1 grading comes from the evidence-scoring step for this candidate. A conservative reading would be L2.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data show that melatonin acts on the MT1 (MTNR1A) and MT2 (MTNR1B) receptors, and also appears in the 5-HT2B receptor record. Through these receptors it regulates circadian rhythm and sleep, which is the basis of its use in insomnia.

Migraine and sleep are closely linked. Poor or disrupted sleep can trigger attacks, and several studies report reduced nocturnal melatonin excretion in people with migraine, which fell further during headache. Beyond circadian regulation, melatonin has anti-inflammatory and antioxidant effects and may modulate serotonergic and pain pathways, including in the trigeminovascular system. These features offer a biologically plausible reason for it to reduce migraine frequency. The TxGNN score is consistent with this plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01357031](https://clinicaltrials.gov/study/NCT01357031) | Phase 3 | Completed | 192 | Double-blind RCT of melatonin 3 mg vs placebo vs amitriptyline 25 mg for migraine prevention in adults |
| [NCT00849511](https://clinicaltrials.gov/study/NCT00849511) | Phase 2 | Completed | 48 | Randomised, double-blind, placebo-controlled cross-over study of melatonin for migraine prevention |
| [NCT03597529](https://clinicaltrials.gov/study/NCT03597529) | Phase 2 | Completed | 84 | CHOCOLATE study: dose-finding of melatonin for acute migraine in children and adolescents |
| [NCT02344316](https://clinicaltrials.gov/study/NCT02344316) | Phase 2 | Completed | 31 | Pilot remote RCT of melatonin vs placebo for migraine prevention in adolescents aged 12-17 |
| [NCT03150797](https://clinicaltrials.gov/study/NCT03150797) | Phase 2 | Terminated | 72 | MAP study: two melatonin doses vs placebo for adolescent migraine prevention; early termination limits interpretation |
| [NCT07743255](https://clinicaltrials.gov/study/NCT07743255) | N/A | Enrolling by invitation | 60 | Melatonin added to propranolol vs propranolol alone for prevention of migraine in children; no results yet |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36445912](https://pubmed.ncbi.nlm.nih.gov/36445912/) | 2022 | Meta-analysis | J Oral Facial Pain Headache | Evaluates efficacy and safety of melatonin for migraine prophylaxis in adults |
| [27165014](https://pubmed.ncbi.nlm.nih.gov/27165014/) | 2016 | RCT | J Neurol Neurosurg Psychiatry | Compared melatonin 3 mg, amitriptyline 25 mg and placebo for migraine prevention (the published report of NCT01357031) |
| [24909684](https://pubmed.ncbi.nlm.nih.gov/24909684/) | 2015 | Clinical study | Curr Drug Saf | Safety and efficacy of melatonin in paediatric migraine prophylaxis |
| [18810607](https://pubmed.ncbi.nlm.nih.gov/18810607/) | 2008 | Open-label trial | Neurol Sci | 3 mg at bedtime for 3 months in 22 children with primary headache; most children with follow-up data reported improvement |
| [33008513](https://pubmed.ncbi.nlm.nih.gov/33008513/) | 2020 | Review | Prog Brain Res | Reviews the therapeutic role of melatonin in migraine prophylaxis and the sleep-migraine link; describes melatonin as relatively safe |
| [16548786](https://pubmed.ncbi.nlm.nih.gov/16548786/) | 2006 | Review | Expert Opin Investig Drugs | Potential therapeutic use of melatonin in migraine and other headache disorders; low melatonin levels in migraine and cluster headache |
| [36014841](https://pubmed.ncbi.nlm.nih.gov/36014841/) | 2022 | Review | Nutrients | Pathogenetic role of melatonin in migraine and implications for pharmacotherapy |
| [39853578](https://pubmed.ncbi.nlm.nih.gov/39853578/) | 2025 | Review | Curr Pain Headache Rep | Nutraceuticals for headache, including melatonin |
| [36990725](https://pubmed.ncbi.nlm.nih.gov/36990725/) | 2023 | Systematic review and meta-analysis | Neurology | Circadian features of cluster headache and migraine |
| [39358369](https://pubmed.ncbi.nlm.nih.gov/39358369/) | 2024 | Case-control | Sci Rep | Serum melatonin levels in Iranian patients with migraine |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14188R | Slenyto | Tablet 1 mg (modified release), oral | Not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions** (20 records; 17 from DDInter plus 3 receptor pharmacology records). Moderate-level interactions include:
  - Warfarin
  - Deferasirox
  - Alpelisib
  - Anagrelide
  - Lorlatinib
  - Olaparib
  - Osimertinib
  - Rucaparib
  - Teriflunomide
  - Vemurafenib
  - Ifosfamide

  Minor-level interactions include cimetidine, obeticholic acid, caffeine, osilodrostat, ethinylestradiol and diethylstilbestrol.
- **Knowledge-graph contraindication signals** (not label text): the knowledge graph links melatonin with liver failure, kidney disease, autoimmune disease (including systemic lupus erythematosus and psoriasis), anxiety and depressive-type disorders, schizophrenia, substance abuse/dependence and constipation, among others. These need verification against the TGA-approved Product Information.

Warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Several completed placebo-controlled RCTs (including a Phase 3 trial against amitriptyline), a meta-analysis in adults, and a plausible link between melatonin and migraine biology support this prediction.
- The trial evidence is mixed in quality: the adolescent studies are small, one was terminated, and the Phase 3 evidence consists of a single trial.
- The Australian ARTG entry is a paediatric-type modified-release product, and its approved indication text was not available.

**To proceed, the following is needed:**
- Review of the TGA-approved PI, since label warnings and contraindications were not available (this was flagged as a blocking data gap)
- Detailed mechanism of action data from DrugBank
- Appraisal of the meta-analysis and RCT results for effect size, optimal dose and formulation
- Confirmation of the approved indication and suitable dosage forms or doses for migraine in Australia
- Review of the moderate drug interactions (particularly warfarin) and the knowledge-graph contraindication signals before clinical use
- Confirmation of efficacy in the target population (adults or children), since the evidence differs between them

**Other predictions:** obesity disorder (L2, Research Question) has only small or indirect trials. Restless legs syndrome has no trials. The other seven predictions have no supporting evidence and are on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

