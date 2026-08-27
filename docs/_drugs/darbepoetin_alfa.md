---
layout: default
title: Darbepoetin Alfa
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Darbepoetin Alfa
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

# Darbepoetin Alfa: From Anaemia to Amenorrhea

## One-Sentence Summary

Darbepoetin alfa is an erythropoiesis-stimulating agent whose established use, referenced within this evidence pack's own trial and literature data, is anaemia related to chronic kidney disease and chemotherapy. The TxGNN model's top-ranked prediction is **Amenorrhea**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale states there is no known mechanistic link. This is a prediction-only signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no ARTG licence/indication text on file (see Australia Market Information below) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 96.73% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for darbepoetin alfa in this evidence pack (Data Gap DG002). Based on the trial and literature text retrieved elsewhere in this pack, darbepoetin alfa is an erythropoiesis-stimulating agent (ESA), used for anaemia associated with chronic kidney disease and chemotherapy-induced anaemia.

For the top-ranked prediction, **Amenorrhea**, the model itself flags the mechanistic link as absent: there is no known EPO/EPOR pathway interaction with the hypothalamic-pituitary-ovarian axis, and the score reflects a raw knowledge-graph prediction with no supporting clinical or literature evidence.

It is worth noting that across all 10 predicted indications in this evidence pack, none reached beyond Hold, and only one (anaphylaxis, rank 3) returned any real-world evidence — 3 clinical trials and 1 case report. That evidence, however, points the opposite direction: the literature describes darbepoetin *causing* allergic/anaphylactoid reactions (a desensitisation case report), not treating anaphylaxis, and the trials are general anaemia/iron-supplementation studies unrelated to this indication. This pattern — high TxGNN scores with contradicted or absent mechanistic support — suggests the current candidate set for darbepoetin alfa is not yet actionable.

## Clinical Trial Evidence

Currently no related clinical trials registered for Amenorrhea.

## Literature Evidence

Currently no related literature available for Amenorrhea.

## Australia Market Information

No ARTG entries are recorded for darbepoetin alfa in this evidence pack — the drug is listed as not currently marketed in Australia (0 licences on file).

## Safety Considerations

No warnings, contraindications, or drug-interaction data were returned for this evidence pack, and no Australian Product Information is on file (consistent with the drug not being marketed in Australia per this data). Safety assessment cannot proceed until TGA/ARTG-sourced Product Information, or an equivalent overseas PI, is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Amenorrhea) has no clinical trial or literature support, and the model's own rationale states no plausible mechanistic link exists — this is an L5, prediction-only signal.
- No candidate across the full ranked list (10 indications) reached beyond Hold; the one indication with real evidence (anaphylaxis) points to a safety signal against the drug rather than a therapeutic use for it.
- Core safety data (warnings, contraindications, DDI) is missing, which blocks any S1 safety pre-assessment regardless of indication.

**To proceed, the following is needed:**
- TFDA/TGA product information — warnings and contraindications (Data Gap DG001, currently Blocking)
- Verified mechanism of action data (Data Gap DG002)
- Preclinical or mechanistic evidence linking EPO/EPOR signalling to the reproductive axis, before further evidence collection on Amenorrhea is warranted
- Confirmation of current Australian market/ARTG registration status for darbepoetin alfa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

