---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 335
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Glatiramer: predicted new indication Hemoglobinopathy (evidence level L5). Approved use: Not stated in the data compiled for this report (literature describes…"
monitor_inn: "Glatiramer"
predicted_indications: ["hemoglobinopathy"]
---

# Glatiramer
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glatiramer: From Multiple Sclerosis to Hemoglobinopathy
{: .text-alpha }

## One-Sentence Summary

Glatiramer (glatiramer acetate) is an immunomodulator marketed in Australia as Copaxone. The data compiled for this report do not list an approved indication text for it, but the literature retrieved describes its use in multiple sclerosis (MS). The TxGNN model predicts it may be effective for **hemoglobinopathy**, but there are **0 clinical trials** and only **1 publication** (a case report-type commentary that is not evidence of efficacy), so this prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (literature describes use in multiple sclerosis) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for glatiramer: "The mechanism(s) by which glatiramer acetate exerts its effects in patients with MS are not fully understood. However, glatiramer acetate is thought to act by modifying immune processes that are believed to be responsible for the pathogenesis of MS." ([DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716), label version 2026-10-26; accessed 2026-11-19.) Based on general knowledge, glatiramer is an immunomodulator used in MS that shifts T-cell responses toward Th2 and regulatory phenotypes.

Hemoglobinopathies are primarily genetic disorders of hemoglobin structure or synthesis. Immunomodulation does not address the underlying defect, so **no credible mechanistic link has been identified**. The high TxGNN score should be treated as a computational prediction only.

The single publication retrieved (PMID 28372806) is a case of multiple immune disorders after natalizumab discontinuation in a patient with MS who also had beta thalassemia. It reflects co-occurrence of conditions, not therapeutic benefit of glatiramer.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Review/Commentary | Revue neurologique | Case of multiple immune disorders after natalizumab discontinuation in a woman with MS and a history of beta thalassemia; does not assess glatiramer for hemoglobinopathy |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 10416F | Copaxone | glatiramer acetate | Injection containing glatiramer acetate 40 mg in 1 mL single dose pre-filled syringe | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: One interaction was identified. **Natalizumab** is rated **Major** (source: DDInter).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no clinical trials, no literature showing efficacy, and no plausible mechanism linking glatiramer's immunomodulation to correcting hemoglobin structure or synthesis defects. The evidence level is L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a credible mechanistic rationale for hemoglobinopathy
- Preclinical or other supporting studies in relevant disease models
- The approved indication text and full TGA Product Information (warnings and contraindications) for safety screening
- Review of the Major interaction with natalizumab and any co-prescribing implications
- Confirmation of route and formulation suitability for the proposed indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

