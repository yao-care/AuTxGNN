---
layout: default
title: Perampanel
parent: Moderate Evidence (L3-L4)
nav_order: 559
evidence_level: L4
indication_count: 10
---

# Perampanel
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Perampanel: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel is an antiseizure medicine (a non-competitive AMPA receptor antagonist) originally used for partial (focal) epilepsy.
The TxGNN model predicts it may be effective for **visual epilepsy**, but there are **no registered clinical trials** and **no publications specific to this condition**.
The only supporting literature covers focal epilepsy in general, so the evidence is **model prediction with indirect support**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy, partial motor epilepsy (from the knowledge graph; no approved indication text is available for the Australian entry) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, perampanel is a selective, non-competitive AMPA-type glutamate receptor antagonist. It reduces excitatory glutamatergic transmission at postsynaptic membranes, which underlies its use as add-on therapy in focal-onset seizures.

Visual epilepsy (photosensitive or occipital seizures) is a focal or reflex seizure type. It plausibly involves the same AMPA-mediated glutamatergic hyperexcitability as the original indication. However, the retrieved literature addresses drug-resistant focal epilepsy in general, not visual epilepsy specifically. The link is therefore indirect and largely overlaps with the approved use rather than demonstrating a new benefit.

The model also gave similarly high scores (about 99.8-99.9%) to several other rare reflex seizure types (startle, thinking, audiogenic, micturition-induced, orgasm-induced, eating and reading seizures) and to beta-ketothiolase deficiency. Such uniform scores suggest the ranking reflects graph proximity rather than disease-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visual epilepsy.

For context, the most clinically developed alternative prediction in the same dataset is **status epilepticus** (score 99.77%, evidence level L3), where perampanel has been studied in trials:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06401707](https://clinicaltrials.gov/study/NCT06401707) | Phase 2 | Recruiting | 52 | Randomised placebo-controlled pilot of perampanel to prevent status epilepticus after cardiac arrest; no results yet |
| [NCT04309721](https://clinicaltrials.gov/study/NCT04309721) | Phase 3 | Terminated | 1 | Add-on enteral perampanel in focal motor status epilepticus; terminated early, no usable data |
| [NCT05684978](https://clinicaltrials.gov/study/NCT05684978) | Phase 4 | Terminated | 1 | Perampanel in refractory status epilepticus; terminated early, no interpretable results |
| [NCT05756621](https://clinicaltrials.gov/study/NCT05756621) | N/A | Completed | 84 | Retrospective cohort of ketamine plus perampanel in super-refractory status epilepticus after cardiac arrest; contextual data only |

---

## Literature Evidence

No publications specific to visual epilepsy were retrieved. The following are the most relevant to perampanel in focal epilepsy, the closest available evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Review (Cochrane) | Cochrane Database Syst Rev | Perampanel add-on therapy in drug-resistant focal epilepsy |
| [35305446](https://pubmed.ncbi.nlm.nih.gov/35305446/) | 2022 | Systematic review / meta-analysis | Epilepsy Res | Efficacy, tolerability and safety of perampanel in pharmacoresistant focal seizures |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Network meta-analysis | Drugs | Indirect comparison of third-generation antiseizure medicines, including perampanel, for focal-onset seizures |
| [35816832](https://pubmed.ncbi.nlm.nih.gov/35816832/) | 2022 | Review | Epilepsy Behav | Scoping review of real-world perampanel effectiveness and safety in Europe |
| [36263757](https://pubmed.ncbi.nlm.nih.gov/36263757/) | 2022 | Cohort / review | Expert Opin Drug Saf | Safety of perampanel as monotherapy or first add-on therapy |
| [40839459](https://pubmed.ncbi.nlm.nih.gov/40839459/) | 2025 | Observational cohort | Epilepsia Open | PERPRISE: real-world effectiveness of perampanel as the only add-on therapy in Germany |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development of perampanel as an AMPA antagonist |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10151G | Fycompa | Tablet 10 mg (as hemisesquihydrate), oral | Not available in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions**: 56 interactions were identified. The listed ones are mostly moderate, and chiefly involve additive central nervous system depression or sedation. Examples include morphine, codeine, hydrocodone, opium, diphenoxylate, difenoxin, dronabinol, nabilone, promethazine, chlorpheniramine, metoclopramide, dextromethorphan, ethanol, and dexamethasone. Chloroquine, hydroxychloroquine and sibutramine are also listed as moderate. Clarithromycin is listed as minor.
- **Literature safety signals**: The retrieved publications report psychiatric adverse effects (irritability, psychosis) and food aversion. One publication notes a boxed warning for serious psychiatric and behavioural reactions. These come from case reports and a literature review, not from Australian label text.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high prediction score for visual epilepsy rests on a general anti-glutamatergic mechanism. There are no trials and no disease-specific publications. The literature largely restates the existing focal epilepsy indication, so it does not independently support a new use.

**To proceed, the following is needed:**
- Disease-specific evidence, such as case series, preclinical photosensitivity models, or a pilot study in visual or photosensitive epilepsy
- Clarification of whether visual epilepsy is already covered by the approved focal-seizure indication
- The approved indication text and safety sections (warnings, contraindications) from the Australian PI
- Mechanism of action data confirmed from a primary source
- For a better-supported direction, consider **status epilepticus** (evidence level L3), pending results from ongoing and future trials, since the completed trials were terminated with one participant each
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

