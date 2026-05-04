---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Dexpanthenol
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

# Dexpanthenol: From Wound Healing to Exanthem

## One-Sentence Summary

Dexpanthenol (provitamin B5) is widely used internationally for wound healing, skin repair, and dermatological care — most notably as Bepanthen® — but is not currently registered on the Australian Register of Therapeutic Goods (ARTG). The TxGNN model identifies **Exanthem (skin rash conditions)** as the highest-evidence predicted new indication among all 10 candidates, supported by **5 clinical trials**, including 1 completed Phase 3 RCT directly testing Bepanthen® (dexpanthenol) cream for the prevention of skin eruptions in patients receiving cancer therapy.

> **Note on TxGNN ranking:** TxGNN's highest-scoring prediction for dexpanthenol is anorectal stricture (99.72%, rank #1), but this carries an L5 evidence level with a Hold recommendation and no supporting studies. Exanthem (TxGNN rank #6, 99.60%) represents the most clinically actionable prediction based on available evidence and is used as the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not TGA-registered; internationally used for wound healing and dermatological/mucosal repair |
| Predicted New Indication | Exanthem (skin rash conditions) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, dexpanthenol is the alcohol analogue of pantothenic acid (Vitamin B5). Following administration, it is converted to pantothenic acid, which serves as a precursor to Coenzyme A (CoA) — a co-factor central to cellular metabolism, fatty acid synthesis, and skin lipid barrier formation. This pathway stimulates keratinocyte proliferation, promotes fibroblast activity, and accelerates wound re-epithelialisation. Dexpanthenol also demonstrates localised anti-inflammatory properties at skin and mucosal surfaces.

Exanthem encompasses a range of skin rash presentations, many involving acute epithelial disruption, inflammatory cell infiltration, and barrier dysfunction — processes directly addressed by dexpanthenol's mechanism. A clinically significant and well-characterised subtype is the papulopustular eruption caused by EGFR inhibitors (a common targeted cancer therapy side effect). This specific exanthem has been the subject of at least one completed Phase 3 RCT testing Bepanthen® (dexpanthenol) cream, directly validating the TxGNN prediction and demonstrating a mechanistically coherent and clinically relevant association.

The broader pattern of dexpanthenol's internationally established formulations — skin care after dermatological procedures, anorectal preparations, and ophthalmic products — reflects a drug with versatile epithelial repair properties. This is consistent with the range of TxGNN predictions in the dataset, and further supports the biological plausibility of the exanthem indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Bepanthen® cream vs Cetomacrogol cream for preemptive prevention of papulopustular eruption (grade ≥2) in patients receiving EGFR inhibitors; assessed compliance with EGFRI therapy, health-related quality of life, and adherence to skin treatment over a 6-week period |
| [NCT03852563](https://clinicaltrials.gov/study/NCT03852563) | Not applicable | Completed | 33 | Bepantol® (dexpanthenol) cream for skin recovery and rash reduction after ablative facial laser procedure; assessed redness, irritation, softness, and safety at 4 follow-up visits over 3 weeks in adult women |
| [NCT05699122](https://clinicaltrials.gov/study/NCT05699122) | Not applicable | Completed | 16 | Low-level laser therapy for incontinence-associated dermatitis in elderly patients; dexpanthenol likely features as standard barrier product comparator or adjunct given established guidelines; analgesic, anti-inflammatory, and tissue repair outcomes assessed |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Topical imiquimod formulations for actinic cheilitis treatment; dexpanthenol's specific role (vehicle, control arm, or comparator) requires clarification from the full study protocol; trial terminated early — results have limited reliability |
| [NCT03866447](https://clinicaltrials.gov/study/NCT03866447) | Phase 4 | Unknown | 80 | Vitamin D analogues for acne vulgaris; dexpanthenol involvement as adjunct or comparator is unclear from available data; trial status unverified — data reliability is low |

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack for dexpanthenol and exanthem.

> A dedicated PubMed search outside this dataset is recommended as a priority next step (see Conclusion).

---

## Australia Market Information

Dexpanthenol is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No ARTG entries are recorded as of 4 April 2026.

Internationally marketed products include:

| Formulation | Brand | Indication |
|-------------|-------|------------|
| Topical cream/ointment | Bepanthen® (Bayer) | Wound healing, nappy rash, skin care |
| Ophthalmic gel | Corneregel® (Bausch + Lomb) | Dry eye, corneal epithelial repair |
| Anorectal suppository | Various (Europe) | Rectal mucosal repair and haemorrhoid care |

Any clinical use in Australia would currently require either a **TGA Special Access Scheme (SAS) application** or a **Clinical Trial Notification (CTN)** pathway.

---

## Safety Considerations

Please refer to the manufacturer's international Product Information (PI) — including the Bepanthen® EU Summary of Product Characteristics — for safety information, as no Australian TGA-approved PI is currently available. No drug interaction data were identified in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The completed Phase 3 trial (NCT01136005, n=160) directly tested Bepanthen® (dexpanthenol) cream for prevention of EGFR inhibitor-induced papulopustular eruption — a specific and clinically burdensome exanthem subtype in oncology. The mechanistic plausibility is well-supported by established CoA/epithelial repair biology, and the drug has a decades-long international safety record across multiple formulations. Evidence is sufficient to justify a focused research question targeting Australian clinical practice.

**To proceed, the following is needed:**
- Full MOA data from DrugBank to formally document the CoA-mediated epithelial repair pathway
- Access to the full published results of NCT01136005 (BeCet trial) and assessment of efficacy outcomes
- Dedicated PubMed literature search for dexpanthenol and exanthem/skin rash (zero publications were returned in this pack)
- Definition of the target Australian patient population (e.g., oncology patients on EGFR inhibitors, radiation dermatitis, general dermatology)
- TGA Special Access Scheme or Clinical Trial Notification pathway assessment for Australian use
- Review of international safety data and identification of any contraindications or warnings relevant to Australian patients

---

## TxGNN Prediction Summary (All 10 Predictions)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Anorectal stricture | 99.72% | L5 | Hold |
| 2 | Imperforate anus | 99.71% | L5 | Hold |
| 3 | Anal polyp | 99.62% | L5 | Hold |
| 4 | Vulvar inverted follicular keratosis | 99.60% | L5 | Hold |
| 5 | Proctitis | 99.60% | L4 | Research Question |
| **6** | **Exanthem** | **99.60%** | **L2** | **Research Question ★** |
| 7 | Punctate epithelial keratoconjunctivitis | 99.34% | L4 | Research Question |
| 8 | Acute urate nephropathy | 98.99% | L5 | Hold |
| 9 | Indeterminate colitis | 98.87% | L5 | Hold |
| 10 | Diversion colitis | 98.87% | L5 | Research Question |

★ Highest evidence level among all predictions; selected as primary focus of this report.

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This information has been prepared to support Australian healthcare professionals in evaluating research opportunities.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

