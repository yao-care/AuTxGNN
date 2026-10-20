---
layout: default
title: Tafamidis
parent: Model Prediction Only (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tafamidis: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Amyloidosis"
monitor_inn: "Tafamidis"
predicted_indications: ["primary release disorder of platelets", "thrombocytopenic purpura", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired amyloid peripheral neuropathy", "primary hyperoxaluria", "dermis disease", "biotin metabolic disease", "mixed-type autoimmune hemolytic anemia"]
---

# Tafamidis
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Tafamidis: From Transthyretin Amyloidosis to Primary Amyloidosis

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabiliser, originally used to treat amyloidosis, particularly transthyretin amyloid cardiomyopathy and polyneuropathy.
The TxGNN model's top-ranked prediction is **primary release disorder of platelets**, which has **no clinical trials and no publications** behind it. The best-supported prediction is **primary amyloidosis** (rank 5), which has **20 publications** but largely overlaps with tafamidis's existing approved use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyloidosis (including transthyretin amyloidosis; the Australian licence text is not available in the data compiled for this report) |
| Predicted New Indication | Primary release disorder of platelets (top-ranked prediction) |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Note on other predictions:** The top-ranked prediction has no supporting evidence. Of the ten predictions, only two have any literature: primary amyloidosis (85.00%, L4) and acquired amyloid peripheral neuropathy (84.77%, L4). Both are closely related to existing tafamidis uses rather than genuinely new indications. The remaining eight predictions are L5 (model prediction only) and are rated Hold.

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Primary release disorder of platelets | 89.27% | L5 | Hold |
| 2 | Thrombocytopenic purpura | 88.73% | L5 | Hold |
| 3 | Pseudo-von Willebrand disease | 87.88% | L5 | Hold |
| 4 | Glanzmann thrombasthenia | 85.79% | L5 | Hold |
| 5 | Primary amyloidosis | 85.00% | L4 | Research Question |
| 6 | Acquired amyloid peripheral neuropathy | 84.77% | L4 | Research Question |
| 7 | Primary hyperoxaluria | 84.33% | L5 | Hold |
| 8 | Dermis disease | 83.36% | L5 | Hold |
| 9 | Biotin metabolic disease | 83.32% | L5 | Hold |
| 10 | Mixed-type autoimmune haemolytic anaemia | 82.31% | L5 | Hold |

---

## Why is This Prediction Reasonable?

The mechanism of action field was not populated in the data compiled for this report. However, pharmacology data indicate that tafamidis binds the thyroxine-binding sites of the transthyretin (TTR) tetramer. This stabilises the tetramer and prevents its dissociation into misfolded, amyloid-forming monomers. It acts on both wild-type and mutant TTR.

**Top-ranked prediction (platelet release disorder).** There is no identifiable mechanistic link. Tafamidis has no known role in platelet granule release or platelet function. The same applies to the other platelet and haematological predictions (thrombocytopenic purpura, pseudo-von Willebrand disease, Glanzmann thrombasthenia, autoimmune haemolytic anaemia). Likewise, primary hyperoxaluria, biotin metabolic disease and dermis disease have no recognised connection to TTR stabilisation. These scores come from graph-based prediction alone and should be treated with caution.

**Primary amyloidosis (rank 5).** The mechanistic fit is strong for TTR amyloidosis, and the ATTR-ACT Phase 3 trial supports tafamidis in transthyretin amyloid cardiomyopathy. However, "primary amyloidosis" classically refers to AL amyloidosis, which is driven by clonal light chains rather than TTR. Tafamidis is not expected to work in AL. The strong evidence therefore applies to ATTR-CM, which is already an approved use, so this is not a novel repurposing candidate.

**Acquired amyloid peripheral neuropathy (rank 6).** Tafamidis is approved in several regions for early-stage hereditary ATTR polyneuropathy. Acquired ATTR shares the same amyloidogenic pathway, so the rationale is sound. However, the evidence is indirect, extrapolated from hereditary ATTR and ATTR-CM, with no trial specific to acquired neuropathy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications in the data compiled for this report.

---

## Literature Evidence

The literature below relates to the best-supported predictions (primary amyloidosis and acquired amyloid peripheral neuropathy). The top-ranked prediction has no related literature. Currently no related literature is available for it.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30145929](https://pubmed.ncbi.nlm.nih.gov/30145929/) | 2018 | RCT | N Engl J Med | Tafamidis in transthyretin amyloid cardiomyopathy (ATTR-ACT); tafamidis binds TTR and prevents tetramer dissociation |
| [39213194](https://pubmed.ncbi.nlm.nih.gov/39213194/) | 2025 | RCT | N Engl J Med | Vutrisiran (RNA interference) in ATTR cardiomyopathy |
| [40380962](https://pubmed.ncbi.nlm.nih.gov/40380962/) | 2025 | RCT analysis | J Am Coll Cardiol | HELIOS-B: vutrisiran improves survival and reduces cardiovascular events in ATTR-CM |
| [41282536](https://pubmed.ncbi.nlm.nih.gov/41282536/) | 2025 | Network meta-analysis | Eur Heart J Open | Relative efficacy of tafamidis, acoramidis, patisiran and vutrisiran in ATTR cardiac amyloidosis |
| [40889572](https://pubmed.ncbi.nlm.nih.gov/40889572/) | 2025 | Systematic review/meta-analysis | J Card Fail | Harmonised outcomes of phase 3 placebo-controlled ATTR-CM drug trials |
| [41334760](https://pubmed.ncbi.nlm.nih.gov/41334760/) | 2025 | Cohort | J Am Heart Assoc | Tafamidis reduced death and acute heart failure hospitalisation in octogenarians with ATTR cardiac amyloidosis |
| [41317156](https://pubmed.ncbi.nlm.nih.gov/41317156/) | 2025 | Cohort | Eur J Heart Fail | Real-world phenotype and survival of wild-type ATTR-CM patients treated with tafamidis |
| [38441582](https://pubmed.ncbi.nlm.nih.gov/38441582/) | 2024 | Review | JAMA | Review of cardiac amyloidosis due to transthyretin protein |
| [26662359](https://pubmed.ncbi.nlm.nih.gov/26662359/) | 2015 | Review | Neurol Ther | Review of tafamidis in TTR-related amyloidosis, including kinetic stabilisation of native and mutant TTR |
| [41493356](https://pubmed.ncbi.nlm.nih.gov/41493356/) | 2026 | Cohort | Amyloid | Long-term outcomes of acquired ATTR amyloidosis after domino liver transplantation, and the effects of disease-modifying drugs |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14100D | Vyndamax | Capsule 61 mg (oral) | Indication text not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions** (13 records, from DDInter and pharmacology sources):
  - **Major:** Ozanimod.
  - **Moderate:** Rosuvastatin, deferasirox, eltrombopag, lusutrombopag, artesunate, axitinib, methotrexate, irinotecan (including liposomal), belinostat and imatinib.
  - Tafamidis's pharmacological target is transthyretin (TTR).

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (primary release disorder of platelets) and most other predictions are model outputs only, with no trials, no literature and no plausible mechanism. The two predictions with literature (primary amyloidosis and acquired amyloid peripheral neuropathy) are L4 and largely overlap with existing or approved tafamidis uses in ATTR. Tafamidis is not expected to be effective in AL amyloidosis, so they do not represent novel repurposing opportunities.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- TGA Product Information safety data (warnings and contraindications), which is a blocking gap for safety screening
- The approved indication text for the Vyndamax ARTG entry
- For primary amyloidosis, clarification of whether the intended target is AL or ATTR amyloidosis
- For acquired amyloid neuropathy, targeted clinical evidence in acquired ATTR neuropathy
- For the platelet and haematological predictions, any biological rationale or preclinical evidence before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

