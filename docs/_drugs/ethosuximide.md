---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ethosuximide: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Absence epilepsy"
monitor_inn: "Ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "nephrogenic diabetes insipidus", "insomnia (disease)", "familial mesial temporal lobe epilepsy with febrile seizures", "diabetes insipidus, nephrogenic, X-linked", "Lafora disease", "renal tubule disease", "Senior-Boichis syndrome", "psychomotor regression-oculomotor apraxia-movement disorder-nephropathy syndrome"]
---

# Ethosuximide
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

# Ethosuximide: From Absence Epilepsy to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ethosuximide is an anti-seizure medicine originally used to treat absence epilepsy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ethosuximide is generally understood to be a T-type calcium channel blocker that acts on thalamic neurons, and this underlies its efficacy in absence epilepsy.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which leads to water retention and low blood sodium. No known pathway connects T-type calcium channel blockade to this receptor or to renal water handling. The prediction therefore rests on the knowledge-graph score alone and is not supported by a plausible mechanistic link.

Other top-ranked predictions show a similar pattern:
- **Nephrogenic diabetes insipidus** (score 99.0%) and **X-linked nephrogenic diabetes insipidus** (95.3%): no trials or literature and no plausible mechanism. Anti-epileptic drugs are more often reported to cause renal tubular effects than to treat them.
- **Insomnia** (97.8%): a weak rationale exists, as thalamic T-type channels are involved in sleep spindles. However, there is no clinical evidence, and ethosuximide is not an established hypnotic.
- **Familial mesial temporal lobe epilepsy with febrile seizures** (97.1%): biologically plausible as an epilepsy, but ethosuximide is generally not effective for focal or temporal lobe seizures.
- **Childhood absence epilepsy susceptibility** (95.7%): this matches the drug's original indication, so it is not a true repurposing case.

## Clinical Trial Evidence

Currently no related clinical trials registered for nephrogenic syndrome of inappropriate antidiuresis.

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

For context, the literature retrieved for other predicted indications is limited. For **childhood absence epilepsy**, 17 papers were retrieved, made up of reviews and preclinical or animal-model studies. No randomised trials were among them. Examples include:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24530152](https://pubmed.ncbi.nlm.nih.gov/24530152/) | 2014 | Review | Pediatric Neurology | Review of recent advances in childhood absence epilepsy |
| [19632158](https://pubmed.ncbi.nlm.nih.gov/19632158/) | 2009 | Review | Epilepsy & Behavior | Review of absence seizures with new concepts |
| [17947380](https://pubmed.ncbi.nlm.nih.gov/17947380/) | 2007 | Preclinical | PNAS | Mouse model of familial childhood absence epilepsy; spike-wave discharges were blocked by ethosuximide |
| [40339636](https://pubmed.ncbi.nlm.nih.gov/40339636/) | 2025 | Preclinical | Progress in Neurobiology | Thalamocortical neuron control of absence seizures in GAERS rats, with ethosuximide-sensitive seizures |

For **renal tubule disease**, the only paper retrieved ([7843203](https://pubmed.ncbi.nlm.nih.gov/7843203/), 1994, European Journal of Pediatrics) reports renal tubular dysfunction following anti-epileptic drug treatment. This is a safety signal, not evidence of benefit.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11703Y | ZARONTIN | Capsule 250 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, haematologic disease, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis, acute intermittent porphyria.
- **Drug Interactions:** 92 interactions were identified, and the 20 listed in the data compiled for this report are all rated Moderate. Main ones include:
  - CNS depressants and sedatives: morphine (including liposomal), opium, ethanol, promethazine, chlorpheniramine, dronabinol, nabilone
  - Antimalarials: chloroquine, hydroxychloroquine, mefloquine
  - Others: aprepitant, metoclopramide, sibutramine, cobicistat, deferasirox, fostamatinib, folic acid, leucovorin, levoleucovorin

Several knowledge-graph contraindications (kidney disease, haematologic disease, neutropenia, agranulocytosis) are relevant to any renal or haematological repurposing target. Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no registered trials or relevant literature, and no plausible mechanistic link between T-type calcium channel blockade and NSIAD, which is driven by AVPR2 gain-of-function. The knowledge-graph contraindications for kidney disease add further caution.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Evidence of a biological pathway linking ethosuximide to vasopressin signalling or renal water handling
- Preclinical data in an NSIAD or AVPR2 model
- The TGA Product Information for ethosuximide warnings and contraindications
- Independent verification of the clinical evidence for the original absence epilepsy indication from primary sources, as the retrieved literature contains no randomised trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

