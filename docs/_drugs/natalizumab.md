---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Natalizumab"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Natalizumab: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Natalizumab is an alpha-4 integrin–blocking monoclonal antibody originally used for multiple sclerosis and Crohn's disease (inflammatory bowel disease).
The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The score is a computational prediction only, so the recommendation is to **hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, natalizumab blocks alpha-4 integrin, which inhibits leukocyte adhesion and migration into inflamed tissue. This is the basis of its use in multiple sclerosis and Crohn's disease.

Bronchitis involves airway inflammation, so there is a theoretical link through reduced leukocyte trafficking. However, no trials or publications support this use. The high TxGNN score reflects a model-based association, not clinical proof.

There is also a counter-concern. Natalizumab causes immunosuppression, and respiratory infections are a recognised concern, so it could plausibly worsen rather than help infective bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for bronchitis.

For context, the other top-ranked predictions were also reviewed. The literature for them mostly describes natalizumab causing skin conditions (such as psoriasis, pustular psoriasis and cutaneous drug reactions) rather than treating them. One observational report (PMID 33589543, 2021) described improvement of comorbid psoriasis in 18 patients with MS on natalizumab, but this is a small observational series, and conflicting case reports exist.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13820J | Tysabri | Injection 150 mg in 1 mL single dose pre-filled syringe | Not available in the compiled data |

---

## Safety Considerations

- **Contraindication (knowledge graph, not label text)**: Progressive multifocal leukoencephalopathy (PML).
- **Drug Interactions**: 100 interactions were identified. The main Major-level interactions include:
  - Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Mercaptopurine, levamisole and trimetrexate
  - Radiopharmaceuticals and related agents: iobenguane (I-131), ibritumomab tiuxetan and tositumomab
- Moderate: naltrexone. Minor: zinc salts.
- The published literature highlights PML (a rare, often fatal JC virus brain infection) as a key risk of natalizumab, along with hypersensitivity reactions and cutaneous adverse events.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on a model score, with no trials, no literature, and a plausible safety concern (infection risk under immunosuppression). The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic case for airway inflammation
- Preclinical or early clinical evidence in bronchitis or related airway disease
- Review of the PI warnings and contraindications, with a risk assessment of PML and respiratory infection
- An assessment of whether an alternative indication is better supported (for example, the psoriasis signal is mixed and carries a paradoxical-reaction risk, so it is also not recommended at this stage)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

