---
layout: default
title: Sonidegib
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Sonidegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "trichothiodystrophy photosensitive", "cutaneous adenocystic carcinoma", "benign neoplasm of sweat gland", "eccrine carcinoma", "obsolete cataract, microcephaly, failure to thrive, kyphoscoliosis syndrome"]
description: "Sonidegib: predicted new indication Medulloblastoma with extensive nodularity (evidence level L5). Approved use: Not recorded in the local data"
---

# Sonidegib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Sonidegib: Medulloblastoma with extensive nodularity
{: .text-alpha }

## One-Sentence Summary

Sonidegib is an oral Hedgehog pathway inhibitor, originally used to treat basal cell carcinoma and related skin cancers.
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**, with **6 clinical trials** and **20 publications** currently supporting this direction.
Most of this evidence relates to basal cell carcinoma (BCC), which overlaps with the approved use, so this is a narrow extension rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 by the strict trial-phase definition (one completed randomised Phase 2 trial, no Phase 3 RCT). The data compiled for this report labels it L1 only if regulatory approval is treated as confirmatory evidence |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (restricted to BCC) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sonidegib is a Smoothened (SMO) receptor antagonist. It blocks the Hedgehog signalling pathway, which is aberrantly activated in the majority of basal cell carcinomas.


Other predictions were also generated. Only two have any supporting evidence:
- **Xeroderma pigmentosum**: a single 2026 case report of sonidegib for multiple BCCs in an XP patient. The benefit is indirect, through treating BCC rather than the underlying DNA repair defect.
- **Medulloblastoma with extensive nodularity**: biologically plausible, because SHH-subgroup medulloblastoma is driven by Hedgehog signalling. However, no trials or literature were found. Concerns include resistance from downstream mutations and growth-plate effects in children.

The remaining predictions (for example ichthyosis, epidermolysis bullosa simplex and benign sweat gland neoplasm) have no apparent mechanistic link and likely reflect network proximity to other skin conditions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01327053](https://clinicaltrials.gov/study/NCT01327053) | Phase 2 | Completed | 230 | Randomised, double-blind comparison of two sonidegib (LDE225) doses in locally advanced or metastatic BCC; efficacy and safety |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | Recruiting | 80 | Dutch prospective registry of vismodegib and sonidegib in advanced and multiple BCC; real-world data |
| [NCT03534947](https://clinicaltrials.gov/study/NCT03534947) | Phase 2 | Completed | 16 | Pilot of 12 weeks of neoadjuvant sonidegib before surgery or imiquimod for BCC in cosmetically sensitive sites |
| [NCT02303041](https://clinicaltrials.gov/study/NCT02303041) | Phase 2 | Terminated | 10 | Pilot of sonidegib plus buparlisib in advanced BCC; terminated early, limited interpretability |
| [NCT04007744](https://clinicaltrials.gov/study/NCT04007744) | Phase 1 | Active, not recruiting | 36 | Sonidegib plus pembrolizumab in advanced solid tumours; dose-finding, not skin-cancer specific |
| [NCT01757327](https://clinicaltrials.gov/study/NCT01757327) | Phase 2 | Withdrawn | 0 | Sonidegib on disseminated tumour cells in early breast cancer; never enrolled, provides no evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Guideline | Eur J Cancer | Updated European consensus guideline on BCC diagnosis and treatment, classifying BCC as "easy-to-treat" or "difficult-to-treat" |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Guideline | Eur J Cancer | Earlier European interdisciplinary BCC guideline |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Review | Cell | Hedgehog pathway is aberrantly activated in most BCC; vismodegib and sonidegib are SMO inhibitors approved for locally advanced BCC |
| [26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/) | 2015 | Review | Drugs | Sonidegib (Odomzo) first global approval profile; oral SMO antagonist |
| [33194718](https://pubmed.ncbi.nlm.nih.gov/33194718/) | 2020 | Review | Front Oncol | Sonidegib for advanced BCC |
| [33888008](https://pubmed.ncbi.nlm.nih.gov/33888008/) | 2021 | Review | Expert Opin Drug Saf | Expert opinion on sonidegib efficacy, safety and tolerability |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | Comprehensive BCC review covering molecular features and resistance to systemic treatment |
| [39062023](https://pubmed.ncbi.nlm.nih.gov/39062023/) | 2024 | Review | Biomedicines | Advanced and metastatic non-melanoma skin cancer: risk factors and treatment options |
| [33725197](https://pubmed.ncbi.nlm.nih.gov/33725197/) | 2021 | Review | Curr Treat Options Oncol | Neoadjuvant approaches in non-melanoma skin cancer; Hedgehog inhibitors are very effective in locally advanced or multiple BCC |
| [41862093](https://pubmed.ncbi.nlm.nih.gov/41862093/) | 2026 | Case report | Actas Dermosifiliogr | Sonidegib for multiple BCCs in a patient with xeroderma pigmentosum (relevant to the rank 2 prediction) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11304Y | Odomzo | Capsule 200 mg (oral) | Not listed in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / SMO inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Creatine kinase (CK) and musculoskeletal symptoms (per the guardrails noted in the data compiled for this report); otherwise refer to the PI |
| Handling Protection | Please refer to the PI and local institutional policy for handling of oral anticancer agents |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the DDI screen. The first 20 reviewed include:
  - **Major**: aprepitant, dexamethasone, clarithromycin, clotrimazole, cobicistat
  - **Moderate**: cimetidine, metreleptin, miconazole, troglitazone, deferasirox
  - **Minor**: acid-suppressing agents (famotidine, ranitidine, nizatidine and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole)
- **Guardrails noted in the data compiled for this report**: monitor for musculoskeletal toxicity (CK elevation) and avoid use in pregnancy because of embryo-fetal toxicity. Irreversible growth-plate effects are a concern in paediatric patients.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A randomised, double-blind Phase 2 trial (n=230) and consensus guidelines support sonidegib in advanced BCC, and the drug is already marketed in Australia. This is a confirmation of an existing use rather than a new indication. It does not support use in non-BCC skin cancers, and the other predicted indications remain at Hold or research-question level.

**To proceed, the following is needed:**
- TGA Product Information warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- The approved indication wording for ARTG 11304Y, to confirm the extent of overlap with BCC
- A restriction to BCC, with CK and musculoskeletal monitoring and pregnancy avoidance
- Prospective data before considering xeroderma pigmentosum or medulloblastoma. Both currently rest on a single case report or on no clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

