---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 9
monitor_inn: "Magnesium sulfate"
predicted_indications: ["toxemia of pregnancy", "thrombotic disease", "pharyngitis", "nasal cavity disease", "psychotic disorder", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "treatment-refractory schizophrenia"]
last_modified_at: 2026-10-30
description: "Magnesium Sulfate: predicted new indication Toxemia of pregnancy (evidence level L5). Approved use: Not recorded in the local data"
---

# Magnesium Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Magnesium Sulfate: Toxemia of pregnancy
{: .text-alpha }

## One-Sentence Summary

Magnesium sulfate is a long-established drug, and the knowledge graph records constipation disorder and pre-eclampsia (mild and severe) as its known uses.
The TxGNN model predicts it for **toxemia of pregnancy**, which is the older term for pre-eclampsia, so this is largely a confirmation of existing practice rather than a new indication.
The prediction is supported by **30 registered clinical trials** and **20 publications**. Most of the trial evidence concerns dosing, duration and special populations rather than whether the drug works at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Toxemia of pregnancy |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Mechanisms proposed in the literature for seizure prevention include NMDA receptor antagonism, cerebral vasodilation and calcium channel blockade. These are not confirmed by the data compiled for this report.

The predicted condition closely overlaps with the pre-eclampsia entries already recorded for magnesium sulfate in the knowledge graph. The model's high score therefore largely reflects relationships it has already seen. Reviews in the literature describe magnesium sulfate as the standard agent for preventing eclamptic seizures. One review reports it is significantly better than diazepam or phenytoin at preventing recurrent seizures in eclampsia.

Because the use is already well established, the open questions are practical ones: the right dose, how long to continue after delivery, and how to dose patients with obesity or reduced kidney function.

---

## Clinical Trial Evidence

The data compiled for this report lists 30 trials. The 10 most relevant are shown below. No results were provided, so the findings column describes each trial's question rather than its outcome. No ANZCTR identifiers were available.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Postpartum magnesium sulfate for 6 vs 24 hours in severe pre-eclampsia after less than 8 hours of pre-delivery treatment |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | 24 hours of postpartum magnesium sulfate vs none, after more than 8 hours of treatment before delivery |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | 1 g vs 2 g intravenous maintenance dose in severe pre-eclampsia |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | Not specified | Completed | 114 | Low-dose regimen vs standard Pritchard regimen for severe pre-eclampsia/eclampsia |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | Not specified | Completed | 2000 | Nimodipine vs magnesium sulfate for preventing eclamptic seizures in severe pre-eclampsia |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | Unknown | 100 | Alternate dosing protocol in overweight and obese women with pre-eclampsia |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuing vs stopping magnesium sulfate after delivery in severe pre-eclampsia |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | Terminated | 62 | 1 g/h vs 2 g/h maintenance dose for eclampsia prevention (stopped early) |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Short-course postpartum magnesium sulfate prophylaxis in severe pre-eclampsia |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat-bolus regimen by Springfusor pump vs continuous infusion: serum levels and outcomes |

A Phase 3 trial comparing levetiracetam with magnesium sulfate for eclampsia prevention (NCT07220902, n=1240) is planned but not yet recruiting.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertension | Magnesium sulfate is well established for eclampsia and recommended in pre-eclampsia with severe features, yet many clinicians remain unconfident using it |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | Intravenous and intramuscular regimens are both effective; regimens can be tailored for low-resource settings and different patients |
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | Eclampsia incidence and outcomes differ widely between high- and low-resource countries |
| [37467840](https://pubmed.ncbi.nlm.nih.gov/37467840/) | 2023 | Review | Am J Obstet Gynecol | Magnesium sulfate reduces eclamptic seizure risk, but no studies address late postpartum severe hypertension alone |
| [38574215](https://pubmed.ncbi.nlm.nih.gov/38574215/) | 2024 | Review | Am Fam Physician | Overview of hypertensive disorders of pregnancy, including pre-eclampsia and eclampsia |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | Review | Drug Safety | Magnesium sulfate is significantly better than diazepam or phenytoin for preventing recurrent seizures in eclampsia |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | Pharmacokinetic principles and standard intravenous and intramuscular regimens for eclampsia |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | Pharmacokinetic study | BMC Pregnancy Childbirth | Population pharmacokinetics and dose optimisation in a Chinese pre-eclampsia population |
| [32642964](https://pubmed.ncbi.nlm.nih.gov/32642964/) | 2020 | Pharmacokinetic study | Drugs R D | Population pharmacokinetic model and factors affecting magnesium levels in pre-eclampsia |
| [24915961](https://pubmed.ncbi.nlm.nih.gov/24915961/) | 2014 | Review | Curr Hypertens Rep | Update on pathogenesis, diagnosis, prevention and management of pre-eclampsia |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 307E (licence number as recorded) | Not specified | Not specified | Not specified in the licence record |

This is a single-ingredient licence with valid status. No approved indication text is available in the licence record, so approved use in Australia cannot be confirmed from the data compiled for this report.

---

## Safety Considerations

No warning or contraindication text from product labelling is available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

- **Contraindication relations in the knowledge graph** (these are knowledge-graph relations, not label text): kidney disease, pyoureter, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, chronic diarrheal disease, appendicitis, atrioventricular block, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita and gastroparesis.
- **Drug interactions:** 92 interactions were found. Major-level interactions include dolutegravir, amikacin and bictegravir. Moderate-level interactions include nifedipine (often used alongside magnesium sulfate in pre-eclampsia), amlodipine, cisatracurium, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), tetracyclines, ciprofloxacin, bisphosphonates and vitamin D analogues.
- **Monitoring:** The trial literature highlights magnesium toxicity risk, particularly with kidney impairment, obesity or prolonged postpartum use. Two trials also looked at interactions with neuromuscular blockade reversal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Magnesium sulfate is already the standard seizure prophylaxis for pre-eclampsia and eclampsia, and two completed Phase 2/3 trials plus several Phase 4 trials directly study it in severe pre-eclampsia. Because no Phase 3 trial has completed, the evidence level is L2. The remaining uncertainty is about dosing, duration and toxicity monitoring, not whether the drug works.

**To proceed, the following is needed:**
- Confirmation of the approved Australian indication, dosage forms and product details from the ARTG record and TGA Product Information
- Published results of the Phase 2/3 duration trials (NCT02317146, NCT02307201) to settle postpartum duration
- A monitoring plan for magnesium toxicity, especially in kidney impairment, obesity and with interacting drugs such as nifedipine
- Mechanism of action data for the drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

