---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 749
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab deruxtecan: From Its Original Oncology Use to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-directed antibody-drug conjugate marketed in Australia as Enhertu, and the data compiled for this report do not list an approved indication text for it.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction (Evidence Level L5) with no identified mechanistic rationale, so it should not be pursued on current evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Trastuzumab deruxtecan is generally characterised as a HER2-directed antibody-drug conjugate carrying a topoisomerase I inhibitor payload, designed to kill HER2-expressing tumour cells.

On this basis, the prediction is **not mechanistically reasonable**. The drug has no known role in bone metabolism, and osteoporosis is not a HER2-driven or oncologic condition. The high TxGNN score (99.31%) reflects graph-based similarity only and is not backed by any trial or publication.

The other top-ranked predictions show the same pattern: diabetic retinopathy (severe nonproliferative and general), bronchitis, diabetic cataract and several tumour or lesion labels. None has trial or literature support, and none has a plausible mechanistic link. For bronchitis, interstitial lung disease/pneumonitis is a known key risk of this drug, which makes a respiratory indication particularly unattractive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13713R | Enhertu | Powder for I.V. infusion 100 mg | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (targeted therapy) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Haematological parameters (FBC), liver and renal function, and respiratory status are reasonable considerations given the drug's known risks |
| Handling Protection | Handle as a cytotoxic agent per local cytotoxic drug handling requirements; confirm against the PI |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for key warnings and contraindications, as these were not available in the data compiled for this report.

**Drug Interactions:** 42 interactions were identified in total. Examples of those rated **Major** include:
- Deferiprone
- Samarium (153Sm) lexidronam
- Adalimumab
- Baricitinib
- Certolizumab pegol
- Cladribine
- Leflunomide
- Natalizumab

Examples rated **Moderate** include palifermin, strontium chloride Sr-89, roflumilast, chloramphenicol, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, dimethyl fumarate and niraparib. Many of these are immunosuppressive or myelosuppressive agents, so additive effects are a concern.

Published case reports, which are not specific to the predicted indication, describe reversible Fanconi syndrome, interstitial lung disease, and a possible association with dermatomyositis during treatment with this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score, with no clinical trials, no literature and no plausible mechanistic link between a cytotoxic HER2-directed ADC and bone metabolism. Systemic cytotoxic exposure would also bring substantial safety risks in a non-oncologic condition.

**To proceed, the following is needed:**
- A mechanistic rationale linking the drug or its payload to bone biology
- Preclinical evidence in an osteoporosis model
- Mechanism of action data (currently unavailable)
- Approved indication text and safety information from the TGA Product Information
- A risk-benefit assessment of the drug's known toxicities (interstitial lung disease, ocular and haematological effects) against any proposed non-oncologic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

