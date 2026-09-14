---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Tramadol is a centrally-acting analgesic (mu-opioid agonist with SNRI activity) used for moderate-to-severe pain.
> The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare GDF5-related skeletal dysplasia,
> but this prediction is currently supported by **no clinical trials** and **no published literature**, and the underlying rationale itself flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain management (moderate-to-severe pain; opioid/SNRI mechanism per rationale data) — no ARTG-approved indication text available |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not directly available in this evidence pack (original_moa is flagged as a data gap, DG002). However, the repurposing rationale confirms tramadol acts as a weak mu-opioid receptor agonist combined with serotonin-noradrenaline reuptake inhibition (SNRI), a mechanism established for pain control rather than for disease-modifying effects in skeletal or connective tissue disorders.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare genetic skeletal dysplasia caused by GDF5 gene defects, affecting cartilage and bone growth. There is no known pharmacological pathway connecting tramadol's opioid/SNRI activity to GDF5-mediated skeletal development. The evidence pack's own rationale explicitly states that this high TxGNN score is most likely a **false positive**, arising from co-occurrence of skeletal-related nodes in the knowledge graph rather than a genuine mechanistic link. At best, tramadol could theoretically be used for symptomatic pain relief in patients with this condition — but this would be off-label symptom management, not a repurposed disease-targeted indication, and no data currently supports even this narrower use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for this candidate — tramadol is listed as **Not Marketed** in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that a blocking data gap (DG001) has been identified: TGA/PI warnings and contraindications for tramadol have not yet been retrieved, which prevents progression to a formal safety (S1) evaluation for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a model score (Evidence Level L5), with zero clinical trials and zero literature citations. The rationale accompanying this prediction explicitly identifies it as a probable knowledge-graph false positive rather than a biologically plausible repurposing candidate, so it does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TGA/PI warnings, contraindications and safety data for tramadol (DG001 — blocking)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Independent preclinical or mechanistic evidence linking opioid/SNRI activity to GDF5-related skeletal pathology, before any further clinical evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

