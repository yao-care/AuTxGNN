---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Permanent Neonatal Diabetes Mellitus

## One-Sentence Summary

> Insulin aspart is a rapid-acting insulin analogue whose established use is glycaemic control in diabetes mellitus.
> Within this evidence pack, the TxGNN model's top-ranked prediction (**Type 1 Diabetes Mellitus**, 99.95%) is **not a genuine repurposing signal** — the evidence pack's own annotations confirm this is already an original approved indication for insulin aspart, surfaced only due to a data gap in `original_indications`.
> The strongest **genuine** repurposing candidate is **Permanent Neonatal Diabetes Mellitus (PNDM)** (99.55%), a rare monogenic disease supported by direct mechanistic reasoning and **1 review-level publication**, though currently **no clinical trials** specifically target this population.

---

## ⚠ Data Quality Note

Before reading further: this evidence pack lists "type 1 diabetes mellitus" as the #1-ranked prediction with the strongest evidence (8 Phase 3/4 trials, 20 publications). **This is not a repurposing candidate.** The pack's own `repurposing_rationale` field explicitly states T1D is one of insulin aspart's original approved indications, and its appearance as a "prediction" reflects a data gap (`original_indications: []`) rather than a real new-use signal. It is excluded from this report's primary recommendation to avoid misleading readers. Several lower-ranked candidates (autoimmune oophoritis, opsismodysplasia, stiff person syndrome variants, and both lipodystrophy entries) are similarly flagged in the pack as likely knowledge-graph co-occurrence artefacts or, in the case of lipodystrophy, reverse-causality errors (insulin injection is a known **cause** of localized lipodystrophy, not a treatment for it). These are excluded here as well.

This report instead focuses on **Permanent Neonatal Diabetes Mellitus (rank 5)**, the highest-ranked candidate with an actual, coherent mechanistic and evidentiary basis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1/Type 2) — inferred from the pack's own rationale annotations; `original_indications` and `original_moa` are recorded as data gaps and not independently confirmed here |
| Predicted New Indication | Permanent Neonatal Diabetes Mellitus (PNDM) |
| TxGNN Prediction Score | 99.55% (rank 5556 among all predictions) |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on established pharmacology, insulin aspart is a rapid-acting human insulin analogue that binds the insulin receptor to promote peripheral glucose uptake and suppress hepatic glucose output.

PNDM is typically caused by mutations in *KCNJ11*, *ABCC8*, or *INS*, resulting in an absolute deficiency of endogenous insulin secretion from infancy — mechanistically identical to the insulin deficiency insulin aspart already treats in Type 1 diabetes. The rapid onset/offset kinetics of insulin aspart are also practically well-suited to the frequent, small-volume dosing or pump-based delivery typically required in neonatal and paediatric care.

Insulin replacement is already standard clinical practice for PNDM. What this evidence pack captures, however, is that **direct trial-level evidence specific to PNDM is absent** — the single supporting publication is a general review rather than a controlled study, so the mechanistic case is strong but the documented evidence base is thin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28527303](https://pubmed.ncbi.nlm.nih.gov/28527303/) | 2017 | Review | Diabetes Research and Clinical Practice | Reviews insulin usage in neonatal diabetes mellitus, with a focus on continuous subcutaneous insulin infusion (CSII) as management for this rare disorder |

---

## Australia Market Information

No ARTG entries were found for insulin aspart in this evidence pack (`total_licenses: 0`), and market status is recorded as **Not Marketed**. Confirmation of current TGA/ARTG registration status should be verified directly against the TGA database before any clinical decision-making, as this may reflect a data collection gap rather than genuine absence from the Australian market (insulin aspart products are widely marketed internationally).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The insulin-deficiency mechanism directly supports insulin replacement in PNDM, and this is already accepted clinical practice — but the evidence pack contains only one indirect review, no PNDM-specific clinical trials, and no confirmed Australian market/ARTG registration for insulin aspart.

**To proceed, the following is needed:**
- Verification of current TGA/ARTG registration status for insulin aspart (the "0 ARTG entries / Not Marketed" result should be confirmed, not assumed correct)
- TFDA/TGA Product Information for formal safety, contraindication, and interaction data (all currently data gaps)
- Confirmed original indications and MOA documentation for insulin aspart (currently data gaps in this pack)
- Direct clinical or observational evidence in PNDM populations, beyond the single available review article
- Re-validation of the TxGNN pipeline's handling of already-approved indications (e.g. T1D here) so they are not presented as novel repurposing candidates in future evidence packs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

