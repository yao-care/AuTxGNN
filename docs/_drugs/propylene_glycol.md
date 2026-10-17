---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Propylene Glycol: predicted new indication Bronchitis (evidence level L5). Approved use: Dry eye syndrome / xerophthalmia"
monitor_inn: "Propylene glycol"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "immature cataract", "mature cataract", "tetanic cataract"]
---

# Propylene Glycol
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

# Propylene Glycol: From Dry Eye Syndrome to Bronchitis

## One-Sentence Summary

Propylene glycol is an ophthalmic lubricant ingredient, originally used for dry eye syndrome (xerophthalmia).
The TxGNN model predicts it may be effective for **bronchitis**, but the data compiled for this report show **no clinical trials** and **3 publications** (none testing propylene glycol as a treatment for bronchitis), so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome / xerophthalmia (from the TxGNN knowledge graph; no approved indication text is recorded for the Australian entries) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propylene glycol is used as a humectant and lubricant in ophthalmic products, which is consistent with its use in dry eye. A mechanistic link to bronchitis is not supported.

The retrieved literature on bronchitis concerns propylene glycol as a constituent of e-cigarette liquids. Those papers describe it as a potential airway irritant and a possible contributor to asthma and lung disease, which points to possible harm rather than benefit. The remaining paper (a quercetin study in a mouse COPD model) does not involve propylene glycol as a therapeutic agent. The high TxGNN score is therefore not backed by clinical or mechanistic evidence.

Other predicted indications (for context, all Hold):
- **Diabetic retinopathy** (L4): indirect evidence only. The one trial compares anti-inflammatory drops and artificial tears for post-injection pain, and a retinopathy paper concerns propylene glycol mannate sulfate, a different compound.
- **Severe nonproliferative diabetic retinopathy, and cataract types (nuclear senile, cortical, senile, diabetic, immature, mature, tetanic)**: prediction only (L5), with no plausible mechanism identified. The only linked paper (diabetic cataract) is an ocular insert formulation study in which propylene glycol is an excipient.

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

For reference, one trial is linked to the related prediction of diabetic retinopathy:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07090044](https://clinicaltrials.gov/study/NCT07090044) | Phase 4 | Completed | 77 | Compared loteprednol, bromfenac and preservative-free artificial tears for pain after intravitreal injection. It does not test propylene glycol as a disease treatment. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews whether chronic e-cigarette use may cause lung disease, including chronic bronchitis and COPD. Suggests potential harm, not benefit. |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette constituents (including propylene glycol) are airway irritants with possible links to asthma. |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a mouse COPD model. Propylene glycol is not the therapeutic agent. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 425J | Not recorded | Not recorded | Not recorded |
| 14768G | Systane Balance | Eye drops 60 micrograms per mL, 10 mL | Not recorded |

Both entries are valid single-ingredient listings. The only recorded route of the product with a stated dosage form is ophthalmic.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interactions were found in the data compiled for this report. Note that the retrieved literature raises the possibility of airway irritation from inhaled propylene glycol (e-cigarette aerosols), which is relevant to any respiratory use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is supported only by a model score (L5). The available literature suggests possible respiratory harm rather than benefit, and the existing Australian products are ophthalmic, so there is no plausible route or mechanism for bronchitis.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible pharmacological rationale for respiratory disease
- Evidence from controlled studies, with propylene glycol as the active agent, in bronchitis
- Safety review of inhaled exposure, given the airway irritation concerns
- Product Information warnings and contraindications for the Australian entries
- Route and formulation compatibility assessment (current products are ophthalmic)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

