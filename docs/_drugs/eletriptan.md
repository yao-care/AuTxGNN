---
layout: default
title: Eletriptan
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Eletriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "sciatic neuropathy"]
description: "Eletriptan: predicted new indication Atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Eletriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Eletriptan: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Eletriptan is a triptan originally used for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **atrophoderma vermiculata**.
Support is limited: there are **no clinical trials** registered for this subtype and **17 publications**, mostly general migraine literature. One of them, a randomised trial, found no benefit when eletriptan was taken during the aura phase.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The published literature describes eletriptan as a selective 5-HT1B/1D receptor agonist. It is thought to act through cranial vasoconstriction and inhibition of trigeminal neuropeptide release. It is approved for the acute treatment of migraine with or without aura.

Brainstem aura (formerly basilar-type migraine) is a subtype of migraine. It plausibly shares the same trigeminovascular pathophysiology, which is why the model links the two. This is better viewed as a subtype refinement of the existing migraine indication than as true repurposing.

There are important caveats:
- No trials specifically target this subtype.
- The available literature is general migraine evidence.
- One randomised study (PMID 15469451) found no effect of eletriptan 80 mg when given during the aura phase.
- Triptans have historically been used cautiously in brainstem aura because of theoretical vasoconstriction concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT | Eur J Neurol | Eletriptan 80 mg taken during the aura phase of migraine with aura showed no effect |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | Cephalalgia | Placebo-controlled study (n=446) of eletriptan in patients with and without aura who had previously responded poorly to, or not tolerated, oral sumatriptan |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | Eur Neurol | Eletriptan 40 mg and 80 mg compared with ergotamine plus caffeine and placebo in acute migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Review | Cochrane Database Syst Rev | Cochrane review of eletriptan for acute migraine (a later version was withdrawn, PMID 17636718) |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Review | Curr Opin Investig Drugs | Describes eletriptan as a 5-HT1B/1D agonist with higher receptor affinity than sumatriptan |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatr Drugs | Review of triptan use in paediatric migraine |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | Case report | Rev Port Cardiol | Non-ST-elevation myocardial infarction a few hours after taking eletriptan for migraine |
| [11050304](https://pubmed.ncbi.nlm.nih.gov/11050304/) | 2000 | Preclinical | Eur J Pharmacol | Compared contractile effects of eletriptan and sumatriptan on human isolated meningeal and coronary arteries |
| [29491334](https://pubmed.ncbi.nlm.nih.gov/29491334/) | 2018 | Case report | Rinsho Shinkeigaku | Triptan-responsive migraine-like headache was caused by a cavernous sinus dural arteriovenous fistula, so a triptan response does not confirm migraine |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 5290K | Relpax | Tablet 40 mg (as hydrobromide), oral | Approved indication text not available in the data compiled |

---

## Safety Considerations

- **Contraindications and related conditions (knowledge-graph based, not label text):** The knowledge graph links eletriptan with these conditions, which are largely cardiovascular and cerebrovascular:
  - hypertension
  - coronary artery disease, myocardial infarction, myocardial ischaemia and Prinzmetal angina
  - stroke, transient ischaemic attack, cerebral infarction and brain ischaemia
  - vertebrobasilar insufficiency
  - peripheral vascular disease and Raynaud disease
  - ischaemic bowel disease
  - familial or sporadic hemiplegic migraine
  - serotonin syndrome
  - liver disease and liver failure
  - diabetes
- **Drug Interactions:** 94 interactions are recorded. Major-level examples include:
  - clarithromycin
  - lorcaserin
  - fenfluramine and dexfenfluramine
  - sibutramine
  - the 5-HT3 antagonists dolasetron, granisetron, ondansetron and palonosetron

  Moderate-level examples include aprepitant, morphine, cimetidine, clotrimazole and miconazole.

Please refer to the TGA-approved Product Information (PI) for the official warnings and contraindications, which were not available in the data compiled.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but it is essentially a subtype of the already-approved migraine indication. There are no trials in brainstem aura. The one directly relevant randomised study showed no benefit when eletriptan was given during the aura phase. Triptan use in this subtype also raises theoretical vascular safety concerns. At present this is a research question rather than a repurposing candidate.

**To proceed, the following is needed:**
- Subtype-specific clinical data on eletriptan in migraine with brainstem aura
- A clinical and regulatory review of vascular safety in this subtype
- The TGA Product Information, including warnings, contraindications and the approved indication wording
- Detailed mechanism of action data
- A review of the high-risk interactions, particularly CYP3A4 inhibitors and serotonergic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

