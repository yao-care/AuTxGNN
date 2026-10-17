---
layout: default
title: Rizatriptan
parent: Model Prediction Only (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rizatriptan: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder"
monitor_inn: "Rizatriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "amenorrhea (disease)", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "sciatic neuropathy", "alopecia", "headache disorder"]
---

# Rizatriptan
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

# Rizatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rizatriptan is a 5-HT1B/1D receptor agonist (triptan) originally used for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a migraine subtype, with a very high score (99.94%).
However, the evidence is indirect: **no clinical trials** and **no publications** address brainstem aura specifically. The available literature covers migraine generally (19 publications).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (the Australian ARTG entry carries no indication text in the data compiled for this report) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 (general migraine reviews only; no studies in this subtype) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rizatriptan is a selective 5-HT1B/1D agonist. Its established effect in migraine is thought to come from cranial vessel constriction, inhibition of neuropeptide release and reduced trigeminal pain transmission.

Brainstem aura is a migraine subtype, so the mechanism could plausibly carry over. However, all 19 retrieved publications are general migraine reviews and guidelines, such as the American Headache Society evidence assessment and reviews of triptans, menstrual, vestibular and paediatric migraine. None addresses brainstem aura directly.

There is also an important safety question. Triptans have historically been cautioned against, or contraindicated, in hemiplegic and basilar-type migraine because of theoretical vasoconstriction concerns. This needs to be resolved before efficacy is considered. One retrospective study (PMID 17718700) reported on triptan use in hemiplegic migraine, but it is not evidence for brainstem aura.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura.

(Rizatriptan has many trials in general acute migraine, but none enrolled patients with this specific subtype.)

## Literature Evidence

No publication addresses brainstem aura specifically. The most relevant general migraine publications retrieved are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society update on evidence for acute migraine drug therapies |
| [11687054](https://pubmed.ncbi.nlm.nih.gov/11687054/) | 2001 | Review (Cochrane) | Cochrane Database Syst Rev | Rizatriptan for acute migraine (a later version was withdrawn, PMID 17636717) |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | J Headache Pain | Frovatriptan compared with rizatriptan and other triptans in migraine with aura |
| [24867845](https://pubmed.ncbi.nlm.nih.gov/24867845/) | 2014 | Pooled analysis of RCTs | Neurol Sci | Gender and triptan efficacy, including rizatriptan comparisons |
| [17718700](https://pubmed.ncbi.nlm.nih.gov/17718700/) | 2007 | Observational study | Eur J Neurol | Triptan efficacy and tolerability in familial or sporadic hemiplegic migraine; no ischaemic stroke or heart attack among the patients reported |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Front Neurol | Treatment options in vestibular migraine |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Menstrual migraine treatment options |
| [16336021](https://pubmed.ncbi.nlm.nih.gov/16336021/) | 2005 | Review | PharmacoEconomics | Pharmacoeconomic review of rizatriptan in acute migraine |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10551H | RIXALT | Orally disintegrating tablet, 10 mg (as benzoate) | Not available in the data compiled |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease relationships in the model's knowledge graph, not from product label text):
- Cardiovascular and cerebrovascular: hypertension, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, myocardial ischaemia, coronary artery disease, Prinzmetal angina, peripheral vascular disease and peripheral arterial disease
- Hepatic and renal: liver disease, gallbladder disease, chronic kidney disease and end-stage renal failure
- Other: haemoglobinopathy and **familial or sporadic hemiplegic migraine**

The hemiplegic migraine flag is particularly relevant to this prediction, given the related aura subtypes.

**Drug Interactions:** 80 interactions are recorded. Those classed as Major include:
- Serotonergic agents: lorcaserin, dexfenfluramine, fenfluramine, sibutramine
- 5-HT3 antagonists: ondansetron, granisetron, palonosetron, dolasetron

Morphine (including liposomal) is classed as Moderate. Other recorded interactions have an unknown severity level.

Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The prediction is mechanistically plausible, but there are no trials or publications specific to brainstem aura. The triptan safety concern in hemiplegic and basilar-type migraine is unresolved, and the knowledge graph flags hemiplegic migraine as a contraindication.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA Product Information warnings and contraindications
- A targeted literature review of triptan safety and efficacy in brainstem aura (basilar-type) migraine
- Clinical or expert neurology input on the vasoconstriction risk in this subtype
- If safety is acceptable, a carefully designed study or registry in this population, with cardiovascular screening and DDI review

---

### Note on Other Predictions

The data also contain a related prediction, **headache disorder** (TxGNN score 81.67%, evidence level L1, Proceed with Guardrails). It is supported by multiple completed Phase 3 placebo-controlled trials (for example NCT00897949, NCT00111709, NCT01001234) and a 2025 RCT in vestibular migraine (PMID 40354049). However, because migraine is already an approved indication, this is better seen as indication confirmation than true repurposing. The remaining predictions (for example alopecia and amenorrhoea) have no supporting evidence and no plausible mechanism, and are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

