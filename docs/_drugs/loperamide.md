---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: Predicted Signal for Acute Contagious Conjunctivitis (Low Confidence)

## One-Sentence Summary

> Loperamide's original approved indication is not documented in this evidence pack (the product is not currently registered/marketed under the reviewed regulatory data). The TxGNN model's top-ranked prediction for this drug is **Acute Contagious Conjunctivitis**, but this signal is supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags it as a likely model artefact rather than a genuine repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license/indication text on file) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Loperamide is not available in this evidence pack, so the pharmacological rationale below is drawn directly from the model's own per-candidate assessment rather than external MOA sources.

For the top-ranked candidate (Acute Contagious Conjunctivitis), no mechanistic link could be established: Loperamide's known pharmacology as a peripherally acting agent affecting gut motility has no plausible pathway to ocular surface infection or inflammation. The evidence pack's own rationale states this score is most likely driven by proximity of the "conjunctivitis" disease node cluster within the knowledge graph embedding space, rather than a genuine biological signal — in other words, a probable model false positive. This is reinforced by the fact that ranks 3, 5–9 in this evidence pack are *all* conjunctivitis-family diagnoses clustered at nearly identical scores (0.9962–0.9987), a pattern consistent with embedding-driven noise rather than independent evidence-backed signals.

Of the ten candidates supplied, the one with the strongest (though still limited) supporting evidence is **amebic dysentery** (rank 2), discussed below — but its literature evidence points toward a safety **contraindication**, not a therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Loperamide has no ARTG entries on file and is recorded as not currently marketed under the regulatory data reviewed (0 licenses).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

**Important context from this evidence pack (not part of the formal safety data, but clinically relevant):** literature associated with the amebic dysentery candidate (rank 2, PMID [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/)) describes a case of fulminant amoebic colitis/toxic megacolon following loperamide use, consistent with the known class risk that anti-motility agents can worsen outcomes in invasive enteric infections. This is a caution against use, not supporting evidence for a new indication.

---

## Other Candidate Indications Considered

For transparency, all ten TxGNN-predicted candidates in this evidence pack are summarised below. None reach a "Go" or unguarded "Proceed" recommendation.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Acute contagious conjunctivitis | 99.97% | L5 | Hold | Likely embedding artefact |
| 2 | Amebic dysentery | 99.95% | L4 | Hold | Literature suggests harm risk (toxic megacolon), not benefit |
| 3 | Conjunctivitis | 99.87% | L5 | Hold | Trials found are for azithromycin/trachoma, unrelated to loperamide |
| 4 | Gastroduodenitis | 99.77% | L3 | Research Question | Single 1986 cohort study; symptomatic-relief hypothesis only |
| 5 | Pseudomembranous conjunctivitis | 99.65% | L5 | Hold | Conjunctivitis-cluster noise |
| 6 | Parasitic conjunctivitis | 99.65% | L5 | Hold | Conjunctivitis-cluster noise |
| 7 | Conjunctival folliculosis | 99.65% | L5 | Hold | Conjunctivitis-cluster noise |
| 8 | Serous conjunctivitis (except viral) | 99.65% | L5 | Hold | Conjunctivitis-cluster noise |
| 9 | Chronic follicular conjunctivitis | 99.65% | L5 | Hold | Conjunctivitis-cluster noise |
| 10 | Angelucci syndrome | 99.63% | L5 | Hold | No physiological pathway overlap |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No candidate in this evidence pack has evidence beyond a single low-tier literature source. The top-ranked prediction is most plausibly a knowledge-graph embedding artefact, and the best-evidenced candidate (amebic dysentery) points toward a safety risk rather than therapeutic benefit. There is no basis to advance this drug-indication pairing.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent product information (warnings, contraindications) — currently a blocking data gap for any safety assessment
- Confirmed mechanism of action data
- Independent mechanistic or preclinical evidence specifically linking Loperamide to an ocular or infectious-disease pathway, before any further trial/literature search is warranted
- If pursuing the gastroduodenitis (rank 4) lead instead, a targeted literature search beyond the single 1986 cohort study to assess reproducibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

