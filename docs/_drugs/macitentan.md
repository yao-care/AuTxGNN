---
layout: default
title: Macitentan
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Macitentan
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

# Macitentan: From Pulmonary Arterial Hypertension to PAH Associated with Congenital Heart Disease

## One-Sentence Summary

> Macitentan is a dual endothelin receptor antagonist (ERA) already indicated for the long-term treatment of pulmonary arterial hypertension (PAH) in general.
> The TxGNN model additionally flags **PAH associated with congenital heart disease (CHD-PAH)** — and, with equally strong evidence, **PAH associated with connective tissue disease (CTD-PAH)** — as specific, well-supported subtypes,
> backed by **2 clinical trials and 18 publications** for CHD-PAH alone. Note that TxGNN's raw top-scoring hits (pulmonary arteriovenous malformation, alopecia-related conditions) had **zero** supporting trials or literature and are assessed in this evidence pack as likely knowledge-graph noise, so they are not used as the headline prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (WHO Group 1), general population — not stated in the supplied regulatory data, but confirmed across the literature evidence (e.g. PMID 32487059: "Macitentan is a dual endothelin receptor antagonist indicated for the long-term treatment of pulmonary arterial hypertension (PAH)") |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease (CHD-PAH) |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Macitentan is a dual endothelin receptor antagonist (ERAA/ERAB) that inhibits endothelin-driven vasoconstriction and smooth-muscle proliferation in the pulmonary vasculature. This is the standard mechanistic basis for WHO Group 1 PAH therapy, and macitentan's pivotal trial (SERAPHIN) pre-specified aetiology subgroups — including CHD-PAH and CTD-PAH — as part of its original PAH indication, so the mechanistic extrapolation to these subtypes is strong rather than speculative.

CHD-PAH (including Eisenmenger syndrome) and CTD-PAH (predominantly systemic sclerosis) together make up a large share of the non-idiopathic PAH population and share the same underlying pulmonary vascular remodelling pathway targeted by ERA therapy. This is reflected in the evidence base: an ongoing Phase 3 long-term follow-up platform trial for CHD-PAH, a completed Phase 3 randomised controlled trial in Eisenmenger syndrome (MAESTRO), and multiple real-world cohort studies (OPUS/OrPHeUS) reporting outcomes specifically in these subgroups.

Because macitentan's original approval already covers PAH broadly, this is best framed not as a novel-disease repurposing but as **subtype-specific evidence consolidation** — relevant for guardrail-conditioned labelling, reimbursement, or registration decisions in a market (Australia) where the drug is currently not marketed at all.

By contrast, the TxGNN model's highest raw-score predictions — pulmonary arteriovenous malformation, hypotrichosis, alopecia areata, and alopecia — returned zero clinical trials and zero literature on query, and the evidence pack's own rationale explicitly attributes these to graph proximity artefacts (e.g. shared "pulmonary vessel" or rare-disease/gene nodes) rather than real pharmacology.

---

## Clinical Trial Evidence — CHD-PAH

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Prospective, open-label long-term follow-up platform study for participants continuing macitentan (and other interventions) after closure of parent PAH studies, including CHD-associated PAH; assesses long-term safety. |
| [NCT05731492](https://clinicaltrials.gov/study/NCT05731492) | Phase 1 | Withdrawn | 0 | Planned paediatric (1 month–<2 years) PK/safety study of macitentan and its active metabolite; withdrawn with no participants enrolled. |

## Literature Evidence — CHD-PAH

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30586694](https://pubmed.ncbi.nlm.nih.gov/30586694/) | 2019 | RCT (Phase 3, MAESTRO) | Circulation | Multicentre, double-blind, placebo-controlled 16-week trial of macitentan in Eisenmenger syndrome (CHD-associated PAH with right-to-left shunt). |
| [41796854](https://pubmed.ncbi.nlm.nih.gov/41796854/) | 2026 | RCT (TOMORROW) | The Journal of Pediatrics | Randomised trial of macitentan vs standard of care in paediatric PAH, evaluating PK, efficacy and safety. |
| [39585521](https://pubmed.ncbi.nlm.nih.gov/39585521/) | 2024 | Cohort (Real-World) | Cardiology and Therapy | OPUS/OrPHeUS real-world data on patients with CHD-PAH newly initiating macitentan. |
| [40616677](https://pubmed.ncbi.nlm.nih.gov/40616677/) | 2026 | Cohort (Multicentre, Real-World) | Pediatric Cardiology | Multicentre experience of oral macitentan in patients under 18 with Group 1 PAH from the Spanish paediatric PH registry. |
| [36329372](https://pubmed.ncbi.nlm.nih.gov/36329372/) | 2023 | Cohort (Real-World, Asian) | Drugs – Real World Outcomes | Prospective multicentre post-marketing surveillance of macitentan safety/outcomes in Asian PAH patients. |
| [36196862](https://pubmed.ncbi.nlm.nih.gov/36196862/) | 2022 | Cohort (Real-World) | Anatolian Journal of Cardiology | Single-centre comparison of macitentan effectiveness/safety across idiopathic and CHD-associated PAH. |
| [35514768](https://pubmed.ncbi.nlm.nih.gov/35514768/) | 2022 | Prospective Cohort (POTENT) | Pulmonary Circulation | Prospective assessment of PAH patients switched from bosentan to macitentan. |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | Journal of Personalized Medicine | Current management and future directions for PAH associated with congenital heart disease. |
| [28867027](https://pubmed.ncbi.nlm.nih.gov/28867027/) | 2017 | Review/Editorial | Heart, Lung & Circulation | Macitentan in pulmonary arterial hypertension associated with congenital heart defects. |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review/Meta-analysis | Medicine | Position of PAH-specific drug therapy, including ERAs, in Eisenmenger syndrome. |

---

## Additional High-Evidence Indication: PAH Associated with Connective Tissue Disease (CTD-PAH)

CTD-PAH scores similarly (98.59%) and carries the same Evidence Level (L1) and recommendation (Proceed with Guardrails) as CHD-PAH — it represents the largest aetiology subgroup in the original SERAPHIN trial and should be considered alongside CHD-PAH for the same regulatory pathway.

**Clinical Trials:** Two trials identified, both weak direct evidence — [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) (Phase 4, terminated, n=3, comparator-focused on ambrisentan switch) and [NCT03726398](https://clinicaltrials.gov/study/NCT03726398) (Phase 2/3, withdrawn, n=0). Neither adds meaningful trial-level support on its own.

**Selected Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis | Internal and Emergency Medicine | Meta-analysis of RCT subgroup/post-hoc data for CTD-PAH treatment. |
| [38617769](https://pubmed.ncbi.nlm.nih.gov/38617769/) | 2024 | Cohort (Real-World) | Journal of Thoracic Disease | Efficacy and safety of macitentan specifically in CTD-PAH. |
| [38451426](https://pubmed.ncbi.nlm.nih.gov/38451426/) | 2024 | Cohort (Real-World) | Cardiology and Therapy | OPUS/OrPHeUS real-world data on CTD-PAH patients newly initiating macitentan. |
| [40840780](https://pubmed.ncbi.nlm.nih.gov/40840780/) | 2025 | Cohort | Vascular Pharmacology | 12-month evaluation of non-invasive low-risk criteria in CTD-PAH (INSPECTIO study). |
| [37728697](https://pubmed.ncbi.nlm.nih.gov/37728697/) | 2023 | Cohort (Real-World) | Advances in Therapy | Retrospective claims-based analysis of real-world CTD-PAH treatment patterns. |

---

## Australia Market Information

Macitentan is currently **not registered on the ARTG** and has **no marketed products in Australia** based on the supplied regulatory data (0 licences on file, market status "Not Marketed").

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence for macitentan in CHD-PAH and CTD-PAH is strong — an ongoing Phase 3 platform trial, a completed Phase 3 RCT (MAESTRO) in Eisenmenger syndrome, and multiple real-world cohorts across both subtypes (Evidence Level L1). However, macitentan is not currently registered or marketed in Australia, and no TGA Product Information, warnings, contraindications, or drug interaction data are available, which blocks formal safety pre-assessment (S1).

**To proceed, the following is needed:**
- TGA/TFDA Product Information (warnings, contraindications, DDI) — Blocking gap (DG001)
- Mechanism of action confirmation from DrugBank or equivalent primary source (DG002)
- Confirmation of ARTG registration pathway/status, since the drug is presently unmarketed in Australia
- Clarification of overlap between the "predicted" CHD-PAH/CTD-PAH indications and macitentan's existing broad PAH approval, to determine whether this is a labelling/subgroup matter rather than a de novo indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

