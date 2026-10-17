---
layout: default
title: Epoprostenol
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Epoprostenol: predicted new indication Trigeminal autonomic cephalalgia (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Epoprostenol"
predicted_indications: ["trigeminal autonomic cephalalgia", "headache disorder", "migraine with brainstem aura", "papillary conjunctivitis", "allergic urticaria", "migraine disorder", "respiratory failure", "obsolete rare pulmonary disease"]
---

# Epoprostenol
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

# Epoprostenol: From Pulmonary Arterial Hypertension to Trigeminal Autonomic Cephalalgia

## One-Sentence Summary

Epoprostenol is a synthetic form of prostacyclin (PGI2), originally used to treat pulmonary arterial hypertension.
The TxGNN model predicts it may be effective for **trigeminal autonomic cephalalgia**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction.
Related evidence in headache and migraine suggests epoprostenol may trigger headache rather than relieve it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (from the TxGNN knowledge graph; the ARTG entry did not include indication text) |
| Predicted New Indication | Trigeminal autonomic cephalalgia |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, epoprostenol is a prostacyclin, a potent vasodilator and inhibitor of platelet aggregation. Its efficacy in pulmonary arterial hypertension is established.

The knowledge graph also lists several upper airway conditions (such as rhinitis, pharyngitis and the common cold) as original indications. These look questionable for this drug, so the prediction may partly reflect graph proximity rather than real pharmacology.

Vasodilatory and neurovascular mechanisms are implicated in trigeminal autonomic cephalalgias, which gives the prediction some biological plausibility. However, the direction of the effect is a concern. A human provocation study in migraine patients ([PMID 19614689](https://pubmed.ncbi.nlm.nih.gov/19614689/)) found that intravenous epoprostenol triggered migraine-like attacks. This suggests PGI2 activates headache pathways, so a therapeutic benefit is doubtful and harm is possible. That study concerned migraine, not trigeminal autonomic cephalalgia, so it is indirect evidence only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10111E | Veletri | Powder for I.V. infusion 500 micrograms (as sodium) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): blood coagulation disease and pulmonary oedema.
- **Drug Interactions**: The interaction screen returned 100 potential interactions in total. The moderate-level ones shown include:
  - Epinephrine
  - Acetylsalicylic acid (aspirin)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Mannitol
  - Ephedrine (including nasal)
  - Dexfenfluramine and fenfluramine
  - Glycerin
  - Papaverine
  - Sibutramine
- **Headache risk**: The migraine provocation study (PMID 19614689) is directly relevant to safety in any headache-related use.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a model score alone (L5), with no trials or publications. The only related human data point to epoprostenol provoking headache, the opposite of a therapeutic effect.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence of benefit in trigeminal autonomic cephalalgia
- Mechanism of action data and a clear rationale for why a PGI2 agonist would help rather than provoke headache
- Review of the TGA PI for warnings, contraindications and approved indications
- A route and setting assessment, since the only Australian product is an intravenous infusion

**Note on other predictions:** Among the other predicted indications, **respiratory failure** (inhaled epoprostenol) has the most supporting evidence (L3). This includes one small completed Phase 4 trial ([NCT01717209](https://clinicaltrials.gov/study/NCT01717209), n=14), observational studies and reviews. It is better treated as a separate research question, and it would need controlled trials first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

