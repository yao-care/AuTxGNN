---
layout: default
title: Zanubrutinib
parent: Model Prediction Only (L5)
nav_order: 788
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zanubrutinib: predicted new indication Myeloid leukaemia (evidence level L5). Approved use: Mantle cell lymphoma, B-cell neoplasm, lymphosarcoma"
monitor_inn: "Zanubrutinib"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "Ewing sarcoma", "neuroblastoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive", "lymphoma, non-Hodgkin, familial", "acute lymphoblastic/lymphocytic leukemia"]
---

# Zanubrutinib
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

## Zanubrutinib: From Mantle Cell Lymphoma and B-Cell Malignancies to Myeloid Leukaemia
{: .text-alpha }

## One-Sentence Summary

Zanubrutinib is an oral Bruton tyrosine kinase (BTK) inhibitor, originally used for mantle cell lymphoma and other B-cell malignancies.
The TxGNN model predicts it may be effective for **myeloid leukaemia**, but there is **1 clinical trial** (a Phase 1 study with weak relevance) and **no publications** that directly study zanubrutinib in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma, B-cell neoplasm, lymphosarcoma (the ARTG record compiled for this report carries no indication text) |
| Predicted New Indication | Myeloid leukaemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 (mechanistic rationale only; no direct clinical studies in myeloid leukaemia) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Zanubrutinib is a selective, covalent BTK inhibitor. BTK is a core part of B-cell receptor signalling, and this is why the drug works in B-cell cancers such as mantle cell lymphoma, chronic lymphocytic leukaemia (CLL) and Waldenström macroglobulinaemia.

BTK is also expressed in myeloid-lineage cells, where it contributes to B-cell receptor, Toll-like receptor and chemokine signalling. This gives a biological rationale for the model's prediction.

However, the link is indirect. The publications retrieved concern zanubrutinib in CLL/SLL, mantle cell lymphoma and Waldenström macroglobulinaemia, not myeloid leukaemia. The only trial found tests a different drug (PRT2527, a CDK9 inhibitor), with zanubrutinib as one possible combination partner in a B-cell malignancy setting. The high TxGNN score is not backed by direct clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose-escalation study of PRT2527 (CDK9 inhibitor) alone or combined with zanubrutinib or venetoclax in relapsed/refractory haematologic malignancies. Results are not summarised in the data compiled. Relevance to myeloid leukaemia is weak. |

## Literature Evidence

None of the publications below studies zanubrutinib in myeloid leukaemia. They cover related B-cell diseases and general safety.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT (Phase 3) | J Clin Oncol | SEQUOIA 5-year follow-up: zanubrutinib vs bendamustine plus rituximab in treatment-naive CLL/SLL |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort (Phase 2) | Lancet Haematol | Zanubrutinib in B-cell malignancies intolerant of earlier BTK inhibitors |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | Updated results: zanubrutinib well tolerated and effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort | Blood Adv | Pooled analysis of zanubrutinib in CLL/SLL with del(17p) and/or TP53 mutation (N = 301) |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Tyrosine kinase inhibitors in chronic leukaemias (CML and CLL) |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK inhibitors in Waldenström macroglobulinaemia |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Cohort | Clin Lymphoma Myeloma Leuk | Hepatitis B reactivation in patients receiving BTK inhibitors, including zanubrutinib |
| [42192981](https://pubmed.ncbi.nlm.nih.gov/42192981/) | 2026 | Review | Cancers | BTK inhibitors in CLL: selectivity, hypogammaglobulinaemia and infection risk |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Rare coexistence of Waldenström macroglobulinaemia and B-cell ALL; not efficacy evidence |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12891L | Brukinsa | Capsule 80 mg (oral) | Not stated in the record compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. Cytopenias are a recognised concern with this drug class. |
| Emetogenicity Classification | Please refer to the PI. This is an oral targeted agent. |
| Monitoring Items | Full blood count (with differential) is the main parameter. Also consider liver function and hepatitis B status, given reports of HBV reactivation with BTK inhibitors. |
| Handling Protection | Please refer to the PI and local institutional policy for oral anticancer agents |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. The Major-level interactions in the portion reviewed include:
  - Aprepitant
  - Acetylsalicylic acid (aspirin)
  - Dexamethasone
  - Clarithromycin
  - Cobicistat
  - Deferasirox
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Ibritumomab tiuxetan
  - Tositumomab (I-131)

  Moderate-level interactions include cimetidine, miconazole, clotrimazole and several others.
- **Literature-based concerns**: The retrieved publications report hepatitis B virus reactivation with BTK inhibitors, and hypogammaglobulinaemia with increased infection risk.

Warnings and contraindications from the TGA-approved Product Information were not available. Please refer to the PI for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no direct evidence supports zanubrutinib in myeloid leukaemia. The only trial is an early-phase study of a different drug, and the literature covers B-cell diseases. The rationale for BTK signalling in myeloid cells has not been tested clinically.

**To proceed, the following is needed:**
- Preclinical or translational data showing BTK dependence in myeloid leukaemia models
- Detailed mechanism of action data
- Results and cohort details from NCT05665530, to see whether any myeloid patients were treated with zanubrutinib
- TGA-approved PI warnings and contraindications, to complete safety screening
- Consideration of other predicted indications for this drug. B-cell non-Hodgkin lymphoma (rank 9) has far stronger trial and publication support, though it largely extends the existing B-cell neoplasm label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

