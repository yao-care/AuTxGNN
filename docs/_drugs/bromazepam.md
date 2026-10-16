---
layout: default
title: Bromazepam
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bromazepam: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Australian registration data compiled for this repo…"
monitor_inn: "Bromazepam"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "insomnia (disease)", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "anxiety", "alcohol withdrawal delirium", "ulerythema ophryogenesis", "dysthymic disorder", "tendinitis"]
---

# Bromazepam
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

# Bromazepam: From Anxiety to Migraine Disorder

## One-Sentence Summary

Bromazepam is a benzodiazepine that acts on GABA-A receptors and is marketed in Australia as Lexotan 3 mg tablets.
The TxGNN model's top-ranked prediction is **migraine disorder** (score 99.06%), but **no clinical trials and no publications** currently support it.
The best-supported direction in the data compiled for this report is **anxiety**, which is essentially an existing use of the drug rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian registration data compiled for this report (the drug is a benzodiazepine anxiolytic) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

Other predictions by rank: migraine with brainstem aura (98.91%), insomnia (98.50%), migraine with or without aura susceptibility (98.14%), atrophoderma vermiculata (97.46%), anxiety (97.35%), alcohol withdrawal delirium (96.86%), ulerythema ophryogenesis (96.74%), dysthymic disorder (96.73%) and tendinitis (96.69%). Only anxiety has clinical trial and RCT-level literature support (Evidence Level L3). Insomnia and alcohol withdrawal delirium are L4, and the rest are L5.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bromazepam is a benzodiazepine, and the class acts as a positive allosteric modulator of the GABA-A receptor. This enhances inhibitory neurotransmission, producing anxiolytic, sedative, muscle-relaxant and anticonvulsant effects.

For **migraine**, a plausible but speculative link is reduced central hyperexcitability, or reduced muscle tension and anxiety-related triggers. Benzodiazepines are not an established migraine therapy. They carry risks of dependence and medication-overuse headache. The migraine-related predictions (ranks 1, 2 and 4) likely reflect proximity within the knowledge graph rather than clinical evidence.

Several predictions have no plausible mechanistic link and are likely knowledge-graph artefacts. These are atrophoderma vermiculata, ulerythema ophryogenesis and tendinitis.

The class-level rationale is strongest for **anxiety**, **insomnia** (sedative-hypnotic effect) and **alcohol withdrawal delirium** (benzodiazepines are standard of care). However, agents such as diazepam, lorazepam and chlordiazepoxide have better-established evidence for alcohol withdrawal.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication, migraine disorder. For the anxiety prediction, one trial was identified:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Multicentre pharmacovigilance study of adverse drug reactions with psychopharmacological treatment in elderly gerontopsychiatric inpatients. It is not an efficacy trial for bromazepam, and bromazepam's role is unclear. Indirect safety-monitoring relevance only. |

No ANZCTR trials were identified in the data compiled.

---

## Literature Evidence

No publications are available for migraine disorder. The table below shows the most relevant publications for the anxiety prediction (the best-supported direction). Several older RCTs are included. Their full designs and results are not available in the data, so they cannot support a grading above L3 without verification.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6132936](https://pubmed.ncbi.nlm.nih.gov/6132936/) | 1983 | RCT | J Clin Psychopharmacol | In 48 patients with generalised anxiety disorder, bromazepam (18 mg/day) and diazepam were superior to placebo from week 1. Bromazepam was more effective than diazepam on somatic anxiety and total score. |
| [1969172](https://pubmed.ncbi.nlm.nih.gov/1969172/) | 1990 | RCT | Psychopharmacology | In 245 general practice patients with generalised anxiety disorder, bromazepam showed greater Hamilton Anxiety reduction than chlorprothixene or placebo over 2 weeks. |
| [2880459](https://pubmed.ncbi.nlm.nih.gov/2880459/) | 1986 | Randomised placebo-controlled study | Acta Psychiatr Scand | In 60 outpatients with generalised anxiety, bromazepam and lorazepam were similarly effective and both were superior to placebo. |
| [13969](https://pubmed.ncbi.nlm.nih.gov/13969/) | 1977 | RCT | Dis Nerv Syst | In 72 patients with anxiety-depressive neurosis, bromazepam was compared with amitriptyline and placebo over 4 weeks, and a larger proportion improved on bromazepam. |
| [2898321](https://pubmed.ncbi.nlm.nih.gov/2898321/) | 1988 | Double-blind comparison | Curr Med Res Opin | Metaclazepam versus bromazepam in 50 patients with anxiety neurosis. |
| [32039743](https://pubmed.ncbi.nlm.nih.gov/32039743/) | 2020 | Systematic review/network meta-analysis | Acta Neuropsychiatr | Pharmacological treatments for social anxiety disorder. |
| [11801236](https://pubmed.ncbi.nlm.nih.gov/11801236/) | 2002 | Review | Biol Psychiatry | Single-trial data suggest bromazepam may have efficacy similar to SSRIs in social anxiety disorder, but SSRIs are first line. |
| [24409202](https://pubmed.ncbi.nlm.nih.gov/24409202/) | 2014 | Review | Ther Adv Neurol Disord | Notes one RCT in which bromazepam was effective for anxiety in Parkinson's disease. |
| [27663828](https://pubmed.ncbi.nlm.nih.gov/27663828/) | 2016 | Case report | Psychiatr Danub | Megadose bromazepam dependence, highlighting dependence and tolerance risks. |
| [1292648](https://pubmed.ncbi.nlm.nih.gov/1292648/) | 1992 | Case report | Biomed Pharmacother | Oromandibular dystonia after bromazepam. |

For insomnia, the retrieved literature is indirect (prescribing surveys, pharmacokinetic reviews and a Parkinson's neuropsychiatry review). None is a bromazepam-specific efficacy study.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4150K | Lexotan | Tablet 3 mg (oral) | Not stated in the data compiled |

---

## Safety Considerations

- **Dependence and tolerance:** Documented in the literature, including a case of megadose dependence. Chronic benzodiazepine use is associated with cognitive impairment, falls, traffic accidents, dependence and tolerance.
- **Adverse reactions:** Case-level reports of oromandibular dystonia.
- **Migraine-specific risk:** Benzodiazepines carry a risk of medication-overuse headache.
- **Elderly patients:** Older adults are at higher risk of adverse drug reactions because of altered metabolism, comorbidity and polypharmacy.

No drug interaction records were found in the data compiled. No knowledge-graph contraindications were identified. Please refer to the TGA-approved Product Information (PI) for formal warnings, contraindications and interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked migraine prediction rests on a model score alone (L5), with no trials or literature, and benzodiazepines are not an established migraine therapy and carry dependence and medication-overuse headache risks. The anxiety signal is real but reflects the drug's existing use rather than repurposing.

**To proceed, the following is needed:**
- Supporting clinical or preclinical evidence for bromazepam in migraine (none exists in the data compiled)
- Verification of the older anxiety RCTs' designs and results, if anxiety is pursued
- The approved indication wording from the Australian PI and ARTG record
- Detailed mechanism of action data and the PI safety information (warnings, contraindications, interactions)
- A benefit-risk assessment addressing dependence and medication-overuse headache against existing migraine therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

