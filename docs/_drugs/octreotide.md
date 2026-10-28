---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 518
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Octreotide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Acromegaly, hyperpituitarism, carcinoid syndrome"
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
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

## Octreotide: From Acromegaly to Vulvar Inverted Follicular Keratosis
{: .text-alpha }

## One-Sentence Summary

Octreotide is a somatostatin analogue originally used to treat acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **no clinical trials and no publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly, hyperpituitarism, carcinoid syndrome (the ARTG entry has no approved indication text recorded, so these come from the knowledge graph) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Octreotide is a somatostatin analogue, and its efficacy in acromegaly and carcinoid syndrome is established. However, nothing in the data compiled for this report links it mechanistically to the predicted new indication.

Vulvar inverted follicular keratosis is a benign skin lesion. No somatostatin-pathway involvement has been identified, and no clinical trials or literature support a role for somatostatin receptor agonism here. The high score (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions reviewed.** The other top-10 predictions are also weakly supported:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Seborrheic keratosis | 0.9955 | L5 | No evidence; benign epidermal lesion |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (vulvar inverted follicular keratosis).

For reference, the literature retrieved for lower-ranked predictions is not supportive:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17984930](https://pubmed.ncbi.nlm.nih.gov/17984930/) | 2007 | Case report | Neuro Endocrinol Lett | ACTH response to octreotide in a probable corticotropic adenoma in a patient with Addison's disease. This reflects pituitary receptor biology, not a treatment effect on adrenal failure (Addison disease prediction) |
| [1973178](https://pubmed.ncbi.nlm.nih.gov/1973178/) | 1990 | Physiological/clinical study | J Endocrinol Invest | Somatostatin and octreotide did not acutely affect hypothalamic-pituitary-adrenal function in patients with corticotropin hypersecretion (negative finding) |
| [7627336](https://pubmed.ncbi.nlm.nih.gov/7627336/) | 1995 | Diagnostic imaging study | Eur J Endocrinol | 99mTc-DMSA imaging in pituitary adenomas; not a treatment study |
| [11194482](https://pubmed.ncbi.nlm.nih.gov/11194482/) | 2000 | Case series | Recenti Prog Med | Pituitary pathology in elderly patients; does not evaluate octreotide (adrenocortical insufficiency prediction) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10533J | Sandostatin LAR | Injection (modified release) 20 mg (as acetate), vial and diluent syringe | Not recorded in the data compiled for this report |

## Safety Considerations

No label-based warnings or contraindications were available. Please refer to the TGA-approved Product Information (PI) for safety information.

**Contraindication-related conditions from the knowledge graph (not label text):**
hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, hypothyroidism (including myxedema and congenital hypothyroidism), liver disease and cirrhosis, gallbladder disease (cholelithiasis, cholecystolithiasis, choledocholithiasis), ileus, intestinal obstruction, sudden cardiac arrest, heart conduction disease, kidney failure, uremia and vitamin B12 deficiency.

**Drug Interactions:**
The interaction query returned 100 interactions. The 20 listed are all rated Moderate, and the main group is glucose-lowering agents, where glycaemic control may be affected:
- Insulins (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, human inhaled)
- GLP-1 receptor agonists (albiglutide, dulaglutide, semaglutide)
- DPP-4 inhibitors (alogliptin, linagliptin)
- SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
- Sulfonylureas (chlorpropamide, glimepiride)
- Others (acarbose, metformin)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no registered trials, no relevant publications and no plausible mechanistic link, so the evidence level is L5. The same holds for the other nine predictions.

**To proceed, the following is needed:**
- Mechanism of action data for octreotide (currently unavailable), and a biological rationale connecting somatostatin receptor signalling to the predicted condition
- Evidence of somatostatin receptor expression in the target tissue, plus preclinical or case-level data
- The ARTG approved indication text and the TGA Product Information, to complete the safety screening
- A review of the knowledge-graph contraindications and the diabetes-related interactions against the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

