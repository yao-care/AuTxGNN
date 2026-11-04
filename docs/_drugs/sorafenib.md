---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 685
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-04
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor marketed in Australia as Nexavar. The TxGNN model predicts it may be useful for **liposarcoma (liposarcoma)**, but no study has tested sorafenib specifically in liposarcoma. The available support is **1 Phase 2 trial** and **a small set of publications** covering soft tissue sarcoma in general, so the evidence level is **L5**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, sorafenib inhibits RAF/MEK/ERK signalling and the VEGFR, PDGFR and c-KIT receptor tyrosine kinases. These pathways drive angiogenesis and cell proliferation in soft tissue sarcomas.

Preclinical work showed that sorafenib inhibited MAPK signalling and growth in malignant peripheral nerve sheath tumour cells and in dedifferentiated liposarcoma cell lines (PMID 18413802). This offers a plausible mechanistic link, but it is laboratory evidence only.

Important caveats: the clinical data concern advanced soft tissue sarcoma as a group, and liposarcoma-specific efficacy cannot be separated out. Liposarcoma is also historically less responsive to this kind of therapy than angiosarcoma or other vascular subtypes. No cited study directly tests sorafenib in liposarcoma, so the prediction remains computational.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) in advanced soft tissue sarcomas. Mixed sarcoma subtypes, so liposarcoma-specific results cannot be isolated from the registry record. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib in advanced soft tissue sarcomas; a multitargeted inhibitor of RAF, VEGFR1–3, PDGF-B, FLT3 and c-KIT. Not specific to liposarcoma. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven treatment of soft tissue sarcomas; trabectedin is highlighted for liposarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Treatment of soft tissue sarcomas by histological subtype. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signalling in nerve sheath tumour and dedifferentiated liposarcoma cell lines. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models; response to PI3K pathway inhibition (not sorafenib). |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Sarcoma patient-derived xenograft models and palbociclib combinations (not sorafenib-specific). |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 10226F | Nexavar | Tablet 200 mg (as tosilate) | Not available in the data compiled |

One valid single-ingredient licence is recorded in the local data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; routine full blood count, liver and renal function, and blood pressure monitoring is generally relevant |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Examples include a major interaction with dolasetron, and moderate interactions with clarithromycin, levofloxacin, dexamethasone, famotidine, loperamide, palonosetron, naltrexone and several laxatives or bowel preparations (for example bisacodyl, lactulose, sodium sulfate).

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9982), but no study tests sorafenib in liposarcoma. The only clinical data concern mixed soft tissue sarcoma populations, and the preclinical data are limited, so the evidence level is L5. Liposarcoma subtypes also have more specifically active established options, such as trabectedin.

**To proceed, the following is needed:**
- Liposarcoma-specific clinical data, for example subgroup results from the soft tissue sarcoma trials (NCT00217620 and the SWOG S0505 study)
- Detailed mechanism of action data for sorafenib
- Review of the TGA Product Information for warnings and contraindications
- A clinical review of the interaction burden, particularly QT-prolonging combinations

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

