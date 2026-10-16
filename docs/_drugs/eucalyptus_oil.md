---
layout: default
title: Eucalyptus Oil
parent: Model Prediction Only (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eucalyptus Oil: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Eucalyptus Oil
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

# Eucalyptus Oil: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Eucalyptus oil is listed in Australia as a marketed single-ingredient product, but the data compiled for this report contain no approved indication text.
The TxGNN model predicts it may be effective for **osteoarthritis**, with a score of 98.5%.
There are currently **no registered clinical trials** and **no publications that test eucalyptus oil as a treatment for osteoarthritis**, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Eucalyptus oil is a plant-derived essential oil whose main constituent, 1,8-cineole (eucalyptol), has reported anti-inflammatory and counter-irritant activity. This is a plausible biological rationale, but it is inferred rather than demonstrated for osteoarthritis.

The two publications retrieved for osteoarthritis (PMID 38409718 and 37111672) are about topical emulgel and nanoemulgel formulations. In them, natural oils, including eucalyptus oil, serve as penetration enhancers or vehicles for NSAIDs such as celecoxib. They do not test eucalyptus oil as a therapeutic agent.

The high TxGNN score is a computational prediction. It should be treated as a hypothesis to test, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis. No ANZCTR identifiers were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38409718](https://pubmed.ncbi.nlm.nih.gov/38409718/) | 2024 | Formulation / in vitro | Anti-inflammatory & Anti-allergy Agents in Medicinal Chemistry | Celecoxib emulgel developed using a natural oil. Eucalyptus oil acts as a formulation component, and there is no test of its own efficacy. |
| [37111672](https://pubmed.ncbi.nlm.nih.gov/37111672/) | 2023 | Review | Pharmaceutics | Overview of nanoemulgels for improving topical delivery of anti-inflammatory drugs. Not direct evidence for eucalyptus oil. |

### Other Predicted Indications (for context)

- **Rheumatoid arthritis (score 98.3%, evidence level L4, "Research Question"):** There is one small 2022 study of eucalyptus inhalation for pain and quality of life in rheumatoid arthritis ([PMID 36060153](https://pubmed.ncbi.nlm.nih.gov/36060153/)). Its design and size could not be verified. A 2024 animal and in silico study ([PMID 38649658](https://pubmed.ncbi.nlm.nih.gov/38649658/)) suggests eucalyptol has anti-arthritic activity, plausibly through effects on IL-17, IL-10, NF-κB, 5-LOX and COX-2. The other retrieved papers concern delivery systems for other drugs and are not evidence for eucalyptus oil.
- **Osteoarthritis susceptibility, gout, pseudoachondroplasia, early-onset familial noncirrhotic portal hypertension, idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, primitive portal vein thrombosis:** No trials or literature, so these are predictions only. Several are rare genetic or hepatic conditions with no plausible mechanistic link.
- **Hepatic porphyria:** There is no supporting evidence. Essential oil constituents are metabolised through hepatic cytochrome P450 enzymes, and some P450 inducers can precipitate porphyria attacks. This is a potential safety concern that calls for caution.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 337R | Not available | Not available | Not available |

The data compiled for this report show one valid single-ingredient licence and no cancelled licences. Product name, dosage form and indication text are not available.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interaction records were found in the data compiled for this report. No disease contraindications were identified from the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction has no clinical trials and no publications testing eucalyptus oil as a treatment, so it is supported by model output alone (evidence level L5). Safety and label information is also missing. Rheumatoid arthritis has somewhat more support (preclinical data and one small symptom-focused study) and is better framed as a research question than as a candidate for advancement.

**To proceed, the following is needed:**
- The TGA-approved Product Information, including approved indications, formulation, route, warnings and contraindications for ARTG 337R
- Mechanism of action data, for example from DrugBank
- Direct preclinical or clinical studies of eucalyptus oil or 1,8-cineole in osteoarthritis
- Verification of the design and size of the 2022 rheumatoid arthritis inhalation study
- Confirmation that the available route of administration matches the intended use (topical, inhaled or oral)
- A safety review of concentrated essential oil exposure, including hepatic effects and porphyria risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

