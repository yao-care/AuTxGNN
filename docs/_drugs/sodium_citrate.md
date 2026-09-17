---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
---

# Sodium Citrate
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

# Sodium Citrate: From an Undocumented Original Indication to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate (DrugBank DB09154) has no original indication or mechanism-of-action data recorded in this evidence pack, and the drug is currently not marketed in Australia. The TxGNN model's top-ranked prediction is that it may be effective for **Papillary Conjunctivitis**, but this is supported by **0 clinical trials** and **0 publications** — a pure knowledge-graph signal with no mechanistic or empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug-level data gap) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sodium citrate is not available in this evidence pack (flagged as a High-severity data gap, DG002), and no original indication has been recorded for the drug either. Without either reference point, there is no basis in the supplied data to assess pharmacological plausibility for an ophthalmic anti-inflammatory or anti-allergic effect.

The evidence pack's own rationale for this prediction is explicit on this point: there is no known mechanistic link, and sodium citrate has no documented pharmacological basis for topical anti-inflammatory or anti-allergic activity relevant to conjunctivitis. The prediction rests solely on the TxGNN knowledge-graph score (0.9995, rank 1095 overall) with no corroborating clinical trial or literature evidence returned by any of the three query sources (ClinicalTrials.gov, ICTRP, PubMed).

This should be read as a hypothesis-generating signal only — useful for flagging a candidate worth future investigation, but not one with any current mechanistic or empirical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Sodium citrate has no ARTG entries and is not currently marketed in Australia according to this evidence pack (0 total licenses recorded).

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is available in this evidence pack. The DDI query returned "not found," and both key warnings and contraindications are recorded as data gaps. Since sodium citrate is not currently marketed in Australia, there is also no TGA-approved Product Information to reference. Retrieval of the underlying product label/warning data is flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety assessment (S1 stage) can begin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Papillary Conjunctivitis is supported only by a TxGNN graph score, with no clinical trials, no literature, and no documented mechanistic rationale — evidence level L5, the lowest tier (model prediction only). There is nothing in the current pack to justify moving this indication past the S0 screening stage.

**To proceed, the following is needed:**
- Mechanism-of-action data for sodium citrate (DG002)
- TFDA/TGA label warnings and contraindications (DG001 — blocking; required before any S1 safety review)
- Original indication documentation for the drug, to establish a baseline for mechanistic comparison
- Any preclinical or in vitro pharmacology data supporting ophthalmic anti-inflammatory/anti-allergic activity
- Targeted literature or trial search specifically linking sodium citrate (not other citrate salts) to conjunctival/ocular allergic conditions

*Note: This evidence pack also contains several other TxGNN-predicted indications for sodium citrate with comparatively stronger (though still preliminary) evidence — notably "stomach disease" (L3, decision stage S1, 50 trials/20 publications, though most trials involve unrelated citrate salts) and "intestinal obstruction" (L4, S1, 15 trials/8 publications). If the intent is to evaluate the drug's best-supported repurposing candidate rather than strictly the top-ranked TxGNN score, "stomach disease" would be the more evidence-rich subject for a follow-up report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

