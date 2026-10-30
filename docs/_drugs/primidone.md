---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Primidone"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Primidone: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Primidone
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

## Primidone: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Primidone is an anticonvulsant originally used to treat epilepsy, including generalised tonic-clonic, partial and Lennox-Gastaut seizures.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **no clinical trials and no publications** currently support this prediction. It is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Primidone is a long-established antiseizure drug and is known to be metabolised in part to phenobarbital and phenylethylmalonamide (PEMA). Its efficacy in epilepsy is established, but this report cannot show a mechanistic route to the predicted tumour indication.

The predicted indication, trigeminal nerve neoplasm, is a tumour of a cranial nerve, whereas primidone acts on seizure control. No plausible link between anticonvulsant action and tumour control has been established. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of antitumour activity.

**Other predictions are more plausible.** Several lower-ranked predictions sit close to primidone's original use:

- **Trigeminal neuralgia** (score 0.9998) has a class-level rationale, because sodium-channel-blocking antiseizure drugs such as carbamazepine are used for it. The linked literature is mostly about carbamazepine and contains no primidone-specific efficacy data. It is flagged as a research question.
- **Beta-ketothiolase deficiency** has no literature and no mechanistic basis, and primidone's enzyme-inducing properties add caution in metabolic disease.

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
| ARTG 1939C | Mysoline | Tablet 250 mg (oral) | Not recorded in the data compiled for this report |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from the label): porphyria and other porphyrin metabolism disorders, liver disease, kidney disease, gallbladder disease, blood disorders (thrombocytopenia, neutropenia, agranulocytosis, leukopenia, pancytopenia, anaemia), sleep apnoea and related hypoventilation syndromes, substance abuse or dependence, and anxiety, neurotic and dysthymic disorders.
- **Drug interactions:** 100 interactions were identified in total. The main ones listed include:
  - **Major:** morphine, eliglustat.
  - **Moderate:** doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcifediol, calcitriol, pioglitazone, canagliflozin, saxagliptin, bupropion, aprepitant, metronidazole, difenoxin, diphenoxylate, dronabinol.
  - **Minor:** cimetidine.
- Primidone is an enzyme inducer, so interaction potential is broad. Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a model output only (L5), with no registered trials, no literature and no plausible mechanistic link to tumour control. The safety profile also includes significant haematological, hepatic and interaction concerns.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to test any link between primidone and tumour biology.
- Preclinical or case-level evidence of primidone activity in trigeminal nerve neoplasm.
- Review of the TGA-approved Product Information for warnings and contraindications.
- Consideration of better-supported alternatives, such as trigeminal neuralgia (as a research question) or reflex seizure subtypes, which sit closer to primidone's established use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

