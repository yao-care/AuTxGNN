---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Prednisone is a synthetic glucocorticoid with broad anti-inflammatory and immunosuppressive activity, though the specific original indication approved for this product is not documented in the current evidence pack. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **32 clinical trial records** and **20 publications** retrieved during evidence collection (only a subset directly test prednisone in this indication — see Clinical Trial Evidence below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no TFDA/ARTG-sourced indication text available; original_indications field is empty) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, prednisone is a synthetic glucocorticoid that suppresses T-cell activation and inflammatory cytokine release; it has been used for decades across a wide range of inflammatory and autoimmune conditions.

Alopecia areata (AA) is a T-cell-mediated autoimmune disease in which immune cells attack the immune-privileged hair follicle. Prednisone's broad-spectrum suppression of T-cell activation and cytokine release maps directly onto this pathophysiology, which is why systemic corticosteroids — including prednisone — already have a long track record as an established (and, in some regimens, off-label) dermatological treatment for severe AA, rather than representing a wholly novel hypothesis.

This mechanistic plausibility is reinforced by decades of clinical experience: prednisone has been studied both as monotherapy (pulsed or alternate-day dosing) and in combination with steroid-sparing agents such as methotrexate, cyclosporine, and more recently baricitinib, generally to improve response rates in severe or treatment-resistant AA.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | Randomized double-blind trial testing methotrexate alone vs. methotrexate + low-dose prednisone vs. placebo for severe alopecia areata ("grave pelade") — the only trial in the retrieved set that directly tests a prednisone-containing regimen in AA. |

**Note:** The disease-tagged search returned 32 trials in total, but the great majority (Phase 2–4 trials in systemic lupus erythematosus, prostate cancer, lymphoma, etc.) capture prednisone only as an incidental background or combination agent for unrelated conditions — these were graded low relevance ("C") or remain unclassified and are excluded from the table above as they provide no direct evidence for prednisone's use in alopecia areata.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 2-step double-blind RCT comparing methotrexate alone vs. methotrexate + low-dose prednisone in alopecia totalis/universalis, addressing whether adding a corticosteroid improves the historically poor response rate in severe AA. |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Cohort | Archives of Dermatology | Early immunologic study of AA with prednisone treatment; foundational evidence supporting corticosteroid use in this disease. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Cohort | Archives of Dermatology | Follow-up of 18 AA patients on alternate-day prednisone: initial response seen, but long-term benefit was limited and substantial steroid-related side effects (acne, obesity, hypertension) were noted. |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Archives of Dermatology | Review of AA therapies (including corticosteroids) covering efficacy, safety and mechanism; notes study heterogeneity limits direct cross-drug comparison. |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case series | Clinical and Experimental Dermatology | 8-case series: baricitinib + low-dose corticosteroids produced major improvement in very severe AA (SALT ≥95) where either agent alone had previously failed. |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort | Dermatology (Basel) | Methotrexate combined with low-to-moderate dose corticosteroids evaluated for efficacy and safety in severe AA. |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Cohort | Journal of the American Academy of Dermatology | Cyclosporine + low-dose prednisone evaluated clinically and immunopathologically in chronic severe AA. |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Cohort | Annales de Dermatologie et de Venereologie | Once-monthly oral pulse prednisone evaluated for efficacy and safety in the management of AA. |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Case series | International Journal of Dermatology | Severe AA treated with systemic corticosteroids; corticosteroids described as an effective treatment option for severe disease. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Early report of AA (partialis and totalis) treated with cortisone/hydrocortisone analogues, prednisone and prednisolone. |

---

## Australia Market Information

Prednisone is currently **not registered** in the Australian Register of Therapeutic Goods (ARTG) under this evidence pack — 0 licences were found, and market status is recorded as Not Marketed. No product-level ARTG listings are available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were returned for prednisone in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT02037191) and a 2023 JAMA Dermatology RCT directly evaluate low-dose prednisone-containing regimens in severe alopecia areata, supported by decades of cohort and case-series experience — this meets L2 evidence (a single completed Phase 2/3 RCT) rather than the L1 bar of ≥2 completed Phase 3 RCTs. Mechanism-of-action data, TGA-approved safety information, and Australian market/registration status are all currently unavailable, so this indication should not proceed without further data.

**To proceed, the following is needed:**
- TGA/ARTG-approved Product Information (warnings, contraindications, drug interactions) — currently a Blocking data gap (DG001)
- Detailed mechanism of action documentation — High-priority data gap (DG002)
- Confirmation of Australian market/registration status and available routes/formulations for prednisone (route compatibility currently unassessed)
- Ideally, an additional independent Phase 2/3 RCT to raise the evidence level from L2 to L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

