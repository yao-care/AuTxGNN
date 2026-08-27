---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome (Post-PCI) to Pulmonary Hypertension

## One-Sentence Summary

> Prasugrel is a thienopyridine-class P2Y12 antiplatelet agent whose established clinical use — per the literature in this evidence pack — is dual antiplatelet therapy following percutaneous coronary intervention (PCI) in acute coronary syndrome (ACS).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> but the **2 clinical trials** and **2 publications** currently attached to this prediction are all off-topic and do not directly support the link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not in ARTG data (drug not marketed in Australia); known use per literature: antiplatelet therapy following PCI in ACS |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for prasugrel in this evidence pack. Based on the literature that is available, prasugrel belongs to the thienopyridine class of P2Y12 receptor antagonists (antiplatelet agents), the same class as clopidogrel. Its efficacy in reducing ischaemic events following stent placement in ACS/PCI has been well established, as reflected in the attached adherence-focused publication (PMID 21241206).

There is a theoretical mechanistic rationale connecting antiplatelet therapy to pulmonary hypertension: in-situ pulmonary artery thrombosis is recognised as part of the pathophysiology of some pulmonary hypertension subtypes, so platelet inhibition could plausibly play a role. However, none of the clinical trials or literature retrieved for this prediction actually test prasugrel — or any P2Y12 inhibitor — in pulmonary hypertension. The two trials concern NOAC management in atrial fibrillation and eligibility screening for a cancer-associated-thrombosis trial; the two publications concern clopidogrel/prasugrel adherence after PCI and a COVID-19 comorbidity registry. All four sources are unrelated to pulmonary hypertension and should be treated as search noise rather than supporting evidence.

Given this gap between the model's high prediction score and the absence of any directly relevant study, this candidate currently rests on mechanistic plausibility alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational, cross-sectional study describing NOAC management in elderly patients with non-valvular atrial fibrillation in Spain — not related to prasugrel or pulmonary hypertension. |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study assessing what proportion of cancer-associated-thrombosis patients would be eligible for trials such as CARAVAGGIO — not related to prasugrel or pulmonary hypertension. |

No Australian (ANZCTR) trials were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort (medication adherence study) | Current Medical Research and Opinion | Evaluates factors associated with clopidogrel/prasugrel use and adherence in ACS patients after PCI — establishes prasugrel's known use, but not related to pulmonary hypertension. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Retrospective analysis | Kardiologiia | ACTIV SARS-CoV-2 registry analysis of background comorbidity therapy and COVID-19 mortality risk — not specific to prasugrel or pulmonary hypertension. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for pulmonary hypertension is high, but none of the attached clinical trials or literature actually studies prasugrel (or its drug class) in this indication — the evidence base is L5 (model prediction only). No safety, MOA, or Australian regulatory data are currently available to support further evaluation.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for prasugrel (DrugBank query)
- TGA-approved Product Information — warnings, contraindications, and drug interaction data
- Targeted literature/trial search specifically for P2Y12 inhibitors (prasugrel, clopidogrel, ticagrelor) in pulmonary hypertension, since current results are off-topic
- Confirmation of ARTG registration status, as prasugrel is not currently marketed in Australia

*Note: this evidence pack's rank-2 candidate (migraine disorder, L3, decision stage S1) has a more direct mechanistic and literature basis — via thienopyridine use in PFO-associated migraine — and may warrant separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

