---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Unspecified Original Indication to Predicted Liposarcoma

## One-Sentence Summary

Sorafenib's original approved indication and mechanism-of-action detail are not documented in this evidence pack (flagged as data gaps DG001/DG002). The TxGNN model predicts potential efficacy in **Liposarcoma**, a rare soft-tissue sarcoma, supported by **2 clinical trials** and **8 publications** — though one of the two trials actually tested a related but distinct drug (regorafenib), so sorafenib-specific clinical evidence for this indication remains limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no ARTG record; drug is not marketed in Australia) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sorafenib is not available in this evidence pack (data gap DG002, High severity). Based on information embedded in the evidence pack's own rationale annotations, sorafenib is consistently characterised as a multi-target tyrosine kinase inhibitor acting on VEGFR-1/2/3, PDGFR-β, and RAF — a profile that underlies its established role as a standard therapy in VEGFR-driven cancers such as renal cell carcinoma (see the "unclassified renal cell carcinoma" candidate in this same pack, which cites sorafenib as an already-approved RCC multi-kinase inhibitor).

Sorafenib's specific original indication could not be extracted from this pack, so the direct relationship between its original and new (liposarcoma) indications cannot be fully characterised here.

Mechanistically, the pack's own rationale for liposarcoma notes that soft-tissue sarcomas frequently show RAF/MEK/ERK pathway activation and are angiogenesis-dependent, which provides a plausible basis for sorafenib's antiangiogenic (VEGFR) and RAF-inhibitory activity to be relevant. However, the same rationale explicitly flags that evidence specific to the liposarcoma subtype (rather than soft-tissue sarcoma broadly) is limited.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib in advanced soft tissue sarcomas (broad population; not liposarcoma-specific). Relevance grade B — only a subset of participants likely had liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol for selected sarcoma subtypes. **Caveat**: the drug actually studied was regorafenib, not sorafenib — mechanistically related (both multi-kinase inhibitors) but not direct sorafenib evidence. Relevance grade C. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib evaluated in advanced soft tissue sarcomas; most directly relevant clinical evidence in this list. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Annals of Surgical Oncology | Neoadjuvant sorafenib plus conformal radiotherapy for extremity soft tissue sarcoma. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven therapy for soft tissue sarcomas, including liposarcoma-active agents. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas by histological subtype. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse models for sarcoma combination therapies (CDK inhibitor palbociclib focus). |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth/MAPK signalling in malignant peripheral nerve sheath and dedifferentiated liposarcoma cell lines. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (xenograft) | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models; identifies PTEN down-regulation and PI3K pathway relevance (not sorafenib-specific). |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | **Caveat**: this case report describes response to trabectedin (not sorafenib) in synovial sarcoma — included in the pack's literature set but does not directly support sorafenib. |

## Cytotoxicity

Sorafenib is classified as antineoplastic based on the evidence pack's own descriptions (multi-kinase inhibitor used across the listed cancer indications: liposarcoma, renal cell carcinoma, breast carcinoma, dermatofibrosarcoma protuberans, etc.).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR-1/2/3, PDGFR-β, RAF) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence level is L2 — only one Phase 2 trial (NCT00217620) directly tests sorafenib in a broad soft-tissue sarcoma population that only partially overlaps with liposarcoma, and the second trial (NCT02048371) actually studied a different drug (regorafenib). Combined with the absence of original indication, MOA, and TFDA safety data (data gaps DG001–blocking, DG002–high), the pack does not yet support progression beyond a research question.

**To proceed, the following is needed:**
- TFDA/PI label warnings and contraindications (DG001, blocking for safety pre-screen)
- Confirmed mechanism of action from DrugBank (DG002)
- Sorafenib's documented original indication(s), which are currently missing from this pack
- A liposarcoma-subtype-specific clinical trial (current evidence is diluted across broader soft-tissue sarcoma populations)
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

