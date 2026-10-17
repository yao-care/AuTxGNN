---
layout: default
title: Chlorthalidone
parent: Model Prediction Only (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chlorthalidone: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension and congestive heart failure"
monitor_inn: "chlorthalidone"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but there are currently **no clinical trials** and **no relevant publications** supporting this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the ARTG entry has no indication text; indications are taken from the knowledge graph) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorthalidone is a thiazide-like diuretic whose efficacy in hypertension and congestive heart failure is well established. It lowers blood pressure and reduces fluid volume through effects on renal ion transport.

A diuretic could theoretically lower intraocular pressure through effects on ion transport or fluid balance. However, this is speculative and not supported by the data compiled for this report. Primary hereditary glaucoma is largely driven by genetic defects in aqueous outflow, so a systemic diuretic mechanism is not a clear fit. The high score (0.999) should be read as a model output, not as evidence of benefit.

**Other predictions** (all L5 unless noted, with no clinical trials):
- **Open-angle glaucoma** (99.90%): systemic diuretics are not an established therapy, and no link is evidenced.
- **Malignant hypertensive renal disease** (99.89%) and **malignant renovascular hypertension** (99.89%): blood pressure lowering is plausible, but these are largely extensions of the existing hypertension indication. Diuretics are not first-line in malignant hypertension, and in renovascular disease they may further stimulate renin.
- **Pulmonary hypertension** (two forms, 99.88%): at most an indirect role in relieving volume overload.
- **Chronic pulmonary heart disease** (99.82%): the only prediction with some indirect support (L4, "Research Question"), described below.
- **Braddock syndrome, acute pulmonary heart disease, congenital hypotrichosis milia**: no plausible mechanistic link and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (primary hereditary glaucoma), currently no related literature is available.

Literature was found only for lower-ranked predictions, and it is weak:

| PMID | Year | Type | Journal | Key Findings | Related Prediction |
|------|-----|------|------|---------|------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Clinical report (design unclear) | La Clinica terapeutica | Diuretic therapy with chlorthalidone in congestive heart failure caused by chronic cor pulmonale | Chronic pulmonary heart disease |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC. Heart Failure | Transition from hypertension to heart failure; supports the general rationale only | Chronic pulmonary heart disease |
| [14288313](https://pubmed.ncbi.nlm.nih.gov/14288313/) | 1965 | Basic research (insect physiology) | J Cell Comp Physiol | Ion transport in the Cecropia moth midgut; unrelated to human disease | Pulmonary hypertension due to lung disease |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13500M | Hygroton 25 | Tablet 25 mg (oral) | Not specified in the data compiled for this report |

## Safety Considerations

- **Contraindications and conditions of concern (from knowledge graph, not label text):** liver failure, kidney disease, anuria, gout, hyperuricaemia, type 2 diabetes mellitus, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, pancreatitis, peptic ulcer disease, systemic lupus erythematosus, asthma, psoriasis, epilepsy, anxiety and related disorders, myocardial infarction, sudden cardiac arrest, hemoglobinopathy and pyoureter. These are model-derived associations and should be verified against the Product Information.
- **Drug interactions:** 210 interactions were recorded. Those listed include:
  - **Major:** cisapride and dolasetron.
  - **Moderate:** acarbose, alogliptin, albiglutide and metformin (glycaemic control); hydrocortisone, dexamethasone, triamcinolone and beclomethasone (corticosteroids); amphotericin B; bupropion; morphine; omeprazole; rabeprazole; cholecalciferol.
  - **Minor:** doxycycline, hyoscyamine and atropine.

Warnings and contraindications from the TGA-approved Product Information were not available. Please refer to the Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hereditary glaucoma rests on a model score alone (L5), with no trials, no literature and no plausible mechanistic link. The only prediction with indirect support is chronic pulmonary heart disease (L4, a Research Question), and that evidence is a 1967 report of unclear design.

**To proceed, the following is needed:**
- Mechanism of action data for chlorthalidone
- Product Information warnings and contraindications for the Australian product, to enable safety screening
- Any preclinical or clinical evidence on intraocular pressure effects, if glaucoma is to be pursued
- A formal literature review on chlorthalidone in cor pulmonale or right heart failure, if that direction is prioritised
- Route and formulation compatibility assessment (currently pending; only an oral tablet is available)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

