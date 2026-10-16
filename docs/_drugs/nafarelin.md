---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nafarelin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Endometriosis"
monitor_inn: "Nafarelin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "pelvic organ prolapse", "syndrome with a Dandy-Walker malformation as major feature", "physiological sexual disorder", "female genital tuberculosis", "isolated genetic hair shaft abnormality", "centra precocious puberty 1", "dysplasia of cervix"]
---

# Nafarelin
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

# Nafarelin: From Endometriosis to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Nafarelin is a GnRH (gonadotropin-releasing hormone) agonist originally used to treat endometriosis and central precocious puberty.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis; precocious puberty (the Australian licence record contains no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nafarelin is a GnRH agonist. Continuous exposure desensitises pituitary GnRH receptors, which suppresses LH and FSH and lowers sex steroids. This is the basis for its use in endometriosis and central precocious puberty.

The link to the predicted indication is weak. Ambras syndrome is a congenital hypertrichosis associated with genomic rearrangements affecting regulation of the *TRPS1* gene. It is not a GnRH-driven or sex-steroid-driven process. The high score (99.87%) is a model output, not evidence of benefit. No mechanistic link has been established.

**Other predictions (all Hold unless noted):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malformation syndrome with odontal/periodontal component | 99.77% | L5 | No plausible mechanism |
| 3 | Hypertrichosis | 99.77% | L5 | Weak and indirect; hypertrichosis is androgen-independent |
| 4 | Pelvic organ prolapse | 99.77% | L5 | Hypoestrogenism would be expected to worsen, not help |
| 5 | Dandy-Walker malformation syndrome | 99.75% | L5 | Structural defect, no plausible mechanism |
| 6 | Physiological sexual disorder | 99.75% | L4 | Only an endometriosis pain paper, which is already a labelled use |
| 7 | Female genital tuberculosis | 99.75% | L5 | No antimycobacterial effect |
| 8 | Isolated genetic hair shaft abnormality | 99.73% | L5 | No established link |
| 9 | Central precocious puberty 1 | 99.70% | L4 | Strong mechanistic fit, but effectively on-label rather than repurposing (Research Question) |
| 10 | Dysplasia of cervix | 99.65% | L5 | HPV-driven; no established role for GnRH agonists |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (nor for the other nine predictions in the data compiled for this report).

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For the rank 6 prediction (physiological sexual disorder), one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7951404](https://pubmed.ncbi.nlm.nih.gov/7951404/) | 1994 | Clinical study (design not verifiable) | Int J Fertil Menopausal Stud | Compared nafarelin with danazol for dysmenorrhoea, dyspareunia and pelvic pain in endometriosis. This is an already-labelled use, so it is only indirect evidence. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2962X | Synarel | Nasal spray (pump pack), 200 micrograms (as acetate) per dose, 60 doses | Not available in the data compiled for this report |

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

Additional signals from the knowledge graph (not label text) list the following conditions as contraindication-related: hypertension, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, osteoporosis (including postmenopausal), obesity (including monogenic obesity), and substance abuse/dependence. These should be verified against the PI.

**Drug interactions:** The interaction query returned only a pharmacological target record (the GnRH1 receptor, the drug's intended target), not a drug-drug interaction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Ambras type hypertrichosis universalis congenita rests only on a model score. There are no trials or publications, and no plausible mechanism, since the condition is a genetic, non-hormonal disorder. Nafarelin is already marketed in Australia (Synarel, ARTG 2962X), but this does not support the new indication.

**To proceed, the following is needed:**
- A mechanistic rationale connecting GnRH agonism to *TRPS1*-related hypertrichosis
- Mechanism of action data for nafarelin
- Retrieval of the TGA Product Information, including warnings and contraindications, to complete safety screening
- Preclinical or case-level evidence in Ambras syndrome or related hypertrichosis
- If a related direction is of interest, central precocious puberty is the best-supported prediction. It is effectively an existing use, so the question is one of label alignment rather than repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

