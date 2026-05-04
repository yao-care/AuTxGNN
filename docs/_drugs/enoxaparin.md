---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Enoxaparin
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

# Enoxaparin: From Venous Thromboembolism to Protein C Deficiency Thrombophilia

---

## One-Sentence Summary

Enoxaparin is a low molecular weight heparin (LMWH) widely used for the prevention and treatment of venous thromboembolism (VTE), including deep vein thrombosis (DVT), pulmonary embolism (PE), and acute coronary syndromes.
The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency (Autosomal Recessive)**, achieving a prediction score of **99.58%** (rank 5,301 among all drug-disease pairs in the knowledge graph).
The current dataset contains **no dedicated clinical trials or publications** for this specific indication; however, the mechanistic rationale is supported by established clinical guideline recommendations that position LMWH as a preferred anticoagulant in protein C-deficient patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Venous thromboembolism prevention and treatment (VTE/DVT/PE); acute coronary syndromes — no ARTG entries were returned by the data query (see Australia Market Information) |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency (Autosomal Recessive) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 (Mechanistic reasoning and indirect clinical guideline support; no dedicated trials or publications in dataset) |
| Australia Market Status | Not found in ARTG query (0 entries returned; likely a data retrieval limitation) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacology, Enoxaparin is a low molecular weight heparin that acts primarily by binding to antithrombin III (AT-III) and potentiating its inhibition of **Factor Xa**, with limited additional activity against thrombin (Factor IIa). This interrupts the coagulation cascade downstream, reducing fibrin clot formation independently of the protein C anticoagulation pathway.

The mechanistic connection between Enoxaparin and autosomal recessive protein C deficiency is theoretically compelling. Protein C deficiency leads to impaired inhibition of the activated cofactors **Factor Va and Factor VIIIa**, creating a persistent hypercoagulable state with a significantly elevated risk of venous thrombosis. Because Enoxaparin acts via Factor Xa inhibition — a step that is *downstream* of, and independent from, the protein C pathway — it can effectively provide anticoagulant protection even when protein C is absent or severely reduced. This represents a mechanistic bypass of the primary defect.

Critically, international clinical guidelines already recommend LMWH as the **preferred anticoagulant** over vitamin K antagonists (VKAs) such as warfarin in patients with protein C deficiency. The basis for this preference is that warfarin transiently suppresses protein C (which is already critically low in these patients) before achieving full therapeutic anticoagulation, creating a paradoxical pro-thrombotic window that can precipitate **warfarin-induced skin necrosis** — a serious and potentially disfiguring complication. The TxGNN model's high prediction score (99.58%) therefore reflects an indication already embedded in clinical practice, even though the specific autosomal recessive subtype has not been the subject of dedicated prospective trials in the retrieved dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Enoxaparin in Thrombophilia due to Protein C Deficiency (Autosomal Recessive).

> **Note:** The clinical trial search query returned 0 results for this specific drug-disease pair. This is consistent with the rarity of autosomal recessive protein C deficiency (an orphan-level condition) and the fact that LMWH use in this context is largely guided by consensus recommendation rather than formal randomised trial evidence.

---

## Literature Evidence

Currently no related literature available for Enoxaparin in Thrombophilia due to Protein C Deficiency (Autosomal Recessive).

> **Note:** The PubMed search returned 0 results for this specific combination. Clinicians seeking supporting evidence should review guidance documents from the International Society on Thrombosis and Haemostasis (ISTH) and the American Society of Hematology (ASH) on hereditary thrombophilia management, which address LMWH use in congenital protein C deficiency.

---

## Australia Market Information

The ARTG data query for Enoxaparin returned **0 registered products**, and market status was recorded as "not marketed." This result is inconsistent with the known TGA approval history of Enoxaparin sodium (Clexane®, sanofi-aventis), which has been a registered and widely used anticoagulant in Australian hospitals. This discrepancy is most likely attributable to a data retrieval or field-mapping limitation in the current dataset rather than a genuine absence from the Australian market.

**Clinicians and researchers should verify current ARTG registration status directly via:**
- [TGA ARTG Public Summary Search](https://www.tga.gov.au/resources/artg) — search for "enoxaparin" or "Clexane"
- The TGA-approved Product Information (PI) for Clexane® contains Australian-specific dosing, warnings, and contraindications

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information. Full Australian-specific safety data — including registered warnings, contraindications, and drug interaction profiles — was not available in this dataset.

> **Important for clinical context:** As a general principle for LMWH use, clinicians should be aware of bleeding risk (including in patients with thrombocytopenia, renal impairment, or concomitant antiplatelet therapy), the need for anti-Xa monitoring in select populations (renal failure, obesity, pregnancy, paediatrics), and the risk of heparin-induced thrombocytopenia (HIT), which, while lower than with unfractionated heparin, remains clinically relevant. Protein C-deficient patients on long-term LMWH will require ongoing haematological monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of LMWH — including Enoxaparin — in patients with congenital protein C deficiency is already consistent with clinical guideline recommendations as a preferred anticoagulation strategy, and the mechanism of action provides a direct and logical basis for efficacy in this indication. The primary gap is not a safety or plausibility concern, but rather the absence of formal prospective evidence specifically in the autosomal recessive subtype, which warrants a structured approach before broader clinical adoption.

**To proceed, the following is needed:**

- **Confirm ARTG status:** Verify current TGA registration for Enoxaparin sodium (Clexane®) directly via the ARTG Public Summary, as the current data query returned 0 entries and appears to reflect a retrieval limitation
- **Obtain TGA Product Information (PI):** Review the full Australian PI for Clexane® to identify registered indications, dosing schedules, warnings, and contraindications relevant to this patient population
- **Targeted literature review:** Conduct a focused search for Enoxaparin (or LMWH class) in hereditary/congenital protein C deficiency, including paediatric populations, long-term management, and transition to oral anticoagulants
- **Review haematology guidelines:** Consult current ISTH, ASH, and British Society for Haematology (BSH) guidance on anticoagulation in hereditary thrombophilias, particularly for the neonatal and paediatric presentations of autosomal recessive protein C deficiency (which may present with purpura fulminans)
- **Assess route and formulation feasibility:** Enoxaparin is a subcutaneous injection; confirm suitability for the intended patient population (chronic use, paediatric dosing, renal dose adjustment)
- **Safety monitoring plan:** Develop a monitoring protocol covering anti-Xa levels, full blood count (FBC), renal function, platelet count (HIT surveillance), and bleeding events for any prospective use
- **Evidence generation:** Consider a prospective case registry or multi-centre observational study to generate Australian-specific data for this rare indication, in collaboration with haematology networks such as the Haematology Society of Australia and New Zealand (HSANZ)

---

> ⚠️ **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by the TxGNN model require clinical validation before therapeutic application. Healthcare professionals should refer to current TGA-approved Product Information and consult relevant clinical guidelines when making prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

