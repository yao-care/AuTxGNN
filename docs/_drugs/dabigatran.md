---
layout: default
title: Dabigatran
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dabigatran: predicted new indication Myocardial infarction (evidence level L5). Approved use: Not available in the data compiled for this report. Dabigatran is gen…"
monitor_inn: "Dabigatran"
predicted_indications: ["hemoglobinopathy", "myocardial infarction", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells", "posterolateral myocardial infarction", "posteroinferior myocardial infarction", "septal myocardial infarction", "coronary thrombosis"]
---

# Dabigatran
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

# Dabigatran: From Thromboembolic Prophylaxis to Myocardial Infarction

## One-Sentence Summary

Dabigatran is an oral direct thrombin inhibitor marketed in Australia as Pradaxa. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be useful for **myocardial infarction** (the highest-ranked prediction with meaningful supporting evidence), with **1 completed Phase 3 placebo-controlled trial** and **19 publications** linked to this direction.
The evidence is mixed: it supports a narrow role (for example, atrial fibrillation patients after PCI) rather than a general indication, and it includes a signal of possible increased MI risk.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report. Dabigatran is generally known for stroke prevention in non-valvular atrial fibrillation and for venous thromboembolism prophylaxis and treatment. |
| Predicted New Indication | Myocardial infarction (the rank 1 prediction, hemoglobinopathy, has only indirect L4 evidence; see the note below) |
| TxGNN Prediction Score | 98.13% (myocardial infarction); 98.43% for the top-ranked hemoglobinopathy |
| Evidence Level | L1 (as graded in the data compiled for this report; see the caveat in the conclusion) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (narrow AF + PCI population only) |

**Note on the ranking:** The top TxGNN prediction is hemoglobinopathy (98.43%), but it is supported only by one small observational report in β-thalassaemia and one mouse study in sickle cell disease. This report focuses on myocardial infarction because it has the most substantial clinical evidence. Other predictions are summarised briefly at the end of the clinical evidence sections.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dabigatran is a direct, competitive thrombin inhibitor. Thrombin drives fibrin formation and platelet activation, so blocking it reduces coagulation-driven thrombus formation.

Acute coronary syndrome and myocardial infarction involve thrombus formation on a ruptured plaque. Thrombin inhibition is therefore mechanistically plausible. However, arterial clots are platelet-rich, and antiplatelet agents are usually more effective than anticoagulants alone in this setting.

The clinical data point to a nuanced role. Evidence supports dual therapy with a P2Y12 inhibitor in AF patients after PCI (RE-DUAL PCI-type regimens), rather than a general MI indication. Trial and meta-analytic data have also raised a signal of possible increased MI risk with dabigatran, which remains debated. The strength of the TxGNN score should not be read as clinical proof.

---

## Clinical Trial Evidence

Myocardial infarction (the most relevant trials, from 5 linked):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01661101](https://clinicaltrials.gov/study/NCT01661101) | Phase 3 | Completed | 1,754 | Placebo-controlled trial of dabigatran (and omeprazole) in myocardial injury after noncardiac surgery |
| [NCT04688723](https://clinicaltrials.gov/study/NCT04688723) | Phase 4 | Unknown | 1,000 | Real-life registry: dabigatran/ticagrelor versus dabigatran/clopidogrel after PCI in ACS patients needing an anticoagulant |
| [NCT03568916](https://clinicaltrials.gov/study/NCT03568916) | N/A | Completed | 227,579 | Multi-database cohort comparing DOACs for stroke prevention in AF; MI is an outcome only |
| [NCT04062097](https://clinicaltrials.gov/study/NCT04062097) | N/A | Completed | 104 | Idarucizumab registry in intracranial haemorrhage on dabigatran; concerns reversal, not MI |
| [NCT02723981](https://clinicaltrials.gov/study/NCT02723981) | Phase 4 | Withdrawn | 0 | COMBO stent with short-term antiplatelet therapy in patients needing oral anticoagulation; no data |

Coronary thrombosis (the most relevant trials, from 7 linked; none is coronary-specific):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01505881](https://clinicaltrials.gov/study/NCT01505881) | Phase 2 | Terminated | 158 | Long-term safety of dabigatran in bileaflet mechanical heart valves; unfavourable thrombotic and bleeding outcomes |
| [NCT02256683](https://clinicaltrials.gov/study/NCT02256683) | Phase 2 | Terminated | 64 | Dabigatran versus phenprocoumon for left atrial appendage thrombus resolution in AF |
| [NCT02313584](https://clinicaltrials.gov/study/NCT02313584) | Phase 3 | Unknown | 464 | Duration of dabigatran after AF ablation in low-risk patients |
| [NCT03539055](https://clinicaltrials.gov/study/NCT03539055) | Phase 4 | Completed | 100 | Short-term dabigatran then aspirin after left atrial appendage closure |
| [NCT04042155](https://clinicaltrials.gov/study/NCT04042155) | N/A | Unknown | 1,600 | Observational DOAC management model in AF and VTE |
| [NCT04157881](https://clinicaltrials.gov/study/NCT04157881) | Phase 4 | Completed | 46 | Pharmacokinetic study of rabeprazole's effect on dabigatran exposure in healthy volunteers |

No clinical trials are registered for hemoglobinopathy. No Australian (ANZCTR) trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

Myocardial infarction (selected from 19 linked publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19717844](https://pubmed.ncbi.nlm.nih.gov/19717844/) | 2009 | RCT (RE-LY) | N Engl J Med | Dabigatran versus warfarin in AF; source of the MI-risk discussion |
| [31533437](https://pubmed.ncbi.nlm.nih.gov/31533437/) | 2020 | Network meta-analysis | Angiology | Direct anticoagulants and risk of MI |
| [24906369](https://pubmed.ncbi.nlm.nih.gov/24906369/) | 2014 | Meta-analysis of RCTs | J Am Heart Assoc | Signals of increased MI risk with dabigatran in randomised trials |
| [29801762](https://pubmed.ncbi.nlm.nih.gov/29801762/) | 2018 | Meta-analysis | Int J Cardiol | Critical meta-analysis of over 580,000 patients combining RCTs and real-world studies on dabigatran and MI |
| [27580712](https://pubmed.ncbi.nlm.nih.gov/27580712/) | 2016 | Meta-analysis (observational) | Thromb Haemost | MI and death in AF patients on dabigatran versus VKA |
| [24492353](https://pubmed.ncbi.nlm.nih.gov/24492353/) | 2014 | Review | J Cardiovasc Med | Increased MI risk with dabigatran: fact or fiction? |
| [25644930](https://pubmed.ncbi.nlm.nih.gov/25644930/) | 2015 | Commentary | Chest | Dabigatran and myocardial infarction |
| [38033089](https://pubmed.ncbi.nlm.nih.gov/38033089/) | 2024 | Guideline | Circulation | 2023 ACC/AHA/ACCP/HRS atrial fibrillation guideline |
| [32860058](https://pubmed.ncbi.nlm.nih.gov/32860058/) | 2021 | Guideline | Eur Heart J | 2020 ESC guideline for non-ST-elevation acute coronary syndromes |
| [29957228](https://pubmed.ncbi.nlm.nih.gov/29957228/) | 2018 | Commentary | J Am Coll Cardiol | Direct oral anticoagulants and MI: "the dust is settling" |

Hemoglobinopathy (2 linked, indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37106692](https://pubmed.ncbi.nlm.nih.gov/37106692/) | 2023 | Observational/review (design to be verified) | Biology | NOACs for thromboembolic prophylaxis in transfusion-dependent β-thalassaemia |
| [24449213](https://pubmed.ncbi.nlm.nih.gov/24449213/) | 2014 | Preclinical (mouse) | Blood | Differential roles of FXa and thrombin in vascular inflammation in sickle cell disease mice |

Coronary thrombosis has 20 linked publications, mostly general anticoagulant reviews (for example [35070113](https://pubmed.ncbi.nlm.nih.gov/35070113/), a comprehensive review of dabigatran in cardiovascular disease management), with no coronary-specific efficacy data.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13489Y | Pradaxa | Capsule 150 mg (as mesilate), oral | Not available in the data compiled for this report |

---

## Safety Considerations

Safety data (warnings, contraindications and drug interactions) were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

Relevant points from the literature:
- Bleeding risk is the main concern with any anticoagulant, particularly when combined with antiplatelet therapy.
- A possible increase in MI risk with dabigatran has been reported in some trial meta-analyses, although larger and real-world analyses have generally not confirmed it.
- In mechanical heart valves, dabigatran showed harm (the RE-ALIGN experience), so it should not be extrapolated to other thrombotic settings.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (restricted to atrial fibrillation patients after PCI or ACS; not supported for a general MI indication)

**Rationale:**
- A completed Phase 3 placebo-controlled trial (NCT01661101) and a PCI registry support a role in specific populations, but the MI-risk signal and bleeding risk call for caution. The L1 grade rests on trial existence in the compiled data; the single completed Phase 3 trial would formally meet only L2 under the stated rules, so the evidence is best regarded as moderate. Other predictions (hemoglobinopathy, coronary thrombosis, and the MI anatomical subtypes) should be held as research questions, and the subtypes consolidated under the parent MI entry.

**To proceed, the following is needed:**
- The approved indication text and PI safety data (warnings, contraindications and interactions) from the TGA, as these are currently missing
- Mechanism of action data from DrugBank
- The published results of NCT01661101 and a focused review of dabigatran versus other anticoagulants in AF + PCI
- A bleeding-risk and MI-risk monitoring plan, with attention to renal function and concomitant antiplatelet therapy
- Prospective data in thalassaemia or sickle cell disease before any further consideration of the hemoglobinopathy prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

