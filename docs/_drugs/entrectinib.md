---
layout: default
title: Entrectinib
parent: Model Prediction Only (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Entrectinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Entrectinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "thrombocytopenia", "cytomegalovirus infection", "pulmonary hypertension", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "female breast carcinoma", "transient neonatal thrombocytopenia", "infectious bovine rhinotracheitis"]
---

# Entrectinib
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

# Entrectinib: From Its Registered Oncology Use to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib is an oral kinase inhibitor (TRK, ROS1 and ALK) marketed in Australia as Rozlytrek, but the data compiled for this report do not include its approved indication text.
The TxGNN model's top-ranked prediction is **multiple endocrine neoplasia**, supported by **1 clinical trial** (terminated, 2 patients, not informative) and **1 publication** (a mechanistic study not specific to entrectinib).
A better-supported secondary prediction, **female breast carcinoma**, has a Phase 2 basket trial and several publications, and is covered in the notes below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L3 (as assigned in the compiled data; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (for the top-ranked indication); Proceed with Guardrails for the NTRK-fusion breast carcinoma subset |

*Note on evidence level:* The supporting material for multiple endocrine neoplasia consists of one terminated, non-specific Phase 1 trial and one mechanistic paper. Under the L1-L5 rules this sits closer to L4 (mechanistic evidence) than L3. The compiled data assign L3, and that grading is reported here with this caveat.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From the rationale analysis, entrectinib inhibits TRK, ROS1 and ALK kinases. It also has reported activity against RET.

Multiple endocrine neoplasia type 2 is driven by activating germline RET mutations. This gives a plausible biological link. A 2024 paper (PMID 38438731) describes resistance mechanisms to selective RET inhibitors in RET-driven cancer. It is relevant to the biology but is not direct clinical evidence for entrectinib.

The rationale is only moderately strong. Entrectinib is not a selective RET inhibitor, and better-validated RET agents (selpercatinib, pralsetinib) already exist.

**Other predictions in the ranked list:**
- **Female breast carcinoma (score 97.76%)** has the strongest evidence of the ten predictions. It is graded L2, with a recommendation of Proceed with Guardrails. NTRK3 fusions (ETV6-NTRK3) define secretory breast carcinoma, a rare subtype. Benefit would be limited to the biomarker-defined (NTRK fusion) subset, not unselected breast cancer.
- **Thrombocytopenia and pulmonary hypertension** have only case reports describing an adverse event context. They do not support benefit.
- **Amenorrhoea, cytomegalovirus infection, other thrombocytopenia variants and infectious bovine rhinotracheitis** have no clinical or literature support and no identifiable mechanistic link. The veterinary disease is likely a knowledge-graph artefact.

## Clinical Trial Evidence

**Multiple endocrine neoplasia (top-ranked prediction)**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision-oncology platform trial. Not specific to multiple endocrine neoplasia, and no interpretable efficacy or safety signal. |

**Female breast carcinoma (supporting context)**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02568267](https://clinicaltrials.gov/study/NCT02568267) | Phase 2 | Active, not recruiting | 534 | STARTRK-2 basket study in solid tumours with NTRK1/2/3, ROS1 or ALK fusions. Supports the tumour-agnostic NTRK use, but is not breast-specific and the breast cohort is small. |
| [NCT02650401](https://clinicaltrials.gov/study/NCT02650401) | Phase 1/2 | Active, not recruiting | 69 | Paediatric and young-adult study in solid and CNS tumours with NTRK or ROS1 fusions. Population largely outside adult breast carcinoma. |
| [NCT05238831](https://clinicaltrials.gov/study/NCT05238831) | Early Phase 1 | Withdrawn | 0 | SMMART-ACT adaptive precision-medicine pilot. No participants enrolled, so no data. |

No ANZCTR trial identifiers were available in the compiled data.

## Literature Evidence

**Multiple endocrine neoplasia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/mechanistic | NPJ Precis Oncol | Off-target resistance mechanisms to selective RET inhibitors (selpercatinib) in a patient with RET-mutant medullary thyroid carcinoma. Not about entrectinib. |

**Female breast carcinoma (supporting context)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37330338](https://pubmed.ncbi.nlm.nih.gov/37330338/) | 2023 | Review | Pathology | NTRK fusions in solid tumours and testing for treatment with larotrectinib or entrectinib. |
| [35927900](https://pubmed.ncbi.nlm.nih.gov/35927900/) | 2023 | Review | Curr Med Chem | Progress in TRK inhibitors. Trk fusions drive secretory breast cancer. |
| [38852701](https://pubmed.ncbi.nlm.nih.gov/38852701/) | 2024 | Preclinical | Cancer Lett | Entrectinib plus pacritinib (TrkA/JAK2) suppressed growth and metastasis in HER2-positive and triple-negative breast cancer models. |
| [35695563](https://pubmed.ncbi.nlm.nih.gov/35695563/) | 2022 | Trial protocol (Phase 2) | Future Oncol | ROSALINE: neoadjuvant ROS1 targeting plus endocrine therapy in invasive lobular carcinoma. |
| [34176200](https://pubmed.ncbi.nlm.nih.gov/34176200/) | 2021 | Case report | Oncologist | Locally recurrent secretory breast carcinoma with NTRK3 fusion. |
| [41064088](https://pubmed.ncbi.nlm.nih.gov/41064088/) | 2025 | Case report | Front Oncol | Late metastatic breast secretory carcinoma (ETV6::NTRK3), 10-year follow-up. |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Review | Int J Mol Sci | Chemotherapy-resistant triple-negative breast cancer. Only indirectly relevant. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12092K | Rozlytrek | Capsule 200 mg (oral) | Not available in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Haematological parameters, liver and renal function are generally reasonable to monitor. |
| Handling Protection | Please refer to the PI |

## Safety Considerations

Label-based warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for these.

**Drug interactions:** 100 interactions were identified. The major-level ones among those listed include:
- Aprepitant
- Dexamethasone
- Clarithromycin
- Dolasetron

Moderate-level interactions include famotidine, loperamide, cimetidine, budesonide, levofloxacin, naltrexone, saxagliptin, empagliflozin and several bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate). Minor-level interactions include naloxegol and metronidazole. Only 20 of the 100 interactions were available for review.

**Signals from the literature:** A 2025 case report (PMID 41002576) describes pulmonary tumour thrombotic microangiopathy progressing during entrectinib therapy despite tumour response. It is noted as a possible safety or disease-complication concern. Kinase inhibitors may also cause cytopenias, so the use of entrectinib for thrombocytopenia is questionable.

## Conclusion and Next Steps

**Decision: Hold** (multiple endocrine neoplasia). **Proceed with Guardrails** applies only to NTRK-fusion-positive breast carcinoma.

**Rationale:**
- For multiple endocrine neoplasia, the only supporting items are one terminated, uninformative Phase 1 trial and one mechanistic paper that is not about entrectinib. Better-validated, selective RET inhibitors are already available.
- The breast carcinoma prediction has a Phase 2 basket trial and several case reports and preclinical studies. However, benefit is restricted to the NTRK-fusion subset, which is largely covered by the tumour-agnostic NTRK use.
- The other eight predictions have no support, and two (thrombocytopenia and pulmonary hypertension) point towards possible harm.

**To proceed, the following is needed:**
- The TGA-approved Product Information, to confirm the registered indication and obtain warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Preclinical or clinical data on entrectinib's RET activity in RET-driven multiple endocrine neoplasia, compared with selective RET inhibitors
- For breast carcinoma, breast-specific outcomes from the STARTRK-2 basket cohort and a plan for NTRK fusion testing
- Review of the full list of 100 drug interactions, particularly strong CYP3A4 inhibitors and inducers, and a safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

