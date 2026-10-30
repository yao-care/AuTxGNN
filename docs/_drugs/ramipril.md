---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Ramipril"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
description: "Ramipril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Not recorded in the local data"
---

# Ramipril
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

## Ramipril: Pulmonary hypertension with unclear multifactorial mechanism
{: .text-alpha }

## One-Sentence Summary

Ramipril is an angiotensin-converting enzyme (ACE) inhibitor originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, but the support is thin: **0 clinical trials** and only **1 directly relevant animal study** among 11 retrieved publications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 (preclinical evidence only) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note on the choice of lead indication:** The top-ranked prediction (pulmonary hypertension with unclear multifactorial mechanism) has the same score but no trials or literature (L5). The second-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia, is the highest-ranked one with any supporting evidence, so this report focuses on it. Other predictions are summarised at the end.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ramipril is a known ACE inhibitor. It reduces angiotensin II formation, which lowers vascular tone and limits vascular remodelling. Its efficacy in hypertension and cerebrovascular risk reduction is established.

Chronic hypoxia drives pulmonary vascular constriction and remodelling, and the renin-angiotensin system may contribute to this. Mechanistically, ACE inhibition could therefore plausibly attenuate hypoxia-induced pulmonary vascular changes. The one directly relevant paper (PMID 9200213, 1996) found that ramipril given to rats during three weeks of hypoxia lowered baseline pulmonary perfusion pressure and attenuated the effects of chronic hypoxia on pulmonary blood vessels.

This is animal evidence only. Systemic hypertension and pulmonary hypertension are distinct conditions, and no human data were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Eleven publications were retrieved for this indication, but only one is directly relevant. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (rat) | Physiological Research | Ramipril (10 mg/kg daily) during 3 weeks of hypoxia lowered baseline pulmonary perfusion pressure and attenuated hypoxic pulmonary vascular effects |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclinical (rat) | Am J Physiol Regul Integr Comp Physiol | Renin-angiotensin system and cardiac contractile function during hypoxia-reoxygenation; tangential |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclinical / human tissue | Eur Heart J | ACE2 expression increases after myocardial infarction; tangential |
| [19380417](https://pubmed.ncbi.nlm.nih.gov/19380417/) | 2009 | Preclinical (animal) | Cardiovasc Res | ACE inhibition upregulates endothelial progenitor cells in cardiac pressure overload; tangential |
| [18464162](https://pubmed.ncbi.nlm.nih.gov/18464162/) | 2008 | Preclinical | Microcirculation | Ramipril or valsartan ameliorates peritubular capillary loss in the kidney; tangential |

The remaining retrieved papers (endometriosis, radiation brain necrosis, Cushing's disease case report, toxoplasmosis case report and others) are unrelated to pulmonary hypertension.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1316G | Ramipril Sandoz | Tablet 10 mg (oral) | Not listed in the data compiled for this report |

## Safety Considerations

**Knowledge-graph contraindication signals** (these come from a knowledge graph, not from label text, and should be checked against the Product Information):
- Renal: kidney disease, renal artery obstruction
- Hepatic and biliary: liver disease, gallbladder disease
- Haematological: neutropenia, agranulocytosis
- Immunological and connective tissue: systemic lupus erythematosus, scleroderma and systemic sclerosis, connective tissue disease
- Vascular: hereditary angioedema (including C1 inhibitor deficiency), hypotensive disorder
- Other: bone and cartilage disease, pyoureter

**Drug interactions** (100 recorded; examples):
- **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), glucose-lowering drugs (metformin, glimepiride, chlorpropamide, alogliptin, SGLT2 inhibitors such as dapagliflozin, empagliflozin and canagliflozin), aspirin, morphine, bupropion and dronabinol

For other safety information, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is a single 1996 rat study, with no clinical trials or human data. The label-derived safety data (warnings and contraindications) were also not available for this review.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for ramipril
- TGA Product Information warnings and contraindications for ramipril, which are required before safety screening
- Confirmation of the approved indication text for the ARTG entry
- Human haemodynamic or clinical studies of ACE inhibition in hypoxia-related pulmonary hypertension, or a preclinical study replicating the rat findings in a modern model
- A safety plan covering hypotension, renal function and potassium monitoring, since these patients often have comorbid cardiac and renal disease

## Other Predicted Indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 1 | Pulmonary hypertension, unclear multifactorial mechanism | 0.9993 | L5 | Model score only |
| 4 | Malignant hypertensive renal disease | 0.9993 | L5 | Largely overlaps with the existing indication |
| 5 | Braddock syndrome | 0.9991 | L5 | No mechanistic link evident |
| 6 | Brain stem infarction | 0.9989 | L5 | Consistent with existing stroke-prevention use |
| 7 | Prinzmetal angina | 0.9983 | L5 | Only an unrelated genetic study retrieved |
| 8 | Intracerebral haemorrhage | 0.9982 | L5 | Preclinical and indirect evidence only |
| 9 | ABri amyloidosis | 0.9979 | L5 | No mechanistic link evident |
| 10 | Cerebral artery occlusion | 0.9974 | L5 | Mixed animal data and one small human cerebral blood flow study (PMID 8797135); overlaps with the approved stroke-related use; flagged as a research question |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

