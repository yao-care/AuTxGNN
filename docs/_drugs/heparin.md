---
layout: default
title: Heparin
parent: Model Prediction Only (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Heparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
---

# Heparin
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

# Heparin: From Pulmonary Embolism and Disseminated Intravascular Coagulation to Protein C Deficiency Thrombophilia

## One-Sentence Summary

Heparin is an injectable anticoagulant originally used for pulmonary embolism, disseminated intravascular coagulation (DIC) and purpura fulminans.
The TxGNN model predicts it may be useful for **thrombophilia due to protein C deficiency (autosomal recessive)**, with a very high prediction score (99.29%).
However, the data compiled for this report contain **no clinical trials and no publications** for this indication, so the prediction rests on model output and mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (knowledge-graph indications; the ARTG entry carries no indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Heparin is a well-established anticoagulant that works by potentiating antithrombin, which inactivates thrombin and factor Xa. This mechanism is the basis of its use in venous thromboembolism and DIC.

Severe (autosomal recessive) protein C deficiency removes a key natural anticoagulant pathway and can cause purpura fulminans and DIC-like thrombosis. These are conditions for which heparin is already an original indication. Anticoagulation is therefore mechanistically plausible in this setting.

It is important to be clear about the limits of this reasoning. The high TxGNN score is a network-based prediction only. No trials or literature were found for this specific indication in the data compiled for this report, so the link remains theoretical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1466E | DBL Heparin Sodium | Injection 5,000 units (as sodium) in 0.2 mL | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from a model knowledge graph, not from approved label text): liver failure, thrombocytopenia (including heparin-induced thrombocytopenia), haemophilia and other blood coagulation diseases, antithrombin III deficiency, intracranial and intracerebral haemorrhage, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, infective endocarditis, placental abruption, osteoporosis, and several retinal conditions (diabetic and hypertensive retinopathy).
- **Drug Interactions**: The interaction query returned 100 records, of which 20 are shown here. Most are rated Moderate, including acetylsalicylic acid and a group of glucose-lowering drugs (glimepiride, glipizide, glyburide, tolbutamide, chlorpropamide, tolazamide, acetohexamide, repaglinide, nateglinide). Fenfluramine, dexfenfluramine and sibutramine are also rated Moderate. Interactions with levocarnitine, mannitol, calcitriol, vitamin A, pantoprazole, mesalazine and doxycycline are of unknown severity.

Approved warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

---

## Other Predictions Reviewed

Nine further predicted indications were assessed. None has sufficient evidence to progress.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Primary release disorder of platelets | 99.06% | L5 | Bleeding disorder, so an anticoagulant is unlikely to help and may worsen bleeding. The 20 papers retrieved do not evaluate heparin for this disorder. |
| 3 | Pseudo-von Willebrand disease | 98.65% | L5 | Platelet-type bleeding disorder. There is no plausible therapeutic mechanism and heparin could worsen bleeding. |
| 4 | Atypical haemolytic-uraemic syndrome with thrombomodulin anomaly | 96.74% | L5 | Anticoagulation is theoretically plausible, but complement inhibition is the established therapy. No clinical evidence. |
| 5 | Painful neuropathy | 96.13% | L5 | The only trial (NCT00445328) compares dalteparin with unfractionated heparin for VTE prevention and is not relevant to this indication. |
| 6 | Retinal telangiectasia | 94.88% | L5 | No mechanistic rationale and no evidence. |
| 7 | Retinal microaneurysm | 94.52% | L5 | No mechanistic link, and a possible increased risk of retinal haemorrhage. |
| 8 | Arteriosclerotic retinopathy | 94.52% | L5 | Only an indirect vascular link. No evidence. |
| 9 | Vertebral artery occlusion | 94.22% | L4 | The most plausible of the group (see below). |
| 10 | Breast fibrocystic disease | 93.20% | L5 | Three papers did not evaluate heparin treatment. Prediction unsupported. |

**Vertebral artery occlusion** is the only alternative with indirect support. Anticoagulation is a recognised option in cervical artery dissection, and the CADISS randomised trial (PMID [30801621](https://pubmed.ncbi.nlm.nih.gov/30801621/), JAMA Neurology, 2019) compared antiplatelet and anticoagulant therapy in general, without isolating heparin. The one registered trial, [NCT01980316](https://clinicaltrials.gov/study/NCT01980316) (Phase 4, completed, n=114), tested argatroban rather than heparin for restenosis after vertebral artery stenting. This evidence is indirect and supports a research question, not a treatment recommendation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (protein C deficiency thrombophilia) has a plausible mechanism but no trials or literature in the data compiled for this report. It is therefore graded L5. Several other predictions are mechanistically doubtful or potentially harmful, particularly the bleeding-type platelet disorders.

**To proceed, the following is needed:**
- Approved warnings and contraindications from the TGA Product Information, which were not available and are needed for safety screening
- Mechanism of action data (for example from DrugBank) to support mechanistic analysis
- A targeted literature search on heparin in severe protein C deficiency, purpura fulminans and neonatal presentations
- Specialist haematology input on bleeding risk and on whether protein C replacement is the established standard of care
- Assessment of vertebral artery occlusion as a separate research question, with a focus on bleeding risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

