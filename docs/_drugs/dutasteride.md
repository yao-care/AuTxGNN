---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dutasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Dutasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

## Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Dutasteride is a 5-alpha reductase inhibitor originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction, so the evidence rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (source: TxGNN knowledge graph; no approved indication text is recorded in the ARTG data compiled for this report) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Dutasteride is generally known as a dual inhibitor of 5-alpha reductase types 1 and 2, which lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and its effect on hair follicles through DHT reduction is the only plausible bridge to hair-related conditions.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital hypertrichosis caused by genomic rearrangements affecting *TRPS1* expression, and it is not clearly androgen-driven. The prediction therefore appears to rest on a very high model score and a general anti-androgen effect on hair follicles, not on direct pharmacological or clinical evidence.

Other top-ranked predictions show a similar pattern:

- **Hair-related conditions** (hypertrichosis, isolated genetic hair shaft abnormality, hypotrichosis simplex of the scalp, congenital hypotrichosis milia, familial isolated trichomegaly): mechanistically plausible only via hair-follicle biology. Most are not clearly DHT-dependent, and the direction of effect is uncertain. For generalised hypertrichosis, dutasteride could even be counterproductive.
- **Hypotrichosis simplex of the scalp** is phenotypically similar to androgenetic alopecia, for which dutasteride has an off-label evidence base, but its genetic cause is not clearly DHT-dependent.
- **Diffuse alopecia areata** is autoimmune (T-cell-mediated, JAK-STAT pathway) and not DHT-driven.
- **Structural or neurological conditions** (malformation syndrome with odontal/periodontal component, Dandy-Walker malformation syndrome, migraine with brainstem aura): no plausible mechanistic link was identified, and these scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the top-ranked prediction (Ambras type hypertrichosis universalis congenita).

For context, one paper was retrieved for a lower-ranked prediction (diffuse alopecia areata). It concerns a different condition and is not evidence for dutasteride in alopecia areata:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Review | American Journal of Clinical Dermatology | Narrative review of androgenetic alopecia in women, covering pathophysiology, clinical evaluation and treatments. It affects nearly 50% of women in their lifetime and is often underdiagnosed and undertreated. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10095H | APO-Dutasteride | Capsule 500 micrograms | Not recorded in the data compiled for this report |

---

## Safety Considerations

- **Contraindications and disease associations (knowledge-graph derived, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, intraoperative floppy iris syndrome.
- **Reproductive safety**: dutasteride is teratogenic in male fetuses, as it interferes with external genitalia development. This argues against use in congenital or paediatric settings.
- **Drug Interactions**: 100 interactions were identified in total. The main ones rated Moderate are:
  - Aprepitant
  - Cimetidine
  - Clarithromycin
  - Clotrimazole
  - Miconazole

  Others, such as pantoprazole, omeprazole, metformin, simvastatin and prednisone, have an unknown severity rating.

Please also refer to the TGA-approved Product Information (PI) for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or literature (Evidence Level L5). The mechanistic link is speculative, because Ambras syndrome is not clearly androgen-driven. The drug is also teratogenic in male fetuses, which complicates use in a congenital condition.

**To proceed, the following is needed:**
- Mechanism of action data confirming a rationale for *TRPS1*-related hypertrichosis
- Preclinical or case-level evidence of any effect on hair growth in this condition
- Review of the TGA Product Information for warnings and contraindications
- A safety assessment for the relevant (likely paediatric) population
- Consideration of better-supported hair-related targets, such as androgen-dependent conditions, before investing in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

