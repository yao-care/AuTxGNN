---
layout: default
title: Zinc Sulfate
parent: Moderate Evidence (L3-L4)
nav_order: 792
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L3). Approved use: Not available in the data compiled for this report"
monitor_inn: "Zinc sulfate"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency", "thrombotic disease", "gastroparesis (disease)", "faucial diphtheria", "cervical disc degenerative disorder", "dyspepsia", "acne (disease)"]
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Zinc Sulfate: From an Unspecified Original Indication to Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is an essential trace element salt that is marketed in Australia, but the data compiled for this report do not record an approved indication for it.
The TxGNN model predicts it may be effective for **pharyngitis**, with **1 clinical trial** (postoperative sore throat) and **2 publications** supporting this direction.
The evidence is indirect, because it concerns post-surgical and radiation-related throat symptoms rather than infectious pharyngitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question) |

*Note: Pharyngitis is the top-ranked prediction by TxGNN score. Acne vulgaris (rank 10, score 94.8%) has the strongest direct clinical evidence (L2) among the predictions. It is discussed in the conclusion.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for zinc sulfate. Based on known information, zinc is an essential cofactor for many metalloenzymes. It has local antiviral and mucosal-protective effects, and lozenges release zinc ions directly in the oropharynx.

Zinc may also support mucosal repair and taste/sensory recovery. This makes a link to throat inflammation plausible. However, the available studies address post-intubation sore throat and radiation-induced mucositis, not infectious pharyngitis. The mechanistic link is therefore plausible but indirect.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomised, double-blind, placebo-controlled study of preoperative zinc lozenges to reduce postoperative sore throat after endotracheal intubation. No results were provided in the data compiled. |

No Australian (ANZCTR) trial identifiers were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Double-blind, placebo-controlled trial of zinc sulfate supplementation for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/Observational | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Recovery from long-lasting post-tonsillectomy taste disturbance; discusses a possible role of zinc deficiency. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 600N | Not available | Not available | Not available |

## Safety Considerations

No label warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

- **Contraindication signals from the knowledge graph** (drug-disease edges, not label text): hypertension, kidney disease, liver disease, diabetes mellitus and diabetic ketoacidosis, heart and cardiovascular disease, hypercalcaemia and nephrocalcinosis, nephrolithiasis, hyperparathyroidism, hyperthyroidism and Graves disease, angle-closure glaucoma, diarrhoeal disease, sarcoidosis and anxiety disorders. These are model-derived signals and need verification against the PI.
- **Drug interactions** (100 recorded; the first 20 reviewed):
  - Moderate: alendronic acid, risedronic acid, ibandronate (bisphosphonates), tetracycline, and baloxavir marboxil.
  - Minor: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), azathioprine, and several biologics and immunosuppressants (e.g. abatacept, adalimumab, belimumab, baricitinib).
- **Local safety signal**: Retrieved preclinical studies show intranasal zinc sulfate can cause cytotoxicity and anosmia (loss of smell). This is relevant to any intranasal use and argues against it.

## Conclusion and Next Steps

**Decision: Hold (research question) for pharyngitis**

**Rationale:**
- The only direct trial is a non-phase postoperative sore throat study with no results provided. The supporting publications address radiation-induced mucositis and post-tonsillectomy taste changes, so the evidence for infectious pharyngitis is indirect (L3).
- Other predictions for context:
  - **Acne vulgaris** has a completed Phase 2 RCT (NCT04899843, n=122, oral zinc with topical retinoids). It is the strongest candidate at L2 and could be considered **Proceed with Guardrails**, although results were not provided and no Phase 3 trial exists.
  - **Acute laryngopharyngitis** is a research question only. Its single publication concerns radiation-induced mucositis.
  - **Nasal cavity disease, congenital prothrombin deficiency, thrombotic disease, gastroparesis, faucial diphtheria, cervical disc degeneration and dyspepsia** have no meaningful supporting evidence and should be held.

**To proceed, the following is needed:**
- The approved indication, dosage form and product details for ARTG entry 600N, and the TGA Product Information with warnings and contraindications (a blocking data gap for safety screening).
- Mechanism of action data from DrugBank.
- Published results from NCT02405832 and NCT04899843.
- A trial in infectious pharyngitis, or a Phase 3 trial in acne, with attention to copper depletion and interactions with tetracyclines and bisphosphonates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

