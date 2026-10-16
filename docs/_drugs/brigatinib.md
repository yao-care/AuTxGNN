---
layout: default
title: Brigatinib
parent: Model Prediction Only (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brigatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer and lung cancer"
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib is an oral tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC) and lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high graph-based score, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model prediction only, and it should be treated as a hypothesis, not a repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer and lung cancer (the ARTG indication text was not available in the data compiled for this report) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, brigatinib is a tyrosine kinase inhibitor, and the supporting literature describes it as a next-generation anaplastic lymphoma kinase (ALK) inhibitor. Its efficacy in ALK-positive NSCLC is well established.

No mechanistic link between brigatinib and gingival fibromatosis can be identified in the data compiled for this report. The TxGNN score is derived from knowledge-graph patterns, not from trials, literature or biological evidence. Any rationale, such as kinase inhibition in a fibrotic or proliferative tissue disorder, would be speculative.

The other top-ranked predictions are also unsupported or only indirectly supported:

| Rank | Predicted Disease | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Fibroma of lung | 99.86% | L5 | Prediction only |
| 3 | Hamartoma of lung | 99.85% | L5 | Prediction only |
| 4 | Lung hilum carcinoma | 99.85% | L5 | Plausible given adjacency to the NSCLC indication, but no direct evidence. Any benefit would likely fall under the existing NSCLC label if ALK-positive |
| 5 | Lung benign neoplasm | 99.85% | L5 | The literature hits are about ALK-positive NSCLC (an existing indication), so this is a term-matching artifact |
| 7 | Lung germ cell tumour | 99.84% | L4 | Indirect evidence only, from ALK-driven tumours outside NSCLC |
| 10 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.83% | L4 | Literature relates to NF2-related schwannomatosis, a different disease |

One signal may merit separate evaluation: brigatinib has been reported in **NF2-related schwannomatosis** (see below). It is not evidence for the predicted syndrome and should be assessed as a distinct indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For context, the following publications were retrieved for other lower-ranked predictions. They do **not** support the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/) | 2024 | Case series | N Engl J Med | Brigatinib in NF2-related schwannomatosis with progressive tumours |
| [34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/) | 2021 | Preclinical | PLoS One | Brigatinib shrank NF2-deficient meningioma and schwannoma through inhibition of multiple tyrosine kinases, but not ALK |
| [34371380](https://pubmed.ncbi.nlm.nih.gov/34371380/) | 2021 | Case report | ESMO Open | Sustained response in refractory metastatic pheochromocytoma with an ALK R1192P mutation |
| [39395329](https://pubmed.ncbi.nlm.nih.gov/39395329/) | 2024 | Case report | Respir Investig | Therapeutic effect in lung large cell neuroendocrine carcinoma with EML4-ALK fusion |
| [27049722](https://pubmed.ncbi.nlm.nih.gov/27049722/) | 2016 | Preclinical | Oncotarget | Brigatinib suppressed ALK-positive neuroblastoma cells, Drosophila and mice |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT | N Engl J Med | ALTA-1L: brigatinib vs crizotinib in ALK-inhibitor-naive ALK-positive NSCLC (approved indication) |
| [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/) | 2021 | RCT | J Thorac Oncol | Final ALTA-1L results (approved indication) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11974F | Alunbrig | Tablet 90 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. A pharmacovigilance analysis (PMID 34418561) and real-world data (PMID 41378495) have examined cardiovascular toxicity with ALK inhibitors, and a case report (PMID 34987411) described fatal tumour lysis syndrome |
| Handling Protection | Please refer to the PI and local cytotoxic or hazardous drug handling policies |

---

## Safety Considerations

Key warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions** (100 interactions recorded; examples below):

- **Major:** aprepitant, dexamethasone, clarithromycin
- **Moderate:** acarbose, famotidine, ranitidine, rabeprazole, cimetidine, metformin, pioglitazone, albiglutide, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, loperamide, morphine, cisapride, clotrimazole

Several of these (acid-suppressing agents, CYP3A-active drugs and antidiabetic agents) are commonly co-prescribed, so a full interaction review would be needed before any new use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.89%) for gingival fibromatosis is a graph-based prediction only. There are no clinical trials, no supporting literature and no identifiable mechanistic link, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for brigatinib (DrugBank)
- A biological rationale linking tyrosine kinase inhibition to gingival fibromatosis, supported by preclinical data
- Warnings and contraindications from the TGA-approved PI, which is a blocking gap for safety screening
- Separate evaluation of **NF2-related schwannomatosis** as a distinct candidate indication, given the 2024 NEJM report and preclinical findings
- Route compatibility assessment (brigatinib is available only as an oral tablet in Australia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

