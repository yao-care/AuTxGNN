---
layout: default
title: Brivaracetam
parent: Model Prediction Only (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brivaracetam: predicted new indication Visual epilepsy (evidence level L5). Approved use: Partial epilepsy"
monitor_inn: "Brivaracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Brivaracetam
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

# Brivaracetam: From Partial Epilepsy to Status Epilepticus

## One-Sentence Summary

Brivaracetam is an antiseizure medicine originally used for partial (focal) epilepsy.
The TxGNN model ranks **visual epilepsy** as its top prediction, but the best-supported prediction in the data compiled for this report is **status epilepticus**, with **1 completed clinical trial** and **19 publications** (including two systematic reviews of intravenous brivaracetam).
Evidence for status epilepticus is mostly observational, so it remains at a preliminary level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy; partial motor epilepsy (the Australian licence entry has no indication text) |
| Predicted New Indication | Visual epilepsy (rank 1); status epilepticus (rank 2) is the best-supported candidate and is evaluated in detail below |
| TxGNN Prediction Score | 99.51% for visual epilepsy; 99.40% for status epilepticus |
| Evidence Level | Visual epilepsy: L4 (indirect). Status epilepticus: L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Visual epilepsy: Hold (research question only). Status epilepticus: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, brivaracetam is a high-affinity ligand of synaptic vesicle protein 2A (SV2A), a propyl analogue of levetiracetam. It binds SV2A with roughly 15 to 30 times the affinity of levetiracetam and penetrates the brain rapidly. Binding to SV2A reduces synaptic vesicle-mediated neurotransmitter release.

**Visual epilepsy (top-ranked prediction).** Visual (photosensitive or occipital) epilepsy is a seizure disorder in the same therapeutic area as the approved focal seizure indication, so a shared antiseizure mechanism is plausible. However, no trial or study specific to visual epilepsy was found. The retrieved literature consists of general epilepsy and status epilepticus reviews and an adjunctive focal-onset seizure trial, all indirect.

**Status epilepticus (best-supported prediction).** Intravenous brivaracetam has a rapid onset of action, which suits emergency seizure control, and it is used off-label in this setting. One paper also examines brivaracetam against levetiracetam using the photosensitivity model, which links to the visual epilepsy prediction.

---

## Clinical Trial Evidence

Evidence below relates to status epilepticus. No clinical trials were registered for visual epilepsy.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | Not applicable | Completed | 152 | IV brivaracetam vs levetiracetam in paediatric status epilepticus; no results provided in the data compiled |

No ANZCTR trial identifiers were found in the data compiled.

---

## Literature Evidence

Evidence below relates to status epilepticus (priority given to systematic reviews and directly relevant studies).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41838218](https://pubmed.ncbi.nlm.nih.gov/41838218/) | 2026 | Systematic review | J Neurol | Brivaracetam for status epilepticus; efficacy and safety described as inadequately characterised |
| [32278203](https://pubmed.ncbi.nlm.nih.gov/32278203/) | 2020 | Systematic review | J Neurol Sci | IV brivaracetam may be an alternative anticonvulsant; controlled studies are sparse |
| [31342405](https://pubmed.ncbi.nlm.nih.gov/31342405/) | 2019 | Systematic review | CNS Drugs | IV brivaracetam's rapid onset and brain permeability make it potentially suited to emergencies |
| [32822230](https://pubmed.ncbi.nlm.nih.gov/32822230/) | 2020 | Review | Epilepsy Curr | American Epilepsy Society review of parenteral antiseizure medicines in refractory convulsive status epilepticus |
| [26891946](https://pubmed.ncbi.nlm.nih.gov/26891946/) | 2016 | Review | Expert Rev Clin Pharmacol | Brivaracetam in focal and idiopathic generalised epilepsies and status epilepticus |
| [31260101](https://pubmed.ncbi.nlm.nih.gov/31260101/) | 2019 | Multicentre registry | Epilepsia | Use of IV brivaracetam in status epilepticus |
| [33561784](https://pubmed.ncbi.nlm.nih.gov/33561784/) | 2021 | Retrospective study | Seizure | Italian multicentre retrospective study of IV brivaracetam in status epilepticus |
| [41043236](https://pubmed.ncbi.nlm.nih.gov/41043236/) | 2025 | Real-world study | Epilepsy Behav | Switching from IV to oral brivaracetam after status epilepticus and cluster seizures |
| [32480279](https://pubmed.ncbi.nlm.nih.gov/32480279/) | 2020 | Case series | Seizure | Brivaracetam in absence status epilepticus |
| [36528008](https://pubmed.ncbi.nlm.nih.gov/36528008/) | 2023 | Review | Epilepsy Behav | Brivaracetam vs levetiracetam in status epilepticus, drawing on the photosensitivity model |

For visual epilepsy, the top-ranked prediction, the retrieved literature is general (epilepsy reviews and one adjunctive focal-onset trial, [PMID 38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/)) and does not address the condition directly.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Licence 11327E | Briviact | Tablet 25 mg (oral) | Not listed in the data compiled |

Only the oral tablet is recorded. The intravenous formulation relevant to status epilepticus is not listed in the data compiled, so route availability needs confirming.

---

## Safety Considerations

- **Drug Interactions:** 69 interactions were recorded. Examples at moderate level include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide, promethazine, ethanol, diphenoxylate, difenoxin, sibutramine and clopidogrel. This pattern suggests additive central nervous system depression with opioids, cannabinoids, alcohol and sedating agents. Minor interactions include proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole), sulfonylureas (chlorpropamide, tolbutamide) and cilostazol.
- **Behavioural adverse events:** Published reviews describe irritability, anger and aggression with brivaracetam and related agents (see [PMID 33839453](https://pubmed.ncbi.nlm.nih.gov/33839453/)).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision:**
- **Status epilepticus: Proceed with Guardrails** (L3)
- **Visual epilepsy: Hold, as a research question only** (L4, no direct evidence)
- **Other lower-ranked predictions** (orgasm-induced seizures, thinking seizures, startle epilepsy, eating seizures, beta-ketothiolase deficiency, and the autosomal dominant epilepsy with auditory features): Hold, with no trials or literature. Audiogenic seizures and micturition-induced seizures have only indirect preclinical or general literature support. The beta-ketothiolase deficiency score is likely a graph artefact.

**Rationale:**
- Status epilepticus has two systematic reviews, several registries and retrospective studies, and one completed paediatric trial without a phase designation or results. This is enough to support a guarded pathway but not to raise the evidence level above L3.
- Visual epilepsy has the highest model score but no direct study.

**To proceed, the following is needed:**
- Results from NCT07163572, and ideally a randomised controlled trial of IV brivaracetam in status epilepticus
- Confirmation of whether an IV brivaracetam product is registered in Australia, and its approved indications
- TGA Product Information warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A direct study of brivaracetam in visual (photosensitive) epilepsy before this prediction is advanced
- A review of interaction risk with opioids, alcohol and other sedating agents in acute care settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

