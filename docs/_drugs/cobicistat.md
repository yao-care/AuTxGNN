---
layout: default
title: Cobicistat
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cobicistat: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Cobicistat is a pharmacokinetic booster (a CYP3A inhibitor) used in HIV-1 antiretroviral combinations, and was originally used for HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction, and the top-ranked indication is a veterinary condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (from the knowledge graph; no approved indication text was available for the ARTG entries) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cobicistat is a CYP3A inhibitor that boosts the blood levels of co-administered HIV antiretrovirals such as darunavir, atazanavir and elvitegravir. It has no antiviral activity of its own.

The high score most likely reflects how closely feline immunodeficiency virus (a lentivirus related to HIV) sits to the original HIV/AIDS indications in the knowledge graph. Any benefit would depend on a partner antiretroviral that is active against the feline virus, and this has not been established. This is therefore a network-proximity signal rather than evidence of efficacy. Veterinary use is also outside the scope of human drug repurposing.

The other two predictions are not stronger:
- **Simian immunodeficiency virus infection** (score 99.92%): this is an animal model of HIV, not a human clinical indication, and it offers no repurposing value beyond the existing HIV use.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.91%): no mechanistic link was identified, and the score may be a network artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10903W | Prezcobix | Tablet: darunavir 800 mg with cobicistat 150 mg | Not available |
| ARTG 10692R | Evotaz | Tablet: atazanavir 300 mg with cobicistat 150 mg | Not available |
| ARTG 11114Y | Genvoya | Tablet: tenofovir alafenamide 10 mg, emtricitabine 200 mg, elvitegravir 150 mg and cobicistat 150 mg | Not available |
| ARTG 11955F | Symtuza | Tablet: darunavir 800 mg, cobicistat 150 mg, emtricitabine 200 mg and tenofovir alafenamide 10 mg | Not available |

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 420 interacting drugs. Cobicistat is a CYP3A inhibitor, so interactions are expected to be extensive. Examples at **Major** level include:
  - Loperamide
  - Triamcinolone
  - Cisapride
  - Budesonide

  Examples at **Moderate** level include:
  - Hydrocortisone
  - Dexamethasone
  - Betamethasone
  - Aprepitant
  - Clarithromycin
  - Clotrimazole
  - Metoclopramide
  - Repaglinide
  - Fenfluramine

  One **Minor** interaction was listed: prucalopride.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest only on model scores, with no clinical trials or publications (Evidence Level L5). The top predictions are veterinary or animal-model conditions, and cobicistat has no intrinsic antiviral activity. It therefore offers no independent repurposing value beyond its existing role in HIV treatment.

**To proceed, the following is needed:**
- Evidence that a partner antiretroviral boosted by cobicistat is active against the predicted disease
- Detailed mechanism of action data
- Approved indication text and PI warnings and contraindications for the ARTG products
- A decision on whether veterinary or animal-model indications fall within the scope of this programme
- Any human-relevant candidate indication, with supporting trials or literature, before safety screening, given the large number of drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

