---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 776
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
monitor_inn: "Verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Verapamil: Obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker, originally used for hypertension, atrial fibrillation, angina and ventricular tachycardia.
The TxGNN model's top-ranked prediction is **obsolete bundle branch block**, but the best-supported candidate in the data compiled for this report is **arrhythmogenic right ventricular cardiomyopathy (ARVC)**.
There are **no registered clinical trials** and only **indirect literature** for any candidate, so the evidence is limited to model prediction and background literature.

> The top-ranked prediction by TxGNN score is "obsolete bundle branch block". All other candidates are summarised in the table that follows.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication (top-ranked) | Obsolete bundle branch block |
| TxGNN Prediction Score (top-ranked) | 0.9962 |
| Most Evidence-Supported Candidate | Arrhythmogenic right ventricular cardiomyopathy (score 98.40%) |
| Evidence Level | L5 for the top-ranked prediction; L4 for ARVC |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold (top-ranked prediction); Research Question (ARVC) |

### All Candidates at a Glance

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Obsolete bundle branch block | 0.9962 | L5 | Hold |
| 2 | Malignant hypertensive renal disease | 0.9927 | L5 | Hold |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9926 | L5 | Hold |
| 5 | Pulmonary hypertension with unclear multifactorial mechanism | 0.9926 | L5 | Hold |
| 6 | Braddock syndrome | 0.9915 | L5 | Hold |
| 7 | Periodic paralysis with transient compartment-like syndrome | 0.9908 | L5 | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, verapamil is an L-type calcium channel blocker. It slows atrioventricular (AV) nodal conduction and relaxes arterial smooth muscle, which underlies its use in hypertension, supraventricular arrhythmias and angina.

**Top-ranked prediction (bundle branch block):** The mechanistic link is weak. Bundle branch block is an infranodal conduction defect, and slowing conduction could make it worse. The disease term is also marked obsolete in the ontology. The high TxGNN score therefore looks like a model artefact rather than a credible new use.

Standard care includes beta-blockers, sotalol, amiodarone and ablation, and verapamil's negative inotropic effect is a concern in cardiomyopathy.

**Other candidates:** The hypertension-related predictions (ranks 2 and 3) are plausible because verapamil lowers blood pressure, but they are managed with other agents in practice. The pulmonary hypertension predictions (ranks 4 and 5) have a plausible vasodilatory rationale, but calcium channel blockers are not recommended for these groups and negative inotropy is a concern with right heart dysfunction. Ranks 6 to 8 and 10 have no clear mechanistic rationale or only a symptomatic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

## Literature Evidence


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24827485](https://pubmed.ncbi.nlm.nih.gov/24827485/) | 2014 | Case report | Intern Med | Verapamil-sensitive fascicular ventricular tachycardia in a patient with isolated left ventricular noncompaction |
| [18375968](https://pubmed.ncbi.nlm.nih.gov/18375968/) | 2008 | Case report | Europace | Electrical storm in a patient with ARVC and an SCN5A mutation |
| [15475817](https://pubmed.ncbi.nlm.nih.gov/15475817/) | 2004 | Review | AACN Clin Issues | Diagnosis and treatment of idiopathic ventricular tachycardia |
| [11729615](https://pubmed.ncbi.nlm.nih.gov/11729615/) | 2001 | Review | Lijec Vjesn | Current management of ventricular tachycardia |
| [8869252](https://pubmed.ncbi.nlm.nih.gov/8869252/) | 1996 | Review | Arch Mal Coeur Vaiss | Idiopathic monomorphic ventricular tachycardia |
| [8846953](https://pubmed.ncbi.nlm.nih.gov/8846953/) | 1995 | Review | Harefuah | Arrhythmogenic right ventricular dysplasia: clinical description of a case and overview |
| [8213549](https://pubmed.ncbi.nlm.nih.gov/8213549/) | 1993 | Cohort | Am J Cardiol | Reentry with an excitable gap in sustained VT unrelated to coronary artery disease, including ARVD patients |
| [7884360](https://pubmed.ncbi.nlm.nih.gov/7884360/) | 1994 | Cohort | J Electrocardiol | Signal-averaged ECG in patients with VT, including ARVD and verapamil-sensitive left ventricular tachycardia |

For pulmonary hypertension due to lung disease or hypoxia (rank 4), the most relevant paper is a 1985 review, [PMID 3881914](https://pubmed.ncbi.nlm.nih.gov/3881914/) (Packer, Am J Cardiol), on calcium-channel antagonists for pulmonary hypertension. The remaining papers retrieved for that candidate are mostly preclinical or unrelated.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1241H | Cordilox SR | Tablet containing verapamil hydrochloride 240 mg (sustained release), oral | Not available in the data compiled for this report |

## Safety Considerations

- These come from knowledge graph edges and should be checked against the approved Product Information.
- **Drug Interactions (100 interactions recorded; examples):**
  - **Major:** Loperamide.
  - **Moderate:** Clarithromycin, cimetidine, aprepitant, bupropion, metformin, canagliflozin, acetylsalicylic acid, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone) and calcium salts.
  - **Minor:** Morphine.

For authoritative warnings and precautions, refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps


**Rationale:**
- The model's top-ranked prediction (bundle branch block) has no supporting evidence and a mechanistic rationale that suggests possible harm. No candidate has clinical trial support, and the literature is indirect, so none supports a change in practice.

**To proceed, the following is needed:**
- Mechanism of action data for verapamil
- TGA Product Information (warnings, contraindications and approved indication text for Cordilox SR), which was not available for this report
- A comparison against standard therapies (beta-blockers, sotalol, amiodarone, ablation)
- Safety assessment for cardiomyopathy populations, particularly regarding negative inotropy, heart failure and AV block
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

