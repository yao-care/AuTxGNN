---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-03
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor (mTORC1 blockade) that is marketed in Australia as an oral tablet. The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a single-arm Phase 2 combination study) and **7 publications** linked, none of which directly establishes efficacy of sirolimus in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, sirolimus inhibits mTORC1, and activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma. This gives a plausible biological rationale for testing an mTOR inhibitor in this tumour type.

This rationale is an extrapolation. The single linked trial tests sirolimus together with another drug, so the contribution of sirolimus alone cannot be separated. The linked literature consists mainly of general sarcoma reviews and studies of cancer risk in transplant recipients, which are only indirectly relevant.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus combined with cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No efficacy results were supplied, and there is no control arm. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (secondary analysis) | J Am Soc Nephrol | In renal transplant recipients, sirolimus after early cyclosporine withdrawal reduced cancer risk. Not a liposarcoma study. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of recent trials of molecular-targeted agents in advanced sarcomas. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Effects of long-term immunosuppressive drugs on malignancy development in renal transplant patients. |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Retrospective cohort | Fam Cancer | Clinical spectrum of PTEN hamartoma tumour syndrome and associated malignancies. |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | Three cases of fibro-adipose vascular anomaly with emphasis on the mTOR pathway. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13860L | Rapamune | Tablet 0.5 mg (oral) | Indication text not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically includes FBC, liver and renal function, and lipid and glucose levels |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Those flagged **Major** include amphotericin B (and its lipid complex), mesalazine, balsalazide and clarithromycin. Moderate interactions include several antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant and cimetidine.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study in the data directly demonstrates sirolimus efficacy in liposarcoma. The only linked trial is a single-arm combination study without supplied results, and the literature is indirect. The prediction therefore rests on the model score and general mTOR biology (Evidence Level L5).

**To proceed, the following is needed:**
- Results of NCT02821507, with the liposarcoma subgroup and the contribution of sirolimus separated from cyclophosphamide
- Confirmation of the histology scope of that trial
- Detailed mechanism of action data
- Warnings and contraindications from the TGA-approved Product Information
- Preclinical or early-phase data for sirolimus specifically in liposarcoma

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

