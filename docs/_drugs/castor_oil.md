---
layout: default
title: Castor Oil
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Castor Oil
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

# Castor Oil: From Traditional Topical Use to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Castor oil is a plant-derived oil with a long history of traditional use for topical hair and skin care as well as a laxative agent, carrying no currently registered therapeutic indications in Australia.
The TxGNN model predicts it may have activity in **hypotrichosis simplex of the scalp** (prediction score 98.06%), though **no clinical trials and no direct publications** exist to support this specific rare genetic condition.
Across the broader predicted hair loss cluster, the more general **alopecia** category (rank 4) has 8 indirect publications, but no castor oil monotherapy RCTs have been conducted for any alopecia subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None (not registered in Australia) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 98.06% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for castor oil. Based on known information, castor oil's principal bioactive component — ricinoleic acid — exerts several biological effects that may theoretically relate to hair follicle biology: (1) EP3 receptor agonism modulates the prostaglandin pathway, potentially extending the anagen (growth) phase of the hair cycle via PGE2-like signalling; (2) indirect 5α-reductase inhibitory effects may attenuate dihydrotestosterone-mediated follicular miniaturisation; and (3) antimicrobial and anti-inflammatory properties may improve the scalp microenvironment. These properties provide a biologically plausible — but unproven — rationale for hair-related indications as a broad class.

Hypotrichosis simplex of the scalp, however, is a **monogenic hereditary condition** caused by loss-of-function mutations in LPAR6 or LIPH genes, which encode lysophosphatidic acid receptor-6 and lipase H respectively. These mutations impair lipid signalling required for normal hair follicle function at the genetic level. Castor oil has no known mechanism capable of correcting this underlying genetic defect, and the elevated TxGNN score is most likely an artefact of the model generalising across the broad "alopecia" disease node cluster in the knowledge graph, rather than reflecting a true drug–disease relationship.

Among all predicted indications in this evidence pack, **alopecia (rank 4, score 97.65%)** is the most scientifically plausible and evidence-supported target. Ethnomedicinal use in the African diaspora is well-documented, and two narrative reviews (PMIDs [37017321](https://pubmed.ncbi.nlm.nih.gov/37017321/), [33178378](https://pubmed.ncbi.nlm.nih.gov/33178378/)) provide indirect support for castor oil's role in hair care. Nevertheless, no standalone RCT has tested castor oil as a monotherapy for any alopecia subtype, and the overall evidence base remains insufficient to advance beyond a preliminary research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypotrichosis simplex of the scalp.

---

## Literature Evidence

Currently no related literature available for hypotrichosis simplex of the scalp.

---

## Safety Considerations

Please refer to available Product Information and standard pharmaceutical references for safety information. As castor oil is not currently listed on the Australian Register of Therapeutic Goods (ARTG), no TGA-approved Product Information is available. Clinicians should consult international pharmacopoeia references (e.g., British Pharmacopoeia, USP) and pharmacological databases for comprehensive safety guidance prior to any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hypotrichosis simplex of the scalp is a rare monogenic disorder for which castor oil has no plausible mechanistic rationale and zero clinical or preclinical evidence to support use; the high TxGNN prediction score is considered an artefact of knowledge graph generalisation across the broader alopecia disease node cluster.

**To proceed, the following is needed:**

- Formally evaluate the more plausible **alopecia** indication (rank 4, decision stage S1 — Research Question) first; a controlled pilot study of topical castor oil for androgenetic or cicatricial alopecia would be an appropriate starting point before pursuing rarer subtypes
- Obtain full mechanism of action characterisation for ricinoleic acid, particularly its effects on the prostaglandin–hair cycle axis (EP3 agonism, PGE2/PGD2 balance) and 5α-reductase inhibitory activity
- Document the topical safety profile through existing GRAS (Generally Recognised As Safe) regulatory status and published dermatological use literature; any formal TGA registration would require a complete safety and efficacy dossier
- For hypotrichosis simplex of the scalp specifically: gene-directed therapies targeting LPAR6/LIPH pathways represent the scientifically appropriate research direction — castor oil is not suitable for this genetic aetiology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

