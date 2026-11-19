---
layout: default
title: Mepolizumab
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-17
monitor_inn: "Mepolizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). In Australia: 12 PBS items (12 currently listed)"
---

# Mepolizumab
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

## Mepolizumab: Thrombocytopenia due to immune destruction
{: .text-alpha }

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody that depletes eosinophils. The TxGNN model (deep learning) predicts thrombocytopenia due to immune destruction as a new indication, with a score of 0.9966; this score may reflect similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but the current support is only **1 case report** and **no registered clinical trials**, so this remains a computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (12 of 12 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mepolizumab: "Mepolizumab is an IL-5 antagonist (IgG1 kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Mepolizumab binds to IL-5 with a dissociation constant of 100 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil cell surface." ([DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea), label version 2025-08-06; accessed 2026-11-19.) Based on known information, mepolizumab is an anti-IL-5 monoclonal antibody that depletes eosinophils. Its role in eosinophil-driven disease is established, and mechanistically it might be applicable to conditions in which eosinophil-driven immune dysregulation contributes to disease.

The link to immune thrombocytopenia is weak. The only supporting publication is a case-level report in which mepolizumab, together with concomitant therapy, resolved a steroid-resistant hypereosinophilic immune diathesis with a mixed thrombotic microangiopathy. Any benefit on platelet counts would therefore be indirect, via control of eosinophil-driven immune dysregulation.

There is no evidence that IL-5 blockade acts on the core mechanisms of immune thrombocytopenia (autoantibody-mediated platelet clearance and impaired platelet production). The very high TxGNN score is a computational prediction only and should not be read as clinical support.

Other top-ranked predictions (primary release disorder of platelets, pseudo-von Willebrand disease, autoimmune thrombocytopenia, Glanzmann thrombasthenia, Evans syndrome, neonatal thrombocytopenia, autosomal thrombocytopenia with normal platelets, filariasis and mixed-type autoimmune haemolytic anaemia) have no clinical trials. Apart from a review of hypereosinophilic syndrome linked to the second-ranked prediction, they have no supporting literature either. Several of them (for example Glanzmann thrombasthenia and pseudo-von Willebrand disease) have no plausible link to IL-5 biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells Mol Dis | Mepolizumab with concomitant therapy resolved a steroid-resistant hypereosinophilic immune diathesis and was associated with improvement of a mixed thrombotic microangiopathy (atypical haemolytic uraemic syndrome context) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12007Y | Nucala | Injection 100 mg in 1 mL single dose pre-filled pen | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interactions were identified in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and a single case report in a different clinical context (hypereosinophilic syndrome with thrombotic microangiopathy). There are no trials, and there is no plausible mechanism linking IL-5 blockade to immune platelet destruction.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to support a mechanistic-link analysis
- Warnings and contraindications from the TGA-approved Product Information, as safety screening cannot proceed without them
- Approved indication text for the ARTG entry
- Mechanistic or preclinical evidence that IL-5 blockade affects platelet destruction in immune thrombocytopenia
- A systematic literature search for further case series or studies in immune thrombocytopenia, particularly cases with coexisting eosinophilia

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

