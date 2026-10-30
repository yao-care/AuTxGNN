---
layout: default
title: Vismodegib
parent: Model Prediction Only (L5)
nav_order: 782
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Vismodegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
description: "Vismodegib: predicted new indication Medulloblastoma with extensive nodularity (evidence level L5). Approved use: Not recorded in the local data"
---

# Vismodegib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Vismodegib: Medulloblastoma with extensive nodularity
{: .text-alpha }

## One-Sentence Summary

Vismodegib is an oral Hedgehog pathway (Smoothened) inhibitor, originally used for basal cell carcinoma and related skin cancers.
The TxGNN model's top-ranked prediction is **medulloblastoma with extensive nodularity**, but it has no supporting trials or literature. The best-supported prediction is **skin cancer** (rank 9), with **12 clinical trials** and **20 publications**. This largely overlaps with the existing basal cell carcinoma indication, so it is not a true repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 for medulloblastoma with extensive nodularity; L1 for skin cancer (to be confirmed, see below) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Medulloblastoma with extensive nodularity: Hold. Skin cancer: Proceed with Guardrails (labelled settings only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Vismodegib is, however, a known Smoothened (SMO) inhibitor. It blocks aberrant Hedgehog signalling, which drives basal cell carcinoma through PTCH1 loss of function.

**Top-ranked prediction (medulloblastoma with extensive nodularity):** This tumour is closely associated with the SHH medulloblastoma subgroup, in which Hedgehog activation (PTCH1/SUFU mutations) drives tumour growth. The mechanism is plausible, particularly for PTCH1-mutant tumours. SUFU-mutant tumours act downstream of SMO and would be expected to be resistant. No trials or literature were found for this entity, so support rests on the model prediction alone. Paediatric use also raises a concern about premature growth plate fusion.


**Xeroderma pigmentosum (rank 2):** Two case reports describe vismodegib clearing BCCs in patients with xeroderma pigmentosum, including an 8-year-old child. This is indirect evidence for BCC in the setting of XP, not for treating XP itself.

**Other predictions (ranks 3 to 8 and 10):** These include annular epidermolytic ichthyosis, epidermolysis bullosa simplex with mottled pigmentation, prostate cancer/brain cancer susceptibility, Brenner tumour, cutaneous adenocystic carcinoma, prostate leiomyoma and benign neoplasm of sweat gland. None has trials or literature, and several have no plausible Hedgehog link. All are Hold.

---

## Clinical Trial Evidence


| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01835626](https://clinicaltrials.gov/study/NCT01835626) | Phase 2 | Completed | 24 | Safety and tolerability of radiotherapy plus vismodegib in locally advanced head and neck BCC |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A (registry) | Recruiting | 80 | Dutch real-world registry of vismodegib and sonidegib in advanced and multiple BCC |
| [NCT05651828](https://clinicaltrials.gov/study/NCT05651828) | Early Phase 1 | Recruiting | 34 | Four dosing schedules (personalised intermittent, fixed intermittent, continuous) in advanced BCC |
| [NCT01631331](https://clinicaltrials.gov/study/NCT01631331) | Early Phase 1 | Completed | 15 | Pilot of off-label vismodegib as an adjuvant to surgery for sporadic BCC |
| [NCT01543581](https://clinicaltrials.gov/study/NCT01543581) | Phase 2 | Completed | 3 | Placebo-controlled study before Mohs surgery; enrolment too small for conclusions |
| [NCT02690948](https://clinicaltrials.gov/study/NCT02690948) | Phase 1/2 | Completed | 16 | Pembrolizumab with or without vismodegib in unresectable or metastatic BCC |
| [NCT02694224](https://clinicaltrials.gov/study/NCT02694224) | Phase 2 | Unknown | 40 | Vismodegib added to neoadjuvant chemotherapy in triple-negative breast cancer (not skin cancer) |
| [NCT06357988](https://clinicaltrials.gov/study/NCT06357988) | Phase 2 | Active, not recruiting | 34 | NCI-MATCH subprotocol T: vismodegib in non-BCC tumours with SMO or PTCH1 mutations |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6452 | NCI-MATCH master protocol; vismodegib is one of many arms |
| [NCT01071564](https://clinicaltrials.gov/study/NCT01071564) | Phase 1 | Terminated | 13 | Vismodegib plus a Notch inhibitor in advanced breast cancer (not skin cancer) |

No ANZCTR identifiers were found in the data compiled for this report. Two further trials (NCT03878524 and NCT05238831) are precision-oncology platform studies that were terminated or withdrawn and are uninformative.

---

## Literature Evidence

Up to 10 publications are shown; guidelines and reviews are prioritised, with the xeroderma pigmentosum case reports included. No RCTs were supplied.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Guideline | Eur J Cancer | Updated European interdisciplinary BCC guideline; categorises BCC as "easy-to-treat" or "difficult-to-treat" |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Guideline | Eur J Cancer | European consensus guideline on BCC diagnosis and treatment |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Review | Cell | Hedgehog inhibition; vismodegib and sonidegib approved for locally advanced BCC, vismodegib also for metastatic BCC |
| [22679179](https://pubmed.ncbi.nlm.nih.gov/22679179/) | 2012 | Review | Clin Cancer Res | FDA approval based mainly on a non-randomised parallel-cohort Phase 2 study |
| [22653209](https://pubmed.ncbi.nlm.nih.gov/22653209/) | 2012 | Review | Nat Rev Drug Discov | Vismodegib as an oral Hedgehog inhibitor for advanced BCC |
| [24756807](https://pubmed.ncbi.nlm.nih.gov/24756807/) | 2014 | Review | Recent Results Cancer Res | Vismodegib binds SMO; Hedgehog dysregulation also seen in medulloblastoma and other cancers |
| [23719880](https://pubmed.ncbi.nlm.nih.gov/23719880/) | 2013 | Review | Am J Health Syst Pharm | Pharmacology, efficacy, adverse effects, cost and place in therapy |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | Comprehensive review of BCC biology and resistance to systemic treatments |
| [28297142](https://pubmed.ncbi.nlm.nih.gov/28297142/) | 2017 | Case report | Pediatr Dermatol | Vismodegib 150 mg/day cleared a nasal-tip BCC in an 8-year-old with xeroderma pigmentosum |
| [30178564](https://pubmed.ncbi.nlm.nih.gov/30178564/) | 2018 | Case report | Pediatr Dermatol | Multiple BCCs in XP: 61% reduction in lesion diameter at 16.5 months; one lesion later progressed |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 11070P | Erivedge | Capsule 150 mg (oral) | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / Smoothened inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Given the teratogenic risk, pregnancy status and contraception are key monitoring points |
| Handling Protection | Please refer to the PI and local handling requirements |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

- **Known concerns noted in the evidence review:** embryo-fetal toxicity (teratogenicity); common adverse events including muscle spasms, alopecia, dysgeusia and weight loss; and a possible risk of premature growth plate fusion in children.
- **Drug interactions:** 56 interactions were identified. One is rated **Moderate**: clarithromycin. The rest are rated Minor and are mainly acid-suppressing agents and antacids, including H2 blockers (famotidine, ranitidine, cimetidine, nizatidine), proton pump inhibitors (omeprazole, esomeprazole, pantoprazole, lansoprazole, rabeprazole, dexlansoprazole) and antacids (aluminium, magnesium and calcium salts, sodium bicarbonate, sodium citrate).

---

## Conclusion and Next Steps

**Decision: Hold for medulloblastoma with extensive nodularity (top-ranked); Proceed with Guardrails for skin cancer (labelled settings only)**

**Rationale:**
- The top-ranked prediction has a plausible mechanism (SHH-subgroup tumours) but no trials or literature, so it rests on model prediction alone (L5).

**To proceed, the following is needed:**
- Australian Product Information, including approved indication text, warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- For medulloblastoma: evidence of activity in PTCH1-mutant versus SUFU-mutant tumours, plus a paediatric risk assessment (growth plate fusion)
- Confirmation of the registration-trial evidence behind the L1 grade
- Embryo-fetal toxicity risk management for any new-setting use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

