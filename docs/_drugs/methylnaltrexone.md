---
layout: default
title: Methylnaltrexone
parent: Model Prediction Only (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Methylnaltrexone
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

# Methylnaltrexone: From Opioid-Induced Constipation to Congenital Hypotrichosis Milia

## One-Sentence Summary

Methylnaltrexone is a peripherally acting mu-opioid receptor antagonist, marketed in Australia as Relistor injection and generally used for opioid-induced constipation.
The TxGNN model predicts it may be effective for **congenital hypotrichosis milia**, but **no clinical trials and no publications** support this prediction.
It is a model-generated signal only and should be treated as hypothesis-level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the ARTG data compiled for this report (the pharmacology source describes use in opioid-induced constipation) |
| Predicted New Indication | Congenital hypotrichosis milia |
| TxGNN Prediction Score | 78.35% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology records show that methylnaltrexone binds the mu (OPRM1), delta (OPRD1) and kappa (OPRK1) opioid receptors. It is described as a peripherally restricted antagonist used for opioid-induced constipation.

The predicted indication is a hereditary hair follicle developmental disorder. No plausible mechanistic link was identified between peripheral opioid receptor blockade and this condition. The high TxGNN score appears to be a graph-based prediction artefact rather than a biologically grounded signal.

Other top-ranked predictions show the same pattern. These include hypotrichosis simplex of the scalp, alopecia, diffuse alopecia areata, exercise-induced malignant hyperthermia, common cold, familial periodic paralysis, obsolete hyperuricemia and trigeminal autonomic cephalalgia. None has trials or literature, and none has a supported mechanism. Respiratory failure (rank 7) has only indirect preclinical context. Methylnaltrexone does not readily cross the blood-brain barrier, so it would not be expected to reverse central respiratory depression.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for congenital hypotrichosis milia.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5423K | Relistor | Solution for injection containing methylnaltrexone bromide 12 mg in 0.6 mL | Not listed in the data compiled |

The only available route is injectable.

---

## Safety Considerations

- **Drug Interactions**: 13 interaction records were found, 10 of them classed as Moderate. The Moderate interactions are with:
  - Alvimopan
  - Naloxone
  - Naldemedine
  - Nalmefene
  - Naloxegol
  - Naltrexone
  - Capmatinib
  - Pitolisant
  - Risdiplam
  - Gilteritinib

  The other three records are pharmacology target entries (delta, kappa and mu opioid receptors) and are not interaction ratings.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). It has no registered trials, no supporting literature and no plausible mechanistic link. The prediction should not progress to clinical consideration on current data.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a biological rationale linking opioid receptor signalling to hair follicle development
- Preclinical evidence (for example, follicle or skin models) supporting the prediction
- The approved indication text and PI warnings and contraindications for the ARTG entry
- A review of whether the higher-ranked alternatives have more credible links, since the top-ranked predictions all lack supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

