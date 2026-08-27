---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Naratriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naratriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Naratriptan is a selective 5-HT1B/1D receptor agonist (triptan class) originally used for the acute treatment of migraine.
> The TxGNN model predicts it may be effective for **migraine with brainstem aura**, with a very high prediction score (**99.98%**),
> but **no clinical trials and no subtype-specific literature** currently support this direction — the 19 retrieved publications all concern migraine generally (including menstrual and paediatric migraine), none address the brainstem-aura subtype specifically, and this subtype is one where triptans carry a recognised vasoconstriction safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment) — per drug-class positioning in the evidence pack; no ARTG/registration record on file for this jurisdiction |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Naratriptan is a selective 5-HT1B/1D receptor agonist. Its established mechanism treats migraine through intracranial vasoconstriction and inhibition of vasoactive peptide release from the trigeminovascular system — this is its original, non-repurposed core indication.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype of migraine rather than a distinct disease, which is why the TxGNN model scores it so highly against a drug already used for migraine broadly. However, this is exactly where the prediction needs scrutiny rather than acceptance at face value: because this subtype involves brainstem/vertebrobasilar circulation, triptans' vasoconstrictive mechanism is conventionally flagged as a relative contraindication or warning in major guidance (e.g. AHS assessments, product labelling), out of concern for precipitating brainstem ischaemia. None of the 19 retrieved publications — which cover general acute migraine treatment, menstrual migraine, prodrome prevention, and paediatric use — specifically address efficacy or safety in the brainstem-aura subtype.

In short, the high TxGNN score most likely reflects semantic proximity to "migraine" in the model's embedding space rather than a genuine, clinically validated new indication. This is a case where the model has not captured a known clinical contraindication signal, and the prediction should be treated as a safety flag for review rather than a repurposing opportunity to pursue.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*Note: PubMed's search matched these publications to "migraine" broadly; none specifically address the migraine-with-brainstem-aura subtype.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomised, double-blind, crossover comparison of naratriptan vs. sumatriptan in migraine patients prone to headache recurrence |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT | Headache | Double-blind, placebo-controlled trial of naratriptan 1mg/2.5mg twice daily as short-term prophylaxis of menstrually associated migraine |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT (prodrome prevention) | Cephalalgia | Investigated naratriptan given during the migraine prodrome to prevent headache onset |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies, including triptans |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Found reduced triptan (sumatriptan) efficacy in migraine with aura vs. without aura — relevant caution for aura subtypes generally |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of hormonal causes, prophylaxis and treatment of menstrual migraine |
| [16268666](https://pubmed.ncbi.nlm.nih.gov/16268666/) | 2005 | Review | CNS Drugs | Review of triptan use in management of menstrual migraine |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Literature review on whether premonitory-phase treatment is a useful migraine management strategy |
| [19126376](https://pubmed.ncbi.nlm.nih.gov/19126376/) | 2009 | Review | Current Pain and Headache Reports | Clinical review of perimenstrual headache classification and treatment |

---

## Australia Market Information

No ARTG entries are on file for Naratriptan in this evidence pack — the drug is currently **not marketed** in this jurisdiction (0 registered licences), so no product/dosage-form table can be produced.

---

## Safety Considerations

**Key Mechanistic Safety Signal**: Triptans, including naratriptan, act via vasoconstriction. This is mechanistically relevant to migraine with brainstem aura, where vertebrobasilar circulation is involved — a recognised area of caution for this drug class.

Please refer to the TGA-approved Product Information (PI) for full contraindication, warning, and drug-interaction information — no PI-level warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DrugBank DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a migraine subtype where the drug's own vasoconstrictive mechanism raises a plausible safety concern rather than a validated efficacy signal, and no clinical trial or subtype-specific literature evidence exists to support it. A blocking data gap on PI-equivalent warnings/contraindications also means the mandatory safety screen (S1) cannot be completed.

**To proceed, the following is needed:**
- TFDA/PI-equivalent label warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism-of-action data via DrugBank API (currently missing — DG002)
- Drug-drug interaction data (current query returned no results)
- Trial or literature evidence specific to the migraine-with-brainstem-aura subtype, particularly addressing vascular safety, before this candidate can move beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

