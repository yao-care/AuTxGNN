---
layout: default
title: Amiloride
parent: Moderate Evidence (L3-L4)
nav_order: 42
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Amiloride: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertension and congestive heart failure"
monitor_inn: "amiloride"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Amiloride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Amiloride: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic, originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **no registered clinical trials** and only **1 publication** (a general review) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the ARTG entry does not state an indication; this is taken from the knowledge-graph indications) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, amiloride blocks the epithelial sodium channel (ENaC) and is already used for hypertension and heart failure, so its efficacy in those conditions has been established. Mechanistically, it may be applicable to other hypertensive conditions.

The link to malignant renovascular hypertension is weak. This condition is driven mainly by renin-angiotensin system activation and renal artery stenosis, so ENaC blockade would at best be an adjunct. The only supporting publication is a review of mineralocorticoid hypertension, which is a different mechanism. The very high TxGNN score (99.82%) probably reflects network proximity to the already-approved hypertension indication rather than disease-specific evidence.

Other predicted indications were also reviewed:
- **Malignant hypertensive renal disease** (99.82%): knowledge-graph prediction only, with no trials or literature. Hyperkalaemia risk in renal impairment is a significant concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.81%): there is a plausible preclinical rationale (hypoxia downregulates alveolar ENaC, and ASIC1 has been implicated in hypoxic pulmonary hypertension), but the literature is mostly preclinical or off-topic and no clinical trials were found. This is better framed as a research question.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.81%) and **Braddock syndrome** (99.75%): computational prediction only, with no supporting evidence.
- **Chronic pulmonary heart disease** (99.68%): there are small heart failure studies of amiloride, but they are indirect and do not address cor pulmonale specifically. This is a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (malignant renovascular hypertension):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Overview of investigating mineralocorticoid hypertension. About 3% of hypertensive patients have corticosteroid-induced hypertension, typically hypokalaemic with low plasma renin activity. The most frequent cause is primary aldosteronism. Not specific to renovascular hypertension. |

Indirect evidence from related predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Double-blind crossover clinical study | Cardiovasc Drugs Ther | Amiloride improved haemodynamics in 11 men with chronic heart failure on digoxin and diuretics (chronic pulmonary heart disease prediction) |
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT (crossover) | Lancet | Captopril alone vs frusemide plus amiloride in mild heart failure (14 patients). 4 patients on captopril alone deteriorated, all with previous pulmonary oedema |
| [25398716](https://pubmed.ncbi.nlm.nih.gov/25398716/) | 2015 | Preclinical/Review | Exp Physiol | Smooth muscle ASIC1 implicated in hypoxic pulmonary hypertension (pulmonary hypertension prediction) |
| [9376126](https://pubmed.ncbi.nlm.nih.gov/9376126/) | 1997 | Preclinical | Am J Respir Cell Mol Biol | Hypoxia reduced amiloride-sensitive sodium channel activity in rat alveolar cells |
| [15219007](https://pubmed.ncbi.nlm.nih.gov/15219007/) | 2004 | Cohort | Eur Respir J | High altitude impaired nasal sodium transport in subjects prone to high-altitude pulmonary oedema |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case report | Am J Med Sci | Severe hyperkalaemia (K+ 9.3 mEq/L) in a 96-year-old woman receiving trimethoprim-sulfamethoxazole (safety signal) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13410T | Moduretic | Tablet containing hydrochlorothiazide 50 mg with amiloride hydrochloride 5 mg | Not stated in the data compiled for this report |

## Safety Considerations

**Contraindications / conditions flagged in the knowledge graph** (these come from drug-disease contraindication links, not label text):
- Renal: kidney disease, diabetic nephropathy, anuria, pyoureter
- Hepatic: liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis
- Metabolic: potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, acidosis disorder, acquired lactic acidosis, hyperuricaemia, gout, hyperparathyroidism, osteitis fibrosa
- Other: systemic lupus erythematosus (including paediatric), neonatal jaundice

Some of these probably reflect the hydrochlorothiazide component of the ARTG product.

**Drug Interactions:** 136 interactions were recorded. Examples include:
- Moderate: metformin, hydrocortisone, dexamethasone, betamethasone, budesonide, bupropion, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, bisacodyl, castor oil, lactulose, lactitol, glycerin, dronabinol
- Minor: doxycycline, amoxicillin, cimetidine

**Hyperkalaemia** is a key concern, particularly in elderly patients, in renal impairment, and when combined with other potassium-raising drugs (see the case report above).

Product Information (PI) warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the prediction is not supported by clinical evidence. There are no trials, and the single publication is an indirect review. The mechanism (ENaC blockade) does not match the main drivers of malignant renovascular hypertension. Hyperkalaemia and renal safety concerns are significant in this population. The pulmonary hypertension and chronic pulmonary heart disease predictions are better treated as research questions.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a formal mechanistic analysis
- TGA Product Information warnings and contraindications to complete safety screening
- Clinical or well-designed preclinical studies of amiloride in renovascular or malignant hypertension
- A renal and potassium monitoring plan for patients with renal artery stenosis or renal impairment
- Review of the single-ingredient amiloride products on the ARTG, since only the hydrochlorothiazide combination product was captured here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

