---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Prasugrel: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Acute coronary syndrome"
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
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

## Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Prasugrel is an oral antiplatelet (P2Y12 inhibitor) originally used for acute coronary syndrome.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **no clinical trials** and **2 loosely related publications**, neither of which studies prasugrel in this condition.
The data compiled for this report show a more credible direction in **migraine disorder** (with patent foramen ovale), supported by **2 clinical trials** and **2 class-level publications**, and this is discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (the ARTG entry carries no indication text) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

*Note: for the alternative candidate, migraine disorder (TxGNN score 0.9988), the evidence level is L3 and the recommendation is a research question rather than a clinical decision.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Prasugrel is known to be a P2Y12 receptor antagonist that inhibits platelet activation and aggregation. Its efficacy in acute coronary syndrome is established.

**Pulmonary hypertension:** Platelet activation and thrombosis are thought to contribute to pulmonary vascular remodelling, so a mechanistic link is conceivable. However, this link is theoretical only. The two papers retrieved concern clopidogrel adherence after ACS and background therapy before COVID-19 infection. Neither evaluates prasugrel in pulmonary hypertension. The high score reflects a model prediction, not demonstrated benefit.

**Migraine disorder (a more plausible alternative):** Some migraine patients have a patent foramen ovale (PFO). One hypothesis is that platelet-derived vasoactive substances (such as serotonin) or small emboli bypass pulmonary filtration. P2Y12 inhibitors may reduce platelet activation. Retrospective data on thienopyridines (clopidogrel and prasugrel) and an open-label ticagrelor pilot suggest possible benefit. This evidence is class-level, not specific to prasugrel, and no randomised prasugrel data exist.

**Other predictions:** Migraine with brainstem aura and migraine susceptibility are subtypes or overlaps of the migraine entry, supported only indirectly. A 2026 preclinical mouse study of prasugrel in seizure kindling suggests possible central nervous system activity, but it is not migraine-specific and is not clinical evidence. Kyphoscoliotic heart disease, rheumatoid arthritis, homozygous familial hypercholesterolaemia, hypoalphalipoproteinaemia, brachydactyly-syndactyly syndrome and leprosy have no supporting trials or literature and no credible mechanistic rationale, so they should be treated as model artefacts at this stage.

---

## Clinical Trial Evidence

**Pulmonary hypertension:** Currently no related clinical trials registered.

**Migraine disorder (alternative candidate):**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recruiting | 32 | PFO-directed therapy for migraine (COMFORT-PFO). Prasugrel is mentioned in the background, but is not confirmed as the study intervention. Indirect evidence. |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | Septal occluder device for migraine. Does not test prasugrel. Terminated with very few participants. |

No ANZCTR trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

**Pulmonary hypertension:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Factors associated with clopidogrel use and adherence after PCI in ACS. Does not address pulmonary hypertension or prasugrel. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort (registry) | Kardiologiia | Effect of pre-infection background therapy on COVID-19 outcomes. Not relevant to prasugrel in pulmonary hypertension. |

**Migraine disorder (alternative candidate):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine use (including prasugrel) in migraineurs with PFO. |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor (same class) for refractory migraine with PFO. Notes that clopidogrel and prasugrel reduced migraine symptoms in some patients. |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinical (mouse) | Eur J Pharmacol | Prasugrel showed neuroprotective effects in a seizure kindling model. Not migraine-specific. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14796R | Prasugrel Lupin | Tablet 10 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are model-derived drug-disease links, not product label text): liver failure, hypotensive disorder, blood coagulation disease, stroke disorder, cerebrovascular disorder, cerebral infarction, transient ischaemic attack, intracranial haemorrhage, thrombocytopenic purpura, vertebrobasilar insufficiency, and injury. Of particular relevance to any new use, a history of stroke or TIA and active bleeding risk are central concerns for a potent antiplatelet.

**Drug interactions** (100 recorded interactions; examples shown):
- **Major:** deferasirox, ibritumomab tiuxetan
- **Moderate:** acetylsalicylic acid (aspirin), morphine, opium, fenfluramine, dexfenfluramine, sibutramine
- **Minor:** proton pump inhibitors and H2 blockers (e.g. omeprazole, pantoprazole, famotidine, ranitidine), bupropion

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For pulmonary hypertension, the high TxGNN score is not backed by any trials or relevant literature, and the mechanistic link is theoretical (L5). The migraine-with-PFO direction (L3) has more support, but it rests on retrospective and class-level data and a small, ongoing trial that does not clearly test prasugrel. It is best framed as a research question rather than a treatment recommendation. Prasugrel's bleeding risk and the knowledge-graph contraindication signals for cerebrovascular disease add caution.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- The TGA Product Information for warnings and contraindications (a blocking gap for safety screening)
- For migraine: confirmation of whether prasugrel is an intervention in NCT07629635, and prasugrel-specific controlled data
- For pulmonary hypertension: any preclinical or clinical evidence of prasugrel effect in this condition
- A bleeding-risk assessment for non-cardiac populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

