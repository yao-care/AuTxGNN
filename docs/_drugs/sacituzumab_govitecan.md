---
layout: default
title: Sacituzumab Govitecan
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Sacituzumab Govitecan: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the data compiled for this report (the registered in…"
monitor_inn: "Sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Sacituzumab Govitecan: From Oncology Use to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Sacituzumab govitecan is a Trop-2-directed antibody-drug conjugate carrying the topoisomerase I inhibitor SN-38, and it is marketed in Australia as Trodelvy.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the registered indication text is blank) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, sacituzumab govitecan is an antibody-drug conjugate that delivers SN-38, a cytotoxic topoisomerase I inhibitor, to Trop-2-expressing cells. It is an oncology product.

No mechanistic link to drug-induced osteoporosis is supported. A cytotoxic payload would not be expected to benefit bone loss. Myelosuppression and other toxicities argue against use in a non-oncology bone indication. The high TxGNN score reflects a model prediction without any clinical or literature backing.

The other top-ranked predictions (severe nonproliferative diabetic retinopathy 0.9969, diabetic retinopathy 0.9960 and diabetic cataract 0.9912) are also unsupported. Many are overlapping or parent/child disease terms, so they are likely not independent signals. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12944G | Trodelvy | Powder for injection 180 mg | Not stated in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (SN-38) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically includes FBC with differential, plus liver and renal function |
| Handling Protection | Follow local cytotoxic drug handling requirements |

## Safety Considerations

- **Drug Interactions**: 40 interactions were recorded in total, and 20 are listed in the compiled data.
  - **Major**: deferiprone, fostamatinib, adalimumab, apalutamide, certolizumab pegol, cladribine, dacomitinib, irinotecan, leflunomide, natalizumab, nilotinib, ozanimod.
  - **Moderate**: alefacept, alemtuzumab, anakinra, canakinumab, dimethyl fumarate, lorlatinib, ocrelizumab, omacetaxine mepesuccinate.
  - The Major interactions include several immunosuppressive, myelosuppressive and other topoisomerase I inhibitor agents (for example, irinotecan).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no publications and no plausible mechanistic link. The drug's cytotoxic profile also presents a poor risk-benefit balance for a non-oncology bone indication.

**To proceed, the following is needed:**
- The TGA-approved Product Information (registered indication, warnings and contraindications)
- Mechanism of action data
- Preclinical or mechanistic evidence linking Trop-2 or SN-38 activity to bone loss
- A risk-benefit assessment for any non-oncology use of a systemic cytotoxic agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

