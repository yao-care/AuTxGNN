---
layout: default
title: Thyrotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Thyrotropin Alfa: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Thyrotropin alfa"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
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

# Thyrotropin alfa: From Thyroid Diagnostic/Adjunctive Use to Migraine Disorder

## One-Sentence Summary

Thyrotropin alfa is recombinant human thyroid-stimulating hormone (TSH), marketed in Australia as Thyrogen; no approved indication text was available in the data compiled for this report. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Thyrotropin alfa is a recombinant form of human TSH that acts on TSH receptors in thyroid tissue.

There is no established mechanistic link between TSH receptor stimulation and migraine. The high TxGNN score most likely reflects proximity in the knowledge graph (for example, shared gene or pathway neighbours) rather than a validated biological rationale. Any link to migraine is speculative.

The other top-ranked predictions are not independent support. Migraine with brainstem aura, and migraine with or without aura (susceptibility), are closely related to the parent migraine prediction. Several others (Raynaud disease, pulmonary hypertension, postural orthostatic tachycardia syndrome) have only loose associations with thyroid status, not with TSH administration. Hyperthyroidism scored highly but is biologically contradictory, since TSH stimulation would be expected to worsen it. It should be treated as a warning signal, not a candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2700D | Thyrogen | Powder for injection 0.9 mg, 2 | Not available in the compiled data |

## Safety Considerations

**Drug Interactions:** 45 potential interactions were identified, all graded Moderate in the DDInter database. The 20 listed in the compiled data are all glucose-lowering agents, including:
- Biguanides and sulfonylureas: metformin, chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide
- Insulins: human insulin and insulin aspart (including aspart protamine)
- GLP-1 receptor agonists: albiglutide, dulaglutide, exenatide, semaglutide
- DPP-4 inhibitors: alogliptin, saxagliptin
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Alpha-glucosidase inhibitor: acarbose

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

Mechanism-based concerns noted in the prediction analysis: thyrotropin alfa can transiently raise thyroid hormone levels and may cause tachycardia. This is relevant to several of the predicted cardiovascular indications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanistic link between TSH receptor agonism and migraine. Safety information from the product label has not been reviewed.

**To proceed, the following is needed:**
- Review of the TGA-approved Product Information (PI) for warnings, contraindications and approved indications
- Mechanism of action data (for example, from DrugBank)
- A biological rationale connecting TSH signalling to migraine, supported by preclinical or observational evidence
- Confirmation of route and dosing feasibility (the product is an injectable powder for diagnostic or adjunctive use)
- A cardiovascular safety assessment, given transient thyroid hormone elevation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

