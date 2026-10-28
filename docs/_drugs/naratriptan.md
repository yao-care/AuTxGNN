---
layout: default
title: Naratriptan
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Naratriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
description: "Naratriptan: predicted new indication Atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Naratriptan
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

## Naratriptan: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Naratriptan is a triptan (5-HT1B/1D agonist) originally used for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **atrophoderma vermiculata**,
but there are currently **no registered clinical trials** and **20 publications** that concern migraine in general rather than this subtype specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, naratriptan is a 5-HT1B/1D receptor agonist (triptan class). Its efficacy in acute migraine is established, and mechanistically it may be applicable to a closely related migraine subtype.

Migraine with brainstem aura is a form of migraine, so shared pathophysiology (trigeminovascular activation, CGRP release) is plausible. However, none of the supplied literature is specific to brainstem aura. It covers migraine in general: the American Headache Society evidence assessment, naratriptan versus sumatriptan, prodrome treatment, menstrual migraine and paediatric use.

The very high TxGNN score mostly reflects closeness to the approved migraine indication, not independent evidence. Triptans have also historically been cautioned against, or contraindicated, in hemiplegic and basilar-type migraine because of theoretical vasoconstriction concerns. Safety needs explicit review before any use in this setting.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The most relevant publications are listed below (up to 10, prioritising RCTs). None is specific to brainstem aura.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomised, double-blind crossover comparison of naratriptan and sumatriptan for headache recurrence in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Naratriptan given during the prodrome to assess prevention of migraine headache |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | Randomised, placebo-controlled study | Headache | Naratriptan 1 mg and 2.5 mg twice daily versus placebo as short-term prophylaxis of menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Sumatriptan was less effective in migraine with aura than without aura |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Review | Expert Opin Pharmacother | Updated review of menstrual migraine: hormonal causes, prophylaxis and treatment |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Review of treatment during the premonitory phase of migraine |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatric Drugs | Use of triptans in paediatric migraine |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review | Headache | Managing intractable migraine with naratriptan |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open-label pilot study | Neurol Sci | Naratriptan as short-term prophylaxis of pure menstrual migraine (multi-centre, non-comparative) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8298R | Naramig | Tablet 2.5 mg (as hydrochloride) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationship data, not product label text): hypertension, liver failure, diabetes mellitus, diabetic ketoacidosis, coronary artery disease, obesity, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, myocardial ischaemia, Prinzmetal angina, peripheral vascular disease, transient ischaemic attack, vertebrobasilar insufficiency, haemoglobinopathy, and **familial or sporadic hemiplegic migraine**. The last is particularly relevant to the proposed use in a brainstem aura subtype.
- **Drug Interactions**: 39 interactions were identified. Major interactions include:
  - Serotonergic agents: lorcaserin, fenfluramine, dexfenfluramine, sibutramine and methylene blue.
  - 5-HT3 antagonists: ondansetron, granisetron, dolasetron and palonosetron.
  - Moderate interactions: morphine, including liposomal morphine.
  - Interactions of unknown severity: lansoprazole, pantoprazole, omeprazole, prednisone, ranitidine, clarithromycin, bupropion, budesonide and promethazine.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible because brainstem aura is a migraine subtype, but the evidence is model-based only (L4), with no trials and no literature specific to brainstem aura. Triptan cautions in hemiplegic and basilar-type migraine are a significant unresolved safety concern. The high TxGNN score mainly reflects proximity to the approved indication.

**To proceed, the following is needed:**
- Mechanism of action data for naratriptan
- The TGA Product Information, including warnings, contraindications and the approved indication text
- A focused safety review of triptan use in brainstem aura, hemiplegic and basilar-type migraine, including vasoconstriction and stroke risk
- Studies or case series specific to migraine with brainstem aura
- A review of serotonergic drug interactions for patients on concurrent therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

