---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-04
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

Sirolimus is an oral mTOR inhibitor marketed in Australia as Rapamune tablets.
The TxGNN model predicts it may be useful for **liposarcoma**, but the evidence is thin: **1 registered clinical trial** (a completed single-arm Phase 2 combination study with no results available) and **no published study that tests sirolimus in liposarcoma**.

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

Detailed mechanism of action data is not available in the data compiled for this report. Sirolimus is known to inhibit mTORC1, a kinase complex that drives cell growth and survival. Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma. Preclinical mouse models of sarcoma also suggest that mTOR inhibition can slow tumour growth. This gives a plausible biological reason to test sirolimus in liposarcoma.

This is a mechanistic extrapolation only. No published study in the compiled data shows that sirolimus works in liposarcoma. The only linked trial tests a combination, so the contribution of sirolimus cannot be separated from its partner drug. The high TxGNN score reflects a model-based association and is not clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma (2014–2021). No results have been published or posted. The design has no control arm, so sirolimus's own effect cannot be determined. |

No ANZCTR trials were identified in the data compiled for this report.

## Literature Evidence

No published study in the compiled data tests sirolimus in liposarcoma. The items below give only indirect context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Current Opinion in Oncology | Rationale and results of molecular-targeted agents in advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Targeted treatments for rare connective tissue tumours and sarcomas, grouped by molecular alteration. |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (secondary analysis) | Journal of the American Society of Nephrology | In adult renal transplant recipients, sirolimus after early cyclosporine withdrawal reduced the risk of cancer. This concerns transplant cancer risk, not liposarcoma treatment. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13860L | Rapamune | Tablet 0.5 mg (oral) | Indication text not available in the data compiled for this report |

One valid single-ingredient licence is recorded, and none are cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions in the listed entries include amphotericin B (including the lipid complex), mesalazine, balsalazide and clarithromycin. Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), several antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), aprepitant and cimetidine.

Please refer to the TGA-approved Product Information (PI) for warnings, contraindications and full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and general mTOR biology. The only linked trial is a single-arm combination study with no available results, and no published study tests sirolimus in liposarcoma, so the evidence level is L5.

**To proceed, the following is needed:**
- Published or posted results of NCT02821507, ideally with data that separate sirolimus's effect from cyclophosphamide's
- Direct clinical or preclinical studies of sirolimus in liposarcoma subtypes
- Detailed mechanism of action data
- Review of the TGA Product Information for safety, and a monitoring plan for infection, metabolic effects and drug interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

