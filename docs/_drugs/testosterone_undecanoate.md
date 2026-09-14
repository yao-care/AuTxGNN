---
layout: default
title: Testosterone Undecanoate
parent: 僅模型預測 (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Testosterone Undecanoate
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

# Testosterone Undecanoate: From Androgen Replacement Therapy to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Testosterone undecanoate is an androgen, generally used for testosterone/androgen replacement therapy (this evidence pack does not itself contain formal original-indication data for the drug). The TxGNN model's top-ranked prediction suggests possible relevance to **Homozygous Familial Hypercholesterolemia**, but this is currently supported by **no clinical trials** and **no published literature** — it is a model-score-only signal, and the proposed mechanism does not clearly align with known androgen pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (testosterone undecanoate is generally used for androgen/testosterone replacement therapy, e.g. male hypogonadism) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 98.73% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for testosterone undecanoate is not available in this evidence pack (a flagged data gap). Based on general pharmacological knowledge, testosterone undecanoate is an androgen used for testosterone replacement, acting via the androgen receptor.

There is no established biological pathway linking androgen receptor signalling to the LDL-receptor gene defect that underlies homozygous familial hypercholesterolemia (HoFH). If anything, the literature on testosterone and lipid metabolism points in the opposite direction — androgens are more often associated with lowering HDL cholesterol rather than correcting the LDL-receptor defect that drives HoFH. Combined with the complete absence of supporting clinical trials or publications, the evidence pack's own assessment is that this top-ranked score likely reflects embedding similarity noise in the knowledge graph rather than a genuine mechanistic relationship.

For context, several **lower-ranked** predictions in this dataset have a more plausible mechanistic basis and, in one case, actual clinical literature: androgen insensitivity syndrome (rank 2, L3 evidence, 2 published studies on testosterone/testosterone undecanoate use), Leydig cell hypoplasia due to LH resistance (rank 3), and 46,XY disorders of sex development due to impaired androgen production (rank 4) — all conditions where exogenous androgen replacement is mechanistically direct (compensating for absent or unresponsive endogenous androgen signalling). These may warrant separate follow-up evaluation even though they are not the top TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: TGA-equivalent warning/contraindication data could not be retrieved for this drug in this evidence pack (a flagged blocking data gap), so a formal safety pre-assessment could not be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HoFH) rests solely on an L5 model score with no clinical trial or literature support, and its proposed mechanism is not well aligned with known androgen pharmacology. The drug is also not currently marketed in Australia, and safety/contraindication data could not be retrieved, which blocks a formal safety pre-assessment.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, precautions, contraindications) — currently unavailable and blocking safety review
- Confirmed mechanism-of-action data for testosterone undecanoate
- Formal original-indication/registration data for the drug
- If repurposing is pursued, consider prioritising the mechanistically stronger, lower-ranked candidates (e.g. androgen insensitivity syndrome, L3 evidence) over the top TxGNN score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

