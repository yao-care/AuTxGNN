---
layout: default
title: Aclidinium
parent: Model Prediction Only (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Aclidinium: predicted new indication Open-angle glaucoma (evidence level L5). Approved use: Not stated in the data compiled for this report (aclidinium is genera…"
monitor_inn: "Aclidinium"
predicted_indications: ["open-angle glaucoma", "primary hereditary glaucoma", "migraine disorder", "migraine with brainstem aura", "irritable bowel syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "glaucoma 1, open angle", "gastroduodenitis", "dermatitis"]
---

# Aclidinium
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

# Aclidinium: From COPD to Open-Angle Glaucoma

## One-Sentence Summary

Aclidinium is an inhaled long-acting muscarinic antagonist (LAMA) marketed in Australia as Bretaris Genuair. The TxGNN model predicts it may be effective for **open-angle glaucoma**, but this is a graph-based prediction only, with **0 clinical trials** and **0 relevant publications** supporting it. The mechanism also points toward a possible safety concern rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (aclidinium is generally known as a COPD maintenance bronchodilator) |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 89.36% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Aclidinium is known to be an inhaled long-acting muscarinic antagonist (LAMA), and its efficacy in its original respiratory indication is established.

For open-angle glaucoma, the mechanistic logic does not support the prediction. Muscarinic antagonists are generally associated with mydriasis and a risk of raised intraocular pressure or angle closure, so a therapeutic benefit is implausible and the drug class may be a safety concern in glaucoma. The high score (0.89) reflects knowledge-graph similarity only.

Other top-ranked predictions are also unsupported by clinical data:
- **Primary hereditary glaucoma and glaucoma 1, open angle:** same concern as above.
- **Migraine disorder, migraine with brainstem aura, headache disorder, trigeminal autonomic cephalalgia:** muscarinic involvement in pain pathways is speculative, and aclidinium has low systemic exposure.
- **Irritable bowel syndrome and gastroduodenitis:** other antimuscarinics are used for gut cramping, giving a class-level rationale, but inhaled aclidinium is rapidly hydrolysed in plasma, so gut exposure is expected to be negligible.
- **Dermatitis:** no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No relevant literature is available for open-angle glaucoma. The only publication retrieved across the predictions (for dermatitis) is not relevant to the predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23679347](https://pubmed.ncbi.nlm.nih.gov/23679347/) | 2013 | RCT (COPD) | COPD | One-year extension of ACCORD COPD I assessing safety and efficacy of twice-daily aclidinium 200 µg and 400 µg in COPD. Not a glaucoma or dermatitis study. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10124W | Bretaris Genuair | Powder for oral inhalation in breath actuated device, 322 micrograms (as bromide) per dose, 60 doses | Not stated in the data compiled |

## Safety Considerations

**Drug Interactions:** 100 potential interactions were identified. The 20 listed in the data compiled for this report are all rated Moderate, and most are other anticholinergic or antimuscarinic agents, where additive effects are expected. Examples:
- Atropine
- Clidinium
- Dicyclomine
- Glycopyrronium
- Hyoscyamine
- Scopolamine
- Trospium
- Amitriptyline
- Promethazine
- Chlorpheniramine

Others include eluxadoline, prucalopride, acetylcholine and inhaled human insulin.

**Ocular concern:** as a muscarinic antagonist, aclidinium may raise intraocular pressure or precipitate angle closure, which is directly relevant to the predicted glaucoma indication.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or relevant literature. The anticholinergic mechanism suggests potential harm rather than benefit in glaucoma, and systemic exposure from the inhaled route is minimal for the other predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data and the approved indication text from the PI
- Review of the PI warnings and contraindications, particularly for narrow-angle glaucoma
- Preclinical or clinical evidence that a muscarinic antagonist could lower intraocular pressure (none currently exists)
- Confirmation of whether the route of administration is compatible with any proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

