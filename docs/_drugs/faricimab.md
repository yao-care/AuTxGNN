---
layout: default
title: Faricimab
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Faricimab
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

# Faricimab: From Neovascular AMD/Diabetic Macular Edema to Diabetic Retinopathy

## One-Sentence Summary

Faricimab (Vabysmo) is a VEGF-A/Angiopoietin-2 bispecific antibody originally approved for neovascular age-related macular degeneration (nAMD) and diabetic macular edema (DME), administered by intravitreal injection. TxGNN generated 10 candidate indications for this drug; 8 of them (including the top-ranked "primary release disorder of platelets") are flagged in the source evidence itself as likely knowledge-graph embedding artefacts with no mechanistic plausibility or supporting studies. The only two candidates with real biological rationale and evidence are **diabetic retinopathy** and severe non-proliferative diabetic retinopathy — both mechanistically an earlier-stage extension of the already-approved DME indication, supported by **6 completed Phase 3 RCTs**, **25 registered clinical trials**, and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular AMD and Diabetic Macular Edema (per literature; no structured `original_moa`/license data available) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action field is not available for this drug (data gap). Based on the literature evidence in this pack (PMID 35474059, "Faricimab: First Approval"), Faricimab is a bispecific antibody that simultaneously binds and neutralises VEGF-A and Angiopoietin-2 (Ang-2), administered by intravitreal injection. It received its first approvals in 2022 for nAMD and DME, both retinal vascular diseases driven by pathological angiogenesis and vascular permeability.

Diabetic macular edema is itself a complication of diabetic retinopathy, and both conditions share the same underlying pathophysiology — retinal ischaemia-driven VEGF overexpression and neovascularisation. The predicted indication therefore represents a plausible extension of an already-validated mechanism into an earlier disease stage (non-proliferative/proliferative DR without yet-established macular edema), rather than a novel biological hypothesis.

It's worth noting explicitly: of the 10 TxGNN candidates in this evidence pack, 8 (platelet release disorder, pseudo-von Willebrand disease, Glanzmann thrombasthenia, drug-induced osteoporosis, esotropia, HER2+ breast carcinoma, RSV infection, fetal/neonatal alloimmune thrombocytopenia) carry no clinical trials, no literature, and are explicitly annotated in the pack as having "no substantive mechanistic link" or being probable embedding-similarity false positives. Diabetic retinopathy is the only candidate with genuine supporting evidence and is the focus of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03622580](https://clinicaltrials.gov/study/NCT03622580) | Phase 3 | Completed | 940 | YOSEMITE — faricimab vs aflibercept Q8W in DME; pivotal approval trial |
| [NCT03622593](https://clinicaltrials.gov/study/NCT03622593) | Phase 3 | Completed | 951 | RHINE — faricimab vs aflibercept Q8W in DME; pivotal approval trial |
| [NCT03823300](https://clinicaltrials.gov/study/NCT03823300) | Phase 3 | Completed | 658 | LUCERNE — faricimab vs aflibercept in nAMD |
| [NCT03823287](https://clinicaltrials.gov/study/NCT03823287) | Phase 3 | Completed | 671 | TENAYA — faricimab vs aflibercept in nAMD |
| [NCT04740931](https://clinicaltrials.gov/study/NCT04740931) | Phase 3 | Completed | 729 | Faricimab in macular edema secondary to CRVO/hemiretinal vein occlusion |
| [NCT04740905](https://clinicaltrials.gov/study/NCT04740905) | Phase 3 | Completed | 553 | Faricimab in macular edema secondary to branch retinal vein occlusion |
| [NCT05224102](https://clinicaltrials.gov/study/NCT05224102) | Phase 4 | Active, not recruiting | 218 | Real-world treatment response in treatment-naive, underrepresented DME populations |
| [NCT06439576](https://clinicaltrials.gov/study/NCT06439576) | N/A | Recruiting | 1000 | Farseeing Study — China real-world effectiveness/safety in DME, RVO, nAMD |
| [NCT05476926](https://clinicaltrials.gov/study/NCT05476926) | N/A | Active, not recruiting | 6000 | VOYAGER — multinational real-world long-term data across approved retinal indications |
| [NCT04597918](https://clinicaltrials.gov/study/NCT04597918) | Phase 2 | Completed | 99 | ALTIMETER — aqueous humour/imaging biomarkers in treatment-naive DME |

*Note: a further Phase 2 trial specifically for non-proliferative DR (MAGIC, [NCT05681884](https://clinicaltrials.gov/study/NCT05681884)) is ongoing and reported separately under the "severe non-proliferative diabetic retinopathy" candidate (rank 6, L2 evidence).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/) | 2022 | RCT | Lancet | YOSEMITE/RHINE 1-year results: faricimab durability up to Q16W dosing in DME |
| [38158159](https://pubmed.ncbi.nlm.nih.gov/38158159/) | 2024 | RCT | Ophthalmology | YOSEMITE/RHINE 2-year treat-and-extend results |
| [30905643](https://pubmed.ncbi.nlm.nih.gov/30905643/) | 2019 | RCT | Ophthalmology | BOULEVARD Phase 2: faricimab vs ranibizumab in DME |
| [36246184](https://pubmed.ncbi.nlm.nih.gov/36246184/) | 2022 | RCT | Ophthalmology Science | YOSEMITE/RHINE study design and rationale |
| [38852921](https://pubmed.ncbi.nlm.nih.gov/38852921/) | 2024 | RCT | Ophthalmology | Faricimab vs aflibercept efficacy in DME patients with worse baseline vision |
| [35474059](https://pubmed.ncbi.nlm.nih.gov/35474059/) | 2022 | Review | Drugs | "Faricimab: First Approval" — drug profile, MOA, and approval summary |
| [37751021](https://pubmed.ncbi.nlm.nih.gov/37751021/) | 2023 | Review | Advances in Therapy | Systematic review and network meta-analysis of faricimab in DME |
| [39362194](https://pubmed.ncbi.nlm.nih.gov/39362194/) | 2024 | Review | Ophthalmologica | Meta-analysis: faricimab efficacy/safety in nAMD, DME, RVO |
| [36012690](https://pubmed.ncbi.nlm.nih.gov/36012690/) | 2022 | Review | Int J Molecular Sciences | Aflibercept vs faricimab in nAMD and DME |
| [39708087](https://pubmed.ncbi.nlm.nih.gov/39708087/) | 2025 | Review | Graefe's Archive Clin Exp Ophthalmol | Emerging evidence for dual Ang-2/VEGF-A blockade in retinal disease |

---

## Australia Market Information

No ARTG entries were found — Faricimab is currently **not marketed** in Australia per the regulatory data in this evidence pack (`total_licenses: 0`). Australian prescribers wishing to use this agent would need to source it via the TGA Special Access Scheme or await formal ARTG registration.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured drug interaction, warning, or contraindication data was retrievable for this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Six completed Phase 3 RCTs (YOSEMITE, RHINE, LUCERNE, TENAYA, and the RVO trials) plus a large real-world evidence base (VOYAGER, Farseeing) establish strong efficacy and safety of faricimab across the VEGF-driven retinal disease spectrum, of which diabetic retinopathy is the underlying condition to DME. However, this represents extension into an earlier disease stage rather than a formally studied standalone DR indication, and the drug is not yet registered in Australia.

**To proceed, the following is needed:**
- TGA Product Information / local regulatory filing, once ARTG registration is pursued
- Formal mechanism-of-action and contraindication data from DrugBank/PI (currently a data gap)
- Results from the ongoing MAGIC Phase 2 trial (NCT05681884) specifically targeting non-proliferative DR before extending use beyond DME
- Confirmation that the other 8 TxGNN-predicted candidates in this pack (platelet disorders, HER2+ breast carcinoma, RSV, etc.) are excluded from further evaluation given their lack of mechanistic plausibility and evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

