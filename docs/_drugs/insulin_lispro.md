---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "Insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Lispro: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Insulin Lispro: Autoimmune oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue, originally used to treat type 1 and type 2 diabetes mellitus, including diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting human insulin analogue. Its efficacy in diabetes is well established, but it has no known immunomodulatory action relevant to ovarian autoimmunity.

The most plausible explanation for the prediction is a shared autoimmune context. Autoimmune oophoritis often occurs within polyglandular autoimmune syndromes that include type 1 diabetes. This is an association between diseases, not a therapeutic mechanism, so the link is unsupported by any evidence compiled for this report.

Other high-scoring predictions (ranks 2 to 10) show similar patterns:
- **Comorbidity-driven signals:** thiamine-responsive dysfunction syndrome, classic stiff person syndrome and focal stiff limb syndrome. Insulin would treat the coexisting diabetes only, not the underlying disease.
- **Likely false positives:** drug-induced localized lipodystrophy, pressure-induced localized lipoatrophy and idiopathic localized lipodystrophy. Insulin injections are themselves a recognised cause of localised lipodystrophy.
- **Hormone replacement:** pancreatic agenesis. Insulin replacement is standard care, but it falls under the existing diabetes indication and is not a novel repurposing.
- **Biological hypothesis only:** opsismodysplasia (INPPL1/SHIP2, a negative regulator of insulin signalling). The direction and clinical relevance of exogenous insulin are unknown.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For context, the only publication retrieved across the top 10 predictions concerns pancreatic agenesis (rank 7) and is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | General review of insulin therapy in type 2 diabetes and practical aspects of starting it; does not address pancreatic agenesis directly |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11645X | Humalog U200 Kwikpen | Injection (human analogue), pre-filled pen, 200 units per mL, 3 mL, pack of 5 | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified in total; the 20 retrieved are mostly Moderate, with a few Minor. The main ones are:
  - **Other glucose-lowering agents (additive hypoglycaemia risk or altered glycaemic control):** metformin, alogliptin and albiglutide.
  - **Sympathomimetics and beta-agonists (may reduce glycaemic control):** epinephrine, salbutamol, formoterol, phenylephrine and pseudoephedrine.
  - **Beta-blockers (may mask hypoglycaemia symptoms):** acebutolol.
  - **Corticosteroids (may raise blood glucose):** hydrocortisone, plus the Minor topical hydrocortisone and alclometasone.
  - **Hormonal agents:** estradiol, ethinylestradiol and levonorgestrel.
  - **Others:** acetazolamide, hydrochlorothiazide, doxycycline, alpelisib and ethanol.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5), with no trials or publications. The likely link is a shared autoimmune context with type 1 diabetes, and insulin lispro has no known mechanism against ovarian autoimmunity. Several other top predictions are comorbidity artefacts or likely false positives, such as insulin-induced lipodystrophy.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic rationale for autoimmune oophoritis
- A systematic literature search for any link between insulin therapy and autoimmune oophoritis
- Product Information (PI) warnings and contraindications for the Australian product
- Confirmation of the approved indication text for the ARTG entry
- Assessment of whether any benefit would simply be management of coexisting diabetes rather than a true new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

