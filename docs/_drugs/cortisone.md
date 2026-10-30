---
layout: default
title: Cortisone
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Cortisone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L4). Approved use: Not available"
monitor_inn: "Cortisone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "adrenocortical insufficiency", "myelodysplastic syndrome", "lymphosarcoma", "candidiasis", "Crohn's colitis", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5"]
---

# Cortisone
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

## Cortisone: From a Corticosteroid with No Recorded Indication to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Cortisone is an oral corticosteroid (a prodrug converted to cortisol in the body), marketed in Australia as cortisone acetate 5 mg tablets.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, but support is very thin: **1 clinical trial** that is not relevant (it studies diffuse large B-cell lymphoma) and **5 publications**, all case reports or reviews from 1951 to 1964.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the ARTG entry has no approved indication text) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cortisone is a prodrug converted to cortisol, which acts on the glucocorticoid receptor. Corticosteroids have lympholytic activity: they can trigger apoptosis (programmed cell death) in lymphoid cells. This gives a plausible link to T-cell lymphoma.

The supporting evidence is weak. The literature consists only of 1950s and 1960s case reports on mycosis fungoides (the most common cutaneous T-cell lymphoma). One of these describes a harmful outcome, a terminal ulceronecrotic process possibly linked to treatment. The single linked trial does not study cortisone or cutaneous T-cell lymphoma, and prednisone appears in it only as part of a chemotherapy regimen.

Other predictions for cortisone are stronger. The most established is adrenocortical insufficiency (rank 2), which is a rediscovery of a known historical use, not true repurposing. For lymphosarcoma (rank 4), steroid-containing regimens are standard in lymphoma, but they use prednisone or dexamethasone rather than cortisone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Active, not recruiting | 422 | R-miniCHOP with or without oral azacitidine in patients aged 75 or older with diffuse large B-cell lymphoma. This is a B-cell disease, and cortisone is not tested (prednisone is only a regimen component). No direct relevance. |

No ANZCTR trials were identified in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Review | J Med Chir Prat | Overview of mycosis fungoides (no abstract available) |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case report | Svenska Lakartidningen | Combined ACTH and cortisone therapy in impetigo herpetiformis, mycosis fungoides and erythrodermic psoriasis |
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case report | Dermatologica | Effects of cortisone in two cases of mycosis fungoides |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case report | Lyon Medical | Two cases treated with delta-cortisone; terminal ulceronecrotic process probably linked to the medication |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case report | Bull Soc Fr Dermatol Syphiligr | Two cases of bronchial epithelioma in patients with mycosis fungoides treated with cortisone |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1246N | Cortate | Tablet containing cortisone acetate 5 mg (oral) | Not stated in the data compiled |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for this indication is limited to a plausible class-level mechanism and a handful of 1950s to 1960s case reports. The single linked trial is unrelated. Modern evidence for corticosteroids in lymphoma concerns prednisone or dexamethasone within combination regimens, not cortisone alone.

**To proceed, the following is needed:**
- The approved indication and Product Information for Cortate, including warnings and contraindications
- Mechanism of action data for cortisone
- Modern clinical evidence, such as controlled studies of corticosteroids in cutaneous T-cell lymphoma, and a clinical view on whether cortisone offers any advantage over prednisone or dexamethasone
- A review of other predictions. Adrenocortical insufficiency has the strongest evidence (L1, Proceed with Guardrails), but its trials test hydrocortisone, not cortisone, and hydrocortisone is now preferred. The candidiasis prediction is likely a model artefact, because cortisone is used to induce candidiasis in animal models.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

