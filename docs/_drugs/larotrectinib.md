---
layout: default
title: Larotrectinib
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Larotrectinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
---

# Larotrectinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Larotrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Larotrectinib (Vitrakvi) is a selective TRK inhibitor registered in Australia, with an approved indication text that is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but support is indirect: **1 clinical trial** (a large precision-oncology basket study) and **2 publications** (a review and a mechanistic case report), none specific to MEN.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the ARTG indication text is blank) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 (indirect; no MEN-specific studies) |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, larotrectinib is a selective TRK inhibitor used on a tumour-agnostic basis for NTRK fusion-positive solid tumours. Its efficacy is confined to tumours driven by NTRK fusions, and mechanistically it may be applicable to a new indication only where such a driver is present.

MEN is driven mainly by RET alterations (MEN2) or MEN1 alterations, not NTRK fusions, so the direct mechanistic link is weak. The only plausible connections are:

- NTRK-fusion-positive tumours that arise in endocrine tissue, such as thyroid.
- The RET-pathway literature on kinase inhibitor resistance, which is relevant to the wider field but does not involve larotrectinib.

The high TxGNN score should therefore be read as a computational signal, not as evidence of clinical benefit in MEN.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | NCI-MATCH: genetically directed treatment in advanced, refractory solid tumours, lymphomas and myeloma. Larotrectinib's relevance depends on an NTRK fusion, not on a MEN diagnosis, so this is indirect support only. |

No ANZCTR trials were identified in the compiled data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Kinase inhibitors for advanced thyroid cancer, including mutation-specific approvals. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/Mechanistic | NPJ Precision Oncology | Off-target resistance to selective RET inhibition in a patient with medullary thyroid carcinoma. Not about larotrectinib. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13027P | Vitrakvi | Capsule 25 mg (as sulfate) | Not available in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRK kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the PI warnings and precautions |
| Monitoring Items | Please refer to the PI warnings and precautions |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policies |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug Interactions:** The interaction screen returned 100 interacting drugs; the first 20 returned are summarised here. Larotrectinib is primarily metabolised via CYP3A4, which is consistent with several of these interactions.

- **Major:** Clarithromycin
- **Moderate:** Hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide (including nasal), pioglitazone, saxagliptin, aprepitant, omeprazole, cimetidine, dolasetron, dronabinol, eliglustat, naldemedine, naltrexone, cisapride, clotrimazole
- **Minor:** Naloxegol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and indirect evidence: a basket trial that does not test MEN specifically, and literature on thyroid cancer and RET inhibitors. There is no clear mechanistic link between TRK inhibition and the main drivers of MEN. Larotrectinib's established activity is limited to NTRK fusion-positive tumours.

**To proceed, the following is needed:**
- Evidence of NTRK fusions in MEN-associated tumours, to define whether a biomarker-selected subgroup exists
- Case series or trial data on larotrectinib in endocrine tumours
- The approved indication text and the safety sections of the PI (warnings, contraindications)
- Detailed mechanism of action data
- A review of the CYP3A4-related interactions, particularly with clarithromycin, if a clinical pathway is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

