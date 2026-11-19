---
layout: default
title: Selpercatinib
parent: Model Prediction Only (L5)
nav_order: 666
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
description: "Selpercatinib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Selpercatinib"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Selpercatinib: From an Unspecified Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor marketed in Australia as Retevmo. The data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **no registered clinical trials** and **no publications that directly address this prediction**. The prediction is model-based only and the direction of effect is uncertain.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (6 of 6 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for selpercatinib: "Selpercatinib is a kinase inhibitor. Selpercatinib inhibited wild-type RET and multiple mutated RET isoforms as well as VEGFR1 and VEGFR3 with IC 50 values ranging from 0.92 nM to 67.8 nM. In other enzyme assays, selpercatinib also inhibited FGFR 1, 2, and 3 at higher concentrations that were still clinically achievable." ([DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828), label version 2026-09-11; accessed 2026-11-19.) Selpercatinib is known to be a selective RET kinase inhibitor, and the literature retrieved relates to RET-driven cancers (RET fusion-positive non-small-cell lung cancer and medullary thyroid carcinoma). The original indication could not be confirmed from the Australian licence record.

No plausible RET-driven mechanism in pulmonary hypertension is established in the supplied data. The high TxGNN score reflects proximity in a knowledge network rather than demonstrated biology. Some multikinase inhibitors have been linked to pulmonary hypertension as an adverse effect, so the direction of effect is uncertain and could be harmful.

Other top-ranked predictions are also unsupported. These include migraine disorder and its subtypes, idiopathic pulmonary arterial hypertension, heritable pulmonary hypertension, and several rare skeletal or dermatological entries. Several look like TxGNN model (deep learning) artefacts. Kinase inhibitors such as imatinib have been explored in pulmonary arterial hypertension, but selective RET inhibitors have not.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications retrieved do not test selpercatinib in pulmonary hypertension. They are listed for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world pharmacovigilance study | Front Pharmacol | Compares adverse event profiles of pralsetinib and selpercatinib using FDA adverse event reports |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective cohort | Ther Adv Med Oncol | Real-world use of selpercatinib in RET fusion-positive NSCLC through an access program (SIREN) |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report | Cureus | Long-term management of metastatic medullary thyroid carcinoma with RET M918T mutation in MEN 2B, including targeted therapy |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14693H | Retevmo | Capsule 40 mg | Not stated in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs, including many rated Major. The main Major interactions listed include:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexlansoprazole
  - Magnesium oxide
  - Aprepitant
  - Clarithromycin
  - Dexamethasone
  
  Moderate interactions include hydrocortisone, triamcinolone, betamethasone, budesonide, pioglitazone, loperamide, bisacodyl, saxagliptin and polyethylene glycol with electrolytes.
- **Pulmonary vascular concern**: Safety signals for kinase inhibitors in the pulmonary vasculature warrant caution if pulmonary hypertension is pursued.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a network-based model score. There are no trials, no relevant literature, and no established mechanism, and a harmful effect on the pulmonary vasculature cannot be excluded.

**To proceed, the following is needed:**
- Confirmed approved indication and Product Information from the TGA record
- Mechanism of action data and a plausible biological link between RET inhibition and pulmonary hypertension
- Preclinical evidence in pulmonary hypertension models, including assessment of pulmonary safety signals
- Review of pharmacovigilance data for pulmonary hypertension events with selpercatinib
- Product Information warnings, contraindications and interaction management plan before any clinical evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

