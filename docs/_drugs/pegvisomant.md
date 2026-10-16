---
layout: default
title: Pegvisomant
parent: Model Prediction Only (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pegvisomant: predicted new indication Borderline ovarian serous tumour (evidence level L5). Approved use: Acromegaly, hyperpituitarism"
monitor_inn: "Pegvisomant"
predicted_indications: ["borderline ovarian serous tumor", "rete ovarii cystadenoma", "ovarian papillary cystadenoma", "pyelonephritis", "malignant ovarian Brenner tumor", "aleukemic mast cell leukemia", "ovarian mucinous cystadenofibroma", "ovarian benign neoplasm", "mucinous ovarian cystadenoma", "ovarian surface papilloma"]
---

# Pegvisomant
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

# Pegvisomant: From Acromegaly to Borderline Ovarian Serous Tumour

## One-Sentence Summary

Pegvisomant is a growth hormone receptor antagonist, originally used to treat acromegaly and hyperpituitarism.
The TxGNN model predicts it may be effective for **borderline ovarian serous tumour**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly, hyperpituitarism (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Borderline ovarian serous tumour |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Pegvisomant is known as a growth hormone (GH) receptor antagonist that lowers IGF-1, and its efficacy in acromegaly is established. Mechanistically, it may be relevant to other conditions in which the GH/IGF-1 axis drives tissue growth.

The only conceivable link to borderline ovarian serous tumour is a speculative one: GH/IGF-1 signalling has been discussed in the context of ovarian epithelial proliferation. No trials, publications or preclinical data were supplied to support this. The high score (98.63%, model rank 13,502) is a computational prediction and does not constitute clinical evidence.

The other nine top-ranked predictions are similar in character and also have no supporting evidence:

- Most are benign or rare ovarian neoplasms: rete ovarii cystadenoma, ovarian papillary cystadenoma, malignant ovarian Brenner tumour, ovarian mucinous cystadenofibroma, ovarian benign neoplasm, mucinous ovarian cystadenoma and ovarian surface papilloma. The rationale for these is the same speculative GH/IGF-1 link.
- Pyelonephritis (a bacterial infection) and aleukaemic mast cell leukaemia (typically KIT-driven) show no credible mechanistic connection to GH receptor antagonism. These are likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11166Q | Somavert | Injection set containing powder for injection 20 mg, 1 and diluent, 1 | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 74 interactions were identified, and the main ones listed are all rated Moderate. They are mostly with glucose-lowering agents, including:
  - Insulin (human, aspart)
  - Metformin
  - Sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide)
  - Pioglitazone and acarbose
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - DPP-4 inhibitor alogliptin
  - GLP-1 agonists (albiglutide, dulaglutide, exenatide)

  Other listed interactions include morphine and pegvaliase. Blood glucose monitoring is a reasonable consideration when pegvisomant is combined with antidiabetic agents.

Warnings and contraindications from the label were not available. Please refer to the TGA-approved Product Information (PI) for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (evidence level L5), with no clinical trials, no publications and no established mechanism linking GH receptor antagonism to borderline ovarian serous tumour. A systemic GH antagonist has no established therapeutic rationale in these largely benign ovarian lesions.

**To proceed, the following is needed:**
- Mechanism of action data, to allow proper mechanistic analysis
- Preclinical evidence (for example, GH/IGF-1 receptor involvement in borderline serous tumours)
- A literature and trial registry search (including ANZCTR) specific to this indication
- Label warnings and contraindications from the TGA PI for safety screening
- Confirmation of the approved indication text for ARTG 11166Q
- Assessment of route compatibility (pegvisomant is available only as an injection)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

