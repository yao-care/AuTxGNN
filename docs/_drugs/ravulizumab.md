---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

Using the evidence pack as provided (Ravulizumab / DB11580, Australia regulatory context). Note: the drug's `original_moa` and `original_indications` fields are blank data gaps in this pack — the only in-pack reference to ravulizumab's known indication/mechanism is embedded in the repurposing rationale text (aHUS, terminal complement C5 blockade), which I've used rather than outside knowledge.

---

# Ravulizumab: From Atypical Haemolytic Uraemic Syndrome (aHUS) to Congenital Neutropenia (G6PC3 deficiency)

## One-Sentence Summary

Ravulizumab's formal original-indication and mechanism-of-action fields are not populated in this evidence pack, but internal rationale text identifies it as a terminal complement (C5) inhibitor already approved for aHUS, a complement-mediated thrombotic microangiopathy.
The TxGNN model's top prediction is **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this pack has **0 clinical trials** and **0 publications** supporting it — and the model's own mechanistic note flags the association as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in structured fields; referenced only in rationale text as aHUS (complement-mediated TMA) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% (rank 960 overall) |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ravulizumab is not available as a structured field in this pack (marked as a data gap). However, the rationale text attached to every candidate consistently describes ravulizumab as a terminal complement pathway inhibitor acting on C5 / the C5a–C5aR1 axis, consistent with its already-established use in aHUS, a complement-mediated thrombotic microangiopathy.

For the top-ranked candidate specifically, the model's own mechanistic assessment argues **against** biological plausibility: G6PC3-deficient congenital neutropenia arises from a glucose-metabolism defect that increases neutrophil apoptosis, and has no known causal link to the C5 pathway. If anything, C5 blockade would blunt C5a–C5aR1-driven neutrophil chemotaxis — the opposite of a therapeutic direction. The pack itself attributes the high score to knowledge-graph node proximity ("neutrophil/immune" clustering) rather than genuine shared biology, i.e. a likely false positive.

Among the ten ranked candidates, only **primary hyperoxaluria** (rank 3) reaches decision stage S1 ("Research Question"): its rationale notes that hyperoxaluria-driven renal calcium-oxalate deposition can trigger a thrombotic microangiopathy, giving a theoretical overlap with ravulizumab's approved aHUS mechanism — though still with no supporting trials or literature. All other candidates, including the top-ranked one, are assessed as mechanistically weak or contrary and are held at S0.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Ravulizumab is not currently registered on the ARTG (0 entries; market status: not marketed in Australia). No product-level dosage form or approved-indication data is available in this pack.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical or literature support (evidence level L5) and is flagged by the model's own rationale as a likely knowledge-graph artefact with a mechanistically contrary direction. Ravulizumab is also not currently marketed in Australia, and core drug-level data (MOA, TGA warnings/contraindications) are outstanding blocking gaps in this pack.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Formal mechanism-of-action record for ravulizumab (DG002)
- If pursuing further, prioritise re-evaluating rank 3 (primary hyperoxaluria) instead, since it is the only candidate reaching S1 and has a mechanistically coherent (if still unproven) rationale
- Confirmation of ravulizumab's original approved indication(s) from a primary regulatory source, since this pack only references it indirectly via rationale text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

