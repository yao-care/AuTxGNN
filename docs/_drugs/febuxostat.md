---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 287
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Febuxostat: predicted new indication Renal hypouricaemia (evidence level L4). Approved use: Hyperuricaemia"
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Febuxostat: From Hyperuricaemia to Renal Hypouricaemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat hyperuricaemia.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but this prediction is mechanistically doubtful, because the condition already involves low serum uric acid.
Evidence is thin: **1 clinical trial** of uncertain relevance and **2 publications** (reviews/case-based) are currently linked to this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricaemia (from the knowledge graph; no approved indication text is listed for the Australian entry) |
| Predicted New Indication | Renal hypouricaemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Febuxostat is known to be a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid, and its efficacy in hyperuricaemia is established.

Renal hypouricaemia, however, is characterised by already low serum uric acid, typically due to loss of function in urate transporters (URAT1/GLUT9). Further urate lowering is therefore mechanistically counterproductive and could add risk. The only literature link is a 2023 report suggesting that non-purine xanthine oxidoreductase inhibitors might help prevent exercise-induced acute kidney injury in a young athlete with familial renal hypouricaemia. This is indirect and hypothetical.

The very high TxGNN score most likely reflects network proximity to urate pathways rather than a true therapeutic fit.

**Other predictions of note (lower-ranked):**
- **Partial HPRT deficiency** and **Lesch-Nyhan syndrome** (Evidence Level L3): xanthine oxidase inhibition can control urate overproduction in these conditions, but it does not correct the enzyme defect or the neurobehavioural features. Xanthine stone and nephropathy risk need monitoring, and paediatric use is off-label. Evidence is limited to case reports and a small case series.
- Several liver, vascular and metabolic predictions (e.g. hepatoportal sclerosis, hepatopulmonary syndrome, hepatic porphyria) have no supporting trials or literature and no clear mechanistic link (Evidence Level L5).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of uric acid control and its effect on stone recurrence and renal function in patients with calculi and hyperuricaemia. Relevance to renal hypouricaemia cannot be confirmed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricaemia (serum urate <2 mg/dL), its causes and clinical relevance for rheumatologists |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (indexed as review) | Internal Medicine | Adolescent footballer with familial renal hypouricaemia (URAT1 mutations) and recurrent exercise-induced AKI; non-purine xanthine oxidoreductase inhibitor (febuxostat) proposed as a possible preventive option |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10445R | Adenuric | Tablet 80 mg (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): stroke disorder, cerebrovascular disorder, cerebral infarction, myocardial infarction, coronary thrombosis, and haemoglobinopathy. These should be verified against the Product Information. Febuxostat is also associated with a cardiovascular death warning (from the CARES trial), which argues for caution.
- **Drug interactions** (22 recorded; main ones):
  - **Major:** mercaptopurine, azathioprine, leflunomide, teriflunomide
  - **Moderate:** theophylline and related xanthines (dyphylline, aminophylline, oxtriphylline), methotrexate, tioguanine, clofarabine, asparaginase and pegaspargase, brentuximab vedotin, trabectedin, epirubicin, naltrexone, and interferon beta products
- Hepatic enzyme elevation is a known concern and is relevant to any liver-related repurposing.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Renal hypouricaemia involves already low uric acid, so further lowering is mechanistically counterproductive and potentially harmful. The evidence consists of one trial of unclear relevance and an indirect case report. The high TxGNN score is not supported by clinical rationale.

**To proceed, the following is needed:**
- Mechanism of action data and product information warnings and contraindications for the Australian product
- Direct clinical evidence in renal hypouricaemia, or a clear case that benefit outweighs the risk of further urate lowering
- Cardiovascular risk assessment given the knowledge-graph contraindication signals
- If pursuing the more plausible HPRT deficiency and Lesch-Nyhan signals: paediatric safety data, xanthine nephropathy and stone monitoring, and comparison with allopurinol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

