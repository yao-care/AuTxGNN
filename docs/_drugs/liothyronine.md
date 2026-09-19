---
layout: default
title: Liothyronine
parent: Moderate Evidence (L3-L4)
nav_order: 399
evidence_level: L3
indication_count: 10
---

# Liothyronine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Liothyronine: From Hypothyroidism to Nodular Goiter (TSH-Suppressive Therapy)

## One-Sentence Summary

Liothyronine (T3, synthetic triiodothyronine) was originally used as a hormone replacement therapy for hypothyroidism.
The TxGNN model's original ranking placed **renal hypodysplasia/aplasia** as the first predicted indication, but this candidate lacks any clinical evidence and is classified as **Hold**; after filtering by evidence quality, the actual candidate with clinical and literature support and an assessment conclusion of "Proceed with Guardrails" is **nodular goiter**—this represents an existing clinical practice of TSH suppression by thyroid hormone to reduce thyroid nodule size, not a novel mechanistic hypothesis, supported by **2 related clinical trials** (neither using liothyronine as the intervention drug) and **20 publications**.

> ⚠️ Clarification: The predicted indications ranked 1–2, 4–8, and 10 in this Evidence Pack (renal hypodysplasia, bilateral renal aplasia, Carney complex, peripheral chondrodysplasia, Potter sequence, acrodysostosis, angiomyxoma/myxoma, scalp simple hair loss) were individually reviewed and found to be TxGNN knowledge graph similarity extrapolation, keyword mismatches, or literature findings opposite to the therapeutic hypothesis, with evidence level L5 and recommendation Hold; they lack reportable value and are therefore excluded. This report focuses on the nodular goiter candidate with the highest evidence level.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypothyroidism (Evidence Pack does not provide TFDA/ARTG product information text; this is the internationally recognized indication for liothyronine) |
| Predicted New Indication | Nodular Goiter |
| TxGNN Prediction Score | 99.94% (original rank 1192) |
| Evidence Level | L3 |
| Australian Market Status | Not marketed |
| ARTG Registry Entries | 0 |
| Recommendation Decision | Proceed with Guardrails |

## Why Is This Prediction Reasonable?

Complete mechanism of action data for liothyronine has not yet been obtained (Evidence Pack marked as Data Gap, DG002, severity High). However, based on established pharmacological consensus, liothyronine is a thyroid hormone receptor agonist clinically used in TSH-suppressive therapy for benign nodular goiter—the principle is to reduce pituitary TSH secretion, thereby decreasing TSH-mediated stimulation of thyroid tissue and inhibiting nodule growth.

In other words, this is not a novel hypothesis uncovered by TxGNN, but rather an extension of existing clinical practice consistent with its original indication (hormone replacement for hypothyroidism). It is particularly important to note that TSH-suppressive therapy itself carries known risks: atrial fibrillation and other cardiovascular events, as well as bone loss—this is why this report recommends "conditional advancement (Guardrails)" rather than direct "Go".

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | NA | Completed | 68 | Evaluation of dill (Anethum graveolens) extract effects on hormone, inflammatory markers, and ultrasound nodule size in patients with thyroiditis and nodular goiter. **Note: Intervention drug is herbal extract, not liothyronine; disease area overlap only (relevance rating C)**. |
| [NCT02665325](https://clinicaltrials.gov/study/NCT02665325) | N/A | Unknown | 100 | Assessment of cognitive function and mood in differentiated thyroid cancer patients receiving postoperative L-thyroxine TSH-suppressive therapy. **Note: Drug is L-thyroxine, not liothyronine; indication is postoperative TSH suppression rather than primary nodular goiter; trial status unclear (relevance rating C)**. |

Currently, the Evidence Pack contains **no clinical trials using liothyronine as the intervention drug directly targeting nodular goiter**; the above two entries are provided only for disease area background reference.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38278171](https://pubmed.ncbi.nlm.nih.gov/38278171/) | 2024 | Review | Lancet | Overview of hyperthyroidism, covering pathophysiology and diagnosis of toxic nodular goiter |
| [37434815](https://pubmed.ncbi.nlm.nih.gov/37434815/) | 2023 | Cohort | Am J Transl Res | Correlation analysis of urinary iodine concentration with thyroid function indices in nodular goiter patients |
| [34980104](https://pubmed.ncbi.nlm.nih.gov/34980104/) | 2022 | Cohort | Environ Health | Case-control study of perchlorate and iodine exposure on risk of nodular goiter and thyroid tumors |
| [28915531](https://pubmed.ncbi.nlm.nih.gov/28915531/) | 2017 | Review | Horm Metab Res | Subclinical hyperthyroidism (including TSH-suppressive therapy context) and cardiovascular disease risk |
| [25297557](https://pubmed.ncbi.nlm.nih.gov/25297557/) | 2014 | Review | J Endocrinol | Spontaneous feline hyperthyroidism as an animal model for human toxic nodular goiter |
| [10426591](https://pubmed.ncbi.nlm.nih.gov/10426591/) | 1999 | Prospective study | Endocr J | Levothyroxine suppressive therapy for diffuse and nodular goiter in euthyroid patients, evaluating thyroid/nodule volume changes |
| [21524033](https://pubmed.ncbi.nlm.nih.gov/21524033/) | 2011 | Review | Am Fam Physician | Subclinical hyperthyroidism (including etiology of nodular goiter) updated review |
| [28671443](https://pubmed.ncbi.nlm.nih.gov/28671443/) | 2017 | Review | Am Fam Physician | Timing considerations in treatment of subclinical hyperthyroidism |
| [36818930](https://pubmed.ncbi.nlm.nih.gov/36818930/) | 2022 | Review | Acta Clin Croat | Amiodarone and thyroid dysfunction (involving thyroid hormone regulatory mechanisms) |
| [27510349](https://pubmed.ncbi.nlm.nih.gov/27510349/) | 2016 | Review | Med J Aust | Primary care management of thyroid disease, including TSH interpretation principles |

The above literature predominantly comprises observational and review articles; **intervention studies directly using liothyronine (rather than levothyroxine) for nodular goiter** are not currently identified in this Evidence Pack.

## Australian Market Information

The Evidence Pack indicates that Liothyronine is currently **not marketed in Australia** (ARTG registry entries: 0), with no product information to be listed.

## Safety Considerations

- **Drug-Drug Interaction Query**: DDI database query result was "not found"; no specific list of interactions obtained.
- **Product Information Warnings/Contraindications**: Evidence Pack marked as data gap (DG001, severity Blocking); safety preliminary assessment (S1) cannot be completed at present.

Since this drug is not marketed in Australia and product information data on warnings, contraindications, and interactions are all missing, **please defer safety assessment until TGA-approved product information (PI) is obtained**.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TSH-suppressive therapy mechanism for nodular goiter is clear and represents an extension of existing clinical practice rather than a novel hypothesis, with evidence level reaching L3; however, the lack of intervention trials directly using liothyronine, the drug's current absence from the Australian market, and the Blocking data gap in product information safety data preclude a direct "Go" decision.

**To proceed further, the following must be completed:**
- TFDA/TGA product information warnings and contraindications data (DG001, Blocking, priority completion for S1 safety preliminary assessment)
- Complete mechanism of action (MOA) data to strengthen mechanistic association analysis (DG002)
- Direct intervention trial evidence for liothyronine (not levothyroxine) use in nodular goiter
- Complete drug-drug interaction database query results
- If market advancement in Australia is being considered, confirmation of ARTG registration pathway and available formulations

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

