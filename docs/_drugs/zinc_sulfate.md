---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 792
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-04
monitor_inn: "Zinc sulfate"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Zinc Sulfate: Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is a zinc salt used as a mineral supplement, and the approved indication is not recorded in the local data. The TxGNN model predicts it may be useful for **pharyngitis**, but the evidence is weak: **1 clinical trial** on a related condition (postoperative sore throat) and **1 randomised trial in pharyngitis itself that found no benefit**. The evidence level is **L5**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Zinc is known to have local antiviral and mucosal-protective effects, and zinc lozenges release zinc ions directly in the oropharynx. Zinc may also support mucosal repair and taste or sensory recovery.

These mechanisms make a role in throat conditions plausible, but the link is indirect. The available studies address postoperative sore throat after intubation and radiation-induced mucosal injury, not infectious pharyngitis. The one randomised trial that studied pharyngitis directly (in radiotherapy patients) did not show a benefit, so the high model score is not supported by clinical findings.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomised, double-blind, placebo-controlled trial of preoperative zinc lozenges for postoperative sore throat after intubation. This is a related condition, not pharyngitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | Journal of the Medical Association of Thailand | Zinc sulfate supplementation for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. No benefit was found for radiation-induced pharyngitis. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/Observational | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Recovery from long-lasting post-tonsillectomy taste disturbance; zinc deficiency discussed as a possible factor. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 600N | Not available | Not available | Not available |

At least one valid single-ingredient licence is recorded, and no licences are cancelled.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions**: A total of 100 interactions were found in the interaction screen. Most of those listed are minor (for example, with corticosteroids and several biologic immunosuppressants). Moderate interactions include:
- Alendronic acid
- Risedronic acid
- Ibandronate
- Tetracycline
- Baloxavir marboxil

These moderate interactions are likely to involve reduced absorption when taken together, so dosing should be separated. Check this against the PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only randomised trial in pharyngitis itself found no benefit, and the other trial studied postoperative sore throat, a related condition. All direct evidence is therefore negative or absent, and the evidence level is L5. The high TxGNN score is not supported by clinical data.

**To proceed, the following is needed:**
- A controlled trial in infectious pharyngitis showing a clinical benefit
- Mechanism of action data
- Product Information warnings and contraindications for the Australian product, to allow safety screening
- Product, dosage form and indication details for the Australian licence

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

