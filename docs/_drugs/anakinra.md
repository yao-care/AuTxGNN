---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Anakinra: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Anakinra"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
---

# Anakinra
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

## Anakinra: From Rheumatoid Arthritis to Extracutaneous Mastocytoma
{: .text-alpha }

## One-Sentence Summary

Anakinra is an interleukin-1 (IL-1) receptor antagonist, originally used for rheumatoid arthritis and cryopyrin-associated periodic syndromes (including CINCA syndrome).
The TxGNN model's top-ranked prediction is **extracutaneous mastocytoma**, but **no clinical trials and no publications** support this specific prediction.
Other lower-ranked predictions have more evidence, particularly **familial Mediterranean fever** and **pyogenic autoinflammatory syndromes (PAPA/PASH/PAPASH)**, which are supported by case-level and review literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; cryopyrin-associated periodic syndrome; CINCA syndrome (the approved indication text for the Australian ARTG entry is not available) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

For context, the other predicted indications in this evaluation were graded as follows:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Extracutaneous mastocytoma | 0.9993 | L5 | Hold |
| 2 | Hepatic infarction | 0.9989 | L5 | Hold |
| 3 | Autosomal recessive familial Mediterranean fever | 0.9989 | L5 | Research Question |
| 4 | Aggressive systemic mastocytosis | 0.9988 | L5 | Hold |
| 5 | Hepatic veno-occlusive disease | 0.9988 | L5 | Hold |
| 6 | Peliosis hepatis | 0.9985 | L5 | Hold |
| 7 | Oligoarticular JIA without anti-nuclear antibodies | 0.9985 | L5 | Hold |
| 8 | Oligoarticular JIA with anti-nuclear antibodies | 0.9985 | L5 | Hold |
| 9 | Pyogenic autoinflammatory syndrome | 0.9983 | L3 | Research Question |
| 10 | Unclassified autoinflammatory syndrome | 0.9981 | L3 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for anakinra is not available in the data compiled for this report. Anakinra is, however, a recombinant IL-1 receptor antagonist, and its efficacy in rheumatoid arthritis and cryopyrin-associated periodic syndromes is established. Mechanistically, it may be applicable to conditions in which IL-1 drives inflammation.

For the top-ranked prediction, **extracutaneous mastocytoma**, the link is plausible but unverified: IL-1 may be involved in mast cell-driven inflammation. The 0.9993 score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There are no supporting trials or publications.

The better-supported predictions are those that are autoinflammatory and IL-1-driven:

- **Familial Mediterranean fever (FMF):** This disease involves pyrin inflammasome dysregulation and excess IL-1β, so IL-1 blockade is mechanistically coherent. Evidence is at case series and review level.
- **PAPA/PASH/PAPASH syndromes:** These involve PSTPIP1-related inflammasome activation and IL-1-driven inflammation, so IL-1 blockade is mechanistically well founded.
- **Unclassified autoinflammatory syndromes:** These often show IL-1-mediated inflammation, supporting an empirical approach, although the evidence is heterogeneous.

Some predictions are poorly supported. Hepatic infarction is an ischaemic/vascular event for which IL-1 blockade is not an established treatment. For oligoarticular juvenile idiopathic arthritis (JIA), anakinra is established in systemic JIA, but oligoarticular disease has a different, largely adaptive, T-cell-driven pathophysiology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (extracutaneous mastocytoma), or for any of the other nine predicted indications.

---

## Literature Evidence

No literature is available for the top-ranked prediction (extracutaneous mastocytoma). The most relevant publications below relate to the best-supported predictions.

**Familial Mediterranean fever (rank 3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case series / Review | Semin Arthritis Rheum | Evaluates IL-1-targeting drugs in FMF, given pyrin's role in IL-1 maturation and secretion |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | Reviews IL-1β biological treatment of FMF in patients not controlled by colchicine |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Review | Curr Med Chem | Reviews colchicine and biologic agents for FMF |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohort | Rheumatol Int | Canakinumab effective in FMF resistant or intolerant to colchicine and/or anakinra (IL-1 class evidence) |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case report | Nephrol Dial Transplant | Successful anakinra treatment of FMF and outcome after renal transplantation |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case report | Nephrol Dial Transplant | Beneficial effect of IL-1 inhibitors in FMF complicated by amyloidosis and renal failure |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Case report | Rheumatol Int | Anakinra efficacy in a patient with colchicine-resistant FMF |

**Pyogenic autoinflammatory syndromes (rank 9)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Scoping review | Front Immunol | Efficacy and safety of anakinra and canakinumab in PSTPIP1-associated inflammatory diseases |
| [24275598](https://pubmed.ncbi.nlm.nih.gov/24275598/) | 2013 | Review | Semin Immunol | Reviews the broad role of IL-1 blockade across inflammatory diseases |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Case report and review | Cureus | Anakinra in PAPASH spectrum disorder |
| [38006373](https://pubmed.ncbi.nlm.nih.gov/38006373/) | 2023 | Case report / Review | Acta Dermatovenerol Croat | PAPA syndrome: challenges in achieving long-term remission |

**Unclassified autoinflammatory syndrome (rank 10)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36589607](https://pubmed.ncbi.nlm.nih.gov/36589607/) | 2022 | Retrospective cohort | Arch Rheumatol | Single-centre experience with anakinra in paediatric rheumatic diseases |
| [41904303](https://pubmed.ncbi.nlm.nih.gov/41904303/) | 2026 | Case report | Eur Arch Otorhinolaryngol | TRAPS-like unclassified syndrome treated successfully with canakinumab |
| [37747561](https://pubmed.ncbi.nlm.nih.gov/37747561/) | 2024 | Registry cohort | Rheumatol Int | Clinical and genetic characteristics of patients in the German anti-IL-1 registry (GARROD) |

**Other predictions**

- *Aggressive systemic mastocytosis (rank 4):* The retrieved papers ([40718535](https://pubmed.ncbi.nlm.nih.gov/40718535/), [25840575](https://pubmed.ncbi.nlm.nih.gov/25840575/)) are case reports on Schnitzler syndrome, not mastocytosis. They are mismatched and do not support this prediction.
- *Oligoarticular JIA (ranks 7 and 8):* The only item is a general JIA review ([28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/)), with no subtype-specific anakinra data.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10263E | Kineret | Injection 100 mg in 0.67 mL single use pre-filled syringe | Not available in the data compiled for this report |

---

## Safety Considerations

**Drug Interactions** (100 interactions were identified in the interaction database; the main ones are listed below):

- **Major:** Deferiprone
- **Moderate:**
  - Corticosteroids: hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone (including ophthalmic)
  - Simvastatin
  - Anticoagulants: apixaban, rivaroxaban, dicoumarol
  - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, iobenguane (I-131), tositumomab and tositumomab (I-131)
- **Minor:** Zinc salts (acetate, gluconate, sulfate)

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, extracutaneous mastocytoma, rests on a score from the TxGNN model (deep learning) alone, which may reflect similarities the model learned between related diseases, not biological evidence, with no registered trials or publications (L5). The better-supported predictions (familial Mediterranean fever, PSTPIP1-associated syndromes and unclassified autoinflammatory syndromes) reach only L3 on case series and review evidence, with no anakinra-specific randomised trials. These are best treated as research questions rather than candidates for immediate clinical use.

**To proceed, the following is needed:**
- Detailed mechanism of action data for anakinra
- The TGA-approved Product Information (warnings, contraindications and approved indication text for ARTG 10263E)
- For extracutaneous mastocytoma: any preclinical or clinical evidence of IL-1 involvement, before further consideration
- For familial Mediterranean fever and PSTPIP1-associated syndromes: a systematic review of anakinra-specific data and, where feasible, a prospective study or registry in colchicine-resistant patients
- Review of the interaction profile, particularly the major interaction with deferiprone and combined use with corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

