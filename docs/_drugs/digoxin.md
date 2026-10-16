---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Digoxin
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used for atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **1 loosely related publication** (a review that does not support the indication).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning (from the knowledge graph; no approved indication text is listed for the Australian product) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Digoxin is a cardiac glycoside whose established effects come from inhibiting the Na+/K+-ATPase pump, which raises intracellular calcium. Its efficacy in atrial fibrillation (ventricular rate control) is established.

The link to Prinzmetal angina is weak. Prinzmetal angina is caused by coronary vasospasm. In theory, raising intracellular calcium could increase vascular tone, and cardiac glycosides are generally not favoured in vasospastic angina. The only retrieved paper concerns the chronopharmacology of antihypertensive treatment and does not support this indication. The high TxGNN score reflects a graph-based association only, not a demonstrated therapeutic rationale.

Other top-ranked predictions (duodenal obstruction, duodenal ulcer, hypoalphalipoproteinemia, homozygous familial hypercholesterolemia and others) also have no identifiable mechanistic basis. Thrombotic disease and stroke disorder have only indirect literature, reflecting digoxin's existing use in atrial fibrillation and heart failure.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology and its impact on antihypertensive treatment; does not address digoxin in Prinzmetal angina |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1322N | Lanoxin | Tablet 250 micrograms (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (graph-derived associations, not label text): kidney disease, potassium deficiency, hypercalcaemia, phosphorus metabolism disease, myocardial infarction, coronary thrombosis, cor pulmonale, Wolff-Parkinson-White syndrome, sick sinus syndrome, ventricular fibrillation, hypertrophic cardiomyopathy, atrioventricular block, hypothyroidism/myxoedema, myocarditis, constrictive pericarditis, restrictive cardiomyopathy, and others.
- **Drug Interactions**: 100 interactions were identified. Examples at Moderate level include acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, metformin, amphotericin B, bupropion, aspirin and calcium phosphate. Minor examples include albiglutide, hyoscyamine, atropine and glycopyrronium.
- Digoxin has a narrow therapeutic index and is cleared renally, which adds risk in any new population. Some observational registry data (for example, the combination of beta-blocker and digoxin in atrial fibrillation) have raised adverse cardiovascular outcome concerns.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone. There are no clinical trials, the single retrieved paper is unrelated, and the pharmacology (calcium-raising, vasoconstrictive potential) argues against use in vasospastic angina. Digoxin's narrow therapeutic index and the extensive contraindication and interaction profile add safety concern.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a plausible mechanistic argument for coronary vasospasm
- Retrieval and review of the TGA Product Information for approved indications, warnings and contraindications (a blocking data gap)
- Preclinical or clinical evidence specific to Prinzmetal angina
- A review of safety in the target population, including renal function, electrolytes and drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

