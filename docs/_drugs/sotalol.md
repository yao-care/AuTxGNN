---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Sotalol"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
description: "Sotalol: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). Approved use: Not recorded in the local data"
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sotalol: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Sotalol is a beta-blocker with class III antiarrhythmic activity, originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**,
but there are currently **no clinical trials** and **no publications** supporting this prediction. The mechanistic review also suggests the prediction is likely a false positive or a safety signal, because sotalol may worsen sinus node dysfunction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on general pharmacology, sotalol combines beta-adrenergic blockade with class III antiarrhythmic activity (potassium channel blockade). It slows the sinus rate and atrioventricular conduction, and it is used for rhythm control in atrial fibrillation.

The predicted condition is a heritable sinus node disorder linked to HCN4 channel dysfunction. There is a loose conceptual link, because both involve ion channels governing cardiac rhythm. However, sotalol would be expected to **worsen** sinus node dysfunction (bradycardia, sinus pauses) rather than treat it. The knowledge graph itself lists sick sinus syndrome, including the familial form, as a contraindication for sotalol. The prediction is therefore most likely a false positive, or best read as a safety signal rather than a therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered for sick sinus syndrome 2, autosomal dominant.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2043M | Cardol | Tablet containing sotalol hydrochloride 160 mg | Not available in the compiled data |

*The licence number is reported as supplied in the compiled data and should be verified against the ARTG.*

## Safety Considerations

**Contraindications flagged in the knowledge graph (not taken from label text):**
- Long QT syndrome (including familial), torsades de pointes
- Sick sinus syndrome (including familial) and atrioventricular block
- Asthma (including intrinsic and allergic) and other bronchial disease
- Hypotensive disorder
- Impaired renal function
- Potassium deficiency disease
- Diabetes mellitus and diabetic ketoacidosis
- Anaphylaxis

**Drug Interactions:** 100 interactions were identified in the DDInter database. Examples of those rated **Major** include:
- Epinephrine
- Clarithromycin
- Picosulfuric acid
- Polyethylene glycol (3350 with electrolytes)

Many others are rated Moderate, including famotidine, cimetidine, loperamide, bupropion, morphine, atropine, bisacodyl, canagliflozin, dapagliflozin and chlorpropamide. Acetylsalicylic acid is rated Minor.

Sotalol also carries proarrhythmic risk (QT prolongation, torsades de pointes). Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. Sotalol's pharmacology and its knowledge-graph contraindications point towards potential harm in sick sinus syndrome, so there is no supportable therapeutic rationale.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from a primary source (for example DrugBank)
- TGA Product Information, to confirm approved indications, warnings and contraindications
- Any preclinical or clinical evidence showing benefit in HCN4-related sinus node dysfunction, which is unlikely given current knowledge

**Other predicted indications (for context):**
Among the other nine predictions, none has therapeutic support. **Stroke disorder** (score 0.9944, L4) is the only one with a trial, and the Phase 3 trial NCT00007605 (n=706, completed) studied amiodarone and sotalol for maintaining sinus rhythm in atrial fibrillation. That is the existing indication, not stroke, so this trial gives indirect context only. It remains a research question rather than a candidate. **Manic bipolar affective disorder** has only literature on QT and torsades interaction hazards with antipsychotics, which argues against use. The remaining predictions (Wildervanck syndrome, sarcoglycanopathy, macrocephaly with dysmorphic facies, obsolete susceptibility to ischemic stroke, nephrogenic syndrome of inappropriate antidiuresis, ABri amyloidosis, periodic paralysis with transient compartment-like syndrome) have no plausible mechanistic link and no evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

