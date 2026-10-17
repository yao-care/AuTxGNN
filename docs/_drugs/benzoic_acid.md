---
layout: default
title: Benzoic Acid
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Benzoic Acid: predicted new indication Bronchitis (evidence level L5). Approved use: Pemphigus, Peyronie disease, penile fibromatosis…"
monitor_inn: "Benzoic acid"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dry eye syndrome", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "hereditary angioedema with C1Inh deficiency", "posterior leukoencephalopathy syndrome", "C1 inhibitor deficiency"]
---

# Benzoic Acid
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

# Benzoic Acid: From Fibrotic and Autoimmune Skin Conditions to Bronchitis

## One-Sentence Summary

Benzoic acid is listed in the TxGNN knowledge graph against fibrotic and autoimmune skin conditions such as Peyronie disease, scleroderma, pemphigus and dermatomyositis.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and only **2 publications** were retrieved, and neither studies benzoic acid itself.
This is a model prediction only (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pemphigus, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans, scleroderma, localised scleroderma, systemic sclerosis, dermatomyositis (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benzoic acid is a simple aromatic carboxylic acid. The original indications come from knowledge graph links rather than from approved label text, so the basis for its original use is unclear.

The retrieved literature does not support a link between benzoic acid and bronchitis. One paper is a review of repaglinide in type 2 diabetes, a drug that contains a benzoic acid derivative. The other is a preclinical study of a soluble epoxide hydrolase inhibitor in smoke-induced COPD. Neither tests benzoic acid. The high score (0.9998) reflects graph proximity only.

Other top-ranked predictions are more coherent with the original indications. Palmar fibromatosis (Dupuytren disease), Ledderhose disease and infantile digital fibromatosis all share fibrotic pathology with Peyronie disease and scleroderma. These are also prediction-only, without trials or literature. Predictions for diabetic retinopathy, dry eye syndrome, hereditary angioedema and posterior leukoencephalopathy syndrome have no direct evidence or no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | Drugs | Repaglinide (a benzoic acid derivative) in type 2 diabetes. Not about benzoic acid or bronchitis. |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Preclinical/Animal study | Am J Respir Cell Mol Biol | A soluble epoxide hydrolase inhibitor in smoke-induced COPD. Does not involve benzoic acid. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 105M | Not available | Not available | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

The knowledge graph lists the following conditions as contraindications for benzoic acid. These come from graph edges, not from label text, and should be verified against the PI:
- **Cardiovascular:** hypertension, coronary artery disease, sudden cardiac arrest, heart conduction disease, cardiovascular disease
- **Hepatic, renal and gastrointestinal:** liver failure, liver disease, kidney disease, pyoureter, gallbladder disease, gastritis, achalasia, megaesophagus
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, glycogen storage disease, cystinuria, galactosemia, anorexia nervosa
- **Haematological:** blood coagulation disease, haemophilia, anaemia, macrocytic anaemia, G6PD deficiency
- **Neuromuscular and urological:** myasthenia gravis, adult-onset myasthenia gravis, neuromuscular junction disease, benign prostatic hyperplasia

No drug interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. No trials were found, and the two retrieved papers do not study benzoic acid. The ARTG entry has no indication or dosage form, so the product cannot be matched to a route or use for bronchitis.

**To proceed, the following is needed:**
- Mechanism of action data for benzoic acid
- The TGA Product Information, including warnings and contraindications, and details of the ARTG entry (dosage form, route, indication)
- Targeted literature and trial searches for benzoic acid itself in bronchitis, and in the fibrotic conditions (palmar fibromatosis, Ledderhose disease), which are more plausible candidates
- Assessment of route compatibility for any proposed new indication
- Verification of the knowledge graph contraindications against label text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

