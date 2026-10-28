---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 688
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Spironolactone: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone is an oral aldosterone (mineralocorticoid receptor) antagonist, originally used for hypertension, congestive heart failure and primary aldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Spironolactone is known to block aldosterone receptors, which explains its use in hypertension, heart failure and primary aldosteronism. It also has anti-androgenic activity, through androgen receptor antagonism and reduced androgen synthesis. This is the basis for its use in androgen-driven hair loss.

The link to this prediction is weak. Hypotrichosis simplex is a rare inherited hair disorder, associated with variants in genes such as *CDSN*, *APCDD1* and *RPL21*. It is not driven by androgens. The high TxGNN score therefore appears to reflect network proximity to other hair disorders rather than a plausible pharmacological mechanism. The connection with the drug's original cardiovascular and renal indications is also indirect.

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
| 13503Q | Spiractin 25 | Tablet 25 mg (oral) | Not stated in the data compiled for this report |

The single entry is a valid single-ingredient product. No manufacturer is recorded.

---

## Safety Considerations

The data compiled for this report contains no label-based warnings or contraindications. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindication signals (knowledge graph, not label text)**:
  - Renal: kidney disease, anuria, pyoureter, nephrocalcinosis.
  - Electrolyte and mineral: potassium deficiency disease, hypercalcaemia, phosphorus metabolism disease.
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, osteitis fibrosa, gout, hyperuricaemia.
  - Hepatic: hepatic coma, hepatic encephalopathy, neonatal jaundice.
  - Other: pancreatitis, systemic lupus erythematosus, including the paediatric form.
- **Drug interactions**: The interaction screen returned 100 interactions in total. Loperamide is rated **Major**. Examples rated Moderate include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone).
  - Metformin.
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin).
  - Exenatide, bupropion, morphine and bisacodyl.

  Examples rated Minor include doxycycline, aspirin and fidaxomicin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). No trials or publications exist for hypotrichosis simplex, and the proposed mechanism does not fit a genetic, non-androgen-driven condition.

**To proceed, the following is needed:**
- Any mechanistic or genetic rationale linking mineralocorticoid or androgen receptor blockade to hypotrichosis simplex, or preclinical data supporting one.
- Detailed mechanism of action data.
- Safety information from the TGA Product Information, including warnings and contraindications.

- It is supported by a completed Phase 2 trial comparing spironolactone with topical minoxidil (NCT00175617, n=40), plus several systematic reviews, including one on oral and topical spironolactone.
- Suggested guardrails:
  - Monitor potassium and blood pressure.
  - Ensure contraception, given teratogenicity and feminisation risks.
  - Avoid use in men.
- Phase 3 randomised evidence is still lacking.

This is worth evaluating as a separate candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

