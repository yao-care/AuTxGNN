---
layout: default
title: Paclitaxel
parent: Model Prediction Only (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Paclitaxel: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Ovarian cancer"
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
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

# Paclitaxel: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a microtubule-stabilising cytotoxic chemotherapy, originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **40 registered clinical trials** and **20 publications** compiled for this indication. Paclitaxel is already widely used in breast cancer in clinical practice, so this is closer to a label-adjacent indication than a novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (based on the supplied data; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** The supplied trial list contains mostly Phase 1/2 studies, although several completed Phase 3 trials with paclitaxel-containing regimens are listed (for example NCT00667251, NCT00006459, NCT00513292, NCT00431080, NCT00075270). In most of these, paclitaxel is a backbone rather than the variable being tested, so L2 reflects the supplied data rather than the full real-world evidence base.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, paclitaxel stabilises microtubules, causing G2/M arrest and apoptosis in rapidly dividing tumour cells.

Ovarian cancer and breast cancer are both epithelial malignancies that respond to taxane-based chemotherapy. Reviews in the supplied literature describe paclitaxel and docetaxel as evidence-based components of therapy for advanced breast, lung and ovarian carcinomas, and paclitaxel is used in adjuvant and metastatic breast cancer regimens. The cytotoxic mechanism does not depend on hormone receptor signalling, which is why it is also relevant across receptor-defined subtypes.

## Clinical Trial Evidence

The table lists the most relevant trials from the data compiled (up to 10). Many involve paclitaxel only as part of a combination regimen.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly 1-hour paclitaxel plus trastuzumab in metastatic breast cancer; paclitaxel is a direct regimen component |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Unknown | Not reported | Randomised comparison of two schedules of docetaxel or paclitaxel in metastatic breast cancer |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | Not reported | Gemcitabine plus paclitaxel versus paclitaxel alone in locally recurrent or metastatic breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy with lapatinib versus trastuzumab as first-line therapy in HER2-positive metastatic breast cancer |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Completed | 580 | Lapatinib plus paclitaxel versus paclitaxel alone in first-line advanced or metastatic breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab or both, each plus paclitaxel, in HER2-positive primary breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | Neoadjuvant FEC followed by paclitaxel plus trastuzumab versus the reverse sequence in HER2-positive operable breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C followed by docetaxel versus paclitaxel as adjuvant therapy in node-positive breast cancer |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Completed | 632 | ETNA: neoadjuvant nab-paclitaxel versus solvent-based paclitaxel in HER2-negative high-risk breast cancer (different formulation) |
| [NCT00934895](https://clinicaltrials.gov/study/NCT00934895) | Phase 1/2 | Terminated | 27 | Weekly nab-paclitaxel with everolimus in advanced breast cancer; terminated early (different formulation) |

No ANZCTR identifiers are available in the data compiled. Further trials are listed for this indication but are not shown here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanes are evidence-based components of therapy for advanced breast, lung and ovarian carcinomas |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Review of paclitaxel and docetaxel in breast and ovarian cancer |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 study | Cancer | Doxorubicin plus paclitaxel in advanced breast carcinoma; efficacy and toxicity assessed, with attention to prior adjuvant anthracycline |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Dose-finding study | Ann Oncol | Maximum tolerated doses of 3-hour paclitaxel with cyclophosphamide in advanced breast cancer |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Review | Cancer | Developments in breast cancer chemotherapy |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translational | Nat Commun | TEKT4 germline variations enriched after treatment and linked to paclitaxel resistance |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical | J Cell Physiol | ZD6474 enhances paclitaxel effects in breast carcinoma cells |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Computational/preclinical | Chem Biol Drug Des | Paclitaxel combinations and in vivo biomarkers in breast carcinoma |

The literature for this indication consists mainly of reviews, Phase 2 studies and preclinical work; no randomised controlled trial of paclitaxel itself is included.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4567J | Paclitaxel Ebewe | Solution concentrate for I.V. infusion 300 mg in 50 mL | Not available in the data compiled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane; microtubule stabiliser) |
| Myelosuppression Risk | High. Neutropenia is a key toxicity (neutropenia and thrombocytopenia appear among the knowledge-graph contraindicated conditions) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential, liver function, renal function, and neuropathy and hypersensitivity monitoring |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Specific toxicity data were not available in the data compiled; please refer to the Product Information (PI) warnings and precautions. The classifications above reflect general knowledge of the taxane class.

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for these.

- **Contraindicated or high-risk conditions (knowledge graph, not label text):** neutropenia, agranulocytosis, thrombocytopenia, anaemia, liver disease, hyperbilirubinaemia (including Gilbert syndrome), kidney disease, peripheral neuropathy, myocardial infarction, sudden cardiac arrest, asthma, psoriasis, diabetes mellitus, diabetic ketoacidosis, and anxiety and related disorders. These should be verified against the PI.
- **Drug interactions (100 recorded; main ones shown):**
  - Moderate: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone, eliglustat, metronidazole, miconazole, rolapitant, rosuvastatin, simvastatin, tinidazole, troglitazone
  - Minor: ascorbic acid, levofloxacin
  - Unknown severity: glimepiride, doxycycline, morphine, metformin, omeprazole

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel is mechanistically plausible and already widely used in breast cancer, with numerous Phase 2 and Phase 3 trials of paclitaxel-containing regimens. However, in most of these trials paclitaxel is a backbone or comparator rather than the tested variable, and the Australian product has no approved indication text on record.

**To proceed, the following is needed:**
- The TGA Product Information, to confirm approved indications, warnings and contraindications
- Detailed mechanism of action data
- A review of paclitaxel-specific efficacy evidence (for example, the Phase 3 trials where it is the comparator or randomised variable) for the specific breast cancer subtype and setting
- A safety monitoring plan covering myelosuppression, hypersensitivity, neuropathy and drug interactions

**Other predicted indications in the data compiled (for context):**
- **Estrogen-receptor negative breast cancer and estrogen-receptor positive breast cancer:** Proceed with Guardrails; Phase 2 evidence, with paclitaxel mostly part of combinations
- **Hormone-resistant breast carcinoma:** Research Question; Phase 1/2 evidence only
- **Breast carcinoma by gene expression profile:** Research Question; evidence mostly predictive-biomarker work
- **Ehrlich tumour carcinoma, bilateral breast carcinoma, nipple carcinoma:** Hold; preclinical or case-report evidence only
- **Parameningeal embryonal rhabdomyosarcoma and botryoid-type embryonal rhabdomyosarcoma of the vagina:** Hold; model prediction only, with no trials or literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

