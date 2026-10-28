---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-28
description: "Levothyroxine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Not recorded in the local data"
---

# Levothyroxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Levothyroxine: Renal hypodysplasia/aplasia
{: .text-alpha }

## One-Sentence Summary

Levothyroxine is a thyroid hormone replacement, recorded in the knowledge graph for hypothyroidism and thyroid-related conditions.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but **no clinical trials and no publications** were found to support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

Other predictions were bilateral renal agenesis (0.9960), Potter sequence (0.9933) and Carney complex (0.9918). None has any supporting trial or publication.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Levothyroxine is a synthetic thyroid hormone, and its use in thyroid disease is recorded in the knowledge graph.

Thyroid hormone has a recognised role in kidney development in animal models, which gives a loose biological rationale. However, renal hypodysplasia/aplasia is a structural malformation that arises in utero. Giving levothyroxine after birth is not expected to reverse it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. One recorded thyroid cancer entry (familial papillary thyroid carcinoma with renal papillary neoplasia) links thyroid and renal disease nodes. This is a computational artefact rather than a therapeutic signal.

The related predictions are also weak:
- **Bilateral renal agenesis:** a lethal structural anomaly with no plausible mechanism for levothyroxine to restore absent kidney tissue.
- **Potter sequence:** a downstream consequence of renal failure or agenesis, determined before birth.
- **Carney complex:** the most biologically plausible, because it involves thyroid nodules and neoplasms. Any use would be adjunctive (for example TSH suppression) rather than disease-modifying, and no data support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12830G | Eltroxin | Tablet containing 125 micrograms anhydrous levothyroxine sodium | Not stated in the licence record |

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI).

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists contraindication relations with hypertension, pituitary and growth hormone deficiency conditions (including hypopituitarism and Sheehan syndrome), hypogonadotropic hypogonadism (including Kallmann syndrome), osteoporosis, diabetes mellitus and diabetic ketoacidosis, coronary artery disease and myocardial infarction, and thymus gland disease. These need confirmation against the PI.
- **Drug Interactions:** 100 interactions were found. The main ones listed are mostly moderate.
  - Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide
  - Acid suppressants: omeprazole, rabeprazole, dexlansoprazole (moderate); cimetidine (minor)
  - Minerals and antacids: calcium phosphate, calcium acetate, magnesium oxide
  - Sympathomimetics: epinephrine, isometheptene, diethylpropion

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence, with no trials or publications on renal hypodysplasia/aplasia. The proposed mechanism is speculative, and a postnatal thyroid hormone is unlikely to correct a structural malformation that arises in utero.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that directly studies levothyroxine in renal hypodysplasia/aplasia
- Mechanism of action data
- Safety information from the TGA-approved Product Information, including warnings and contraindications
- If a lead is wanted, Carney complex (thyroid manifestations) is the more plausible candidate to examine first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

