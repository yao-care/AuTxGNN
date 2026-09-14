---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: Extending Anti-VEGF Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is an anti-VEGF-A antibody fragment already used intravitreally for VEGF-driven retinal disease; the original indication record for this evidence pack is incomplete (drug not marketed in Australia, no ARTG data).
> Of ten candidate indications flagged by TxGNN, the top-ranked prediction — **Severe Nonproliferative Diabetic Retinopathy (severe NPDR)** — is supported by **6 clinical trials** and **19 identified publications**, including multiple completed Phase 3 RCTs, making it by far the strongest of the candidates reviewed (the remaining nine, mostly unrelated cataract subtypes and "haemorrhagic disease of newborn," have little or no supporting evidence and are recommended for Hold).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack — drug is not marketed in Australia and no ARTG licence text is available |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank for this evidence pack (marked as a data gap). Based on the evidence assembled for this candidate, Ranibizumab is a humanised monoclonal antibody Fab fragment that binds and neutralises vascular endothelial growth factor-A (VEGF-A). Diabetic retinopathy — including its severe nonproliferative stage — is pathologically driven by VEGF-mediated retinal neovascularisation and increased vascular permeability, so intravitreal anti-VEGF therapy directly targets this pathway.

Importantly, this is not a novel repurposing hypothesis so much as an extension of an already-established clinical use: anti-VEGF therapy (including Ranibizumab specifically) is already standard of care for diabetic macular oedema and proliferative diabetic retinopathy, supported by large Phase 3 programmes such as DRCR.net Protocol I/S and RIDE/RISE. The prediction for severe NPDR reflects earlier intervention in the same disease continuum — using anti-VEGF therapy prophylactically in high-risk NPDR eyes to prevent progression to vision-threatening complications, rather than waiting until proliferative disease develops.

Because the mechanistic rationale is well established and largely already validated in related diabetic retinopathy indications, the main residual uncertainty is less about *whether* the mechanism works and more about the specific severe-NPDR population, dosing regimen (including newer delivery systems), and long-term risk–benefit balance versus observation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Active, not recruiting | 174 | Port Delivery System with Ranibizumab vs comparator in diabetic retinopathy without centre-involved DME — efficacy, safety and pharmacokinetics |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Multicentre study of intravitreal ranibizumab vs sham injection for prevention of high-risk diabetic retinopathy |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Intravitreal anti-VEGF for prevention of vision-threatening complications in high-risk diabetic retinopathy eyes |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | DRCR.net Protocol I: ranibizumab ± laser vs triamcinolone + laser vs laser alone for diabetic macular oedema/retinopathy |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Six-month study of intravitreal ranibizumab for macular oedema with NPDR — effects on microaneurysm turnover and non-perfused retinal area |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy across exudative AMD, PDR, macular oedema and CNV (broader population, lower direct relevance) |

*No ANZCTR (Australian) trial registrations were identified for this indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion RCT: Port Delivery System with ranibizumab vs monitoring in NPDR without macular oedema — evaluates less-frequent prophylactic dosing |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Reviews ranibizumab's proven efficacy across the diabetic retinopathy spectrum, including DME |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Review/Meta-analysis | Health Technology Assessment | Systematic review and economic analysis of anti-VEGF vs laser photocoagulation for diabetic retinopathy |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Review/Meta-analysis | Health Technology Assessment | Systematic review/meta-analysis: anti-VEGF vs laser photocoagulation, including non-proliferative disease |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Review | Journal of Diabetes and its Complications | Overview of advances in diabetic retinopathy treatment, VEGF-A as a key therapeutic target |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Cohort (RCT post-hoc) | Ophthalmology Retina | Meta-analysis of baseline DR severity and time to DME resolution with ranibizumab across Phase 3 trials |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Cohort (RCT post-hoc) | Clinical Ophthalmology | Predictors of early diabetic retinopathy regression with ranibizumab in RIDE/RISE trials |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Cohort (RCT post-hoc) | Ophthalmic Surgery, Lasers & Imaging Retina | Post-hoc analysis of untreated fellow eyes in RIDE/RISE, characterising natural DR progression |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohort | JAMA Ophthalmology | Retinal non-perfusion characteristics on ultra-widefield angiography in severe NPDR and PDR |
| [36580154](https://pubmed.ncbi.nlm.nih.gov/36580154/) | 2023 | Basic/Mechanistic | International Ophthalmology | Serum/vitreous VEGF levels across diabetic retinopathy severity and anti-VEGF agents |

---

## Australia Market Information

Ranibizumab currently has **no ARTG entries** — the evidence pack records the drug as not marketed in Australia, with zero registered licences.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were returned for this evidence pack, and a formal drug interaction database query returned no results.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and largely de-risked — anti-VEGF therapy, including ranibizumab itself, is already validated in closely related diabetic retinopathy indications (DME, PDR), supported by two completed Phase 3 RCTs (NCT00444600, NCT02634333) plus additional ongoing Phase 3 evidence specific to severe NPDR. However, the drug is not currently registered in Australia, and drug-specific safety/PI data was not available in this pack.

**To proceed, the following is needed:**
- TGA/ARTG registration status confirmation, or Special Access Scheme pathway if pursuing use ahead of local registration
- Full Product Information — warnings, precautions and contraindications (currently unavailable in this evidence pack)
- Confirmation of DrugBank-sourced mechanism-of-action detail to formally document the mechanistic linkage
- Clinical outcome data specific to the severe-NPDR (pre-DME) population from the ongoing Phase 3 trials (NCT04503551, NCT03452657) before considering routine use in this earlier disease stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

