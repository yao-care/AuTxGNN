---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Nilotinib
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

# Nilotinib: From Chronic Myeloid Leukaemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib (DrugBank DB04868) is a second-generation BCR-ABL tyrosine kinase inhibitor originally developed for chronic myeloid leukaemia (CML). The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but this direction is currently supported by **0 clinical trials** and only **1 mechanistic review article** — the evidence base is thin and largely theoretical at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia (CML) — based on well-established public information; the evidence pack itself has no structured original-indication data (data gap) |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed (未上市) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nilotinib is not available in this evidence pack (data gap, DG002). Based on known public information, nilotinib is a second-generation BCR-ABL tyrosine kinase inhibitor used for chronic myeloid leukaemia, and it also inhibits PDGFR (both PDGFRA and PDGFRB) and KIT kinases as off-target activity within the same structural class as imatinib.

Dermatofibrosarcoma protuberans is typically driven by a COL1A1-PDGFB fusion gene, which causes constitutive activation of PDGFRB signalling. Imatinib — a drug with a very similar kinase-inhibition profile to nilotinib — is already approved for this indication. This provides a plausible mechanistic rationale for nilotinib: since it shares PDGFR-inhibitory activity with imatinib, it is reasonable to hypothesise similar activity in PDGFR-driven tumours such as DFSP.

However, this rationale is currently extrapolated from imatinib's class effect and general PDGFR pharmacology rather than from any nilotinib-specific study in DFSP. No dedicated nilotinib clinical trial or case series in DFSP was identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors (as a class) in neoplastic disease; provides mechanistic background for PDGFR blockade in PDGFR-driven tumours but does not report nilotinib-specific efficacy data in DFSP |

---

## Safety Considerations

No local safety data is available for nilotinib in this evidence pack. Key warnings, contraindications, and drug interaction data are all flagged as a **blocking data gap (DG001)** — TFDA label warnings/contraindications could not be retrieved, which means a formal safety pre-assessment (S1) cannot currently be completed. Please refer to the officially approved Product Information (PI) from a jurisdiction where nilotinib is marketed (e.g. FDA, EMA) for interim safety guidance until local label data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (DFSP) has no clinical trial evidence and only one non-disease-specific mechanistic review (evidence level L4). Combined with the drug's current unmarketed status locally (0 ARTG/license entries) and a blocking safety data gap, there is not yet enough evidence to proceed past the research-question stage.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TFDA/PI warnings and contraindications before any safety pre-assessment
- Resolve DG002: confirm nilotinib's MOA via DrugBank API to firm up the mechanistic rationale
- Nilotinib-specific preclinical or case-report data in DFSP, since current support is inferred from the imatinib class effect
- Consider that **liposarcoma (rank 2)** is a more evidence-mature candidate — it has an actual Phase I/II trial (GEIS-27, [NCT02587169](https://clinicaltrials.gov/study/NCT02587169)) and a related Phase I publication (evidence level L3, decision stage S2) — and may warrant parallel or prioritised review over DFSP

---

## Other TxGNN-Predicted Indications (Overview)

For context, this evidence pack contains 10 candidate indications for nilotinib. Only the top-ranked one is detailed above per report scope; the remainder are summarised here for awareness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Dermatofibrosarcoma protuberans | 99.31% | L4 | S1 | Research Question |
| 2 | Liposarcoma | 98.85% | L3 | S2 | Research Question |
| 3 | Ovarian myxoid liposarcoma | 98.74% | L5 | S0 | Hold |
| 4 | Ewing sarcoma | 98.45% | L5 | S0 | Hold |
| 5 | Ganglioneuroblastoma (disease) | 97.02% | L5 | S0 | Hold |
| 6 | Heart fibrosarcoma | 97.01% | L5 | S0 | Hold |
| 7 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 96.94% | L5 | S0 | Hold (likely a KG entity-mapping artefact — recommend verifying entity validity before any further review) |
| 8 | Kidney fibrosarcoma | 96.90% | L5 | S0 | Hold |
| 9 | Fibroblastic neoplasm | 96.90% | L4 | S1 | Research Question |
| 10 | Conventional fibrosarcoma | 96.79% | L5 | S0 | Hold |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

