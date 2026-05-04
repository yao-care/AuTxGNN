---
layout: default
title: Alemtuzumab
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Alemtuzumab
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

# Alemtuzumab: From Chronic Lymphocytic Leukaemia to Hepatic Infarction

## One-Sentence Summary

Alemtuzumab (Campath/Lemtrada) is a humanised anti-CD52 monoclonal antibody approved internationally for B-cell chronic lymphocytic leukaemia (CLL) and relapsing-remitting multiple sclerosis, but it is not currently marketed in Australia.
The TxGNN model assigns it the highest repurposing score for **Hepatic Infarction** (94.44%), however this indication is currently supported by **no clinical trials and no published literature** — suggesting the prediction may reflect a knowledge graph artefact rather than a genuine biological signal.
For clinical context, the second-ranked prediction — **syndrome with combined immunodeficiency** — carries evidence level L2 with a "Proceed with Guardrails" recommendation, supported by 13 clinical trials and 12 publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | B-cell chronic lymphocytic leukaemia; relapsing-remitting multiple sclerosis (international approvals; not TGA-registered) |
| Predicted New Indication | Hepatic Infarction |
| TxGNN Prediction Score | 94.44% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TGA-approved Product Information is available for Alemtuzumab in Australia due to the absence of ARTG registration. Based on published international data, Alemtuzumab is a humanised IgG1κ monoclonal antibody targeting CD52 — a glycoprotein expressed at high density on mature B and T lymphocytes, NK cells, monocytes, and macrophages. Binding to CD52 activates complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC), resulting in rapid, profound, and prolonged lymphodepletion. This mechanism underpins its efficacy in B-cell CLL and its role as an immunosuppressive conditioning agent in haematopoietic stem cell transplantation (HSCT).

The predicted indication of hepatic infarction presents a mechanistically weak link. Hepatic infarction is primarily a vascular condition caused by arterial embolism, critical hepatic hypoperfusion, or thrombosis of the hepatic artery — rather than an immune-mediated process. While Alemtuzumab's profound lymphodepletion could theoretically dampen any immune-mediated component of vascular endothelial inflammation, the drug has no direct anticoagulant, thrombolytic, or vasodilatory properties. The conditions are pathophysiologically dissimilar.

The high TxGNN score for this indication most likely reflects non-specific connectivity through "liver pathology" nodes in the underlying knowledge graph, rather than a validated mechanistic relationship. This type of prediction artefact is a recognised limitation of graph neural network models when applied to rare or predominantly vascular conditions with limited linked training data. Without any supporting clinical or preclinical evidence, this prediction requires substantial mechanistic validation before any further development steps can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Alemtuzumab is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No active ARTG entries exist for this drug. Alemtuzumab was previously marketed in Australia as **Lemtrada** (for relapsing-remitting MS) but has since been withdrawn from the Australian market. Healthcare professionals seeking to access this drug for clinical use should consult the TGA regarding the Special Access Scheme (SAS) or Authorised Prescriber pathways.

---

## Cytotoxicity

Alemtuzumab meets cytotoxicity section criteria — it is approved internationally for B-cell CLL (a haematological malignancy) and exerts direct cytotoxic effects on lymphoid cells via CDC and ADCC.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — anti-CD52 humanised monoclonal antibody (not a conventional cytotoxic agent) |
| Myelosuppression Risk | High — profound and prolonged lymphodepletion affecting B cells, T cells, and NK cells; neutropenia and thrombocytopenia reported in clinical studies; immune reconstitution may take months to years |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC) with differential; lymphocyte subsets (particularly CD4+ T-cell counts); renal function; liver function tests; viral reactivation surveillance (CMV, EBV); thyroid function (autoimmune thyroid disease is a known delayed adverse effect in MS use) |
| Handling Protection | Follow institutional monoclonal antibody and biological therapy handling protocols; cytotoxic handling precautions should be applied in accordance with institutional policy and state/territory health regulations |

---

## Safety Considerations

Please refer to the international Product Information (PI) — available from the EMA (Lemtrada) or FDA (Campath) — for comprehensive safety information, including black box warnings related to serious autoimmune conditions, infusion reactions, and malignancy risk. No TGA-specific safety data is available due to the absence of current Australian registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns the highest prediction score to hepatic infarction, but the mechanistic link is biologically implausible — hepatic infarction is a vascular condition driven by arterial occlusion or hypoperfusion, and Alemtuzumab's mechanism (CD52-directed lymphodepletion) has no established relevance to this pathophysiology. The complete absence of clinical trial or published literature evidence confirms an L5 classification, and no development pathway can be recommended at this time.

**To proceed with this indication, the following would be needed:**
- Preclinical mechanistic studies investigating whether CD52-mediated lymphodepletion influences hepatic vascular or endothelial pathology
- Knowledge graph audit to determine whether the high TxGNN score reflects a genuine biological signal or a non-specific connectivity artefact
- Detailed MOA documentation from DrugBank and current international PI to support any hypothesis generation

---

> **Higher-Priority Repurposing Candidate — Separate Evaluation Recommended**
>
> The second-ranked TxGNN prediction, **syndrome with combined immunodeficiency** (score: 93.73%, evidence level: **L2**), is supported by 13 clinical trials — including a completed Phase 2/3 study (NCT01019876) and two active Phase 2 recruiting trials (NCT01962415, NCT07284641) — and 12 published studies. Alemtuzumab's mechanism as a lymphodepleting conditioning agent for HSCT is directly relevant to this indication, and the recommendation is **"Proceed with Guardrails."** A dedicated evaluation report for this candidate is strongly advised.

---

*This report is generated for research reference purposes only and does not constitute medical or prescribing advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

