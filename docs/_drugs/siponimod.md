---
layout: default
title: Siponimod
parent: Model Prediction Only (L5)
nav_order: 676
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Siponimod: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Siponimod"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "Prinzmetal angina", "rheumatoid arthritis", "atrophoderma vermiculata", "ulerythema ophryogenesis", "myelodysplastic syndrome"]
---

# Siponimod
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

## Siponimod: From an Unspecified Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Siponimod is an oral sphingosine-1-phosphate (S1P) receptor modulator marketed in Australia as Mayzent. The data compiled for this report do not include an approved indication text for it.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Siponimod is known to be a selective S1P1/S1P5 receptor modulator. S1P signalling has been implicated in pulmonary vascular remodelling and endothelial barrier function, which is the only basis for a mechanistic link to pulmonary hypertension.

This link is speculative. S1P1 modulation can also affect vascular tone and cause bradycardia and other cardiovascular effects, so the net effect in pulmonary hypertension could be neutral or harmful. The original indication was not captured in the data, so the relationship between the original and predicted indications cannot be assessed here.

### Other predictions in the top 10

None of the other predictions has clinical trial support.

- **Rheumatoid arthritis** (score 99.16%, evidence L4) has the most plausible rationale. S1P-mediated lymphocyte trafficking is a reasonable target in immune-mediated disease, and two reviews (PMID 33983615 and 29500302) discuss S1P modulation beyond multiple sclerosis. This is class-level support only, with no siponimod-specific data in rheumatoid arthritis.
- **Migraine disorder, migraine with brainstem aura, and migraine susceptibility** (99.66%, 99.56% and 99.49%) share a single weak signal. The one relevant paper (PMID 35382764) is a case report of migraine in a patient receiving interferon β1a and siponimod for multiple sclerosis, and it does not show therapeutic benefit. The other retrieved items are general neurology updates.
- **Kyphoscoliotic heart disease, atrophoderma vermiculata, ulerythema ophryogenesis, Prinzmetal angina and myelodysplastic syndrome** have no identifiable supporting mechanism or evidence. Siponimod's lymphopenia and cardiac conduction effects are potential concerns in myelodysplastic syndrome and Prinzmetal angina respectively.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

For context, the nearest literature found for other predicted indications is below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33983615](https://pubmed.ncbi.nlm.nih.gov/33983615/) | 2021 | Review | Drugs | S1P signalling in immune-mediated diseases beyond multiple sclerosis (rheumatoid arthritis prediction) |
| [29500302](https://pubmed.ncbi.nlm.nih.gov/29500302/) | 2019 | Review | Cold Spring Harb Perspect Med | Overview of oral multiple sclerosis therapies, including S1P modulators (rheumatoid arthritis prediction) |
| [35382764](https://pubmed.ncbi.nlm.nih.gov/35382764/) | 2022 | Case report/Review | BMC Anesthesiology | Migraine remission in an MS patient starting interferon β1a; siponimod is discussed as an immunomodulator, with no efficacy shown in migraine |
| [30629375](https://pubmed.ncbi.nlm.nih.gov/30629375/) | 2019 | Review | Rev Med Suisse | Neurology update noting siponimod reduces disability progression in secondary progressive MS; not specific to migraine |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12158X | Mayzent | Tablet 2 mg (as hemifumarate) | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. The first 20 returned include the following.
  - **Major**: famotidine, ranitidine, cimetidine, hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, aprepitant, clarithromycin, dolasetron, palonosetron, oxandrolone, levofloxacin.
  - **Moderate**: loperamide, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes), sodium sulfate, naltrexone.
- **Mechanism-related concerns** (from the prediction rationale, not label text): S1P receptor modulators carry cardiac conduction and bradycardia warnings, and lymphopenia is expected.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction rests only on a model score, with no clinical trials or literature. Siponimod's cardiovascular effects (bradycardia, conduction effects) also raise a plausible safety concern for this population. Rheumatoid arthritis is the only prediction with indirect class-level support, and it would be better framed as a research question than a repurposing candidate.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm the approved indication, warnings and contraindications
- Mechanism of action data
- Preclinical or mechanistic evidence for S1P1/S1P5 modulation in pulmonary vascular disease
- A cardiovascular safety assessment for the target population
- A targeted literature review of S1P modulators in pulmonary hypertension and rheumatoid arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

