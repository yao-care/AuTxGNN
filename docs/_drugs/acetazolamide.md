---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Open-angle glaucoma, angle-closure glaucoma, altitude sickness…"
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
---

# Acetazolamide
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

## Acetazolamide: From Glaucoma and Altitude Sickness to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is an oral carbonic anhydrase inhibitor, originally used for glaucoma, altitude sickness, congestive heart failure and absence epilepsy.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, angle-closure glaucoma, altitude sickness, congestive heart failure, absence epilepsy (the ARTG entry has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Acetazolamide is known as a carbonic anhydrase inhibitor, and this class alters acid-base balance and fluid handling. That is the basis of its use in glaucoma, altitude sickness and heart failure.

A possible link to exercise-induced malignant hyperthermia would be through effects on acid-base balance and muscle ion handling. This is speculative. No clinical trials or publications in the data compiled for this report support it, and the high score reflects a computational prediction only.

The other top-ranked predictions are also unsupported. Most have no evidence at all. Cardiomyopathy has only indirect evidence (reviews on heart failure, case reports and one animal study). Intestinal obstruction has case reports suggesting acetazolamide may cause ileus rather than treat it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for exercise-induced malignant hyperthermia.

For context, the next-ranked prediction, hypertrophic cardiomyopathy, has three publications, none of which addresses that condition directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | General update on heart failure management; not specific to acetazolamide or hypertrophic cardiomyopathy |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Overview of new cardiovascular drugs in 2022; no acetazolamide-specific finding |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | J Cardiol Cases | Acetazolamide used for hypochloremia in an advanced heart failure patient who also had hypertrophic cardiomyopathy |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1004W | Diamox | Tablet 250 mg (oral) | Indication text not available |

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text):** liver failure, liver disease, kidney disease, renal tubular acidosis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), respiratory failure, haematologic disease, gout, gallbladder disease, pyoureter, type 1 and type 2 diabetes mellitus, and diabetic ketoacidosis.
- **Drug Interactions:** The query returned 100 interactions, and the first 20 are listed in the data compiled for this report. The main ones are:
  - **Major:** acetylsalicylic acid (aspirin), cisapride.
  - **Moderate:** antidiabetic agents (acarbose, acetohexamide, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide), amphotericin B formulations, corticosteroids (beclomethasone, betamethasone, dexamethasone), and laxatives (bisacodyl, castor oil).
  - **Minor:** doxycycline.
- **Signals from the retrieved literature:** case reports describe adynamic ileus and non-cardiogenic pulmonary oedema after intravenous acetazolamide. Cirrhosis is a particular concern, as acetazolamide can precipitate hyperammonaemia and encephalopathy.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications for exercise-induced malignant hyperthermia, and evidence for the other top predictions is absent, indirect, or points to possible harm (ileus).

**To proceed, the following is needed:**
- Mechanism of action data to assess a plausible link to the predicted indication
- Targeted literature and trial searches on carbonic anhydrase inhibition in malignant hyperthermia and related muscle disorders
- TGA Product Information, including approved indications, warnings and contraindications, for the Diamox ARTG entry
- A safety review for the relevant populations, especially those with liver, kidney or adrenal disease and those taking aspirin or antidiabetic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

