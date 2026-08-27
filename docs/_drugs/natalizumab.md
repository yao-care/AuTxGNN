---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: From an Undocumented Original Indication to Bronchitis (Data Gap)

## One-Sentence Summary

Natalizumab's original indication and mechanism of action are not yet recorded in this evidence pack (data gaps DG001/DG002). The TxGNN model's top-ranked prediction for this drug is **Bronchitis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a model-only prediction with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licences or indication text recorded (data gap, see DG001) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Natalizumab (data gap DG002, pending DrugBank API lookup). Based on what the evidence pack does contain, Natalizumab is an anti‑α4‑integrin monoclonal antibody (VLA‑4 antagonist) that blocks leukocyte transendothelial migration, producing a systemic immunosuppressive effect.

For the Bronchitis prediction specifically, the evidence pack's own mechanistic assessment notes that blocking leukocyte migration could theoretically alter airway immune responses, but VLA‑4 antagonists are also known to increase infection risk — a direction that works *against*, not for, a respiratory-infection indication like bronchitis. No clinical trial or literature evidence exists to resolve this in either direction.

Because the original indication and MOA are both unrecorded data gaps, a proper comparison between the original and predicted indications cannot be completed at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

No TGA-approved Product Information exists for Natalizumab in Australia (the drug has 0 ARTG entries). Key warnings, contraindications, and drug interaction data are all recorded as data gaps in this evidence pack — this is a **Blocking** gap (DG001) that prevents any Stage 1 (S1) safety pre-assessment from proceeding.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the evidence level is L5 — a model-only prediction with zero clinical trials or literature support. The rationale text accompanying this prediction itself flags a mechanistically unfavourable direction (VLA‑4 antagonism raising infection risk rather than treating bronchitis). Natalizumab is also unregistered in Australia, and a Blocking data gap (DG001) prevents safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/TGA product safety data (DG001, Blocking) — required before any S1 safety pre-assessment can start
- Detailed mechanism of action data (DG002, High) to properly assess mechanistic plausibility
- At least one supportive clinical trial or publication directly evaluating Natalizumab in a bronchitis or related respiratory indication
- A regulatory pathway assessment, given the drug currently has no ARTG registration

**Additional context:** Nine other TxGNN-predicted indications were reviewed for this drug in the same evidence pack (parapsoriasis, psoriasis, severe nonproliferative diabetic retinopathy, acute lichenoid pityriasis, pityriasis lichenoides, penile fibromatosis, pustulosis palmaris et plantaris, dermatitis, neonatal dermatomyositis). None exceeded L4 evidence, and the literature available for the skin-related candidates (psoriasis, dermatitis, pustulosis palmaris et plantaris) predominantly describes Natalizumab-*induced* adverse skin reactions or PML risk rather than therapeutic benefit. All ten candidates carry a Hold recommendation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

