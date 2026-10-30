---
layout: default
title: Polyethylene Glycol
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "polyethylene glycol"
predicted_indications: ["congenital ichthyosiform erythroderma"]
description: "Polyethylene Glycol: predicted new indication Congenital ichthyosiform erythroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Polyethylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Polyethylene Glycol: Congenital ichthyosiform erythroderma
{: .text-alpha }

## One-Sentence Summary

Polyethylene glycol (PEG) is used as an osmotic laxative for constipation and as a lubricant in eye drops for dry eye syndrome.
The TxGNN model predicts it may be effective for **Congenital Ichthyosiform Erythroderma**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, polyethylene glycol is a hydrophilic polymer used as an osmotic laxative and as an ocular lubricant, and its efficacy in constipation and dry eye is established. Whether this applies to congenital ichthyosiform erythroderma is unproven.

One plausible but unverified rationale is that PEG is a humectant-type polymer. In topical or emollient vehicles it may hydrate the stratum corneum and help with the scaling and dryness typical of this condition.

There are important limits to this reasoning. PEG's marketed uses are not mechanistically linked to the keratinisation defects (for example, TGM1, ALOX12B and ALOXE3 mutations) that cause this disease. The only support for the prediction is the high TxGNN score, so it should be treated as a hypothesis to test, not as a finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13100L | Systane | Eye drops 4 mg-3 mg per mL, single dose units 0.8 mL, 30 | Not stated in the data compiled for this report |

The only registered product is an ophthalmic preparation. No topical dermatological formulation is listed, so route compatibility with the predicted skin indication has not been established.

## Safety Considerations

- **Contraindications (TxGNN model associations, not label text):** The TxGNN model (deep learning) links PEG-containing products to contraindications in several disease groups. These come from the model's learned similarities between related diseases, not biological evidence, and may reflect other PEG formulations (such as bowel preparations) rather than the eye drops:
  - Cardiovascular and renal: hypertension, congestive heart failure, cardiovascular disease, kidney disease, anuria
  - Gastrointestinal: ileus, paralytic ileus, intestinal obstruction, toxic megacolon, pyloric stenosis, familial visceral myopathy, appendicitis
  - Metabolic and endocrine: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hyperthyroidism, Graves disease, thyrotoxicosis
  - Neurological: epilepsy
  - Ocular: angle-closure glaucoma, eye infections, conjunctivitis
  - Other: pyoureter
- **Drug Interactions:** No interaction records were found.

Please refer to the TGA-approved Product Information (PI) for warnings and verified contraindications for any specific product.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no mechanistic data. The mechanistic link to the underlying keratinisation defects is weak, and no suitable topical product is registered in Australia.

**To proceed, the following is needed:**
- Mechanism of action data for PEG and a plausible link to the disease biology
- A systematic literature and trial registry search (including ANZCTR) for PEG in ichthyosis
- Preclinical or early clinical evidence of benefit, for example PEG-containing emollients in ichthyosis
- Assessment of route and formulation, since only an ophthalmic product is registered
- Product Information warnings and contraindications for relevant products
- Review of the knowledge-graph contraindications against the intended formulation and patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

