---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Nebivolol
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

# Nebivolol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Nebivolol is a third-generation, β1-selective adrenergic blocker with nitric-oxide-mediated vasodilatory action, originally used to treat hypertension. The TxGNN model's top-ranked prediction for this drug is **malignant renovascular hypertension**, but currently **no clinical trials or published literature** directly support this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (per drug-class literature in this evidence pack) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Nebivolol is not available in this evidence pack (flagged as a High-severity data gap). Based on known information within the supporting literature (e.g. PMID 19393838, 31066991, 30426333), Nebivolol is a third-generation β1-selective adrenoceptor antagonist that also promotes nitric-oxide-mediated vasodilation, and its efficacy in essential hypertension is well established.

Malignant renovascular hypertension is a severe, renin-angiotensin-driven subtype of hypertension, so there is a plausible pharmacological class-level link to a general antihypertensive agent. However, this is a theoretical extension rather than a demonstrated one: malignant hypertension is a hypertensive emergency typically managed with intravenous antihypertensives for rapid blood pressure control, and oral β-blockers such as nebivolol are not standard first-line therapy in this acute setting. No trial or publication in this evidence pack tests nebivolol specifically in this population.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is zero clinical trial or literature evidence for nebivolol in malignant renovascular hypertension, and the acute/emergency nature of this condition makes an oral β-blocker mechanistically questionable as monotherapy. Evidence is insufficient to progress beyond hypothesis stage.

**To proceed, the following is needed:**
- Direct pharmacological or clinical evidence linking nebivolol specifically to renovascular/malignant hypertension
- TFDA/TGA Product Information (PI) — labelled warnings and contraindications are currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Confirmation of Australian regulatory/ARTG status, as the drug is currently not marketed

---

### Note: Other Predicted Indications with Stronger Evidence

The same evidence pack contains two lower-ranked predictions with meaningfully more support than the top-ranked candidate above, worth flagging for anyone triaging this drug's repurposing portfolio:

| Rank | Indication | Evidence Level | Decision Stage | Key Support |
|------|-----------|----------------|-----------------|-------------|
| 6 | Chronic pulmonary heart disease (cor pulmonale) | L2 | Research Question | 4 clinical trials incl. a head-to-head Phase 4 vs. carvedilol/bisoprolol in heart failure and hypoxia (NCT00517725, NCT00924833); 18 literature entries on β-blocker safety in COPD/HF overlap |
| 7 | Prinzmetal (vasospastic) angina | L2 | Research Question | Direct Phase 4 completed trial "The Effect of Nebivolol in Hypertensive Patients With Coronary Arterial Spasm" (NCT03930433, n=51) |

By contrast, ranks 1–5, 8–10 (including the title indication above) are all Evidence Level L5 with no supporting trials or literature — several (e.g. Braddock syndrome, ocular tuberculosis, congenital TMJ ankylosis) appear to be knowledge-graph noise with no plausible mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

