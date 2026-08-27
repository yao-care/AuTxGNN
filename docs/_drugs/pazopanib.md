---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
---

# Pazopanib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pazopanib: Toward Renal Cell Carcinoma Subtypes and Soft-Tissue Sarcomas

## One-Sentence Summary

This evidence pack does not record an approved original indication or mechanism of action for Pazopanib (DrugBank ID DB06589) — both are flagged as data gaps. TxGNN assigns very high, closely clustered scores (99.3–99.6%) to **10 oncology indications**, spanning renal cell carcinoma (RCC) subtypes and soft-tissue sarcomas (liposarcoma, dermatofibrosarcoma protuberans (DFSP), solitary fibrous tumour/fibroblastic neoplasm). Supporting evidence is uneven: the three top-ranked RCC subtypes have no matched trials or literature, while liposarcoma (9 trials, 20 publications) and DFSP (4 trials, 14 publications) are well supported, including completed Phase 2 trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack |
| Predicted New Indication | Oncology cluster — top-ranked: renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions (tied with RCC-associated-with-neuroblastoma and unclassified RCC) |
| TxGNN Prediction Score | 99.63% (top score, shared by 3 RCC subtypes; full 10-indication cluster ranges 99.29–99.63%) |
| Evidence Level | Heterogeneous — L2 (unclassified RCC, liposarcoma) down to L5 (Xp11.2/neuroblastoma-associated RCC, ovarian myxoid liposarcoma, kidney fibrosarcoma); see portfolio table below |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

### Predicted Indication Portfolio

| Rank | Predicted Indication | TxGNN Score | Trials | Literature | Evidence Level |
|------|----------------------|-------------|--------|------------|-----------------|
| 1 | RCC associated with Xp11.2 translocations/TFE3 fusions | 99.63% | 0 | 0 | L5 |
| 2 | RCC associated with neuroblastoma | 99.63% | 0 | 0 | L5 |
| 3 | Unclassified renal cell carcinoma | 99.63% | 1 | 6 | L2 |
| 4 | Liposarcoma | 99.59% | 9 | 20 | L2 |
| 5 | Childhood kidney cell carcinoma | 99.54% | 1 | 0 | L4 |
| 6 | Ovarian myxoid liposarcoma | 99.51% | 0 | 0 | L5 |
| 7 | Heart fibrosarcoma | 99.37% | 3 | 0 | L4 |
| 8 | Fibroblastic neoplasm (SFT/desmoid) | 99.35% | 3 | 20 | L3 |
| 9 | Kidney fibrosarcoma | 99.33% | 0 | 0 | L5 |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | 4 | 14 | L3 |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Pazopanib is not available in this evidence pack (Data Gap DG002), and no original indication is on file. However, the trial and literature evidence retrieved here provides indirect mechanistic context: across the RCC and soft-tissue sarcoma trials, Pazopanib is repeatedly evaluated head-to-head with or as an alternative to sorafenib, sunitinib, regorafenib and sapanisertib — agents from the anti-angiogenic multi-target tyrosine kinase inhibitor (TKI) class used in vascularised solid tumours. This places the predicted indications within a biologically coherent family: RCC and soft-tissue sarcomas (liposarcoma, DFSP, solitary fibrous tumour) are all treated in current oncology practice with this same drug class.

A more specific mechanistic link is available for DFSP: literature in this pack (PMID 37592448) reports that Pazopanib inhibits the COL1A1-PDGFB fusion protein that drives DFSP, giving that particular indication a target-based rationale rather than a purely score-driven one.

The three top-ranked RCC subtypes (Xp11.2-translocation, neuroblastoma-associated, and unclassified) share an identical TxGNN score, suggesting the model is generalising a broad "RCC" signal rather than distinguishing between these rare molecular subtypes — only "unclassified RCC" among the three currently has corroborating trial/literature evidence.

## Clinical Trial Evidence

| Trial Number | Indication | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Unclassified RCC | Phase 3 | Completed | 544 | Sorafenib→pazopanib vs. pazopanib→sorafenib sequencing in advanced/metastatic RCC |
| [NCT01575548](https://clinicaltrials.gov/study/NCT01575548) | Childhood kidney cell carcinoma | Phase 3 | Active, not recruiting | 129 | Adjuvant pazopanib vs. placebo after metastasectomy in metastatic RCC |
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Liposarcoma | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable/metastatic liposarcoma |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Liposarcoma | Phase 2 | Completed | 52 | Activity/tolerability of pazopanib in relapsed advanced/metastatic liposarcoma |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Liposarcoma / soft tissue sarcoma | Phase 2 | Completed | 54 | Randomised: gemcitabine ± pazopanib in refractory soft tissue sarcoma (PAPAGEMO trial) |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Liposarcoma / bone sarcoma | Phase 2 | Completed | 178 | Pazopanib + oral topotecan in metastatic, non-resectable soft tissue/bone sarcoma |
| [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) | Fibroblastic neoplasm (SFT/EMC) | Phase 2 | Completed | 96 | Single-agent pazopanib in unresectable/metastatic solitary fibrous tumour and extraskeletal myxoid chondrosarcoma |
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Dermatofibrosarcoma protuberans | Phase 2 | Terminated | 23 | Pazopanib in unresectable, locally advanced/transformed DFSP |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | Heart fibrosarcoma / sarcoma | Phase 1/2 | Terminated | 151 | Sapanisertib (MLN0128/TAK-228) vs. pazopanib in advanced/metastatic sarcoma |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fibroblastic neoplasm / heart fibrosarcoma | Phase 1/2 | Recruiting | 139 | Maintenance pazopanib with dose-escalated radiotherapy ± selinexor in non-rhabdomyosarcoma soft tissue sarcoma |

## Literature Evidence

| PMID | Year | Type | Journal | Indication | Key Findings |
|------|-----|------|------|------|---------|
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | RCT | JAMA Oncology | Liposarcoma / STS | Final results of PAPAGEMO: pazopanib ± gemcitabine in anthracycline/ifosfamide-refractory soft tissue sarcoma |
| [30578023](https://pubmed.ncbi.nlm.nih.gov/30578023/) | 2019 | Phase 2 trial | Lancet Oncology | Fibroblastic neoplasm (SFT) | Multicentre single-arm trial of pazopanib in malignant/dedifferentiated solitary fibrous tumour |
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Phase 2 trial | J Invest Dermatol | Dermatofibrosarcoma protuberans | Multicentre phase II study of pazopanib in unresectable DFSP |
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Phase 2 trial | Cancer | Liposarcoma | Prospective phase 2 study of pazopanib in intermediate/high-grade liposarcoma |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Mechanistic/preclinical | Cancer Science | Dermatofibrosarcoma protuberans | Pazopanib identified as inhibitor of the COL1A1-PDGFB fusion driving DFSP |
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 trial | Cancer Res Treat | Unclassified / non-clear-cell RCC | Single-arm phase II study of pazopanib efficacy/safety in non-clear-cell RCC |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world/retrospective | Ecancermedicalscience | Unclassified RCC | Sunitinib vs. pazopanib interchangeability in non-clear-cell/sarcomatoid RCC |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | Liposarcoma | Established and experimental systemic treatment options for advanced liposarcoma |
| [29614488](https://pubmed.ncbi.nlm.nih.gov/29614488/) | 2018 | Retrospective | Oncology | Fibroblastic neoplasm (SFT) | Efficacy/safety of pazopanib in recurrent or metastatic solitary fibrous tumour |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Real-world/retrospective | Eur Urol Oncol | Unclassified RCC | IMDC database comparison of contemporary vs. traditional first-line therapies in non-clear-cell RCC |

## Australia Market Information

Pazopanib has no ARTG entries and is not currently marketed in Australia based on the data available in this evidence pack.

## Cytotoxicity

All 10 TxGNN-predicted indications for Pazopanib in this pack are malignancies (renal cell carcinoma subtypes and soft-tissue sarcomas), and the retrieved trials position it alongside other anti-angiogenic tyrosine kinase inhibitors — indicating it is an antineoplastic agent even though DrugBank category and toxicity data are not available in this pack (Data Gap DG002).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Likely targeted therapy (multi-target tyrosine kinase inhibitor class, inferred from trial comparators sorafenib/sunitinib/regorafenib); DrugBank category not confirmed in this pack |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. A drug-drug interaction database query for Pazopanib returned no results (`not_found`).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN and the retrieved literature support a biologically plausible, multi-indication oncology signal — particularly for liposarcoma and dermatofibrosarcoma protuberans, each backed by completed Phase 2 trials. However, the TGA Product Information (warnings/contraindications) is a **Blocking** data gap (DG001) that prevents any safety pre-screen, and Pazopanib is not currently marketed in Australia (0 ARTG entries). The evaluation cannot proceed to a Go/Guardrails decision until safety data is obtained.

**To proceed, the following is needed:**
- TGA Product Information (PI): warnings, contraindications, drug interactions (Blocking, DG001)
- DrugBank-confirmed mechanism of action (DG002)
- Confirmation of Pazopanib's approved original indication(s) and Australian regulatory pathway, since no ARTG entry currently exists
- A decision on which specific predicted indication to prioritise: the top-ranked Xp11.2-translocation and neuroblastoma-associated RCC subtypes currently have no supporting trials or literature (L5), whereas liposarcoma and DFSP are the most actionable near-term candidates given existing Phase 2 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

