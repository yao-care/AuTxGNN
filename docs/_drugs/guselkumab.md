---
layout: default
title: Guselkumab
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Guselkumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
description: "Guselkumab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Guselkumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Guselkumab: Drug-induced osteoporosis
{: .text-alpha }

## One-Sentence Summary

Guselkumab (Tremfya) is an IL-23 inhibitor whose established use is in immune-mediated inflammatory disease, mainly plaque psoriasis.
The TxGNN model (deep learning) predicts it may be effective for **drug-induced osteoporosis**, but this is a model prediction only and may reflect similarities the model learned between related diseases, not biological evidence, with **0 clinical trials** and **0 publications** currently supporting this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally recorded in the data compiled for this report. From its known pharmacology, guselkumab selectively blocks the p19 subunit of IL-23, which drives the IL-23/Th17 inflammatory axis in psoriasis and other immune-mediated diseases.

IL-23/IL-17 signalling has been implicated in inflammatory bone loss, which is the only plausible link to osteoporosis. That link is indirect and not specific to drug-induced osteoporosis. No direct mechanistic connection has been established, and the prediction should be treated as hypothesis-level only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form |
|---------|------|------|
| 11614G | Tremfya | Injection 100 mg in 1 mL single use pre-filled syringe |

The approved indication text was not available in the data compiled.

## Safety Considerations

- **Drug Interactions** (100 interactions identified; the main ones from the 20 reviewed are listed):
  - **Major:** adalimumab (combination of two immunomodulating biologics).
  - **Moderate:** warfarin, apixaban, rivaroxaban, dicoumarol, simvastatin, tacrolimus, theophylline and related agents, roflumilast, nifedipine, lidocaine, fentanyl, hydrocodone, and tetanus toxoid vaccine.
  - **Minor:** zinc salts (sulfate, acetate, gluconate, chloride).

No key warnings or contraindications were available in the data compiled. Please refer to the TGA-approved Product Information (PI) for full safety information, including infection risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis rests on a model score alone. There are no registered trials or publications, and the mechanistic link is indirect and speculative.

Two other TxGNN predictions for guselkumab have substantial supporting evidence and deserve separate evaluation:
- **Psoriasis** has many completed Phase 3 trials and RCTs (for example VOYAGE 1/2), but it is the drug's established indication, so it is not true repurposing.
- **Ulcerative colitis** has Phase 2b/3 QUASAR evidence (NCT04033445, PMID 39706209). It would be a candidate for "Proceed with Guardrails", subject to confirming its regulatory status in Australia.

**To proceed with drug-induced osteoporosis, the following is needed:**
- Preclinical or mechanistic studies linking IL-23 blockade to bone loss in a drug-induced setting
- Registered clinical studies or observational data in the target population
- Extraction of PI warnings and contraindications, and confirmation of the approved indications in the Australian licence data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

