---
layout: default
title: Risedronic Acid
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Risedronic Acid: predicted new indication Paget disease of bone (evidence level L5). Approved use: Osteoporosis, postmenopausal osteoporosis, Paget disease of bone"
monitor_inn: "Risedronic acid"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "osteomesopyknosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "Glanzmann thrombasthenia"]
---

# Risedronic Acid
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

## Risedronic Acid: From Osteoporosis to Paget Disease of Bone
{: .text-alpha }

## One-Sentence Summary

Risedronic acid is a nitrogen-containing bisphosphonate, originally used to treat osteoporosis (including postmenopausal osteoporosis) and Paget disease of bone.
The highest-scoring TxGNN predictions (pseudo-von Willebrand disease, platelet disorders, HIV) have no supporting evidence. The only prediction with literature support, **Paget disease of bone**, is already a listed original indication, so it is not true repurposing. It is backed by **3 review articles** and **no registered clinical trials** in the data compiled for this report.

**Note on indication selection:** The top-ranked prediction (rank 1) is pseudo-von Willebrand disease, with no trials, no literature and no plausible mechanistic link. This report therefore focuses on rank 9, Paget disease of bone, the only prediction with supporting literature and a clear mechanism. The other predictions are summarised below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, Paget disease of bone (the Australian ARTG entry carries no indication text in the data compiled) |
| Predicted New Indication | Paget disease of bone (rank 9; the rank 1 prediction is pseudo-von Willebrand disease, Hold) |
| TxGNN Prediction Score | 95.18% (rank 1 pseudo-von Willebrand disease: 98.93%) |
| Evidence Level | L4 (reviews only; no trials) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (Paget disease of bone only) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, risedronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase in osteoclasts, reducing bone resorption.

Paget disease of bone is driven by excessive, disorganised osteoclast-mediated bone remodelling. An antiresorptive agent that suppresses osteoclast activity is mechanistically well suited to it. Paget disease is also already among the drug's original indications, so this prediction mainly confirms existing use rather than identifying a new one. The early-onset genetic form (Paget disease of bone 2, rank 10, score 94.36%) shares osteoclast-mediated pathology and is plausible, but no subtype-specific evidence was found.

**Other top predictions are not supported:**

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 1 | Pseudo-von Willebrand disease | 98.93% | No evidence; no plausible mechanistic link (platelet GP1BA gain-of-function) |
| 2 | Primary release disorder of platelets | 98.90% | No evidence; likely a network-neighbour artefact |
| 3 | HIV infectious disease | 97.95% | No evidence; bisphosphonates are used for HIV-associated bone loss, which is a complication, not the infection |
| 4 | Neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter | 96.90% | Ultra-rare genetic disorder; no link |
| 5 | Osteomesopyknosis | 96.81% | Sclerosing bone condition; further antiresorption may be counterproductive |
| 6–7 | Feline AIDS; simian immunodeficiency virus infection | 96.62% | Veterinary/non-human models; not relevant |
| 8 | Glanzmann thrombasthenia | 96.05% | No evidence; no mechanistic link |

All of these are at evidence level L5 with a recommendation of Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered in the data compiled for this report (no ClinicalTrials.gov or ANZCTR entries).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11176760](https://pubmed.ncbi.nlm.nih.gov/11176760/) | 2001 | Review | Archives of Internal Medicine | Clinical review of risedronate; approved for prevention and treatment of postmenopausal and corticosteroid-induced osteoporosis |
| [17385948](https://pubmed.ncbi.nlm.nih.gov/17385948/) | 2007 | Review | Drugs | Zoledronic acid in Paget disease: a single 5 mg IV dose gave a higher response rate and faster bone turnover reduction than comparator (a different bisphosphonate, so indirect support only) |
| [15799218](https://pubmed.ncbi.nlm.nih.gov/15799218/) | 2002 | Review | Treatments in Endocrinology | Overview of the shift from symptomatic therapy to antiosteoclastic agents, with a focus on bisphosphonates in Paget disease |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13360E | Actonel | Tablet containing risedronate sodium 5 mg (oral) | Not available in the data compiled |

The licence number is reproduced as supplied and should be verified against the ARTG.

## Safety Considerations

**Contraindications flagged by the knowledge graph** (derived from drug-disease graph links, not product label text):
- Renal: kidney disease, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- Upper gastrointestinal: gastritis, duodenitis, achalasia and other oesophageal motility disorders (megaoesophagus, oesophageal dyskinesia)
- Mineral metabolism: hypercalcaemia, hyperparathyroidism, osteitis fibrosa, phosphorus metabolism disease
- Bone and other: osteonecrosis of the jaw, lytic metastatic bone lesions, sarcoidosis, fibromyalgia, myositis, constipation disorder, pyoureter

**Drug Interactions** (100 interactions recorded; the 20 listed are all Moderate):
- Polyvalent cation products, which reduce absorption: calcium salts (acetate, carbonate, citrate, gluconate, lactate, glubionate, phosphate), magnesium salts and antacids (aluminium hydroxide, magaldrate, magnesium hydroxide/oxide), iron, kaolin and attapulgite
- Acetylsalicylic acid
- Kanamycin

Dosing separation from these products should be checked against the Product Information. Please also refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Paget disease of bone only); Hold for all other predictions**

**Rationale:**
- Paget disease of bone has a clear mechanistic basis and is already a listed original indication, supported by three reviews. However, no trial data were supplied, so the evidence level is only L4.
- All higher-scoring predictions rest on graph scores alone with no evidence and no plausible mechanism, and should not proceed.

**To proceed, the following is needed:**
- Confirmation of the approved Australian indications, as the ARTG entry carries no indication text and the PI warnings and contraindications were not obtained
- Primary RCT evidence for risedronate specifically in Paget disease (the current reviews are partly about other bisphosphonates)
- Detailed mechanism of action data
- Renal function assessment and monitoring for osteonecrosis of the jaw and atypical fracture risk
- Subtype-specific evidence before considering early-onset Paget disease of bone 2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

