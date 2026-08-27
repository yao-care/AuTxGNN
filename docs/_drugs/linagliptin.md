---
layout: default
title: Linagliptin
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Linagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor; the evidence pack's own literature references its use in type 2 diabetes combination therapy, though no confirmed original-indication record exists because the drug is not currently marketed in Australia. The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale finds no biological link between DPP-4 inhibition and this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from literature in this pack; not a confirmed Australian regulatory indication) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 94.90% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Linagliptin is not available in this evidence pack. Based on the literature captured elsewhere in the pack (relating to a different candidate indication), Linagliptin belongs to the DPP-4 inhibitor class and is used, often in combination, for glycaemic control in type 2 diabetes.

Opsismodysplasia is a rare skeletal dysplasia primarily caused by *INPPL1* mutations (with *SGPL1* also implicated in some cases), affecting endochondral bone formation. There is no established biological pathway connecting DPP-4 inhibition or incretin signalling to skeletal growth-plate development.

The evidence pack's own repurposing rationale is explicit on this point: the high TxGNN score for this candidate appears to be driven by embedding similarity in the knowledge graph rather than any identifiable mechanistic basis. This should be read as a hypothesis-generating signal only, not a mechanistically grounded lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) were returned for Linagliptin in this evidence pack. As Linagliptin is not currently marketed in Australia, no TGA-approved Product Information exists locally — safety assessment would need to draw on overseas regulatory labelling (e.g., FDA, EMA) as an interim source pending formal TGA evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but is unsupported by any clinical trial or literature evidence specific to opsismodysplasia, and the model's own rationale identifies no plausible mechanistic link. Combined with the drug's unmarketed status in Australia and missing MOA/safety data, this candidate does not meet the threshold to progress beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product label (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action data from DrugBank or primary literature
- Preclinical or case-level evidence specifically linking DPP-4 inhibition to opsismodysplasia pathophysiology, given none currently exists
- Re-evaluation against lower-ranked candidates in this pack (e.g. pancreatic agenesis, rank 8) which at least have literature returned, though not disease-specific, and were also scored Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

