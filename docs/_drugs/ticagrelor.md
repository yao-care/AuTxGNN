---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Acute coronary syndrome…"
monitor_inn: "Ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "ischemic disease", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

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
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 (observational cohort data only; the one Phase 3 trial is still ongoing) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible blocker of the platelet P2Y12 receptor and reduces platelet aggregation. Its efficacy in coronary and peripheral arterial disease is established, and it may be applicable to intracranial arteriosclerosis.

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

| Licence Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13524T | ARX-TICAGRELOR | Tablet 90 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Contraindication signals** (from knowledge-graph associations, not label text): liver failure, liver disease, gallbladder disease and intracranial haemorrhage.
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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

