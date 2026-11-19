---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 9
monitor_inn: "Acarbose"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-17
description: "Acarbose: predicted new indication focal stiff limb syndrome (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Acarbose: alpha-glucosidase inhibitor → focal stiff limb syndrome
{: .text-alpha }

## One-Sentence Summary

Acarbose is an oral alpha-glucosidase inhibitor that acts locally in the gut to delay carbohydrate absorption. The TxGNN model predicts it may be relevant to **focal stiff limb syndrome**, with a score of 0.9965. There are **no clinical trials and no publications** that study this disease, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for acarbose: "In contrast to sulfonylureas, Acarbose Tablets do not enhance insulin secretion. The antihyperglycemic action of acarbose results from a competitive, reversible inhibition of pancreatic alpha-amylase and membrane-bound intestinal alpha-glucoside hydrolase enzymes." ([DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a), label version 2026-08-11; accessed 2026-11-19.) Acarbose is known as an alpha-glucosidase inhibitor that acts locally in the gut to delay carbohydrate absorption and blunt postprandial glucose rises.

Focal stiff limb syndrome is a neurological disorder within the stiff-person spectrum, linked to impaired GABAergic inhibition or autoimmune mechanisms. No mechanistic link to alpha-glucosidase inhibition has been identified. The only loose connection is that autoimmune conditions related to this spectrum can co-occur with diabetes, which does not support acarbose as a treatment.

The score is a model output only. It is not a clinical finding and should not be read as evidence of efficacy.

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
| ARTG 13869Y | GLYBOSAY | Tablet 100 mg | Not recorded in the local data |

---

## Safety Considerations

Detailed label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Drug Interactions**: The interaction query returned 100 entries. Examples at moderate level include acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, atazanavir, bedaquiline, bendroflumethiazide, benzphetamine, benzthiazide and betamethasone. Minor-level examples include albiglutide, alclometasone (topical), lipoic acid, amcinonide and anisindione.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. No trials or publications study focal stiff limb syndrome, and no plausible mechanistic link to acarbose has been identified.

**To proceed, the following is needed:**
- Any clinical or preclinical study directly addressing focal stiff limb syndrome
- A plausible, documented mechanism linking alpha-glucosidase inhibition to the disease
- Mechanism of action data and TGA Product Information warnings and contraindications for review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

