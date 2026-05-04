---
layout: default
title: Eprosartan
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Eprosartan
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

# Eprosartan: From Hypertension to Malignant Renovascular Hypertension

---

## One-Sentence Summary

Eprosartan is an angiotensin receptor blocker (ARB) belonging to the AT1 antagonist class, used clinically for the management of hypertension.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with a mechanistic fit rated **Grade A** due to direct RAS pathway alignment — however, **no Eprosartan-specific clinical trials or direct literature** for this indication have been identified to date, keeping the evidence at Level L4.

> **Note for clinicians:** Although malignant renovascular hypertension is the top-ranked TxGNN prediction, a lower-ranked prediction — **ischemic stroke susceptibility (Rank 7)** — carries an independently assessed **L2 evidence level** and a "Proceed with Guardrails" recommendation. Clinicians should consider reviewing that indication in parallel.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ARB class; not formally registered in Australia) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 93.69% |
| Evidence Level | L4 (Mechanistic / class-level evidence only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eprosartan is a selective angiotensin II receptor antagonist (AT1 blocker) that prevents angiotensin II from binding to its target receptor, thereby blocking the downstream cascade of vasoconstriction and aldosterone secretion. Notably, Eprosartan may also inhibit presynaptic AT1 receptors on sympathetic nerve terminals — a dual mechanism (AT1 blockade + sympathetic inhibition) that may distinguish it from some other ARBs and could be particularly relevant in settings of high sympathetic drive.

The core pathophysiology of malignant renovascular hypertension is a textbook example of RAS over-activation: renal artery stenosis triggers sustained renin release → angiotensin II overproduction → severe, accelerated hypertension with end-organ damage. Eprosartan's mechanism directly targets the angiotensin II effector step in this cascade, representing a Grade A mechanistic fit as assessed in the TxGNN analysis. The drug essentially addresses the effector arm of the very pathway that drives this condition.

The biological rationale is further supported by established class-level evidence: other ARBs — specifically losartan (RENAAL trial) and irbesartan (IDNT trial) — have demonstrated renal-protective benefits in hypertensive renal disease in large randomised trials, and ARB use in renovascular hypertension is already embedded in specialist practice. What is missing is Eprosartan-specific trial data for this precise indication. The TxGNN model has identified a mechanistically sound target, but direct clinical evidence has yet to be generated.

---

## Clinical Trial Evidence

No clinical trials are currently registered for Eprosartan in malignant renovascular hypertension (search conducted 10 March 2026 across ClinicalTrials.gov and ICTRP, including ANZCTR).

---

## Literature Evidence

No directly relevant literature was identified for Eprosartan in malignant renovascular hypertension (PubMed search conducted 10 March 2026).

> **Context for the broader prediction set:** 20 PubMed records were retrieved for indication Rank 4 (pulmonary hypertension owing to lung disease/hypoxia), but review indicated these publications address hypoxia biology generally and do not study Eprosartan specifically in pulmonary hypertension. They are not included here as they do not constitute supporting evidence for the primary predicted indication.

---

## Australia Market Information

Eprosartan (DrugBank ID: DB00876) is **not currently registered with the Therapeutic Goods Administration (TGA)** and has no ARTG entries. It is not available as a marketed product in Australia.

Clinicians requiring prescribing information should refer to international product labelling (e.g., FDA-approved prescribing information for Teveten®, or EMA assessment reports) as no TGA-approved Product Information (PI) exists.

---

## Safety Considerations

No TGA-approved Product Information is available for Eprosartan in Australia. No drug interaction data was retrieved in the evidence search.

Please refer to international prescribing information (FDA/EMA-approved Teveten® PI) for comprehensive safety guidance, including:
- Foetal/neonatal toxicity (class effect of all ARBs — contraindicated in pregnancy)
- Hyperkalaemia risk, particularly in renal impairment or with concurrent potassium-sparing agents
- First-dose hypotension in volume-depleted patients
- Renal function monitoring in bilateral renal artery stenosis (the very population targeted by this prediction — ARBs can precipitate acute kidney injury in this setting and require careful risk-benefit assessment)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Eprosartan in malignant renovascular hypertension is strong (Grade A alignment), and ARB class agents already have recognised clinical utility in RAS-mediated hypertensive conditions. However, no Eprosartan-specific clinical trial data exists for this indication (L4 evidence), the drug is not registered in Australia, and critically — ARB use in bilateral renal artery stenosis (a common cause of renovascular hypertension) carries a documented risk of precipitating acute kidney injury, requiring careful patient selection before any clinical exploration.

**To proceed, the following is needed:**

- **Mechanism of action confirmation:** Obtain full DrugBank MOA data to characterise Eprosartan's sympathetic inhibition component and whether it offers differentiated benefit over other ARBs already used in this setting
- **Safety review:** Formal risk-benefit analysis of ARB use specifically in bilateral renovascular disease; engage a renal/hypertension specialist to assess patient selection criteria
- **Class-level evidence mapping:** Systematic review of losartan and irbesartan data in malignant renovascular hypertension to establish whether class-level evidence is sufficient to support a pilot study
- **TGA registration pathway:** Assess SAS (Special Access Scheme) or clinical trial authorisation requirements given there is no current Australian registration
- **Parallel review of Rank 7 (Ischemic Stroke Susceptibility):** This lower-ranked TxGNN prediction carries an independently assessed L2 evidence level and "Proceed with Guardrails" recommendation — likely informed by the MOSES trial (Eprosartan vs. nitrendipine in secondary stroke prevention) — and may represent a more immediately actionable repurposing opportunity

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Report generated: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

