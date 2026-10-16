---
layout: default
title: Fondaparinux
parent: Model Prediction Only (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fondaparinux: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Pulmonary embolism"
monitor_inn: "Fondaparinux"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Ledderhose disease", "vertebral artery occlusion", "arteriosclerotic retinopathy", "retinal microaneurysm", "infantile digital fibromatosis", "palmar fibromatosis", "retinal telangiectasia"]
---

# Fondaparinux
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

# Fondaparinux: From Pulmonary Embolism to Primary Release Disorder of Platelets

## One-Sentence Summary

Fondaparinux is an anticoagulant originally used for pulmonary embolism (venous thromboembolism).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this prediction rests on **0 clinical trials** and **1 unrelated publication** (a palliative care case report), so the evidence is model-based only.
The mechanism points the wrong way: this is a bleeding disorder, and an anticoagulant would be expected to worsen it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism (per the knowledge graph; the Australian licence record contains no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From established pharmacology, fondaparinux is an indirect factor Xa inhibitor that acts through antithrombin III. It is used to prevent and treat venous thromboembolism, including pulmonary embolism.

The predicted condition is a platelet function disorder in which platelets fail to release their granule contents, which causes a bleeding tendency. Fondaparinux has no direct action on platelet granule release or platelet function. Because it reduces clotting, it would be expected to add to the bleeding risk rather than treat the condition.

On this evidence the prediction is **not mechanistically plausible**. The high score likely reflects a graph-based association (both conditions involve haemostasis) and not a therapeutic relationship. The same applies to the other top-ranked predictions, such as pseudo-von Willebrand disease and Glanzmann thrombasthenia, which are also bleeding disorders.

For context, the one predicted indication with a plausible rationale is **vertebral artery occlusion** (rank 5, score 87.44%). It is a thrombotic cerebrovascular condition, so anticoagulation is mechanistically conceivable. It is rated L4 and flagged as a research question only, with no trials or literature identified. Use would also need to be weighed against haemorrhagic risk in the posterior circulation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case report | Journal of the Advanced Practitioner in Oncology | Palliative chemotherapy and palliative care in a young patient with metastatic adenocarcinoma. Not relevant to fondaparinux or platelet release disorders. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8775W | Arixtra | Injection containing fondaparinux sodium 2.5 mg in 0.5 mL single dose pre-filled syringe | Not recorded in the data compiled for this report |

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease relationship data, not from approved label text):
- Heparin-induced thrombocytopenia
- Thrombocytopenia, including immune thrombocytopenia
- Blood coagulation disease
- Kidney disease
- Anaemia, including macrocytic anaemia
- Endocarditis, including subacute bacterial endocarditis
- Diabetic retinopathy and diabetic cataract
- Pyoureter

Several of these (thrombocytopenia, coagulation disorders, retinal vascular disease) overlap directly with the predicted indications and reinforce the bleeding-risk concern.

**Drug Interactions:** The interaction screen returned 100 interactions in total. Examples of those rated **Major** include:
- Acetylsalicylic acid (aspirin)
- Ibuprofen
- Ketorolac
- Abciximab
- Acalabrutinib
- Anagrelide
- Antithrombin alfa and antithrombin III human
- Deferasirox
- Trastuzumab emtansine
- Ibritumomab tiuxetan and tositumomab

Most of these combinations raise bleeding risk. Moderate-level examples include fenfluramine, dexfenfluramine, sibutramine, sugammadex and radioiodine products.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, because label-level safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no relevant literature, and a mechanism that conflicts with the condition. Fondaparinux is an anticoagulant and primary release disorder of platelets is a bleeding disorder, so use would risk harm. The model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- A plausible mechanistic rationale showing how factor Xa inhibition could benefit platelet release disorders (none is currently apparent)
- Label-level warnings and contraindications from the TGA Product Information
- Mechanism of action data, and the approved indication text for the Australian licence
- If the team wishes to pursue the most plausible lead, a focused literature and trial search on **vertebral artery occlusion**, with a haemorrhagic risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

