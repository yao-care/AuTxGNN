---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Cladribine
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

# Cladribine: From Hairy Cell Leukaemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analogue with established efficacy in hairy cell leukaemia and, more recently, relapsing-remitting multiple sclerosis (approved overseas as Leustatin® and Mavenclad® respectively). The TxGNN model predicts it may be effective for **Parameningeal Embryonal Rhabdomyosarcoma** — a rare, high-risk paediatric tumour invading adjacent meningeal structures — however, there are currently **0 clinical trials** and **0 publications** directly supporting this specific indication. This prediction is supported by computational modelling only (Evidence Level L5), and further preclinical and clinical investigation is required before any translational steps can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hairy cell leukaemia; relapsing-remitting multiple sclerosis (from established overseas approvals — no Australian ARTG registration exists) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the submitted Evidence Pack. Based on published pharmacology, Cladribine is a synthetic chlorinated purine nucleoside analogue. It is phosphorylated intracellularly by deoxycytidine kinase (dCK) to an active triphosphate form, which accumulates in lymphocytes and monocytes and disrupts both DNA synthesis and repair — ultimately triggering apoptosis in dividing and resting cells alike. This selectivity for haematopoietic cells explains its strong efficacy in lymphoid malignancies such as hairy cell leukaemia.

Parameningeal embryonal rhabdomyosarcoma (RMS) is among the poorest-prognosis subtypes of RMS, characterised by anatomical proximity to meningeal structures and a high risk of CNS dissemination. The TxGNN knowledge graph connects Cladribine to RMS through the purine metabolism pathway: rhabdomyosarcoma cells express dCK to varying degrees, providing a theoretical basis for intracellular drug activation. A relevant pharmacokinetic advantage is Cladribine's CNS penetration — cerebrospinal fluid concentrations reach approximately 25% of plasma levels — which could theoretically benefit parameningeal disease where local drug exposure is clinically meaningful.

However, this prediction is entirely computational. The high TxGNN scores observed across multiple RMS subtypes in this Evidence Pack (ranks 1–5 and 8 are all RMS-related) strongly suggest a **knowledge graph cluster effect**: Cladribine's node in the graph connects to the parent RMS ontological node and propagates high scores across all child nodes, rather than producing independently validated signals for each subtype. The relative paucity of direct mechanistic evidence — particularly the lower dCK expression in mesenchymal tumours compared to lymphoid malignancies — introduces significant uncertainty about drug activation efficiency in this tumour type.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cladribine in parameningeal embryonal rhabdomyosarcoma.

---

## Literature Evidence

Currently no related literature available for Cladribine in parameningeal embryonal rhabdomyosarcoma.

---

## Australia Market Information

Cladribine is not currently registered with the Therapeutic Goods Administration (TGA) and holds no ARTG entries. There are no TGA-approved Product Information documents available through standard Australian channels.

Prescribers wishing to access Cladribine in Australia would need to do so via:
- **TGA Special Access Scheme (SAS)** — Category B or C depending on clinical urgency
- **Authorised Prescriber** pathway for ongoing access in defined patient populations

For safety and dosing reference, the following overseas-approved documents are the most relevant interim resources:
- **FDA**: Leustatin® (cladribine injection) Prescribing Information — hairy cell leukaemia
- **EMA**: Mavenclad® (cladribine tablets) SmPC — relapsing-remitting multiple sclerosis

---

## Cytotoxicity

Cladribine is an antineoplastic purine nucleoside analogue (conventional cytotoxic chemotherapy). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analogue (2-chlorodeoxyadenosine) |
| Myelosuppression Risk | **High** — severe and prolonged lymphopenia and neutropenia are dose-limiting class effects; CD4+ T-cell depletion may persist for months to years |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count with differential (FBC), CD4+ and CD8+ lymphocyte subsets, serum creatinine and LFTs, signs and symptoms of opportunistic infection |
| Handling Protection | Must be prepared and administered following cytotoxic drug handling regulations; avoid skin or mucous membrane contact |

---

## Safety Considerations

As Cladribine is not registered in Australia, no TGA-approved Product Information is available. Please refer to the FDA Leustatin® prescribing information or the EMA Mavenclad® SmPC for full safety information including warnings regarding severe myelosuppression, immunosuppression, opportunistic infections, and use in pregnancy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates high prediction scores for Cladribine across multiple rhabdomyosarcoma subtypes; however, these likely reflect a knowledge graph cluster effect rather than independently validated signals. There is no clinical or preclinical evidence specifically supporting Cladribine use in parameningeal embryonal rhabdomyosarcoma, the drug is not registered in Australia, and comprehensive safety data is unavailable through local regulatory channels.

**To proceed, the following is needed:**

- **Preclinical validation**: dCK expression profiling in parameningeal RMS cell lines and patient-derived xenograft (PDX) models to confirm drug activation potential
- **Broader RMS literature review**: Systematic search for Cladribine (or structurally related purine analogues such as clofarabine, nelarabine) in paediatric solid tumours, to characterise the class effect and identify any indirect supporting evidence
- **Safety data remediation**: Download and review of overseas PI documents (FDA Leustatin® / EMA Mavenclad® SmPC) for complete warnings, contraindications, and drug interactions — this gap is rated **Blocking** in the Evidence Pack
- **Standard-of-care assessment**: Review current COG ARST protocols and SIOP/CWS RMS guidelines to define where Cladribine could fit (salvage setting, combination partner, CNS-penetrant alternative) and identify the target patient population
- **TGA access pathway planning**: If a compassionate use or investigator-initiated trial is being considered, initiate a TGA Special Access Scheme or Authorised Prescriber application early in the planning process

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

