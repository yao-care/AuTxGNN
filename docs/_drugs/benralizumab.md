---
layout: default
title: Benralizumab
parent: Model Prediction Only (L5)
nav_order: 83
evidence_level: L5
indication_count: 5
monitor_inn: "Benralizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
last_modified_at: 2026-11-24
description: "Benralizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Benralizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Benralizumab: anti-IL-5Rα monoclonal antibody → Thrombocytopenia due to immune destruction
{: .text-alpha }

## One-Sentence Summary

Benralizumab is a monoclonal antibody that targets the IL-5 receptor alpha subunit and depletes eosinophils and basophils. The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, with a score of 0.9934. However, **no clinical trials and no publications** currently support this specific prediction, so it rests on computational prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab binds the IL-5 receptor alpha subunit (IL5RA) and depletes eosinophils and basophils through antibody-dependent cellular cytotoxicity (ADCC). According to the Mechanism of Action section of the US FDA-approved prescribing information for benralizumab: "Benralizumab is a humanized afucosylated, monoclonal antibody (IgG1, kappa) that directly binds to the alpha subunit of the human interleukin-5 receptor (IL-5Rα) with a dissociation constant of 11 pM. The IL-5 receptor is expressed on the surface of eosinophils and basophils." ([DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784), label version 2026-05-13; accessed 2026-11-20.)

A link to immune-mediated thrombocytopenia is speculative. It could involve Th2/eosinophil-related immune dysregulation, but no direct mechanism is established from the available data. The high TxGNN score is a computational output only and should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for thrombocytopenia due to immune destruction.

---

## Literature Evidence

Currently no related literature available for thrombocytopenia due to immune destruction.

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 11994G | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |
| 11995H | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |
| 11996J | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |
| 11997K | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |
| 11999M | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |
| 12000N | Fasenra Pen | Benralizumab | Injection 30 mg in 1 mL single dose pre-filled pen | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacological one, with the target IL-5 receptor alpha subunit (IL5RA), which is the intended target of benralizumab. No drug–drug interaction with another medicine is listed.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials, publications or established mechanism, so it sits at evidence level L5.

**To proceed, the following is needed:**
- Mechanistic studies linking IL-5Rα/eosinophil biology to immune thrombocytopenia
- Preclinical or case-level evidence in immune thrombocytopenia
- Warnings and contraindications from the TGA Product Information
- Detailed mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism of action data is not otherwise available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

