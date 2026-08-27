---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Labetalol
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

> Labetalol is a combined alpha/beta-adrenergic blocking agent, clinically established for the treatment of hypertension, including hypertensive emergencies.
> The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
> though currently only **0 clinical trials** and **2 case-report publications** support this specific direction, and key regulatory safety data remain unavailable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, including hypertensive emergencies (based on known clinical use — no confirmed local regulatory record; see Data Gap below) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| Australia Market Status | Not currently marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for labetalol is not available in this evidence pack (Data Gap — High severity, remediation pending via DrugBank API). Based on known pharmacology, labetalol is a combined alpha‑1 and non-selective beta-adrenergic blocking agent, and its efficacy in hypertension — including severe and hypertensive-emergency presentations — is well established and is already the basis for its IV use in accelerated/malignant hypertension.

Malignant renovascular hypertension is, mechanistically, a severe subtype of hypertension driven by excessive renin-angiotensin activation secondary to renal artery narrowing. Because labetalol's original indication already covers malignant hypertension as a clinical entity, the predicted extension to the renovascular subtype is pharmacologically plausible — it does not require a new mechanism, only application of an existing one to a specific aetiology. This is reflected in the model's very high prediction score.

However, the supporting evidence in this pack does not yet demonstrate this specifically: the two literature citations describe labetalol being used as part of blood-pressure control in cases of malignant hypertension, but neither is a dedicated study of labetalol in renovascular hypertension. The mechanistic rationale is therefore reasonable, but currently inferred rather than directly demonstrated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case Report | The Medical Journal of Australia | Case of malignant hypertension (with renal arteritis/aneurysms and cortical infarction) in a young man; minoxidil and labetalol were used for initial blood pressure control. |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case Report | BMC Nephrology | Paediatric case of hyponatremic hypertensive syndrome presenting as malignant hypertension in the setting of renovascular disease; illustrates the clinical overlap between renovascular and malignant hypertension but does not directly evaluate labetalol. |

---

## Australia Market Information

Labetalol currently has no ARTG entries recorded in this evidence pack (0 licenses; market status: not marketed). No product, dosage form, or approved-indication data are available for Australia at this time.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Note: A Blocking-severity data gap has been identified — TFDA/PI-equivalent warnings and contraindications for labetalol are not currently available in this dataset, which prevents completion of the initial (S1) safety screening stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for labetalol in malignant renovascular hypertension is currently limited to two case reports (L4, no dedicated clinical trials), and a Blocking data gap (missing PI warnings/contraindications) prevents entry into the S1 safety review stage. While the mechanistic rationale is reasonable given labetalol's established role in hypertensive emergencies, dedicated evidence for this specific renovascular subtype is not yet sufficient to proceed.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — key warnings and contraindications (Blocking data gap)
- Detailed mechanism of action (MOA) data via DrugBank (High-priority data gap)
- Targeted literature/clinical search specifically on labetalol use in renovascular or malignant hypertension subtypes
- Confirmation of ARTG/TGA registration status for labetalol in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

