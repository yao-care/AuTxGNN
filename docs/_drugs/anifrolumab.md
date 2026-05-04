---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (Saphnelo) is a fully human monoclonal antibody targeting the type I interferon receptor (IFNAR1), approved internationally for moderate-to-severe systemic lupus erythematosus (SLE), but not yet registered in Australia.
The TxGNN model predicts it may have application in **Diabetic Cataract**, with a prediction score of **98.50%**; however, **no supporting clinical trials or directly relevant literature** were identified.
All 10 top predictions in this evidence pack relate to ophthalmic conditions — all rated **L5** (model prediction only) — and all carry a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe systemic lupus erythematosus (SLE) — approved internationally; not registered in Australia |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.50% (model rank: 14,647) |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly available information, Anifrolumab is a fully human IgG1κ monoclonal antibody that binds to subunit 1 of the type I interferon receptor (IFNAR1), blocking the downstream signalling of all type I interferons. Its proven efficacy is in SLE — a systemic autoimmune condition characterised by pathological type I IFN overactivation — where it reduces disease activity and organ damage.

The proposed mechanistic link to diabetic cataract is indirect at best. The most plausible hypothetical pathway runs as follows: Anifrolumab reduces SLE disease activity → enables tapering of long-term corticosteroid therapy → reduced steroid-induced lens toxicity → lower risk of posterior subcapsular cataract. This is a multi-step, population-level inference rather than a direct pharmacological mechanism. Type I IFN pathway inhibition has no known direct role in lens crystallin metabolism, sorbitol accumulation (the primary biochemical driver of diabetic cataract), or lens epithelial cell protection.

A critical modelling caveat must be noted: while the absolute TxGNN scores appear high (~0.98–0.99), the corresponding model ranks are very elevated — ranging from 14,647 to 17,199 across all 10 predictions. Furthermore, multiple distinct cataract subtypes (ranks 2–6) share identical scores to four decimal places, which is a strong indicator of knowledge graph structural clustering rather than independent biological signal. This pattern suggests systematic artefact in the graph topology for this drug-disease class and substantially reduces confidence in these predictions as genuine repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anifrolumab in any of the 10 predicted ophthalmic indications (diabetic cataract, cortical cataract, diabetic retinopathy, and related cataract subtypes). Searches of ClinicalTrials.gov and the ICTRP registry returned zero results across all indications as of the data cutoff (April 2026).

---

## Literature Evidence

Currently no related literature available for Anifrolumab in the treatment of diabetic cataract.

> **Note on adjacent evidence (Rank 7 — Cortical Cataract):** A narrative review was identified in the broader search:
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/) | 2025 | Narrative Review | *Int J Mol Sci* | Ophthalmological safety monitoring in SLE patients receiving conventional and emerging therapies, including Anifrolumab |
>
> **Important limitation**: This publication discusses ocular adverse event surveillance in the SLE treatment population — it does not provide evidence for using Anifrolumab to treat cataract. Its presence in the search results reflects keyword co-occurrence (SLE + Anifrolumab + ophthalmology) and does not constitute repurposing support.

---

## Australia Market Information

Anifrolumab is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). No TGA-approved products containing Anifrolumab are available in Australia as of April 2026.

| Status | Detail |
|--------|--------|
| ARTG Registration | None |
| TGA Market Status | Not marketed |
| International Approvals | FDA (2021), EMA (2022) — for moderate-to-severe SLE in adults on standard therapy |

Clinicians wishing to access Anifrolumab in Australia may consider the **TGA Special Access Scheme (SAS Category B)** or enquire about participation in relevant clinical trials. The AstraZeneca Saphnelo Product Information should be consulted for full prescribing details.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Anifrolumab is not currently registered in Australia, clinicians should consult the international prescribing information (AstraZeneca Saphnelo PI) and the TGA's clinical evidence review documents for the most current safety profile, which includes considerations relevant to immunosuppression, infection risk (including herpes zoster), and infusion-related reactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Anifrolumab are ophthalmic conditions at evidence level L5, with no supporting clinical trials or directly relevant literature. The mechanistic connection between IFNAR1 blockade and lens pathology is indirect and speculative, and the clustering of near-identical prediction scores across multiple biologically distinct cataract subtypes strongly suggests a knowledge graph structural artefact rather than a genuine biological signal. This candidate does not meet the threshold for further investment at this stage.

**To proceed, the following would be needed:**

- Pre-clinical evidence demonstrating a plausible direct biological mechanism linking type I IFN signalling to lens epithelial cell protection or cataractogenesis
- Hypothesis-generating data connecting IFNAR1 inhibition to diabetic lens pathology (e.g., effects on the sorbitol/polyol pathway, lens oxidative stress, or AGE accumulation)
- Independent technical review to determine whether the identical TxGNN scores across multiple cataract subtypes reflect a knowledge graph topology artefact (e.g., shared disease node parents) rather than genuine model predictions
- If mechanistic plausibility is subsequently established: a formal repurposing hypothesis document and ethics-approved exploratory study protocol with ophthalmological endpoints

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application. Refer to the YMYL disclaimer applicable to all TxGNN outputs.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

