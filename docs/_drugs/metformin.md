---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Metformin
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

# Metformin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

> Metformin is a well-established biguanide antidiabetic agent (background knowledge — not present in this evidence pack, which records no original indication data).
> The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, with a very high similarity score of **99.45%**, but **zero clinical trials and zero publications** currently support this specific link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no TFDA/ARTG license data returned) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed (per this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

*Note: this evidence pack found no ARTG registration for metformin. Given metformin is widely used clinically, this most likely reflects a gap in this data collection run rather than genuine market absence — worth independently verifying against the TGA ARTG database before treating "not marketed" as fact.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Metformin's known pharmacology is AMPK activation, suppression of hepatic gluconeogenesis, and improved insulin sensitivity — a metabolic mechanism used in type 2 diabetes management.

Classic Stiff Person Syndrome, by contrast, is an autoimmune neurological disorder (predominantly anti-GAD65 antibody-mediated) with pathology centred on disrupted GABAergic neurotransmission. There is no established mechanistic overlap between metformin's insulin-sensitising pathway and GABAergic autoimmune neurotransmission.

The rationale accompanying this prediction is explicit that the very high TxGNN score is more likely explained by shared "diabetes comorbidity" nodes in the knowledge graph than by a genuine biological relationship. In other words, this specific prediction should be treated as a network-proximity artefact rather than a mechanistically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Australia Market Information

No ARTG entries were returned for metformin in this evidence pack (total licenses: 0), so no product/dosage-form table can be generated. This should be verified directly against the ARTG before relying on it, since metformin products are commonly marketed internationally.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — this is a model-only prediction with no supporting clinical trials or literature, and the accompanying mechanistic rationale itself flags the score as a likely knowledge-graph artefact rather than a true drug–disease relationship.

**To proceed, the following is needed:**
- Confirm metformin's actual ARTG/TGA market status in Australia (this pack's "not marketed" result conflicts with common knowledge and should be re-verified)
- TFDA/TGA Product Information warnings and contraindications (currently a blocking data gap, DG001)
- Detailed mechanism of action data from DrugBank (currently a high-severity data gap, DG002)
- Any preclinical or mechanistic studies specifically linking metformin/AMPK pathways to GABAergic autoimmune disease, if this candidate is to be pursued further

*For reference, two other candidates in this pack carry marginally stronger (though still weak) evidence and may be worth independent tracking: **pancreatic agenesis** (rank 8, L4, 20 literature hits — though the rationale notes these are largely indirect diabetes/pancreatic-cancer keyword matches, not agenesis-specific) and **homozygous familial hypercholesterolemia** (rank 10, L4, staged as "Research Question" on the basis of a 1988 in-vitro cholesterol-synthesis study).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

