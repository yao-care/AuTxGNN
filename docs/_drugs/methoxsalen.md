---
layout: default
title: Methoxsalen
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Methoxsalen: predicted new indication Localized pagetoid reticulosis (evidence level L5). Approved use: Primary cutaneous T-cell lymphoma"
monitor_inn: "Methoxsalen"
predicted_indications: ["localized pagetoid reticulosis", "neoplasm of mature B-cells", "small intestinal Burkitt lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "vulvar inverted follicular keratosis"]
---

# Methoxsalen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Methoxsalen: From Cutaneous T-Cell Lymphoma and Vitiligo to Localized Pagetoid Reticulosis
{: .text-alpha }

## One-Sentence Summary

Methoxsalen is a photosensitising agent originally used for primary cutaneous T-cell lymphoma and vitiligo.
The TxGNN model predicts it may be effective for **localized pagetoid reticulosis** (an indolent variant of mycosis fungoides), but there are currently **0 clinical trials** and **0 publications** specific to this disease. The prediction is supported by model scoring and biological plausibility only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary cutaneous T-cell lymphoma; vitiligo (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of methoxsalen as: DNA inhibitor ([ChEMBL CHEMBL416 (methoxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL416), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, methoxsalen is a psoralen. It is used with UVA light (PUVA) and in extracorporeal photopheresis. It intercalates into DNA and, once activated by UVA, forms crosslinks that induce apoptosis in malignant T cells.

Localized pagetoid reticulosis (Woringer-Kolopp disease) is an indolent variant of mycosis fungoides, which is a primary cutaneous T-cell lymphoma. Because methoxsalen is already used in cutaneous T-cell lymphoma, the biological rationale is plausible. However, the high TxGNN score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not independent evidence of efficacy.

The other top predictions are mostly B-cell lymphomas, deep-seated extranodal lymphomas and a benign skin lesion. They have no plausible mechanistic link to UVA photochemotherapy and are not discussed further.

## Clinical Trial Evidence

Currently no related clinical trials registered for localized pagetoid reticulosis. No trials were found for the other top-ranked predictions either.

## Literature Evidence

No literature specific to localized pagetoid reticulosis is available. The only supporting publication relates to the rank 2 prediction, indolent primary cutaneous T-cell lymphoma, and is indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) | 2006 | Review | Ontario Health Technology Assessment Series | Evidence-based analysis of the effectiveness, safety and cost-effectiveness of extracorporeal photopheresis for refractory erythrodermic CTCL and refractory chronic graft-versus-host disease |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 12154Q | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12156T | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12162D | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12173Q | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12839R | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12854M | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12855N | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |
| 12876Q | Uvadex | Methoxsalen | Solution for blood fraction 20 microgram per mL, 10 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The only registered route is "Other" (a solution for blood fraction, consistent with extracorporeal use). It has not been assessed whether this is suitable for the predicted indication.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Photosensitising agent (psoralen) activated by UVA. Not a conventional cytotoxic, but the effect on malignant T cells is DNA crosslinking and apoptosis. |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the Product Information (PI) warnings and precautions |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

- **Contraindications suggested by the knowledge graph** (these come from the knowledge graph, not from label text, and need verification against the PI):
  - Photosensitivity conditions: photosensitivity disease, photoparoxysmal response
  - Porphyrias: including porphyria cutanea tarda, variegate porphyria and erythropoietic protoporphyria
  - Skin cancers: melanoma, basal cell carcinoma, squamous cell carcinoma and other carcinomas
  - Other: liver disease, gallbladder disease, systemic lupus erythematosus, xeroderma pigmentosum, albinism, Waardenburg syndrome, piebaldism, Griscelli syndrome and peroxisome biogenesis disorder
- **Drug Interactions**: 100 interactions were found, and the 20 retrieved are all Moderate severity. They include:
  - Tetracyclines: doxycycline, tetracycline, minocycline
  - Sulfonylureas: chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide
  - Others: levofloxacin, sulfasalazine, promethazine, ibuprofen, flurbiprofen, alosetron

  Many of these are photosensitising or hypoglycaemic agents. Concurrent use with a psoralen needs review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for localized pagetoid reticulosis rests on a model score and a plausible link to the existing CTCL indication. There are no trials or publications specific to this disease (Evidence Level L5). Safety data from the label are also missing. The rank 2 prediction (indolent CTCL) is better framed as a research question within the existing CTCL indication, with only indirect evidence.

**To proceed, the following is needed:**
- Case series, registry data or literature on PUVA or photopheresis in localized pagetoid reticulosis
- Mechanism of action data (for example from DrugBank)
- The TGA Product Information, including indications, warnings, contraindications and the approved route and use of Uvadex
- A check of the knowledge-graph contraindications (especially skin cancer history and photosensitivity) against the PI
- Confirmation of whether the existing Uvadex use already covers this disease within the CTCL indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL416 (methoxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL416) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

