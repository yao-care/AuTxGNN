---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Latanoprost: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension"
---

# Latanoprost
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2-alpha analogue eye drop, originally used for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently there are **0 clinical trials** and **0 publications** in the data compiled for this report, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (from the knowledge graph; no approved indication text is recorded in the ARTG data) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, latanoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure (IOP) by increasing uveoscleral outflow.

Primary hereditary glaucoma (for example, primary congenital glaucoma) also involves raised IOP, so the prediction is a close extension of the approved indications rather than a true repurposing. The mechanism could plausibly apply.

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
| 1 | Primary hereditary glaucoma | 99.88% | Plausible; close to the approved use |
| 2 | Visceral calciphylaxis | 99.83% | No clear mechanistic link |
| 3 | Hypotrichosis simplex of the scalp | 99.81% | Biologically plausible (prostaglandin analogues stimulate hair growth; a related analogue is approved for eyelash hypotrichosis), but the genetic follicular defect may not respond. May merit a focused literature search |
| 4–6 | Venous, arterial and neurogenic thoracic outlet syndrome | 99.72–99.78% | No credible mechanistic link (mechanical compression disorders) |
| 7 | Congenital hypotrichosis milia | 99.71% | Similar rationale to rank 3, but a rare congenital disorder |
| 8 | Angiodysplasia of stomach | 99.70% | No credible link; vasodilation could be undesirable in a bleeding lesion |
| 9 | Blue toe syndrome | 99.69% | Speculative only; topical dosing gives no relevant systemic exposure |
| 10 | Lymphangiectasis | 99.67% | Too indirect to support a hypothesis |

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

