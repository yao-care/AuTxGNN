---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 1 and type 2 diabetes mellitus"
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analogue, originally used to treat type 1 and type 2 diabetes mellitus (including diabetic ketoacidosis).
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only signal and should not be treated as a therapeutic lead without further evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 and type 2 diabetes mellitus (the ARTG entry in the data compiled for this report has no indication text; the indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a long-acting insulin analogue whose efficacy in diabetes mellitus is well established. There is no evidence that it acts on ovarian autoimmunity.

The only plausible link is indirect. Autoimmune oophoritis can occur alongside polyglandular autoimmune syndromes, which may include type 1 diabetes. In that setting, insulin would treat the coexisting diabetes, not the ovarian condition. The high TxGNN score is therefore likely driven by shared autoimmune and diabetes associations in the knowledge graph, not by a therapeutic mechanism.

Other top-ranked predictions show similar patterns:
- **Stiff person syndrome and focal stiff limb syndrome:** anti-GAD65 autoimmunity commonly co-occurs with type 1 diabetes.
- **Thiamine-responsive dysfunction syndrome and pancreatic agenesis:** insulin treats the associated diabetes. This is standard care, not true repurposing.
- **Localized lipodystrophies:** injected insulin is itself a known cause of injection-site lipodystrophy, so these predictions may reflect an adverse-effect association.
- **Opsismodysplasia:** a speculative link through INPPL1 (SHIP2), a regulator of insulin signalling, with no evidence that insulin alters the skeletal phenotype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For context, the only literature retrieved among the top 10 predictions relates to pancreatic agenesis (rank 6). None of these papers is a controlled study of insulin glargine in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Practical aspects of starting insulin therapy in type 2 diabetes |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes associated with endocrine disorders and new treatments |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 case treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Cohort (veterinary) | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11302W | Toujeo Solostar | Injection (human analogue), cartridges, 300 units per mL, 1.5 mL, 5 | Not available in the data compiled for this report |

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** 100 interactions were identified. Most of those listed are Moderate severity, and a few are Minor. Examples include:
- **Glucose-lowering agents (additive hypoglycaemia risk or altered glycaemic control):** metformin, pioglitazone, alogliptin, albiglutide
- **Sympathomimetics and bronchodilators (may blunt glycaemic control or mask hypoglycaemia):** epinephrine, salbutamol, formoterol, pseudoephedrine, phenylephrine
- **Beta-blocker:** acebutolol
- **Corticosteroids:** hydrocortisone (Moderate); topical hydrocortisone and alclometasone (Minor)
- **Others:** ethanol, hydrochlorothiazide, acetazolamide, doxycycline, ethinylestradiol, estradiol, alpelisib

A further consideration is that injected insulin can itself cause injection-site lipodystrophy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis rests solely on a model score, with no trials or literature, and no known therapeutic mechanism for insulin glargine in this condition. The other top-ranked predictions are either standard diabetes care or possible adverse-effect associations, not novel repurposing opportunities.

**To proceed, the following is needed:**
- Mechanism of action data for insulin glargine, and a mechanistic rationale for ovarian autoimmunity
- A systematic literature search for insulin or glucose-lowering therapy in autoimmune oophoritis and polyglandular autoimmune syndromes
- Safety information (warnings and contraindications) from the TGA-approved Product Information
- Confirmation of the approved indication and route compatibility for the ARTG entry
- If the aim is a clinically useful direction, re-ranking predictions to exclude those explained by diabetes comorbidity or insulin adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

