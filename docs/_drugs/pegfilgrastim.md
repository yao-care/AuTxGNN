---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pegfilgrastim: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Pegfilgrastim"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "primary release disorder of platelets", "diabetic cataract", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "drug-induced osteoporosis", "senile cataract", "cortical cataract", "nuclear senile cataract"]
---

# Pegfilgrastim
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

## Pegfilgrastim: From Neutropenia Prevention to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegfilgrastim is a long-acting form of granulocyte colony-stimulating factor (G-CSF), a protein that stimulates neutrophil production. The TxGNN model predicts it may be relevant for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pegfilgrastim is a G-CSF analogue that stimulates neutrophil production. Its established use is in supporting neutrophil recovery, but the approved indication text was not included in the data compiled for this report.

The link to diabetic retinopathy is speculative. One hypothesis is that G-CSF mobilises haematopoietic or endothelial progenitor cells, which might influence retinal microvascular repair. No data support this. Neutrophil-mediated inflammation could also worsen retinal damage, so the direction of any effect is uncertain. The high score (0.9989) is a model output and should not be read as evidence of efficacy.

Other predicted indications were also reviewed, and none has supporting trials or literature:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Diabetic retinopathy | 99.73% | L5 | Overlaps with the lead prediction; no supporting evidence |
| Primary release disorder of platelets | 98.37% | L5 | No established role in platelet granule function |
| Diabetic cataract | 98.25% | L5 | Lens polyol and oxidative pathways are unrelated to G-CSF signalling |
| Pseudo-von Willebrand disease | 98.03% | L5 | Platelet GPIb defect is not addressed by G-CSF receptor agonism |
| Glanzmann thrombasthenia | 97.69% | L5 | Integrin αIIbβ3 defect; no known pegfilgrastim effect |
| Drug-induced osteoporosis | 96.75% | L5 | Indirect bone-marrow link conceivable; direction of effect uncertain |
| Senile, cortical and nuclear senile cataract | 96.31–96.37% | L5 | No mechanistic rationale; the identical scores for two forms suggest an ontology-driven prediction |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 6363X | Ziextenzo | Injection 6 mg in 0.6 mL single use pre-filled syringe | Not stated in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

**Drug Interactions:** The interaction screen returned 100 entries. The 20 reviewed here were all rated **Moderate**. They include:
- Cytotoxic and antineoplastic agents: paclitaxel, mercaptopurine, azacitidine, arsenic trioxide, altretamine, trimetrexate and asparaginase (*E. coli*)
- Targeted and biologic agents: abemaciclib, acalabrutinib, avapritinib, alemtuzumab, aldesleukin and belantamab mafodotin
- Radiopharmaceuticals and radioimmunotherapy: iobenguane (I-131), tositumomab (with and without I-131), ibritumomab tiuxetan and fludeoxyglucose (18F)
- Others: levamisole and pegvaliase

The remaining 80 interactions were not itemised in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no registered trials, no publications and no supported mechanism. Pegfilgrastim has no demonstrated benefit in diabetic retinopathy, and inflammatory effects could plausibly be harmful in the retina.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale for retinal disease
- A systematic literature search, including preclinical studies of G-CSF in diabetic retinopathy models
- The TGA Product Information, including approved indications, warnings and contraindications
- Review of the full interaction list and of ocular safety signals
- Preclinical evidence of benefit before any clinical trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

