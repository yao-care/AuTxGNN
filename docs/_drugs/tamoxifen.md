---
layout: default
title: Tamoxifen
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tamoxifen: predicted new indication Mammary Paget disease (evidence level L5). Approved use: Female breast carcinoma"
monitor_inn: "Tamoxifen"
predicted_indications: ["mammary Paget disease", "Ehrlich tumor carcinoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Tamoxifen
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

# Tamoxifen: From Breast Carcinoma to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is an oral selective oestrogen receptor modulator, originally used to treat breast carcinoma (female breast carcinoma, invasive ductal carcinoma and ductal adenocarcinoma).
The TxGNN model predicts it may be effective for **mammary Paget disease**, but the supporting evidence is thin: **1 clinical trial** (not testing tamoxifen for this condition) and **10 publications**, mostly case reports and surgical series.
Other predicted breast conditions, particularly **breast carcinoma in situ** and **oestrogen-receptor positive breast cancer**, have much stronger Phase 3 support. These are largely established uses of tamoxifen rather than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Female breast carcinoma; invasive ductal breast carcinoma; breast ductal adenocarcinoma (from the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | Mammary Paget disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 (for mammary Paget disease) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

**Other predicted indications in the data compiled for this report:**

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Breast carcinoma in situ | 99.67% | L1 | Proceed with Guardrails |
| Oestrogen-receptor positive breast cancer | 99.67% | L1 | Proceed with Guardrails |
| Hormone-resistant breast carcinoma | 99.67% | L3 | Research question |
| Invasive tubular breast carcinoma | 99.67% | L4 | Hold |
| Intraductal cribriform breast adenocarcinoma | 99.69% | L5 | Hold |
| Basal-like breast carcinoma | 99.68% | L5 | Hold |
| Sebaceous breast carcinoma | 99.67% | L5 | Hold |
| Ehrlich tumour carcinoma (mouse model) | 99.67% | L5 | Hold |
| Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.67% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tamoxifen is a selective oestrogen receptor modulator that blocks oestrogen receptors in breast tissue. Its efficacy in hormone receptor-positive breast cancer is well established.

Mammary Paget disease is usually associated with underlying ductal carcinoma in situ or invasive breast cancer, which is often hormone receptor-positive. In that setting, oestrogen receptor antagonism is plausible. One case report describes a response of hormone receptor-positive extramammary Paget disease to tamoxifen, and a case of extensive Paget disease of the nipple responded to tamoxifen alongside radiotherapy.

However, there is no direct trial evidence of tamoxifen efficacy in Paget disease itself. The high TxGNN score likely reflects the drug's existing breast cancer indications rather than specific benefit in this condition.

For context, the strongest evidence in this dataset applies to related, more established conditions:
- **Breast carcinoma in situ (DCIS):** randomised trials, including the placebo-controlled TAM-01 low-dose tamoxifen trial, support recurrence reduction.
- **Oestrogen-receptor positive breast cancer:** this matches the drug's original use and is not novel repurposing.

---

## Clinical Trial Evidence

Trial evidence for mammary Paget disease itself is limited to one trial, which does not test tamoxifen efficacy in this condition.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Medroxyprogesterone vs observation to prevent endometrial pathology in postmenopausal women taking tamoxifen (including those with Paget disease of the nipple). It addresses a tamoxifen adverse effect, not efficacy. |

**Selected trials for the better-supported related indication, breast carcinoma in situ:**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06982313](https://clinicaltrials.gov/study/NCT06982313) | N/A | Completed | 1545 | Long-term follow-up of TAM-01 (low-dose tamoxifen) with pooled analysis in DCIS and high-risk lesions |
| [NCT01357772](https://clinicaltrials.gov/study/NCT01357772) | Phase 3 | Active, not recruiting | 500 | Placebo-controlled low-dose tamoxifen (5 mg/day) in breast intraepithelial neoplasia |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Completed | 2980 | IBIS-II DCIS: tamoxifen vs anastrozole after surgery |
| [NCT00053898](https://clinicaltrials.gov/study/NCT00053898) | Phase 3 | Completed | 3104 | Anastrozole vs tamoxifen in postmenopausal DCIS after lumpectomy and radiotherapy |
| [NCT00003857](https://clinicaltrials.gov/study/NCT00003857) | Phase 3 | Completed | 636 | Tamoxifen alone vs tamoxifen plus radiotherapy in good-risk DCIS |
| [NCT04046159](https://clinicaltrials.gov/study/NCT04046159) | Phase 3 | Unknown | 810 | Radiotherapy vs low-dose tamoxifen after breast-conserving surgery in low-risk ER-positive DCIS |
| [NCT06671912](https://clinicaltrials.gov/study/NCT06671912) | Phase 3 | Suspended | 1556 | LoTam: low-dose tamoxifen vs usual hormonal therapy in molecular low-risk early breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-analysis (cohort) | Breast Care | Local recurrence after mastectomy vs breast-conserving surgery for Paget disease; total recurrence 20-40% |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Review | Br J Surg | 48 women with Paget disease of the nipple; mostly treated surgically, tamoxifen in one case |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case report | Breast | Extensive nipple Paget disease; response to tamoxifen, then radiotherapy |
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case report | Invest New Drugs | Hormone receptor-positive metastatic extramammary Paget disease treated successfully with tamoxifen |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Case report/series | Clin Breast Cancer | Paget disease as local recurrence after breast-conserving treatment |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case report | Am Surg | Paget disease of the male breast; review of 32 cases |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case report | Arch Gynecol Obstet | Synchronous vulvar and breast Paget disease with underlying cancer |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case report | Surg Today | Synchronous bilateral breast cancer with Paget disease |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Cohort | Niger J Clin Pract | 8 of 240 breast cancer patients had nipple-areola Paget disease |
| [18288984](https://pubmed.ncbi.nlm.nih.gov/18288984/) | 2008 | Review | Curr Med Chem | Pharmacotherapies for bone loss; only tangentially relevant |

**Key supporting RCTs for breast carcinoma in situ:**
- [36917758](https://pubmed.ncbi.nlm.nih.gov/36917758/) (2023, J Clin Oncol): 10-year TAM-01 results, low-dose tamoxifen to prevent recurrence in breast intraepithelial neoplasia.
- [30973790](https://pubmed.ncbi.nlm.nih.gov/30973790/) (2019, J Clin Oncol): TAM-01 primary results, low-dose tamoxifen to prevent local and contralateral recurrence.
- [23076938](https://pubmed.ncbi.nlm.nih.gov/23076938/) (2012, Cochrane): postoperative tamoxifen for DCIS.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10911G | Nolvadex-D | Tablet 20 mg (as citrate) | Not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (selective oestrogen receptor modulator), not a conventional cytotoxic |
| Myelosuppression Risk | Low; however, thrombocytopenia and leukopenia appear among the knowledge-graph contraindication associations, so periodic FBC is reasonable |
| Emetogenicity Classification | Low |
| Monitoring Items | FBC, liver function, calcium, gynaecological review (endometrial symptoms), thromboembolic symptoms |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

- **Knowledge-graph contraindication associations** (not label text; verify against the PI): thrombocytopenia, leukopenia, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, stroke and cerebrovascular disorders, cerebral infarction, pulmonary embolism, vision disorders and blindness.
- **Drug interactions:** 100 interactions were identified. Examples of **major** interactions include bupropion, cimetidine, lorcaserin, dolasetron, eliglustat, cisapride, fenfluramine and dexfenfluramine. Examples of **moderate** interactions include famotidine, loperamide, aprepitant, dexamethasone, clarithromycin, granisetron and levofloxacin. Minor: fidaxomicin. Several major interactions relate to CYP2D6 inhibition or QT prolongation.
- **Other considerations noted in the data:** endometrial and thromboembolic risk, CYP2D6 metabolism, and endocrine resistance mechanisms.

---

## Conclusion and Next Steps

**Decision: Hold** (for mammary Paget disease)

**Rationale:**
Evidence for tamoxifen in mammary Paget disease is limited to case reports and surgical series, with no trial testing tamoxifen efficacy in this condition (L4). The high TxGNN score appears to reflect the drug's general breast cancer associations.

By contrast, **breast carcinoma in situ** and **oestrogen-receptor positive breast cancer** are L1 with a decision of **Proceed with Guardrails**. These are established uses of tamoxifen, not novel repurposing. Guardrails: restrict to hormone receptor-positive disease, individualise by risk and benefit, and monitor for endometrial and thromboembolic events.

**To proceed, the following is needed:**
- Hormone receptor status data and prospective or registry evidence for tamoxifen specifically in mammary Paget disease
- Mechanism of action data and the TGA Product Information (warnings, contraindications, approved indications) for ARTG 10911G
- A safety monitoring plan covering endometrial and thromboembolic risk, CYP2D6 status and interacting medicines
- Review of the other predicted indications (rated L5) as low priority, noting that Ehrlich tumour carcinoma is a mouse model and not a human indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

