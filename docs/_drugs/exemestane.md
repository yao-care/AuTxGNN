---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 282
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
monitor_inn: "Exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
description: "Exemestane: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Not recorded in the local data"
---

# Exemestane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Exemestane: Antithrombin deficiency type 2
{: .text-alpha }

> **Note on the selected indication:** The top-ranked prediction (rank 1) is antithrombin deficiency type 2, which has no supporting evidence. All three are reported below. The original indication is not recorded in the data compiled for this report. It is described here from general knowledge of the drug class.

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor, marketed in Australia as Aromasin 25 mg tablets. It is generally used for hormone-receptor-positive breast cancer in postmenopausal women.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2** (top-ranked), but there are **0 clinical trials** and **0 publications** supporting this. Across the top 10 predictions, only amenorrhoea has literature (**5 publications**), and none of these supports exemestane as a treatment for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Exemestane is known as a steroidal aromatase inhibitor that lowers circulating oestrogen by blocking the conversion of androgens to oestrogens.

For antithrombin deficiency type 2, no established mechanism links aromatase inhibition to antithrombin function. Hormonal agents can influence coagulation, but aromatase inhibition is not known to correct a SERPINC1 defect. The score of 0.9983 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Exemestane also carries thromboembolic warnings, which argues against use in a thrombophilic state.

The same applies to the other coagulation-related predictions (factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, thrombophilia). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a pharmacological rationale.


## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

## Literature Evidence

No literature was retrieved for antithrombin deficiency type 2. The five publications below were retrieved for amenorrhoea (rank 2). They describe amenorrhoea as a treatment effect or clinical context in breast cancer, not as a therapeutic target. Titles and abstracts are truncated, so study designs cannot be confirmed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort (presumed) | Ann Oncol | Incidence and predictors of ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhoea who switched from tamoxifen to exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone-receptor-positive early breast cancer |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review/Commentary | J Clin Oncol | Whether oestradiol monitoring is needed in women receiving ovarian suppression for breast cancer |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Prog Med | Current role of LHRH analogues in early and advanced breast cancer in premenopausal patients |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klin Onkol | Aromatase inhibitor treatment in postmenopausal women with breast cancer and management of side effects |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10103R | Aromasin | Tablet 25 mg (oral) | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (steroidal aromatase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Bone health and menopausal-type adverse effects are considerations raised by the mechanism. |
| Handling Protection | Please refer to the PI |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The listed examples include two rated Moderate: **dexamethasone** and **troglitazone**. Many others have an unknown severity rating, including pantoprazole, morphine, metformin, omeprazole, simvastatin, acetylsalicylic acid, rosuvastatin and ondansetron. Severity ratings need clinical review.
- **Thromboembolic risk**: Exemestane carries thromboembolic warnings, which argues against use in thrombophilic conditions.
- **Androgenic activity**: Weak androgenic activity of the steroidal structure and its metabolites suggests a risk of worsening acne, not improvement.
- **Oestrogen lowering**: Oestrogen lowering may worsen headache, so use in migraine is unsupported.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a computational signal with no trials, no literature and no plausible mechanism, and there is a thromboembolic safety concern. The only predictions with literature (amenorrhoea) describe it as a treatment effect, not a target. All predictions are rated Hold.

**To proceed, the following is needed:**
- Mechanism of action data and the approved indication text from the TGA-approved PI
- Warnings and contraindications from the PI, which are required before any safety screening
- Clinical review of the interaction severity ratings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

