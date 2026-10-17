---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 758
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma"]
---

# Tyrosine
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

# Tyrosine: From Unspecified Nutritional Use to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid and a precursor of catecholamines and thyroid hormones. It is marketed in Australia in oral dietary-management products, but no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (no approved indication text recorded for the ARTG entries) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tyrosine is a proteinogenic amino acid and the starting substrate for catecholamine synthesis (L-DOPA, dopamine, noradrenaline) and for thyroid hormone synthesis.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots, usually caused by disc herniation or other structural lesions, and is managed surgically. No plausible pathway links tyrosine supplementation to this condition. The high score (0.998) appears to be a knowledge-graph association only, and this report does not find it mechanistically credible.

The other top-ranked predictions show the same pattern:
- **Hyperthyroidism and hyperthyroxinemia:** Tyrosine is a thyroid hormone precursor, so supplementation would be expected to be neutral or unfavourable, not beneficial.
- **Glaucoma subtypes (angle-closure, traumatic, neovascular, aqueous misdirection):** These are largely anatomical or vascular disorders with no tyrosine link.
- **Resistance to thyroid hormone (THRB mutation):** This is a receptor defect that a hormone precursor would not address.
- **Postural orthostatic tachycardia syndrome:** There is a plausible indirect link via catecholamine synthesis, but the only publication is a case report using a tyrosine hydroxylase inhibitor, which acts in the opposite direction.

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

For context, one trial exists for the fourth-ranked prediction (hyperthyroidism):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Placebo-controlled trial of a zinc, selenium and L-tyrosine supplement to prevent thyrotoxicosis in adults with elevated TPOAb and the SEPP1 r25191G/A polymorphism. Tyrosine is not the sole active component, and no efficacy data are available. |

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

The literature retrieved for the other predictions is general and does not test tyrosine as an intervention:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism aetiology, diagnosis and management. No tyrosine-specific evidence. |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | Plasma amino acid alterations in early primary angle-closure glaucoma. Associative biomarkers only, not evidence of therapeutic benefit. |
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome case responding to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor. Opposite pharmacological direction, and not about POTS. |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Basic/genetic study | Endocrinology | THRB mutations at serine 314 impair ligand binding in thyroid hormone resistance. No tyrosine intervention. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma aetiopathogenesis and treatment. No tyrosine link. |

Note: several retrieved papers (for example PMID 24821006) concern tyrosine kinase inhibitors, which are a different drug class and unrelated to the amino acid.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9165J | Tyrosine 1000 | Oral powder sachets, 4 g (1 g tyrosine), 30 | Not available |
| ARTG 12015J | TYR Easy Tablet | Tablets containing 0.91 g protein, 462 | Not available |
| ARTG 10260B | TYR Anamix Junior | Oral powder sachets, 36 g, 30 | Not available |
| ARTG 14126L | TYR explore5 | Oral powder sachets, 12.5 g, 30 | Not available |
| ARTG 10934L | TYR Easy Shake & Go | Oral powder bottle, 34 g, 30 | Not available |

All five entries are valid single-ingredient listings with oral routes of administration.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction records were found, and no knowledge-graph contraindications were identified.

Tyrosine is a thyroid hormone precursor, so use in people with hyperthyroidism or other thyroid disorders warrants clinical caution.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome is supported only by a knowledge-graph score, with no clinical trials, no literature and no plausible mechanism. No other top-ranked prediction has supporting evidence either (all L4 to L5).

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking tyrosine to the proposed indication
- Approved indication text and Product Information (warnings and contraindications) for the ARTG entries
- Preclinical or clinical evidence in the target condition before any further evaluation
- Review of the top predictions for ontology artefacts (for example, the obsolete neurogenic bladder term) and for lexical false matches to tyrosine kinase inhibitors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

