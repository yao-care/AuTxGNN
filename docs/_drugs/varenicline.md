---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report (varenicline is known…"
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

## Varenicline: From Smoking Cessation to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Varenicline is a nicotinic receptor partial agonist, marketed in Australia as VARENAPIX 1 mg tablets. The TxGNN model predicts it may be effective for **migraine disorder**, but this is a computational prediction only. There are **no registered clinical trials** and **no publications** showing efficacy in migraine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (varenicline is known as a smoking cessation aid) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, varenicline is a partial agonist of alpha4beta2 nicotinic acetylcholine receptors and a full agonist of alpha7 receptors. Its established use is smoking cessation, where it reduces cravings and withdrawal symptoms.

Nicotinic and cholinergic signalling has been loosely linked to pain modulation and cortical spreading depression. However, no established mechanism connects varenicline to migraine treatment. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as clinical support.

The second-ranked prediction, migraine with brainstem aura, is a subtype of migraine and has no independent evidence. Lower-ranked predictions (hair disorders such as alopecia, glaucoma, headache disorder and pulmonary hypertension) also lack supporting evidence. The retrieved literature for headache disorder and pulmonary hypertension concerns smoking cessation and adverse events, not treatment of those conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications show varenicline efficacy in migraine. The only publication retrieved for this prediction is a case report of an adverse event.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest reported in a patient taking varenicline; not relevant to migraine efficacy |

For the related prediction of headache disorder, the retrieved papers (for example the EAGLES randomised trial, PMID [27116918](https://pubmed.ncbi.nlm.nih.gov/27116918/), and a report of bath-related headache induced by varenicline, PMID [23175211](https://pubmed.ncbi.nlm.nih.gov/23175211/)) cover smoking cessation and safety. Headache appears as an adverse event, not a treatment target.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5469W | VARENAPIX | Tablet 1 mg | Not listed in the data compiled for this report |

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The TxGNN knowledge graph links varenicline to contraindication edges for anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent vascular claudication and peripheral arterial disease. These must be verified against the approved label.
- **Drug Interactions**: 100 interactions were identified in the DDI database. Cimetidine is the only one graded (Minor). Others, such as metformin, glimepiride, rosiglitazone, omeprazole, pantoprazole, lansoprazole, morphine, simvastatin, prednisone, doxycycline and epinephrine, are of unknown severity.
- **Reported adverse events in the literature**: headache (including bath-related headache), cardiac arrest (case report), and diffuse exanthema (case report).

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no efficacy literature and no plausible established mechanism. Headache is a known adverse effect of varenicline, which argues against a migraine benefit.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic link between nicotinic receptor activity and migraine
- Preclinical or pilot clinical evidence of benefit in migraine
- The TGA PI warnings and contraindications, and the approved indication for ARTG 5469W
- Review of the psychiatric and cardiovascular cautions in a migraine population
- Severity grading for the unclassified drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

