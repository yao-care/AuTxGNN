---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Not stated in the Australian registration data compiled for this repo…"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-beta-thalassemia disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome"]
---

# Fluorouracil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fluorouracil: From Gastric and Colorectal Cancer to Rhabdomyosarcoma

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy originally used for gastrointestinal cancers (including gastric, pancreatic and colonic metastatic disease) and, topically, for skin conditions such as superficial basal cell carcinoma and actinic keratosis.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina** (the top-ranked prediction), but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
Evidence for the broader rhabdomyosarcoma group is limited to 4 older reviews, series and a case report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data compiled for this report. The knowledge graph lists gastric cancer, pancreatic adenocarcinoma, metastatic colon cancer, superficial basal cell carcinoma, actinic keratosis and related skin conditions |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fluorouracil is a thymidylate synthase inhibitor and antimetabolite that disrupts DNA and RNA synthesis in rapidly dividing cells. Its efficacy in gastrointestinal adenocarcinomas is well established, and a cytotoxic effect on a proliferative embryonal sarcoma is biologically plausible.

However, the prediction is supported mainly by the model's network proximity score. Standard rhabdomyosarcoma regimens (VAC/VAI: vincristine, actinomycin D, cyclophosphamide or ifosfamide) do not include fluorouracil. Related predictions (other rhabdomyosarcoma subtypes, liver sarcoma, and sickle cell-related haemoglobinopathies) share the same limitation: a plausible general cytotoxic mechanism but no direct clinical support. The haemoglobinopathy predictions rest on speculative fetal haemoglobin induction, and fluorouracil's myelosuppression makes that risk-benefit profile unfavourable in non-malignant chronic disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (botryoid-type embryonal rhabdomyosarcoma of the vagina) or any of the other nine predicted indications.

---

## Literature Evidence

No publications were found for the top predicted indication. The closest evidence relates to the broader category of rhabdomyosarcoma (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Value of adjuvant chemotherapy for childhood sarcomas, about half of which are rhabdomyosarcomas; not specific to fluorouracil |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | 13-year experience with childhood nasopharyngeal carcinoma; indirect relevance |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | Adult lingual rhabdomyosarcoma; cisplatin plus 5-fluorouracil was a prior line that was followed by disease progression |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | General review of curability of cancers with chemotherapy, including rhabdomyosarcoma |

For liver sarcoma (rank 7), the most relevant papers are a 2019 single-centre cohort on adult primary liver sarcoma ([29346784](https://pubmed.ncbi.nlm.nih.gov/29346784/), Digestive Surgery) and a 2001 report of two paediatric cases of ruptured undifferentiated liver sarcoma ([11294295](https://pubmed.ncbi.nlm.nih.gov/11294295/), J Hepatobiliary Pancreat Surg). Neither establishes a fluorouracil-specific benefit. Most other retrieved papers were preclinical or off-target.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13758D | TOLAK 4% ONCE DAILY | Cream 40 mg per g (4%), 20 g | Not stated in the data compiled |

The only registered Australian product is a topical cream. No injectable formulation appears in the data compiled, so route compatibility with systemic sarcoma therapy has not been established.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph lists neutropenia, leukopenia, thrombocytopenia and agranulocytosis among its contraindication associations |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential, liver and renal function (suggested given the associations below) |
| Handling Protection | Follow local cytotoxic drug handling requirements for systemic formulations |

---

## Safety Considerations

- **Key Warnings and Contraindications**: Label-based data were not available for this report. The knowledge graph (not label text) associates fluorouracil with caution or contraindication in: dihydropyrimidine dehydrogenase (DPD) deficiency, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrhoeal disease, active peptic ulcer disease, stomatitis, pharyngitis and pyoureter.
- **Drug Interactions** (100 interactions identified; the first 20 retrieved are shown here): Moderate interactions with **metronidazole** and **tinidazole**. Minor interactions with **cimetidine** and **levofloxacin**. The remainder (e.g. calcitriol, doxycycline, omeprazole, pantoprazole, metformin, morphine) have unclassified severity.

Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.75%), but there are no clinical trials or publications for the top-ranked indication, so the evidence level is L5 (model prediction only). Fluorouracil is not part of standard rhabdomyosarcoma regimens, and the only Australian product is a topical cream.

**To proceed, the following is needed:**
- Detailed mechanism of action data (e.g. from DrugBank)
- Product Information warnings and contraindications (this safety data gap blocks progression to safety screening)
- Preclinical or clinical evidence specific to rhabdomyosarcoma subtypes, and a comparison against standard VAC/VAI regimens
- Assessment of route and formulation compatibility, as the registered product is topical only
- DPD deficiency screening and a haematological monitoring plan if systemic use is ever considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

