---
layout: default
title: Ranibizumab
parent: Model Prediction Only (L5)
nav_order: 624
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Ranibizumab"
predicted_indications: ["immature cataract", "craniostenosis cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "hemorrhagic disease of newborn"]
description: "Ranibizumab: predicted new indication Immature cataract (evidence level L5). Approved use: Not recorded in the local data"
---

# Ranibizumab
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

## Ranibizumab: Immature cataract
{: .text-alpha }

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment originally used for retinal diseases such as diabetic retinopathy, diabetic macular oedema and macular degeneration.
The TxGNN model predicts it may be effective for **immature cataract**,
with **no registered clinical trials** but **18 publications** (including post hoc analyses of Phase 3 RCTs and a recent randomised trial of a ranibizumab port delivery system) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (as graded in the data compiled for this report; see note below) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* No clinical trials were supplied for this indication. The L1 grade rests on literature titles, namely post hoc analyses of the RIDE/RISE Phase 3 RCTs and the PAVILION randomised trial. Abstracts and full texts were not reviewed, so the grade should be treated as provisional.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ranibizumab is a VEGF-A inhibitor. VEGF drives retinal vascular permeability and neovascularisation in diabetic retinopathy. By neutralising VEGF-A, ranibizumab reduces vascular leakage and can regress retinopathy severity.

Diabetic retinopathy and diabetic macular oedema are already original indications for ranibizumab.

The literature supports this link. Post hoc analyses of the RIDE and RISE trials describe regression of diabetic retinopathy severity with ranibizumab. The PAVILION randomised trial tested a ranibizumab port delivery system in nonproliferative diabetic retinopathy without macular oedema.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication in the data compiled for this report.

The RIDE/RISE trials (NCT00473382 / NCT00473330) are referenced in the literature below, but were not supplied as registered trial records.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmol | PAVILION: ranibizumab port delivery system vs monitoring in nonproliferative diabetic retinopathy without macular oedema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT (post hoc meta-analysis) | Ophthalmol Retina | Baseline retinopathy severity and time to macular oedema resolution with ranibizumab in Phase 3 trials |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT (post hoc) | Clin Ophthalmol | Predictors of early retinopathy regression with ranibizumab in RIDE/RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT extension analysis | BMJ Open Ophthalmol | Retinopathy severity scale changes with less frequent ranibizumab after induction (RIDE/RISE extension) |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review / meta-analysis | Eur J Pharmacol | Sustained ranibizumab port delivery for disease modification and durability in diabetic retinopathy and macular oedema |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic review | Health Technol Assess | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy: economic analysis |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review / meta-analysis | Health Technol Assess | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy: clinical effectiveness |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Overview of ranibizumab for diabetic retinopathy, including macular oedema |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Cohort | Front Endocrinol | Nomogram predicting response to anti-VEGF plus laser in severe nonproliferative diabetic retinopathy |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT secondary analysis | Retina | Five-year changes in retinopathy severity with ranibizumab in DRCR.net Protocol I |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10138N | Lucentis | Solution for intravitreal injection 1.65 mg in 0.165 mL pre-filled syringe | Not available in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): eye infectious disease and conjunctivitis.
- **Drug Interactions**: No interactions were found in the data queried.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Severe nonproliferative diabetic retinopathy lies within the established retinal disease spectrum for ranibizumab. The literature includes Phase 3 post hoc analyses and a randomised trial in nonproliferative disease. However, no registered trials were supplied and the evidence grade rests on titles rather than reviewed full texts.

**To proceed, the following is needed:**
- Review of abstracts and full texts to confirm the evidence grade, and registered trial records (RIDE/RISE, PAVILION)
- Approved indication wording from the ARTG entry and the TGA Product Information, including warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Confirmation of the route and dosing regimen for this stage of disease (the intravitreal syringe is the only registered form; the port delivery system is not in the ARTG data supplied)
- Assessment of whether other predicted indications warrant follow-up. The cataract-related predictions and hemorrhagic disease of newborn have no supporting mechanism or evidence and should remain on Hold. The withdrawn trial in hereditary haemorrhagic telangiectasia (NCT01406639) could be considered separately as its own indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

