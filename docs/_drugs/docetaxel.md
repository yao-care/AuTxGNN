---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Docetaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Docetaxel: From Cytotoxic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a semisynthetic taxane antineoplastic agent and a well-established component of solid tumour chemotherapy regimens internationally.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction.
Notably, this prediction aligns with established global clinical practice — confirming a strong mechanistic and evidentiary foundation — while the Australian regulatory dataset requires manual verification to confirm local registration status.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset (TGA registration data not retrieved — see note below) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Australia Market Status | Not found in current dataset (manual ARTG verification required) |
| Number of ARTG Entries | 0 (data gap — see note below) |
| Recommended Decision | Proceed with Guardrails |

> **⚠️ Data Quality Note:** The Australia regulatory query was directed to the TFDA (Taiwan FDA) data source and returned zero results. This is a data pipeline issue, not a reflection of actual Australian registration status. Healthcare professionals should verify Docetaxel's current ARTG status directly at [www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) before clinical use.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not recorded in the current Evidence Pack. Based on the published scientific literature, Docetaxel is a semisynthetic taxane derived from the European yew (*Taxus baccata*) and belongs to the antitubulin drug class. Docetaxel binds to the β-tubulin subunit of microtubules, stabilising the polymerised form and preventing depolymerisation. This arrests tumour cell cycle progression at the G2/M checkpoint, ultimately triggering apoptosis. Because rapidly proliferating cancer cells depend critically on intact mitotic spindle function, highly proliferative malignancies — including most breast cancer subtypes — are intrinsically sensitive to this mechanism.

The mechanistic rationale for Docetaxel in breast cancer extends across all major molecular subtypes. In HER2-positive disease, Docetaxel demonstrates synergistic cytotoxicity when combined with Trastuzumab: Trastuzumab-mediated antibody-dependent cell-mediated cytotoxicity (ADCC) is potentiated by Docetaxel-induced microtubule disruption, producing enhanced tumour cell death through complementary pathways. This synergy underpins internationally established regimens such as TCH (Docetaxel + Carboplatin + Trastuzumab) and sequential EC→TH. In triple-negative breast cancer (TNBC), where no approved targeted therapies exist for the majority of patients, taxane-based chemotherapy remains the cornerstone of both neoadjuvant and adjuvant protocols, with pathological complete response (pCR) serving as a validated surrogate endpoint for long-term survival.

The TxGNN prediction score of 99.90% reflects the strength of drug–disease relationships captured in the underlying knowledge graph. In this instance, the model is not identifying a novel repurposing opportunity but rather confirming a mechanistically and clinically well-supported indication already embedded in global oncology practice. For Australian healthcare professionals, the clinical priority is not the existence of evidence, but rather ensuring local registration status is confirmed, that treatment is delivered within approved eviQ protocols, and that appropriate safety monitoring — particularly G-CSF prophylaxis and peripheral neuropathy surveillance — is implemented according to Australian standards.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | One of the largest breast cancer adjuvant chemotherapy RCTs ever conducted; compared TC×6 or AC→weekly Paclitaxel with or without Trastuzumab in women with HER2-low node-positive or high-risk node-negative invasive breast cancer |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1,384 | Prospective randomised trial comparing EC→Docetaxel (100 mg/m²) vs ET→Capecitabine as adjuvant chemotherapy for HER2-negative, node-positive breast cancer; long-term follow-up completed in 2019 |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | Randomised double-blind trial of Bevacizumab + Docetaxel vs Docetaxel + placebo as first-line therapy for HER2-negative metastatic breast cancer; evaluated anti-angiogenic combination in taxane-eligible patients |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Landmark TCH trial: randomised comparison of Docetaxel+Trastuzumab (DH) vs Docetaxel+Carboplatin+Trastuzumab (TCH) as first-line chemotherapy for HER2-amplified advanced breast cancer |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Triple Negative Trial: direct randomised comparison of Carboplatin vs Docetaxel (taxane standard of care) in ER-/PR-/HER2- metastatic or recurrent locally advanced breast cancer; final results publication pending confirmation |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | ECOG trial comparing AC→Paclitaxel vs AC→Docetaxel administered weekly or every 3 weeks in node-positive stage II–IIIA breast cancer; established dosing schedule optimisation evidence |
| [NCT00464646](https://clinicaltrials.gov/study/NCT00464646) | Phase 2 | Completed | 105 | Phase 2 study of sequential EC→Docetaxel+Trastuzumab+Bevacizumab as neoadjuvant/adjuvant therapy in HER2-positive locally advanced breast cancer; specifically evaluated cardiac safety impact of adding Bevacizumab |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC study: EC→Docetaxel+Carboplatin in Nigerian women with TNBC; assessing pathological complete response rate and blood-based biomarkers of chemotherapy resistance in a population with limited prior data |
| [NCT01503905](https://clinicaltrials.gov/study/NCT01503905) | N/A | Unknown | 600 | Multicentre randomised trial comparing Docetaxel+Epirubicin vs Docetaxel+Epirubicin+Cyclophosphamide as neoadjuvant chemotherapy in operable premenopausal breast cancer; includes assessment of chemo-induced amenorrhea outcomes |
| [NCT00217672](https://clinicaltrials.gov/study/NCT00217672) | Phase 2 | Completed | 76 | Randomised Phase 2 trial of Docetaxel with or without Bevacizumab as first-line therapy for HER2-negative metastatic breast cancer; provided preliminary data informing larger Phase 3 anti-angiogenic combination trials |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | Journal of Clinical Oncology | ABC Trials (three linked RCTs including NSABP B-49): compared TC×6 (Docetaxel+Cyclophosphamide) vs standard TaxAC regimens in early breast cancer; established that TC6 may be non-inferior to some but not all anthracycline-taxane combinations |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | Journal of Clinical Oncology | Foundational review of Docetaxel's preclinical and clinical profile; established the antineoplastic taxoid mechanism and summarised early clinical response data that underpinned subsequent approval |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Prospective | Breast Cancer (Tokyo) | Prospective study of anthracycline-free Docetaxel+Cyclophosphamide+Trastuzumab (HER-TC) as neoadjuvant chemotherapy in HER2-positive breast cancer; evaluated pCR rates and tolerability as an alternative to anthracycline-containing regimens |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Cohort | British Journal of Cancer | Microarray gene expression analysis identifying predictive biomarkers of pathological complete response (pCR) to Trastuzumab+Docetaxel-based treatment in HER2-positive breast carcinoma |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Research and Treatment | Comprehensive review of Docetaxel-anthracycline combination regimens in metastatic breast cancer; summarised Phase 2 and Phase 3 evidence for Doxorubicin and Epirubicin combinations and the rationale for non-overlapping toxicity profiles |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | UK review of Paclitaxel and Docetaxel in breast and ovarian cancer; assessed early licensing evidence and concluded on the then-unproven nature of benefits, providing historical benchmark for subsequent evidence development |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews lessons learned from Docetaxel clinical development, covering pharmacogenetics, population pharmacokinetic modelling, and quantitative pharmacology — relevant to dose individualisation in Australian practice |
| [15316749](https://pubmed.ncbi.nlm.nih.gov/15316749/) | 2004 | Phase 2 | Cancer Chemotherapy and Pharmacology | Phase 2 study of Docetaxel + high-dose Epirubicin as neoadjuvant chemotherapy in locally advanced breast cancer; assessed pathological complete response as a predictor of long-term survival |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Retrospective investigation of the association between adjuvant Docetaxel-based chemotherapy and breast cancer-related lymphedema in stage II/III patients; relevant to long-term adverse event monitoring and patient counselling |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clinical Breast Cancer | Phase 2 trial of Docetaxel + Cisplatin (both 70 mg/m²) as primary neoadjuvant chemotherapy for locally advanced breast carcinoma ≥5 cm; evaluated pCR rates and downstaging prior to modified radical mastectomy |

---

## Australia Market Information

No ARTG registration data was retrieved for Docetaxel in the current Evidence Pack. The regulatory data query was directed to the TFDA (Taiwan FDA) database and returned zero results, indicating that Australian TGA-specific data has not yet been integrated into this pipeline.

**Action required:** Healthcare professionals should verify current registration status and access approved Product Information directly through the [TGA ARTG Public Summary Search](https://www.tga.gov.au/resources/artg). Docetaxel is internationally registered under multiple brand names (including Taxotere and various generics) and is expected to have ARTG entries for intravenous use in oncology. Australian dosing protocols should be accessed via **eviQ Cancer Treatments Online** ([eviQ.org.au](https://www.eviQ.org.au)).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (antitubulin / microtubule-stabilising agent) |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia occurs in 10–50% depending on regimen, dose, and G-CSF prophylaxis use. G-CSF primary prophylaxis is recommended for regimens containing Docetaxel ≥75 mg/m² |
| Emetogenicity Classification | Low to moderate (minimal-to-low emetogenic potential per MASCC/ESMO guidelines; note that dexamethasone premedication is required for fluid retention and hypersensitivity prevention rather than primarily for antiemesis) |
| Monitoring Items | Full blood count with differential (before each cycle and at expected nadir); liver function tests (AST, ALT, ALP, bilirubin — dose modification required for hepatic impairment); serum creatinine; peripheral neuropathy grading (CTCAE scale, each cycle); body weight and signs of fluid retention; cardiac function assessment when used with anthracyclines or Trastuzumab |
| Handling Protection | Full cytotoxic drug handling precautions required in accordance with Australian standards — refer to eviQ protocols, relevant state/territory pharmacy compounding guidelines, and institutional cytotoxic safety policies |

> **Additional toxicity notes of clinical relevance:** Docetaxel causes a cumulative fluid retention syndrome (peripheral oedema, pleural effusion, weight gain) that is substantially reduced by standard dexamethasone premedication (typically oral Dexamethasone 8 mg twice daily for 3 days, commencing the day before infusion). Nail toxicity, alopecia, and cutaneous reactions are common. Severe hypersensitivity reactions can occur; premedication is mandatory. Peripheral neuropathy may be cumulative and dose-limiting in some patients, particularly in combination with other neurotoxic agents.

---

## Safety Considerations

No specific safety data — including key warnings, contraindications, or drug interaction information — was available in the current Evidence Pack. All safety fields were returned without data.

> Please refer to the **TGA-approved Product Information (PI)** for Docetaxel for complete safety information, including black-box warnings, contraindications, precautions for use in hepatic impairment, and management of serious adverse reactions. Australian oncology practitioners should also consult **eviQ Cancer Treatments Online** for evidence-based protocol guidance, supportive care recommendations, and standardised monitoring plans.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a 99.90% prediction score for Docetaxel in female breast carcinoma, consistent with the extensive international evidence base that qualifies this as L1 evidence. Multiple completed Phase 3 RCTs — including trials enrolling over 3,270 and 1,384 patients — establish Docetaxel as a standard-of-care chemotherapy backbone across HER2-positive, HER2-negative, and triple-negative breast cancer subtypes. This is not a novel drug repurposing but a validation of established international clinical practice; the "Proceed with Guardrails" recommendation reflects the need to address Australian-specific data gaps before formal local implementation documentation is complete.

**To proceed, the following is needed:**

- **TGA/ARTG verification:** Confirm current Docetaxel registration status on the ARTG, identify all registered brand names, and obtain TGA-approved indication text and dosing information
- **TGA-approved Product Information review:** Access and document the current Australian PI for Docetaxel, specifically for approved indications, contraindications, warnings (including hepatic impairment dose adjustment criteria), and premedication requirements
- **Mechanism of action data:** Retrieve formal DrugBank MOA documentation (DrugBank ID: DB01248) to complete the regulatory-level mechanistic rationale for clinical governance review
- **eviQ protocol alignment:** Confirm that intended use aligns with current eviQ-recommended Docetaxel breast cancer protocols (e.g., TC, TCH, AC→T, FEC-D, dose-dense regimens) and access standardised monitoring and dose modification tables
- **Safety monitoring plan:** Develop a structured toxicity management plan covering G-CSF prophylaxis criteria, dexamethasone premedication schedule, peripheral neuropathy assessment frequency, and fluid retention monitoring intervals
- **Institutional governance:** Confirm formulary status, confirm cytotoxic handling and preparation compliance at treating institutions, and ensure PBS/MBS funding pathway review where relevant

> **Secondary finding:** The TxGNN model also identified **Ewing sarcoma** (rank 2, score 99.90%, evidence level L2) and **rhabdomyosarcoma** (rank 8, evidence level L2) as secondary repurposing candidates, supported by completed Phase 2 trials of Gemcitabine+Docetaxel in paediatric sarcomas. These warrant separate evaluation reports if further development in the Australian context is of interest.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

