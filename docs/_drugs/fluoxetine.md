---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluoxetine: predicted new indication Schizoid personality disorder (evidence level L5). Approved use: Not stated in the Australian licence record"
monitor_inn: "Fluoxetine"
predicted_indications: ["schizoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder", "paranoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants", "melancholia"]
---

# Fluoxetine
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

# Fluoxetine: From Depression and Anxiety Disorders to Schizoid Personality Disorder

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) originally used for depressive, anxiety, obsessive-compulsive and eating disorders. The TxGNN model predicts it may be effective for **schizoid personality disorder**, but **no clinical trials** and only **2 publications** (a general review and a depression cohort study) relate to this prediction, so the high score rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence record; the knowledge graph lists major depressive disorder, bulimia nervosa, obsessive-compulsive disorder, anxiety disorder and related mood disorders |
| Predicted New Indication | Schizoid personality disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Fluoxetine is known to be an SSRI, and its efficacy in depression, anxiety and obsessive-compulsive disorder is established. A serotonergic mechanism could plausibly help affective or anxiety symptoms that co-occur with cluster A personality disorders.

However, no direct evidence supports efficacy in schizoid personality disorder itself. The same score (99.92%) was given to several personality disorders (histrionic, schizotypal, paranoid), which suggests the prediction reflects knowledge-graph similarity rather than disorder-specific evidence.

**Other predictions reviewed (for context):**

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Schizotypal personality disorder | 99.92% | L3 | Small, older, uncontrolled fluoxetine studies (1991, 1998); a safety signal (transient psychosis with polydipsia) |
| Agoraphobia | 99.86% | L3 | Fluoxetine panic disorder studies and a 2023 network meta-analysis; overlaps with existing anxiety use |
| Manic bipolar affective disorder | 99.64% | L2 | Evidence supports bipolar depression, not mania; risk of mood switching with antidepressants |
| Phobic disorder | 99.63% | L1 | Phase 3 childhood social phobia trial (NCT00043537); partly within existing use |
| Melancholia | 99.57% | L2 | A subtype of major depression, so effectively existing use |
| Histrionic personality disorder, paranoid personality disorder, benign paroxysmal torticollis of infancy, Ohdo syndrome | 99.89%–99.92% | L4–L5 | No credible mechanistic link or only indirect evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for schizoid personality disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews pharmacological treatment of cluster A personality disorders (paranoid, schizoid, schizotypal); these patients tend to be isolative and have reduced quality of life |
| [16390895](https://pubmed.ncbi.nlm.nih.gov/16390895/) | 2006 | Cohort | American Journal of Psychiatry | Course of illness and predictors in depressed patients treated for 6 months; not specific to schizoid personality disorder |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1434L | FLUOTEX | Capsule 20 mg (as hydrochloride) | Not available in the data compiled |

---

## Safety Considerations

**Contraindication-related conditions flagged in the knowledge graph** (these are graph-derived associations, not product label text):
- Mood and psychiatric: bipolar disorder, major affective disorder
- Neurological and cerebrovascular: epilepsy, stroke and cerebrovascular disorders, cerebral infarction
- Cardiovascular: myocardial infarction, coronary thrombosis, orthostatic hypotension, hypotensive disorders, postural orthostatic tachycardia syndrome, multiple system atrophy
- Hepatic and metabolic: liver failure, liver disease, cirrhosis, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity
- Haematological: neutropenia, agranulocytosis, blood coagulation disease
- Other: benign prostatic hyperplasia, female breast carcinoma

**Drug interactions** (100 interactions recorded; examples):
- **Major:** bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron, cisapride
- **Moderate:** acetylsalicylic acid (aspirin), morphine, clarithromycin, famotidine, loperamide, chlorpropamide, dronabinol, eluxadoline

**Related literature signal:** a case report describes transient psychosis with psychogenic polydipsia in a schizotypal patient taking fluoxetine (PMID 9664779).

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for schizoid personality disorder is supported only by the model score. There are no registered trials, no disorder-specific fluoxetine data, and only indirect literature, so the evidence level is L5.
- Of the predictions reviewed, schizotypal personality disorder and agoraphobia are the more promising research questions, though neither is yet ready for practice change.

**To proceed, the following is needed:**
- Mechanism of action data and a disorder-specific biological rationale
- Targeted literature review of SSRI use in cluster A personality disorders, with controlled studies if available
- Australian Product Information (warnings, contraindications, approved indications) to complete safety screening
- Review of the schizotypal personality disorder evidence (including the psychosis signal) before any further work on the cluster A group
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

