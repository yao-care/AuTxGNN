---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Asthma, bronchial disease"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
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

## Salbutamol: From Asthma to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting beta-2 agonist bronchodilator, originally used to treat asthma and bronchial disease.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this specific prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchial disease |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, salbutamol is a beta-2 adrenergic agonist. Its efficacy in asthma and bronchial disease is established, and mechanistically it may be applicable to allergic eye conditions.

Papillary conjunctivitis is an allergic or inflammatory eye condition in which mast cells play a role. Beta-2 agonism might plausibly dampen mast cell mediator release in ocular allergy, which is the main reason the model links the two. This is a hypothesis only. The data compiled for this report contain no trial or publication that tests salbutamol in papillary conjunctivitis.

Indirect, older preclinical work exists for the related condition atopic conjunctivitis, where topical salbutamol suppressed immediate allergic conjunctivitis in guinea pigs (1987). That work is not evidence for papillary conjunctivitis in humans.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1103C | Ventolin | Oral solution 2 mg (as sulfate) per 5 mL, 150 mL | Not specified in the data compiled for this report |

The only registered product is an oral formulation. No ocular or topical eye formulation is listed, so route compatibility with an eye indication is unresolved.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (drawn from drug-disease relationships in the TxGNN knowledge graph, not from approved label text):
- Cardiovascular: hypertension, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, myocardial ischaemia, coronary artery disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, acidosis (including metabolic), hyperthyroidism, Graves disease, thyrotoxicosis
- Neurological: epilepsy
- Ocular: angle-closure glaucoma, ocular hypertension (relevant to any eye-directed use)
- Urological: benign prostatic hyperplasia, bladder neck obstruction

**Drug Interactions** (100 interactions in total; examples shown):
- **Moderate:**
  - Glucose-lowering agents: acarbose, acetohexamide, chlorpropamide, albiglutide, alogliptin, canagliflozin, dapagliflozin
  - Epinephrine
  - Isometheptene
  - Famotidine
  - Clarithromycin
  - Cisapride
  - Bisacodyl
  - Castor oil
  - Diethylpropion
- **Minor:** corticosteroids (hydrocortisone, beclomethasone, betamethasone, budesonide, dexamethasone)

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is model-only (L5), with no trials or literature for papillary conjunctivitis. The only registered Australian product is oral, and the knowledge graph flags several contraindications (including glaucoma-related ones) that matter for any eye-directed use.

**To proceed, the following is needed:**
- Human clinical or mechanistic studies of beta-2 agonists in papillary or allergic conjunctivitis
- Mechanism of action data to support the proposed mast cell link
- A feasible route and formulation for eye delivery, as only an oral product is currently registered in Australia
- Review of the PI warnings and contraindications, which could not be retrieved for this report

**Note on other predictions for salbutamol:** Other indications predicted for this drug have stronger support, notably obstructive lung disease (L1). That prediction largely extends the existing bronchodilator use rather than representing true repurposing, so it may be worth evaluating separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

