---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Calcitriol: predicted new indication Top-ranked: obsolete vitamin D deficiency . Best-supported: hypophosp… (evidence level L5). Approved use: Hypercalcaemia, nephrocalcinosis, phosphorus metabolism …"
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets", "hypophosphatemic rickets", "osteomalacia (disease)", "vitamin D-dependent rickets"]
---

# Calcitriol
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

# Calcitriol: From Hypercalcaemia and Mineral Metabolism Disorders to Hypophosphataemic Rickets

## One-Sentence Summary

Calcitriol is the active form of vitamin D, originally used for mineral metabolism disorders such as hypoparathyroidism, renal osteodystrophy and hypophosphataemia.
The TxGNN model's top-ranked prediction is "obsolete vitamin D deficiency", but the best-supported new direction is **hypophosphataemic rickets (including X-linked hypophosphataemia)**, with **2 clinical trials** and **more than 15 publications** supporting it.
Evidence for the other predicted indications is weak or indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphataemia, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Top-ranked: obsolete vitamin D deficiency (rank 1, a retired ontology term). Best-supported: hypophosphataemic rickets (ranks 7 and 8) |
| TxGNN Prediction Score | 99.96% (top-ranked); 98.08% (hypophosphataemic rickets); 99.28% (hereditary hypophosphataemic rickets) |
| Evidence Level | L5 for the top-ranked prediction; L2 for hypophosphataemic rickets |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the top-ranked prediction; Proceed with Guardrails for hypophosphataemic rickets |

The top-ranked prediction has no trials or literature, and the term is flagged as obsolete in the ontology. Nutritional vitamin D deficiency is normally treated with cholecalciferol or ergocalciferol, not calcitriol. The rest of this report therefore focuses on the best-supported candidate, hypophosphataemic rickets.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Calcitriol is the active hormonal form of vitamin D (1,25-dihydroxyvitamin D3). It supports intestinal absorption of calcium and phosphate and bone mineralisation.

In X-linked hypophosphataemia (XLH), excess FGF23 suppresses renal 1-alpha-hydroxylase and phosphate reabsorption. This leaves endogenous calcitriol inappropriately low. Calcitriol, usually with phosphate, replaces the deficient active vitamin D. This is long-established standard therapy, and it fits closely with calcitriol's existing use in hypophosphataemia and other phosphate metabolism disorders.

Other predictions have a weaker or different basis:
- **Familial isolated hypoparathyroidism:** a strong mechanistic fit, but arguably an extension of an existing indication rather than true repurposing. No trials or literature were found.
- **Vitamin D-dependent rickets:** calcitriol is the established therapy for type 1A (CYP27B1 deficiency), but evidence is limited to case reports, case series and reviews (L4).
- **Osteomalacia:** plausible for phosphate-wasting or calcitriol-deficient forms, but the evidence is indirect (L4). Nutritional osteomalacia is usually treated with native vitamin D.
- **Renal tubular acidosis:** evidence is indirect (L4). One 1984 study found that renal tubular acidosis does not alter circulating calcitriol.
- **Acromesomelic dysplasia, craniofacial conodysplasia and Dahlberg-Borer-Newcomer syndrome:** no clear mechanistic rationale. These are likely artefacts of graph proximity or term mapping (L5).

---

## Clinical Trial Evidence

Both trials below apply to hypophosphataemic rickets and hereditary hypophosphataemic rickets.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Completed | 16 | Calcitriol monotherapy (without phosphate) for one year in children and adults with XLH. It tests effects on serum phosphate, skeletal mineralisation, kidney calcification and growth. |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High versus low dose active vitamin D (e.g. calcitriol) combined with neutral phosphate in children with XLH, to establish weight-based dosing. |

No ANZCTR trials were identified in the data compiled for this report. No clinical trials were registered for the other predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35484227](https://pubmed.ncbi.nlm.nih.gov/35484227/) | 2022 | Consensus Statement | Nat Rev Endocrinol | Interdisciplinary management of FGF23-related phosphate wasting syndromes, including XLH |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | XLH: PHEX defects, FGF23 excess, renal phosphate wasting and reduced calcitriol synthesis |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcif Tissue Int | Diagnosis and therapy of XLH |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment with vitamin D and its analogues, including calcitriol |
| [30454743](https://pubmed.ncbi.nlm.nih.gov/30454743/) | 2019 | Review | Pediatr Clin North Am | Conventional treatment is phosphate plus calcitriol, requiring monitoring for adverse effects such as nephrocalcinosis |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Review | Metabolism | Management of XLH in adults |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical study | J Clin Invest | High-dose calcitriol with phosphorus for healing bone disease in XLH rickets/osteomalacia |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical study | Calcif Tissue Int | Bone mass in children with familial hypophosphataemic rickets after calcitriol and phosphate |
| [2157942](https://pubmed.ncbi.nlm.nih.gov/2157942/) | 1990 | Cohort | Metabolism | Calcitriol is beneficial in vitamin D-dependent rickets type 1 and X-linked hypophosphataemic rickets |
| [36405822](https://pubmed.ncbi.nlm.nih.gov/36405822/) | 2022 | Case series | Front Pediatr | Long-term outcomes of 12 children with vitamin D-dependent rickets type 1A |

The literature is mostly reviews, consensus statements and older clinical studies. No completed Phase 3 randomised controlled trial was identified.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13457G | Rocaltrol | Capsule 0.25 microgram (oral) | Not available in the data compiled for this report |

There is one valid single-ingredient entry and no cancelled entries.

---

## Safety Considerations

Safety data from the TGA Product Information was not available, so please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

The following came from the knowledge graph and the interaction database, not from label text.

- **Knowledge graph contraindication signals:** kidney disease, sarcoidosis, hypercalcaemia, nephrocalcinosis, nephrolithiasis, hyperphosphataemia, hypervitaminosis, acute urate nephropathy, pyoureter and arteriosclerosis obliterans.
- **Drug interactions (100 recorded):**
  - **Major:** cholecalciferol, calcifediol and burosumab.
  - **Moderate (examples):** thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone), digoxin and digitoxin, anticonvulsants (fosphenytoin, carbamazepine), barbiturates, bile acid sequestrants (cholestyramine, colesevelam, colestipol), aluminium hydroxide and topical calcipotriol.
- **Condition-specific guardrails for XLH:** monitor calcium, phosphate and PTH, and perform renal ultrasound for hypercalciuria, nephrocalcinosis and secondary or tertiary hyperparathyroidism. Burosumab is an alternative treatment but has a major recorded interaction with calcitriol.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (obsolete vitamin D deficiency); Proceed with Guardrails for hypophosphataemic rickets**

**Rationale:**
- The top-ranked prediction has no trials or literature, uses a retired ontology term, and is not standard calcitriol use. Hypophosphataemic rickets is mechanistically well grounded and supported by two trials, consensus statements and reviews. It is capped at L2 because there is no completed Phase 3 RCT and trial statuses and sample sizes are limited.
- Calcitriol is already established therapy for this condition internationally, so Australian use would be an extension of existing practice. The current ARTG entry has no indication text on record.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm approved indications, warnings and contraindications
- Mechanism of action data for the record
- Results and publication of NCT03748966 and the status of NCT03820518
- A monitoring plan (calcium, phosphate, PTH, renal ultrasound) and guidance on the burosumab interaction
- Clarification of whether the Rocaltrol label covers rickets or hypophosphataemia
- For lower-ranked predictions, disease-specific evidence before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

