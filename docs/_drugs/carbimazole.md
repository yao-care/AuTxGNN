---
layout: default
title: Carbimazole
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 2
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-11-24
description: "Carbimazole: predicted new indication resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Carbimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Carbimazole: thyroid peroxidase inhibitor (antithyroid drug) → resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Carbimazole is an antithyroid drug that is metabolised to methimazole and lowers thyroid hormone production.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but **no clinical trials** and only **1 publication** (a diagnostic case report) are linked to this prediction, and the mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of carbimazole as: Thyroid peroxidase inhibitor ([ChEMBL CHEMBL508102 (carbimazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL508102), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, carbimazole acts through its active metabolite methimazole, which inhibits thyroid peroxidase and so reduces the synthesis of thyroid hormone.

In resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-beta), the core problem is reduced tissue sensitivity to thyroid hormone, producing high thyroxine with a non-suppressed TSH. Lowering hormone production would be expected to raise TSH further and could worsen goitre. The mechanistic rationale is therefore weak and potentially counterproductive, and the high model score should be read with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report / review | BMJ Case Reports | A young man with persistently elevated free T4 and non-suppressed TSH was labelled hyperthyroid for 10 years and intermittently treated with carbimazole. The article describes the diagnostic pattern, not a treatment benefit. |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1153Q | Neo-Mercazole | Carbimazole | Tablet 5 mg | Valid |
| 13967D | Neo-Mercazole | Carbimazole | Tablet 5 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials. The single publication is a diagnostic case report with no evidence of treatment benefit, and the mechanism suggests antithyroid therapy could be counterproductive in this condition. No cited study directly shows benefit, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether any plausible benefit exists
- Evidence that reducing thyroid hormone synthesis is beneficial in RTH-beta, rather than raising TSH and worsening goitre
- Safety information from the TGA-approved Product Information (warnings and contraindications)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL508102 (carbimazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL508102) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

