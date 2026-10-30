---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Latanoprost"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
description: "Latanoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Not recorded in the local data"
---

# Latanoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Latanoprost: Visceral calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Latanoprost is a prostaglandin F2-alpha analogue eye drop, originally used for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**,
but currently there are **0 clinical trials** and **0 publications** in the data compiled for this report, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, latanoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure (IOP) by increasing uveoscleral outflow.


There are caveats. Developmental defects in the outflow pathway in congenital forms may reduce the response to treatment. Paediatric use would also need separate safety and efficacy review. No trials or publications support the link at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14453Q | Xalatan | Eye drops 50 micrograms per mL, 2.5 mL | Not recorded in the data compiled |

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (not taken from label text): uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, conjunctivitis and acute contagious conjunctivitis.
- **Drug Interactions**: 100 potential interactions were identified in the DDI database, but none has a severity level assigned. Examples include calcitriol, glimepiride, doxycycline, clotrimazole, lansoprazole, cimetidine, atropine, pantoprazole, mesalazine and acarbose. These should be interpreted with caution given latanoprost's minimal systemic exposure as a topical ophthalmic agent.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Other Predicted Indications (Context)

All of the top 10 predictions have Evidence Level L5, with no supporting trials or literature.

| Rank | Predicted Indication | TxGNN Score | Assessment |
|---|---|---|---|
| 2 | Visceral calciphylaxis | 0.9983 | No clear mechanistic link |
| 3 | Hypotrichosis simplex of the scalp | 0.9981 | Biologically plausible (prostaglandin analogues stimulate hair growth; a related analogue is approved for eyelash hypotrichosis), but the genetic follicular defect may not respond. May merit a focused literature search |
| 4–6 | Venous, arterial and neurogenic thoracic outlet syndrome | 99.72–0.9978 | No credible mechanistic link (mechanical compression disorders) |
| 7 | Congenital hypotrichosis milia | 0.9971 | Similar rationale to rank 3, but a rare congenital disorder |
| 8 | Angiodysplasia of stomach | 0.9970 | No credible link; vasodilation could be undesirable in a bleeding lesion |
| 9 | Blue toe syndrome | 0.9969 | Speculative only; topical dosing gives no relevant systemic exposure |
| 10 | Lymphangiectasis | 0.9967 | Too indirect to support a hypothesis |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically reasonable but is supported by model output alone, with no registered trials or publications. It is also essentially an extension of existing glaucoma use. The package insert safety data for Australia could not be retrieved, which blocks safety screening.

**To proceed, the following is needed:**
- Retrieve and review the Australian Product Information (warnings, contraindications and approved indication text for Xalatan)
- Mechanism of action data (for example, from DrugBank)
- A targeted literature and trial registry search (including ANZCTR) for latanoprost in primary congenital or hereditary glaucoma
- Paediatric safety and efficacy review, as hereditary glaucoma commonly presents in infancy
- A focused literature search on prostaglandin analogues for hypotrichosis, as the most biologically plausible non-glaucoma candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

