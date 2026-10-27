---
layout: default
title: Apalutamide
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Apalutamide: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
monitor_inn: "Apalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "benign reproductive system neoplasm", "fibroma of prostate", "prostate phyllodes tumor", "benign neoplasm of prostate", "benign prostate phyllodes tumor", "palmoplantar keratoderma-sclerodactyly syndrome"]
---

# Apalutamide
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

## Apalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility
{: .text-alpha }

## One-Sentence Summary

Apalutamide is an oral androgen receptor inhibitor, originally used to treat prostate cancer.
The TxGNN model predicts it may be effective for **prostate cancer/brain cancer susceptibility** (score 98.4%), but **no clinical trials and no publications** were found for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (the ARTG indication text is not available; this comes from the knowledge graph) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, apalutamide is an androgen receptor (AR) antagonist, and its efficacy in prostate cancer is well established. Mechanistically, it may be applicable only to AR-dependent disease.

The top-ranked prediction describes a genetic susceptibility trait, not a treatable disease state. The high score most likely reflects the closeness of this term to prostate cancer in the knowledge graph. An AR inhibitor has no clear therapeutic target in a susceptibility trait, so the prediction is not biologically convincing on its own.

Other top-ranked predictions are also weak. Several are rare prostatic or reproductive tumours (prostate leiomyoma, fibroma of prostate, prostate phyllodes tumour, Brenner tumour). AR dependence is unclear or unestablished in these, and none has supporting data. The rank 10 prediction (palmoplantar keratoderma-sclerodactyly syndrome) has no known AR link, and apalutamide commonly causes rash, which argues against its use there.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (prostate cancer/brain cancer susceptibility).

For context, the broader "male reproductive organ cancer" prediction (rank 8) returned many trials. Almost all are in prostate cancer, which is already an approved indication, so they reflect label optimisation, not repurposing. The most notable are below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) | Phase 3 | Active, not recruiting | 1052 | TITAN: apalutamide plus ADT vs ADT in metastatic hormone-sensitive prostate cancer |
| [NCT02257736](https://clinicaltrials.gov/study/NCT02257736) | Phase 3 | Active, not recruiting | 982 | Apalutamide plus abiraterone/prednisone vs abiraterone/prednisone in chemotherapy-naive mCRPC |
| [NCT04134260](https://clinicaltrials.gov/study/NCT04134260) | Phase 3 | Active, not recruiting | 586 | INNOVATE: adding apalutamide to salvage treatment in node-positive prostate cancer after prostatectomy |
| [NCT04181203](https://clinicaltrials.gov/study/NCT04181203) | Phase 3 | Active, not recruiting | 490 | Apalutamide with salvage radiotherapy and ADT in high-risk biochemically relapsed prostate cancer |
| [NCT02867020](https://clinicaltrials.gov/study/NCT02867020) | Phase 2 | Completed | 128 | Abiraterone plus ADT vs apalutamide vs both in advanced prostate cancer with non-castrate testosterone |
| [NCT03371719](https://clinicaltrials.gov/study/NCT03371719) | Phase 2 | Active, not recruiting | 298 | BALANCE: salvage radiotherapy with or without apalutamide in recurrent prostate cancer |
| [NCT03124433](https://clinicaltrials.gov/study/NCT03124433) | Phase 2 | Completed | 30 | NEAR: neoadjuvant apalutamide before radical prostatectomy |
| [NCT05191680](https://clinicaltrials.gov/study/NCT05191680) | Phase 2 | Recruiting | 90 | TAPS02: short-term apalutamide in men on active surveillance for prostate cancer |

All of these are in prostate cancer and do not support the predicted new indication.

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For context, the "benign neoplasm of prostate" prediction (rank 7) returned publications, all about apalutamide in prostate cancer (malignant disease) and not benign prostatic tumours. The strong evidence is therefore indirect and already covered by the approved indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) | 2019 | RCT | N Engl J Med | Apalutamide plus ADT in metastatic castration-sensitive prostate cancer (TITAN) |
| [33914595](https://pubmed.ncbi.nlm.nih.gov/33914595/) | 2021 | RCT | J Clin Oncol | TITAN final survival analysis after unblinding and crossover |
| [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) | 2018 | RCT | N Engl J Med | Apalutamide and metastasis-free survival in non-metastatic castration-resistant prostate cancer (SPARTAN) |
| [32907777](https://pubmed.ncbi.nlm.nih.gov/32907777/) | 2021 | RCT | Eur Urol | SPARTAN overall survival analysis |
| [42223077](https://pubmed.ncbi.nlm.nih.gov/42223077/) | 2026 | RCT | N Engl J Med | Perioperative apalutamide in high-risk localised prostate cancer |
| [36167599](https://pubmed.ncbi.nlm.nih.gov/36167599/) | 2023 | RCT (Phase 2) | Eur Urol | ARNEO: neoadjuvant degarelix with or without apalutamide before prostatectomy |
| [39426080](https://pubmed.ncbi.nlm.nih.gov/39426080/) | 2024 | Review | ESMO Open | Drug-drug interactions with androgen receptor pathway inhibitors |
| [33480983](https://pubmed.ncbi.nlm.nih.gov/33480983/) | 2021 | Review | Endocr Rev | Hormonal therapy for prostate cancer |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12992T | Erlyand | Tablet 60 mg | Not available in the data compiled for this report |

Apalutamide is available as an oral tablet only.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Thyroid function, fracture and fall risk, and skin reactions are relevant to this drug class. |
| Handling Protection | Please refer to the PI and local handling guidance |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Those listed in the data compiled for this report include the following.
  - **Major**: bupropion, cisapride, dolasetron, eliglustat
  - **Moderate**: famotidine, rabeprazole, esomeprazole, hydrocortisone, clarithromycin, glimepiride, glipizide, chlorpropamide, dapagliflozin, empagliflozin, loperamide, bisacodyl, alosetron, alvimopan, fidaxomicin, castor oil
- **Known toxicity profile** (from the prediction rationale): rash, fatigue, fracture and fall risk, and hypothyroidism.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a genetic susceptibility trait, not a treatable disease, and no trials or publications support it. The high score likely reflects graph proximity to prostate cancer. The strong Phase 3 evidence for apalutamide belongs to its existing prostate cancer indication and cannot be counted here. The other top-ranked predictions are rare or benign conditions with no evidence and an unfavourable toxicity trade-off.

**To proceed, the following is needed:**
- A clinically meaningful, treatable target indication, since the top prediction is a susceptibility trait
- Mechanism of action data and evidence of AR dependence in any candidate disease
- Preclinical or clinical studies specific to a candidate indication
- The TGA Product Information, including warnings, contraindications and the approved indication text
- Review of the major drug interactions, with a risk-benefit assessment for non-malignant or benign conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

