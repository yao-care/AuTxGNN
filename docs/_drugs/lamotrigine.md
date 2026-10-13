---
layout: default
title: Lamotrigine
parent: Moderate Evidence (L3-L4)
nav_order: 409
evidence_level: L3
indication_count: 10
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is an anticonvulsant originally used to treat epilepsy, including partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but this appears to be an artefact of the knowledge graph, with **0 clinical trials** and only **2 publications**, neither of which concerns neoplasm treatment.
The closely related prediction, **trigeminal neuralgia**, has far stronger support (**2 completed clinical trials** and **18 publications**), so it is the more credible repurposing direction and is discussed alongside the top-ranked item below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial epilepsy, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1); trigeminal neuralgia (rank 2) is the better-supported alternative |
| TxGNN Prediction Score | 99.97% (trigeminal nerve neoplasm); 99.89% (trigeminal neuralgia) |
| Evidence Level | L5 (trigeminal nerve neoplasm); L2 (trigeminal neuralgia) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (trigeminal nerve neoplasm); Proceed with Guardrails (trigeminal neuralgia) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release, which underlies its effect in epilepsy.

**Trigeminal nerve neoplasm:** The very high score appears to reflect the disease's proximity to trigeminal neuralgia in the knowledge graph, not a true anti-tumour effect. There is no evidence that lamotrigine acts on tumour biology. The two papers retrieved concern trigeminal neuralgia (a general treatment review and a Gamma Knife case report for a cavernous malformation), not neoplasm treatment.

**Trigeminal neuralgia:** The rationale here is much stronger. Trigeminal neuralgia involves focal demyelination and ectopic, hyperexcitable firing of trigeminal afferents. Sodium channel blockade dampens this firing, the same mechanism as carbamazepine and oxcarbazepine, the first-line agents. The European Academy of Neurology guideline (2019) lists lamotrigine as an add-on or second-line option. A practical constraint is the slow dose titration needed to limit rash risk (including Stevens-Johnson syndrome), which is awkward in a condition with severe acute pain.

---

## Clinical Trial Evidence

**Trigeminal nerve neoplasm:** Currently no related clinical trials registered.

**Trigeminal neuralgia:**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Lamotrigine compared with carbamazepine for efficacy and safety in trigeminal neuralgia; small sample limits conclusions |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | NA | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine in trigeminal neuralgia; underpowered |

No ANZCTR identifiers were identified in the data compiled for this report.

---

## Literature Evidence

**Trigeminal nerve neoplasm:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; not about neoplasm |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a cavernous malformation |

**Trigeminal neuralgia (selected):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on trigeminal neuralgia management |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drugs used for trigeminal neuralgia, their efficacy and side effects |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Pharmacotherapy update: carbamazepine and oxcarbazepine are effective but limited by adverse effects; newer agents are possible adjuncts |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | Practical guide to diagnosis and medical and surgical treatment |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Pathophysiology and pharmacological treatments |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Current and innovative pharmacological options for typical and atypical trigeminal neuralgia |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka | Notes lamotrigine is used off-label in Japan as an alternative to carbamazepine |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in cluster headache and trigeminal neuralgia |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13842M | Lamictal | Tablet 25 mg | Not available in the data compiled for this report |

---

## Safety Considerations

- **Key Warnings and Contraindications:** Label-based data were not available. Please refer to the TGA-approved Product Information (PI). Rash, including Stevens-Johnson syndrome, is a recognised risk with lamotrigine and drives the slow titration schedule.
- **Knowledge-graph contraindication signals (not label text):** liver disease, gallbladder disease, and haematological conditions (thrombocytopenia, neutropenia, agranulocytosis, anaemia, pancytopenia, aplastic anaemia), as well as non-infectious meningitis, anxiety disorder, neurotic disorder and dysthymic disorder. These should be checked against the PI.
- **Drug Interactions:** 100 interactions were identified in total. Moderate-level interactions include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and orlistat. Metformin is listed as minor. Several others (e.g. omeprazole, pantoprazole, doxycycline, glimepiride) have an unknown severity level.

---

## Other Predicted Indications (Brief)

| Predicted Indication | Evidence Level | Key Point | Recommendation |
|------|------|------|------|
| Startle epilepsy | L3 | Two small case series report benefit (PMIDs [10512780](https://pubmed.ncbi.nlm.nih.gov/10512780/), [21896426](https://pubmed.ncbi.nlm.nih.gov/21896426/)); no registered trials | Research Question |
| Restless legs syndrome | L3 | One 2005 pilot trial ([15680305](https://pubmed.ncbi.nlm.nih.gov/15680305/)) and case reports; no registered trials; not an established therapy | Research Question |
| Audiogenic seizures | L4 | Animal-model evidence only | Research Question |
| Orgasm-induced, eating, thinking, micturition-induced and reading seizures | L4-L5 | No indication-specific lamotrigine data; likely inferred from the parent epilepsy classification | Hold |

---

## Conclusion and Next Steps

**Decision: Hold (trigeminal nerve neoplasm, the top-ranked prediction); Proceed with Guardrails (trigeminal neuralgia)**

**Rationale:**
- The top-ranked prediction, trigeminal nerve neoplasm, has no supporting trials and no evidence of anti-tumour activity; it is most likely a knowledge-graph artefact. Trigeminal neuralgia is a plausible, guideline-recognised second-line use, supported by two small completed trials, but no adequately powered Phase 3 RCT is confirmed.

**To proceed, the following is needed:**
- Confirmation of the intended indication (neoplasm versus neuralgia) before any further work
- An adequately powered, controlled trial of lamotrigine in trigeminal neuralgia
- Detailed mechanism of action data
- The TGA-approved indication text and PI warnings and contraindications, including a rash and titration plan suited to acute pain
- Review of the haematological and hepatic signals and the drug interaction profile for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

