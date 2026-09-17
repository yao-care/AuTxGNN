---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Psychiatric Disorders to Retinal Dystrophy With or Without Extraocular Anomalies

## One-Sentence Summary

Quetiapine is an atypical antipsychotic historically used for psychiatric conditions such as schizophrenia and bipolar disorder. The TxGNN model predicts a possible association with **retinal dystrophy with or without extraocular anomalies**, with a **99.57% prediction score**, but this direction currently has **no clinical trials** and **no quetiapine-specific literature** — the supporting evidence is essentially a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / bipolar disorder (based on known pharmacology — no ARTG registration data available, as the drug is not currently marketed in Australia per this evidence pack) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this candidate is not available in the evidence pack. Based on known pharmacology, quetiapine is an atypical (second-generation) antipsychotic with 5-HT2A and D2 receptor antagonism, and its efficacy in schizophrenia and bipolar disorder is well established.

However, for this specific predicted indication the evidence pack's own analysis is explicit: **there is no known mechanistic link**. Retinal dystrophy with or without extraocular anomalies is a rare inherited retinal/ocular developmental disorder, and quetiapine has no known pharmacological target relevant to retinal development or degeneration. The only ocular association documented for quetiapine in general clinical knowledge is a recognised safety signal — a possible increased risk of cataract — which is an adverse-effect consideration, not a therapeutic rationale.

In short, the high TxGNN score here appears to be a knowledge-graph proximity signal rather than a biologically grounded hypothesis. This should be treated as a computational lead only, not as a candidate with plausible mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections; not related to quetiapine |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia; not related to quetiapine |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Overview of congenital ptosis; not related to quetiapine |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape; not related to quetiapine |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Unilateral cryptophthalmia case description; not related to quetiapine |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis case; not related to quetiapine |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex overview; not related to quetiapine |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric orbital lesions; not related to quetiapine |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case; not related to quetiapine |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Therapeutic Advances in Ophthalmology | Eye involvement in inherited metabolic disorders; not related to quetiapine |

**Note:** These 10 articles were returned by a general disease-term literature search and do not discuss quetiapine specifically. None establish a drug-disease link — they are background ophthalmology literature only.

## Australia Market Information

Quetiapine has 0 ARTG (Australian Register of Therapeutic Goods) entries in this evidence pack and is recorded as not currently marketed in Australia. No product-level data is available to summarise.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Warnings, contraindications and drug-interaction data could not be retrieved from the regulatory source at this data cutoff (2026-08-28).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are zero clinical trials, no quetiapine-specific literature, and no plausible mechanistic link for this indication — this is evidence level L5 (model prediction only). Combined with missing PI safety data, there is insufficient basis to progress.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking gap
- Detailed mechanism of action data from DrugBank
- Any preclinical or mechanistic rationale specifically linking quetiapine to retinal/ocular developmental pathways, before further evidence collection is warranted

**Note:** Within this same evidence pack, a lower-ranked candidate — **trichotillomania** (rank 8, evidence level L4, "Research Question" stage) — has actual quetiapine-specific case reports and a plausible serotonin-dopamine mechanistic rationale. That candidate may warrant separate, more active evaluation than the top-ranked prediction discussed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

