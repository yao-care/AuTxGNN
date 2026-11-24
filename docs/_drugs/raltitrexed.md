---
layout: default
title: Raltitrexed
parent: Model Prediction Only (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Raltitrexed: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Colorectal cancer and malignant mesothelioma"
monitor_inn: "Raltitrexed"
predicted_indications: ["sclerosing cholangitis", "myelodysplastic syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "partial deletion of the long arm of chromosome 5"]
---

# Raltitrexed
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

## Raltitrexed: From Colorectal Cancer to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Raltitrexed is a thymidylate synthase inhibitor (antifolate) used as a cytotoxic chemotherapy, with the available pharmacology data describing its use in colorectal cancer and malignant mesothelioma.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, with a very high model score.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer and malignant mesothelioma (from pharmacology data; the Australian registration entry has no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of raltitrexed as: Thymidylate synthase inhibitor ([ChEMBL CHEMBL225071 (raltitrexed): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL225071), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, raltitrexed is a thymidylate synthase (TYMS) inhibitor. It blocks DNA synthesis in rapidly dividing cells, which underpins its use in colorectal cancer and malignant mesothelioma.

The link to sclerosing cholangitis is weak. This is an immune-mediated, fibroinflammatory biliary disease, and no plausible connection to thymidylate synthase inhibition has been established. The high TxGNN score (0.9997, model rank 823) is a model-based prediction only.

Cytotoxic antimetabolites can cause hepatotoxicity and transaminase elevation, which is a concern in a cholestatic liver disease.

### Other Predicted Indications (all L5, all Hold)

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Myelodysplastic syndrome | 0.9997 | Conceptual rationale exists, as antimetabolites such as azacitidine and decitabine are used in MDS. However, marked myelosuppression is a major liability in patients with existing cytopenias. |
| 3–7 | Sickle cell disease variants (Hb D, Hb E, beta-thalassaemia, Hb C, HPFH) | 0.9996 | Identical scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Raltitrexed has no demonstrated fetal haemoglobin-inducing activity, and myelosuppression could worsen anaemia. |
| 8 | Unclassified myelodysplastic syndrome | 0.9996 | Likely inherited from the parent MDS node. Same myelosuppression concern. |
| 9 | Refractory cytopenia of childhood | 0.9996 | A cytotoxic antifolate would be expected to worsen marrow suppression. Paediatric safety data are lacking. |
| 10 | Partial deletion of the long arm of chromosome 5 | 0.9995 | Related to del(5q) MDS, where lenalidomide acts via a distinct mechanism. No link to thymidylate synthase inhibition is established. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 4610P | Tomudex | Raltitrexed | Powder for I.V. infusion 2 mg in single use vial | Valid |
| 7256X | Tomudex | Raltitrexed | Powder for I.V. infusion 2 mg in single use vial | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate, thymidylate synthase inhibitor) |
| Myelosuppression Risk | High. Myelosuppression is a dose-limiting toxicity. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | FBC (with differential), liver function and renal function. Please also refer to the PI. |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Hepatotoxicity**: Cytotoxic antimetabolite toxicity, including transaminase elevation, is a concern in cholestatic liver disease such as sclerosing cholangitis.
- **Myelosuppression**: This is a major liability in patients with pre-existing cytopenias (MDS, refractory cytopenia of childhood) and in haemoglobinopathies, where antifolate-induced cytopenias could worsen anaemia.
- **Paediatric use**: Paediatric safety data for raltitrexed are lacking.
- **Drug Interactions**: The interaction query found only the pharmacological target, thymidylate synthase (TYMS). No drug-drug interactions were identified.

Warnings and contraindications from the label were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications are supported by model output only (L5), with no registered trials or publications. There is no plausible mechanistic link for the top prediction, sclerosing cholangitis. The known toxicity profile (hepatotoxicity, marked myelosuppression) is a significant concern in the predicted conditions.

**To proceed, the following is needed:**
- Product Information (PI) warnings and contraindications for the Australian-registered product (ARTG 4610P), which are required before any safety screening
- Detailed mechanism of action data, to assess any mechanistic link
- Preclinical or mechanistic studies to establish a biological rationale for the top-ranked indications
- A review of why the TxGNN model (deep learning) produced identical scores across the sickle cell variants, to check whether the signal only reflects similarities the model learned between related diseases rather than biological evidence
- A safety assessment specific to hepatic impairment, pre-existing cytopenias and paediatric populations

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL225071 (raltitrexed): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL225071) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

