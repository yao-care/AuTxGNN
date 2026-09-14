---
layout: default
title: Zinc Oxide
parent: 僅模型預測 (L5)
nav_order: 733
evidence_level: L5
indication_count: 10
---

# Zinc Oxide
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

# Zinc Oxide: From No Registered Indication to Acne

## One-Sentence Summary

> Zinc oxide (DrugBank DB09321) currently has no ARTG registration in Australia and no original-indication data available in this evidence pack.
> The TxGNN model predicts it may be effective for **Acne**, ranking as the top candidate among 10 indications evaluated.
> Currently **no dedicated clinical trials** but **7 supporting publications** (mostly reviews and preclinical studies) underpin this direction, corresponding to Evidence Level **L3**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack — drug is not currently marketed in Australia |
| Predicted New Indication | Acne (acne vulgaris) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for zinc oxide is not currently available in this evidence pack. However, the repurposing rationale generated alongside the prediction notes that zinc oxide has well-documented antibacterial activity (including inhibition of *Cutibacterium acnes*), anti-inflammatory and sebum-regulating properties, and skin-repair effects. These properties are consistent with its long-standing use as an ingredient in topical dermatological preparations (e.g. calamine lotion, sunscreens, skin protectants), where it has an established long-term topical safety record.

Acne pathophysiology involves excess sebum production, bacterial proliferation, and follicular inflammation — all mechanisms that zinc oxide's known topical actions could plausibly address. This gives the prediction a biologically coherent rationale even in the absence of formal MOA documentation, though the current evidence is limited to reviews and preclinical/in vitro studies rather than dedicated clinical trials in acne patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical (split-face) | Skin Res Technol | Split-face bioinstrumental assessment of a topical care regimen for mild inflammatory catamenial acne in young women; oral contraceptives alone showed limited effect on skin clearing. |
| [29193602](https://pubmed.ncbi.nlm.nih.gov/29193602/) | 2018 | Review | Dermatologic Therapy | Reviews zinc's role (topical and systemic) as an adjunct to standard antibiotic/retinoid acne therapy, with a more favourable adverse-effect profile than conventional treatments. |
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Review | Int J Dermatol | Reviews zinc oxide and titanium dioxide nanoparticles in skincare, including investigational nano-formulations for acne vulgaris and other dermatologic conditions. |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Preclinical (in vivo) | Science Advances | Ultrasound-triggered zinc-porphyrin MOF microneedle patch for transdermal delivery, targeting *C. acnes*-driven inflammatory acne. |
| [29284390](https://pubmed.ncbi.nlm.nih.gov/29284390/) | 2018 | Preclinical (in vitro) | Curr Med Chem | Reviews ultrasonic functionalisation of textiles with nanoparticle (including zinc-based) coatings for antimicrobial wound and acne skin care applications. |
| [41033952](https://pubmed.ncbi.nlm.nih.gov/41033952/) | 2025 | Preclinical (in vitro) | Science Bulletin | ZnO-based piezoelectric heterojunction nanomaterial selectively modulates skin microbiota by responding to *C. acnes* respiratory activity, showing antibacterial efficacy in vitro. |
| [31322532](https://pubmed.ncbi.nlm.nih.gov/31322532/) | 2019 | Formulation Development | Georgian Med News | Development of powder cosmetic/cosmeceutical formulations, including zinc-based ingredients, for daily acne-prone skin care. |

---

## Safety Considerations

This drug is not currently registered in Australia, so no TGA-approved Product Information is available for reference. No drug interaction records were found in the source queried. Formal safety, warning, and contraindication data need to be sourced from overseas regulatory filings or published literature before clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zinc oxide's known antibacterial, anti-inflammatory, and sebum-regulating properties provide a biologically coherent rationale for acne, supported by multiple reviews and preclinical studies — but no dedicated clinical trials have tested zinc oxide specifically for acne treatment, so the evidence level remains L3 (observational/review-level) rather than trial-confirmed.

**To proceed, the following is needed:**
- TGA/PI safety information — this is currently a **blocking data gap** (DG001), preventing formal safety pre-assessment (S1)
- Confirmed mechanism-of-action documentation (DG002)
- A dedicated clinical trial (RCT) directly evaluating zinc oxide for acne
- Formulation and route-compatibility assessment (topical formulation and dosing not yet defined in this evidence pack)

**Note on other predicted indications:** Ranks 2–9 (anorectal stricture, anal polyp, papillary conjunctivitis, postinfectious vasculitis, post-bacterial disorder, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome, post-infectious syndrome) currently have **no meaningful supporting evidence** — either no trials/literature at all, or retrieved trials/literature that are mechanistically unrelated to zinc oxide (KG mismatches). These are recommended **Hold**. Rank 10 (otitis externa) shows an early antifungal mechanistic signal (L4) from a single veterinary in vitro study and is marked **Research Question**, warranting monitoring but not action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

