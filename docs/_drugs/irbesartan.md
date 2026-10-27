---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Irbesartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, hypertensive disorder, diabetic nephropathy"
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "chronic pulmonary heart disease", "obsolete susceptibility to ischemic stroke"]
---

# Irbesartan
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

## Irbesartan: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (the ARTG entry has no indication text; these come from the knowledge graph used by the model) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, irbesartan is an AT1 receptor antagonist. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so blocking the AT1 receptor is a plausible approach. However, the predicted indication sits very close to irbesartan's existing hypertension indication, so it offers limited repurposing novelty. The score is a computational prediction only, with no supporting trials or literature.

Other high-scoring predictions (ranks 2 to 10) were also reviewed:
- **Malignant hypertensive renal disease** (99.31%): consistent with AT1 blockade lowering blood pressure and intraglomerular pressure, but no evidence was provided. Evidence level L5, Hold.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.25%): 11 publications were retrieved, but these are mostly animal or in vitro studies on cardiac or altitude-related hypoxia, and several are off-target. No human pulmonary hypertension trials. Evidence level L4, Research Question.
- **Chronic pulmonary heart disease** (96.53%): literature is indirect, mainly on heart failure with preserved ejection fraction (including the I-PRESERVE trial population) and one pilot RCT of irbesartan with exercise in COPD patients. Evidence level L4, Research Question.
- **Pulmonary hypertension with unclear multifactorial mechanism, Prinzmetal angina, Braddock syndrome, two rare genetic vascular syndromes, and an obsolete stroke susceptibility term**: no trials or literature, prediction only (L5, Hold). The stroke entry is an obsolete ontology term and not clinically actionable.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (or for any of the other nine predictions reviewed).

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For context, the most relevant publications retrieved for the closest-supported predictions are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18949104](https://pubmed.ncbi.nlm.nih.gov/18949104/) | 2008 | RCT (pilot) | Can Respir J | Aerobic exercise training alone or with irbesartan assessed for effects on blood pressure and heart rate variability in COPD patients |
| [22887722](https://pubmed.ncbi.nlm.nih.gov/22887722/) | 2012 | Cohort | Circ Heart Fail | Sex differences in outcomes in elderly patients with HFpEF, from the I-PRESERVE (irbesartan) trial |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Pleiotropic effects of AT1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical | Biomed Pharmacother | Irbesartan ameliorated chronic mountain sickness in a rat model via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Not classified | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in rats with high-altitude pulmonary hypertension, with involvement of intestinal flora |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical | Sleep Breath | Irbesartan attenuated sleep apnoea-induced cardiac apoptosis |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13380F | Avapro | Tablet 150 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from model relationships, not from label text, and must be verified against the Product Information): angioedema (including hereditary, acquired and RAAS-blocker-induced forms), pancreatitis, systemic lupus erythematosus, myopathy and rhabdomyolysis, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, hyperuricaemia and gout, hypotensive disorders, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, hepatic coma and encephalopathy, anuria, renal artery obstruction, and several others.
- **Drug Interactions** (100 interactions in the screening database; examples):
  - **Major**: potassium citrate and potassium bicarbonate (risk of hyperkalaemia).
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec), aspirin, morphine, bupropion, aprepitant, dronabinol, and bowel preparations (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Please refer to the TGA-approved Product Information (PI) for warnings and formal contraindications, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.31%), but no clinical trials or publications support irbesartan for malignant renovascular hypertension (L5). The indication also overlaps heavily with irbesartan's existing hypertension use, so the added value is limited. Among the other predictions, only pulmonary hypertension due to lung disease or hypoxia and chronic pulmonary heart disease have any supporting literature, and that is preclinical or indirect (L4, Research Question).

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the TGA Product Information (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- The approved indication text for ARTG 13380F
- A targeted literature search for ARB use in renovascular hypertension, and clinical evidence for the pulmonary hypertension and cor pulmonale predictions
- A decision on whether the top prediction offers enough novelty beyond the existing hypertension indication to justify further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

