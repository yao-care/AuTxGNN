---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bisoprolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder). The Australian licence record h…"
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "Prinzmetal angina", "obsolete susceptibility to ischemic stroke", "brain stem infarction", "cerebrovascular disorder"]
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Bisoprolol is a cardioselective beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials or publications** currently support this specific prediction.
The best-supported alternative signal in the data is **chronic pulmonary heart disease** (3 trials, 20 publications), which is discussed below as a secondary finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The Australian licence record has no approved indication text. |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, bisoprolol is a beta-1 selective blocker. Blocking beta-1 receptors lowers heart rate and cardiac output and reduces renin release from the kidney. Reduced renin release is plausible in renovascular hypertension, where renin activation drives blood pressure.

Malignant renovascular hypertension is a severe form of the condition for which bisoprolol is already used. The high TxGNN score probably reflects closeness to the existing hypertension indication rather than independent evidence. Malignant hypertension is usually managed with acute, titratable parenteral agents, not oral bisoprolol, so practical applicability is doubtful.

Other predictions in the data share the same limits:
- **Malignant hypertensive renal disease** (99.94%): same reasoning, no evidence provided.
- **Pulmonary hypertension** (99.93%): the link to systemic antihypertensive action is weak, and beta-blockers are approached cautiously in pulmonary arterial hypertension because of concern about right ventricular function.
- **Chronic pulmonary heart disease** (98.63%): the only prediction with Phase 3 trial evidence (see below).

---

## Clinical Trial Evidence

No clinical trials are registered for malignant renovascular hypertension. Currently no related clinical trials registered.

For reference, the best-supported secondary prediction, **chronic pulmonary heart disease**, has the following trials. All involve heart failure or COPD populations rather than pulmonary heart disease directly.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03917914](https://clinicaltrials.gov/study/NCT03917914) | Phase 3 | Completed | 280 | Double-blind RCT of proactive cardiac risk treatment (bisoprolol vs placebo) in COPD (PACE trial); results not provided in the data |
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Nebivolol vs bisoprolol vs carvedilol in heart failure: exercise capacity, hypoxia, chemoreceptor response and lung function |
| [NCT00702156](https://clinicaltrials.gov/study/NCT00702156) | Phase 2 | Terminated | 27 | Bisoprolol vs placebo in heart failure with moderate to severe COPD; underpowered and inconclusive |

For **Prinzmetal angina**, one Phase 4 trial exists:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05294887](https://clinicaltrials.gov/study/NCT05294887) | Phase 4 | Unknown | 132 | Crossover trial of bisoprolol and diltiazem in symptomatic patients with non-obstructed coronary arteries; no results provided |

No ANZCTR identifiers were available in the data.

---

## Literature Evidence

No publications address malignant renovascular hypertension. Currently no related literature available.

For the secondary prediction (chronic pulmonary heart disease), the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | BICS trial: bisoprolol in COPD patients at high risk of exacerbation |
| [40386836](https://pubmed.ncbi.nlm.nih.gov/40386836/) | 2025 | RCT | Health Technol Assess | BICS trial full report (bisoprolol in COPD) |
| [38152590](https://pubmed.ncbi.nlm.nih.gov/38152590/) | 2023 | Systematic review/meta-analysis | Int J Chron Obstruct Pulmon Dis | Efficacy and safety of bisoprolol in COPD |
| [19460848](https://pubmed.ncbi.nlm.nih.gov/19460848/) | 2009 | RCT | Eur J Heart Fail | Bisoprolol in heart failure with moderate to severe COPD |
| [22015086](https://pubmed.ncbi.nlm.nih.gov/22015086/) | 2011 | RCT | Respir Med | Bisoprolol vs carvedilol in chronic heart failure with COPD |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction (indirect) |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Carvedilol, bisoprolol and metoprolol in coexistent heart failure and COPD (Taiwan national database) |
| [38597065](https://pubmed.ncbi.nlm.nih.gov/38597065/) | 2024 | Review | Curr Med Res Opin | Pharmacological differences between beta-blockers |

The data provided do not show the direction of effect in the BICS trial, so outcome results should be reviewed directly before drawing any conclusion.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13419G | Bisoprolol generichealth | Tablet containing bisoprolol fumarate 2.5 mg (oral) | Not stated in the data |

---

## Safety Considerations

No label warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Disease-level cautions from the knowledge graph** (not label text): the graph links bisoprolol to cautions or contraindications in asthma (including allergic and intrinsic asthma), diabetes mellitus and diabetic ketoacidosis, kidney disease, liver disease, hepatic encephalopathy, anuria, myasthenia gravis, psoriasis, systemic lupus erythematosus, gout, pancreatitis, gallbladder disease, anxiety and related mood disorders, and several metabolic conditions (potassium deficiency, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease). These should be checked against the PI.
- **Drug interactions**: 100 interactions were identified; the first 20 retrieved are mostly Moderate, with a few Minor. Moderate examples include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, acetohexamide and calcium salts. Minor examples include aspirin, aluminium hydroxide and attapulgite.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The lead prediction, malignant renovascular hypertension, is supported only by a model score (L5), with no trials or literature. Oral bisoprolol is also not the usual approach for malignant hypertension.
- The only prediction with substantive evidence is chronic pulmonary heart disease (L1 by the Phase 3 rule, but the studies are in COPD and heart failure populations, so the fit is partial). It is better framed as a research question than a repurposing recommendation.

**To proceed, the following is needed:**
- Clinical evidence specific to malignant renovascular hypertension, or a decision to prioritise another prediction
- Review of the BICS and PACE trial outcomes, with confirmation of their relevance to chronic pulmonary heart disease
- Mechanism of action data and the TGA Product Information (warnings and contraindications), which are missing
- Confirmation of the approved indication text for the ARTG entry
- A clinical assessment of whether oral bisoprolol has any role in severe or malignant hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

