---
layout: default
title: Ribociclib
parent: Moderate Evidence (L3-L4)
nav_order: 588
evidence_level: L4
indication_count: 10
---

# Ribociclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ribociclib: From Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Ribociclib is a CDK4/6 inhibitor established for HR+/HER2‑negative advanced or metastatic breast cancer. The TxGNN model predicts a possible link to **Myeloid Leukemia**, but the only supporting literature is preclinical and a case report describing CDK4/6‑inhibitor‑*induced* leukaemia — evidence that argues against, rather than for, therapeutic use. This candidate currently sits at evidence level **L4** with a **Hold** recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2-negative advanced or metastatic breast cancer (established use; not captured in the current data set — see note below) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned in this evidence pack (flagged as a High-severity data gap). Based on the clinical trial titles and literature captured elsewhere in the pack, ribociclib is a selective, orally administered cyclin-dependent kinase 4/6 (CDK4/6) inhibitor used with endocrine therapy for hormone receptor-positive breast cancer.

The TxGNN network-proximity score for myeloid leukaemia is high, but the two pieces of literature actually returned point in opposite therapeutic directions. One is an in vitro study exploring whether CDK4/6 inhibitors can overcome pharmacokinetic drug resistance in AML cells — a mechanistic, cell-line-level observation, not clinical evidence of benefit. The other is a case report of a patient who *developed* AML with eosinophilia after CDK4/6 inhibitor treatment, in the setting of pre-existing clonal haematopoiesis of indeterminate potential (CHIP) — i.e., the drug class is implicated as a possible contributor to leukaemogenesis, not a leukaemia treatment.

Taken together, the mechanistic story is unresolved and arguably contradictory: cell-cycle arrest via CDK4/6 inhibition could theoretically affect leukaemic blasts, but real-world case data instead raise a safety signal for AML emergence during treatment. This is a network-prediction artefact rather than a therapeutically coherent hypothesis at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/In vitro | Cancers | CDK4/6 inhibitors (including ribociclib) tested in vitro against ABCB1/ABCG2-mediated pharmacokinetic drug resistance in AML cells resistant to anthracycline-based chemotherapy. |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case Report | American Journal of Hematology | AML with eosinophilia arising after CDK4/6 inhibitor treatment in a patient with underlying clonal haematopoiesis — a drug-induced adverse event, not evidence of therapeutic benefit. |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case Report (appears unrelated) | Frontiers in Oncology | Describes a dual primary vulvar/breast adenocarcinoma diagnosis; the abstract does not mention ribociclib or myeloid leukaemia and appears to be a mismatched search result rather than genuine supporting evidence. |

## Australia Market Information

Ribociclib is not currently marketed in Australia and has no ARTG entries on record (0 of 0). No dosage form or approved-indication data is available from this data set.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule CDK4/6 inhibitor) — not a conventional cytotoxic agent, but carries a dose-limiting myelosuppressive profile |
| Myelosuppression Risk | High — neutropenia is the most common and dose-limiting toxicity of ribociclib in its established breast cancer indication; thrombocytopenia and anaemia are also reported (noted in pharmacovigilance and meta-analysis literature elsewhere in this evidence pack) |
| Emetogenicity Classification | Low (based on known class characteristics; not directly documented in this evidence pack) |
| Monitoring Items | FBC with differential (baseline, then periodically during treatment), liver function tests, ECG for QT-interval prolongation |
| Handling Protection | Oral targeted-therapy agent — standard institutional handling precautions for oral oncolytics apply; confirm against local cytotoxic-drug handling policy |

## Safety Considerations

Ribociclib is not currently TGA-registered, so no Australian Product Information exists to reference. Please refer to the overseas-approved Product Information (e.g., FDA or EMA labelling for Kisqali) for warnings, contraindications and drug interaction data until local registration status changes.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for a myeloid leukaemia indication is limited to one in vitro mechanistic study and one case report describing drug-induced (not drug-treated) AML — the mechanistic direction is unresolved and potentially contradictory, and the drug is not currently registered in Australia. This does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank (currently a data gap)
- TFDA/TGA-equivalent Product Information, warnings and contraindications (currently blocking — no safety pre-screen possible)
- Preclinical in vivo or clinical evidence directly testing ribociclib in myeloid leukaemia, rather than resistance-modulation or adverse-event literature
- Clarification of AML-risk signal (clonal haematopoiesis interaction) before any further evaluation

**Note on this evidence pack:** of the ten ranked candidates, most (ranks 2–6, 8–10) have no literature or trial support and appear to be TxGNN network false positives; rank 7 ("female breast carcinoma") is not a new indication but ribociclib's already-established use, surfaced here due to the missing `original_indications` field. None of the ten candidates currently support a genuine repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

