---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

> Levetiracetam is a widely used second-generation antiepileptic drug, established globally for partial-onset seizures (with or without secondary generalisation) and other seizure types.
> The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype),
> with **9 clinical trials** and **20 publications** currently identified in this evidence pack — though none directly and specifically studies visual/photosensitive epilepsy as the primary endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset seizures, with adjunctive use in myoclonic and primary generalised tonic-clonic seizures (established global indication per literature in this evidence pack; no Australian ARTG/PI text available — see Market Status) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (preclinical/mechanistic; no controlled trials specific to visual epilepsy) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question (Decision Stage S1) |

---

## Why is This Prediction Reasonable?

Detailed, Australia-specific mechanism-of-action documentation is not available in this evidence pack (flagged as a High-severity data gap, DG002 — recommended remediation: query DrugBank API). Based on the literature captured here, levetiracetam is an established second-generation antiepileptic drug that binds synaptic vesicle protein 2A (SV2A), modulating neurotransmitter release and broadly dampening cortical hyperexcitability. It is approved worldwide as adjunctive and monotherapy treatment of partial-onset seizures, and as adjunctive treatment of myoclonic seizures in juvenile myoclonic epilepsy and primary generalised tonic-clonic seizures.

Visual epilepsy (photosensitive/reflex epilepsy) is thought to arise from excessive occipital cortical excitability triggered by visual stimuli — mechanistically the same broad category of cortical hyperexcitability that levetiracetam's SV2A-mediated action is designed to suppress. This provides biological plausibility for the TxGNN prediction.

However, the rationale supplied with this candidate is explicit that the supporting evidence is indirect: all 9 clinical trials and 20 publications identified relate to general epilepsy, status epilepticus, or neonatal seizures, and none specifically enrolled or studied patients with visual/photosensitive epilepsy. The prediction should therefore be read as mechanistically plausible but clinically unproven for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Tests whether levetiracetam reduces hippocampal hyperactivity in psychotic disorders using fMRI during a visual scene-processing task; not a visual-epilepsy efficacy trial. |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Efficacy of levetiracetam in control of neonatal seizures (general seizure population). |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Liceo Study — observational effectiveness of newer AEDs (including levetiracetam) as first bitherapy in focal epilepsy. |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | AVASPA gene therapy trial for Canavan disease; levetiracetam relevance is incidental/background rather than a study intervention. |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST trial — optimal duration/agent (phenytoin vs levetiracetam) for seizure prophylaxis after traumatic brain injury. |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Randomised placebo-controlled study of cognitive/neuropsychological effects of adjunctive levetiracetam in children with refractory partial-onset seizures. |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for migraine prophylaxis, with or without visual aura. |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | Randomised placebo-controlled trial of prophylactic levetiracetam for functional outcome after intracerebral haemorrhage. |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated (enrolment n=1) | 1 | Same hippocampal-hyperactivity/psychosis mechanism study as NCT04559529; terminated early. |

None of the above trials directly evaluate levetiracetam in a visual/photosensitive epilepsy population.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures — randomised comparison of efficacy and safety. |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Med J | Randomised comparison of phenobarbital and levetiracetam efficacy/tolerability in childhood epilepsy. |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | Open-label RCT | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome. |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in ICH, TBI, neurosurgery and SAH — efficacy, dosing and adverse events remain unclear. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network Meta-analysis | J Neurology | Comparative efficacy/safety of antiseizure medications (including levetiracetam) for idiopathic generalised epilepsies. |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalised epilepsy, including juvenile myoclonic epilepsy. |
| [35538830](https://pubmed.ncbi.nlm.nih.gov/35538830/) | 2023 | Meta-analysis | CNS Neurol Disord Drug Targets | Safety/effectiveness comparison of levetiracetam vs phenytoin in paediatric status epilepticus. |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review/Network Meta-analysis | Seizure | Treatment options, including levetiracetam, for benzodiazepine-resistant status epilepticus. |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam's approved indications and clinical profile in epilepsy ("Spotlight" review). |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arq Neuropsiquiatr | General review of status epilepticus diagnosis, monitoring and treatment. |

All identified literature addresses levetiracetam in general epilepsy/status epilepticus contexts; none specifically studies visual or photosensitive epilepsy.

---

## Australia Market Information

Levetiracetam is currently **not marketed** in Australia under this evidence pack, with **0 ARTG entries** recorded. No product listing, dosage form, or approved-indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable for this evidence pack (TFDA/TGA labelling data gap — DG001, Blocking severity — must be resolved before any S1 safety pre-screen can proceed).

---

## Conclusion and Next Steps

**Decision: Research Question (Decision Stage S1)**

**Rationale:**
The mechanistic link between levetiracetam's SV2A-mediated anti-hyperexcitability action and visual epilepsy's cortical hyperexcitability is biologically plausible, but every identified trial and publication addresses general epilepsy, status epilepticus, or neonatal seizures rather than visual/photosensitive epilepsy specifically — there is no direct clinical evidence for this indication.

**To proceed, the following is needed:**
- TGA-approved Product Information — key warnings, contraindications, and drug interaction data (Blocking gap, DG001)
- Confirmed mechanism-of-action detail from DrugBank (High-priority gap, DG002)
- A trial or case series enrolling patients specifically diagnosed with visual/photosensitive epilepsy
- Formal ARTG registration status confirmation, since the drug is currently not marketed in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

