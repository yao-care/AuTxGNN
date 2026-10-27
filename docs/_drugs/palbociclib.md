---
layout: default
title: Palbociclib
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Palbociclib: predicted new indication Hyperthyroidism (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Palbociclib"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brachydactyly-syndactyly syndrome", "myeloid leukemia", "multiple endocrine neoplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "hyperthyroxinemia", "Prinzmetal angina"]
---

# Palbociclib
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

## Palbociclib: From Breast Cancer (Original Indication Not Recorded) to Hyperthyroidism
{: .text-alpha }

**Note on selection:** The prompt specifies using the first predicted indication (rank 1, hyperthyroidism). It has no supporting evidence, so this report also summarises the better-supported candidates (rheumatoid arthritis and myeloid leukaemia) where they inform the decision.

## One-Sentence Summary

Palbociclib is a CDK4/6 inhibitor marketed in Australia as Ibrance (tablet), and the data compiled for this report do not record its approved indication text.
The TxGNN model's top-ranked prediction is **hyperthyroidism** (score 99.44%), but there are **0 clinical trials** and **0 publications** supporting it.
Among lower-ranked predictions, **myeloid leukaemia** (4 early-phase trials, 20 publications) and **rheumatoid arthritis** (preclinical data, 1 case report, 1 cohort study) have more support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG indication text is blank) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Palbociclib is a selective CDK4/6 inhibitor, a class used in hormone receptor-positive, HER2-negative breast cancer. Blocking CDK4/6 arrests the cell cycle at the G1-to-S transition.

For hyperthyroidism, **no mechanistic link has been identified**. No trials or publications support CDK4/6 inhibition in thyroid overactivity. The high TxGNN score is a graph-based association only and should not be treated as evidence of benefit.

By contrast, two other predictions have a plausible rationale:
- **Myeloid leukaemia (rank 6):** CDK6 is a key dependency in AML, particularly MLL- and NUP98-rearranged disease. Preclinical work shows synergy with venetoclax/azacitidine, menin inhibitors and LSD1 inhibition.
- **Rheumatoid arthritis (rank 2):** CDK6 drives synovial fibroblast hyperplasia in mouse arthritis models, and one case report describes RA improvement in a breast cancer patient on palbociclib.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperthyroidism.

For reference, trials registered for the better-supported prediction, myeloid leukaemia:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02310243](https://clinicaltrials.gov/study/NCT02310243) | Phase 1/2 | Unknown | 50 | Palbociclib monotherapy in MLL-rearranged acute leukaemias; no results provided |
| [NCT03132454](https://clinicaltrials.gov/study/NCT03132454) | Phase 1 | Active, not recruiting | 32 | Palbociclib alone and with sorafenib, decitabine or dexamethasone in relapsed/refractory leukaemia |
| [NCT05627232](https://clinicaltrials.gov/study/NCT05627232) | Phase 1 | Recruiting | 24 | Palbociclib pre-treatment then CPX-351 in relapsed/refractory AML |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Precision-oncology platform trial; minimal informative value |

## Literature Evidence

Currently no related literature available for hyperthyroidism.

For reference, selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case report | Mod Rheumatol Case Rep | RA improved in a breast cancer patient treated with palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | Oncologist | Immune-mediated diseases in breast cancer patients on CDK4/6 inhibitors plus endocrine therapy |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical | Int J Mol Sci | CDK6-dependent synovial hyperplasia in arthritic mice |
| [36076608](https://pubmed.ncbi.nlm.nih.gov/36076608/) | 2022 | Preclinical | Biomed Pharmacother | Palbociclib enhances venetoclax plus azacitidine activity in AML |
| [38890447](https://pubmed.ncbi.nlm.nih.gov/38890447/) | 2024 | Preclinical | Leukemia | Menin plus kinase inhibitors effective in NUP98-rearranged leukaemia |
| [38430306](https://pubmed.ncbi.nlm.nih.gov/38430306/) | 2024 | Case report | Cancer Chemother Pharmacol | Palbociclib with venetoclax and azacitidine in refractory therapy-related AML |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12818P | Ibrance | Tablet 75 mg | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions; neutropenia and bone marrow suppression are recognised effects of the class |
| Emetogenicity Classification | Please refer to the PI |
| Monitoring Items | Full blood count; please refer to the PI for further monitoring |
| Handling Protection | Please refer to the PI |

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified (DDInter). Examples include:
  - **Major:** clarithromycin, cobicistat, deferiprone, samarium (153Sm) lexidronam
  - **Moderate:** aprepitant, dexamethasone, cimetidine, simvastatin, saxagliptin, cilostazol, among others
  - **Minor:** prucalopride
- **Class safety signals:** Pharmacovigilance analyses report thromboembolic events, interstitial lung disease and pulmonary toxicity with CDK4/6 inhibitors.

No warnings or contraindications were available from the label data. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperthyroidism, rests on a model score alone, with no trials, no literature and no mechanistic link. Label-based safety data were also unavailable. Myeloid leukaemia (L3) and rheumatoid arthritis (L4) are more credible research questions than the top-ranked hyperthyroidism prediction.

**To proceed, the following is needed:**
- Retrieve the TGA Product Information (approved indication, warnings, contraindications)
- Obtain detailed mechanism-of-action data
- For hyperthyroidism: any mechanistic or experimental evidence before further consideration
- Consider re-prioritising the evaluation toward myeloid leukaemia (await results from the Phase 1/2 trials) and rheumatoid arthritis (needs prospective clinical data)
- Check Australian trial registrations (ANZCTR) for relevant studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

