---
layout: default
title: Olsalazine
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 10
---

# Olsalazine
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

# Olsalazine: From Ulcerative Colitis to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is a 5-aminosalicylate (5-ASA) prodrug whose established use is ulcerative colitis. The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone, and the pack's own mechanistic review flags it as a likely knowledge-graph adjacency artefact rather than a genuine pharmacological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (per known pharmacology cited in the mechanistic rationale; not present as a structured field in this pack) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this pack (marked as a data gap). Based on the mechanistic rationale supplied alongside the prediction, olsalazine is a 5-ASA prodrug that is cleaved by gut bacteria to release the active moiety locally in the colon, where it exerts anti-inflammatory (COX/LOX inhibition, NF-κB modulation) and antioxidant effects. Its established efficacy is confined to ulcerative colitis.

Myelodysplastic syndrome is a clonal bone marrow stem-cell disorder — a pre-leukaemic haematological condition — and has no established biological connection to gut-localised anti-inflammatory activity. The evidence pack itself states this directly: the high TxGNN score most likely reflects proximity between "inflammation/immune modulation" nodes in the knowledge graph rather than a mechanistically derived relationship.

Given olsalazine's very low systemic bioavailability (it is designed for local colonic action), a plausible route to any systemic haematological effect is not apparent from the available information. This prediction should be treated as a hypothesis-generating model output only, not as evidence of biological plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5, model prediction only) with no clinical trials or literature, and the pack's own mechanistic assessment considers the drug–disease link to be a likely graph-adjacency artefact rather than a biologically grounded hypothesis. There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/TGA-sourced Product Information (warnings, contraindications) — currently a blocking data gap
- Confirmed original mechanism of action (MOA) data from DrugBank or another primary source
- An independent pharmacological/preclinical rationale linking 5-ASA activity to MDS pathophysiology, given the current mechanistic review argues against a plausible link
- Ongoing monitoring for any future clinical trial or literature signal on this drug–disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

