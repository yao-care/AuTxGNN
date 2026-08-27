---
layout: default
title: Perhexiline
parent: 僅模型預測 (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
---

# Perhexiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Perhexiline: From Angina Pectoris to Migraine Disorder

## One-Sentence Summary

Perhexiline is a cardiac metabolic modulator historically used for angina pectoris (a CPT-1 inhibitor affecting myocardial fatty-acid oxidation). The TxGNN model predicts it may be effective for **Migraine Disorder**, with a high similarity score of **99.04%**, but currently **no clinical trials and no migraine-specific literature** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (based on known pharmacology and literature; not formally recorded in the evidence pack) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for Perhexiline is not available (DrugBank MOA field is a recorded data gap). What is known from the accompanying analysis is that Perhexiline acts primarily as an inhibitor of carnitine palmitoyltransferase-1 (CPT-1), shifting cardiac energy metabolism away from fatty-acid oxidation and towards glucose oxidation, and that it is metabolised via CYP2D6. It has historically been used to treat angina pectoris.

The predicted link to migraine disorder has **no known mechanistic basis**. Migraine pathophysiology centres on the trigeminovascular system and CGRP-mediated neurogenic inflammation — pathways that do not overlap with CPT-1 inhibition or fatty-acid metabolism. The evidence pack's own rationale explicitly states there is no known mechanistic connection between Perhexiline's pharmacology and migraine.

In other words, this prediction is driven purely by TxGNN embedding similarity rather than by biological plausibility, clinical trial data, or published literature. It should be treated as a hypothesis-generating signal only, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

*(Searches for "Perhexiline" + "migraine disorder" across ClinicalTrials.gov, ICTRP and PubMed all returned zero results. Literature retrieved for other, lower-ranked candidate indications — e.g. a 1975 angina pectoris trial matched under "headache disorder," and general periodontitis background papers matched under a rare malformation-syndrome term — were keyword mismatches, not drug-specific evidence, and are not included here.)*

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine indication is an L5 prediction — a pure computational signal with no supporting clinical trials, no disease-specific literature, and no established mechanistic pathway linking CPT-1 inhibition to migraine pathophysiology. There is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- A confirmed Product Information / regulatory safety document for Perhexiline (currently a blocking data gap — required before any S1 safety assessment)
- A verified DrugBank mechanism-of-action record
- A confirmed original indication record (angina pectoris is inferred from pharmacology, not formally documented in this evidence pack)
- Targeted, disease-specific literature and trial searches for Perhexiline in migraine, since current search hits are keyword mismatches
- Preclinical or mechanistic studies exploring any plausible CPT-1/fatty-acid oxidation link to migraine, if this direction is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

