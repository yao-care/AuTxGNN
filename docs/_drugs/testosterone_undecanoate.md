---
layout: default
title: Testosterone Undecanoate
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Testosterone Undecanoate: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Hypogonadism"
monitor_inn: "Testosterone undecanoate"
predicted_indications: ["homozygous familial hypercholesterolemia", "androgen insensitivity syndrome", "Leydig cell hypoplasia due to LH resistance", "46,XY disorder of sex development due to impaired androgen production", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "telecanthus", "ovarian hyperstimulation syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 5"]
---

# Testosterone Undecanoate
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

## Testosterone Undecanoate: From Hypogonadism to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Testosterone undecanoate is an androgen replacement therapy, originally used to treat hypogonadism (including primary ovarian failure and hypogonadotropic hypogonadism).
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanism has been identified.
The prediction is model-based only, so the recommendation is **Hold**. A more credible direction is androgen insensitivity syndrome (see the note below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypogonadism (also primary ovarian failure and hypogonadotropic hypogonadism, per the knowledge graph); the ARTG entry carries no indication text |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 98.73% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Testosterone undecanoate is an ester prodrug of testosterone and acts through the androgen receptor. Its efficacy in hypogonadism comes from replacing deficient testosterone.

For homozygous familial hypercholesterolemia, no supporting mechanism has been identified. This condition is driven by LDL receptor dysfunction. Androgens generally lower HDL cholesterol and have inconsistent effects on LDL cholesterol, so there is no plausible link to this drug. The high TxGNN score reflects graph-based proximity only and should not be read as clinical support.

**Other predictions in the top 10 (for context):**
- **Androgen insensitivity syndrome (AIS, score 95.7%)** is the only prediction with published literature (L3). In partial AIS, residual receptor function may allow a high androgen dose to promote virilisation. In complete AIS the receptor is non-functional, so benefit from direct androgen action is not expected. This is a "Research Question".
- **Leydig cell hypoplasia due to LH resistance (94.5%)** and **46,XY disorder of sex development due to impaired androgen production (93.7%)** are mechanistically plausible (L4), but androgen replacement is already standard care, so these are arguably extensions of the existing hypogonadism indication rather than true repurposing.
- The remaining predictions (fragile X carrier symptoms, blepharophimosis-related conditions, telecanthus, ovarian hyperstimulation syndrome and partial chromosome 5p trisomy/tetrasomy) have no mechanistic or clinical support (L5, Hold). Testosterone could plausibly worsen ovarian hyperstimulation syndrome, so that indication also raises a safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered for homozygous familial hypercholesterolemia. No trials were found for the other top-ranked predictions either.

## Literature Evidence

Currently no related literature available for homozygous familial hypercholesterolemia.

For context, two publications were identified for the second-ranked prediction, androgen insensitivity syndrome:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39039878](https://pubmed.ncbi.nlm.nih.gov/39039878/) | 2024 | Clinical study in children (self-controlled design reported; full design not confirmed) | Zhonghua Er Ke Za Zhi | Evaluated the efficacy and safety of oral testosterone undecanoate in children with genetically diagnosed AIS at Beijing Children's Hospital (2009–2021) |
| [8246276](https://pubmed.ncbi.nlm.nih.gov/8246276/) | 1993 | Double-blind crossover study (4 patients) | Journal of Sex & Marital Therapy | Oral testosterone undecanoate (120 mg/day) versus placebo for 4 weeks in gonadectomised women with complete testicular feminisation; assessed hormone levels, mood, sociosexual functioning and body self-image (indirect evidence only) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10205D | Reandron 1000 | I.M. injection containing testosterone undecanoate 1,000 mg in 4 mL | Not stated in the data compiled for this report |

Only an injectable (intramuscular) product is listed. Both AIS studies above used oral testosterone undecanoate, so route compatibility would need to be assessed before any further work.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No interaction records were found in the data compiled for this report, and no disease-level contraindications were recorded.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Homozygous familial hypercholesterolemia is supported only by a graph-based prediction. There are no trials or publications, and the known effects of androgens on lipids do not fit the underlying LDL receptor defect.

**To proceed, the following is needed:**
- Mechanism of action data and TGA Product Information warnings and contraindications (both currently missing)
- A decision on whether to pursue the higher-evidence candidate (androgen insensitivity syndrome) instead, including verification of study design, sample size and AIS subtype from the full text of the 2024 paediatric study
- Assessment of route compatibility, as the registered Australian product is an injection while the AIS studies used oral dosing
- For Leydig cell hypoplasia and 46,XY DSD, confirmation of whether these fall within the existing hypogonadism indication rather than representing a new one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

