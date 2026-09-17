---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Raloxifene
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

# Raloxifene: From Osteoporosis to Duodenal Ulcer (Disease)

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM) established in postmenopausal osteoporosis treatment and, per TGA-approved labelling, invasive breast cancer risk reduction. The TxGNN model's top-ranked prediction for this drug is **duodenal ulcer (disease)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis found no plausible biological link — it is flagged internally as likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis in postmenopausal women (structured field in evidence pack is empty; see Data Verification Note below) |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Australia Market Status | Reported as "Not marketed" in evidence pack — **see Data Verification Note, this appears incorrect** |
| Number of ARTG Entries | 0 (evidence pack) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in this evidence pack. Based on well-established pharmacology, raloxifene is a SERM acting as an estrogen receptor antagonist/agonist across bone, breast and endometrial tissue, with its clinical effect driven by inhibition of osteoclast-mediated bone resorption.

There is no established pathway linking SERM activity to duodenal ulcer pathophysiology (gastric acid secretion, mucosal protection, or *H. pylori*-related mechanisms). The evidence pack's own repurposing rationale for this candidate states explicitly that this is a "pure graph-based connection with no clinical or literature support," despite the high TxGNN similarity score.

This is a case where a high model confidence score is **not** accompanied by any experimental or mechanistic corroboration. TxGNN scores reflect knowledge-graph embedding similarity, not validated pharmacology, and should be treated with particular caution when — as here — zero supporting trials or publications exist and the mechanistic write-up itself contradicts the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

**Data Verification Note:** The evidence pack reports raloxifene as "not marketed" with 0 ARTG entries. A cross-check against the public TGA ARTG register found an active registration that the evidence pack's regulatory query appears to have missed:

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 64709 | EVISTA (raloxifene hydrochloride 60 mg), Eli Lilly Australia Pty Ltd | Tablet, blister pack | Treatment of osteoporosis in postmenopausal women; reduction of invasive breast cancer risk (per TGA/PI summary) |

This is an external verification, not sourced from the evidence pack itself — the underlying pipeline gap (DG001, "TFDA/TGA warnings and contraindications" data gap, severity Blocking) should be corrected so the regulatory query correctly matches this ARTG record.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (Evidence pack fields for key warnings, contraindications, and drug interactions are all marked as data gaps; DG001 flags this as a **Blocking** gap that prevents a preliminary safety assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (duodenal ulcer) has a high TxGNN score but zero supporting clinical trials or literature, and the evidence pack's own mechanistic assessment concludes the link is not biologically plausible — most likely graph-connectivity noise rather than a genuine pharmacological signal.
- A Blocking data gap (missing TGA-approved warnings/contraindications) prevents even a preliminary safety (S1) evaluation.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently blocking further evaluation
- Confirmed mechanism-of-action data from DrugBank
- Correction of the regulatory data pipeline to reflect the existing ARTG 64709 registration
- Independent mechanistic or preclinical evidence for the duodenal ulcer link before any further investment, given the current absence of support

**Note on other candidates in this evidence pack:** Of the 10 predicted indications supplied, 9 have no supporting evidence (evidence level L5) and one — pregnancy-associated osteoporosis (rank 8) — reaches L4, but its only clinical trial is graded "C" relevance (mismatched population) and its rationale flags a safety contradiction (raloxifene is contraindicated in pregnancy). All 10 candidates carry a "Hold" recommendation; none currently support progression past S0.

Sources:
- [EVISTA raloxifene hydrochloride 60mg tablet blister pack (64709) | TGA](https://www.tga.gov.au/resources/artg/64709)
- [Australian Product Information - EVISTA (raloxifene)](https://medsinfo.com.au/api/documents/Evista_PI?format=pdf)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

