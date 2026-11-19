---
layout: default
title: Eculizumab
parent: Model Prediction Only (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Eculizumab: predicted new indication cyclic hematopoiesis (evidence level L5). Approved use: Paroxysmal nocturnal haemoglobinuria"
monitor_inn: "Eculizumab"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Eculizumab: From Paroxysmal Nocturnal Haemoglobinuria to Cyclic Hematopoiesis
{: .text-alpha }

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, originally used to treat paroxysmal nocturnal haemoglobinuria (PNH) and neuromyelitis optica.
The TxGNN model (deep learning) predicts it may be effective for **cyclic hematopoiesis**, but there are **no clinical trials** and **no disease-specific publications** supporting this prediction. It rests on the TxGNN model prediction alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal haemoglobinuria; neuromyelitis optica (the approved indication text for the ARTG entry is not available) |
| Predicted New Indication | Cyclic haematopoiesis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (12 of 12 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for eculizumab: "Eculizumab, the active ingredient in SOLIRIS, is a monoclonal antibody that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a and C5b and preventing the generation of the terminal complement complex C5b-9. SOLIRIS inhibits terminal complement-mediated intravascular hemolysis in PNH patients and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722), label version 2026-07-08; accessed 2026-11-19.) Based on known information, eculizumab is a humanised monoclonal antibody that targets complement protein C5 and blocks terminal complement activation. Its efficacy in PNH, where uncontrolled complement activation drives haemolysis, is established. In the publications compiled for this report, it is also described as effective in atypical haemolytic uraemic syndrome and used in myasthenia gravis.

The link to cyclic haematopoiesis (cyclic neutropenia) is weak. Cyclic neutropenia is typically caused by ELANE mutations affecting neutrophil precursors, and no established role for terminal complement (C5) inhibition has been identified. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are mostly congenital neutropenia conditions, and they share the same problem. Eculizumab also increases susceptibility to encapsulated bacteria, particularly meningococcal infection. This would compound infection risk in neutropenic or immunodeficient patients, so the benefit-risk balance looks unfavourable.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications address cyclic haematopoiesis directly. The data compiled for this report contain no literature for this indication.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10182X | Soliris | Solution concentrate for I.V. infusion, 300 mg in 30 mL | Not available in the data compiled for this report |

## Cytotoxicity

Not applicable. Eculizumab is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Drug Interactions**: Four interactions were identified, all classed as Minor. They involve human immunoglobulin G in its intravenous, subcutaneous, intramuscular and combined intravenous/subcutaneous forms.
- **Infection risk (from the predicted-indication analysis)**: Complement C5 inhibition increases susceptibility to encapsulated bacteria, including meningococcus. This is a particular concern in neutropenic or immunodeficient populations.

Warnings and contraindications from the product label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials and no disease-specific literature, and no plausible mechanism links C5 inhibition to cyclic haematopoiesis. The added infection risk in neutropenic patients makes the benefit-risk balance look unfavourable.

**To proceed, the following is needed:**
- Mechanistic evidence that terminal complement activation contributes to cyclic neutropenia
- Preclinical or early-phase clinical data in cyclic haematopoiesis
- The mechanism of action data for eculizumab (currently missing)
- The TGA Product Information, including warnings and contraindications, for safety screening
- A risk assessment of meningococcal and other encapsulated-bacteria infection in neutropenic patients, including vaccination and prophylaxis requirements
- The approved indication text for the Australian ARTG entry

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

