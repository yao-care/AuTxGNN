---
layout: default
title: Benzydamine
parent: Model Prediction Only (L5)
nav_order: 88
evidence_level: L5
indication_count: 1
monitor_inn: "Benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
last_modified_at: 2026-11-24
description: "Benzydamine: predicted new indication benign prostatic hyperplasia (disease) (evidence level L5). In Australia: 3 PBS items (3 currently listed)"
---

# Benzydamine
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

## Benzydamine: topical NSAID-like anti-inflammatory agent → benign prostatic hyperplasia (benign prostatic hyperplasia (disease))
{: .text-alpha }

## One-Sentence Summary

Benzydamine is a locally acting anti-inflammatory and analgesic agent, supplied in Australia as a mouth and throat rinse.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (disease)**,
but there are currently **no clinical trials and no publications** supporting this direction, so the prediction is model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | benign prostatic hyperplasia (disease) |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of benzydamine as: Cyclooxygenase inhibitor ([ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610), CC BY-SA 3.0; accessed 2026-11-19.) Benzydamine is generally described as a locally acting agent with anti-inflammatory, analgesic and local anaesthetic properties, including reduced production of pro-inflammatory cytokines such as TNF-alpha and IL-1beta and membrane-stabilising effects.

A possible, but unverified, link to benign prostatic hyperplasia is the role that chronic prostatic inflammation and lower urinary tract symptoms may play in disease progression. This link is hypothetical and is not supported by any study or data compiled for this report.

The very high TxGNN score (0.9926) is a computational output only. It may partly reflect patterns in the underlying data, particularly given the absent mechanism annotation, and should not be read as evidence of efficacy. Route compatibility is also unassessed: the only Australian product is an oral rinse, not a formulation designed for prostatic or systemic delivery.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1121B | Difflam | Benzydamine | Mouth and throat rinse containing benzydamine hydrochloride 22.5 mg per 15 mL, 500 mL | Valid |
| 5032W | Difflam | Benzydamine | Mouth and throat rinse containing benzydamine hydrochloride 22.5 mg per 15 mL, 500 mL | Valid |
| 5385K | Difflam | Benzydamine | Mouth and throat rinse containing benzydamine hydrochloride 22.5 mg per 15 mL, 500 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications addressing benign prostatic hyperplasia, and no mechanism data to support it. The only Australian product is a mouth and throat rinse, which is not an obvious route for this use.

**To proceed, the following is needed:**
- Mechanism of action data for benzydamine and a plausible pathway to prostatic tissue
- Preclinical or clinical studies directly addressing benign prostatic hyperplasia
- Assessment of route and formulation feasibility, since only a mouth and throat rinse is currently supplied
- Product Information warnings and contraindications to enable safety screening

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

