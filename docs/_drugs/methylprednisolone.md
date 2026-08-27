---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a synthetic glucocorticoid; this Evidence Pack does not contain a documented original indication or Australian ARTG entry for the drug, so no local approved use can be cited. The TxGNN model predicts it may be effective for **Alopecia Areata**, and the evidence pack returned **18 clinical trial records** and **20 publications** on this drug–disease pair — though only a subset (mostly cohort studies, one systematic review, and one Phase 4 trial) directly involve methylprednisolone in alopecia areata; several of the trial hits are unrelated studies (e.g., systemic lupus erythematosus drug trials) surfaced by broad disease-term matching rather than genuine evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no ARTG-approved indication text available; drug not currently marketed in Australia) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methylprednisolone was not available in this evidence pack (flagged as a High-severity data gap). Based on the drug's known pharmacological identity, methylprednisolone is a systemic glucocorticoid with anti-inflammatory and immunosuppressive activity.

According to the evidence pack's own repurposing rationale: IV or oral methylprednisolone pulse therapy is thought to act by suppressing the autoimmune inflammatory response around the hair follicle (T-cell–mediated follicular attack), thereby promoting hair regrowth. This is already an established off-label option in dermatology practice for moderate-to-severe alopecia areata, and the mechanism is supported by multiple directly relevant treatment studies (see Literature Evidence below).

Because alopecia areata is a T-cell-mediated autoimmune disease, the general immunosuppressive mechanism of glucocorticoids provides a plausible pharmacological link, distinguishing this candidate from several lower-ranked, mechanistically speculative predictions in the same evidence pack (e.g., non-inflammatory or purely genetic hair-loss disorders).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone (higher dose, more frequent pulses than standard) evaluated for safety/efficacy in severe therapy-resistant alopecia areata |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared needle-free DERMOJET vs conventional syringe for intralesional corticosteroid injection in alopecia areata; drug not explicitly confirmed as methylprednisolone (relevance grade B) |

**Note:** The evidence pack returned 18 clinical trial records for this drug–disease pair, but most (grade C) are unrelated trials of other drugs in systemic lupus erythematosus, surfaced by disease-term overlap rather than genuine relevance to methylprednisolone in alopecia areata. Only the two trials above were assessed as directly pertinent.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Reviews efficacy, relapse rates, side effects and prognostic factors of corticosteroid pulse therapy in alopecia areata |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Systematic review of cyclosporine with/without systemic corticosteroids in alopecia areata |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Methylprednisolone alone vs methylprednisolone + methotrexate in 26 patients with extensive alopecia areata |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777767/) | 1998 | Open Prospective Cohort | J Am Acad Dermatol | Pulse methylprednisolone therapy in 45 patients with severe alopecia areata |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort/Case Series | Indian J Dermatol Venereol Leprol | IV methylprednisolone pulse therapy in severe alopecia areata |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Cohort/Case Series | Saudi Medical Journal | Oral mega-pulse methylprednisolone for severe therapy-resistant alopecia areata |
| [21592197](https://pubmed.ncbi.nlm.nih.gov/21592197/) | 2011 | Retrospective Cohort | J Dermatology | Prognostic factors for response to methylprednisolone pulse therapy in 70 patients with alopecia areata |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Cohort | Open Access Maced J Med Sci | Methotrexate + mini-pulse methylprednisolone in severe alopecia areata (Vietnamese cohort) |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Cohort/Combination Therapy | J Dermatolog Treat | Combination cyclosporine and methylprednisolone in severe alopecia areata |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective Cohort | Indian J Dermatol | Sex differences in response to steroid pulse therapy in alopecia areata |

---

## Australia Market Information

No ARTG entries are currently registered for methylprednisolone in this evidence pack — market status is recorded as **Not marketed** in Australia, with **0** total licences. Any Australian use would currently rely on alternative marketed corticosteroid products or special access pathways; this should be confirmed directly against the TGA ARTG database before proceeding.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack does not contain usable data on key warnings, contraindications, or drug–drug interactions for methylprednisolone (all fields returned as data gaps; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Methylprednisolone pulse therapy for alopecia areata is supported by L3-level evidence — a systematic review, several retrospective cohort studies, and one completed Phase 4 trial — consistent with its established off-label use in dermatology practice. However, the drug has no current Australian market presence and key safety documentation (TGA PI warnings/contraindications) is missing, so guardrails are warranted before clinical application.

**To proceed, the following is needed:**
- TGA Product Information / warnings and contraindications for methylprednisolone (currently a Blocking data gap)
- Confirmed mechanism-of-action data from DrugBank (currently a High-severity data gap)
- Verification of Australian supply pathway, since no ARTG-registered product currently exists
- A relevance re-screen of the 18 retrieved clinical trials, since most matched on disease term only and are not genuinely about methylprednisolone in alopecia areata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

