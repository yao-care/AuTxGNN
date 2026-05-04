---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib (ALUNBRIG™) is a next-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor, approved in the United States, Japan, and Europe for ALK-positive advanced non-small cell lung cancer (NSCLC), though it is not currently registered in Australia.
The TxGNN model predicts it may have potential activity in **Fibromatosis, Gingival** (hereditary gingival fibromatosis), with a prediction score of **99.89%**.
However, there are **no clinical trials and no supporting publications** specific to this indication, and the mechanistic rationale linking ALK inhibition to gingival fibromatosis is currently unsupported — this prediction is likely a knowledge graph inference artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive advanced non-small cell lung cancer (NSCLC) — globally approved but **not registered in Australia** |
| Predicted New Indication | Fibromatosis, Gingival (Hereditary Gingival Fibromatosis) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on published literature indexed within this report, brigatinib is a next-generation ALK (anaplastic lymphoma kinase) tyrosine kinase inhibitor designed to overcome crizotinib resistance. It inhibits wild-type ALK as well as a broad range of ALK resistance mutations, and also shows activity against EGFR and other kinase targets. It is approved in the United States (2017, accelerated; 2020, full approval), Japan, and the European Union for ALK-rearranged advanced or metastatic NSCLC — both as a first-line agent and in patients who have progressed on prior ALK inhibitors.

Hereditary gingival fibromatosis (HGF) is a rare connective tissue overgrowth disorder driven by mutations in genes such as SOS1, REST, and HMGA2. These pathways are entirely unrelated to the ALK/EGFR signalling axis that brigatinib targets. There is no established biological rationale linking ALK tyrosine kinase inhibition to the proliferative fibroblastic pathology underlying gingival fibromatosis.

The TxGNN high prediction score (0.9989) for this indication most likely reflects a knowledge graph inference artefact — possibly mediated through shared "fibrosis-related" or "connective tissue" graph nodes — rather than a genuine mechanistic relationship. **This prediction is considered biologically implausible at this stage and does not support clinical development in this direction.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brigatinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Brigatinib in Fibromatosis, Gingival.

---

## Australia Market Information

Brigatinib is **not currently registered with the Therapeutic Goods Administration (TGA)**. There are no ARTG entries for this medicine as of the data cutoff date (10 April 2026). Sponsors seeking to make brigatinib available in Australia would need to lodge a new registration application with the TGA.

For reference, brigatinib (ALUNBRIG™) holds marketing authorisation in the following key jurisdictions for ALK-positive advanced NSCLC:

| Jurisdiction | Regulatory Body | Status | Indication Summary |
|---|---|---|---|
| United States | FDA | Approved (2017/2020) | ALK+ metastatic NSCLC, first-line and post-crizotinib |
| Japan | PMDA | Approved | ALK+ advanced NSCLC (global + J-ALTA data) |
| European Union | EMA | Approved | ALK+ advanced NSCLC |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — second-generation ALK/EGFR tyrosine kinase inhibitor (TKI); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate (anaemia and lymphopenia reported in trials; less myelosuppressive than conventional chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC with differential), liver function tests (LFTs), renal function, pulmonary function and chest imaging (ILD/pneumonitis monitoring), serum lipase, amylase, blood glucose, blood pressure, ECG (QTc) |
| Handling Protection | Standard oral antineoplastic handling precautions apply; follow institutional cytotoxic safe-handling guidelines for preparation, administration, and waste disposal |

> **⚠️ Brigatinib-specific safety signal:** Early-onset pulmonary adverse events (interstitial lung disease / pneumonitis) have been observed within the first 7 days of treatment initiation in clinical trials — a class-specific but brigatinib-prominent risk requiring close early monitoring.

---

## Safety Considerations

No TGA-approved Product Information (PI) is available as brigatinib is not registered in Australia. Please refer to the current **US FDA ALUNBRIG™ Prescribing Information** or the **EMA Summary of Product Characteristics** for comprehensive warnings, contraindications, and drug interaction data.

**Notable safety signal identified within this evidence pack:**
A fatal tumour lysis syndrome (TLS) case has been reported in a patient receiving sequential ALK inhibitor therapy including brigatinib (PMID: [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/)). While TLS is uncommon in solid tumours, this case warrants awareness in patients with high tumour burden transitioning between ALK inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction of fibromatosis, gingival carries no mechanistic plausibility and is supported by zero clinical trials and zero publications specific to this indication; the high prediction score (99.89%) is most likely an artefact of the knowledge graph topology rather than a genuine therapeutic signal, making any clinical development in this direction premature and unjustified at this stage.

**To proceed meaningfully with Brigatinib repurposing or registration in Australia, the following is recommended:**

- **Investigate higher-plausibility repurposing candidates from this evidence pack:**
  - **Rank 7 — Lung Germ Cell Tumour** (Evidence Level L4): Indirect preclinical data support a potential role for brigatinib in ALK-rearranged rare tumours (PMID: [39395329](https://pubmed.ncbi.nlm.nih.gov/39395329/), [27049722](https://pubmed.ncbi.nlm.nih.gov/27049722/)); warrants a dedicated research question
  - **NF2-Related Schwannomatosis** (identified in Rank 10 literature): A Phase 2 clinical study (PMID: [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/), *NEJM* 2024) demonstrated tumour shrinkage with brigatinib through multi-kinase inhibition independent of ALK — this represents a distinct, potentially viable repurposing signal requiring a separate evaluation
  - **Rank 4 / Rank 8 (Lung Hilum Carcinoma / Pulmonary Sulcus Neoplasm):** These are anatomical sub-classifications of NSCLC; if ALK-rearrangement is confirmed, these fall within the drug's existing globally approved indication
- **Obtain full MOA data from DrugBank API** (Data Gap DG002) to enable complete mechanistic plausibility analysis
- **Obtain regulatory product information** (Data Gap DG001) — retrieve the FDA ALUNBRIG™ PI as a functional substitute for TGA PI to complete safety and contraindication assessment
- **Assess TGA registration pathway** if there is commercial intent to make brigatinib available in Australia for its established indication (ALK+ NSCLC); given existing evidence from multiple Phase 3 trials (ALTA-1L, ALTA-3), a full registration application would be well-supported

---
*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

