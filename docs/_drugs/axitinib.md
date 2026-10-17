---
layout: default
title: Axitinib
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Axitinib: predicted new indication Unclassified renal cell carcinoma (evidence level L5). Approved use: Renal cell carcinoma (clear cell and non-papillary subtypes)"
monitor_inn: "Axitinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Axitinib
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

# Axitinib: From Renal Cell Carcinoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Axitinib is an oral VEGFR1-3 tyrosine kinase inhibitor, originally used to treat renal cell carcinoma (including clear cell and non-papillary types).
The TxGNN model's top-ranked prediction is **unclassified renal cell carcinoma**, but no clinical trials or publications are available for that subtype, so it rests on the model score alone.
The strongest evidence in the data compiled for this report relates to the broader **renal carcinoma** group, which is the already-approved disease family and is supported by **multiple Phase 3 RCTs**. The next most notable candidates are TFE3-translocation RCC and collecting duct carcinoma, each with a small Phase 2 trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (clear cell and non-papillary subtypes); no approved indication text is available in the Australian licence data |
| Predicted New Indication | Unclassified renal cell carcinoma (rank 1) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 for the top-ranked prediction (model prediction only). Subtypes with more evidence: L2 (TFE3-translocation RCC, collecting duct carcinoma) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails only for the established renal carcinoma indication |

**Other predictions in the data (ranked by TxGNN score):**

| Rank | Predicted Disease | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Unclassified renal cell carcinoma | 99.90% | L5 | Hold |
| 2 | RCC with Xp11.2/TFE3 translocations | 99.90% | L2 | Research Question |
| 3 | RCC associated with neuroblastoma | 99.90% | L5 | Hold |
| 4 | Childhood kidney cell carcinoma | 99.87% | L4 | Hold |
| 5 | Liposarcoma | 99.87% | L4 | Research Question |
| 6 | Renal carcinoma | 99.85% | L1 | Proceed with Guardrails |
| 7 | Ovarian myxoid liposarcoma | 99.84% | L5 | Hold |
| 8 | Angiolipoma | 99.83% | L5 | Hold |
| 9 | Collecting duct carcinoma | 99.81% | L2 | Research Question |
| 10 | Familial spontaneous pneumothorax | 99.78% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, axitinib is a selective inhibitor of vascular endothelial growth factor receptors 1, 2 and 3 (VEGFR1-3). Clear cell RCC is typically driven by loss of the VHL gene, which leads to HIF accumulation and VEGF overexpression. This makes it a hypervascular tumour that is sensitive to antiangiogenic therapy.

The top-ranked predictions are histological subtypes of the disease family that axitinib is already used for. Antiangiogenic activity is therefore plausible. However, for unclassified RCC specifically, no trials or publications were found, so the high score is the only support.

Some other predictions are less convincing:
- **TFE3-translocation RCC and collecting duct carcinoma** are non-clear-cell subtypes where VEGF signalling and combination therapy with immune checkpoint inhibitors are plausible. Evidence is limited to small Phase 2 trials without results.
- **Liposarcoma** has only preclinical support (axitinib showed antiangiogenic and antitumour activity in myxoid liposarcoma cell lines).
- **Familial spontaneous pneumothorax** is likely a gene-disease association (FLCN/Birt-Hogg-Dubé syndrome, linked to kidney tumours) rather than a therapeutic rationale. Axitinib has no plausible mechanism here.
- **Angiolipoma** is a benign lesion, and the risk-benefit of a systemic TKI is unfavourable.

---

## Clinical Trial Evidence

**Top-ranked prediction (unclassified renal cell carcinoma):** Currently no related clinical trials registered.

**Most relevant trials for the closest subtypes and the broader renal carcinoma group** (up to 10 shown):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) (AXIS) | Phase 3 | Completed | 723 | Axitinib vs sorafenib as second-line therapy in metastatic RCC |
| [NCT02853331](https://clinicaltrials.gov/study/NCT02853331) (KEYNOTE-426) | Phase 3 | Completed | 861 | Pembrolizumab plus axitinib vs sunitinib, first-line advanced RCC |
| [NCT04394975](https://clinicaltrials.gov/study/NCT04394975) | Phase 3 | Completed | 421 | Toripalimab plus axitinib vs sunitinib, first-line RCC |
| [NCT06364631](https://clinicaltrials.gov/study/NCT06364631) | Phase 3 | Recruiting | 1250 | Platform trial comparing first-line strategies (ICI-ICI vs ICI-VEGFR TKI) in metastatic RCC |
| [NCT01693822](https://clinicaltrials.gov/study/NCT01693822) (A-PREDICT) | Phase 2 | Completed | 65 | Axitinib in metastatic RCC patients unsuitable for nephrectomy; efficacy, safety and biomarkers |
| [NCT00835978](https://clinicaltrials.gov/study/NCT00835978) | Phase 2 | Completed | 213 | Axitinib with or without dose titration in metastatic RCC |
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, not recruiting | 15 | Axitinib plus nivolumab vs nivolumab alone in TFE/translocation RCC (relevant to rank 2) |
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | Recruiting | 30 | Immune checkpoint inhibitors plus axitinib in previously treated collecting duct carcinoma (relevant to rank 9) |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) (NAXIVA) | Phase 2 | Completed | 24 | Neoadjuvant axitinib for venous tumour thrombus in clear cell RCC |
| [NCT05176288](https://clinicaltrials.gov/study/NCT05176288) | Phase 2 | Withdrawn | 0 | Avelumab, palbociclib and axitinib; no participants enrolled, so no evidence |

The TFE3 and collecting duct carcinoma trials are small, have no results provided, and cannot yet establish efficacy for those subtypes. Many additional registered trials (about 40 in total for renal carcinoma) are not listed here. No ANZCTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Top-ranked prediction (unclassified renal cell carcinoma):** Currently no related literature available.

**Key publications for the broader renal carcinoma group and subtypes** (up to 10 shown):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | RCT | N Engl J Med | Pembrolizumab plus axitinib vs sunitinib in previously untreated advanced RCC |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | RCT | N Engl J Med | Avelumab plus axitinib vs sunitinib in previously untreated advanced RCC (JAVELIN Renal 101) |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | RCT (5-year follow-up) | Nat Med | KEYNOTE-426 long-term survival and biomarker analyses |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | RCT (final analysis) | Ann Oncol | JAVELIN Renal 101 final analysis, including overall survival |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | RCT | Ann Oncol | RENOTORCH: toripalimab plus axitinib vs sunitinib, first-line advanced RCC |
| [33284113](https://pubmed.ncbi.nlm.nih.gov/33284113/) | 2020 | RCT (extended follow-up) | Lancet Oncol | KEYNOTE-426 extended follow-up of efficacy and safety |
| [26487541](https://pubmed.ncbi.nlm.nih.gov/26487541/) | 2015 | Review | Drugs | Axitinib in advanced RCC; AXIS trial showed significant PFS benefit |
| [35428926](https://pubmed.ncbi.nlm.nih.gov/35428926/) | 2022 | Review | Urologie | Collecting duct carcinoma; nivolumab plus axitinib reported to prolong survival in case-based evidence |
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | Preclinical | Sarcoma | Axitinib has antiangiogenic and antitumour activity in myxoid liposarcoma cell lines |
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | Treatment of advanced paediatric RCC; data for advanced disease are lacking |

The large RCTs relate mainly to clear cell RCC and are indirect evidence for the rarer subtypes. A paediatric case report (PMID 26279736) describes axitinib used in a child with malignant epithelioid angiomyolipoma, but it is not direct evidence for paediatric RCC.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 10539Q | Inlyta | Tablet 1 mg (oral) | Not available in the data compiled for this report |

Only one entry was identified. The approved indication text should be confirmed against the TGA-approved Product Information.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI. Based on the DDI and guardrail considerations below, blood pressure, bleeding and thromboembolic events warrant attention |
| Handling Protection | Please refer to the PI and local institutional policy for oral anticancer agents |

---

## Safety Considerations

**Drug Interactions** (100 interactions listed in the data compiled for this report; the main clinically relevant ones shown):

| Interacting Drug | Severity |
|------|------|
| Clarithromycin | Major |
| Dexamethasone | Major |
| Aprepitant | Moderate |
| Clotrimazole | Moderate |
| Miconazole | Moderate |
| Naltrexone | Moderate |

Many other listed interactions are minor, mostly acid-reducing agents and antacids (e.g. famotidine, ranitidine, rabeprazole, esomeprazole, lansoprazole, aluminium hydroxide, calcium carbonate, cimetidine, magnesium salts). Only 20 of the 100 interactions were available for review here.

Key warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these. The guardrail considerations noted in the evidence are hypertension, thromboembolic and haemorrhagic risks, and management of drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, unclassified renal cell carcinoma)
**Proceed with Guardrails** applies only to the established renal carcinoma indication, which is not true repurposing.

**Rationale:**
- Unclassified RCC has a very high TxGNN score (99.90%) but no trials or publications, so the evidence level is L5.
- The renal carcinoma group has L1 evidence (AXIS, KEYNOTE-426 and JAVELIN Renal 101), but this reflects the already-approved use of axitinib.
- TFE3-translocation RCC and collecting duct carcinoma are reasonable research questions, each supported only by a small, resultless Phase 2 trial.

**To proceed, the following is needed:**
- Subtype-specific clinical data for unclassified RCC (retrospective series or prospective studies)
- Results from the TFE3-translocation (NCT03595124) and collecting duct carcinoma (NCT06211114) trials
- Detailed mechanism of action data
- TGA Product Information review for warnings, contraindications and approved indication wording (a blocking data gap)
- A safety plan covering hypertension, thromboembolic and bleeding risks, and strong CYP3A4 inhibitor/inducer interactions (e.g. clarithromycin, dexamethasone)
- No further development is suggested for the benign or implausible candidates (angiolipoma, familial spontaneous pneumothorax) without a mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

