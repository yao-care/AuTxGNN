---
layout: default
title: Migalastat
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Migalastat
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

# Migalastat: From Fabry Disease to Hepatoportal Sclerosis

## One-Sentence Summary

Migalastat is a pharmacological chaperone originally used to treat Fabry disease in patients with amenable *GLA* gene mutations. The TxGNN model predicts it may be effective for **Hepatoportal Sclerosis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the identical prediction score shared across the top five ranked indications suggests the result may reflect a knowledge-graph clustering artefact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fabry disease (patients with amenable *GLA* mutations) — sourced from the repurposing rationale text; no formal indication record was returned |
| Predicted New Indication | Hepatoportal Sclerosis |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for migalastat is marked as a data gap in this evidence pack. However, the repurposing rationale indicates migalastat's known mechanism is as a pharmacological chaperone for α-galactosidase A (α-Gal A), used exclusively in Fabry disease patients with amenable *GLA* mutations, acting on the lysosomal glycosphingolipid metabolism pathway.

No mechanistic link between this pathway and hepatoportal sclerosis (a vascular/fibrotic liver pathology) has been identified. Notably, the top five ranked predictions for this drug (hepatoportal sclerosis, primitive portal vein thrombosis, hepatopulmonary syndrome, early-onset noncirrhotic portal hypertension, and idiopathic copper-associated cirrhosis) all share the exact same TxGNN score (0.98853...), which strongly suggests these predictions originate from a shared "rare liver disease" node cluster in the graph embedding rather than five independent biological signals. This pattern should be treated as a flag for low confidence, not as corroborating evidence.

Given the absence of a plausible mechanistic rationale and the artefact-like scoring pattern, this prediction should not be interpreted as pharmacologically grounded without further independent validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Migalastat is not currently registered on the ARTG (Australian Register of Therapeutic Goods); no product entries are available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only, no clinical trials or literature), and the identical TxGNN scores across the top five predicted indications indicate a likely graph-clustering artefact rather than a genuine mechanistic signal. Mechanism-of-action and safety data are also incomplete, so this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed original-indication and mechanism-of-action data for migalastat (from DrugBank/PI, not inferred text)
- TFDA/TGA-approved Product Information for warnings, contraindications, and drug interactions
- Independent mechanistic assessment of why an α-Gal A chaperone would affect hepatoportal sclerosis pathology, given the current lack of biological rationale
- Investigation into whether the identical scores across ranks 1–5 reflect a TxGNN embedding artefact before further evidence collection is prioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

