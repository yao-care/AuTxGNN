---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 142
evidence_level: L5
indication_count: 5
monitor_inn: "Ceftriaxone"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-17
description: "Ceftriaxone: predicted new indication polyclonal hyperviscosity syndrome (evidence level L5). In Australia: 11 PBS items (11 currently listed)"
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ceftriaxone: Third-generation cephalosporin (beta-lactam antibiotic) → polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Ceftriaxone is an injectable beta-lactam antibiotic that acts on bacterial cell wall synthesis.
The TxGNN model predicts it may be relevant to **polyclonal hyperviscosity syndrome**, but there are **no clinical trials and no publications** supporting this prediction, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (11 of 11 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for ceftriaxone: "Ceftriaxone is an antibacterial drug. […] Ceftriaxone is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftriaxone has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467), label version 2022-01-13; accessed 2026-11-19.) Ceftriaxone is known to be a beta-lactam antibiotic that inhibits bacterial cell wall synthesis.

Polyclonal hyperviscosity syndrome is a haematological/immunological condition with no bacterial target, so no mechanistic link to ceftriaxone has been identified. The high prediction score is a model output only. It should not be read as a sign of clinical benefit, and it has no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11169W | Ceftriaxone Viatris | Powder for injection 2 g (as sodium) | Indication text not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: The interaction search returned 100 records. The main ones flagged as Major are:
  - Calcium chloride
  - Calcium glucoheptonate
  - Calcium gluconate

  Moderate interactions include kanamycin, neomycin, streptomycin and picosulfuric acid.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no plausible mechanism, since the condition has no bacterial target. Evidence is at the model-prediction level only (L5).

**To proceed, the following is needed:**
- Any study that directly examines ceftriaxone in polyclonal hyperviscosity syndrome
- A plausible mechanistic rationale
- Mechanism of action data and warnings and contraindications from the TGA Product Information

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

