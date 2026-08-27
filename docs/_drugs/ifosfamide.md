---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Soft Tissue Sarcoma to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an oxazaphosphorine alkylating agent long established as a chemotherapy backbone for soft tissue sarcoma, testicular cancer, and rhabdomyosarcoma. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, a direction currently supported by **8 clinical trials** (including one completed Phase 3 RCT of a different ifosfamide-based schedule) and **20 publications**, though most of this evidence dates from the 1990s–2000s and reflects salvage/combination therapy in anthracycline-resistant or metastatic disease rather than first-line use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma / testicular carcinoma (established chemotherapy backbone per literature in this evidence pack; no formal TFDA/DrugBank indication record currently available) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record is not yet available for this drug profile (data gap, remediation pending via DrugBank API query). Based on the repurposing analysis in this evidence pack, ifosfamide is an oxazaphosphorine alkylating agent that is activated hepatically via CYP3A4/CYP2B6 to 4-hydroxy-ifosfamide, which causes DNA cross-linking and subsequent apoptosis — a cell-cycle-nonspecific cytotoxic mechanism.

Breast cancer tissue, like sarcoma and germ cell tumours, is highly proliferative and therefore inherently sensitive to alkylating-agent DNA damage. This mechanistic plausibility is reinforced by a substantial body of older literature (1988–2002) documenting ifosfamide combination regimens (with vinorelbine, etoposide, epirubicin, paclitaxel, or carboplatin) in anthracycline-resistant and CMF-resistant metastatic breast cancer, generally as second-line/salvage therapy rather than a first-line standard.

It is worth noting the mechanistic link here is not novel biology so much as an established but under-used salvage-therapy role — the evidence largely predates modern taxane/anthracycline-based standards of care, so its clinical relevance today needs re-assessment against current treatment algorithms.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | RCT of Paclitaxel+Carboplatin vs Ifosfamide+Paclitaxel in chemotherapy-naïve carcinosarcoma of the uterus, fallopian tube, peritoneum or ovary (not breast cancer specifically); recruited but no public results found |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose Cisplatin/Cyclophosphamide/Etoposide/Ifosfamide + Carboplatin/Taxol with autologous stem cell support in advanced cancer, including breast |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (Topotecan/Ifosfamide/Mesna/Etoposide) followed by autologous stem cell rescue in metastatic breast cancer |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + Ifosfamide as first-line chemotherapy in metastatic breast cancer |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Randomised trial comparing multi-cycle high-dose vs optimised conventional-dose chemotherapy in metastatic breast cancer |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 with double autologous bone marrow transplant for stage IV breast cancer; ifosfamide used as background high-dose chemotherapy |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Activated T-cell therapy after peripheral stem cell transplant in stage IV breast cancer; ifosfamide used in conditioning, not the primary intervention |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid high-throughput drug screening assay in refractory solid tumours (in vitro platform, not a clinical efficacy trial) |

No ANZCTR-registered trials were identified for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8711499](https://pubmed.ncbi.nlm.nih.gov/8711499/) | 1996 | Randomised Phase 2 | Seminars in Oncology | n=357; epirubicin/ifosfamide maintenance vs treatment interruption in advanced metastatic breast cancer; 8% CR, 37% PR |
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | Cancer | Paclitaxel (24h infusion) + ifosfamide in anthracycline-resistant metastatic breast cancer |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Cohort/Phase 2 | Cancer Chemother Pharmacol | Ifosfamide substituted for cyclophosphamide in CMF regimen; effective in CMF-resistant/relapsed breast cancer (n=25) |
| [11138456](https://pubmed.ncbi.nlm.nih.gov/11138456/) | 2000 | Cohort | Cancer Chemother Pharmacol | Ifosfamide metabolism and DNA damage in tumour and peripheral blood lymphocytes of breast cancer patients |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 | J Clin Oncol | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer |
| [10602907](https://pubmed.ncbi.nlm.nih.gov/10602907/) | 1999 | Cohort | Cancer Chemother Pharmacol | Ifosfamide, carboplatin and etoposide (ICE) in 25 patients with metastatic/refractory breast cancer after prior chemotherapy failure |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Cohort | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Cohort | Cancer Chemother Pharmacol | Ifosfamide/etoposide with mesna uroprotection in 44 patients with advanced, anthracycline-pretreated breast cancer |
| [7695982](https://pubmed.ncbi.nlm.nih.gov/7695982/) | 1995 | Cohort | Eur J Cancer | Pharmacokinetics, metabolism and clinical effect of ifosfamide (with doxorubicin/epirubicin) in 15 metastatic/locally advanced breast cancer patients |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Review | Drugs | Review of ifosfamide/mesna antineoplastic activity, pharmacokinetics and therapeutic efficacy across tumour types |

## Australia Market Information

Ifosfamide currently has **0 ARTG entries** and is **not marketed** in Australia according to the data available in this evidence pack. No product/dosage form/indication details can be reported at this time.

## Cytotoxicity

Ifosfamide is a conventional cytotoxic chemotherapy agent (oxazaphosphorine alkylator, cyclophosphamide analogue), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — oxazaphosphorine alkylating agent (prodrug activated by hepatic CYP3A4/CYP2B6 to 4-hydroxy-ifosfamide) |
| Myelosuppression Risk | High — this evidence pack also documents ifosfamide-based regimens (often with etoposide) associated with secondary myelodysplastic syndrome/AML in long-term survivors, underscoring significant marrow-toxic/leukemogenic potential in addition to acute cytopenias |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions — not characterised in the available evidence pack |
| Monitoring Items | FBC with differential, renal function, and urinalysis (uroprotection with mesna is repeatedly referenced in the literature to manage haemorrhagic cystitis/urotoxicity) |
| Handling Protection | Standard cytotoxic drug handling precautions apply, consistent with other alkylating-agent chemotherapy |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug interaction data are not currently available for ifosfamide in this evidence pack (blocking data gap — TFDA/product labelling not yet retrieved).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The breast carcinoma signal is supported by one completed Phase 3 RCT (of a related but not directly matching ifosfamide-based regimen), several Phase 1/2 trials, and 20 publications spanning three decades — sufficient to justify further evaluation (L2), but the trials are largely older, several are terminated or status-unknown, and the drug is currently unregistered in Australia (0 ARTG entries) with no TGA safety documentation retrieved.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Clarification of ARTG registration pathway given zero current listings
- Updated outcome data for trials currently listed as "Unknown" status (e.g. NCT00954174, NCT00026078, NCT00012311)
- A clinician review of whether this evidence, mostly predating modern anthracycline/taxane-based standards, remains clinically relevant today

**Note on this evidence pack:** several other TxGNN-predicted indications for ifosfamide in this pack (e.g. myelodysplastic syndrome, monocytic leukaemia, aregenerative anaemia) are flagged by the underlying analysis as likely reflecting ifosfamide's known **myelosuppressive/leukemogenic toxicity** rather than a genuine treatment signal, and one (rhabdomyosarcoma, L1 evidence) is an already-established indication rather than a new discovery. These are excluded from this report's primary recommendation but should be considered before broader use of this evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

