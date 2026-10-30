---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Tipiracil: predicted new indication Cecum villous adenoma (evidence level L5). Approved use: Malignant colon neoplasm / colorectal cancer"
monitor_inn: "tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
---

# Tipiracil
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

## Tipiracil: From Colorectal Cancer to Cecum Villous Adenoma
{: .text-alpha }

## One-Sentence Summary

Tipiracil is a component of the trifluridine/tipiracil combination (TAS-102, Lonsurf), originally used to treat colorectal cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant colon neoplasm / colorectal cancer (the approved indication text is not listed in the ARTG data compiled for this report) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tipiracil is a thymidine phosphorylase inhibitor and one component of the trifluridine/tipiracil combination. Its efficacy in metastatic colorectal cancer has been established. Tipiracil does not kill tumour cells itself. It prevents the breakdown of trifluridine, a cytotoxic nucleoside analogue, so that the trifluridine reaches effective levels in the body.

A villous adenoma of the cecum is a premalignant colorectal lesion, so there is a loose anatomical and biological link to colorectal cancer. However, adenomas are normally managed by endoscopic resection rather than systemic chemotherapy. The high score comes from the TxGNN model (deep learning) and probably reflects similarities the model learned between related colon diseases, not biological evidence or a true therapeutic rationale. No clinical or literature evidence supports this prediction.

Other highly ranked predictions in this dataset include lipoma of colon, rectosigmoid junction neoplasm, cecum neuroendocrine tumour G1, colonic lymphangioma, cecal disease, colon leiomyoma, benign neoplasm of cecum, cavernous haemangioma of colon and colorectal gastrointestinal stromal tumour. All are graded L5, except cecal disease, which is graded L4 on indirect evidence only. Most are benign lesions for which a cytotoxic regimen would be inappropriate. The rectosigmoid junction neoplasm is effectively a sub-site of the already approved colorectal indication rather than a true repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for cecum villous adenoma.

For context, the nearest-ranked prediction with any literature, "cecal disease" (rank 6), retrieved only case reports on trifluridine/tipiracil in the already approved colorectal cancer setting. They do not show efficacy in a distinct cecal disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32655959](https://pubmed.ncbi.nlm.nih.gov/32655959/) | 2020 | Case report | Case Rep Oncol Med | Readministration of cancer drugs in a patient with chemorefractory metastatic colorectal cancer (cecal primary) |
| [30677817](https://pubmed.ncbi.nlm.nih.gov/30677817/) | 2018 | Case report | Dermatol Online J | Leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura after trifluridine/tipiracil in metastatic appendiceal cancer |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | Case report | Gan To Kagaku Ryoho | Complete pain response to CT-guided celiac plexus neurolysis after postoperative recurrence of colon cancer |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11507P | Lonsurf 15/6.14 | Tablet containing 15 mg trifluridine with 6.14 mg tipiracil (as hydrochloride) | Not specified in the data compiled for this report |

## Cytotoxicity

The combination product is an antineoplastic used for colorectal cancer. Tipiracil itself is not cytotoxic, but it is used with the cytotoxic nucleoside analogue trifluridine.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (trifluridine, a thymidine-based nucleoside analogue, with tipiracil as a thymidine phosphorylase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The literature compiled notes leukopenia and neutropenia as adverse effects of the combination. |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count (with differential); liver and renal function, per the PI |
| Handling Protection | Follow local cytotoxic drug handling requirements; please refer to the PI |

## Safety Considerations

- **Drug Interactions**: 13 moderate-level interactions were flagged in the interaction database (14 records in total, including one pharmacology entry): cimetidine, tafenoquine, ketoconazole, brigatinib, crizotinib, encorafenib, ethinylestradiol, lenvatinib, medroxyprogesterone acetate, megestrol acetate, ribociclib, rucaparib and vandetanib. A further pharmacology record lists tipiracil as binding the SARS-CoV-2 non-structural protein 15, which is not a clinical interaction.
- **Adverse effects reported in the literature**: leukopenia, neutropenia, fatigue, diarrhoea and vomiting; one case report describes leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cecum villous adenoma is supported by model score alone (L5), with no trials or publications. Adenomas are managed by endoscopic resection, so systemic cytotoxic chemotherapy is unlikely to be appropriate for a premalignant or benign lesion.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic-link analysis
- TGA Product Information, including warnings, contraindications and the approved indication text, to enable safety screening
- Any preclinical or clinical evidence specific to adenomas or other premalignant colorectal lesions
- A clear clinical rationale for systemic therapy over endoscopic resection
- Consideration of whether the rectosigmoid junction neoplasm prediction should be treated as an on-label sub-site of colorectal cancer rather than a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

