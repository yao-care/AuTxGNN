---
layout: default
title: Escitalopram
parent: Model Prediction Only (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Escitalopram: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
---

# Escitalopram
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

# Escitalopram: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Escitalopram is a selective serotonin reuptake inhibitor (SSRI) originally used to treat depression (unipolar, endogenous and major depressive disorder) and anxiety disorders.
The TxGNN model predicts it may be effective for **Dysthymic Disorder**, the highest-ranked prediction with meaningful supporting evidence. This direction is supported by **6 clinical trials** (2 directly relevant) and **6 publications**, including a placebo-controlled RCT and a meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (per knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Dysthymic disorder (the top-ranked prediction, Ohdo syndrome and variants, has no supporting evidence and is not pursued) |
| TxGNN Prediction Score | 98.55% (dysthymic disorder) |
| Evidence Level | L1 (as graded in the data compiled for this report; see caveat below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked prediction:** Rank 1 was Ohdo syndrome and variants (score 98.56%). It has no trials or literature and no plausible mechanistic link, so it appears to be a graph-based artefact (Hold, L5). Dysthymic disorder (rank 2) is the first prediction with clinical support and is the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, escitalopram is the S-enantiomer of citalopram and a selective serotonin reuptake inhibitor. Its efficacy in major depressive disorder is established, and mechanistically it may be applicable to dysthymic disorder.

Dysthymia is a chronic, lower-grade depressive disorder in the same spectrum as major depressive disorder. This is therefore largely an extension within the depressive spectrum rather than a true repurposing. A placebo-controlled RCT of escitalopram in dysthymic disorder (PMID 21811192) and a meta-analysis of antidepressants in dysthymia (PMID 21527126) support the prediction.

**Evidence level caveat:** The L1 grade rests on NCT00080158 (Phase 2/3, n=120), which studied adolescent suicide attempters, not dysthymia. The directly relevant trials are Phase 4 and small. A conservative reading would therefore be closer to L2–L3 for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00220701](https://clinicaltrials.gov/study/NCT00220701) | Phase 4 | Completed | 36 | 12-week double-blind placebo-controlled study of escitalopram in dysthymic disorder, with 12-week open-label extension (directly relevant) |
| [NCT00234312](https://clinicaltrials.gov/study/NCT00234312) | Phase 4 | Completed | 40 | Escitalopram vs. sertraline in dysthymic disorder and double depression (directly relevant; active comparator) |
| [NCT00296712](https://clinicaltrials.gov/study/NCT00296712) | Phase 4 | Completed | 55 | Escitalopram/bupropion combination as first-line depression treatment; combination design confounds the escitalopram effect |
| [NCT01973283](https://clinicaltrials.gov/study/NCT01973283) | Phase 4 | Completed | 100 | Antidepressant response on depressive symptoms and frailty in older adults (indirect) |
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | Treatments for depressed adolescent suicide attempters (different population) |
| [NCT00296777](https://clinicaltrials.gov/study/NCT00296777) | Phase 4 | Completed | 28 | Brain testing and fMRI correlated with treatment outcome in depressed outpatients (biomarker-oriented) |

No ANZCTR trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21811192](https://pubmed.ncbi.nlm.nih.gov/21811192/) | 2010 | RCT | Int Clin Psychopharmacol | 36 outpatients with dysthymic disorder randomised to escitalopram (up to 20 mg/day) or placebo for 12 weeks |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis | J Clin Psychiatry | Efficacy of antidepressants for dysthymia in placebo-controlled RCTs; compared responses with major depressive disorder |
| [19820552](https://pubmed.ncbi.nlm.nih.gov/19820552/) | 2009 | RCT | J Psychiatr Pract | Whether starting two antidepressants together speeds and increases remission in depression |
| [25647343](https://pubmed.ncbi.nlm.nih.gov/25647343/) | 2015 | Cohort | Psychoneuroendocrinology | Shift toward T helper 2 responses and increased innate immunity modulators in depressed patients on escitalopram |
| [23260337](https://pubmed.ncbi.nlm.nih.gov/23260337/) | 2013 | Case report/Review | Gen Hosp Psychiatry | SSRI-induced galactorrhoea; 23 reported cases, mostly with escitalopram and paroxetine |
| [21448115](https://pubmed.ncbi.nlm.nih.gov/21448115/) | 2011 | Case report | Psychiatr Danub | Allergic reactions during sertraline and escitalopram treatment in a patient with dysthymia |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10181W | Lexapro | Oral solution 20 mg (as oxalate) per mL, 15 mL | Not available in the data compiled for this report |

Only an oral solution is listed. No other formulations were identified.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, heart disease, cardiovascular disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug interactions:** 100 interactions were identified; 20 were reviewed. Major-level interactions include **bupropion, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron and phentermine**. Moderate interactions include acetylsalicylic acid (bleeding risk), morphine, omeprazole, cimetidine, famotidine, loperamide and glimepiride, among others. The remaining interactions were not reviewed.
- **Other considerations:** One literature source notes that SSRIs, including escitalopram, may cause galactorrhoea. Doses above labelled limits (relevant to OCD, not dysthymia) raise QT-prolongation concerns.

Warnings and contraindications from the TGA-approved Product Information (PI) were not available. Please refer to the PI for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Escitalopram already holds depression and anxiety indications, and dysthymia sits within the depressive spectrum. A placebo-controlled RCT and a meta-analysis support efficacy, but the directly relevant trials are small (n=36–40) and Phase 4, and the L1 grade depends on a trial in a different population.

**To proceed, the following is needed:**
- Confirmation of the approved indication text for ARTG 10181W and the TGA PI warnings and contraindications
- Detailed mechanism of action data
- Larger, adequately powered trials in dysthymia (ideally Phase 3), or confirmation that the evidence suffices as an extension of the existing depression indication
- Interaction management plan, particularly for bupropion and QT-prolonging or serotonergic agents
- Monitoring for patients with cardiac disease, epilepsy, bipolar disorder, or bleeding risk

---

## Other Predictions (For Reference)

| Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Obsessive-compulsive disorder | 98.36% | L1 | Proceed with Guardrails | SSRIs are first-line for OCD; includes a Phase 3 open-label high-dose study (NCT00305500), a relapse-prevention RCT (PMID 17240120) and a placebo-controlled paroxetine-referenced RCT (PMID 17407626). Higher doses raise QT and tolerability concerns. |
| Agoraphobia | 96.90% | L1 (stage S2) | Proceed with Guardrails | Evidence is for panic disorder with or without agoraphobia (PMID 14658946, network meta-analyses), not agoraphobia alone. |
| Ohdo syndrome, Ohdo-type blepharophimosis, benign paroxysmal torticollis of infancy, histrionic, paranoid, schizoid and schizotypal personality disorders | 97.0%–98.6% | L5 | Hold | No supporting trials or relevant literature; likely graph-based artefacts. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

