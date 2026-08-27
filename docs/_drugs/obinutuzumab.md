---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Obinutuzumab
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Pregerminal Center Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma

## One-Sentence Summary

Obinutuzumab is a second-generation anti-CD20 monoclonal antibody already used internationally for chronic lymphocytic leukaemia (CLL), although it is **not currently registered in Australia**. The TxGNN model's top-ranked prediction is for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma** (a molecular subtype of CLL/SLL), but this evidence pack currently holds **0 clinical trials** and **0 publications** for that specific subtype. The strongest independently-supported candidates in this evidence pack are instead **follicular lymphoma** (Phase 3 RCT-level, L1) and **mantle cell lymphoma** (L2) — see the overview table below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) — a globally recognised approved indication for obinutuzumab; not captured in the Australian regulatory data in this evidence pack, as the drug is not yet registered here |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

## Other Predicted Indications in This Evidence Pack

This evidence pack scored 10 candidate indications for obinutuzumab. Evidence quality varies sharply, so this table is included to guide which candidates merit closer attention:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pregerminal center CLL/SLL | 99.21% | L4 | S1 | Research Question |
| 2 | CLL/SLL with IGHV somatic hypermutation | 99.21% | L4 | S1 | Research Question |
| 3 | **Follicular lymphoma** | 99.18% | **L1** | S3 | **Proceed with Guardrails** |
| 4 | **Mantle cell lymphoma** | 98.75% | **L2** | S3 | **Proceed with Guardrails** |
| 5 | Metastatic neoplasm | 98.51% | L4 | S0 | Hold |
| 6 | Malignant spiradenoma | 98.47% | L5 | S0 | Hold |
| 7 | Neoplasm of mature B-cells | 98.08% | L3 | S2 | Research Question |
| 8 | Small intestinal Burkitt lymphoma | 97.84% | L5 | S0 | Hold |
| 9 | Langerhans cell histiocytosis | 97.81% | L5 | S0 | Hold |
| 10 | Thyroid gland MALT lymphoma | 97.76% | L5 | S0 | Hold |

Ranks 1–2 and 5–6 and 8–10 either have no supporting trials/literature in this dataset or, in the case of malignant spiradenoma and Langerhans cell histiocytosis, target cell types that do not typically express CD20 — these are likely knowledge-graph embedding artefacts rather than genuine repurposing signals.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for obinutuzumab was not returned from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic rationale text included with the predictions, obinutuzumab is described as a second-generation anti-CD20 monoclonal antibody, and its efficacy in CLL is well established internationally (e.g. the CLL11 trial). Mechanistically, anti-CD20 activity is applicable across CD20-positive B-cell malignancies, which is why the model surfaces several lymphoma/leukaemia subtypes as high-scoring candidates.

The rank-1 and rank-2 predictions — "pregerminal center CLL/SLL" and "CLL/SLL with IGHV somatic hypermutation" — are not truly novel indications; they are molecular/prognostic subclassifications of CLL/SLL, a disease obinutuzumab is already approved for in most markets. The evidence pack's own annotation for these predictions states this is likely a data-collection gap (the trial/literature pipeline was queried against the narrow subtype label rather than the parent disease) rather than a true absence of supporting evidence.

By contrast, follicular lymphoma (rank 3) and mantle cell lymphoma (rank 4) are supported by direct, disease-specific clinical trial and literature evidence within this dataset, including completed Phase 3 randomised trials. These represent the more actionable near-term opportunities from this prediction set.

## Clinical Trial Evidence

Currently no related clinical trials registered for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma** in this evidence pack.

*(Note: substantial trial evidence exists for follicular lymphoma and mantle cell lymphoma — see the overview table above. A dedicated evaluation of either of those indications would surface that evidence directly.)*

## Literature Evidence

Currently no related literature available for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma** in this evidence pack.

## Australia Market Information

Obinutuzumab has **no ARTG entries** and is **not currently marketed** in Australia according to this evidence pack (0 licenses recorded).

## Cytotoxicity

Obinutuzumab is an antineoplastic agent (anti-CD20 monoclonal antibody used in B-cell malignancies).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody) |

Detailed myelosuppression risk, emetogenicity classification, monitoring requirements, and handling precautions are not available in this evidence pack. Please refer to the TGA-approved Product Information (PI) for this information.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a Blocking-severity data gap pending TGA/TFDA product information retrieval).

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The rank-1 predicted indication has no independent clinical trial or literature evidence in this dataset, and mechanistically overlaps with obinutuzumab's already-known original indication (CLL) rather than representing a genuinely new use. It is not ready for a repurposing decision as framed. Two other candidates in this same evidence pack — follicular lymphoma and mantle cell lymphoma — are substantially better supported (L1 and L2 respectively) and warrant separate evaluation as "Proceed with Guardrails" candidates.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data from DrugBank (currently a High-severity gap)
- TGA Product Information / warnings, contraindications, and interaction data (currently a Blocking-severity gap)
- Re-run trial/literature collection against the parent CLL/SLL disease term (not just the narrow molecular-subtype label) to close the apparent data-collection gap for rank 1–2
- Confirmation of any pathway toward Australian (TGA/ARTG) registration, since obinutuzumab is not currently marketed here
- A separate, dedicated evaluation of the follicular lymphoma and mantle cell lymphoma predictions, which carry materially stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

