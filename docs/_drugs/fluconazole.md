---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Fluconazole
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

# Fluconazole: From Antifungal Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Fluconazole is a triazole antifungal, though the evidence pack contains no jurisdiction-specific approved indication text (drug is not currently listed on the ARTG).
> The TxGNN model's top-ranked prediction is **Punctate Epithelial Keratoconjunctivitis**,
> but this ranking is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (Fluconazole is a triazole antifungal in general use; no jurisdiction-specific approved indication text was returned) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on well-established clinical knowledge, fluconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14-α-demethylase), blocking ergosterol synthesis in the fungal cell membrane. It is used systemically for candidiasis, cryptococcal infections and other fungal diseases.

For this specific prediction, however, the model's own rationale states that punctate epithelial keratoconjunctivitis is most commonly caused by viral infection (e.g. adenovirus) or allergic mechanisms — conditions that have no established connection to fluconazole's antifungal, ergosterol-targeting mechanism. No clinical or literature evidence currently supports this association.

In other words, this is a high-scoring TxGNN prediction that lacks both mechanistic plausibility and any corroborating real-world evidence at this time — the score alone should not be read as clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Fluconazole is not currently marketed in Australia under this dataset (0 ARTG entries recorded; market status: Not Marketed). No product-level information is available to summarise.

---

## Safety Considerations

Key warnings, contraindications and drug-interaction data are all marked as gaps in this evidence pack. Notably, the underlying data-gap log flags the missing TFDA/local product-information warnings and contraindications as a **Blocking** gap, meaning this candidate cannot yet proceed to an initial safety assessment (S1 stage). As fluconazole is not currently registered on the ARTG in this dataset, no TGA-approved Product Information is available either — safety information should be sourced from an alternative jurisdiction's approved product information (e.g. FDA label) before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (punctate epithelial keratoconjunctivitis) has a high model score but zero supporting clinical trials or literature, and the model's own mechanistic rationale identifies no plausible link to fluconazole's antifungal activity. This is Evidence Level L5 — a model prediction with no corroborating study evidence — and does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/local product information (warnings and contraindications) — currently a Blocking data gap preventing entry into initial safety screening (S1)
- Detailed mechanism-of-action data confirming or refuting any biological plausibility for this indication
- Preclinical or in vitro evidence specifically linking fluconazole to punctate epithelial keratoconjunctivitis, given the model's own rationale suggests none currently exists

**Note on other candidates in this evidence pack:** Among the 10 predictions supplied, *pneumocystosis* (rank 7, score 97.8%) has substantially more real-world evidence (7 clinical trials, 20 publications, Evidence Level L3) than the top-scored candidate above, and is flagged as a "Research Question" rather than "Hold." However, its own mechanistic rationale is also weak — *Pneumocystis jirovecii* lacks the ergosterol target of triazoles, so most of the supporting studies reflect fluconazole's use for co-occurring fungal infections in the same immunocompromised populations (HIV/transplant), not direct anti-Pneumocystis activity. If this evaluation is intended to identify the most promising repurposing candidate for fluconazole overall (rather than strictly the top TxGNN score), pneumocystosis may warrant separate consideration — but neither candidate is currently ready to advance past Hold/Research Question status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

