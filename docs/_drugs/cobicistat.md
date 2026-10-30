---
layout: default
title: Cobicistat
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
monitor_inn: "cobicistat"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Cobicistat: predicted new indication feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cobicistat: CYP3A inhibitor (pharmacokinetic booster) → feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Cobicistat is a CYP3A inhibitor used as a pharmacokinetic booster in HIV-1 antiretroviral combinations. The TxGNN model predicts it may be relevant to **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** were found to support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cobicistat has no antiviral activity of its own. It inhibits the CYP3A enzymes, which raises blood levels of co-administered antiretrovirals such as atazanavir, darunavir and elvitegravir. Detailed mechanism-of-action data were not available in the data compiled for this report.

The high score most likely reflects how closely the predicted disease sits to HIV-related conditions in the model's network. Feline immunodeficiency virus is a lentivirus related to HIV. Any benefit would depend on a partner antiretroviral that is active against that virus, and this has not been established. Veterinary use is also outside the scope of human drug repurposing.

The two other predictions in the compiled data, simian immunodeficiency virus infection (0.9992) and a rare neurodevelopmental disorder (0.9991), carry no supporting trials or literature either. The neurodevelopmental disorder has no identifiable mechanistic link to cobicistat.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10903W | Prezcobix | Tablet containing darunavir 800 mg with cobicistat 150 mg | Not recorded in the local data |
| ARTG 10692R | Evotaz | Tablet containing atazanavir 300 mg and cobicistat 150 mg | Not recorded in the local data |
| ARTG 11114Y | Genvoya | Tablet containing tenofovir alafenamide 10 mg, emtricitabine 200 mg, elvitegravir 150 mg and cobicistat 150 mg | Not recorded in the local data |
| ARTG 11955F | Symtuza | Tablet containing darunavir 800 mg, cobicistat 150 mg, emtricitabine 200 mg and tenofovir alafenamide 10 mg | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 420 interactions were recorded in the data compiled for this report. Examples of those rated Major include:
  - loperamide
  - triamcinolone
  - cisapride
  - budesonide

  Moderate examples include hydrocortisone, dexamethasone, aprepitant, clarithromycin, repaglinide and metoclopramide.

Warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. No trials or publications address this disease. Cobicistat only boosts other drugs, and the predicted condition is a veterinary one, not a human indication.

**To proceed, the following is needed:**
- Studies that directly examine this disease, with a defined partner antiretroviral
- Mechanism-of-action data
- Product Information safety data (warnings and contraindications)
- A review of the 420 recorded drug interactions for any proposed new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

