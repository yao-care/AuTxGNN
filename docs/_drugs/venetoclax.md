---
layout: default
title: Venetoclax
parent: Model Prediction Only (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax: From Acute Lymphoblastic Leukaemia and Richter Syndrome to Myeloid Leukaemia

## One-Sentence Summary

Venetoclax is an oral BCL-2 inhibitor, originally linked to acute lymphoblastic leukaemia and Richter syndrome in the TxGNN knowledge graph.
The TxGNN model predicts it may be effective for **myeloid leukaemia** (the most evidence-supported prediction in the data compiled for this report), with **37 clinical trials** and **20 publications** linked to this prediction.
Venetoclax-azacitidine in AML is already a labelled use elsewhere, so this is better described as an extension or confirmation than as novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic/lymphocytic leukaemia; Richter syndrome (knowledge graph indications; the ARTG indication text is not available) |
| Predicted New Indication | Chronic lymphocytic leukaemia/small lymphocytic lymphoma with IGHV somatic hypermutation (rank 1); the best-supported prediction is **myeloid leukaemia** (rank 4) |
| TxGNN Prediction Score | 99.55% (rank 1); 99.47% (myeloid leukaemia) |
| Evidence Level | L5 (rank 1 prediction); L1 for myeloid leukaemia |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the rank 1 prediction; Proceed with Guardrails for myeloid leukaemia |

**Note on the rank 1 prediction:** it has no linked trials and no relevant literature. It is a molecular subtype of CLL/SLL, which is already an approved venetoclax indication, so it is not true repurposing. Because it is rank 1 it is shown in the overview, but the detailed evidence below focuses on myeloid leukaemia, the best-supported prediction in the data.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for venetoclax are not available in the data compiled for this report. Venetoclax is, however, a selective BCL-2 inhibitor, and this is supported by the linked literature. It restores apoptosis in malignant cells that depend on BCL-2 for survival.

AML cells and leukaemic stem cells depend on BCL-2 and on mitochondrial apoptotic priming. Venetoclax combined with a hypomethylating agent (azacitidine or decitabine) is an established regimen for older or unfit patients with newly diagnosed AML. This is supported by a large body of Phase 1b to Phase 3 work and by review articles. Acute lymphoblastic leukaemia and AML are both blood cancers with BCL-2 dependence, so the mechanism plausibly carries across.

Other predictions share the BCL-2 rationale, with varying support:
- **Chronic myelogenous leukaemia, BCR-ABL1 positive (rank 5):** Phase 2 work combining venetoclax with BCR-ABL inhibitors, strongest in advanced-phase disease.
- **Follicular lymphoma (rank 7):** a strong rationale because of t(14;18) and BCL-2 overexpression, with several Phase 2 trials.
- **Hodgkin lymphoma (rank 3):** indirect evidence only. Most linked trials are in B-cell non-Hodgkin lymphoma, and classical Hodgkin lymphoma shows limited BCL-2 dependence.
- **Ewing sarcoma, metastatic neoplasm, malignant spiradenoma:** preclinical or very weak evidence. "Metastatic neoplasm" is a non-specific category that should be split into specific tumour types.

---

## Clinical Trial Evidence

Selected trials linked to the myeloid leukaemia prediction (the full set includes 37 registered trials):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06852222](https://clinicaltrials.gov/study/NCT06852222) | Phase 3 | Recruiting | 600 | Bleximenib vs placebo added to venetoclax + azacitidine in newly diagnosed AML with KMT2A or NPM1 alterations. Venetoclax is in the backbone, so this tests the added agent. |
| [NCT05177731](https://clinicaltrials.gov/study/NCT05177731) | Phase 3 | Active, not recruiting | 188 | Venetoclax + decitabine vs conventional "7+3" induction in young adults with AML |
| [NCT07132684](https://clinicaltrials.gov/study/NCT07132684) | Phase 3 | Recruiting | 240 | Venetoclax + azacitidine vs daunorubicin/idarubicin + cytarabine induction in fit older AML patients |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | Venetoclax added to fractionated busulfan conditioning in high-risk AML/MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax with busulfan, cladribine and fludarabine conditioning before transplant in AML/MDS |
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1b/2 | Recruiting | 96 | Ivosidenib + venetoclax ± azacitidine in IDH1-mutated myeloid disease |
| [NCT06696183](https://clinicaltrials.gov/study/NCT06696183) | Phase 2 | Recruiting | 60 | Gilteritinib with venetoclax and azacitidine in newly diagnosed FLT3-mutated AML |
| [NCT06429098](https://clinicaltrials.gov/study/NCT06429098) | Phase 2 | Active, not recruiting | 40 | Venetoclax-based, anthracycline-free regimen in CBFB::MYH11-positive AML |
| [NCT07228273](https://clinicaltrials.gov/study/NCT07228273) | Phase 2 | Recruiting | 102 | Venetoclax with FLAG-IDA vs standard induction in newly diagnosed AML |
| [NCT05144243](https://clinicaltrials.gov/study/NCT05144243) | Phase 4 | Active, not recruiting | 44 | Venetoclax + azacitidine in AML patients ineligible for intensive chemotherapy, in China |

No ANZCTR identifiers were available in the data compiled for this report.

**Important caveat:** the only Phase 3 trial with a venetoclax backbone (NCT06852222) tests an add-on drug rather than venetoclax itself, and it is still recruiting. Evidence level L1 is therefore based on the volume of trials, and the data do not include completed Phase 3 results for venetoclax.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29339097](https://pubmed.ncbi.nlm.nih.gov/29339097/) | 2018 | Phase 1b | Lancet Oncol | Venetoclax with decitabine or azacitidine in elderly patients with untreated AML: safety and preliminary efficacy |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Clinical analysis | Clin Cancer Res | Venetoclax + azacitidine in treatment-naïve AML with IDH1/2 mutations |
| [40913104](https://pubmed.ncbi.nlm.nih.gov/40913104/) | 2025 | Post hoc analysis | Leukemia | VIALE-A and M14-358: venetoclax + azacitidine vs azacitidine alone, stratified by age and AML composite model |
| [41075807](https://pubmed.ncbi.nlm.nih.gov/41075807/) | 2025 | Phase 1b/2 | Lancet Haematol | Enasidenib + venetoclax in IDH2-mutated relapsed/refractory AML or MDS |
| [42035228](https://pubmed.ncbi.nlm.nih.gov/42035228/) | 2026 | Phase 2 | Am J Hematol | Cladribine, low-dose cytarabine and venetoclax alternating with azacitidine + venetoclax in 190 older or unfit AML patients |
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomed Pharmacother | Venetoclax in adult AML |
| [38866760](https://pubmed.ncbi.nlm.nih.gov/38866760/) | 2024 | Review | Cell Death Dis | Venetoclax therapy and emerging resistance mechanisms in AML |
| [28161120](https://pubmed.ncbi.nlm.nih.gov/28161120/) | 2017 | DDI evaluation | Clin Ther | Venetoclax-posaconazole interaction in AML: dose adjustments |
| [40266036](https://pubmed.ncbi.nlm.nih.gov/40266036/) | 2025 | Clinical study | Pediatr Blood Cancer | Venetoclax alone or with chemotherapy in paediatric and young adult relapsed/refractory AML |
| [31048321](https://pubmed.ncbi.nlm.nih.gov/31048321/) | 2019 | Preclinical | Cancer Discov | Targeting mitochondrial structure sensitises AML to venetoclax |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11630D | Venclexta | Oral starter pack: 14 × 10 mg, 7 × 50 mg, 7 × 100 mg and 14 × 100 mg tablets | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCL-2 inhibitor, BH3-mimetic) |
| Myelosuppression Risk | Medium to high. Myelosuppression and tumour lysis syndrome are the most commonly encountered toxicities (PMID 35659041), and rise further in combination with hypomethylating agents or chemotherapy. |
| Emetogenicity Classification | Please refer to the Product Information (PI) |
| Monitoring Items | FBC with differential, electrolytes, uric acid, renal and liver function, particularly during dose ramp-up for tumour lysis syndrome risk |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified (20 shown in the data compiled for this report). Major interactions include:
  - aprepitant, dexamethasone, clarithromycin, eliglustat, rolapitant, fidaxomicin, cobicistat, deferiprone and samarium (153Sm) lexidronam.
  - Moderate interactions include alvimopan, loperamide, cimetidine, miconazole, rifaximin, clotrimazole, deferasirox and others.
  - The literature adds that strong CYP3A inhibitors such as posaconazole raise venetoclax exposure and require dose adjustment (PMID 28161120).

Warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (myeloid leukaemia); Hold (rank 1 CLL/SLL subtype)**

**Rationale:**
- Myeloid leukaemia has a strong mechanistic rationale and many Phase 1 to Phase 3 trials plus clinical literature. However, venetoclax-azacitidine in AML is already an established use, and the sole Phase 3 with a venetoclax backbone is still recruiting and tests an add-on agent.
- The rank 1 CLL/SLL subtype has no trials or literature in the data and is a subtype of an already approved indication, so it warrants no action beyond review of the existing label.

**To proceed, the following is needed:**
- TGA Product Information, to confirm the current ARTG approved indications and the safety warnings and contraindications (the label data were a blocking gap).
- Mechanism of action data from DrugBank.
- A guardrail plan covering CYP3A inhibitor interactions, myelosuppression and tumour lysis syndrome monitoring.
- Review of PBS listing and reimbursement criteria for AML.
- Subtype-specific data before considering the t(8;21) AML prediction.
- For Hodgkin lymphoma, Ewing sarcoma and metastatic neoplasm: no action until specific clinical evidence emerges. Metastatic neoplasm should be split into specific tumour types.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

