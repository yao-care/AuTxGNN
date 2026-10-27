---
layout: default
title: Nebivolol
parent: Model Prediction Only (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nebivolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder). The ARTG entry in the data comp…"
monitor_inn: "Nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina", "ocular tuberculosis", "congenital temporomandibular joint ankylosis", "polydipsia"]
---

# Nebivolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Nebivolol: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Nebivolol is a third-generation beta-blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials** and **no publications** currently support this specific prediction.
The score most likely reflects its similarity to the already-approved hypertension indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The ARTG entry in the data compiled for this report has no approved indication text, so this is taken from the knowledge-graph indication data. |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, nebivolol is a highly beta-1-selective blocker that also promotes nitric oxide-mediated vasodilation. Its efficacy in hypertension is established.

Malignant renovascular hypertension is driven largely by activation of the renin-angiotensin system. Beta-1 blockade reduces renin release, so a benefit is plausible in theory. However, the prediction score is probably inflated by the close similarity between this condition and nebivolol's approved indication. No trial or publication was found that tests nebivolol in this setting.

**Other predicted indications (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 99.42% | L5 | Theoretical blood pressure-lowering benefit. Rodent renoprotection data come from other indications. |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.39% | L4 | Only indirect preclinical and beta-blocker safety literature. Beta-blockers are generally not recommended in pulmonary arterial hypertension, so a safety signal must be excluded first. |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 99.39% | L5 | No evidence. Risk of reduced right ventricular output. |
| 5 | Braddock syndrome | 99.14% | L5 | No identifiable mechanistic link. Likely a graph artefact. |
| 6 | Chronic pulmonary heart disease | 91.85% | L3 | Adjacent evidence only (heart failure with COPD). No evidence of efficacy in cor pulmonale itself. |
| 7 | Prinzmetal angina | 87.48% | L4 | Plausible NO-mediated action, but vasospasm safety is unestablished. |
| 8-10 | Ocular tuberculosis, congenital TMJ ankylosis, polydipsia | 62.7-65.5% | L5 | No plausible mechanistic link or evidence. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

For context, trials were found for other predicted indications:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Nebivolol vs bisoprolol vs carvedilol in heart failure: effects on exercise capacity, hypoxia, chemoreceptor response and pulmonary function. Relevant to chronic pulmonary heart disease only indirectly. |
| [NCT06424834](https://clinicaltrials.gov/study/NCT06424834) | Phase 2/3 | Recruiting | 150 | Targeted medical therapy vs placebo for angina with non-obstructive coronary arteries (MVP-ANOCA). It is unclear whether nebivolol is an arm, and no results are available. Indirect relevance to Prinzmetal angina. |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

No literature is available for malignant renovascular hypertension. The most relevant publications found for other predicted indications are below (all indirect).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Randomised comparative study | Int J Cardiol | CARNEBI: carvedilol vs nebivolol vs bisoprolol in moderate heart failure. |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | RCT | Cardiovasc Ther | Nebivolol vs carvedilol on exercise performance at high altitude in healthy subjects. |
| [15031571](https://pubmed.ncbi.nlm.nih.gov/15031571/) | 2004 | Clinical study | Respiration | Nebivolol vs nifedipine over two weeks in hypertensive patients with COPD. |
| [21516766](https://pubmed.ncbi.nlm.nih.gov/21516766/) | 2011 | Clinical study | Klin Med | Nebivolol in coronary heart disease with COPD (n=50): lowered blood pressure and heart rate, with no adverse effect on bronchial patency. |
| [19815121](https://pubmed.ncbi.nlm.nih.gov/19815121/) | 2009 | Review | J Am Coll Cardiol | Nebivolol as a third-generation beta-blocker with endothelial NO-mediated effects. |
| [30426333](https://pubmed.ncbi.nlm.nih.gov/30426333/) | 2018 | Review | Drugs | Nebivolol and its fixed-dose combinations in hypertension. |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | Eur J Heart Fail | Beta-blocker use in heart failure with concurrent COPD in Denmark. |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclinical (animal) | Pharmacol Rep | Renal protective effect of nebivolol in rat acute renal injury models. |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclinical (animal) | Can J Physiol Pharmacol | Nebivolol protected against methotrexate nephrotoxicity in rats. |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclinical (animal) | Drug Chem Toxicol | Nebivolol alleviated methotrexate liver damage in rats. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13441K | APO-Nebivolol | Tablet 10 mg (as hydrochloride) | Not stated in the data compiled for this report |

Only the oral route is available (tablet).

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for label safety information.

**Knowledge-graph contraindication signals** (not label text) include:
- Liver failure, liver disease, gallbladder disease
- Diabetes mellitus, diabetic ketoacidosis, hypoglycaemia
- Peripheral vascular disease, intermittent claudication, peripheral arterial disease
- Atrioventricular block, sick sinus syndrome (including familial)
- Bronchial disease

**Drug interactions:** 100 interactions were identified in the data compiled for this report. The main ones listed are mostly Moderate:
- Epinephrine, morphine, bupropion, lorcaserin
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
- Anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine)
- Antidiabetics (canagliflozin, dapagliflozin, chlorpropamide)
- Calcium acetate and calcium phosphate

Minor interactions include acetylsalicylic acid and magnesium oxide.

**Indication-specific cautions:** In pulmonary hypertension, beta-blockade may reduce right ventricular output. In vasospastic angina, the safety of nebivolol is unestablished.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant renovascular hypertension rests on model score alone (L5), with no trials or publications. The score is likely inflated by similarity to nebivolol's approved hypertension indication.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- TGA Product Information warnings and contraindications (a blocking gap for safety screening)
- Targeted literature review on beta-blockers in renovascular and malignant hypertension
- Clinical evidence (observational or trial) in the predicted indication
- For pulmonary hypertension and Prinzmetal angina, a safety assessment before any further work
- Clarification of the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

