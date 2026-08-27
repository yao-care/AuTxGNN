---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
---

# Lapatinib
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

# Lapatinib: A TxGNN-Predicted Signal for Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib's original approved indication is not recorded in this evidence pack (the drug currently has no ARTG entries in Australia). The TxGNN model's top-ranked prediction is **Dermatofibrosarcoma Protuberans (DFSP)**, but this signal is currently supported by **zero clinical trials** and **zero publications** — it reflects network-similarity scoring only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (drug is not currently registered in Australia) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field for lapatinib is flagged as a data gap in this evidence pack. However, the rationale text attached to other candidates in this same pack (ranks 2 and 8) consistently references lapatinib's established mechanism as a **dual EGFR/HER2 tyrosine kinase inhibitor**, used clinically in HER2-positive breast cancer — this is corroborated evidence within the pack itself, even though it is not captured in the formal MOA field.

Dermatofibrosarcoma protuberans is a soft-tissue sarcoma driven almost exclusively by a **COL1A1-PDGFB gene fusion**, and its standard targeted therapy is imatinib, a PDGFR inhibitor. This is a distinct signalling pathway from EGFR/HER2. The evidence pack's own repurposing rationale for this candidate explicitly states there is **no known mechanistic relationship** between lapatinib's kinase-inhibition profile and DFSP's PDGFR-driven biology.

Taken together, this candidate should be read as a TxGNN network-similarity artefact rather than a biologically grounded repurposing hypothesis at this stage. The score (99.30%) is high, but score magnitude alone does not substitute for mechanistic plausibility or empirical support — both of which are currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for lapatinib in this evidence pack (total licenses: 0). The drug is not currently marketed in Australia under this dataset.

---

## Cytotoxicity

Lapatinib is an antineoplastic agent (referenced in this evidence pack in the context of HER2-positive breast cancer treatment).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (dual EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (DFSP) has no supporting clinical trials or literature, and the evidence pack itself identifies no plausible mechanistic link between lapatinib's EGFR/HER2 inhibition and DFSP's PDGFR-driven pathology. A high TxGNN score alone is insufficient to progress this candidate.

**To proceed, the following is needed:**
- Confirmed original indication and formal MOA data for lapatinib (currently data gaps)
- TGA/ARTG registration status verification
- Preclinical or mechanistic studies specific to DFSP
- Safety and drug-interaction data (currently unavailable)

**Note:** Within this same evidence pack, rank 8 (*Plasmodium falciparum* malaria) carries stronger supporting evidence — L3, in-vitro data showing lapatinib inhibits haemozoin formation — and may warrant separate evaluation as a more mechanistically grounded signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

