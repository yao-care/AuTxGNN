---
layout: default
title: Cabozantinib
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Cabozantinib: predicted new indication Liposarcoma (evidence level L5). Approved use: Renal cell carcinoma (including clear cell) and medullary thyroid car…"
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
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

## Cabozantinib: From Renal Cell Carcinoma to Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Cabozantinib is an oral multikinase inhibitor originally used for renal cell carcinoma (RCC) and medullary thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with a very high score.
Evidence is still early: **1 clinical trial** (Phase 2, soft tissue sarcoma generally, not liposarcoma-specific) and **1 publication** (Phase 1) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (including clear cell) and medullary thyroid carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 (early-phase clinical data only, none specific to liposarcoma) |
| Australia Market Status | Listed on the PBS Schedule (18 of 18 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 18 (valid: 18) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cabozantinib: "In vitro biochemical and/or cellular assays have shown that cabozantinib inhibits the tyrosine kinase activity of MET, VEGFR-1, -2 and -3, AXL, RET, ROS1, TYRO3, MER, KIT, TRKB, FLT-3, and TIE-2. These receptor tyrosine kinases are involved in both normal cellular function and pathologic processes such as oncogenesis, metastasis, tumor angiogenesis, drug resistance, and maintenance of the tumor microenvironment." ([DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5), label version 2025-10-19; accessed 2026-11-19.) The data compiled indicate that cabozantinib inhibits the kinases MET, VEGFR2 and AXL. These pathways are implicated in tumour blood vessel growth and tumour progression in soft tissue sarcoma.

Cabozantinib's efficacy in RCC is established, and RCC is also driven by angiogenesis and MET/AXL signalling. Liposarcoma is a soft tissue sarcoma, so the same pathways could plausibly matter. A Phase 1 study has also reported that cabozantinib shows activity in several soft tissue sarcoma subtypes.

The evidence is early-phase and covers soft tissue sarcoma broadly rather than liposarcoma specifically. The mechanistic link is therefore only partly applicable.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomised comparison of ipilimumab plus nivolumab with or without cabozantinib in advanced soft tissue sarcoma. Likely includes liposarcoma subtypes, but is not liposarcoma-specific. No results yet (expected completion May 2028). |

No ANZCTR trials were identified in the data compiled.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | Am J Clin Oncol | Safety of neoadjuvant cabozantinib with concurrent radiation therapy in extremity soft tissue sarcoma. Cabozantinib shows activity in multiple soft tissue sarcoma subtypes, but combining it with radiation has been limited by concern about fistula or perforation. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11360X | Cabometyx | Tablet 60 mg (oral) | Not stated in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically includes full blood count, liver and renal function, and electrolytes |
| Handling Protection | Please refer to the PI and local institutional policy on handling of oral anticancer agents |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. The following are classed as **Major**:
  - Acetylsalicylic acid
  - Cisapride
  - Clarithromycin
  - Dolasetron
  - Granisetron
  - Levofloxacin

  Moderate interactions include loperamide, aprepitant, dexamethasone, bisacodyl and several laxatives. Fidaxomicin is classed as Minor. Only 20 of the 100 interactions were available for this report, so a full interaction review is needed before any use.
- **Combination with radiation**: the Phase 1 sarcoma study highlights concern about fistula or perforation when cabozantinib is given with radiation therapy.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high and the mechanism is plausible. However, the supporting evidence is limited to one ongoing Phase 2 trial in soft tissue sarcoma generally and one Phase 1 study, with no liposarcoma-specific efficacy data. This is best treated as a research question rather than a candidate for clinical adoption.

**To proceed, the following is needed:**
- Results from the Phase 2 soft tissue sarcoma trial (NCT05836571), with liposarcoma-specific subgroup data
- Detailed mechanism of action data (MOA)
- Warnings and contraindications from the TGA Product Information, to allow safety screening
- A full review of the drug interaction list
- Confirmation of the approved indication wording for the ARTG entry

**Note:** The renal cell carcinoma predictions have stronger evidence than liposarcoma. For example, unclassified RCC is supported by several Phase 2 trials and published cohorts, and may merit separate evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data from DrugBank is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

