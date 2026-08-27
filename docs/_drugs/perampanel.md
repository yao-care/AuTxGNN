---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel is a selective, non-competitive AMPA-receptor antagonist used for focal-onset and generalised tonic-clonic seizures in epilepsy. The TxGNN model predicts a possible role in **visual epilepsy** (a photosensitive/visually-triggered seizure subtype), but the **3 clinical trials** and **19 publications** identified all study general epilepsy populations rather than this specific reflex subtype — the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — focal-onset (partial-onset) and primary generalised tonic-clonic seizures (per literature evidence; no Australian regulatory record exists — see below) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned by DrugBank for this evaluation (data gap). However, the literature evidence collected for this candidate independently confirms the mechanism: perampanel is a novel, orally active, non-competitive AMPA-receptor antagonist that reduces glutamate-mediated postsynaptic excitation and suppresses seizure activity across rodent seizure models (PMID 21635236). It is approved internationally as adjunctive and monotherapy treatment for focal-onset seizures and generalised tonic-clonic seizures (PMID 24559052, 36150304).

Visual (photosensitive) epilepsy involves cortical hyperexcitability triggered by visual/light stimuli, and AMPA-receptor blockade is mechanistically plausible for dampening this cortical over-excitation — EEG photic-stimulation response is a standard assessment tool in this subtype, and one identified trial (NCT02900755) specifically evaluated perampanel's effect on EEG parameters in epilepsy patients.

That said, none of the three clinical trials or nineteen publications retrieved were designed around, or restricted to, visual/photosensitive epilepsy specifically — they studied general epilepsy populations (PK/safety, cognition/EEG, neurophysiology testing). The mechanistic rationale is sound, but direct efficacy evidence for this reflex subtype is currently absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Tolerability, safety and pharmacokinetics of perampanel (E2007) in patients with refractory partial or generalised seizures on concomitant AEDs — general epilepsy population, not visual-subtype specific. |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Effects of perampanel on cognition and EEG in epilepsy patients; EEG/photic-response assessment is relevant methodology for visual epilepsy but the study was not restricted to this subtype. |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Effects of perampanel on neurophysiology tests including visual evoked potential (VEP) in healthy volunteers; weak relevance — mechanistic/neurophysiology focus, not a treatment-efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES practice guideline on efficacy and tolerability of newer antiepileptic drugs (including perampanel) for new-onset epilepsy. |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review | Brain & Development | Systematic review/meta-analysis of perampanel efficacy, tolerability and safety in children and adolescents with epilepsy. |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy & Behavior | Reviews perampanel monotherapy clinical trial and real-world evidence for focal-onset and generalised tonic-clonic seizures. |
| [31912315](https://pubmed.ncbi.nlm.nih.gov/31912315/) | 2020 | Cohort | Clinical Pharmacokinetics | Therapeutic drug monitoring of antiepileptic drugs, including perampanel, in women before/during/after pregnancy. |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Cohort | Med J Malaysia | Efficacy and safety of adjunctive perampanel in a real-world epilepsy cohort. |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Post-hoc analysis | Neurology | Impact of concomitant enzyme-inducing AEDs on perampanel efficacy/safety across the three Phase 3 trials. |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Case Series | Frontiers in Neurology | Real-life experience of perampanel as add-on/second-line monotherapy in childhood absence epilepsy. |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | Review of antiseizure medication management (including perampanel) during pregnancy and lactation. |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | PK/PD Review | Expert Opin Drug Metab Toxicol | Pharmacokinetic and pharmacodynamic evaluation of perampanel for partial-onset seizures. |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development history of perampanel as an AMPA-receptor antagonist antiepileptic drug. |

None of the above specifically studies visual/photosensitive epilepsy.

---

## Australia Market Information

Perampanel is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)** — 0 entries found in this evidence pack.

---

## Safety Considerations

No key warnings, contraindications, or drug interaction data were returned for this evaluation (all marked as data gaps; DDI query status: not found). As perampanel is not TGA-registered, there is no Australian Product Information available.

> Please refer to overseas regulatory labelling (e.g. FDA, EMA Summary of Product Characteristics) for safety information, pending TGA registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (AMPA-receptor antagonism dampening cortical hyperexcitability) is plausible for visual epilepsy, but no identified trial or publication specifically addresses this reflex seizure subtype — all evidence comes from general epilepsy populations. Combined with the drug's unregistered status in Australia, the evidence does not yet support progression beyond a research question.

**To proceed, the following is needed:**
- TFDA/TGA product information and formal MOA data (currently data gaps)
- A trial or case series specifically enrolling patients with visual/photosensitive-triggered seizures
- Drug interaction and contraindication data
- ARTG registration pathway assessment, given the drug is not currently marketed in Australia

**Note on alternative candidate:** Among the 10 TxGNN-predicted indications in this evidence pack, **status epilepticus** (rank 10) has materially stronger, more direct evidence — a recruiting Phase 2 trial (NCT06401707) specifically testing perampanel for post-cardiac-arrest status epilepticus prophylaxis, a dedicated systematic review (PMID 35151187), and multiple real-world cohort studies — earning it a higher evidence tier (L2) and a "Proceed with Guardrails" recommendation. This may warrant a separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

