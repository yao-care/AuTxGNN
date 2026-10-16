---
layout: default
title: Potassium Permanganate
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Potassium Permanganate: predicted new indication Benign prostatic hyperplasia (evidence level L5). Approved use: Not available"
---

# Potassium Permanganate
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

# Potassium Permanganate: From an Unspecified Original Indication to Benign Prostatic Hyperplasia

## One-Sentence Summary

Potassium permanganate is a topical oxidising antiseptic and astringent, and no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**, but there are **0 clinical trials** and only **2 publications** (pathology studies that do not test the drug), so the prediction is not supported by real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the single ARTG entry has no indication text) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 97.66% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, potassium permanganate is a topical oxidising antiseptic and astringent. Its mechanism is generally understood as oxidation of microbial and tissue proteins, and no effect on prostatic growth or androgen signalling is known.

The data compiled for this report found **no credible mechanistic link** between the drug and BPH. The two retrieved papers concern amyloid deposits in prostatic corpora amylacea and seminal vesicle amyloidosis, and neither involves potassium permanganate as a treatment. The high TxGNN score most likely reflects a knowledge-graph association, probably via amyloid-related nodes, rather than a pharmacological rationale.

The other top-ranked predictions are similarly unsupported. These include alopecia, congestive heart failure, osteoarthritis, hypotrichosis, pulmonary hypertension and alopecia areata. Most have no evidence at all. Where literature exists, it concerns amyloid pathology staining, toxicology or experimental models, not therapeutic use. Systemic exposure to permanganate is toxic.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1385482](https://pubmed.ncbi.nlm.nih.gov/1385482/) | 1992 | Pathology study | J Clin Pathol | Immunohistological study of amyloid in prostatic corpora amylacea; does not test the drug |
| [9431316](https://pubmed.ncbi.nlm.nih.gov/9431316/) | 1997 | Case report / pathology | Arch Pathol Lab Med | Localised seminal vesicle amyloidosis in men treated hormonally for prostate carcinoma; does not test the drug |

Neither publication evaluates potassium permanganate as a BPH therapy.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 420D | Not available | Not available | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

Note: the data compiled for this report found no drug interaction records. Systemic exposure to permanganate is known to be toxic, so any non-topical use would need careful toxicological assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on the model score alone (Evidence Level L5). There are no clinical trials, the retrieved literature does not involve the drug as a treatment, and no plausible mechanism links a topical oxidising antiseptic to BPH.

**To proceed, the following is needed:**
- Approved indication text and product details for the ARTG entry, plus the TGA Product Information with warnings and contraindications
- Mechanism of action data (for example from DrugBank) and a credible pharmacological rationale for prostatic tissue
- Preclinical evidence of benefit in BPH models
- A toxicology and route-of-administration assessment, since the drug is a topical antiseptic and systemic exposure is hazardous
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

