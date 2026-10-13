---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation (Original Indication Not Recorded) to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is an oral direct Factor Xa inhibitor used as an anticoagulant. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but the data compiled for this report contain **no clinical trials** and **no publications** that directly support this use. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Australian licence data (the approved indication text is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Rivaroxaban is a direct Factor Xa inhibitor. Detailed mechanism of action data are not available in the data compiled for this report, so this description draws on general pharmacological knowledge.

Rheumatoid arthritis (RA) involves chronic inflammation with activation of coagulation and an elevated thrombotic risk. One retrieved review discusses thrombin generation in autoimmune disease. This offers only a plausible, indirect link through the coagulation-inflammation axis.

There is no evidence that rivaroxaban modifies RA disease activity. The high TxGNN score is a computational prediction without clinical support. The other retrieved papers concern venous thromboembolism, atrial fibrillation adherence, and a single case report. None of them tests rivaroxaban as an RA treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity venous thromboembolism diagnosis and treatment. Recurrent VTE occurs in 20–36% of patients within 10 years. Not RA-specific. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay can assess hypercoagulability in autoimmune disease. Background only, no drug treatment data. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation. Not RA-related. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Perioperative embolic cerebral infarction in an 88-year-old woman with atrial fibrillation, CKD and RA on oral steroids. RA is a comorbidity, not a treatment target. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11633G | Rivaroxaban Dr.Reddy's | Tablet 10 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Disease associations from the knowledge graph** (drug–disease contraindication links in the TxGNN knowledge graph, not label text): liver failure, kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease.
- **Drug Interactions**: The interaction query returned 100 records. The first 20 were provided, and the major-level ones among them are:
  - Acetylsalicylic acid
  - Cobicistat
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab (I-131)

  Moderate-level interactions include aprepitant, dexamethasone, cimetidine, clarithromycin, eliglustat, miconazole, clotrimazole, rolapitant and sugammadex, among others.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no registered trials, no literature testing rivaroxaban in RA, and only an indirect coagulation-inflammation link. The evidence level is L5.

**To proceed, the following is needed:**
- Preclinical or clinical data showing that Factor Xa inhibition affects RA disease activity
- Detailed mechanism of action data
- The approved indication text and PI warnings and contraindications for the Australian product
- A safety review covering bleeding risk, hepatic and renal impairment, and major interactions, particularly with aspirin and with antirheumatic or corticosteroid co-therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

