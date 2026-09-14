---
layout: default
title: Tafamidis
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloid Cardiomyopathy to Primary Release Disorder of Platelets

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabilizer whose established mechanism and treated condition — transthyretin amyloid cardiomyopathy (ATTR-CM) — appear only in this evidence pack's supporting literature, not in its structured original-indication data (which is empty).
The TxGNN model's top-ranked prediction for this drug is **Primary Release Disorder of Platelets**, with a raw score of **89.27%**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known pharmacological pathway connecting TTR stabilization to platelet-release function.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured data; supporting literature in this pack repeatedly identifies transthyretin amyloid cardiomyopathy (ATTR-CM) as the drug's established use |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form for this drug. Based on the evidence pack's own annotations, tafamidis is understood to act as a transthyretin (TTR) stabilizer — a mechanism supported by extensive literature in this pack describing its use in transthyretin amyloid cardiomyopathy (e.g., PMID 30145929, *NEJM*, "Tafamidis Treatment for Patients with Transthyretin Amyloid Cardiomyopathy").

For the top-ranked prediction evaluated here — Primary Release Disorder of Platelets — the model's own rationale explicitly states there is **no known pharmacological pathway** linking TTR stabilization to platelet-release function, and that the score reflects knowledge-graph embedding proximity only, without any literature or clinical trial corroboration. This prediction should be treated as a hypothesis-generation artefact rather than a mechanistically grounded lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries exist for tafamidis — it is not currently marketed in Australia (0 licences on file), so no product-specific dosage form or approved-indication text is available locally.

## Safety Considerations

No Australian Product Information (PI) exists for tafamidis, as it is not currently registered on the ARTG. Safety warnings, contraindications, and drug-drug interaction data were also not found in the queried sources (DrugBank/TFDA/DDI queries all returned no result — see data gaps DG001, DG002). Prescribers should consult overseas regulatory PI (e.g., FDA/EMA) directly rather than relying on this evidence pack for safety guidance.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Primary Release Disorder of Platelets) is driven purely by knowledge-graph proximity — it has zero clinical trial or literature support, and the model's own rationale confirms no plausible mechanistic link to TTR stabilization. Combined with tafamidis having no Australian market presence, there is no basis to advance this specific indication.

**To proceed, the following is needed:**
- TFDA/TGA-sourced product warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation (High-severity data gap, DG002)
- Independent biological validation before any further investment in the platelet-disorder hypothesis
- For a more actionable direction, note that a lower-ranked candidate in this same evidence pack — **primary amyloidosis** (rank 5, 17 clinical trials, 20 publications, including Phase 3/4 ATTR-CM trials) — carries substantially stronger evidence and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

