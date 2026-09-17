---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 3
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2α analogue used to lower intraocular pressure in glaucoma and ocular hypertension. TxGNN predicts a possible link to **Visceral Calciphylaxis** with a near-maximal score, but currently there are **no clinical trials** and **no supporting literature** — this is a model-only prediction with a high likelihood of being a false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (topical eye drop) — based on known pharmacology; not confirmed via Australian regulatory data |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Travoprost is not available (data gap). Based on known pharmacology, Travoprost is a prostaglandin F2α analogue applied topically to the eye, where it lowers intraocular pressure by increasing uveoscleral outflow. Its systemic bioavailability is very low, which limits any plausible mechanism for extra-ocular effects.

Visceral calciphylaxis is driven by vascular calcification, endothelial dysfunction, and microthrombosis — a pathology with no established connection to prostaglandin F2α receptor activity in ocular tissue. The evidence pack's own mechanistic assessment concludes there is no known biological overlap, and judges this TxGNN output as likely model noise rather than a genuine repurposing signal.

The same pattern holds for the two lower-ranked predictions — venous and arterial thoracic outlet syndrome — which are anatomical/structural conditions (vascular compression at the thoracic outlet) rather than conditions amenable to a topical ocular hypotensive drug. All three candidates share an identical profile: extremely high TxGNN score, zero clinical or literature evidence, and weak-to-absent mechanistic rationale — consistent with the model surfacing high-confidence but biologically implausible associations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Australia Market Information

Travoprost currently has no ARTG entries and is not marketed in Australia (total registered licences: 0). No approved Australian product information exists at this time.

---

## Safety Considerations

Travoprost is not currently registered in Australia, so no TGA-approved Product Information is available for this evidence pack. Key warnings, contraindications, and drug interaction data are all marked as data gaps and require sourcing from overseas regulatory documentation (e.g., FDA/EMA product information) before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (and the two runner-up candidates) rests entirely on a TxGNN model score with no clinical trials, no literature, and no plausible mechanistic link — this does not meet the minimum evidence bar to progress beyond initial screening (S0).

**To proceed, the following is needed:**
- Confirmed original MOA and indications for Travoprost (currently data gaps — DG002)
- TFDA/TGA-equivalent product information, warnings, and contraindications (currently data gaps — DG001, blocking)
- Preclinical or mechanistic studies specifically linking PGF2α pathway activity to vascular calcification/calciphylaxis
- Confirmation of Australian regulatory pathway, given the drug is not currently marketed here
- Ongoing literature/trial monitoring, since none currently exists for any of the three predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

