---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Finasteride
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

# Finasteride: From Benign Prostatic Hyperplasia to Hypertrichosis

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** (top-ranked), but there are **no clinical trials** and **no publications** supporting this prediction. The most literature-supported prediction is **hypertrichosis** (4 narrative reviews or methods papers, none showing efficacy), so this report details the top-ranked prediction and notes the others.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (per the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Finasteride is generally known as a 5-alpha-reductase inhibitor that lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and BPH is a DHT-driven condition.

For Ambras syndrome, the mechanistic link is weak. It is a congenital genetic condition (chromosome 8q22 rearrangements affecting TRPS1 regulation) and is not known to be androgen-driven. The high TxGNN score appears to reflect network proximity in the knowledge graph (finasteride's links to hair-related conditions) rather than a plausible biological rationale.

**Other predictions reviewed (all rated Hold unless noted):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Hypertrichosis | 99.99% | L4 | Hypertrichosis is androgen-independent, so the fit is weak. The retrieved papers are narrative reviews and a methods paper, and none shows finasteride treats it. Any signal likely reflects overlap with hirsutism. |
| 3 | Malformation syndrome with odontal/periodontal component | 99.99% | L5 | No identified mechanistic link |
| 4 | Syndrome with Dandy-Walker malformation | 99.99% | L5 | No plausible mechanism. Fetal exposure risk. |
| 5 | Isolated genetic hair shaft abnormality | 99.99% | L5 | Inherited structural defects are not DHT-mediated |
| 6 | Familial isolated trichomegaly | 99.15% | L5 | Speculative follicle link |
| 7 | Prostate calculus | 98.60% | L4 | Classed as a Research Question. Any benefit would be a secondary effect of BPH treatment, not a distinct indication. |
| 8 | Persistent fetal circulation syndrome | 90.49% | L5 | No link. Not indicated in neonates. |
| 9 | Chronic thromboembolic pulmonary hypertension | 89.87% | L5 | No established mechanism |
| 10 | Migraine with brainstem aura | 88.84% | L5 | Speculative neurosteroid link only |

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

For the **prostate calculus** prediction, the literature was mostly BPH and bladder-stone studies (for example, [PMID 12137828](https://pubmed.ncbi.nlm.nih.gov/12137828/), nonsurgical BPH management in men with bladder calculi, and the 2025 JAMA review [PMID 40658396](https://pubmed.ncbi.nlm.nih.gov/40658396/) on lower urinary tract symptoms in men). None shows that finasteride treats prostatic calculi directly.

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
- If pursued, consider the prostate calculus prediction only as a research question tied to BPH management, and the hair-related predictions only with clear mechanistic justification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

