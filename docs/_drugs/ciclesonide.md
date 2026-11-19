---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 5
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
last_modified_at: 2026-11-17
description: "Ciclesonide: predicted new indication atopic eczema (evidence level L5). In Australia: 4 PBS items (4 currently listed)"
---

# Ciclesonide
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

## Ciclesonide: inhaled corticosteroid prodrug → atopic eczema
{: .text-alpha }

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid prodrug that is activated to des-ciclesonide in the body. The TxGNN model predicts it may be effective for **atopic eczema**, but the data compiled for this report contain **no clinical trials and no publications** on this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atopic eczema |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ciclesonide: "Ciclesonide is a prodrug that is enzymatically hydrolyzed to a pharmacologically active metabolite, C21-desisobutyryl-ciclesonide (des-ciclesonide or RM1) following oral inhalation. Des-ciclesonide has anti-inflammatory activity with affinity for glucocorticoid receptors that is 120 times greater than the parent compound and 12 times greater than dexamethasone." ([DailyMed: Alvesco (ciclesonide) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6112fb-78ef-43cf-8ae3-36370eb45468), label version 2025-02-28; accessed 2026-11-19.) Ciclesonide is an inhaled corticosteroid prodrug activated by esterases to des-ciclesonide, which acts through the glucocorticoid receptor.

Glucocorticoid receptor-mediated anti-inflammatory activity is plausibly relevant to atopic eczema, for which topical corticosteroids are standard care. This is a mechanistic argument only. The formulation, activation in skin and local safety of ciclesonide for this use are not established.

Other predictions in the data (for example, the closely related term "dermatitis, atopic") are likely redundant ontology entries for the same condition. They should be merged during review and are not treated here as separate findings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14312G | Alvesco 80 | Pressurised inhalation 80 micrograms per dose, 120 doses (CFC-free formulation) | Not recorded in the local data |

All four listed PBS items are inhaled formulations. No topical presentation is recorded, so route compatibility with atopic eczema is unresolved.

<!-- review:begin au-lic-20261117-ciclesonide-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The only listed product is an inhaled formulation." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-ciclesonide-1 -->

## Safety Considerations

- **Drug Interactions**: 63 interactions were recorded. Examples include:
  - Major: cladribine.
  - Moderate: clarithromycin, miconazole, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, conivaptan, fostamatinib, inhaled rapid-acting insulin, topical abametapir.
  - Minor: formoterol, salbutamol, arformoterol.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9996), but there are no trials or publications on atopic eczema, so evidence is limited to model output (L5). Only an inhaled product is marketed in Australia, and skin delivery and local safety are not established.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of ciclesonide in atopic eczema or other eczematous skin disease
- Route and formulation feasibility assessment, since only an inhaled product is registered
- Full mechanism of action data
- Warnings and contraindications from the TGA Product Information
- Review of the major and moderate drug interactions for any proposed population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Alvesco (ciclesonide) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6112fb-78ef-43cf-8ae3-36370eb45468) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

