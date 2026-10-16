---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 751
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Travoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension"
monitor_inn: "Travoprost"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome"]
---

# Travoprost
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

# Travoprost: From Open-Angle Glaucoma and Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a prostaglandin F2-alpha analogue eye drop, originally used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**,
but there are currently **no registered clinical trials** and **no publications** supporting this direction, so it is a model-derived prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, travoprost is a prostaglandin F2-alpha analogue (FP receptor agonist). Its efficacy in open-angle glaucoma and ocular hypertension is established, and the vasodilatory activity of this class might loosely relate to the microvascular ischaemia seen in calciphylaxis.

This link is speculative. Calciphylaxis occurs mainly in patients with end-stage renal disease. It involves vascular calcification, thrombosis and skin necrosis, and none of these are known to respond to FP receptor agonism. In addition, systemic exposure from ophthalmic dosing is minimal, so it is doubtful that enough drug would reach the affected vessels.

The very high TxGNN score reflects a pattern found by the model in the knowledge graph. It is not clinical corroboration.

Two other predictions were also generated, both at the same evidence level (L5) and with the same Hold recommendation:
- **Venous thoracic outlet syndrome** (score 99.99%): mainly a mechanical compression and thrombosis problem, managed with anticoagulation, thrombolysis and surgical decompression. A topical ophthalmic prostaglandin analogue has no established mechanistic role.
- **Arterial thoracic outlet syndrome** (score 99.99%): involves subclavian artery compression, aneurysm or embolisation, and is treated surgically. Any vasodilatory rationale is hypothetical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14549R | Travatan | Eye drops 40 micrograms per mL, 2.5 mL | Not available in the data compiled for this report |

Only the ophthalmic route is available in Australia. Any new indication in a systemic condition would likely need a different formulation or route, and route compatibility has not yet been assessed.

---

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication links, not label text): uveitis, iris disease, ciliary body disease, panuveitis, iritis, cystoid macular oedema, macular retinal oedema.
- **Drug Interactions**: The interaction query returned 49 potential interacting drugs, but none has a severity grading (all listed as "Unknown"). Examples include calcitriol, pantoprazole, sucralfate, morphine, metformin, omeprazole, prednisolone, simvastatin and acetylsalicylic acid. Of note, calcitriol and other drugs commonly used in patients with kidney disease appear in the list, which is relevant to the calciphylaxis population. These entries should be interpreted with caution until their clinical significance is clarified.

Warnings and contraindications from the label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational model. There are no clinical trials or publications, the mechanistic link to calciphylaxis is speculative, and systemic exposure from ophthalmic dosing is minimal. Label safety data are also missing.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a plausible biological link between FP receptor agonism and calcific vasculopathy
- Preclinical or mechanistic studies (for example, in vascular calcification models) to move beyond L5
- A literature and trial registry search (including ANZCTR) for any supporting studies
- Product Information warnings and contraindications from the TGA-approved PI, to complete safety screening
- An assessment of route and formulation compatibility, since only an ophthalmic product is registered in Australia
- Clarification of the severity of the drug interaction signals, particularly for drugs used in renal disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

