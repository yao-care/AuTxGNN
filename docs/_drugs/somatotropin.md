---
layout: default
title: Somatotropin
parent: Model Prediction Only (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Somatotropin: predicted new indication Middle ear neuroendocrine tumour (evidence level L5). Approved use: Pituitary dwarfism, isolated congenital growth hormone deficiency…"
monitor_inn: "Somatotropin"
predicted_indications: ["middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "familial generalized lentiginosis", "rhabdoid tumor", "gastrocutaneous syndrome"]
---

# Somatotropin
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

# Somatotropin: From Growth Hormone Deficiency and Turner Syndrome to Middle Ear Neuroendocrine Tumour

## One-Sentence Summary

Somatotropin (recombinant human growth hormone) is originally used for growth failure conditions such as pituitary dwarfism, isolated congenital growth hormone deficiency, Turner syndrome, Prader-Willi syndrome and Noonan syndrome.
The TxGNN model ranks **middle ear neuroendocrine tumour** as its top prediction, but **no clinical trials and no publications** were found to support this direction. It is a model-only prediction, and it raises a theoretical safety concern rather than a therapeutic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pituitary dwarfism, isolated congenital growth hormone deficiency, Turner syndrome, monosomy X, gonadal dysgenesis, Prader-Willi syndrome, Noonan syndrome (from the knowledge graph; no approved indication text is listed for the Australian product) |
| Predicted New Indication | Middle ear neuroendocrine tumour |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, somatotropin acts through growth hormone (GH) and insulin-like growth factor 1 (IGF-1) signalling, which drives growth and can also promote cell proliferation.

For the top-ranked prediction, this proliferative signalling is a theoretical **safety concern** in a neuroendocrine tumour rather than a reason to expect benefit. No mechanistic link between somatotropin and this tumour can be verified from the data compiled for this report. The score appears to come only from the model's knowledge-graph proximity.

The same pattern applies to the other top-ranked oncology predictions (malignant cutaneous granular cell skin tumour, ectomesenchymoma, human herpesvirus 8-related tumour and rhabdoid tumour). All are model-only predictions with no supporting studies, and growth-promoting signalling is a theoretical risk in each.

Several lower-ranked predictions are more coherent, but they are mostly extensions of existing indications rather than true repurposing:

| Predicted Condition | Score | Evidence Level | Comment |
|------|------|------|------|
| Mixed gonadal dysgenesis | 95.58% | L4 | Related to the listed gonadal dysgenesis indication; shares the short-stature phenotype |
| Mosaic monosomy X | 95.06% | L4 | Variant of Turner syndrome / monosomy X, both already listed |
| Turner syndrome due to structural X chromosome anomalies | 95.02% | L4 | Subtype of Turner syndrome; likely already covered |

These three are labelled "Research Question" in the data. Their support is indirect only, and no trials or publications were supplied for them.

## Clinical Trial Evidence

Currently no related clinical trials registered for middle ear neuroendocrine tumour. No trials were found for any of the other top 10 predictions either.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10426R | Genotropin GoQuick | Powder for injection 12 mg (36 i.u.) with diluent in pre-filled pen (with preservative) | Not listed in the data compiled for this report |

The only available route is injectable.

## Safety Considerations

- **Theoretical oncologic concern**: GH/IGF-1 signalling can promote cell proliferation. This is a concern for any malignant or tumour-predisposing condition among the predictions, and for immunocompromised patients in the case of human herpesvirus 8-related tumours.
- **Drug Interactions**: The interaction query returned 100 records. The 20 reviewed were all rated Moderate. They include:
  - Glucose-lowering agents: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide, dulaglutide
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Proton pump inhibitors: omeprazole, rabeprazole
  - Others: clarithromycin, aprepitant, dolasetron, dronabinol

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests only on a model score, with no clinical trials, no literature and no verifiable mechanism. Growth-promoting signalling also makes this a theoretical safety concern in tumour settings. The Turner syndrome and gonadal dysgenesis variants are more plausible, but they are likely already covered by existing indications rather than new repurposing opportunities.

**To proceed, the following is needed:**
- Mechanism of action data for somatotropin
- Product Information warnings and contraindications for the Australian product (Genotropin GoQuick), including its approved indication text
- A literature and trial search for each predicted condition, especially any evidence on GH use in neuroendocrine tumours and in patients with tumour-predisposing syndromes
- For the Turner syndrome and gonadal dysgenesis variants, confirmation of whether the current label already covers them, which would make them label clarifications rather than repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

