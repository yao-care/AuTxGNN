---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Germ Cell Tumours and Small Cell Lung Cancer to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is an established cytotoxic chemotherapy agent (epipodophyllotoxin class / topoisomerase II inhibitor) used internationally for germ cell tumours, small cell lung cancer (SCLC), and lymphomas — although it holds no current TGA registration in Australia.
The TxGNN model predicts it may be effective for **Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFA)**,
with **0 clinical trials** and **1 case report publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally approved for germ cell tumours, small cell lung cancer, and lymphoma |
| Predicted New Indication | Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFA) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Etoposide is a topoisomerase II inhibitor belonging to the epipodophyllotoxin class. It works by stabilising the topoisomerase II–DNA cleavage complex, thereby inducing irreversible double-strand DNA breaks and triggering apoptosis in rapidly proliferating cells. This schedule-dependent mechanism is particularly effective against tumour cells with high mitotic activity.

Well-differentiated fetal adenocarcinoma of the lung (WDFA) is an exceptionally rare monophasic variant of pulmonary blastoma. Its tumour cells retain embryonic fetal lung epithelial characteristics, including active proliferative signalling pathways reminiscent of developing lung tissue. Because topoisomerase II expression is strongly upregulated in rapidly cycling cells, the theoretical basis for sensitivity to Etoposide is biologically plausible. Pulmonary blastoma as a broader entity (rank 3 in this dataset) shares the same embryonic histological features, and isolated case literature has documented etoposide-containing regimen responses in that setting.

However, this reasoning remains an indirect extrapolation. No dedicated studies of Etoposide in WDFA exist, and the high TxGNN score (99.94%) reflects algorithmic inference from biological graph similarity rather than validated clinical data. WDFA is so rare that dedicated trials are essentially infeasible without international multicentre collaboration. The current evidence does not support clinical use in WDFA outside of a research or compassionate-access framework.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Etoposide in well-differentiated fetal adenocarcinoma of the lung.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report + Literature Review | The Journal of International Medical Research | Classic biphasic pulmonary blastoma case; no standard treatment guidelines exist due to rarity. Patient received nedaplatin plus paclitaxel as adjuvant chemotherapy; on disease recurrence, further chemotherapy was administered. Etoposide not directly used in this case, but confirms the broader pulmonary blastoma/WDFA chemotherapy landscape |

---

## Australia Market Information

Etoposide currently has **no ARTG registration** and is not listed as a marketed product in Australia based on available data. Clinicians in Australia who require Etoposide for patients would need to access it through the TGA's **Special Access Scheme (SAS Category B or C)** or via an **Authorised Prescriber** arrangement, using international regulatory approvals (e.g., FDA, EMA) as the reference safety and efficacy basis.

> **Note for clinicians:** ARTG status should be independently verified via the TGA's official ARTG public summary ([https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg)), as registration status may change.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Epipodophyllotoxin class (topoisomerase II inhibitor) |
| Myelosuppression Risk | **High** — Neutropenia is the principal dose-limiting toxicity; thrombocytopenia and anaemia are common; febrile neutropenia risk is significant, particularly with multi-day IV regimens |
| Emetogenicity Classification | Low to moderate (IV formulation); moderate GI toxicity (nausea, vomiting, mucositis) more frequent with oral dosing |
| Monitoring Items | FBC with differential count (at least weekly during treatment cycles), liver function tests (ALT, AST, bilirubin), renal function (eGFR), blood pressure during IV infusion (hypotension risk), and cumulative haematological toxicity assessment |
| Handling Protection | Must be prepared and administered in accordance with cytotoxic drug handling regulations (SHPN/State health guidelines and ISOPP standards); biological safety cabinet required; personal protective equipment mandatory |

---

## Safety Considerations

Specific TGA-approved Product Information (PI) and TFDA prescribing information warnings are not available in this dataset. Please refer to the most current **internationally recognised Product Information** (FDA prescribing information, EMA SmPC, or equivalent) for complete safety information including:

- Bone marrow suppression monitoring protocols
- Secondary malignancy risk (treatment-related myeloid leukaemia — a known long-term risk with topoisomerase II inhibitors)
- Hypersensitivity reactions
- Reproductive toxicity and teratogenicity
- Drug–drug interaction profile

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a high algorithmic prediction score (99.94%) for Etoposide in well-differentiated fetal adenocarcinoma of the lung; however, this is supported by a single tangentially related case report and a biologically plausible but unvalidated mechanistic hypothesis. There is insufficient clinical evidence to support use in this indication, and the extreme rarity of WDFA makes prospective trial design highly challenging.

**To proceed, the following is needed:**
- Histopathological studies confirming topoisomerase II overexpression in WDFA tumour tissue
- Prospective case series or international registry data on WDFA treated with etoposide-containing regimens
- Consideration of compassionate access via TGA Special Access Scheme if a patient-level need is identified
- Collaboration with international rare tumour networks (e.g., EORTC Rare Cancers Working Group) to accumulate sufficient case numbers
- Formal MOA data (DrugBank) retrieval to strengthen the mechanistic rationale

---

> **Additional Note — Broader Prediction Landscape:** While WDFA ranks #1 by TxGNN score, clinicians should note that this dataset also contains **Level 1 evidence (L1 / Proceed with Guardrails)** predictions for **Ewing Sarcoma** (rank 4) and **Rhabdomyosarcoma** (rank 6), where Etoposide is already a core component of established chemotherapy regimens (VDC/IE and IRS protocols respectively). These indications may represent more actionable near-term clinical translation opportunities.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Produced by AuTxGNN — Drug Repurposing Research System (data cutoff: 5 April 2026).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

