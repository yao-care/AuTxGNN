---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Antineoplastic Chemotherapy to Liver Sarcoma

## One-Sentence Summary

Fluorouracil (5-FU, DB00544) is a fluoropyrimidine antimetabolite used as a chemotherapy backbone (e.g. FOLFOX, FOLFIRINOX) in gastrointestinal malignancies. TxGNN generated 10 candidate indications for this drug, but **9 of the 10 have zero supporting clinical trials or literature** and several are flagged in the model rationale itself as likely embedding-similarity artefacts (confusion with hydroxyurea). This report therefore focuses on the one candidate that reached an actual evidence-backed decision stage — **Liver Sarcoma** — supported by **5 clinical trials** (indirect) and **20 publications**, including a directly relevant cohort study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the regulatory record supplied (fluorouracil is not currently ARTG-registered under this candidate). Known clinically as a fluoropyrimidine chemotherapy agent for GI malignancies. |
| Predicted New Indication | Liver Sarcoma |
| TxGNN Prediction Score | 99.68% (rank 4316 of model output) |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** |

**Note on candidate selection:** TxGNN's numerically top-ranked predictions for fluorouracil (botryoid-type embryonal rhabdomyosarcoma of the vagina, rhabdomyosarcoma variants, sickle-cell/haemoglobinopathy syndromes) all returned **zero clinical trials and zero-to-minimal literature**, and the model rationale explicitly flags the haemoglobinopathy predictions (ranks 8–10) as probable false positives from embedding proximity to hydroxyurea. Liver Sarcoma (TxGNN rank 4316) is the only candidate that reached Decision Stage S1 with real evidentiary support, so it is used as the reportable indication here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on the evidence assembled, fluorouracil is a pyrimidine antimetabolite that inhibits thymidylate synthase (TS), and is an established chemotherapy backbone for gastrointestinal and hepatobiliary malignancies (e.g. FOLFOX, FOLFIRINOX regimens for metastatic colorectal cancer).

Liver sarcoma is mechanistically a "neighbouring indication" extrapolation rather than a direct match: the existing evidence base is drawn largely from colorectal cancer with liver metastasis or general solid-tumour trials, not from primary hepatic sarcoma populations specifically. One directly relevant cohort study (Zhou et al., 2019) examined surgical treatment and chemotherapy of adult primary liver sarcoma in China, providing the strongest single piece of evidence for this candidate.

Overall, the mechanistic plausibility is moderate-to-low: 5-FU's antimetabolite activity is broadly cytotoxic to rapidly dividing tumour cells, which provides a generic rationale for activity in sarcoma, but there is no sarcoma-specific mechanistic data confirming meaningful efficacy over other cytotoxic options.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | Completed | 553 | Cetuximab + FOLFOX-4 vs FOLFOX-4 alone in RAS wild-type metastatic colorectal cancer. Relevance grade C — not liver sarcoma, but shows 5-FU-containing regimen safety data. |
| [NCT03914170](https://clinicaltrials.gov/study/NCT03914170) | N/A (retrospective) | Completed | 70 | FOLFIRINOX (incl. 5-FU) + cetuximab in RAS wild-type mCRC; population included liver-metastatic patients. Relevance grade B — indirect. |
| [NCT01374425](https://clinicaltrials.gov/study/NCT01374425) | Phase 2 | Completed | 376 | Bevacizumab + mFOLFOX6 vs bevacizumab + FOLFIRI in untreated mCRC. Relevance grade C. |
| [NCT04999761](https://clinicaltrials.gov/study/NCT04999761) | Phase 1 | Recruiting | 917 | Platform study of AB122-based treatments in advanced solid tumours. Relevance grade C — not sarcoma-specific. |
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | Phase 4 | Recruiting | 40 | Atezolizumab + bevacizumab + Y-90 radioembolization for hepatocellular carcinoma bridging/downstaging to transplant. Relevance grade C — no 5-FU arm identified. |

**None of the above trials directly enrol a primary liver sarcoma population; all evidence is indirectly extrapolated from colorectal cancer or general solid-tumour settings.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29346784](https://pubmed.ncbi.nlm.nih.gov/29346784/) | 2019 | Cohort (Tier 2) | Digestive Surgery | Surgical treatment and chemotherapy outcomes in adult primary liver sarcoma, single-centre China experience — the most directly relevant evidence for this indication. |
| [9873095](https://pubmed.ncbi.nlm.nih.gov/9873095/) | 1999 | Review | Liver Transplantation and Surgery | Review of management of hepatic metastases, including gastrointestinal sarcoma as one of several origins. |
| [11294295](https://pubmed.ncbi.nlm.nih.gov/11294295/) | 2001 | Case Report | J Hepatobiliary Pancreat Surg | Two paediatric cases of ruptured undifferentiated (embryonal) liver sarcoma; chemotherapy regimen used did not include 5-FU. |
| [37112602](https://pubmed.ncbi.nlm.nih.gov/37112602/) | 2023 | Preclinical | Toxics | 5-FU combined with chamomile flower extract in a Sarcoma 180 mouse model — antitumour and toxicological profiling. |
| [1406088](https://pubmed.ncbi.nlm.nih.gov/1406088/) | 1992 | Preclinical (pharmacology) | Magnetic Resonance Imaging | 19F-MRS study of 5-FU metabolism in liver and RIF-1 tumour-bearing mice. |
| [4032755](https://pubmed.ncbi.nlm.nih.gov/4032755/) | 1985 | Early-phase pharmacology | Gan no Rinsho | Phase I dose-finding of a 5-FU derivative (590-S/tegafur-related), general anticancer activity. |
| [3630210](https://pubmed.ncbi.nlm.nih.gov/3630210/) | 1987 | Preclinical (metabolism) | Xenobiotica | Hepatic metabolism of a 5-FU prodrug and enzyme induction studies in rats. |
| [28239866](https://pubmed.ncbi.nlm.nih.gov/28239866/) | 2017 | Preclinical (pharmacokinetics) | Biopharm Drug Dispos | Effect of vasomodulators on hepatic disposition of 5-FU applied to the liver surface in rats. |
| [52569](https://pubmed.ncbi.nlm.nih.gov/52569/) | 1975 | Preclinical | Gan | Antitumour agent comparison (including 5-FU) in Sarcoma-180 cells transplanted to liver, kidney, lung. |
| [37018833](https://pubmed.ncbi.nlm.nih.gov/37018833/) | 2023 | Preclinical | An Acad Bras Cienc | Histological evaluation of 5-FU-treated liver in Sarcoma-180-bearing mice. |

10 additional lower-relevance publications (mostly preclinical pharmacology/metabolism studies, plus colorectal-cancer-focused reviews) are available in the underlying evidence pack but are omitted here for brevity.

---

## Australia Market Information

Fluorouracil is **not currently registered on the ARTG (Australian Register of Therapeutic Goods)** under this drug candidate — 0 licences were found in the evidence pack.

---

## Cytotoxicity

*(Fluorouracil is a fluoropyrimidine antimetabolite chemotherapy agent, meeting the antineoplastic classification criteria.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite; inhibits thymidylate synthase) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. TFDA/TGA label warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — DG001 — preventing the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking** data gap (DG001) means TFDA/TGA-level safety warnings and contraindications could not be assessed, which by itself precludes progression past initial safety screening.
- Evidence for Liver Sarcoma is indirect (extrapolated from colorectal/hepatobiliary trials, not a primary liver-sarcoma population), reaching only L3/Research-Question status, and fluorouracil is not currently marketed in Australia under this candidate.
- The remaining 9 of 10 TxGNN-predicted indications for this drug have no clinical trial or literature support and should not be progressed at all.

**To proceed, the following is needed:**
- Retrieve TGA/TFDA Product Information (label warnings, contraindications, DDI) to close DG001
- Obtain formal DrugBank/pharmacology MOA data to close DG002
- Seek liver-sarcoma-specific clinical evidence (case series or trial), rather than relying on colorectal-cancer extrapolation
- Clarify Australian registration pathway/status for fluorouracil under this specific candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

