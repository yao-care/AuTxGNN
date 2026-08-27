---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From EGFR-Mutant Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor used in EGFR-mutant non-small cell lung cancer (NSCLC) — this is drawn from literature captured in this evidence pack, as formal indication/licence text was not available. The TxGNN model predicts a possible link to **Fibromatosis, Gingival**, a benign gum tissue overgrowth condition, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale flags it as a likely spurious association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR-mutant non-small cell lung cancer (NSCLC) *(inferred from literature within this pack; TFDA/TGA licence text not available — Data Gap)* |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Gefitinib in this evidence pack (flagged as a High-severity data gap). Based on literature captured elsewhere in this pack, Gefitinib is an EGFR tyrosine kinase inhibitor whose established efficacy is in EGFR-mutant NSCLC, where it blocks EGFR-driven proliferative signalling in tumour epithelium.

Gingival fibromatosis is a benign, non-neoplastic overgrowth of gingival connective tissue, mechanistically distinct from EGFR-driven epithelial malignancy. The evidence pack's own model-generated rationale for this candidate states directly that there is "no known direct link" between the two, and that the high TxGNN score reflects a pure knowledge-graph prediction with no supporting evidence.

Taken together, the pharmacological rationale for this specific pairing is weak: a high similarity score from the prediction model has not been corroborated by any clinical, preclinical, or case-level literature. This pattern — high model score paired with no retrievable evidence — is consistent with a knowledge-graph artefact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial, literature, or mechanistic evidence connecting Gefitinib to gingival fibromatosis, and the model's own rationale identifies this as a likely false-positive knowledge-graph association. No Taiwan/TGA licensing or safety data exists to support even a preliminary safety review.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information, including warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data for Gefitinib (currently a High-severity data gap)
- Any preclinical or case-level evidence specifically linking EGFR-TKI therapy to gingival fibromatosis, before this candidate can move past S0

**Note:** Within this same evidence pack, three other candidates — *lung hilum carcinoma* (rank 5), *lung germ cell tumor* (rank 8), and *pulmonary sulcus neoplasm* (rank 9) — are anatomic subtypes or regions of NSCLC and show closer mechanistic alignment with Gefitinib's established EGFR-driven indication. These may warrant a separate, dedicated evaluation report rather than being assessed under the top TxGNN-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

