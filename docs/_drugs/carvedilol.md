---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Carvedilol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "obsolete susceptibility to ischemic stroke", "cerebrovascular disorder", "ocular tuberculosis", "brain stem infarction"]
---

# Carvedilol
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

## Carvedilol: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Carvedilol is a beta/alpha-1 blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials and no publications** currently support this specific prediction (evidence is model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; no approved-indication text is recorded on the Australian licence entry) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carvedilol combines non-selective beta-blockade with alpha-1 blockade and vasodilation, and its blood-pressure-lowering effect is established in hypertension.

Malignant renovascular hypertension is a severe form of hypertension. The link to the original indication is therefore plausible in terms of blood pressure control. However, this condition is driven largely by activation of the renin-angiotensin system, so a beta/alpha blocker is not an obvious first-line mechanistic fit.

The very high TxGNN score most likely reflects the closeness of this disease to the approved hypertension indication in the knowledge graph, not independent evidence of benefit. The same score and reasoning apply to the closely related prediction, malignant hypertensive renal disease (99.55%, L5, also Hold).

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

For context, trials exist for other lower-ranked predictions, but they do not test this indication:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Nebivolol vs bisoprolol vs carvedilol in heart failure: exercise capacity, hypoxia, chemoreceptor response and pulmonary function (relevant to chronic pulmonary heart disease, rank 6) |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | CAMERA: carvedilol vs metoprolol respiratory effects in heart failure; no data |
| [NCT00741585](https://clinicaltrials.gov/study/NCT00741585) | Phase 4 | Completed | 21,983 | HYGIA: prognostic value of circadian ambulatory blood pressure pattern; not carvedilol-specific (cerebrovascular disorder, rank 8) |

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

Selected publications for other predicted indications (indirect context only):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17336720](https://pubmed.ncbi.nlm.nih.gov/17336720/) | 2007 | RCT post-hoc (COMET) | J Am Coll Cardiol | Carvedilol protected better against vascular events than metoprolol in heart failure |
| [22015086](https://pubmed.ncbi.nlm.nih.gov/22015086/) | 2011 | Randomised trial | Respir Med | Bisoprolol vs carvedilol in chronic heart failure with COPD |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised crossover trial | J Am Coll Cardiol | Respiratory, haemodynamic and clinical effects of switching between beta-blockers in heart failure with COPD |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in older patients with heart failure, COPD, diabetes and renal failure |
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Preclinical (animal) | Eur J Pharmacol | Carvedilol reversed hypertension induced by chronic intermittent hypoxia in rats |
| [10950380](https://pubmed.ncbi.nlm.nih.gov/10950380/) | 2000 | Preclinical (animal) | J Cereb Blood Flow Metab | Carvedilol provided neuroprotection in transient focal stroke |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 13387N | Dilatrend 25 | Tablet 25 mg (oral) | Not recorded in the data compiled |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** liver failure, asthma (including intrinsic and allergic), bronchitis, bronchial disease, pulmonary emphysema, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), atrioventricular block, sick sinus syndrome (including familial), Prinzmetal angina, anaphylaxis, intraoperative floppy iris syndrome.
- **Drug Interactions:** 100 interactions were identified; the first 20 retrieved are summarised here.
  - **Major:** epinephrine.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), hyoscyamine, atropine, bupropion, morphine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate).
  - **Minor:** acetylsalicylic acid, aluminium hydroxide, attapulgite.
- For pulmonary hypertension predictions, beta-blockade carries a theoretical risk of reduced cardiac output and right ventricular function.

Please also refer to the TGA-approved Product Information (PI) for full warnings, as label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). No trials or publications address malignant renovascular hypertension, and the score likely reflects proximity to the approved hypertension indication. The mechanism is also questionable, since this condition is driven largely by renin-angiotensin activation.

**To proceed, the following is needed:**
- Mechanism of action data for carvedilol
- Label warnings and contraindications from the TGA Product Information, plus the approved indication text for the Australian entry
- A targeted literature and trial search for carvedilol in malignant or renovascular hypertension
- Comparison against established treatments for this condition
- Of the other predictions, chronic pulmonary heart disease (L3) and cerebrovascular disorder (L4) have more supporting material, but this is mainly tolerability or preclinical data, so both would remain research questions rather than candidates for adoption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

