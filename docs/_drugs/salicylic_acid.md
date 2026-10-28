---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is a long-established keratolytic and anti-inflammatory agent, used for skin conditions such as acne, seborrhoeic dermatitis and tinea, and for inflammatory conditions such as rheumatoid arthritis and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 2 of 2) |
| Number of ARTG Entries | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, salicylic acid is thought to act through anti-inflammatory pathways (such as COX inhibition and NF-kB modulation), although the pharmacology source compiled for this report notes that public bioactivity data confirming a primary molecular target are lacking. It is already used for allergic and inflammatory conditions such as allergic rhinitis, which gives a loose, plausible link to allergic or inflammatory conjunctival disease.

There are important limits to this reasoning. Topical ocular use of salicylic acid is irritating and potentially unsafe, and no ocular-specific mechanism or data were available. The high TxGNN score reflects a computational prediction, not demonstrated benefit.

Other top-ranked predictions were also reviewed. Most (for example, genetic skeletal dysplasias such as brachyolmia, pseudoachondroplasia and acromesomelic dysplasia) have no plausible mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Two are worth noting:
- **Spondyloarthropathy (susceptibility)** is the most biologically coherent candidate, since NSAIDs are first-line therapy and salicylates are used in related joint conditions. This rationale is class-level only, and other NSAIDs are better established. It is flagged as a research question.
- **Rosacea conjunctivitis** has only a weak indirect rationale, with the same ocular irritation concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Two valid single-ingredient ARTG entries were identified. Product names, dosage forms and approved indication text were not available in the data compiled for this report.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 117E | Not available | Not available | Not available |
| ARTG 7928G | Not available | Not available | Not available |

## Safety Considerations

- **Pharmacology note**: The data list ASIC3 (an acid-sensing ion channel) as a pharmacological target of salicylic acid. This is not a drug-drug interaction in the usual clinical sense.
- **Ocular use**: Topical ocular application of salicylic acid is irritating and potentially unsafe, a key concern for the predicted conjunctival indications.

No label-based warnings or contraindications were available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests solely on a model score, with no clinical trials, no literature and a safety concern with ocular application. The evidence level is L5.

**To proceed, the following is needed:**
- Obtain the TGA Product Information for both ARTG entries to confirm approved indications, dosage forms, warnings and contraindications
- Detailed mechanism of action data, including ocular-relevant pharmacology
- Preclinical ocular tolerability and safety data for any conjunctival use
- A systematic literature search for salicylates or NSAIDs in allergic conjunctivitis
- Consideration of spondyloarthropathy as a better-grounded research question, using class-level NSAID evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

