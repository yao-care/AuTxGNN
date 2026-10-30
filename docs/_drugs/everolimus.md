---
layout: default
title: Everolimus
parent: High Evidence (L1-L2)
nav_order: 280
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Everolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
description: "Everolimus: predicted new indication Liposarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Everolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

## Everolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Everolimus is an oral mTOR inhibitor, originally used for renal cell carcinoma and breast carcinoma, and also in tuberous sclerosis-related conditions such as kidney angiomyolipoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a Phase 2 combination study) and **4 publications** compiled for this report. Only one of those publications reports the trial directly, and the others are preclinical or review articles.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L2 (one Phase 2 trial, single-arm and combination, not yet completed) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, everolimus inhibits mTORC1, a central regulator of cell growth and survival. Its efficacy in renal cell carcinoma and breast carcinoma is established, so it is mechanistically plausible in other tumours that depend on the PI3K/AKT/mTOR pathway.

Dedifferentiated liposarcoma is characterised by CDK4/MDM2 amplification, and PI3K/AKT/mTOR activation is a recognised co-driver. Ribociclib inhibits CDK4/6 and everolimus inhibits mTORC1, so combining them may block two complementary proliferation and survival pathways. Laboratory models have shown synergistic growth inhibition with this combination.

This rationale is coherent but unproven. The available clinical data come from a combination regimen, so the contribution of everolimus alone cannot be isolated.

Other top-ranked predictions are mostly sarcoma subtypes (rhabdomyosarcoma variants, dermatofibrosarcoma protuberans). Two are renal cell carcinoma subtypes, which overlap with the existing approved indication class and are not clear new repurposing signals. Rhabdomyosarcoma (rank 7) is the only other prediction with clinical trial data, from early-phase paediatric studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib plus everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after at least one prior systemic therapy. Two-centre, single-arm design assessing anti-tumour activity. Estimated completion December 2026. |

No ANZCTR trial identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial report | Clin Cancer Res | Ribociclib plus everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma. The pairing is based on CDK4/6 and mTOR targeting, with synergy shown in tumour models. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Patient-derived xenograft models of sarcoma used to identify combinations with the CDK inhibitor palbociclib. Not everolimus-specific. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin combined with other anticancer agents in xenograft models. Not everolimus-specific. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclinical | Oncogene | The XPO1 inhibitor KPT-330 (selinexor) disrupts transcriptional circuitry in dedifferentiated liposarcoma. Not everolimus-specific. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10131F | Afinitor | Tablet 5 mg (oral) | Indication text not available in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph links everolimus to cytopenias (see Safety Considerations). |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Full blood count, liver and renal function, glucose and lipids (inferred from the knowledge graph contraindication signals; confirm against the PI) |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

---

## Safety Considerations

The Product Information was not available in the data compiled for this report, so please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

- **Knowledge graph contraindication signals** (not label text): liver failure and liver disease, kidney disease, thrombocytopenia, neutropenia, leukopenia, anaemia, hyperglycaemia and diabetes, hypertriglyceridaemia and hyperlipidaemia, interstitial lung disease, stomatitis, congestive heart failure, pericardial effusion, haemolytic-uraemic syndrome, and lymphoma. These indicate areas for caution and baseline assessment, not confirmed contraindications.
- **Drug interactions:** 100 interactions were identified. The main ones listed are:
  - **Major:** amphotericin B (including lipid complex), aprepitant, dexamethasone, clarithromycin.
  - **Moderate:** several antidiabetic agents (metformin, acarbose, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamide, albiglutide, dulaglutide), cimetidine, eliglustat and eluxadoline.
  - **Minor:** zinc sulfate.

---

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The only direct evidence is one unfinished, single-arm Phase 2 combination trial in dedifferentiated liposarcoma. Everolimus-alone efficacy cannot be separated out, and the other predictions rely mostly on the model score. The prediction is mechanistically sensible, so it is worth monitoring rather than acting on.

**To proceed, the following is needed:**
- Final results of NCT03114527 and, ideally, a randomised comparison.
- Detailed mechanism of action data for everolimus.
- TGA Product Information safety data (warnings, contraindications) and the approved indication text for the ARTG entry.
- A review of the interaction profile and monitoring plan, given the major interactions listed above.
- Subtype-specific evidence before any of the other sarcoma or renal cell carcinoma subtype predictions are considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

