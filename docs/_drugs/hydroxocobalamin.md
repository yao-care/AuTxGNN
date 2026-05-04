---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Varices Without Bleeding

## One-Sentence Summary

Hydroxocobalamin is the natural, injectable form of Vitamin B12, recognised globally for treating B12 deficiency states including megaloblastic anaemia, peripheral neuropathy, and pernicious anaemia.
The TxGNN model predicts it may be effective for **Esophageal Varices Without Bleeding**,
with **no clinical trials** and **no publications** currently supporting this specific direction.
This prediction carries an evidence level of **L5** — model prediction only — and a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B12 deficiency (megaloblastic anaemia, neurological complications, pernicious anaemia) |
| Predicted New Indication | Esophageal Varices Without Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacology, Hydroxocobalamin is the natural cobalamin (Vitamin B12) form that is preferred for intramuscular injection because it lacks the cyanide moiety found in cyanocobalamin and has a longer serum half-life. It is converted intracellularly into two active co-enzyme forms: methylcobalamin (supporting the homocysteine-to-methionine pathway via methionine synthase) and adenosylcobalamin (supporting the methylmalonyl-CoA-to-succinyl-CoA conversion via methylmalonyl-CoA mutase). These pathways underpin DNA synthesis, myelin sheath formation, and red blood cell maturation.

The proposed link to oesophageal varices is mechanistically very weak. The TxGNN knowledge graph likely captured this connection via a co-morbidity pathway: patients with chronic liver disease — the primary cause of portal hypertension and oesophageal varices — frequently have disrupted B12 metabolism, particularly those with alcoholic liver disease. However, a metabolic co-morbidity association is fundamentally different from a therapeutic mechanism. Hydroxocobalamin has no known ability to reduce portal venous pressure, promote variceal regression, or prevent variceal haemorrhage.

A further concern about prediction quality is that TxGNN assigned an identical score (0.9923) to both *esophageal varices without bleeding* and *esophageal varices with bleeding* — two clinically distinct presentations requiring very different management. This suggests the model cannot distinguish between these subtypes, which significantly limits the specificity and reliability of this prediction. Standard of care for oesophageal varices involves vasoactive agents (terlipressin, octreotide), non-selective beta-blockers, and endoscopic band ligation — none of which involve vitamin supplementation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Hydroxocobalamin in Esophageal Varices Without Bleeding.

---

## Literature Evidence

Currently no related literature available for Hydroxocobalamin in Esophageal Varices Without Bleeding.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> As Hydroxocobalamin is not currently listed on the ARTG, clinicians requiring safety information should consult international product information (UK MHRA, European EMA, or WHO monograph) or the DrugBank entry DB00200.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or mechanistic evidence supporting Hydroxocobalamin as a treatment for oesophageal varices. The TxGNN prediction reflects a knowledge graph co-morbidity association (chronic liver disease ↔ B12 metabolic disruption) rather than a pharmacologically actionable repurposing opportunity, and the model's inability to differentiate bleeding from non-bleeding variceal subtypes further undermines confidence in this signal.

**To proceed, the following is needed:**

- Preclinical data demonstrating a plausible mechanism by which B12 repletion reduces portal hypertension or variceal progression
- Clinical literature linking Hydroxocobalamin supplementation to variceal outcomes in cirrhotic populations
- Formal mechanism of action (MOA) data retrieval from DrugBank (currently unavailable — Data Gap DG002)
- TGA ARTG registration assessment or Special Access Scheme (SAS) Category B pathway evaluation for use in Australia
- Review of TGA-approved product information for safety, contraindications, and key warnings (Data Gap DG001)

---

> **⚠️ Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predictions should be interpreted in conjunction with TGA-approved clinical guidance and qualified specialist review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

