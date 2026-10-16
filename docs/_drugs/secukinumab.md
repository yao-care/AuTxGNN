---
layout: default
title: Secukinumab
parent: Model Prediction Only (L5)
nav_order: 661
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Secukinumab: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Secukinumab
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

# Secukinumab: From Established Immune-Mediated Inflammatory Disease to Primary Release Disorder of Platelets

## One-Sentence Summary

Secukinumab is an anti-IL-17A monoclonal antibody marketed in Australia as Cosentyx. The original indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a purely computational signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general knowledge, secukinumab is an anti-IL-17A monoclonal antibody. It is used in IL-17-driven immune-mediated conditions such as psoriasis, psoriatic arthritis, axial spondyloarthritis and hidradenitis suppurativa.

No plausible mechanistic link was identified for the predicted indication. Platelet release (secretion) disorders arise from intrinsic defects in platelet granules or signalling, not from IL-17A-driven inflammation. The high TxGNN score is a graph-based prediction with no supporting clinical or literature evidence, and it should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern:
- **Platelet and bleeding disorders** (pseudo-von Willebrand disease, Glanzmann thrombasthenia, fetal and neonatal alloimmune thrombocytopenia) have no mechanistic link to IL-17A inhibition.
- **Breast cancer subtypes** (HER2-positive, progesterone-receptor positive and negative, luminal A or B, normal breast-like) have only speculative links through tumour-promoting inflammation. Several share identical scores, suggesting a graph-neighbourhood artefact.
- **Drug-induced osteoporosis** has weak biological plausibility, since IL-17 can promote osteoclastogenesis via RANKL, but no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary release disorder of platelets.

## Literature Evidence

Currently no related literature available for primary release disorder of platelets.

The literature retrieved for the lower-ranked "breast tumor luminal A or B" prediction (SUNSHINE/SUNRISE phase 3 trials in hidradenitis suppurativa, psoriasis and arthritis reviews, and others) concerns other, already-established indications. It does not support any predicted new indication.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10425Q | Cosentyx | Injection 150 mg in 1 mL pre-filled pen | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Of the entries shown:
  - **Major**: adalimumab (combining biologic immunomodulators).
  - **Moderate**: simvastatin, apixaban, warfarin, rivaroxaban, dicoumarol, lidocaine, hydrocodone, fentanyl, theophylline, aminophylline, oxtriphylline, roflumilast, tacrolimus, nifedipine, and tetanus toxoid vaccine.
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride).
- **Class-related signal from the literature**: IL-17 blockers have been associated with paradoxical gastrointestinal effects, including exacerbation of Crohn's disease and ulcerative colitis. Infection risk is also a recognised consideration with biologic therapy.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials or publications, and the biology of platelet release disorders is unrelated to IL-17A inhibition.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking IL-17A to platelet secretion defects, supported by preclinical data
- Detailed mechanism of action data and the approved indication text from the TGA Product Information
- Safety information from the PI (warnings and contraindications)
- Any observational or preclinical evidence in the predicted indication before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

