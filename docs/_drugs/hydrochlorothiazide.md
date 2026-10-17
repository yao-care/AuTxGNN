---
layout: default
title: Hydrochlorothiazide
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydrochlorothiazide: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
monitor_inn: "Hydrochlorothiazide"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "acute pulmonary heart disease", "primary hereditary glaucoma", "open-angle glaucoma", "hypotrichosis simplex of the scalp"]
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydrochlorothiazide is a thiazide diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** currently support this specific prediction.
The prediction most likely reflects the closeness of this condition to the approved hypertension indication in the knowledge graph rather than new evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (the Australian licence entry has no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hydrochlorothiazide is a thiazide diuretic that is generally understood to inhibit the sodium-chloride cotransporter in the kidney. Its efficacy in hypertension and heart failure is established, so a prediction for a severe hypertensive kidney condition is biologically plausible on paper.

However, malignant hypertension is a hypertensive emergency. It is normally managed with rapid-acting parenteral agents, not thiazides. The high score most likely reflects graph proximity to the approved hypertension indication rather than any new evidence.

The same pattern applies to the other top-ranked predictions. Malignant renovascular hypertension (98.42%) overlaps with the approved indication, but renovascular hypertension is driven by renin-angiotensin activation, and thiazides may be less effective as monotherapy. Pulmonary hypertension predictions (98.35%) likely reflect the shared "hypertension" term, since thiazides do not address pulmonary vascular remodelling.

Chronic pulmonary heart disease (97.80%) has a more plausible, but only symptomatic, rationale. Diuretics, including thiazides combined with loop diuretics, are used to manage fluid overload in right heart failure. The remaining predictions (Braddock syndrome, glaucoma, hypotrichosis simplex of the scalp) have no identified mechanistic basis and are probably knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no clinical trials are registered for the top-ranked prediction, malignant hypertensive renal disease.

One trial was identified for a lower-ranked prediction, acute pulmonary heart disease (93.17%):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07469722](https://clinicaltrials.gov/study/NCT07469722) | Phase 2/3 | Not yet recruiting | 128 | Point-of-care ultrasound-guided diuretic strategy in acute decompensated heart failure. It tests a strategy, not hydrochlorothiazide specifically, and no results are available. |

## Literature Evidence

Currently no related literature is available for malignant hypertensive renal disease. The table below lists the most relevant publications retrieved for lower-ranked predictions. They are indirect, and most are reviews or preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT (hypertension, HCTZ combination) | Clin Ther | 26-week comparison of telmisartan and atenolol, with hydrochlorothiazide added as required, in mild to moderate hypertension |
| [38215973](https://pubmed.ncbi.nlm.nih.gov/38215973/) | 2024 | Post hoc analysis of RCT | Rev Clin Esp | CLOROTIC trial: adding hydrochlorothiazide to furosemide improved diuretic response in acute heart failure; this analysis looked at sex differences |
| [36595088](https://pubmed.ncbi.nlm.nih.gov/36595088/) | 2023 | Review | Eur J Pediatr | Overview of diuretic indications, mechanisms and side effects in paediatrics |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Fail | Transition from hypertension to heart failure |
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Small randomised crossover study | Dtsch Med Wochenschr | Diuretic combination (hydrochlorothiazide + triamterene) versus digitalis in 16 patients with chronic heart failure |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Haemodynamic study | Fortschr Med | Verapamil/triamterene/hydrochlorothiazide combination in 12 patients with chronic heart failure |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Hydrochlorothiazide-associated pulmonary oedema, a safety signal rather than a benefit |
| [35959982](https://pubmed.ncbi.nlm.nih.gov/35959982/) | 2022 | Case report | J Investig Med High Impact Case Rep | Methaemoglobinaemia reported as a rare adverse event |
| [2719123](https://pubmed.ncbi.nlm.nih.gov/2719123/) | 1989 | Preclinical physiology | Am J Physiol | Effects of diuretics, including hydrochlorothiazide, on renal erythropoietin production |
| [13776772](https://pubmed.ncbi.nlm.nih.gov/13776772/) | 1961 | Preclinical (animal) | Proc Soc Exp Biol Med | Renal sodium reabsorption and oxygen uptake in dogs during hypoxia and hydrochlorothiazide infusion |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13409R | Dithiazide | Tablet 25 mg (oral) | Not specified in the data compiled for this report |

## Safety Considerations

The data compiled for this report holds no label-derived warnings or contraindications, so please refer to the TGA-approved Product Information (PI) for these.

- **Knowledge-graph contraindication signals** (not label text, and they should be verified against the PI): liver failure, liver disease and cirrhosis, kidney disease, pancreatitis, gallbladder disease, peptic ulcer disease, epilepsy, asthma and bronchitis, anxiety and related disorders, porphyria, angioedema (including hereditary and acquired forms), systemic lupus erythematosus, autoimmune haemolytic anaemia, fetal erythroblastosis, myopathy and muscle disease, and familial periodic paralysis.
- **Drug interactions:** 100 interactions were recorded, and the first 20 are summarised here. Most are rated Moderate, including acarbose, rabeprazole, hydrocortisone, albiglutide, alogliptin, acetohexamide, cholecalciferol, calcifediol, calcitriol, amphotericin B (several formulations), beclomethasone, betamethasone, bisacodyl and bupropion. Doxycycline and atropine are rated Minor.
- **Literature safety signal:** Case reports describe hydrochlorothiazide-associated pulmonary oedema and drug-induced methaemoglobinaemia.
- **Relevance to this prediction:** Kidney disease appears among the knowledge-graph contraindication signals, which needs careful consideration for a renal-related indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by model scores (Evidence Level L5 for the top prediction). Malignant hypertensive renal disease is a hypertensive emergency that is not managed with thiazides, and no trials or publications support the use. The high scores most likely reflect closeness to the approved hypertension indication.

**To proceed, the following is needed:**
- Mechanism of action data (currently missing)
- Product Information warnings and contraindications for the Australian product, which are required before safety screening can proceed
- Approved indication text for the Australian licence entry
- Clinical or observational evidence specific to hydrochlorothiazide in malignant hypertension or hypertensive renal disease
- If a lower-ranked prediction is of interest, chronic pulmonary heart disease (fluid-overload management with loop plus thiazide diuretics) is the most clinically plausible, but its evidence is indirect and a targeted review would be needed first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

