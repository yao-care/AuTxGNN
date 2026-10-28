---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 186
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Crizotinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer (lung cancer)"
monitor_inn: "Crizotinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
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

## Crizotinib: From Non-Small Cell Lung Cancer to fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Crizotinib is an oral tyrosine kinase inhibitor originally used to treat ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model ranks **fibromatosis, gingival** as its top predicted new indication, but this is a network-based prediction only, with **no clinical trials** and **no publications** supporting it.
Among the other predicted indications, only lung germ cell tumour has any trial-level (tumour-agnostic) evidence, and it too is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (lung cancer) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, crizotinib is an ATP-competitive inhibitor of the receptor tyrosine kinases ALK, ROS1 and c-MET. Its efficacy in ALK-rearranged and ROS1-rearranged NSCLC is well established.

For gingival fibromatosis, no mechanistic link to ALK, ROS1 or MET inhibition can be identified. The high TxGNN score (0.9981) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature were found to support it, so the prediction should be treated as a hypothesis rather than a lead.

Other predictions in the list show varying degrees of plausibility:
- **Lung hilum carcinoma, pulmonary sulcus neoplasm and lung benign neoplasm**: these overlap with the existing lung cancer indication. The Phase 3 RCTs found (PROFILE 1014, PROFILE 1007, ALEX, ALTA-1L) concern ALK-positive NSCLC, so they do not represent new-indication evidence. For benign lung neoplasms the match appears to be a disease-label artefact.
- **Lung germ cell tumour**: the only prediction with trial-level evidence, but those trials are tumour-agnostic, and any benefit would depend on an actionable ALK, ROS1 or MET alteration.
- **Hamartoma of lung**: the sole publication is a case report of an ALK-negative tumour, which does not support crizotinib activity.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (gingival fibromatosis). Currently no related clinical trials registered.

For context, the following tumour-agnostic trials were linked to the rank 7 prediction (lung germ cell tumour). Neither reports results specific to germ cell tumours.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01121588](https://clinicaltrials.gov/study/NCT01121588) | Phase 1 | Terminated | 44 | Phase 1b basket study of crizotinib in non-lung tumours with ALK genetic alterations; safety and activity in genomically selected tumours |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6452 | NCI-MATCH: genetically directed treatment in advanced, refractory solid tumours, lymphomas and myeloma; relevant only to alteration-matched patients |

---

## Literature Evidence

No publications were found for the top-ranked prediction (gingival fibromatosis). Currently no related literature available.

For context, the key publications linked to other predictions are shown below. They concern the approved NSCLC indication or are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23724913](https://pubmed.ncbi.nlm.nih.gov/23724913/) | 2013 | RCT (Phase 3) | N Engl J Med | Crizotinib versus chemotherapy in previously treated advanced ALK-positive lung cancer (approved indication) |
| [25470694](https://pubmed.ncbi.nlm.nih.gov/25470694/) | 2014 | RCT (Phase 3) | N Engl J Med | First-line crizotinib versus chemotherapy in ALK-positive lung cancer (approved indication) |
| [28586279](https://pubmed.ncbi.nlm.nih.gov/28586279/) | 2017 | RCT (Phase 3) | N Engl J Med | Alectinib versus crizotinib in untreated ALK-positive NSCLC |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT (Phase 3) | N Engl J Med | Brigatinib versus crizotinib in ALK-positive NSCLC |
| [31313100](https://pubmed.ncbi.nlm.nih.gov/31313100/) | 2019 | Review | Drugs | Crizotinib and newer inhibitors in ROS1-rearranged NSCLC |
| [33568345](https://pubmed.ncbi.nlm.nih.gov/33568345/) | 2021 | Clinical study | Clin Cancer Res | Crizotinib activity in ALK-aberrant relapsed/refractory neuroblastoma (Children's Oncology Group ADVL0912) |
| [34011083](https://pubmed.ncbi.nlm.nih.gov/34011083/) | 2021 | Case report | Medicine | ALK-negative lung inflammatory myofibroblastic tumour; does not support crizotinib activity |
| [39716454](https://pubmed.ncbi.nlm.nih.gov/39716454/) | 2024 | Case report | Am J Case Rep | Pathological complete response to neoadjuvant crizotinib plus chemotherapy in ROS1-positive lung adenocarcinoma |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10322G | Xalkori | Capsule 250 mg (oral) | Not available in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; the literature also highlights cardiac monitoring (bradycardia, QT prolongation) |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these.

- **Drug Interactions**: The interaction screen returned 100 interacting drugs; the first 20 are summarised here.
  - **Major**: clarithromycin, cisapride, dolasetron, eliglustat, granisetron. Several of these are associated with QT prolongation or CYP3A-mediated interactions.
  - **Moderate**: famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone, bisacodyl, budesonide, clotrimazole, among others.
- **Literature-reported adverse events** (case reports): cardiac toxicity including bradycardia and QT prolongation (PMID 29717400), sick sinus syndrome (PMID 25922742), erythema multiforme (PMID 25994067), and erosive oesophagitis in a paediatric patient (PMID 29357780).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, gingival fibromatosis, rests solely on a network-based score. There are no trials or publications, and no plausible link to crizotinib's ALK/ROS1/MET mechanism. The evidence level is L5. Most other predictions either duplicate the approved NSCLC indication or rely on non-transferable evidence. Lung germ cell tumour (L3) is the only one worth a research question, and only for tumours carrying actionable ALK, ROS1 or MET alterations.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale linking crizotinib to gingival fibromatosis
- Preclinical or case-level evidence in the predicted indication
- The TGA-approved Product Information, including approved indication text, warnings and contraindications
- For lung germ cell tumour, molecular profiling data showing actionable ALK, ROS1 or MET alterations, and a review of tumour-agnostic trial outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

