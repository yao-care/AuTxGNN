---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Antifolate Chemotherapy Agent to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is a long-established antifolate (dihydrofolate reductase inhibitor) used across numerous chemotherapy and immunomodulatory regimens. The TxGNN model's top-ranked prediction links it to **Pulmonary Blastoma**, but this evidence pack shows **0 clinical trials** and **0 publications** currently supporting that specific link — it is a pure knowledge-graph association at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (original indication and mechanism of action are both flagged as data gaps — DG001/DG002) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Methotrexate is not available in this evidence pack. Based on the information present, Methotrexate is widely recognised as an antifolate (antimetabolite) chemotherapeutic and immunomodulatory agent — this is reflected throughout the trial records returned for other candidate indications in this same data pull, which repeatedly describe it as blocking enzymes needed for cell growth in rapidly dividing cells.

The link to pulmonary blastoma is a pure TxGNN knowledge-graph association: it extends Methotrexate's general antimetabolite/antineoplastic profile to a rare paediatric/young-adult lung tumour, without any disease-specific supporting data. Pulmonary blastoma is an extremely rare malignancy, and no clinical trials or peer-reviewed literature in this evidence pack test Methotrexate specifically in this condition.

Because the mechanistic rationale is generic rather than disease-specific, and no clinical or literature evidence exists for this indication, the prediction should currently be treated as a research hypothesis only, not a clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for Methotrexate in this evidence pack (0 of 0 licenses). According to this data pull, Methotrexate is currently listed as **not marketed** in Australia. Given Methotrexate is a widely used medicine internationally, this should be independently confirmed against the current TGA ARTG register before being relied upon.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — antifolate/antimetabolite (dihydrofolate reductase inhibitor), based on chemotherapy regimens described in this evidence pack's trial records |
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
- The pulmonary blastoma prediction is supported only by the TxGNN model score (L5, S0) with zero clinical trials or literature identified, and Methotrexate currently shows no Australian market presence in this evidence pack — there is no basis to progress this indication further at this time.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (PI) — warnings, contraindications, and interactions (Blocking gap DG001)
- Confirmed mechanism of action data (DG002)
- Independent verification of current TGA ARTG registration status for Methotrexate
- Any disease-specific pulmonary blastoma trial or case-report evidence, should it emerge

---

## Other TxGNN-Predicted Indications (Same Candidate Pack)

This evidence pack ("TW-DB00563-multi") scored Methotrexate against 10 candidate indications. The table below is provided for context — the two with the strongest underlying evidence (small cell lung carcinoma and Hodgkin lymphoma) reflect Methotrexate's historical use in older combination regimens (CMV, VBM) that have since been superseded by current standard-of-care, so neither reaches a "Go" recommendation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pulmonary blastoma | 99.45% | L5 | S0 | Hold |
| 2 | Primary pulmonary lymphoma | 99.45% | L4 | S1 | Research Question |
| 3 | Small cell lung carcinoma | 99.43% | L2 | S1 | Research Question |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | 99.42% | L5 | S0 | Hold |
| 5 | Hodgkin's lymphoma | 99.32% | L2 | S2 | Research Question |
| 6 | Rhabdomyosarcoma (disease) | 99.25% | L3 | S1 | Research Question |
| 7 | Pregerminal-centre CLL/SLL | 99.23% | L5 | S0 | Hold |
| 8 | CLL/SLL with IGHV somatic hypermutation | 99.23% | L5 | S0 | Hold |
| 9 | Parameningeal embryonal rhabdomyosarcoma | 99.21% | L5 | S0 | Hold |
| 10 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.21% | L5 | S0 | Hold |

If a full report is needed on small cell lung carcinoma or Hodgkin's lymphoma instead (the two candidates with actual L2-level historical clinical evidence in this pack), that can be generated separately using the same template.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

