---
layout: default
title: Potassium Permanganate
parent: 僅模型預測 (L5)
nav_order: 549
evidence_level: L5
indication_count: 10
---

# Potassium Permanganate
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

# Potassium Permanganate: Original Indication Undocumented — Assessment of Predicted New Indications

## One-Sentence Summary

Potassium permanganate (DrugBank DB13831) has no original indication or mechanism-of-action data available in the current evidence pack, and the drug is not marketed in Australia (0 ARTG entries). TxGNN's model predicts 10 candidate indications, the highest-ranked being **Benign Prostatic Hyperplasia** (97.66% prediction score), but the drug's own repurposing rationale flags the supporting literature as keyword coincidence rather than genuine mechanistic evidence — none of the 10 candidates currently clears an evidentiary bar to proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available regulatory data |
| Predicted New Indication | Benign Prostatic Hyperplasia (top-ranked of 10 candidates) |
| TxGNN Prediction Score | 97.66% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for potassium permanganate in this evidence pack, and no original indication is recorded either. Without a documented pharmacological baseline, it is not possible to construct a mechanistic bridge between an existing use and the top predicted indication (Benign Prostatic Hyperplasia).

More importantly, the evidence review for this candidate explicitly concludes the link is **not genuine**: the two supporting PubMed articles concern prostatic corpora amylacea and seminal vesicle amyloidosis, topics unrelated to potassium permanganate's pharmacology or to BPH treatment. The reviewer's own assessment characterises this as a keyword coincidence (both articles happen to reference prostate pathology) rather than a real repurposing signal.

This pattern repeats across the other nine candidates in the pack — none has a coherent mechanistic rationale, and one candidate (osteoarthritis, rank 4) has literature that runs in the *opposite* direction: a 1979 study used potassium permanganate to *induce* a crystal-deposition disease model, which would argue against, not for, therapeutic use in osteoarthritis.

---

## Predicted Indications — Full Candidate Summary

Given that all 10 TxGNN-predicted candidates carry weak or contradictory evidence, the full ranked list is provided for transparency rather than focusing on the top candidate alone:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 1 | Benign prostatic hyperplasia | 97.66% | L5 | Hold | Literature is keyword coincidence, not mechanistic |
| 2 | Alopecia | 97.17% | L5 | Hold | No literature or trials |
| 3 | Congestive heart failure | 96.86% | L5 | Hold | 5 literature hits, all unrelated topics |
| 4 | Osteoarthritis | 96.71% | L4 | Hold | Evidence points opposite direction (disease-induction model, not treatment) |
| 5 | Hypotrichosis simplex of the scalp | 96.62% | L5 | Hold | No literature or trials; rare genetic disease |
| 6 | Congenital hypotrichosis milia | 96.48% | L5 | Hold | No literature or trials; rare genetic disease |
| 7 | Osteoarthritis susceptibility | 96.27% | L5 | Hold | No literature or trials |
| 8 | Acute pulmonary heart disease | 96.13% | L5 | Hold | No literature or trials |
| 9 | Pulmonary hypertension | 95.99% | L5 | Hold | 2 literature hits, unrelated topics |
| 10 | Diffuse alopecia areata | 95.87% | L5 | Hold | No literature or trials |

---

## Clinical Trial Evidence (Rank 1: Benign Prostatic Hyperplasia)

Currently no related clinical trials registered.

---

## Literature Evidence (Rank 1: Benign Prostatic Hyperplasia)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1385482](https://pubmed.ncbi.nlm.nih.gov/1385482/) | 1992 | Case study/Pathology | Journal of Clinical Pathology | Immunohistological study of amyloid in prostatic corpora amylacea; not a treatment or KMnO4-related study |
| [9431316](https://pubmed.ncbi.nlm.nih.gov/9431316/) | 1997 | Case report | Archives of Pathology & Laboratory Medicine | Localized seminal vesicle amyloidosis in hormonally treated prostate carcinoma patients; not a treatment or KMnO4-related study |

Neither article discusses potassium permanganate or a treatment mechanism for BPH — both were captured on prostate-related keyword overlap only.

---

## Australia Market Information

No ARTG entries currently found. Potassium permanganate is not marketed in Australia under this evidence pack's regulatory data (0 licences recorded).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were located for potassium permanganate in the sources queried (DDI database search returned no result).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No original indication, mechanism-of-action, or safety data exists for potassium permanganate in this evidence pack, and none of the 10 TxGNN-predicted candidates is supported by genuine clinical or mechanistic evidence — the top candidate's literature was assessed by the review itself as coincidental keyword matches, and one candidate's evidence points against therapeutic benefit.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (labelled warnings, contraindications) — currently a Blocking data gap
- Verified mechanism of action from DrugBank or primary literature
- A documented original/established indication for baseline comparison
- Real clinical trial or high-quality literature evidence specific to any candidate indication before advancing past S0/S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

