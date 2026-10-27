---
layout: default
title: Levetiracetam
parent: Model Prediction Only (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Levetiracetam: predicted new indication Visual epilepsy (evidence level L5). Approved use: Partial epilepsy"
monitor_inn: "Levetiracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Levetiracetam
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

## Levetiracetam: From Partial Epilepsy to Visual Epilepsy
{: .text-alpha }

## One-Sentence Summary

Levetiracetam is an antiseizure medication originally used to treat partial (focal) epilepsy.
The TxGNN model predicts it may be effective for **visual epilepsy** (a reflex epilepsy triggered by visual stimuli), but no clinical trials and only general seizure literature support this specific prediction.
The strongest evidence in the data compiled for this report is for a related prediction, **status epilepticus**, which is supported by **16 registered clinical trials** and **20 publications**, including large Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy (the TGA licence record contains no approved indication text) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (for visual epilepsy; L1 for the related prediction, status epilepticus) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (for visual epilepsy); Proceed with Guardrails for status epilepticus |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, levetiracetam binds to synaptic vesicle protein 2A (SV2A) and modulates neurotransmitter release. This plausibly reduces the cortical hyperexcitability seen in photosensitive or visually triggered seizures.

Visual epilepsy is a form of reflex epilepsy, and levetiracetam is already established in focal epilepsy. Mechanistically, it may be applicable. However, the retrieved literature covers general seizure populations (neonatal, post-stroke, neurocritical care, feline epilepsy) and does not address visually induced epilepsy specifically. The high TxGNN score likely reflects the drug's general antiseizure class effect rather than disease-specific evidence.

Other top-ranked predictions are all seizure-related. Several are reflex epilepsies (startle, audiogenic, reading, eating, micturition-induced, thinking and orgasm-induced seizures). Status epilepticus has the strongest evidence. One prediction, beta-ketothiolase deficiency, has no evident mechanistic link and appears to be a graph-based artefact.

---

## Clinical Trial Evidence

No clinical trials are registered for visual epilepsy. Currently no related clinical trials registered for this prediction.

For context, the related prediction **status epilepticus** (rank 9) has the following key trials:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | Completed | 478 | ESETT: fosphenytoin vs valproic acid vs levetiracetam in benzodiazepine-refractory status epilepticus; comparable efficacy |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | Completed | 203 | IV levetiracetam plus clonazepam vs clonazepam alone in prehospital generalised tonic-clonic status epilepticus |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | Completed | 80 | Levetiracetam vs sodium valproate in children with refractory generalised convulsive status epilepticus |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | Completed | 144 | Levetiracetam plus midazolam in paediatric generalised convulsive status epilepticus |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Phase 4 | Completed | 62 | Open-label levetiracetam vs fosphenytoin in convulsive status epilepticus |
| [NCT04176887](https://clinicaltrials.gov/study/NCT04176887) | Phase 4 | Unknown | 60 | Levetiracetam vs phenytoin in paediatric status epilepticus |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | Recruiting | 124 | Ketamine plus levetiracetam vs levetiracetam alone in children with benzodiazepine-refractory convulsive status epilepticus |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Phase 3 | Recruiting | 770 | KESETT: ketamine plus levetiracetam vs levetiracetam alone in established status epilepticus |
| [NCT00362141](https://clinicaltrials.gov/study/NCT00362141) | Phase 2 | Unknown | 12 | Safety and tolerability of add-on levetiracetam in status epilepticus |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | Not specified | Completed | 138 | Levetiracetam vs valproic acid in paediatric status epilepticus |

No ANZCTR identifiers were included in the data compiled for this report.

---

## Literature Evidence

For visual epilepsy, the retrieved literature is general to seizures and not disease-specific. Selected items:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | Lancet Neurol | PEACH: prophylactic levetiracetam for seizure prevention in acute intracerebral haemorrhage |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocrit Care | Levetiracetam for seizure prophylaxis in neurocritical care |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Network meta-analysis | Neurology | Antiseizure medications in poststroke seizures |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Meta-analysis | Epilepsy Behav | Levetiracetam for myoclonic seizures in idiopathic generalised epilepsy |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with encephalitis |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam in epilepsy |

Key literature for the related prediction (status epilepticus):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | Three anticonvulsants (including levetiracetam) in benzodiazepine-refractory status epilepticus |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT | Lancet | ESETT by age group: levetiracetam, fosphenytoin and valproate |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | EcLiPSE: levetiracetam as an alternative to phenytoin in children |

Disease-specific reports also exist for other reflex-seizure predictions, for example startle epilepsy (PMID [18486495](https://pubmed.ncbi.nlm.nih.gov/18486495/), an uncontrolled add-on study) and reading epilepsy (PMID [22386591](https://pubmed.ncbi.nlm.nih.gov/22386591/), a small case series).

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13937M | Levactam | Tablet 1 g (oral) | Not recorded in the data compiled for this report |

---

## Safety Considerations

Contraindication and warning text from the product label was not available. The knowledge graph links levetiracetam to the following conditions through drug-disease contraindication edges (these are not label text and need verification against the PI):

- **Psychiatric:** anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, depersonalisation disorder
- **Haematological:** neutropenia, agranulocytosis, leukopenia, pancytopenia
- **Organ disease:** kidney disease, liver disease, gallbladder disease, pyoureter

**Drug interactions:** The interaction query returned 100 records. Those rated Moderate include morphine (including liposomal), dronabinol, metoclopramide, nabilone, opium and sibutramine. Other entries have an unknown severity rating.

The retrieved literature also reports adverse effects including hyponatraemia and gingival hyperplasia (case reports), and renal dose adjustment is relevant given the pharmacokinetic studies in haemodialysis and haemofiltration.

Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (visual epilepsy)

**Rationale:**
The visual epilepsy prediction rests on a high model score and a plausible SV2A mechanism, with no registered trials and no disease-specific literature. The evidence level is L4. By contrast, status epilepticus (L1) has Phase 3 RCT support showing levetiracetam is comparable to fosphenytoin and valproate, and could proceed with guardrails. That evidence supports equivalence rather than superiority.

**To proceed, the following is needed:**
- Disease-specific clinical data for visual or photosensitive epilepsy (for example, a photoparoxysmal response study, noting the related SV2A ligand seletracetam has a Phase 2 trial in this setting)
- Mechanism of action data to be confirmed from DrugBank
- TGA Product Information, including the approved indication text, warnings and contraindications, which were missing from the data compiled for this report
- Clarification of whether the status epilepticus use is already covered by the current ARTG indication, and which formulations (IV) are available in Australia, since the single ARTG entry is an oral 1 g tablet
- For any reflex-epilepsy extension, a safety monitoring plan covering behavioural and psychiatric effects, haematological effects and renal dose adjustment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

