---
layout: default
title: Allopurinol
parent: Moderate Evidence (L3-L4)
nav_order: 34
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L4). Approved use: Gout, hyperuricaemia, acute urate nephropathy"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor, originally used to treat gout, hyperuricaemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are **0 clinical trials** and only **2 loosely related publications** (a hypothesis paper and a rat study, neither of which tests allopurinol), so this remains a model prediction with very little support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout, hyperuricaemia, acute urate nephropathy (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid production, and its efficacy in gout is well established. A mechanistic link to hepatic porphyria is not demonstrated.

The two publications retrieved are indirect. One is a hypothesis paper on targeting 5-aminolevulinate synthase (the rate-limiting enzyme of haem synthesis) through tryptophan and haem-utilisation pathways. The other is a rat study of carbamazepine and hepatic haem metabolism. Neither studies allopurinol as a treatment for porphyria.

There is also a safety concern. Allopurinol has been reported to affect hepatic haem turnover in animal models and may be porphyrinogenic in some settings, so the direction of effect is uncertain and could be harmful. The very high TxGNN score is a model output and is not backed by clinical data. Several other predictions share near-identical scores, which suggests a shared knowledge-graph artefact rather than disease-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of liver 5-ALAS, via tryptophan or inhibition of haem use by tryptophan 2,3-dioxygenase, as therapy for acute hepatic porphyrias. Does not test allopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (rat) | Biochemical Pharmacology | Low-dose carbamazepine worsened loss of haem in rat liver, relevant to how drugs exacerbate porphyria. Does not involve allopurinol. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13358C | Zyloprim | Tablet 100 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not product label text): liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, and anti-glomerular basement membrane disease.
- **Drug interactions** (100 recorded; examples below):
  - *Moderate*: aluminium hydroxide, attapulgite, kaolin, magaldrate, sucralfate
  - *Minor*: amoxicillin, chlorpropamide
  - *Unknown severity*: calcitriol, vitamin A, pantoprazole, omeprazole, glimepiride, metformin, acarbose, rosiglitazone, mesalazine, doxycycline, clotrimazole, morphine, palonosetron

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based safety data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by indirect literature and no clinical trials, and the available information suggests the effect on porphyria could be neutral or harmful. A high model score alone is not sufficient to justify progression.

**To proceed, the following is needed:**
- A review of whether allopurinol is porphyrinogenic, including the TGA PI and porphyria drug-safety databases
- Mechanism of action data and a specific mechanistic rationale linking xanthine oxidase inhibition to haem biosynthesis
- Preclinical studies directly testing allopurinol in porphyria models
- Retrieval of PI warnings and contraindications to complete safety screening
- Confirmation of the approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

