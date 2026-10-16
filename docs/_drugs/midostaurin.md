---
layout: default
title: Midostaurin
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Midostaurin: predicted new indication Familial thrombocytosis (evidence level L5). Approved use: Acute myeloid leukaemia (including FLT3-, NPM1-…"
monitor_inn: "Midostaurin"
predicted_indications: ["familial thrombocytosis", "reactive thrombocytosis", "metastatic melanoma", "inverse Klippel-Trenaunay syndrome", "thrombocythemia", "non-cutaneous melanoma", "epithelioid cell melanoma", "eyelid melanoma", "scrotum melanoma", "amelanotic skin melanoma"]
---

# Midostaurin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Midostaurin: From Acute Myeloid Leukaemia to Familial Thrombocytosis

## One-Sentence Summary

Midostaurin was originally used to treat acute myeloid leukaemia (AML), including several molecular subtypes.
The TxGNN model predicts it may be effective for **familial thrombocytosis**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting this specific indication.
Among the other top-ranked predictions, only metastatic melanoma (a negative Phase IIA study) and thrombocythemia (indirect review articles) have any literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukaemia (including FLT3-, NPM1-, CEBPA-mutated and other subtypes) |
| Predicted New Indication | Familial thrombocytosis |
| TxGNN Prediction Score | 98.92% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

Note: the original indication is taken from the knowledge graph indication list, because the Australian licence record contains no approved indication text.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the evidence summarised for this prediction, midostaurin is a multikinase inhibitor (acting on KIT, FLT3 and PKC), and its efficacy in myeloid disease is established. Mechanistically, it could affect myeloproliferative signalling relevant to familial thrombocytosis.

However, this link is speculative. Familial thrombocytosis is usually driven by germline *THPO*, *MPL* or *JAK2* variants, not by the kinase targets of midostaurin. No trial or literature data were available to support the prediction.

**Other top-ranked predictions (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Reactive thrombocytosis | 98.76% | L5 | Secondary to inflammation or iron deficiency; treatment targets the cause, so a kinase inhibitor has no clear rationale |
| 3 | Metastatic melanoma | 97.64% | L3 | Phase IIA study reported lack of activity |
| 5 | Thrombocythemia | 97.48% | L4 | Biologically plausible (MPN), but only indirect review evidence; flagged as a research question |
| 4, 6–10 | Inverse Klippel-Trenaunay syndrome and melanoma subtypes (non-cutaneous, epithelioid cell, eyelid, scrotum, amelanotic skin) | 96.4–97.6% | L5 | Prediction only; no supporting data |

## Clinical Trial Evidence

Currently no related clinical trials registered for familial thrombocytosis. No clinical trials were identified for any of the top 10 predicted indications.

## Literature Evidence

No literature is available for familial thrombocytosis. The following publications relate to other top-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16969355](https://pubmed.ncbi.nlm.nih.gov/16969355/) | 2006 | Phase IIA trial | Br J Cancer | Midostaurin 75 mg orally three times daily in 17 patients with metastatic melanoma; the study reported a lack of activity (negative result) |
| [29704617](https://pubmed.ncbi.nlm.nih.gov/29704617/) | 2018 | Review | Pharmacol Res | Role of small-molecule KIT inhibitors in neoplastic disorders; indirect context only |
| [29277359](https://pubmed.ncbi.nlm.nih.gov/29277359/) | 2018 | Review | Clin Lymphoma Myeloma Leuk | State-of-the-art update on myeloproliferative neoplasms (MPN); indirect relevance to thrombocythemia |
| [23471017](https://pubmed.ncbi.nlm.nih.gov/23471017/) | 2011 | Review | Blood Cancer J | Proceedings on epigenetic mutations and treatment progress in MPN; indirect relevance to thrombocythemia |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11505M | Rydapt | Capsule 25 mg (oral) | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Haematological parameters (FBC), liver and renal function; please confirm against the PI |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling policy |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in the interaction database; the first 20 reviewed include two **Major** interactions, with **clarithromycin** and **dolasetron**. Most others are Moderate, including antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide, dulaglutide), famotidine, cimetidine, aprepitant, dexamethasone, loperamide, and bowel preparations or laxatives (bisacodyl, picosulfuric acid, polyethylene glycol). The full list should be reviewed before any use.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for familial thrombocytosis is supported by the model score alone (L5), with no trials or literature. The mechanistic link is speculative because the disease is typically driven by germline *THPO*, *MPL* or *JAK2* variants. Midostaurin also carries a substantial toxicity and interaction burden. The only clinical study among the top predictions (metastatic melanoma) was negative.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- TGA Product Information (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Preclinical or mechanistic evidence linking midostaurin to familial thrombocytosis
- A closer look at thrombocythemia (essential thrombocythemia) as a more biologically plausible research question, including a review of whether the cited MPN papers discuss midostaurin
- Review of the full interaction list, especially the major interactions with clarithromycin and dolasetron
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

