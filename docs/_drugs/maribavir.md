---
layout: default
title: Maribavir
parent: Model Prediction Only (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Maribavir: predicted new indication Bronchitis (evidence level L5). Approved use: Not available in the data compiled for this report (maribavir is know…"
monitor_inn: "Maribavir"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "bronchial neoplasm (disease)", "diabetic retinopathy", "filariasis", "rectosigmoid junction neoplasm", "colonic lymphangioma", "lipoma of colon", "cecum neuroendocrine tumor G1", "cecum villous adenoma"]
---

# Maribavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Maribavir: From Cytomegalovirus Infection to Bronchitis

## One-Sentence Summary

Maribavir is an oral antiviral that inhibits the cytomegalovirus (CMV) UL97 protein kinase. It is marketed in Australia as Livtencity, but the data compiled for this report do not include an approved indication text.
The TxGNN model predicts it may be effective for **bronchitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (maribavir is known as an anti-CMV agent) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 87.79% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Maribavir is a benzimidazole riboside that inhibits the human CMV UL97 protein kinase. This blocks viral DNA replication, assembly and nuclear egress.

No clear mechanistic link between maribavir and bronchitis has been established. Most bronchitis cases are caused by non-CMV viruses or bacteria, which maribavir is not known to act against. A possible tangential link exists only for CMV-associated respiratory infection in immunocompromised patients.

The high TxGNN score is a computational prediction only. It should not be read as evidence of efficacy.

**Other predictions (all L5, all Hold):** The model also ranked the following conditions. None has clinical trial or literature support, and none has a plausible mechanistic link to UL97 kinase inhibition.

| Rank | Predicted Disease | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Severe nonproliferative diabetic retinopathy | 79.11% | No link to VEGF, inflammatory or microvascular pathways |
| 3 | Bronchial neoplasm | 77.78% | Unvalidated link via CMV presence in some tumours |
| 4 | Diabetic retinopathy | 76.24% | Broader category of rank 2, same lack of rationale |
| 5 | Filariasis | 74.26% | No known activity against filarial parasites |
| 6 | Rectosigmoid junction neoplasm | 73.41% | Likely a graph-association artefact |
| 7 | Colonic lymphangioma | 73.32% | Benign malformation, no plausible link |
| 8 | Lipoma of colon | 73.23% | Benign adipose tumour, no plausible link |
| 9 | Caecum neuroendocrine tumour G1 | 73.13% | No activity against tumour drivers |
| 10 | Caecum villous adenoma | 73.07% | Wnt/APC-driven lesion, not targeted by maribavir |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14856X | Livtencity | Tablet 200 mg (oral) | Not available in the data compiled |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction records were found in the data compiled for this report, and no knowledge-graph contraindications were listed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or publications, and no plausible mechanistic link between CMV UL97 kinase inhibition and bronchitis. Safety data are also incomplete.

**To proceed, the following is needed:**
- The approved indication text for Livtencity from the ARTG entry and TGA Product Information
- Warnings and contraindications from the Product Information (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Evidence of CMV involvement in bronchitis, or a better-supported indication, through a targeted literature and trial registry search (including ANZCTR)
- A route and formulation compatibility assessment (currently oral tablet only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

