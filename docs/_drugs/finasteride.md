---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Finasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Finasteride: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** (top-ranked), but there are **no clinical trials** and **no publications** supporting this prediction. The most literature-supported prediction is **hypertrichosis** (4 narrative reviews or methods papers, none showing efficacy), so this report details the top-ranked prediction and notes the others.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Finasteride is generally known as a 5-alpha-reductase inhibitor that lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and BPH is a DHT-driven condition.

For Ambras syndrome, the mechanistic link is weak. It is a congenital genetic condition (chromosome 8q22 rearrangements affecting TRPS1 regulation) and is not known to be androgen-driven. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions reviewed (all rated Hold unless noted):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Hypertrichosis | 0.9999 | L5 | Hypertrichosis is androgen-independent, so the fit is weak. The retrieved papers are narrative reviews and a methods paper, and none shows finasteride treats it. Any signal likely reflects overlap with hirsutism. |
| 3 | Malformation syndrome with odontal/periodontal component | 0.9999 | L5 | No identified mechanistic link |
| 4 | Syndrome with Dandy-Walker malformation | 0.9999 | L5 | No plausible mechanism. Fetal exposure risk. |
| 5 | Isolated genetic hair shaft abnormality | 0.9999 | L5 | Inherited structural defects are not DHT-mediated |
| 6 | Familial isolated trichomegaly | 0.9915 | L5 | Speculative follicle link |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predictions.

## Literature Evidence

Currently no related literature available for Ambras type hypertrichosis universalis congenita.

For the next-ranked prediction, **hypertrichosis**, the following publications were retrieved. None demonstrates that finasteride treats hypertrichosis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de Dermatologie et de Vénéréologie | Hypertrichosis (non-androgen-dependent areas) differs from hirsutism. Adult causes are often iatrogenic, metabolic, nutritional or paraneoplastic. |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Reviews new treatments for androgenetic alopecia and hirsutism. |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Finasteride for male pattern hair loss and laser hair removal for hypertrichosis and hirsutism. |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods | Der Hautarzt | TrichoScan digital hair analysis tool. Not a treatment study. |


## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14191X | Finpro | Tablet 5 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: Liver disease and gallbladder disease are flagged in the TxGNN knowledge graph.
- **Drug Interactions**: The interaction query returned 100 entries, all with an unclassified severity level. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, pantoprazole, metformin, omeprazole and morphine. Severity and clinical significance need to be confirmed against the Product Information.
- **Fetal risk**: Finasteride carries a risk of male external genital abnormalities with in-utero exposure. This is relevant to the congenital and neonatal predictions.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone. There are no clinical trials, and the retrieved literature does not show that finasteride treats any predicted condition. The top-ranked condition is a congenital genetic disorder with no plausible androgen-driven mechanism.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) to support a mechanistic-link analysis
- TGA Product Information warnings and contraindications, and the approved indication text for the ARTG entry
- Clinical review of the severity of the flagged drug interactions
- A targeted literature search for finasteride in hypertrichosis and hirsutism to separate real signal from hirsutism overlap
- If pursued, consider the hair-related predictions only with clear mechanistic justification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

