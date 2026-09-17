---
layout: default
title: Resorcinol
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Resorcinol
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

# Resorcinol: From Topical Acne Treatment to Acne Keloid

## One-Sentence Summary

Resorcinol is generally known as a topical keratolytic/mild antibacterial agent used in dermatology for acne-related skin conditions, though formal original-indication data is not available in this evidence pack. The TxGNN model predicts possible effectiveness for **Acne Keloid** (acne keloidalis), but this is currently supported by **zero clinical trials** and **zero published literature** — the 99.83% prediction score reflects model output only, not an actual evidence base.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (drug not marketed in Australia; no approved-indication record on file) |
| Predicted New Indication | Acne Keloid (acne keloidalis) |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available (original_moa: Data Gap). Based on general pharmacological knowledge, Resorcinol is a topical keratolytic and mild antibacterial agent, historically used in dermatology for acne and follicular hyperkeratosis-related skin lesions. Acne keloidalis also involves follicular hyperkeratosis and chronic inflammation, which gives a superficial, organ-system-level rationale for the prediction.

However, the evidence pack's own rationale explicitly flags this as a weak link: the high TxGNN score more likely reflects proximity of "acne"-related nodes within the knowledge graph than a genuine, mechanism-validated causal relationship. This caution applies consistently across all 10 top-ranked predictions for this drug — several (e.g. ankylosing spondylitis, rheumatoid vasculitis, hypermobility of coccyx, polyarticular juvenile rheumatoid arthritis) involve organ systems with no plausible pharmacological connection to a topical keratolytic agent. This pattern indicates the predictions are likely graph-embedding artifacts rather than validated repurposing signals, and the top-ranked "acne keloid" result should be read with the same caution.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

Note: TFDA-equivalent warning/contraindication data is marked as a **Blocking**-severity data gap in this evidence pack (DG001) — this currently prevents any formal S1 safety assessment from being conducted for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence supports any of the 10 top-ranked predicted indications for Resorcinol, mechanism-of-action data is unavailable, safety data is blocked by an unresolved data gap, and the drug currently has zero ARTG entries in Australia. There is no actionable basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Resolution of DG001 (TFDA/TGA-equivalent product warnings and contraindications) and DG002 (mechanism of action)
- Confirmed original approved-indication history for Resorcinol
- Preclinical or mechanistic studies specifically linking resorcinol to acne keloidalis pathophysiology
- A targeted literature/trial search using validated disease synonyms (e.g. "acne keloidalis nuchae", "folliculitis keloidalis") to check for evidence missed by the current search terms
- Clarification of the Australian regulatory/market pathway, given the drug is currently unregistered (0 ARTG entries)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

