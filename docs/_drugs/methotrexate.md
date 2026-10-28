---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Acute lymphoblastic leukaemia, non-Hodgkin lymphoma…"
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
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

## Methotrexate: From Acute Lymphoblastic Leukaemia and Lymphoma to Pulmonary Blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate medicine originally used for acute lymphoblastic leukaemia, non-Hodgkin lymphoma, rheumatoid arthritis, psoriasis and cutaneous T-cell lymphoma.
The TxGNN model predicts it may be effective for **pulmonary blastoma** (the top-ranked prediction), but this prediction has **no clinical trials and no publications** supporting it.
Other predictions in the list have more support, notably **Hodgkin lymphoma** and **rhabdomyosarcoma**, and these are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukaemia, non-Hodgkin lymphoma, rheumatoid arthritis, psoriasis, mycosis fungoides (approved indication text for the Australian product is not available) |
| Predicted New Indication | Pulmonary blastoma (top-ranked) |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

**Other predictions of note** (all scores 0.9921 to 0.9945):

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Primary pulmonary lymphoma | 0.9945 | L5 | Hold |
| 5 | Hodgkin lymphoma | 0.9932 | L3 | Research question |
| 6 | Rhabdomyosarcoma | 0.9925 | L2 | Research question |

Ranks 4 and 7 to 10 (well-differentiated fetal adenocarcinoma of the lung, two CLL/SLL subtypes, parameningeal embryonal rhabdomyosarcoma, and botryoid-type embryonal rhabdomyosarcoma of the vagina) have prediction-only support (L5, Hold).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Methotrexate is generally recognised as an antifolate that inhibits dihydrofolate reductase (DHFR) and impairs nucleotide synthesis in rapidly dividing cells. Its efficacy in leukaemia and lymphoma is established, and mechanistically it may be applicable to other fast-growing tumours.

For **pulmonary blastoma**, this link is plausible but unsupported. It is a rare, aggressive lung tumour, and no trials or literature were retrieved.

The better-supported predictions share the same rationale:
- **Hodgkin lymphoma:** methotrexate is established in non-Hodgkin lymphoma and has been used in the VBM regimen (vinblastine, bleomycin, methotrexate) for early-stage Hodgkin lymphoma.
- **Rhabdomyosarcoma:** a Phase 2 trial of high-dose methotrexate in children with high-risk rhabdomyosarcoma has been published, but the data are old and efficacy is unconfirmed.
- **Small cell lung carcinoma:** methotrexate appeared in historical combination chemotherapy, but the retrieved trials involve non-small cell lung cancer or supportive care.

## Clinical Evidence for Pulmonary Blastoma

Currently no related clinical trials registered.

### Selected Trials for Other Predictions

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03520842](https://clinicaltrials.gov/study/NCT03520842) | Phase 2 | Completed | 22 | Regorafenib plus oral methotrexate in KRAS-mutated NSCLC (small cell lung carcinoma prediction; different histology) |
| [NCT05663866](https://clinicaltrials.gov/study/NCT05663866) | Phase 2 | Active, not recruiting | 68 | Methotrexate to prevent amivantamab infusion reactions in NSCLC (supportive care only) |
| [NCT00290498](https://clinicaltrials.gov/study/NCT00290498) | Phase 2 | Completed | 67 | R-HCVAD alternating with rituximab-methotrexate-cytarabine vs R-CHOP in aggressive B-cell NHL (Hodgkin lymphoma prediction; NHL rather than Hodgkin) |
| [NCT00005977](https://clinicaltrials.gov/study/NCT00005977) | Phase 3 | Completed | 83 | Methotrexate dose intensification in advanced small non-cleaved cell NHL and B-cell ALL |
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Phase 3 | Active, not recruiting | 650 | B-NHL 2013 protocol for children and adolescents with mature aggressive B-cell lymphoma (NHL, not Hodgkin) |
| [NCT00928018](https://clinicaltrials.gov/study/NCT00928018) | Phase 3 | Completed | 139 | Methotrexate as part of GVHD prophylaxis in lymphoma transplant (supportive care) |
| [NCT00574496](https://clinicaltrials.gov/study/NCT00574496) | Phase 2 | Completed | 25 | Salvage chemotherapy then allogeneic transplant in high-risk or relapsed Hodgkin lymphoma (methotrexate likely GVHD prophylaxis) |
| [NCT00357084](https://clinicaltrials.gov/study/NCT00357084) | Phase 2 | Completed | 53 | Methotrexate with glucocorticoids for acute GVHD (relevance to rhabdomyosarcoma uncertain) |

Most of these trials use methotrexate as one component or as supportive care, so they do not isolate its antitumour effect in the predicted indication. No trial tests methotrexate specifically for pulmonary blastoma.

## Literature Evidence

No literature was retrieved for pulmonary blastoma. The most relevant publications for the other predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Clinical study | Cancer | VBM chemotherapy plus irradiation in early-stage, favourable Hodgkin lymphoma |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review | Crit Rev Oncol Hematol | VBM gave 94-100% complete remission in early Hodgkin lymphoma, with early pulmonary toxicity |
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | Phase 2 trial | J Pediatr Hematol Oncol | High-dose methotrexate in untreated children with high-risk or metastatic rhabdomyosarcoma |
| [36614297](https://pubmed.ncbi.nlm.nih.gov/36614297/) | 2023 | Cohort | Int J Mol Sci | BOMP-EPI (includes methotrexate) in adult relapsed or metastatic rhabdomyosarcoma |
| [2835443](https://pubmed.ncbi.nlm.nih.gov/2835443/) | 1988 | Clinical study | J Clin Oncol | Adjuvant chemotherapy after resection of small cell lung carcinoma |
| [2983855](https://pubmed.ncbi.nlm.nih.gov/2983855/) | 1985 | Clinical study | Cancer | Adding methotrexate to VAC plus radiotherapy in small cell lung cancer; no improvement reported |
| [30842385](https://pubmed.ncbi.nlm.nih.gov/30842385/) | 2019 | Cohort | Rinsho Ketsueki | High-dose methotrexate plus rituximab in primary CNS lymphoma (not pulmonary) |
| [32590768](https://pubmed.ncbi.nlm.nih.gov/32590768/) | 2020 | Case report | Medicine | Primary pulmonary NK/T-cell lymphoma, two cases and review |
| [38720609](https://pubmed.ncbi.nlm.nih.gov/38720609/) | 2024 | Case report | Kyobu Geka | Primary pulmonary DLBCL arising from methotrexate-associated lymphoproliferative disorder |

Note that some retrieved papers describe methotrexate as a *cause* of lymphoproliferative disorders rather than a treatment, and several concern CNS lymphoma rather than pulmonary disease.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11268C | Trexject | Injection 15 mg in 0.3 mL pre-filled syringe | Not available in the data compiled |

Only injectable presentations are listed in the data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate antimetabolite) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions; the knowledge graph flags leukopenia, thrombocytopenia and anaemia as contraindicated conditions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count, liver and renal function (consistent with the contraindication signals listed below) |
| Handling Protection | Follow local cytotoxic drug handling requirements |

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI).

**Contraindicated conditions (TxGNN model (deep learning) signals, not label text; they may reflect similarities the model learned between related diseases, not biological evidence):** liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, leukopenia, anaemia (including macrocytic), peptic and gastric ulcer disease, ulcerative colitis, inflammatory bowel disease, stomatitis, interstitial lung disease, pulmonary fibrosis, substance abuse or dependence, immune system disease, and pyoureter.

**Drug interactions:** 100 interactions were identified; the 20 listed in the data include these **major** ones:
- Rabeprazole
- Amoxicillin
- Acetylsalicylic acid (aspirin)

Moderate interactions include doxycycline, tetracycline, clarithromycin, mesalazine, balsalazide, amphotericin B, bupropion, pioglitazone, acarbose, chenodeoxycholic acid, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone). Potassium citrate is a minor interaction.

Relevant to lung indications: interstitial lung disease and pulmonary fibrosis appear as contraindications, and pulmonary toxicity was noted with VBM in early Hodgkin lymphoma trials.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked indication, pulmonary blastoma)

**Rationale:**
- The pulmonary blastoma prediction rests on model score alone (L5), with no trials or publications. Of the other predictions, Hodgkin lymphoma (L3) and rhabdomyosarcoma (L2) have the most support and could be taken forward as research questions, while the evidence for small cell lung carcinoma and primary pulmonary lymphoma is indirect.

**To proceed, the following is needed:**
- Mechanism of action data to strengthen the mechanistic-link analysis
- TGA-approved Product Information for warnings, contraindications and approved indications (a blocking gap for safety screening)
- Targeted literature review and case-series data for pulmonary blastoma
- For Hodgkin lymphoma and rhabdomyosarcoma, a focused review of modern evidence, since the supporting studies are older and mixed
- A pulmonary safety plan, given the lung-related contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

