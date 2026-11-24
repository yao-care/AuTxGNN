---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 724
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Acute coronary syndrome…"
monitor_inn: "Ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
---

# Ticagrelor
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

## Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis
{: .text-alpha }

## One-Sentence Summary

Ticagrelor is an oral antiplatelet drug (a P2Y12 inhibitor), originally used for acute coronary syndrome and peripheral vascular disease.
The TxGNN model predicts it may be useful for **intracranial arteriosclerosis** (narrowing of the arteries inside the brain).
Support so far is early: **2 clinical trials** (one large Phase 3 trial still in progress) and **2 publications**, with no completed outcome trial yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome, peripheral arterial disease and intermittent claudication (the registered label text was not available in the data compiled for this report) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (observational cohort data only; the one Phase 3 trial is still ongoing) |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ticagrelor: "Ticagrelor and its major metabolite reversibly interact with the platelet P2Y 12 ADP-receptor to prevent signal transduction and platelet activation. Ticagrelor and its active metabolite are approximately equipotent." ([DailyMed: Brilinta (ticagrelor) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7b3f443-e83d-4bf2-0e96-023448fed9a8), label version 2026-05-07; accessed 2026-11-19.) Based on known pharmacology, ticagrelor is a reversible blocker of the platelet P2Y12 receptor and reduces platelet aggregation. Its efficacy in coronary and peripheral arterial disease is established, and it may be applicable to intracranial arteriosclerosis.

Intracranial atherosclerotic stenosis causes stroke largely through platelet-rich clots forming on narrowed arteries and through small clots breaking off and travelling downstream. Stronger P2Y12 inhibition is therefore biologically plausible. Ticagrelor also does not depend on CYP2C19 enzyme activity, unlike clopidogrel. This may matter in populations where many people carry loss-of-function gene variants and respond poorly to clopidogrel.

The case is still limited by thin evidence and by bleeding risk. The evidence consists of one ongoing large trial, one small pilot study and a single observational cohort. Any benefit has to be weighed against bleeding, including intracranial haemorrhage, which is listed as a contraindication signal for this drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | Active, not recruiting | 1683 | Tests whether rivaroxaban, ticagrelor or both are better than clopidogrel at lowering 1-year ischaemic stroke, intracerebral haemorrhage or vascular death in intracranial atherostenosis. Ticagrelor is not the only experimental agent, and no results have been reported. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Not applicable (pilot) | Recruiting | 100 | Pilot trial of genotype-guided P2Y12 inhibitor selection (including ticagrelor) versus standard clopidogrel in symptomatic intracranial atherosclerotic disease. Small, so statistical power is low, and no results yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Reports experience with ticagrelor 60 mg twice daily plus aspirin 81 mg, compared with standard aspirin and clopidogrel, for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design paper | Int J Stroke | Describes the design and early progress of CAPTIVA. Standard treatment is clopidogrel plus aspirin for 90 days, but recurrent stroke risk stays high for up to 12 months. |

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1418P | ARX-TICAGRELOR | Ticagrelor | Tablet 90 mg | Valid |
| 13524T | ARX-TICAGRELOR | Ticagrelor | Tablet 90 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindication signals** (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence): liver failure, liver disease, gallbladder disease and intracranial haemorrhage.
- **Drug Interactions** (100 interactions were identified; main examples below):
  - **Major:** clarithromycin.
  - **Moderate:** acetylsalicylic acid (aspirin), morphine, simvastatin, dexamethasone, budesonide, aprepitant, miconazole and saxagliptin, among others.
  - **Minor:** naloxegol and prucalopride.

Morphine is relevant in acute settings because it can delay absorption of oral ticagrelor. Please also refer to the TGA-approved Product Information (PI) for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but the only large trial (CAPTIVA) has not reported results and does not test ticagrelor alone. The other evidence is a small pilot and a single observational cohort. Bleeding risk, particularly intracranial haemorrhage, is a real concern in this population.

Separately, ticagrelor has stronger trial support in related ischaemic settings (for example, after PCI and in stroke/TIA). These sit outside this specific prediction and would be assessed as a different indication.

**To proceed, the following is needed:**
- CAPTIVA results (expected after its January 2027 completion date) showing ticagrelor performance against clopidogrel
- Results from the genotype-guided pilot trial and larger randomised data in intracranial disease
- Detailed mechanism of action data
- Warnings and contraindications from the TGA-approved Product Information, to support a formal safety screen
- A bleeding-risk plan covering patient selection, regimen (with or without aspirin) and treatment duration

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Brilinta (ticagrelor) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7b3f443-e83d-4bf2-0e96-023448fed9a8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

