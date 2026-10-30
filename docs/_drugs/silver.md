---
layout: default
title: Silver
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Silver: predicted new indication Bone Paget disease (evidence level L5). Approved use: Not recorded in the data compiled for this report (marketed as silver…"
monitor_inn: "silver"
predicted_indications: ["bone Paget disease"]
---

# Silver
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

## Silver: From Wound Care Dressings to bone Paget disease
{: .text-alpha }

## One-Sentence Summary

Silver is the active antimicrobial component in several silver-impregnated wound dressings marketed in Australia. The TxGNN model predicts it may be relevant to **bone Paget disease**, but **0 clinical trials** and **no supportive publications** back this prediction. The five retrieved papers mention silver only as a laboratory staining reagent, not as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report (marketed as silver-containing wound dressings) |
| Predicted New Indication | Bone Paget disease |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Silver is used in Australia as a component of topical wound dressings, but no approved indication text is recorded for these products in the data compiled for this report.

No credible mechanistic link between silver and Paget disease of bone was identified. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It most likely reflects co-occurrence of "silver" with Paget disease literature through histological staining methods (for example, silver staining of nucleolar organizer regions in osteoclasts). This is a methodological artefact rather than a therapeutic signal.

There is also no pharmacological basis to infer an osteoclast-modulating effect of silver. In addition, silver dressings are applied to the skin surface, whereas Paget disease of bone is a systemic skeletal disorder. Route compatibility has not been established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications evaluates silver as a treatment. All are laboratory or histology papers.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9836854](https://pubmed.ncbi.nlm.nih.gov/9836854/) | 1998 | Histopathology study | Bone | Silver-stained nucleolar organizer regions (AgNORs) were increased in osteoclast nuclei in Paget's disease. Silver is used as a stain, not a therapy. |
| [3163726](https://pubmed.ncbi.nlm.nih.gov/3163726/) | 1988 | Imaging/localisation study | J Nucl Med | Gallium-67 citrate localises in osteoclast nuclei in Paget's disease. Unrelated to silver pharmacology. |
| [9227338](https://pubmed.ncbi.nlm.nih.gov/9227338/) | 1997 | Laboratory methods | J Pathol | Vitamin D receptor mRNA quantification in tissue sections. Unrelated to silver as a therapeutic agent. |
| [2420233](https://pubmed.ncbi.nlm.nih.gov/2420233/) | 1985 | Histological methods | Anat Anz | Silver impregnation method for bone tissue. |
| [4111887](https://pubmed.ncbi.nlm.nih.gov/4111887/) | 1972 | Histological methods | Stain Technol | Silver staining of bone before decalcification to measure osteoid. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12591Q | Atrauman Ag 499573 | Tulle dressings 10 cm x 10 cm, 10 | Not recorded |
| ARTG 10097K | Aquacel Ag 403708 | Dressing 10 cm x 10 cm | Not recorded |
| ARTG 4252T | Allevyn Ag Adhesive 66800073 | Dressings, adhesive, 7.5 cm x 7.5 cm, 10 | Not recorded |
| ARTG 2439J | Mepilex Ag | Dressings 10 cm x 10 cm, 5 | Not recorded |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). The retrieved literature uses silver only as a staining reagent, and there are no registered clinical trials. A topical wound dressing is also not a plausible route for treating a systemic bone disease.

**To proceed, the following is needed:**
- Evidence of a genuine pharmacological link between silver and osteoclast biology or Paget disease (preclinical or mechanistic studies)
- Mechanism of action data for silver
- Original approved indication text and warnings/contraindications from the Product Information for the ARTG-listed products
- Assessment of route and formulation feasibility, since the marketed products are topical dressings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

