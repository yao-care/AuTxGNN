---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phenobarbital: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
---

# Phenobarbital
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

# Phenobarbital: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a long-established barbiturate anticonvulsant, originally used for epilepsy (including generalised tonic-clonic and partial seizures) and some headache disorders.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **no registered clinical trials** and only **1 publication** (an unrelated case series), so the top prediction is effectively unsupported.
Several lower-ranked predictions (reflex epilepsies such as audiogenic, startle and reading seizures) are far more biologically plausible, but they are extensions of the existing epilepsy use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the data compiled for this report contains no TGA-approved indication text; the original indications come from the knowledge graph and include generalised tonic-clonic epilepsy, partial epilepsy, Lennox-Gastaut syndrome and migraine/headache disorders) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, phenobarbital enhances GABA-A receptor-mediated inhibition, and its efficacy in epilepsy is well established.

**For the top-ranked prediction (trigeminal nerve neoplasm), the rationale is weak.** The only retrieved paper is a case series on Sturge-Weber syndrome, a neurocutaneous disorder with seizures, not a trigeminal nerve tumour. Phenobarbital has no known antineoplastic activity. The high score most likely reflects graph proximity to seizure and trigeminal-related nodes rather than a true therapeutic link.

**The more credible predictions are seizure-related.** Thinking, audiogenic, eating, orgasm-induced, startle, micturition-induced and reading seizures are all rare reflex epilepsies. Phenobarbital's GABAergic anticonvulsant action makes these plausible, but this is largely an extension of its existing epilepsy indication. Trigeminal neuralgia (rank 9) has a theoretical rationale through anticonvulsant therapy, but carbamazepine is the standard agent and no direct phenobarbital efficacy data were retrieved. Beta-ketothiolase deficiency (rank 10) has no credible mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predicted indications.

---

## Literature Evidence

Evidence for the top-ranked prediction (trigeminal nerve neoplasm):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases (clinical features, course, treatment response); not about trigeminal nerve tumours |

Selected supporting literature for the more plausible seizure-related predictions (indirect evidence):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures; general seizure evidence, not reflex-seizure specific |
| [37873971](https://pubmed.ncbi.nlm.nih.gov/37873971/) | 2023 | Systematic review | Cochrane Database Syst Rev | Anti-seizure medications in neonates |
| [37655702](https://pubmed.ncbi.nlm.nih.gov/37655702/) | 2023 | Guideline | Epilepsia | ILAE recommendations on treating neonatal seizures |
| [23515971](https://pubmed.ncbi.nlm.nih.gov/23515971/) | 2013 | Systematic review | CNS Drugs | Pharmacotherapy of focal epilepsy in children |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | RCT (veterinary) | J Feline Med Surg | Levetiracetam vs phenobarbital in feline audiogenic reflex seizures |
| [27057183](https://pubmed.ncbi.nlm.nih.gov/27057183/) | 2016 | RCT | Iran J Child Neurol | Intermittent diazepam vs continuous phenobarbital to prevent febrile seizure recurrence |
| [24726506](https://pubmed.ncbi.nlm.nih.gov/24726506/) | 2014 | Case report | Seizure | Neonatal eating epilepsy, 50-year follow-up |
| [7259585](https://pubmed.ncbi.nlm.nih.gov/7259585/) | 1981 | Case report | Arq Neuropsiquiatr | Food-induced seizures; best response to valproate, clonazepam and phenobarbital combined |
| [42022979](https://pubmed.ncbi.nlm.nih.gov/42022979/) | 2026 | Case report | Clin Case Rep | Infant with sound-triggered events: reflex epilepsy vs exaggerated startle |
| [10416094](https://pubmed.ncbi.nlm.nih.gov/10416094/) | 1999 | Cohort | Clin Pediatr | Lowered IQ persisted after early phenobarbital treatment for febrile seizures |

No literature was retrieved for orgasm-induced seizures or beta-ketothiolase deficiency.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1850J | Phenobarb | Tablet 30 mg (oral) | Approved indication text not available |

---

## Safety Considerations

**Contraindications / conditions of concern (from drug-disease relationships in the knowledge graph, not label text):** liver failure and liver disease, kidney disease, porphyria (including inherited porphyria), chronic obstructive pulmonary disease, hypothyroidism, thrombocytopenia, hyperglycaemia, peptic/gastric ulcer and gastritis, systemic lupus erythematosus, anxiety, dysthymic and other psychotic or mental disorders, hypertension, and gallbladder disease.

**Drug Interactions:** 100 interactions were identified. Major interactions include morphine (including liposomal), eliglustat, naldemedine, naloxegol and rolapitant. Moderate interactions include corticosteroids (dexamethasone, hydrocortisone, prednisolone, prednisone, betamethasone, triamcinolone), doxycycline, metronidazole, pioglitazone, bupropion, aprepitant, dronabinol, cholecalciferol and pyridoxine.

**Additional safety signals from the retrieved literature:**
- Early-life exposure was linked to neuronal apoptosis and long-term cognitive and behavioural effects in animal studies, and to lowered IQ in children treated for febrile seizures.
- Antiepileptic drug exposure in utero is associated with congenital malformations and adverse cognitive outcomes.
- Anticonvulsant hypersensitivity syndrome and enzyme induction (affecting carbamazepine and other drugs) are recognised concerns.

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications, as label data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (trigeminal nerve neoplasm) has no clinical trials, a single irrelevant publication and no plausible antineoplastic mechanism, so the score is likely a graph artefact. The seizure-related predictions are mechanistically plausible but are extensions of the established epilepsy indication with only indirect or preclinical evidence (L4), and are better treated as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to support mechanistic analysis
- TGA Product Information warnings and contraindications for the ARTG-listed product, and its approved indication text (currently blocking safety screening)
- If pursuing a seizure-related indication, targeted evidence in the specific reflex epilepsy (case series or controlled data), with a review of how this differs from the existing epilepsy indication
- For trigeminal neuralgia, comparative evidence against carbamazepine and a plan for managing enzyme-induction interactions
- No further work is recommended for trigeminal nerve neoplasm, orgasm-induced seizures or beta-ketothiolase deficiency unless new supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

