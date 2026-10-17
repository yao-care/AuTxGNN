---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Magnesium Sulfate: predicted new indication Preeclampsia/eclampsia (evidence level L5). Approved use: Constipation disorder"
monitor_inn: "Magnesium sulfate"
predicted_indications: ["thrombotic disease"]
---

# Magnesium Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Magnesium Sulfate: From Constipation and Pre-eclampsia to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate is a long-established medicine, originally used for constipation and pre-eclampsia. The TxGNN model's top prediction is **preeclampsia/eclampsia**, which is already a recognised use, so this is better read as validation of an existing indication than as true repurposing. The data compiled for this report include **29 clinical trials** and **20 publications** for this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder; severe pre-eclampsia; pre-eclampsia; mild pre-eclampsia (from the TxGNN knowledge graph, as no approved indication text is available for the Australian licence) |
| Predicted New Indication | Preeclampsia/eclampsia |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 (as assigned in the compiled data) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

Two further predictions appear in the data: "toxemia of pregnancy" (99.998%) and "thrombotic disease" (99.905%). They are discussed briefly at the end of the report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the sources compiled for this report. Based on general pharmacology and the cited literature, magnesium is thought to reduce seizure risk in preeclampsia by:

- Antagonising NMDA receptors (central anticonvulsant effect; see PMID 1566765)
- Causing cerebral vasodilation and opposing calcium-dependent arterial constriction (PMID 2672428, PMID 16978425)
- Protecting the blood-brain barrier

The original indications already include pre-eclampsia, so the predicted indication is essentially the same disease spectrum (including the convulsive form, eclampsia). The prediction is therefore highly plausible. Reviews describe magnesium sulfate as the drug of choice for preventing and controlling eclamptic seizures, and it proved superior to diazepam and phenytoin in preventing recurrent seizures in eclampsia (PMID 8879973).

---

## Clinical Trial Evidence

The table lists the most relevant trials (up to 10), selected by direct relevance to magnesium sulfate in preeclampsia/eclampsia.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | 6 vs 24 hours of postpartum magnesium sulfate in severe preeclampsia after under 8 hours of pre-delivery treatment |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1,114 | Postpartum magnesium sulfate vs none in severe preeclampsia treated for more than 8 hours before delivery |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | 1 g vs 2 g intravenous maintenance dose in severe pre-eclampsia (efficacy and safety) |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2,000 | Nimodipine vs magnesium sulfate for preventing eclamptic seizures in severe preeclampsia |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | Completed | 114 | Low-dose regimen vs standard Pritchard regimen in severe preeclampsia/eclampsia |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat bolus (Springfusor pump) vs continuous infusion: serum magnesium levels and clinical outcomes |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Short-course postpartum magnesium sulfate prophylaxis in severe preeclampsia |
| [NCT00344058](https://clinicaltrials.gov/study/NCT00344058) | N/A | Completed | 200 | 12 vs 24 hour postpartum regimens in preeclampsia |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuing vs stopping magnesium sulfate after delivery in severe preeclampsia |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | Not yet recruiting | 1,240 | LEVMag trial: levetiracetam vs magnesium sulfate for eclamptic seizure prevention (equivalence design) |

Most of these trials address dosing and duration rather than whether the drug works at all. Further dosing trials in obese women are also listed (for example NCT06486025, NCT02835339, NCT03661775). No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | Review of efficacy, benefits and risks of magnesium sulfate seizure prophylaxis |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | Magnesium sulfate described as the ideal anticonvulsant; efficacy and safety documented over about 60 years |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | Review | Drug Saf | Better than diazepam or phenytoin for preventing recurrent seizures in eclampsia |
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertens | Established role in eclampsia; broad indications in preeclampsia beyond neurological symptoms |
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | Eclampsia in the 21st century: incidence and outcomes |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | Regimens in high-income and low/middle-income countries |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | Pharmacokinetic principles of IV and IM regimens |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | Population PK study | BMC Pregnancy Childbirth | Population pharmacokinetics and dose optimisation in a Chinese preeclampsia population |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | Cerebral hemodynamics in preeclampsia and the rationale for an alternative to magnesium sulfate |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | Preclinical | Am J Obstet Gynecol | Central anticonvulsant effects on hippocampal seizures |

The data compiled for this report did not include a randomised trial publication for this indication. The literature is mainly reviews and pharmacology studies.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 307E | Not available | Not available | Not available |

The licence is recorded as a valid single-ingredient product, but product name, dosage form, manufacturer and approved indication text were not available in the data compiled for this report. Check the ARTG entry directly.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): kidney disease, pyoureter, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, chronic diarrhoeal disease, appendicitis, atrioventricular block, hyperkalaemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita and gastroparesis.
- **Drug interactions**: 92 interactions were recorded. Major interactions include dolutegravir, amikacin and bictegravir. Moderate interactions include nifedipine, amlodipine, doxycycline, tetracycline, ciprofloxacin, cisatracurium, bisphosphonates (alendronic acid, risedronic acid, ibandronate), vitamin D analogues and corticosteroids. The calcium channel blocker and neuromuscular blocker interactions matter in obstetric practice, and trials in the data also examine magnesium's effect on sugammadex reversal of rocuronium.
- **Monitoring suggested by the evidence**: reflexes, respiratory rate and urine output for magnesium toxicity; serum magnesium where available; dose adjustment in renal impairment and obesity.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications, as these were not available in the data compiled for this report.

---

## Other Predictions in the Data

- **Toxemia of pregnancy** is an older term for preeclampsia/eclampsia. It draws on largely the same trials, so it is not independent evidence and should not be counted twice.
- **Thrombotic disease** has weak support. The only trial is NCT03237819 (Phase 3, n=74, status unknown, no results) in thrombotic thrombocytopenic purpura, which is a specific microangiopathy rather than thrombosis in general. Supporting studies are older animal experiments, and much of the retrieved literature is off-target. The compiled data classify this as L3 and a research question, not a candidate for use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Magnesium sulfate is already an established, guideline-endorsed treatment for seizure prevention in severe preeclampsia and eclampsia. The trial base is large, although it concentrates on dosing and duration.
- The "new" indication largely duplicates the original one, so the main questions are regimen optimisation and safe use, not whether the drug works.

**To proceed, the following is needed:**
- Confirm the ARTG entry details (product, dosage form, approved indication) and the PI warnings and contraindications
- Confirm the mechanism of action from an authoritative source such as DrugBank
- Establish a toxicity monitoring plan (reflexes, respiratory rate, urine output, serum magnesium)
- Provide dosing guidance for renal impairment and obesity
- Review the interaction list against local practice (calcium channel blockers, neuromuscular blockers, aminoglycosides)
- Do not pursue thrombotic disease without results from NCT03237819 and a clearly defined indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

