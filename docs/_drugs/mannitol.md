---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Brain oedema and intracranial hypertension"
---

# Mannitol
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

# Mannitol: From Intracranial Hypertension and Cerebral Oedema to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain oedema, intracranial hypertension, ocular hypertension and congestive heart failure, and in Australia is registered as an inhaled product for cystic fibrosis.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and only **1 general review article** that does not support this use.
This prediction should be treated as a model output without clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain oedema and intracranial hypertension (original indications from the knowledge graph also include ocular hypertension, pseudotumor cerebri, congestive heart failure and cystic fibrosis; the ARTG entry has no indication text recorded) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic agent. It is used to draw water out of tissues (for example the brain and eye) and to promote osmotic diuresis. In theory, this could affect water balance.

However, the link to the predicted indication is weak. NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). It is managed with fluid restriction and solute loading (for example urea). Mannitol would be expected to worsen osmotic diuresis, and it has no established role in this condition. The high TxGNN score therefore appears to be a network-based prediction rather than a clinically grounded one.

Other candidates in the top 10 predictions (for example malignant hyperthermia-related conditions and periodic paralysis) appear to arise because mannitol is used as an excipient or vehicle in other products (such as dantrolene formulations or potassium infusions), not because of a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes ten common pitfalls in evaluating and treating hyponatraemia. It is a general review and does not support mannitol use in NSIAD. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2008Q | Bronchitol | Pack containing 280 capsules of powder for inhalation 40 mg and 2 inhalers | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** anuria, impaired renal function, pulmonary oedema, intracranial haemorrhage, liver failure, hepatic coma and encephalopathy, and others. Other listed conditions include thrombocytopenia, neutropenia, agranulocytosis, anaemia, porphyria, and sleep apnoea syndromes.
- **Drug Interactions:** 100 interactions were identified. Examples from the first 20 include:
  - **Major:** amikacin
  - **Moderate:** lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, dapagliflozin, canagliflozin, desvenlafaxine, cisatracurium, amifostine, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid, diatrizoate
  - **Minor:** doxycycline

In the context of the predicted indication, mannitol may worsen volume shifts and diuresis. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. There are no registered trials, and the one linked publication is a general hyponatraemia review. Mannitol's osmotic diuretic action is mechanistically at odds with NSIAD management, so the prediction is likely a false positive.

**To proceed, the following is needed:**
- Mechanism of action data for mannitol (for example from DrugBank)
- Product Information warnings and contraindications from the TGA for the registered product
- Any direct preclinical or clinical evidence of benefit in NSIAD, which is currently absent
- Review of the other top-ranked predictions, which show a similar pattern of excipient-driven associations without therapeutic backing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

