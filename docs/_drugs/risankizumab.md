---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

Risankizumab (DrugBank DB14762) is a humanised IgG monoclonal antibody targeting the p19 subunit of IL‑23, originally developed and approved for psoriasis and related psoriatic disease. The TxGNN model predicts it may also be effective for **Dermatitis** (with the strongest signal for atopic dermatitis), supported by **7 clinical trials** and **16 publications**, including one completed Phase 2 RCT specifically in moderate‑to‑severe atopic dermatitis. The product is not currently registered in Australia, and key safety/labelling data are missing from this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis (per literature record of first global approval; not independently confirmed by Australian licensing data, as the product is not currently marketed here) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in this evidence pack (flagged as a High‑severity data gap). Based on the literature captured in this pack, risankizumab is a humanised IgG monoclonal antibody that selectively binds the p19 subunit of interleukin‑23 (IL‑23), blocking IL‑23 signalling and downstream Th17‑pathway inflammation. It received its first global approval in 2019 for psoriasis vulgaris, psoriatic arthritis, generalised pustular psoriasis and erythrodermic psoriasis (PMID 31098898).

Psoriasis and dermatitis are both chronic, immune‑mediated inflammatory skin conditions, and atopic dermatitis in particular shares overlapping Th2/Th22 and, to some extent, Th17 pathway activity — providing a mechanistic rationale for IL‑23/IL‑22 blockade (PMID 36588137). This mechanistic overlap is consistent with why a model trained on drug–disease relationships would flag dermatitis as a plausible repurposing candidate for an IL‑23 inhibitor already validated in a closely related inflammatory skin disease.

It is worth noting that most of the supporting clinical evidence in this pack relates to psoriasis (including genital, scalp and erythrodermic subtypes) rather than dermatitis directly. The single trial and RCT publication specific to atopic dermatitis provide the most direct support for the "dermatitis" prediction; the psoriasis-focused evidence is relevant mainly as mechanistic and drug-class context rather than as direct proof for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomised, placebo-controlled study of risankizumab in adult and adolescent subjects with moderate-to-severe **atopic dermatitis** — the most directly relevant trial to the predicted indication |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Risankizumab vs apremilast in adults with moderate plaque psoriasis |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Risankizumab in adults with moderate-to-severe genital or scalp psoriasis |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A (observational) | Completed | 240 | Prospective cohort in Taiwan comparing durability of risankizumab response (PASI 90) vs other biologics in moderate-to-severe chronic plaque psoriasis |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A (observational) | Completed | 1000 | Retrospective study of genetic and cardiometabolic factors affecting 10-year survival of biologic therapies (including risankizumab) in cutaneous psoriasis |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A (observational) | Recruiting | 840 | Multi-centre biomarker profiling study across six immune-mediated inflammatory skin diseases, including atopic dermatitis and psoriasis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice for intradermal testing of FDA-approved medications (including risankizumab) for atopic dermatitis and psoriasis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 randomised, double-blind, placebo-controlled trial showing risankizumab efficacy in moderate-to-severe atopic dermatitis, supporting IL-23/IL-22 blockade rationale |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic Review | American Journal of Clinical Dermatology | Systematic review of systemic therapies, including risankizumab, for erythrodermic psoriasis |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Systematic Review | Inflammopharmacology | Systematic review of IL inhibitors (including IL-23 agents) in lichen planus, covering therapeutic and paradoxical effects |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" review describing risankizumab's IL-23 p19 mechanism and initial approval for psoriasis-spectrum disease |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Narrative Review | Children (Basel) | Review of biologics/small-molecule therapies, including risankizumab, for paediatric alopecia areata, psoriasis, atopic dermatitis and hidradenitis suppurativa |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | Review of current and emerging biologics, including risankizumab, for paediatric atopic dermatitis |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraisal of systemic immunomodulators, including risankizumab, for psoriasis and eczema in military populations |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Retrospective Observational | Experimental Dermatology | Single-centre longitudinal study of risankizumab treatment response in patients with a history of erythrodermic psoriasis |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case Series | International Journal of Dermatology | Effectiveness and safety of combined dupilumab and risankizumab in patients with concomitant atopic dermatitis and psoriasis |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | Journal of Dermatological Treatment | Case report of acrodermatitis continua of Hallopeau successfully treated with risankizumab |

---

## Australia Market Information

Risankizumab is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)** according to this evidence pack (0 licences on file). No product, dosage form or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No warnings, contraindications or drug interaction data were retrievable in this evidence pack (DDI query status: not found), and TFDA/PI label data is flagged as a **Blocking** data gap that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While there is a completed Phase 2 RCT and supportive literature for IL-23 blockade in atopic dermatitis, the product is not marketed or registered in Australia (0 ARTG entries) and product safety/labelling data (warnings, contraindications) are entirely unavailable — explicitly blocking any initial safety evaluation. Until these gaps are closed, the indication cannot be progressed regardless of the promising TxGNN score and mechanistic plausibility.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) or equivalent overseas label (warnings, contraindications, DDI) to enable initial safety evaluation
- Confirmed mechanism of action data via DrugBank API
- Clarification of Australian regulatory/import pathway status, since the product currently has no ARTG entry
- Disease-specific evidence review to confirm whether "dermatitis" evidence should be scoped narrowly to atopic dermatitis rather than the broader psoriasis-spectrum trial data included here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

