---
layout: default
title: Selexipag
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
---

# Selexipag
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

# Selexipag: From Pulmonary Arterial Hypertension to Pulmonary Arterial Hypertension Associated with Congenital Heart Disease

## One-Sentence Summary

Selexipag is an oral, selective prostacyclin (IP) receptor agonist already established for treating pulmonary arterial hypertension (PAH) in adults, as confirmed by the literature evidence in this pack.
The TxGNN model predicts it may also be effective for **Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (PAH‑CHD)**, a recognised WHO Group 1 PAH subtype,
with **2 clinical trials** and **15 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — not recorded in the drug-level regulatory fields of this evidence pack, but confirmed by supporting literature (e.g. PMID 41429287, PMID 39076250) |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Selexipag is not recorded at the drug level in this evidence pack (flagged as data gap DG002). However, the supporting evidence assembled for this prediction consistently describes Selexipag as a selective IP prostacyclin receptor agonist, whose active metabolite (MRE‑269) drives pulmonary vasodilation and inhibits vascular smooth-muscle proliferation and platelet activation — mechanisms that act on the shared pathophysiology of PAH rather than on any single underlying cause.

PAH‑CHD is classified as a WHO Group 1 PAH subtype, the same functional category as the general PAH population in which Selexipag's efficacy has already been demonstrated. Because the IP receptor pathway targeted by Selexipag operates downstream of the vascular remodelling process common to all Group 1 PAH aetiologies, the mechanism is plausible regardless of whether the underlying trigger is idiopathic disease or a congenital shunt lesion.

This is further supported by real-world and post-marketing data: a dedicated Phase 4 study assessed Selexipag's effect on right ventricular remodelling specifically in PAH-CHD, and a post-hoc analysis of the pivotal GRIPHON RCT (PMID 30632656) specifically characterised outcomes in corrected CHD-PAH patients. This suggests the "new" indication is less a mechanistic leap and more a formal extension into a subgroup already partly represented in Selexipag's foundational evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04435782](https://clinicaltrials.gov/study/NCT04435782) | Phase 4 | Terminated | 9 | Assessed the effects of Selexipag on right ventricular (RV) function in PAH participants using cardiac MRI; terminated early, limiting conclusions. |
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Open-label, long-term extension/platform study allowing continued access to study interventions (including Selexipag) for participants from several parent PH trials; designed to assess long-term safety rather than confirm efficacy. |

No ANZCTR-registered trials were identified for this indication in the current evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30632656](https://pubmed.ncbi.nlm.nih.gov/30632656/) | 2019 | RCT subgroup (Cohort) | European Journal of Heart Failure | Post-hoc analysis of the pivotal GRIPHON RCT characterising corrected CHD-PAH patients treated with Selexipag; this subgroup has a poorer prognosis than other CHD-PAH patients. |
| [33442633](https://pubmed.ncbi.nlm.nih.gov/33442633/) | 2020 | Cohort (case series) | European Heart Journal – Case Reports | Describes contemporary use of Selexipag in PAH-CHD, noting it may reduce disease progression and improve exercise capacity while avoiding risks of parenteral prostacyclin therapy. |
| [29521655](https://pubmed.ncbi.nlm.nih.gov/29521655/) | 2018 | Cohort (case report) | American Journal of Therapeutics | First report of Selexipag use in CHD-associated PAH and Eisenmenger syndrome. |
| [41429287](https://pubmed.ncbi.nlm.nih.gov/41429287/) | 2025 | Phase 2 (single-arm PK study) | Chest | Prospective, multicentre Phase 2 study of pharmacokinetics, safety, tolerability and exploratory efficacy of Selexipag in children with PAH. |
| [36204579](https://pubmed.ncbi.nlm.nih.gov/36204579/) | 2022 | Cohort | Frontiers in Cardiovascular Medicine | Assessed safety and efficacy of Selexipag-based triple combination therapy (with ERAs and PDE5is) in Chinese PAH patients. |
| [32394855](https://pubmed.ncbi.nlm.nih.gov/32394855/) | 2020 | Case series | Kardiologiia | Registry experience with Selexipag in PAH, including patients with corrected congenital heart defects, drawn from the GRIPHON/GRIPHON-OL studies. |
| [33781364](https://pubmed.ncbi.nlm.nih.gov/33781364/) | 2021 | Case series | Cardiology in the Young | Single-centre report on Selexipag use in four paediatric PAH patients, focused on those with congenital heart disease. |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | Journal of Personalized Medicine | Reviews current management and future directions for PAH-CHD, noting novel agents have improved morbidity/mortality in this subgroup. |
| [30545978](https://pubmed.ncbi.nlm.nih.gov/30545978/) | 2019 | Review | European Respiratory Journal | Paediatric PAH task force update on definition, classification, diagnostics and management, relevant background for paediatric CHD-PAH. |
| [31738929](https://pubmed.ncbi.nlm.nih.gov/31738929/) | 2020 | Expert Consensus | Chest | Expert consensus statements on the use of oral prostacyclin pathway agents (including Selexipag) for initiation in adults with PAH. |

---

## Australia Market Information

Selexipag is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)** and has no marketed product in Australia according to this evidence pack (0 licences on file).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications and drug interaction data are not currently available in this evidence pack (data gap DG001, flagged as **Blocking** — required before any safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and partly substantiated by a post-hoc RCT subgroup analysis (GRIPHON) and a dedicated Phase 4 study, but the Phase 4 study was terminated early with only 9 participants, and no confirmatory RCT has been conducted specifically in the PAH-CHD population. Evidence level L2 supports cautious progression rather than unconditional adoption.

**To proceed, the following is needed:**
- TGA-approved Product Information / label data, including key warnings and contraindications (currently a blocking data gap, DG001)
- Detailed mechanism of action documentation at the drug level (currently a high-priority data gap, DG002)
- Confirmation of ARTG registration pathway, given Selexipag is not currently marketed in Australia
- Results from the terminated NCT04435782 study and outcomes from the ongoing NCT05179876 extension study once available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

