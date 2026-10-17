---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metoprolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, acute coronary syndrome, myocardial infarction"
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
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

# Metoprolol: From Hypertension and Myocardial Infarction to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker originally used for hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (top-ranked), but this is a subtype of its existing indication and has no direct supporting evidence.
The most evidence-rich prediction in the data compiled for this report is **chronic pulmonary heart disease** (4 clinical trials, 20 publications), although that evidence is indirect and largely concerns beta-blocker safety in COPD.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, acute coronary syndrome, myocardial infarction (the ARTG entries carry no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension (top-ranked prediction) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (top-ranked prediction); best-supported alternative, chronic pulmonary heart disease, is L2 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, metoprolol is a beta-1 selective adrenergic blocker. It lowers heart rate, myocardial oxygen demand and renin release, and its efficacy in hypertension and myocardial infarction is established.

**Top prediction (malignant renovascular hypertension):** Reduced renin release and blood pressure lowering make this mechanistically plausible. However, it is a subtype of hypertension, already an approved indication, so this is not true repurposing. The only linked paper (PMID 1988765) concerns chromogranin A in diagnosing pheochromocytoma and does not address this condition. The related prediction, malignant hypertensive renal disease (score 99.91%), has no trials or literature at all.

**Other predictions:**
- **Myocardial infarction subtypes** (posteroinferior, posterolateral, septal; scores 99.80–99.84%): These fall within the approved MI indication. Support is limited to small physiological and comparative studies, mostly from the 1980s–2000s.
- **Chronic pulmonary heart disease** (score 99.40%): This is the best-supported prediction, but the evidence is indirect. The relevant question is whether beta-blockers are safe and beneficial in patients with cardiac disease and coexisting COPD, not treatment of cor pulmonale itself. Beta-1 selective blockade appears generally tolerated in COPD, but results are mixed (see below).
- **Pulmonary hypertension (two forms)**: There is no established mechanistic rationale. Beta-blockers are generally avoided or used cautiously in pulmonary arterial hypertension because of possible right ventricular depression.
- **Braddock syndrome and trichotillomania**: No mechanistic link and no evidence. These are purely computational predictions.

---

## Clinical Trial Evidence

Evidence for the top-ranked prediction: currently no related clinical trials registered. The table below covers the best-supported prediction, chronic pulmonary heart disease.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol in heart failure with reduced ejection fraction and COPD; primary outcomes are all-cause death and re-hospitalisation, comparing doses. No results. |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | Randomised, double-blind, placebo-controlled trial of beta-blocker (metoprolol) to prevent COPD exacerbations. Early termination limits conclusions. |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | Carvedilol vs metoprolol respiratory assessment in chronic heart failure. No participants enrolled, so no data. |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | Terminated | 14 | Treatment study in post-COVID exertional dyspnoea and tachycardia. Only tangentially related. |

No ANZCTR trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

The table below covers chronic pulmonary heart disease (the best-supported prediction). Priority is given to RCTs, then reviews and cohorts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | BICS trial of bisoprolol in COPD at high risk of exacerbation. Notes that an earlier trial found metoprolol did not reduce exacerbations and increased those requiring hospital admission. |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction (relevant to the approved MI indication). |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Crossover trial | J Am Coll Cardiol | Beta1-selective vs nonselective beta-blockers in chronic heart failure with COPD: respiratory, haemodynamic and clinical effects. |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Secondary analysis of RCT | Ann Am Thorac Soc | BLOCK COPD analysis: chronotropic index and COPD exacerbations, including susceptibility to metoprolol adverse effects. |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in older patients with heart failure, COPD, diabetes and renal failure (Danish registers). |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Survival effects of carvedilol, bisoprolol and metoprolol in coexistent heart failure and COPD (Taiwan database). |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Review | Expert Rev Respir Med | Practical recommendations for beta-blocker use in COPD. |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Clinical study | Heart Vessels | Metoprolol appeared safe in 50 patients with coronary artery disease and COPD. |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Clinical physiological study | Clin Cardiol | Effects of oral metoprolol on cardiac and pulmonary function in 6 patients with reversible airways obstruction. |
| [3568727](https://pubmed.ncbi.nlm.nih.gov/3568727/) | 1987 | Clinical study | Crit Care Med | Metoprolol for multifocal atrial tachycardia in 11 patients with serious pulmonary disease. |

None of these studies tests metoprolol in pulmonary heart disease itself.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13420H | Metrol-XL 190 | Tablet 190 mg (controlled release) | Not stated in the data compiled |
| ARTG 1324Q | Metoprolol Sandoz | Tablet containing metoprolol tartrate 50 mg | Not stated in the data compiled |

Both entries are valid single-ingredient oral products.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are model-derived associations, not label text) include:
- Cardiometabolic and metabolic: diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, gout and hyperuricaemia, potassium deficiency
- Hepatic and pancreatic: liver disease, hepatic coma/encephalopathy, pancreatitis, gallbladder disease
- Neuromuscular and endocrine: myasthenia gravis and neuromuscular junction disease, phaeochromocytoma, hyperparathyroidism
- Other: systemic lupus erythematosus, psoriasis, anxiety and related disorders, anuria, neonatal jaundice

**Drug interactions:** 100 interactions were identified (DDInter); the 20 reviewed were mostly moderate. Notable moderate interactions include:
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- Epinephrine
- Anticholinergics (atropine, hyoscyamine, glycopyrronium)
- Bupropion, morphine, lorcaserin, cimetidine
- Antidiabetic agents (canagliflozin, dapagliflozin, chlorpropamide)
- Calcium salts

Minor interactions include acetylsalicylic acid and magnesium oxide.

**Indication-specific concern:** beta-blockade may reduce cardiac output and tissue oxygenation under hypoxia (rat study, PMID 19809291). In the BLOCK COPD trial, metoprolol was linked to more COPD exacerbations requiring hospital admission (as cited in PMID 38762800). Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predictions (malignant renovascular hypertension and malignant hypertensive renal disease) are subtypes of an already approved indication, with no supporting trials or relevant literature (L5), so they do not represent genuine repurposing.
- The best-supported prediction, chronic pulmonary heart disease (L2), has only indirect evidence, a terminated Phase 3 trial with a signal of harm in COPD, and an unstarted Phase 4 trial.

**To proceed, the following is needed:**
- Mechanism of action data
- Approved indication text for the ARTG entries, and the PI warnings and contraindications
- Results from NCT06825728 (metoprolol in HFrEF with COPD) and a full analysis of NCT02587351
- Direct studies of metoprolol in pulmonary heart disease
- Clarification of whether MI and hypertension subtype predictions add value beyond the current indications
- A safety monitoring plan for patients with COPD, diabetes or hypotension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

