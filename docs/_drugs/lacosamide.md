---
layout: default
title: Lacosamide
parent: Model Prediction Only (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lacosamide: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report (approved indicati…"
monitor_inn: "Lacosamide"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
---

# Lacosamide
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

## Lacosamide: From Epilepsy (Presumed) to Migraine Disorder
{: .text-alpha }

*Note: the data compiled for this report contain no approved-indication text for the Australian listing. The original indication is therefore not confirmed from the registry. Lacosamide is a recognised antiseizure medicine, but this is general knowledge, not a data-supported statement.*

## One-Sentence Summary

Lacosamide is an antiseizure medicine with one Australian listing, although the listing carries no indication text.
The TxGNN model predicts it may be effective for **migraine disorder** (the top-ranked prediction, manic bipolar affective disorder, has weaker evidence).
Migraine currently has **4 registered clinical trials** (3 Phase 3, 1 Phase 2) and **a published randomised double-blind trial (2026)** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (approved indication text is blank) |
| Predicted New Indication | Migraine disorder (the evidence-leading candidate; the top-ranked prediction is manic bipolar affective disorder, 99.96%) |
| TxGNN Prediction Score | 0.9987 (migraine disorder); 0.9996 (manic bipolar affective disorder) |
| Evidence Level | L5 (migraine disorder), by the compiled assessment. Strict application of the rules would give a lower level, since the Phase 3 trials are active-comparator or pilot designs and outcome data are unverified |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (migraine disorder) |

**Candidate overview.** Ten indications were predicted. Only migraine disorder has substantial clinical evidence.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Manic bipolar affective disorder | 0.9996 | L5 | Research Question |
| 2 | Tourette syndrome | 0.9995 | L5 | Hold |
| 3 | Trichotillomania | 0.9992 | L5 | Hold |
| 4 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9991 | L5 | Hold |
| 5 | **Migraine disorder** | 0.9987 | L1 | Proceed with Guardrails |
| 6 | Insomnia | 0.9983 | L5 | Hold |
| 7 | Migraine with brainstem aura | 0.9982 | L5 | Research Question |
| 8 | Myofascial pain syndrome | 0.9981 | L5 | Research Question |
| 9 | Obsessive-compulsive disorder | 0.9978 | L5 | Hold |
| 10 | Papillary conjunctivitis | 0.9972 | L5 | Hold |

The sections below focus on migraine disorder. Bipolar disorder is discussed briefly.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the literature, lacosamide enhances slow inactivation of voltage-gated sodium channels and may modulate collapsin response mediator protein 2 (CRMP2).

Migraine involves neuronal hyperexcitability and release of calcitonin gene-related peptide (CGRP) in the trigeminal system. Sodium channel blockade is plausibly relevant. In mice, lacosamide affected cortical spreading depolarisation, a standard model of migraine aura. Preclinical work also suggests it inhibits CGRP release via CRMP2. Other antiseizure medicines (such as topiramate) are already used for migraine prevention, which supports the biological reasonableness of the prediction.

For bipolar disorder, the same sodium channel mechanism is shared with mood-stabilising antiseizure drugs such as lamotrigine and carbamazepine. Clinical support is thin: a retrospective 30-day comparison, a 12-week open-label pilot in bipolar depression, and case reports. One case report describes lacosamide-precipitated neutropenia in a patient with bipolar disorder.

## Clinical Trial Evidence

Migraine disorder:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | Completed | 600 | Lacosamide vs propranolol in migraine; primary outcome is reduction in monthly migraine days and ≥50% responder rate |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | Unknown | 600 | Lacosamide vs topiramate in migraine, with the same outcome measures; no results confirmed |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 (labelled) | Completed | 200 | Randomised pilot of lacosamide 50 mg twice daily plus ibuprofen vs ibuprofen alone; serum CGRP measured (biomarker-focused) |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | Completed | 218 | Double-blind, placebo-controlled trial of lacosamide 100 and 300 mg/day for migraine prophylaxis; results not provided |

Other predicted indications:

| Indication | Trial | Phase | Status | Enrolment | Relevance |
|---|---|---|---|---|---|
| Myofascial pain syndrome | [NCT00401830](https://clinicaltrials.gov/study/NCT00401830) | Phase 2 | Completed | 159 | Placebo-controlled trial of 400 mg/day in fibromyalgia syndrome; outcomes not provided, so the indication match is uncertain |
| Obsessive-compulsive disorder | [NCT03271528](https://clinicaltrials.gov/study/NCT03271528) | Phase 1 | Completed | 66 | Alcohol craving in heavy drinkers; **not relevant to OCD** |

No Australian (ANZCTR) trial identifiers were available in the data compiled for this report. No clinical trials are registered for bipolar disorder.

## Literature Evidence

Migraine disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | RCT | Molecular Neurobiology | Lacosamide vs propranolol in episodic migraine; randomised double-blind trial of efficacy and safety as an alternative for patients who cannot tolerate propranolol |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | RCT | Acta Neurologica Belgica | Effect of lacosamide on serum CGRP levels in episodic migraine |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Systematic review / meta-analysis | Epilepsia | Adverse event profile of lacosamide across randomised trials (epilepsy populations) |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Preclinical (mouse) | J Headache Pain | Effect of lacosamide on cortical spreading depolarisation |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Preclinical | Pain Reports | (S)-Lacosamide in preclinical models of cephalic pain via CRMP2 and CGRP release |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Review | Expert Opin Emerg Drugs | Emerging treatments for chronic and refractory chronic migraine |

Bipolar disorder (for context):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide with other antiepileptics in bipolar disorder without epilepsy |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week trial of lacosamide in bipolar depression |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective cohort | Epilepsy Behav | Lacosamide effect on depression and anxiety symptoms in focal refractory epilepsy |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report | Indian J Psychol Med | Lacosamide-precipitated neutropenia in a patient with bipolar disorder and epilepsy |

For Tourette syndrome, the only relevant literature is a review of tics induced by antiepileptic drugs ([32804278](https://pubmed.ncbi.nlm.nih.gov/32804278/)), which points to a possible adverse effect rather than benefit.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10293R | Lacosamide ARX | Tablet 50 mg (oral) | Not stated in the data compiled for this report |

Only one single-ingredient, valid listing was identified. Other strengths and formulations were not found in the data compiled for this report.

## Safety Considerations

Warnings and contraindication text from the Australian Product Information were not available. Please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, atrial fibrillation, atrial flutter, coronary artery disease, myocardial ischaemia, atrioventricular block, sick sinus syndrome and familial sick sinus syndrome. These indicate cardiac conduction and rhythm concerns that should be checked against the PI.
- **Drug interactions:** 25 interactions were recorded; 20 are listed in the data compiled for this report. **Major:** dolasetron, ceritinib, siponimod. **Moderate (examples):** clarithromycin, ethanol, cobicistat, chloroquine, hydroxychloroquine, mefloquine, lidocaine, ketoconazole, pasireotide, alectinib, brigatinib, crizotinib, fingolimod, idelalisib, imatinib, ozanimod, sunitinib. Many involve additive effects on cardiac conduction (such as PR or QT prolongation), which is consistent with the cardiac signals above.
- **Literature signal:** a case report of neutropenia in a patient with bipolar disorder.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (migraine disorder). Hold for the other predicted indications without clinical support.**

**Rationale:**
- Migraine has a plausible mechanism, preclinical support, one completed Phase 2 placebo-controlled trial and a published 2026 randomised trial against propranolol. However, the Phase 3 trials are active-comparator or pilot designs, one has unknown status, and placebo-controlled results are unverified. Bipolar disorder remains a research question, and the remaining indications lack supporting evidence.

**To proceed, the following is needed:**
- Results of the Phase 2 placebo-controlled migraine trial (NCT00440518), and confirmation of outcomes and data provenance for the Phase 3 trials, given that several similar registrations with matching enrolment sizes exist
- The status of NCT06243692, and full-text review of PMID 41863672
- The Australian PI warnings and contraindications and the approved indication text, with a focus on cardiac conduction risk
- A cardiac screening and interaction-management plan, including ECG review for patients with conduction disease or on interacting drugs
- Mechanism of action data from DrugBank
- A decision on whether an Australian trial registration (ANZCTR) or PBS review would be needed for a migraine indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

