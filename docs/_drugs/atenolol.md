---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 65
evidence_level: L5
indication_count: 5
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-30
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension"
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, recorded in the knowledge graph for hypertension and myocardial infarction, among other conditions. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (a relation recorded in the knowledge graph; the Australian licence record contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Atenolol is a beta-1 selective blocker. Its blood pressure lowering and its reduction of renin release make a link to hypertensive kidney disease biologically plausible.

There are important caveats. Atenolol's relationship to hypertension is already recorded in the knowledge graph, so this prediction may largely reflect the overlap with that original use rather than independent repurposing evidence. Malignant hypertension is usually managed acutely with intravenous agents, and beta-blockers are not first-line for it.

Other predictions for this drug are weaker still. They include pulmonary hypertension (two types), Braddock syndrome and chronic pulmonary heart disease. They are not assessed in detail here because the top-ranked prediction is the focus of this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1081X | Atenolol GH | Tablet 50 mg (oral) | Not stated in the licence record |

This is a single-ingredient product, valid and marketed.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. The label warnings and contraindications were not available in the data compiled for this report.

- **Relations recorded in the knowledge graph (not label text):** Atenolol is recorded as contraindicated with several conditions. These include asthma (including allergic and intrinsic forms), diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, atrioventricular block, Raynaud disease, anaphylaxis, liver failure, pancreatitis, systemic lupus erythematosus, psoriasis, gout, anuria, anxiety and related disorders, and several electrolyte or metabolic disorders (potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease). These should be checked against the PI.
- **Drug interactions:** The interaction screen returned 100 interactions, and 20 are available for review. Most are rated Moderate, including epinephrine, bupropion, morphine, several corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide), atropine, hyoscyamine, acetohexamide and several calcium salts. Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. There are no trials and no publications on this disease, so the evidence level is L5. The prediction may simply reflect atenolol's existing use in hypertension, and beta-blockers are not first-line for malignant hypertension.

**To proceed, the following is needed:**
- Clinical or observational studies of atenolol in malignant hypertensive renal disease
- Mechanism of action data
- TGA Product Information warnings and contraindications for safety screening
- Indication text for the Australian licence record
- A review of how this indication differs from atenolol's existing use in hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

