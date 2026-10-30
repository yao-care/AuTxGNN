---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Trihexyphenidyl: predicted new indication Attention deficit-hyperactivity disorder (evidence level L4). Approved use: Parkinson disease and related parkinsonian and dystonic disorders"
monitor_inn: "Trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Trihexyphenidyl
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

## Trihexyphenidyl: From Parkinson Disease to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic medicine, originally used to treat Parkinson disease and related movement disorders such as parkinsonism and dystonia.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **no clinical trials** and only **1 publication** (a case series that does not test ADHD treatment) supporting this direction. The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian and dystonic disorders (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trihexyphenidyl is a central muscarinic (M1-preferring) antagonist that modulates the balance between cholinergic and dopaminergic signalling in the striatum. This is the basis of its use in Parkinson disease and dystonia.

Altered dopaminergic and cholinergic signalling has been implicated in ADHD, and in the tic and dystonia conditions that often co-occur with it. This gives a plausible but indirect link to the original indications.

There are also reasons for caution. Anticholinergic effects on attention and memory argue against use in ADHD. The only retrieved publication concerns tic disorder with dystonia, not ADHD treatment. The high TxGNN score should be read as a hypothesis for investigation, not as evidence of benefit.

Other predictions in the ranked list were also reviewed:
- **ADHD, inattentive type:** the same indirect rationale applies, with no supporting evidence.
- **PLA2G6-associated neurodegeneration:** the most biologically plausible candidate in the list, because adult-onset dystonia-parkinsonism overlaps with trihexyphenidyl's established symptomatic uses. Any benefit would be symptomatic only, and the evidence is limited to a case report. It is flagged as a research question.
- **Faciodigitogenital syndrome, congenital glycosylation disorder, polymicrogyria syndrome, retinal dystrophy, myelitis, Charcot-Marie-Tooth type 1G and Rasmussen encephalitis:** no mechanistic link or supporting evidence was identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series | Movement Disorders | Clinical series of primary tic disorder with persistent dystonia. ADHD appears only as a comorbidity. It provides no evidence of trihexyphenidyl efficacy in ADHD. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1109J | Artane | Tablet containing trihexyphenidyl hydrochloride 2 mg (oral) | Not available |

## Safety Considerations

Safety information specific to the label was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

- **Conditions linked to contraindication or caution (knowledge-graph data, not label text):**
  - Eye: open-angle and angle-closure glaucoma.
  - Gastrointestinal: paralytic ileus, achalasia and megaoesophagus, hiatus hernia, ulcerative colitis and inflammatory bowel disease, gastric ulcer, *Clostridium difficile* colitis, necrotising enterocolitis.
  - Genitourinary and organ function: benign prostatic hyperplasia, kidney disease, liver disease, gallbladder disease.
  - Cardiovascular and respiratory: hypertension, hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest, COPD.
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease.
- **Drug Interactions:** 100 interactions were identified, and the 20 reviewed include:
  - **Major:** potassium citrate and potassium chloride.
  - **Moderate:** other anticholinergic or antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, mepenzolate, methscopolamine), as well as loperamide, morphine, metoclopramide, prucalopride, eluxadoline, pramlintide, dronabinol, nabilone and magnesium hydroxide.
- **Indication-specific concerns:**
  - Anticholinergic cognitive effects (impaired attention and memory) are directly relevant to ADHD.
  - Anticholinergics may lower the seizure threshold, which matters for Rasmussen encephalitis.
  - Effects on accommodation and intraocular pressure are relevant to retinal conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction rests on a high model score and an indirect mechanistic link only. There are no registered trials and no publication testing trihexyphenidyl in ADHD. Known anticholinergic effects on attention and memory work against the proposed use.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank).
- TGA Product Information warnings and contraindications for Artane, as the safety data were incomplete.
- A systematic literature search for direct evidence of trihexyphenidyl in ADHD, tic disorders and dystonia-parkinsonism.
- For PLA2G6-associated neurodegeneration, a targeted review or case series of symptomatic trihexyphenidyl use in dystonia-parkinsonism.
- A safety assessment of anticholinergic cognitive effects, particularly in children and adolescents.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

