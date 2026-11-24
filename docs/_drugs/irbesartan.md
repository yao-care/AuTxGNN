---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Australia: 12 PBS items (12 currently listed)"
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (12 of 12 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for irbesartan: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), label version 2026-08-24; accessed 2026-11-19.) Based on known pharmacology, irbesartan is an AT1 receptor antagonist. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so blocking the AT1 receptor is a plausible approach. However, the predicted indication sits very close to irbesartan's existing hypertension indication, so it offers limited repurposing novelty. The score is a computational prediction only, with no supporting trials or literature.

Other high-scoring predictions (ranks 2 to 10) were also reviewed:
- **Malignant hypertensive renal disease** (0.9931): consistent with AT1 blockade lowering blood pressure and intraglomerular pressure, but no evidence was provided. Evidence level L5, Hold.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (0.9925): 11 publications were retrieved, but these are mostly animal or in vitro studies on cardiac or altitude-related hypoxia, and several are off-target. No human pulmonary hypertension trials. Evidence level L4, Research Question.
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

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2136K | Avapro HCT 300/25 | Irbesartan + hydrochlorothiazide | Tablet 300 mg-25 mg | Valid |
| 8246B | Irbesartan Sandoz | Irbesartan | Tablet 75 mg | Valid |
| 8247C | Avapro | Irbesartan | Tablet 150 mg | Valid |
| 8248D | Avapro | Irbesartan | Tablet 300 mg | Valid |
| 8404H | Avapro HCT 150/12.5 | Irbesartan + hydrochlorothiazide | Tablet 150 mg-12.5 mg | Valid |
| 8405J | Avapro HCT 300/12.5 | Irbesartan + hydrochlorothiazide | Tablet 300 mg-12.5 mg | Valid |
| 13380F | Avapro | Irbesartan | Tablet 150 mg | Valid |
| 13435D | Irbesartan Sandoz | Irbesartan | Tablet 75 mg | Valid |
| 13446Q | Avapro HCT 300/25 | Irbesartan + hydrochlorothiazide | Tablet 300 mg-25 mg | Valid |
| 13545X | Avapro HCT 300/12.5 | Irbesartan + hydrochlorothiazide | Tablet 300 mg-12.5 mg | Valid |
| 13564X | Avapro | Irbesartan | Tablet 300 mg | Valid |
| 13572H | Avapro HCT 150/12.5 | Irbesartan + hydrochlorothiazide | Tablet 150 mg-12.5 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from model relationships, not from label text, and must be verified against the Product Information): angioedema (including hereditary, acquired and RAAS-blocker-induced forms), pancreatitis, systemic lupus erythematosus, myopathy and rhabdomyolysis, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, hyperuricaemia and gout, hypotensive disorders, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, hepatic coma and encephalopathy, anuria, renal artery obstruction, and several others.
- **Drug Interactions** (100 interactions in the screening database; examples):
  - **Major**: potassium citrate and potassium bicarbonate (risk of hyperkalaemia).
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec), aspirin, morphine, bupropion, aprepitant, dronabinol, and bowel preparations (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Please refer to the TGA-approved Product Information (PI) for warnings and formal contraindications, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9931), but no clinical trials or publications support irbesartan for malignant hypertensive renal disease (L5). The indication also overlaps heavily with irbesartan's existing hypertension use, so the added value is limited. Among the other predictions, only pulmonary hypertension due to lung disease or hypoxia has any supporting literature, and that is preclinical or indirect (L4, Research Question).

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the TGA Product Information (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- The approved indication text for ARTG 13380F
- A targeted literature search for ARB use in renovascular hypertension, and clinical evidence for the pulmonary hypertension and cor pulmonale predictions
- A decision on whether the top prediction offers enough novelty beyond the existing hypertension indication to justify further work

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

