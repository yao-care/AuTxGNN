---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Denosumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Osteoporosis, postmenopausal osteoporosis, drug-induced osteoporosis"
monitor_inn: "Denosumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dermatitis", "diabetic cataract", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "amyopathic dermatomyositis"]
---

# Denosumab
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

# Denosumab: From Osteoporosis to Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a monoclonal antibody originally used to treat osteoporosis, including postmenopausal and drug-induced osteoporosis.
The TxGNN model predicts it may be useful for **severe nonproliferative diabetic retinopathy** (top-ranked prediction) and **diabetic retinopathy** (second-ranked), but **no clinical trials** and **no direct publications** currently support these indications.
The only indirect literature concerns denosumab in type 2 diabetes generally, so this is a model-only prediction at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, drug-induced osteoporosis (the Australian licence record lists no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predicted indications (for context):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Diabetic retinopathy | 99.23% | L4 | Hold |
| 3 | Dermatitis | 97.25% | L3 | Research question |
| 4 | Diabetic cataract | 96.66% | L4 | Hold |
| 5 | Acrodermatitis chronica atrophicans | 96.23% | L5 | Hold |
| 6 | Neonatal dermatomyositis | 95.81% | L5 | Hold |
| 7 | Hydroa vacciniforme, familial | 95.20% | L5 | Hold |
| 8 | Secondary interstitial lung disease of childhood (connective tissue disease) | 94.97% | L5 | Hold |
| 9 | Acne keloid | 94.78% | L5 | Hold |
| 10 | Amyopathic dermatomyositis | 94.67% | L5 | Hold |

Dermatitis is the only prediction with a registered clinical trial, and that trial was not in dermatitis patients (see below).

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Denosumab is known to be a human monoclonal antibody against RANKL (receptor activator of nuclear factor kappa-B ligand), which suppresses osteoclast-mediated bone resorption. This is the basis of its use in osteoporosis.

The link to diabetic retinopathy is speculative. RANKL/RANK signalling is also involved in inflammation, immune regulation and vascular biology, so a role in retinal microvascular disease is conceivable. However, no direct data show an effect on the retina. The high TxGNN scores (99.63% and 99.23%) come from knowledge-graph proximity and are not evidence of efficacy.

The indirect literature relates to type 2 diabetes, not retinopathy. A 2024 real-world cohort study with meta-analysis reported that denosumab, compared with bisphosphonates, was associated with a lower incidence of type 2 diabetes, fewer foot ulcers and lower all-cause mortality. Whether any of this translates into retinal benefit is unknown.

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy or diabetic retinopathy.

For context, one trial was linked to a lower-ranked prediction (dermatitis):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01978483](https://clinicaltrials.gov/study/NCT01978483) | Phase 1 | Completed | 31 | Effect of RANKL inhibition on UV-induced immunosuppression. It offers mechanistic insight into skin immunity but did not enrol dermatitis patients or measure dermatitis outcomes. |

## Literature Evidence

No publications directly address denosumab in severe nonproliferative diabetic retinopathy. The two papers below were retrieved for diabetic retinopathy and are only indirectly relevant.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohort / meta-analysis | Diabetes, Obesity & Metabolism | Denosumab vs bisphosphonates: lower incidence of type 2 diabetes, foot ulceration and all-cause mortality. Microvascular complications, including retinopathy, were among the outcomes examined, but the data compiled here report no retinopathy-specific result. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observational | Cureus | Use of the FRAX fracture risk tool in adults with type 2 diabetes. Not relevant to retinopathy. |

For diabetic cataract (rank 4), a 2020 multi-database cohort study ([PMID 32026309](https://pubmed.ncbi.nlm.nih.gov/32026309/), *Drugs & Aging*) compared cataract surgery and macular degeneration risk after denosumab versus zoledronic acid. It is an ocular safety comparison and is not evidence of benefit.

For dermatitis (rank 3), the literature is mostly case reports of denosumab-associated skin reactions. These are safety signals, not evidence of efficacy:
- [39175449](https://pubmed.ncbi.nlm.nih.gov/39175449/): acute generalised exanthematous pustulosis (2024)
- [32656848](https://pubmed.ncbi.nlm.nih.gov/32656848/): lichen planus, two cases (2021)
- [31890758](https://pubmed.ncbi.nlm.nih.gov/31890758/): DRESS syndrome (2020)
- [29076163](https://pubmed.ncbi.nlm.nih.gov/29076163/): cutaneous hypersensitivity reaction (2018)

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10061M | Wyost | Injection 120 mg in 1.7 mL | Not listed in the data compiled for this report |

Only one licence is on record (a valid single-ingredient product). The record does not include approved indication text or manufacturer.

## Safety Considerations

**Drug Interactions:** 100 potential interactions were identified. The 20 listed in the data compiled for this report are all rated Moderate. They include:
- **Corticosteroids:** hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, corticotropin and tetracosactide
- **Radiopharmaceuticals and radioimmunotherapy:** ibritumomab tiuxetan, iobenguane (I-131), tositumomab (including I-131)
- **Immunosuppressants and antineoplastics:** tacrolimus, mercaptopurine, trimetrexate, levamisole
- **Biologic:** dupilumab

Corticosteroid co-prescription is common in practice and should be reviewed, particularly in patients who may receive intraocular or periocular steroids.

**Safety signals from the literature:** Case reports describe cutaneous adverse reactions with denosumab (AGEP, DRESS, lichen planus, hypersensitivity reactions, erythema nodosum) and one report of c-ANCA vasculitis. For the neonatal and paediatric predictions (neonatal dermatomyositis, childhood interstitial lung disease), denosumab's association with hypocalcaemia and effects on bone and immune development in paediatric use raises additional concern.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. These were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions for severe nonproliferative diabetic retinopathy and diabetic retinopathy rest on knowledge-graph scores alone (L5 and L4), with no trials and only indirect diabetes-related literature. The mechanistic link is plausible but unproven, and the other predicted indications either lack evidence or are supported mainly by adverse-event case reports.

**To proceed, the following is needed:**
- The TGA Product Information, to complete the safety review (warnings, contraindications and approved indications)
- Detailed mechanism of action data, and preclinical evidence of RANKL/RANK involvement in retinal microvascular disease
- Retinopathy-specific outcomes from existing denosumab diabetes cohorts, or a targeted observational analysis
- If the above are supportive, a registered early-phase trial (Phase 1/2) in diabetic retinopathy, checked against ANZCTR for any Australian studies
- A review of corticosteroid co-prescription risk in the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

