---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# Idelalisib: From B-Cell Malignancies to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib is a PI3Kδ-selective kinase inhibitor used internationally for relapsed chronic lymphocytic leukaemia (CLL), follicular lymphoma and small lymphocytic lymphoma (SLL), though it is **not currently registered or marketed in Australia**. The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**, with **9 clinical trials** and **20 publications** currently identified in this evidence pack supporting the direction, including two clinical reports specifically in relapsed/refractory MCL.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic lymphocytic leukaemia (CLL), follicular lymphoma (FL), small lymphocytic lymphoma (SLL) — per literature evidence in this pack; drug is not TGA-registered |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (evidence pack labels this a "Research Question", decision stage S2) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from DrugBank for this drug record (flagged as a data gap in the evidence pack). However, the literature evidence collected here consistently and independently describes idelalisib as a first-in-class, orally administered **phosphatidylinositol 3-kinase delta (PI3Kδ) inhibitor**. PI3Kδ is expressed almost exclusively in haematopoietic cells and is a key node in B-cell receptor (BCR) signalling, which drives survival and proliferation across multiple B-cell malignancies.

Idelalisib's established/approved use has been in CLL, follicular lymphoma and SLL — all B-cell neoplasms that, like mantle cell lymphoma, depend on constitutive BCR/PI3Kδ pathway activation. Mantle cell lymphoma is itself a B-cell non-Hodgkin lymphoma subtype in which the PI3K/AKT pathway is recognised as a contributor to pathogenesis, providing a plausible mechanistic bridge from the approved indications to MCL.

That said, one preclinical paper in this pack (PMID 33850273) specifically notes that idelalisib shows **intrinsic resistance in MCL treatment** unless combined with a p300/CBP inhibitor, and a second (PMID 40466505) describes CBX5-loss-driven resistance mechanisms. This tempers the mechanistic rationale — MCL response to idelalisib monotherapy appears less reliable than in CLL/FL/SLL, which is consistent with the modest (Phase 1) clinical evidence available below rather than confirmatory Phase 3 data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Safety of idelalisib combined with anti-CD20 mAb, chemotherapy, mTOR/immunomodulatory agents in relapsed/refractory iNHL, MCL or CLL |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1/2 | Completed | 106 | Idelalisib + lenalidomide vs lenalidomide alone in relapsed/refractory MCL |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1b | Completed | 20 | BCL201 + idelalisib dose-escalation in FL and MCL; safety/tolerability endpoint |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib (GS-9973) + idelalisib in relapsed/refractory heme malignancies including MCL, DLBCL, CLL, iNHL |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell malignancies; safety/cytopenia/GVHD focus |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib + other targeted agents (incl. idelalisib) in B-cell malignancies |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-world plasma concentration vs side-effect correlation for ibrutinib and idelalisib (idelalisib EMA-approved for MCL noted) |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality-of-life study of oral therapies (incl. idelalisib) used in CLL, FL, Waldenström's and MCL |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib (LOXO-305) study in CLL/SLL/NHL; idelalisib not the study intervention — low direct relevance |

No ANZCTR (Australian) trial registrations were found for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Clinical Trial Report | Cancer Discovery | PI3Kδ inhibitor idelalisib was effective in heavily pretreated patients with mantle cell lymphoma |
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 Trial Report | Blood | 48-week Phase 1 study (n=40) of idelalisib in relapsed/refractory MCL; primary outcome safety/DLT, secondary ORR/PFS/DOR |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical/Mechanistic | Clin Cancer Res | Idelalisib impacts MCL cell growth via inhibition of translation-regulatory mechanisms |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | P300/CBP inhibitor A-485 overcomes intrinsic idelalisib resistance in MCL in vitro/in vivo |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL; propolis restores sensitivity via ferroptosis |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances anti-tumour effect of palbociclib via PLK1 in relapsed/refractory DLBCL and MCL |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Practical approach to incidence and management of toxicity with ibrutinib and idelalisib in indolent B-cell malignancies including MCL |
| [26841011](https://pubmed.ncbi.nlm.nih.gov/26841011/) | 2016 | Review | Cancer Journal | Idelalisib targeting the PI3K pathway in non-Hodgkin lymphoma |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Current regimens and novel agents for mantle cell lymphoma (context review) |

---

## Australia Market Information

Idelalisib currently has **no ARTG entries** and is **not marketed in Australia** (0 licences on record). No TGA-approved product information is available for this drug.

---

## Cytotoxicity

Idelalisib is an antineoplastic agent (approved oncology indications; PI3Kδ-targeted small-molecule kinase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ-selective small-molecule kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

No key warnings, contraindications, or drug interaction data were returned for idelalisib in this evidence pack, and the drug is not TGA-registered. Please refer to the TGA-approved Product Information (PI) for safety information once/if this drug becomes available in Australia; in the interim, refer to the US FDA or EMA product labelling.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for idelalisib in MCL is limited to Phase 1/2 studies (best single trial: Phase 1, n=40, direct MCL population) plus two preclinical resistance-mechanism papers, without a confirmatory Phase 3 RCT — consistent with the evidence pack's own L3/"Research Question" scoring. The drug is also not currently registered or marketed in Australia, and core safety/MOA data are unavailable, so no regulatory pathway assessment can be made at this time.

**To proceed, the following is needed:**
- TGA product information / regulatory pathway assessment, given the drug currently has no Australian market presence
- Confirmed mechanism-of-action data from DrugBank (currently a data gap)
- Formal safety/DDI profile (key warnings, contraindications, interactions — currently not found)
- A confirmatory Phase 2/3 trial specifically in MCL, given noted intrinsic-resistance mechanisms reported in preclinical literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

