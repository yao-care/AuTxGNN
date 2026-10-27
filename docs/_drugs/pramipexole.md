---
layout: default
title: Pramipexole
parent: Moderate Evidence (L3-L4)
nav_order: 594
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Pramipexole: predicted new indication Attention deficit-hyperactivity disorder (evidence level L4). Approved use: Parkinson disease and restless legs syndrome"
monitor_inn: "Pramipexole"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "specific developmental disorder", "chondromyxoid fibroma", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "schizophrenia", "atypical glycine encephalopathy"]
---

# Pramipexole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Pramipexole: From Parkinson Disease and Restless Legs Syndrome to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Pramipexole is a dopamine agonist originally used to treat **Parkinson disease** and **restless legs syndrome**.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but the supporting evidence is thin: **no registered clinical trials** and only **7 publications**, none of which tests pramipexole in ADHD directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and restless legs syndrome (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Pramipexole is known to be a non-ergot dopamine agonist that prefers D2/D3 receptors. Its efficacy in Parkinson disease and restless legs syndrome reflects that dopaminergic activity.

ADHD is a condition in which dopamine signalling is thought to be dysregulated. The literature also links ADHD to variants of the dopamine D4 receptor gene. This gives the prediction a plausible but indirect mechanistic rationale.

Direct support is very limited. It consists of one case report of ADHD with chronic pain and oral dysesthesia treated with atomoxetine plus pramipexole, and one randomised trial in Tourette's syndrome, a related neurodevelopmental condition. The remaining retrieved papers concern restless legs syndrome, a different drug (piribedil) or basic receptor biology.

**Other predictions:** Among the other predicted indications, **schizophrenia** (TxGNN rank 9 in this list) has stronger evidence. It has a Phase 3 add-on trial (NCT01320982, 400 participants, status unknown, no results available) and a published 16-week randomised placebo-controlled trial of add-on pramipexole (PMID 35921506). It is outside the scope of this report, but it may merit a separate assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ADHD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22407510](https://pubmed.ncbi.nlm.nih.gov/22407510/) | 2012 | RCT (Tourette's syndrome, adjacent indication) | Movement Disorders | Multicentre, placebo-controlled trial of pramipexole in Tourette's syndrome, based on the idea that dopamine agonists could normalise central dopamine hypersensitivity |
| [37342213](https://pubmed.ncbi.nlm.nih.gov/37342213/) | 2023 | Case report | Frontiers in Pain Research | Remission of chronic low back pain and oral dysesthesia in a patient with comorbid ADHD treated with atomoxetine and pramipexole |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical | Pharmacological Research | Dopamine D4 receptor variants and α2A adrenoceptors form heteromers, with implications for ADHD and impulse-control disorders |
| [19412489](https://pubmed.ncbi.nlm.nih.gov/19412489/) | 2006 | Review | Neuropsychiatric Disease and Treatment | Pramipexole is a D3-selective non-ergoline agonist with potential use in restless legs syndrome |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | Review of restless legs syndrome (indirect relevance) |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Clinical study | Clinical Neuropharmacology | Piribedil compared with pramipexole and ropinirole for vigilance in Parkinson disease (different drug and condition) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 14324X | SIMIPEX XR | Extended-release tablet containing pramipexole dihydrochloride monohydrate 375 micrograms (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph:** These come from drug-disease links in the TxGNN knowledge graph (PrimeKG), not from product label text. They include:
  - multiple system atrophy
  - orthostatic hypotension
  - postural orthostatic tachycardia syndrome
  - drug-induced dyskinesia
  - kidney disease
  - psychotic disorders (psychotic disorder, schizoaffective disorder, schizophreniform disorder, mental disorder)
  - melanoma
  - sleep disorders (obstructive sleep apnoea, sleep apnoea syndrome, congenital central hypoventilation syndrome, narcolepsy)
  - other central nervous system diseases
- **Drug Interactions:** 100 interactions were identified in total. Those graded **Moderate** include morphine (including liposomal), opium, cimetidine, dronabinol, nabilone and metoclopramide. Ranitidine is graded Minor. Several others, such as metformin, omeprazole and pantoprazole, have an unknown severity grade.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the prediction rests on a plausible dopaminergic mechanism, one case report and an adjacent Tourette's trial. No trial has tested pramipexole in ADHD. Several knowledge-graph contraindications involve psychiatric and sleep conditions that commonly accompany ADHD, so safety needs careful attention.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to support the mechanistic-link analysis
- The TGA Product Information, to complete safety screening (warnings and contraindications)
- ADHD-specific clinical evidence, such as a well-designed pilot or randomised trial
- A safety plan for impulse-control disorders, sleepiness and psychiatric adverse effects in ADHD populations
- Confirmation of the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

