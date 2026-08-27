---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Orlistat
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

# Orlistat: From Obesity Management to Non-Alcoholic Fatty Liver Disease (NAFLD/NASH)

> **Note on indication selection:** TxGNN's top-ranked prediction by raw score is *hypervitaminosis* (99.4%), but the evidence pack's own rationale flags this as a known adverse effect of lipase inhibition, not a viable treatment target — and it has zero supporting trials or literature (L5/Hold). This report instead focuses on **fatty liver disease (NAFLD/NASH)**, the only candidate among the 10 predicted indications with completed clinical trials, matching publications, and an actionable recommendation.

## One-Sentence Summary

Orlistat is a gastric/pancreatic lipase inhibitor originally used for weight management in obesity. TxGNN predicts potential efficacy for **non-alcoholic fatty liver disease (NAFLD/NASH)**, with **2 directly relevant completed Phase 4 clinical trials** (and corresponding peer-reviewed publications identified during evidence review) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (well-established use; not recorded in this evidence pack's structured fields) |
| Predicted New Indication | Non-Alcoholic Fatty Liver Disease (NAFLD/NASH) |
| TxGNN Prediction Score | 85.26% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not separately documented in this evidence pack. Based on the repurposing analysis, Orlistat inhibits gastric and pancreatic lipase, reducing dietary fat absorption by approximately 30% — the established pharmacological basis for its use in weight management.

This mechanism maps directly onto NAFLD/NASH pathophysiology: reduced fat absorption lowers hepatic fat delivery and contributes to weight loss, both of which address the lipotoxicity and insulin resistance that drive fatty liver disease. Obesity is itself a primary risk factor for NAFLD, so a drug that treats obesity has a plausible, direct route to benefiting fatty liver outcomes rather than a purely coincidental network association.

Two completed Phase 4 trials tested this hypothesis directly rather than as a downstream inference: **NCT00207311** and **NCT00160407** both enrolled overweight patients with hepatic steatosis/NASH and used orlistat as the active intervention.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00207311](https://clinicaltrials.gov/study/NCT00207311) | Phase 4 | Completed | 30 | RCT of orlistat in patients with >33% hepatic steatosis or NASH plus chronic hepatitis C. Corresponds to published RCT (PMID 16630771) showing significant ALT and ultrasound-graded steatosis improvement; insulin resistance and fibrosis signals warrant monitoring. **[Relevance: A]** |
| [NCT00160407](https://clinicaltrials.gov/study/NCT00160407) | Phase 4 | Completed | 50 | Orlistat (Xenical) in overweight patients with NASH. Corresponds to published RCT (PMID 19053049): enhanced weight loss with improvement in necroinflammatory and fibrotic liver changes. **[Relevance: A]** |
| [NCT00001723](https://clinicaltrials.gov/study/NCT00001723) | Phase 2 | Completed | 200 | Safety/efficacy of orlistat in adolescents with obesity-related comorbidities. Supports the obesity→liver pathway but was not a NAFLD-primary-endpoint trial. **[Relevance: B]** |
| [NCT04270656](https://clinicaltrials.gov/study/NCT04270656) | N/A | Completed | 46 | Studies insulin pump therapy (not orlistat) in T2D patients with NAFLD — same disease category only, not direct orlistat evidence. **[Relevance: C]** |
| [NCT05934110](https://clinicaltrials.gov/study/NCT05934110) | Phase 2 | Unknown | 320 | Compares EMP16 + acarbose combination against conventional orlistat and placebo; orlistat's role as comparator (not primary intervention) could not be confirmed from the available summary. **[Relevance: C]** |
| [NCT06501326](https://clinicaltrials.gov/study/NCT06501326) | Phase 4 | Unknown | 102 | Studies liraglutide (not orlistat) in obesity with MAFLD — different drug, listed for category context only. **[Relevance: C]** |
| [NCT07437001](https://clinicaltrials.gov/study/NCT07437001) | N/A | Not yet recruiting | 60 | Studies electroacupuncture (not orlistat) for central obesity and fatty liver — not direct orlistat evidence. **[Relevance: C]** |

No ANZCTR-registered trials were identified for this indication in the evidence pack.

## Literature Evidence

The evidence pack's structured literature collector returned no results specifically indexed against this indication. However, the repurposing rationale references two externally-identified publications corresponding to the trials above — **PMID 16630771** (Zelber-Sagi et al., 2006, RCT, corresponds to NCT00207311) and **PMID 19053049** (RCT, corresponds to NCT00160407) — which were confirmed during evidence review but are not yet formally captured in this dataset's literature table. These should be added to the formal evidence base before further progression.

## Australia Market Information

Orlistat is **not currently marketed** in Australia under this evidence pack (0 ARTG entries recorded). No product listing, dosage form, or approved indication text is available to summarise.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack did not return usable data on key warnings, contraindications, or drug–drug interactions (DDI query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 4 RCTs directly tested orlistat in NAFLD/NASH populations, with corresponding publications showing measurable improvement in hepatic steatosis, ALT, and (in one trial) necroinflammatory/fibrotic changes — meaningfully stronger evidence than the other 9 TxGNN candidates in this pack, all of which are L5/Hold with no supporting trials or literature. However, orlistat is not currently marketed in Australia and this evidence pack lacks safety/DDI data, so guardrails are needed before advancing.

**To proceed, the following is needed:**
- TGA Product Information — key warnings, contraindications, DDI profile (currently blocking data gap, DG001)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Formal incorporation of PMID 16630771 and PMID 19053049 into the structured literature evidence base
- Clarification of the ARTG registration pathway, since the drug is not currently marketed in Australia
- Independent assessment of fibrosis/insulin-resistance safety signals noted in NCT00207311 before any clinical translation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

