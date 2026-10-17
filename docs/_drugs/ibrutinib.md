---
layout: default
title: Ibrutinib
parent: Model Prediction Only (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ibrutinib: predicted new indication Polyclonal hypergammaglobulinemia (evidence level L5). Approved use: Mantle cell lymphoma…"
monitor_inn: "Ibrutinib"
predicted_indications: ["polyclonal hypergammaglobulinemia", "monoclonal paraproteinemia disease", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "small intestinal Burkitt lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "marginal zone lymphoma", "extracutaneous mastocytoma"]
---

# Ibrutinib
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

# Ibrutinib: From B-Cell Malignancies to Polyclonal Hypergammaglobulinemia

## One-Sentence Summary

Ibrutinib is an oral Bruton's tyrosine kinase (BTK) inhibitor, originally used for B-cell cancers such as mantle cell lymphoma and Waldenström macroglobulinemia.
The TxGNN model predicts it may be effective for **polyclonal hypergammaglobulinemia** (raised immunoglobulin levels from many B-cell clones), with a score of 91.8%.
**No clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma, Waldenström macroglobulinemia and other B-cell neoplasms (from the knowledge graph; no approved-indication text was available in the Australian licence data) |
| Predicted New Indication | Polyclonal hypergammaglobulinemia |
| TxGNN Prediction Score | 91.75% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibrutinib is known as a BTK inhibitor, and its efficacy in B-cell malignancies is established. Mechanistically, it may be applicable to polyclonal hypergammaglobulinemia.

BTK is a key signalling step in B-cell activation. Blocking it could plausibly reduce B-cell activation and immunoglobulin production, which is the biological link to this prediction. The original indications are B-cell neoplasms, some of which (such as Waldenström macroglobulinemia) involve excess immunoglobulin production. Excess immunoglobulin from many B-cell clones is a different clinical situation, however, and no study was provided to show that BTK inhibition corrects it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11213E | Imbruvica | Capsule 140 mg (oral) | Not specified in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions |
| Monitoring Items | Full blood count; also consider cardiovascular status and bleeding, as noted in the PI |
| Handling Protection | Please refer to the PI and local institutional policy |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions; the 20 listed in the data compiled for this report include:
  - **Major**: aprepitant, acetylsalicylic acid (aspirin), clarithromycin, cobicistat and deferasirox.
  - **Moderate**: examples include loperamide, dexamethasone, cimetidine, miconazole and the gliptins (saxagliptin, linagliptin, sitagliptin).
  - **Minor**: prucalopride.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no trials, no literature and no confirmed mechanistic data for polyclonal hypergammaglobulinemia. This is Evidence Level L5.

Other predictions for ibrutinib in the same data are better supported, and a review could look at them first:
- **Marginal zone lymphoma**: a Phase 3 trial (SELENE, NCT01974440), several Phase 2 studies and published long-term follow-up. It could proceed with guardrails, because the Phase 3 population mixes follicular and marginal zone lymphoma.
- **Monoclonal paraproteinemia (Waldenström macroglobulinemia)**: largely an existing indication rather than true repurposing.

**To proceed, the following is needed:**
- Mechanism of action data confirming how BTK inhibition would affect polyclonal immunoglobulin production
- Preclinical or early clinical evidence in hypergammaglobulinemia
- The TGA-approved PI warnings and contraindications, which were not available for this review
- A benefit-risk assessment against known BTK-inhibitor toxicities and the major drug interactions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

