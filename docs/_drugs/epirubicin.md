---
layout: default
title: Epirubicin
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-04
monitor_inn: "Epirubicin"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
description: "Epirubicin: predicted new indication Primary pulmonary lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Epirubicin
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

## Epirubicin: Primary pulmonary lymphoma
{: .text-alpha }

## One-Sentence Summary

Epirubicin is an anthracycline cytotoxic chemotherapy agent that damages DNA by inhibiting topoisomerase II. The TxGNN model predicts it may be useful in **primary pulmonary lymphoma** (score 0.9971). No clinical trials are registered for this use, and none of the retrieved publications tests epirubicin in this disease, so the evidence level is **L5 (model prediction only)**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Epirubicin is an anthracycline, the 4' epimer of doxorubicin. Anthracyclines intercalate into DNA and poison topoisomerase II, which is most damaging to rapidly dividing cells. Epirubicin has been used alone or in combination in a range of malignancies, and it appears in some lymphoma regimens, such as CEOP and VEBEP.

Lymphomas are generally chemosensitive, and anthracycline-containing regimens are the usual backbone for aggressive B-cell lymphoma. This is probably why the model links epirubicin to a lymphoma arising in the lung. However, the standard anthracycline in those regimens is doxorubicin (as in R-CHOP). The retrieved literature does not isolate epirubicin's contribution in pulmonary lymphoma. The prediction is therefore a plausible class-level extrapolation, not an evidence-based finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The retrieved publications are indirect. They are case reports, small retrospective series, and a general drug review. None tests epirubicin in primary pulmonary lymphoma.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | General review of epirubicin's pharmacology and use in cancer chemotherapy. It reports efficacy broadly comparable to doxorubicin-containing regimens in several malignancies. It does not address pulmonary lymphoma. |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Retrospective cohort | Annals of Hematology | Retrospective study of 117 patients with diffuse large B-cell lymphoma treated first-line with Pola-R-CHP, an anthracycline-containing regimen. This is indirect evidence for the anthracycline class, not epirubicin. |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Single-centre analysis of clinical features and prognostic factors in primary extranodal diffuse large B-cell lymphoma in the rituximab era. It is relevant to the disease setting but is not an epirubicin study. |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Pilot cohort | Cancer Journal | Pilot study of the intensive VEBEP regimen plus involved-field radiotherapy in advanced Hodgkin's disease. The regimen contains epirubicin, but the disease is different. |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Revista de Investigacion Clinica | Case of non-Hodgkin lymphoma involving the lung with haemorrhagic pleural effusion. It describes the diagnostic work-up and does not provide evidence for epirubicin. |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report and review | Translational Cancer Research | Case report of misdiagnosed primary MALT lymphoma of the pleura. It is relevant to thoracic lymphoma diagnosis, not to epirubicin therapy. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4375G | Epirubicin Accord | Solution for injection containing epirubicin hydrochloride 200 mg in 100 mL | Not stated in the data compiled for this report |

## Cytotoxicity

The following is general class information for anthracyclines. Please refer to the Product Information (PI) for product-specific details.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline) |
| Myelosuppression Risk | High (neutropenia is dose-limiting) |
| Emetogenicity Classification | Moderate to high, depending on dose |
| Monitoring Items | Full blood count with differential, liver function, renal function, and cardiac function (for example left ventricular ejection fraction) before and during treatment |
| Handling Protection | Must follow cytotoxic drug handling regulations, including protective equipment and safe disposal |

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 recorded interactions. Examples include:
  - **Major**: cimetidine and dolasetron.
  - **Moderate**: famotidine, clarithromycin, levofloxacin, bupropion, loperamide, pioglitazone, acarbose, minocycline, palonosetron, naltrexone, and several bowel-preparation products.
  - **Minor**: metronidazole.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (evidence level L5). There are no registered trials and no study testing epirubicin in primary pulmonary lymphoma. Doxorubicin-based regimens already serve as the standard anthracycline backbone in lymphoma.

**To proceed, the following is needed:**
- Direct clinical evidence, such as trials or well-documented cohorts of epirubicin-containing regimens in primary pulmonary lymphoma, showing a benefit over standard doxorubicin-based therapy
- Detailed mechanism-of-action data
- TGA Product Information warnings and contraindications, to support a safety review
- A cardiac and haematological monitoring plan suited to lymphoma populations

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

