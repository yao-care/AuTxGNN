---
layout: default
title: Lorlatinib
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lorlatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer"
monitor_inn: "Lorlatinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Lorlatinib
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

## Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis
{: .text-alpha }

## One-Sentence Summary

Lorlatinib is an oral kinase inhibitor originally used to treat non-small cell lung cancer (NSCLC) and lung cancer.
The TxGNN model ranks **gingival fibromatosis** as its top predicted new indication (score 99.81%), but **no clinical trials and no publications** support this prediction.
It is a computational signal only and should not be treated as actionable evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer; lung cancer (the ARTG indication text is not available in the data compiled for this report) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lorlatinib is not available in the data compiled for this report. From the literature retrieved, lorlatinib is a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor. It is used in ALK-positive advanced NSCLC, where it has Phase 3 evidence (the CROWN study).

The review found **no identifiable link** between ALK/ROS1 inhibition and gingival fibromatosis. The high TxGNN score appears to be a computational artefact of the knowledge graph rather than a biological rationale. Gingival fibromatosis is not known to be driven by ALK or ROS1 signalling.

The other top-ranked predictions are similarly weak:

- **Fibroma of lung, hamartoma of lung, lung benign neoplasm and pulmonary sulcus neoplasm** likely score highly because of their proximity to the approved lung cancer indication in the knowledge graph. They are not known to be ALK-driven. The publications retrieved for lung benign neoplasm concern ALK-positive NSCLC and cannot be transferred to benign tumours.
- **Lung hilum carcinoma** is the most plausible prediction. ALK-positive disease would be expected to respond, but this is effectively within the approved NSCLC indication rather than true repurposing. The only supporting evidence is a single 2023 case report of pathological complete response after neoadjuvant lorlatinib.
- **Lung germ cell tumour** has no direct evidence. The literature relates to ALK-driven neuroblastoma (including a Phase 1 trial), ALK-fusion glioma and pulmonary large-cell neuroendocrine carcinoma. This suggests activity in ALK-driven tumours generally, not in germ cell tumours.
- **Inclusion body myopathy with Paget disease, junctional epidermolysis bullosa and the leukomelanoderma syndrome** have no mechanistic link to ALK signalling. The publications retrieved for the last of these are adverse-event reports, not therapeutic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

The only literature found relates to lower-ranked predictions, and all of it concerns ALK-driven cancers or lorlatinib adverse events:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33207094](https://pubmed.ncbi.nlm.nih.gov/33207094/) | 2020 | RCT (Phase 3) | N Engl J Med | First-line lorlatinib vs crizotinib in advanced ALK-positive NSCLC (CROWN) |
| [38819031](https://pubmed.ncbi.nlm.nih.gov/38819031/) | 2024 | RCT (Phase 3, 5-year follow-up) | J Clin Oncol | Long-term progression-free survival and intracranial benefit of lorlatinib vs crizotinib in NSCLC |
| [42217582](https://pubmed.ncbi.nlm.nih.gov/42217582/) | 2026 | Phase 3 update | Ann Oncol | 7-year CROWN update confirming long-term outcomes |
| [36535300](https://pubmed.ncbi.nlm.nih.gov/36535300/) | 2023 | RCT subanalysis | Lancet Respir Med | 3-year CROWN data, including intracranial activity |
| [39368244](https://pubmed.ncbi.nlm.nih.gov/39368244/) | 2024 | Network meta-analysis | Lung Cancer | Lorlatinib compared with other ALK inhibitors as first-line therapy |
| [37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/) | 2023 | Phase 1 trial | Nat Med | Lorlatinib with or without chemotherapy in ALK-driven relapsed or refractory neuroblastoma |
| [37934724](https://pubmed.ncbi.nlm.nih.gov/37934724/) | 2023 | Case report | Am J Case Rep | Pathological complete response after neoadjuvant lorlatinib in advanced ALK-positive lung cancer |
| [38554546](https://pubmed.ncbi.nlm.nih.gov/38554546/) | 2024 | Review | Lung Cancer | Practical guide to managing lorlatinib adverse events |

These papers support lorlatinib's use in ALK-positive NSCLC. They do not support the predicted new indication.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12091J | Lorviqua | Tablet 100 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. The literature highlights lipid profile (hypercholesterolaemia and hypertriglyceridaemia), central nervous system effects and pulmonary symptoms |
| Handling Protection | Please refer to the PI and local institutional policy for oral anticancer agents |

---

## Safety Considerations

Warnings and contraindications are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

**Drug interactions:** A screen identified 100 potential interactions. The main ones from the listed entries are:

- **Major:** dexamethasone, clarithromycin
- **Moderate (examples):** hydrocortisone, betamethasone, triamcinolone, bupropion, aprepitant, cimetidine, morphine, alosetron, eliglustat, dronabinol, naldemedine, naloxegol
- **Moderate (glucose-lowering agents):** chlorpropamide, glimepiride, dapagliflozin, empagliflozin, saxagliptin, linagliptin

**Safety signals from the retrieved literature (case-level or observational):**

- Hyperlipidaemia and complex dyslipidaemia
- Acute respiratory distress syndrome
- Pulmonary toxicity when given concurrently with anti-GD2 antibody therapy
- Drug-induced Sweet syndrome
- Metabolic effects such as weight gain

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, gingival fibromatosis, has a high model score but no clinical trials, no publications and no plausible mechanistic link to ALK/ROS1 inhibition. Evidence is L5 (model prediction only). Phase 3 evidence exists only for the already-approved NSCLC indication and cannot be extended to this condition.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to test whether any biological rationale exists
- Preclinical or mechanistic evidence linking ALK/ROS1 signalling to gingival fibromatosis
- The ARTG approved indication text and TGA Product Information, to complete the safety screen
- If a lung-related use is of interest, a focused evaluation of **lung hilum carcinoma** restricted to ALK-positive disease, which falls largely within the existing NSCLC indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

