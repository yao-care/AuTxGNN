---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 182
evidence_level: L5
indication_count: 3
monitor_inn: "Codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-11-17
description: "Codeine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Codeine
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

## Codeine: opioid analgesic and antitussive → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid medicine marketed in Australia as a single-ingredient tablet. The TxGNN model predicts it may be relevant to **nasal cavity disease**, but the data compiled for this report contain **no clinical trials** and only **1 publication**, which is a case report describing a drug-related complication rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (12 of 12 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for codeine in the data compiled for this report. Codeine is a well-known opioid, and the mechanistic link to nasal cavity disease cannot be established from the available information.

The only publication is a case report of a rhinolith (a stone in the nose) that formed around a hardened mixture of codeine and opium in an impacted foreign body. This describes a complication linked to the drug, not a therapeutic effect. The high TxGNN score most likely reflects the model's pattern-based proximity to related upper-airway conditions rather than a plausible new mechanism. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man with long-standing nasal obstruction and foul-smelling discharge had a rhinolith formed around an impacted foreign body, a hardened codeine and opium mixture. This is a complication, not a treatment effect. |

This publication does not study codeine as a treatment for nasal cavity disease, so it does not provide direct supporting evidence for the predicted use.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12054K | Aspen Pharmacare Australia Pty Ltd | Tablet containing codeine phosphate hemihydrate 30 mg | Not recorded in the local data |
| 191C | Not recorded | Not recorded | Not recorded in the local data |

The two items in the table are single-ingredient and currently listed. The data compiled for this report contain 12 current PBS items in all: 6 single-ingredient codeine items and 6 combinations (paracetamol with codeine, aspirin with codeine).

<!-- review:begin au-lic-20261117-codeine-1 -->

> **Review correction (2026-11-17)**: Originally stated: "Both licences are single-ingredient and currently valid." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-codeine-1 -->

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. Major-level interactions in the listed sample include **alvimopan** and **bupropion**. Moderate-level interactions include atropine, cimetidine, dexamethasone, dronabinol, eluxadoline, fenfluramine, granisetron, loperamide and several anticholinergic agents (clidinium, dicyclomine, glycopyrronium, hyoscyamine).

For warnings, contraindications and other safety information, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only supporting publication reports a complication involving codeine, not a benefit. There are no clinical trials. The high model score is therefore not backed by any direct study of the predicted disease, and the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether any plausible therapeutic link to nasal cavity disease exists
- Studies that directly evaluate codeine for nasal cavity disease, if a clinical rationale can be identified
- Review of the TGA Product Information for warnings and contraindications
- Confirmation of the approved indication text for the Australian licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

