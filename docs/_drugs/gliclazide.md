---
layout: default
title: Gliclazide
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Gliclazide
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

# Gliclazide: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Gliclazide is a sulfonylurea antidiabetic agent traditionally used to manage type 2 diabetes mellitus. The TxGNN model predicts a possible new application in **Classic Stiff Person Syndrome**, but this prediction is currently unsupported by any clinical trials or published literature, and the evidence pack's own mechanistic review flags it as likely a knowledge-graph artefact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (regulatory data absent); gliclazide is internationally recognised as a sulfonylurea used for type 2 diabetes mellitus |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for gliclazide is not available in this evidence pack. Based on general pharmacological knowledge, gliclazide belongs to the sulfonylurea class of oral hypoglycaemics: it binds the SUR1 subunit of the pancreatic β-cell KATP channel, triggering depolarisation and insulin release. Its efficacy in type 2 diabetes is well established.

Classic Stiff Person Syndrome, however, is an autoimmune neurological disorder driven by anti-GAD65 antibodies and impaired GABAergic neurotransmission — a mechanism with no established link to sulfonylurea-mediated insulin secretion. The evidence pack's own repurposing rationale for this candidate states that the high TxGNN score likely reflects structural proximity within the knowledge graph (e.g. shared metabolic/endocrine network neighbours) rather than a true pharmacological relationship, and is not corroborated by any clinical trial or literature evidence.

Given this, the mechanistic case for this specific candidate is weak. Two lower-ranked candidates in the same evidence pack — thiamine-responsive dysfunction syndrome (rank 3) and pancreatic agenesis (rank 5) — have somewhat more biological plausibility, since both involve KATP-channel-related β-cell dysfunction (analogous to sulfonylurea-responsive neonatal diabetes), and are scored "Research Question" rather than "Hold." These may warrant closer literature monitoring even though this report focuses on the top-ranked candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

No ARTG entries are recorded for gliclazide in this evidence pack; market status is listed as not marketed. This should be verified directly against the TGA ARTG database, as the underlying regulatory data source (DG001, blocking gap) has not yet been retrieved.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate scores highly on TxGNN (97.96%) but has zero supporting clinical trials or literature, an evidence level of L5, and the evidence pack's own mechanistic review considers the biological link implausible. In addition, a Blocking data gap on TGA Product Information warnings and contraindications (DG001) means a safety pre-screen cannot yet be completed.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI), including warnings, contraindications, and drug interactions (resolves DG001)
- Confirmation of gliclazide's actual ARTG market status in Australia
- Detailed mechanism of action data (resolves DG002)
- Any preclinical or mechanistic studies specifically linking sulfonylureas to GABAergic/autoimmune neurological pathways, if this candidate is to be pursued further
- Consider redirecting research attention to the mechanistically stronger candidates in this evidence pack (thiamine-responsive dysfunction syndrome, pancreatic agenesis) for literature monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

