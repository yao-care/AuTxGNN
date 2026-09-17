---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using no special skill here — this is a direct content-generation task per the given Evidence Pack template, not a TxGNN pipeline/engineering task.

One judgment call before drafting: the pack's `predicted_indications[0]` (duodenal ulcer, score 99.86%) is explicitly annotated by the pipeline itself as a mechanism-free false positive (`decision_stage: S0`, `Hold`, "無已知機轉關聯...判斷為 TxGNN 高分但無實證支撐的假陽性預測"). The only candidate the pack's own scoring promotes past S0 is rank 8 — Pregnancy and Lactation-Associated Osteoporosis (PLO), `L3`/`S2`/"Proceed with Guardrails," with real trials and 20 literature hits. Building the report around rank 1 would produce a self-contradicting document (feature a prediction the evidence explicitly refutes), so I'm reporting on the pack's actual best-supported candidate (rank 8) and flagging the top raw-score hits as screened-out noise in the summary.

---

# Teriparatide: From Osteoporosis to Pregnancy and Lactation-Associated Osteoporosis

## One-Sentence Summary

Teriparatide is a recombinant human parathyroid hormone fragment (PTH 1-34) approved for osteoporosis, working by stimulating bone formation. The TxGNN model's highest raw-score predictions (e.g. duodenal ulcer, esophageal malformation) lack any mechanistic or evidentiary support and are flagged as likely false positives; the strongest genuinely supported candidate is **Pregnancy and Lactation-Associated Osteoporosis (PLO)**, a rare osteoporosis subtype, backed by **2 clinical trials** and **20 publications**, including cohort and case-series data specific to teriparatide.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (identified from mechanistic rationale in the evidence pack; formal ARTG-sourced indication text and MOA record are data gaps — see below) |
| Predicted New Indication | Pregnancy and Lactation-Associated Osteoporosis (PLO) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 (observational studies / systematic review) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for teriparatide is not formally recorded in this dataset (flagged as a data gap, DG002). Based on the information accompanying the prediction, teriparatide is the 1-34 amino-acid fragment of human parathyroid hormone; intermittent dosing shifts bone remodelling toward net osteoblastic bone formation. This is the established pharmacological basis for its approved use in osteoporosis.

PLO is not a mechanistically distinct disease — it is a recognised rare subtype of osteoporosis, driven by the transient calcium and bone-turnover demands of late pregnancy and lactation, presenting with fragility (typically vertebral) fractures. Because the underlying pathology in PLO is the same bone-remodelling imbalance that teriparatide is designed to correct, this repurposing candidate does not require a novel mechanistic leap; it extends an existing anabolic action to a physiologically distinct but pathologically analogous population. This is reflected directly in the evidence pack's own rationale: "與核准適應症（骨質疏鬆症）機轉完全一致" (fully consistent with the mechanism of the approved indication).

By contrast, the model's top raw-score hits (duodenal ulcer, esophageal disorders, Worth syndrome, etc.) have no plausible link to PTH signalling and zero supporting trials or literature — several were even flagged in the pack as running in the opposite pharmacological direction (e.g. Worth syndrome is a bone-*overgrowth* disorder). These should not be treated as credible repurposing signals.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Evaluated PTH(1-34) effect on oral bone regeneration alongside periodontal surgery; supports PTH pathway bioactivity but not PLO-specific (graded indirect relevance) |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Studied bone loss in renal osteodystrophy (CKD-associated osteoporosis); population and design differ from PLO (graded indirect relevance) |

Neither trial directly enrolled a PLO population; both are cited as supportive-only evidence of PTH pathway activity in bone. No ANZCTR-registered trials were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic Review/Meta-analysis | J Clin Endocrinol Metab | Comparative effectiveness of therapeutic interventions (including teriparatide) in PLO |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Cohort | Geburtshilfe Frauenheilkd | Teriparatide effect on subsequent fracture and BMD in 47 women with PLO and vertebral fractures |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Case Series | Calcif Tissue Int | Retrospective multicentre cohort: teriparatide (20 μg/day) vs conventional management on BMD/TBS in 19 PLO patients |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Management strategies for PLO with a focus on teriparatide use |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review/Meta-analysis | Osteoporos Int | Presentation, risk factors and treatment response in pregnancy-associated osteoporosis (35 studies, 943 patients) |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Cohort | Calcif Tissue Int | BMD after teriparatide discontinuation with/without antiresorptive therapy in PLO |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | Calcif Tissue Int | Overview of pregnancy and lactation-associated osteoporosis |
| [28084543](https://pubmed.ncbi.nlm.nih.gov/28084543/) | 2017 | Review | Z Rheumatol | Notes teriparatide and bisphosphonates as the best treatment options for PLO |
| [37551335](https://pubmed.ncbi.nlm.nih.gov/37551335/) | 2023 | Review | Int J Womens Health | Recent insights into PLO, including treatment options |
| [37819437](https://pubmed.ncbi.nlm.nih.gov/37819437/) | 2023 | Retrospective cohort | Calcif Tissue Int | Clinical features, incidence and treatment outcome in PAO, single-centre 20-year experience |

## Australia Market Information

Teriparatide is currently **not marketed** in Australia within this dataset, with **0 ARTG entries** on record. No product-level detail (dosage form, brand, approved indication text) is available to report.

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is available for teriparatide in this dataset — all fields are recorded as data gaps (DG001, blocking severity), and no interaction records were returned. Please refer to the TGA-approved Product Information (PI), where available, or the manufacturer's global labelling for safety guidance before any clinical consideration.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The PLO indication is mechanistically coherent (same drug, same target pathology as the approved osteoporosis indication) and is supported by multiple cohort studies, case series, and a systematic review specifically evaluating teriparatide in this population — the strongest evidence tier of any candidate in this evidence pack. However, no RCTs exist, teriparatide is not currently marketed/registered in Australia, and safety/MOA documentation is incomplete.

**To proceed, the following is needed:**
- TFDA/TGA-sourced product information: warnings, contraindications, and formal MOA documentation (data gaps DG001, DG002)
- Confirmation of ARTG registration pathway, since the drug is currently unmarketed in Australia
- Reproductive/lactation-specific safety data, given the target population is pregnant or breastfeeding women
- Prospective or comparative (vs. bisphosphonate) trial data specific to PLO, as current evidence is observational only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

