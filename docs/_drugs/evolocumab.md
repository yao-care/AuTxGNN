---
layout: default
title: Evolocumab
parent: Model Prediction Only (L5)
nav_order: 281
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-17
monitor_inn: "Evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
description: "Evolocumab: predicted new indication Symptomatic form of hemophilia in female carriers (evidence level L5). In Australia: 6 PBS items (6 currently listed)"
---

# Evolocumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Evolocumab: Symptomatic form of hemophilia in female carriers
{: .text-alpha }

## One-Sentence Summary

Evolocumab is a PCSK9-inhibiting monoclonal antibody, originally used to lower LDL cholesterol in homozygous familial hypercholesterolaemia and related dyslipidaemias.
The TxGNN model predicts it may be effective for **symptomatic haemophilia in female carriers**, but **no clinical trials and no publications** currently support this direction.
This is a prediction from the TxGNN model (deep learning) only and is not backed by a plausible biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for evolocumab: "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), label version 2026-10-12; accessed 2026-11-19.) Based on known information, evolocumab is a monoclonal antibody that binds PCSK9. This increases LDL receptor availability on liver cells and lowers circulating LDL cholesterol.

The predicted new indication is not closely related to the original indications. Haemophilia in female carriers arises from deficient factor VIII or factor IX due to X-linked variants. It is unrelated to the PCSK9/LDL receptor pathway. No plausible mechanistic link has been identified.

The high TxGNN score (0.9982) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis-generating signal only.

Other top-ranked predictions show the same pattern. These include familial apolipoprotein C-II deficiency, thrombocytopenic purpura, factor XI deficiency, haemophilia A with vascular abnormality, haemorrhagic disease of the newborn, and inherited thrombophilia. All are L5 with no supporting studies. Several are non-specific ontology categories (for example "disease of catalytic activity"), and no actionable hypothesis can be formed for them. Familial apolipoprotein C-II deficiency has only indirect plausibility, because it is a lipid disorder, but it is driven by a defect upstream of the LDL receptor pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10958R | Repatha | Injection 140 mg in 1 mL single use pre-filled pen | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacological target entry, not a drug-drug interaction. It lists evolocumab binding to its target, proprotein convertase subtilisin/kexin type 9 (PCSK9). No clinically significant drug-drug interactions were identified in the data compiled.

Please refer to the TGA-approved Product Information (PI) for warnings, contraindications and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no clinical trials or publications, and evolocumab's PCSK9 mechanism has no plausible link to a clotting factor deficiency in female carriers. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- A defensible mechanistic hypothesis linking PCSK9 inhibition to the coagulation pathway, supported by preclinical data
- Published clinical or preclinical evidence in haemophilia carriers
- Detailed mechanism of action data
- Safety information from the TGA-approved Product Information (warnings and contraindications), which was not available for this report
- Confirmation of the approved indication wording for the ARTG entry
- Route-compatibility assessment (current product is an injectable pre-filled pen)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

