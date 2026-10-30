---
layout: default
title: Enfortumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Enfortumab Vedotin: predicted new indication Leprosy (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Enfortumab Vedotin: From Its Registered Use to Leprosy (Top TxGNN Prediction)
{: .text-alpha }

## One-Sentence Summary

Enfortumab vedotin (Padcev) is a Nectin-4-directed antibody-drug conjugate (ADC) with an MMAE cytotoxic payload, and it is registered in Australia as a single-ingredient intravenous product. The TxGNN model's top-ranked prediction is **leprosy**, but there are **0 clinical trials** and **0 publications** supporting it. The prediction is model-derived only and has no plausible mechanistic basis. Of the ten predictions reviewed, only **HER2-positive breast carcinoma** (rank 10) has any supporting evidence (one Phase 2 multicohort trial and class-level literature), and it is discussed below as the most credible research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Leprosy (rank 1); most evidence-supported alternative: HER2-positive breast carcinoma (rank 10) |
| TxGNN Prediction Score | 0.9953 (leprosy) |
| Evidence Level | L5 (leprosy); L3 (HER2-positive breast carcinoma) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold (leprosy); the HER2-positive breast carcinoma question is a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, enfortumab vedotin is an antibody-drug conjugate that targets Nectin-4, a cell-surface protein, and delivers the cytotoxic payload MMAE to cells expressing it. The literature compiled here describes its use in metastatic urothelial carcinoma, including in combination with pembrolizumab.

**Leprosy (rank 1):** No reasonable mechanistic link was identified. Leprosy is a bacterial infection, and a cytotoxic ADC directed at a tumour antigen is not a plausible treatment. The high score (0.9953) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Several other top-ranked predictions, such as cerebral infarction, homozygous familial hypercholesterolemia, HIV infection, and two veterinary herpesvirus diseases (malignant catarrhal fever and infectious bovine rhinotracheitis), show the same lack of plausibility. The two veterinary diseases share an identical score, which suggests an ontology-mapping artefact.

**Infection-related predictions with literature (CMV and candidiasis):** The only publications attached to these are a case report of severe ulcerative oesophagitis after enfortumab vedotin plus pembrolizumab, and a pharmacovigilance (FAERS) study of ADC risk signals in bladder cancer. Both describe adverse events, not therapeutic benefit. They are safety signals, not efficacy evidence.

**HER2-positive breast carcinoma (rank 10):** This is the only prediction with a plausible rationale. Nectin-4 is expressed in a subset of breast cancers, notably triple-negative and some HER2-positive tumours, which provides a possible target for MMAE delivery. However, efficacy in HER2-positive disease has not been confirmed.

---

## Clinical Trial Evidence

**Leprosy:** Currently no related clinical trials registered.

**HER2-positive breast carcinoma** (the only prediction with a registered trial):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) (EV-202) | Phase 2 | Active, not recruiting | 329 | Open-label, multicohort study of enfortumab vedotin in locally advanced or metastatic solid tumours; primary endpoint is objective response rate (RECIST v1.1). Breast cancer is among the cohorts, but results were not available and the study is not specific to HER2-positive disease. |

No ANZCTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

**Leprosy:** Currently no related literature available.

**HER2-positive breast carcinoma** (class-level and indirect evidence only; none directly tests enfortumab vedotin in this disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42480966](https://pubmed.ncbi.nlm.nih.gov/42480966/) | 2026 | Review | Cancer Letters | ADCs against multidrug-resistant cancers: biomarker-guided patient selection, payload engineering, linker chemistry and bystander effects. |
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Review | Crit Rev Oncol Hematol | Narrative synthesis of real-world evidence for 10 recently approved oncology drugs. |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | Molecular pathology of bladder cancer. |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | Overview of ADCs, including novel targets and payloads. |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Preclinical | Cancer Letters | Persister polyploid giant cancer cells mediate resistance to HER2-directed ADCs; only indirectly relevant. |

**Safety-related publications attached to other predictions:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Case report | Reports (MDPI) | Severe diffuse ulcerative oesophagitis in a 72-year-old man with metastatic urothelial carcinoma treated with enfortumab vedotin plus pembrolizumab. |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Pharmacovigilance (FAERS) | Clinical Epidemiology | Real-world risk signals of ADCs in bladder cancer. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13634N | Padcev | Powder for I.V. infusion 20 mg | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate with a cytotoxic MMAE payload) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; haematological parameters (FBC) and liver and renal function are generally relevant for cytotoxic payloads |
| Handling Protection | Contains a cytotoxic payload; follow local cytotoxic drug handling requirements and the PI |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction screen returned 100 interacting drugs in total (20 shown in the data compiled for this report). Most are rated Moderate, and the list is dominated by antidiabetic agents.
- **Major:** Clarithromycin
- **Moderate (examples):** Aprepitant; antidiabetic agents including metformin, pioglitazone, acarbose, glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide, and the DPP-4 inhibitors (alogliptin, linagliptin, saxagliptin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin) and GLP-1 agonists (albiglutide, dulaglutide, exenatide)

**Safety signals from the literature:** Severe ulcerative oesophagitis has been reported with enfortumab vedotin plus pembrolizumab (single case report), and a FAERS study has characterised real-world ADC risk signals in bladder cancer.

---

## Conclusion and Next Steps

**Decision: Hold** (for leprosy and the other computational predictions). HER2-positive breast carcinoma may be considered a research question only.

**Rationale:**
- The top-ranked prediction, leprosy, has no clinical, literature or mechanistic support, and a cytotoxic oncology ADC is not a plausible treatment for a bacterial infection. All ten predictions sit at evidence level L5 except HER2-positive breast carcinoma (L3), which rests on one Phase 2 multicohort trial without available results and on indirect, class-level literature.

**To proceed, the following is needed:**
- Retrieve the TGA-approved Product Information, including approved indications, warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism of action data
- Obtain results from EV-202 (NCT04225117), particularly the breast cancer cohort, and Nectin-4 expression data in HER2-positive breast cancer
- Check whether any cohort-level data separate HER2-positive from triple-negative disease
- Review the clinical significance of the interaction signals (especially clarithromycin) against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

