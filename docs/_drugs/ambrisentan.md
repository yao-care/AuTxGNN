---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

> **YMYL Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.

---

## One-Sentence Summary

Ambrisentan is a selective endothelin receptor type A (ETA) antagonist approved internationally for the treatment of pulmonary arterial hypertension (PAH), though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Pulmonary Arteriovenous Malformation (PAVM)** as its top-ranked new indication,
with **no registered clinical trials** and **1 case report publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not TGA-registered; internationally approved for Pulmonary Arterial Hypertension |
| Predicted New Indication | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Ambrisentan is a selective endothelin receptor type A (ETA) antagonist. By blocking ETA receptors in pulmonary vascular smooth muscle, it reduces endothelin-1 (ET-1)-mediated vasoconstriction and pathological vascular remodelling — the mechanism underpinning its efficacy in pulmonary arterial hypertension.

Pulmonary arteriovenous malformation (PAVM) involves abnormal direct connections between pulmonary arteries and veins that bypass the capillary bed, resulting in intrapulmonary right-to-left shunting. PAVM most commonly arises in the context of hereditary haemorrhagic telangiectasia (HHT) — an autosomal dominant vascular dysplasia — and is structurally distinct from PAH. The core pathology is one of abnormal vessel development, not ET-1-driven vasoconstriction or pulmonary hypertension.

While ET-1 plays a general role in vascular tone regulation, the mechanistic basis for ETA antagonism in treating structural PAVMs is considered weak. There is no established evidence that ET-1 pathway dysregulation drives PAVM formation or progression. The TxGNN model's high prediction score likely reflects shared vascular biology at the network level between PAH and PAVM (both classified as pulmonary vascular diseases), rather than actionable pharmacological overlap. Standard management of PAVM remains transcatheter embolisation or, in selected cases, surgical resection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World Journal of Clinical Cases | A single case of hereditary haemorrhagic telangiectasia (HHT) complicated by pulmonary arterial hypertension, with family gene analysis. Highlights HHT–PAH co-occurrence but does not evaluate Ambrisentan specifically for PAVM. |

---

## Australia Market Information

Ambrisentan is not currently registered with the Therapeutic Goods Administration (TGA) and holds no ARTG entries in Australia. Clinicians requiring access would need to explore the Special Access Scheme (SAS) or the Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) — or the internationally approved PI (e.g., EMA Volibris or FDA Letairis) — for comprehensive safety information, as no local safety data is available from the evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
PAVM is a structural vascular malformation managed primarily by interventional procedures (embolisation); there is no clinical or preclinical evidence supporting ETA antagonism as a therapeutic approach for PAVM, and the mechanistic link is weak. Additionally, Ambrisentan has no TGA registration in Australia, adding a significant access barrier.

**To proceed, the following is needed:**
- Retrieval of full MOA data from DrugBank (DB06403) to formally document pharmacology
- Preclinical or mechanistic evidence demonstrating an ET-1/ETA role in PAVM pathogenesis
- Review of TGA Product Information (or international PI equivalent) for contraindications, hepatotoxicity warnings, and teratogenicity (Category X)
- Assessment of TGA Special Access Scheme (SAS Category B) feasibility if clinical use is considered
- Consideration of stronger TxGNN-predicted indications with existing clinical trial evidence (see note below)

---

> **Supplementary Note — Other High-Scoring Indications:** While PAVM ranks first by TxGNN score, several other predicted indications for Ambrisentan carry substantially stronger clinical evidence and are more mechanistically plausible, including:
> - **PAH associated with HIV infection** (Rank 3, Evidence Level L1, TxGNN 99.30%) — supported by 1 completed Phase 3 RCT and retrospective cohort data; **Recommended: Proceed with Guardrails**
> - **PAH associated with connective tissue disease** (Rank 6, Evidence Level L2, TxGNN 99.30%) — supported by 3 clinical trials (2 completed) and a systematic review/meta-analysis in *JAMA*; **Recommended: Proceed with Guardrails**
> - **PAH associated with congenital heart disease** (Rank 2, Evidence Level L2, TxGNN 99.37%) — supported by 9 trials including a completed Phase 3b study in 134 Chinese PAH patients; **Recommended: Research Question**
>
> These indications warrant separate full evaluation reports if clinical prioritisation is being considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

