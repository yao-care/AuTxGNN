---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
---

# Olanzapine
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

# Olanzapine: From Schizophrenia/Bipolar I Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Olanzapine is an atypical antipsychotic (5-HT2A/D2 receptor antagonist) originally used for schizophrenia and bipolar I disorder. The TxGNN model's top-ranked prediction for this drug is **Benign Paroxysmal Torticollis of Infancy**, but this association is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely statistical artifact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and bipolar I disorder (atypical antipsychotic; TFDA/ARTG licence data not available — see Market Information below) |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Olanzapine is not available in this evidence pack (flagged as a High-severity data gap). Based on other information within the pack, Olanzapine is known to act primarily through D2 dopamine and 5-HT2A serotonin receptor antagonism, a mechanism well established in the treatment of psychotic and mood disorders.

For this specific prediction, however, the evidence pack's own mechanistic rationale is explicit that **no pharmacological link exists**: benign paroxysmal torticollis of infancy is generally regarded as a migraine-variant channelopathy, and it has no known relationship to Olanzapine's D2/5-HT2A antagonism. The reviewer notes this is most likely a statistical association produced by the TxGNN model rather than a mechanism-driven signal.

Because no clinical trials, no literature, and no coherent mechanistic story support this candidate, it should be treated as a low-confidence, exploratory hit only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Olanzapine has no ARTG entries in this evidence pack (market status: **Not marketed**, 0 licences on record). No product, dosage form, or approved-indication data is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (TFDA warnings/contraindications and a formal DDI search were both attempted but returned no data — this is flagged in the evidence pack as a Blocking data gap for safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (benign paroxysmal torticollis of infancy) has no supporting clinical trials or literature, and the pack's own mechanistic review characterises it as a statistical artifact rather than a genuine biological signal. Combined with the absence of Australian market registration and a blocking gap in safety/PI data, there is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/TGA Product Information (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action detail from DrugBank — currently a High-severity gap
- Any independent evidence (preclinical or clinical) connecting Olanzapine to benign paroxysmal torticollis of infancy, none of which currently exists

**Note:** This same evidence pack contains other Olanzapine candidates with materially stronger evidence — notably *neurotic depression* and *melancholia* (both L2/S2, ~20 supporting publications each, consistent with the established olanzapine–fluoxetine combination used in treatment-resistant depression), and *agoraphobia*/*dysthymic disorder* (L3/S1). If repurposing evaluation continues, one of these better-substantiated candidates would be a more productive next target than the top TxGNN-ranked hit reported here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

