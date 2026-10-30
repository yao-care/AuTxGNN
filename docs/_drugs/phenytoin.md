---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Phenytoin: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is a long-established antiseizure medicine, originally used for epilepsy, including generalised tonic-clonic seizures, partial seizures and status epilepticus.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no clinical trials** and **no literature that actually addresses a neoplasm** to support it. The two retrieved papers concern trigeminal neuralgia and Sturge-Weber syndrome.
The more credible signals in the ranked list are for **trigeminal neuralgia** (supported by guidelines, reviews and retrospective clinical studies) and for reflex-seizure subtypes of epilepsy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Phenytoin is generally understood to block voltage-gated sodium channels and limit repetitive neuronal firing, which underpins its efficacy in epilepsy.

For the top-ranked prediction, **trigeminal nerve neoplasm**, this mechanism offers no established antitumour rationale. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (such as trigeminal nerve pain and seizure phenotypes), not biological evidence. The retrieved papers (a review of trigeminal neuralgia and a case series on Sturge-Weber syndrome) do not study a neoplasm.

Several other predictions are more plausible mechanistically:

- **Trigeminal neuralgia (rank 9):** Sodium channel blockade reduces ectopic firing in trigeminal afferents, the same principle behind carbamazepine's efficacy. Phenytoin is regarded as a second-line or limited-evidence option, and carbamazepine and oxcarbazepine remain first-line.
- **Reflex and stimulus-triggered seizures (startle, thinking, orgasm-induced, eating, audiogenic, micturition-induced and reading seizures):** These are subtypes of epilepsy, which is already an approved indication, so they are not true repurposing. Evidence is limited to case reports and animal models.
- **Beta-ketothiolase deficiency (rank 10):** This is a metabolic disorder with no mechanistic link to phenytoin, and the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for the top-ranked indication or for any of the ten predicted indications.

---

## Literature Evidence

**Top-ranked prediction (trigeminal nerve neoplasm):** no literature addresses a neoplasm.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; not about a neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 cases of Sturge-Weber syndrome; not about a neoplasm |

**Most relevant literature for the more plausible predictions:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on trigeminal neuralgia management |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Clinical study | Cephalalgia | Retrospective analysis of 144 cases of IV lacosamide and phenytoin for acute trigeminal neuralgia exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Retrospective cohort | Headache | IV phenytoin as acute rescue treatment for trigeminal neuralgia crisis |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Res | Contrasts phenytoin and carbamazepine in trigeminal neuralgia as marketing-based versus evidence-based treatment |
| [22592741](https://pubmed.ncbi.nlm.nih.gov/22592741/) | 2012 | Cochrane review | Cochrane Database Syst Rev | Phenytoin for neuropathic pain and fibromyalgia in adults |
| [21561835](https://pubmed.ncbi.nlm.nih.gov/21561835/) | 2011 | Case report | Epileptic Disord | Reflex seizures induced by micturition and defecation, successfully treated with clobazam and phenytoin |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | Open-label RCT | Seizure | Phenytoin versus levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [10719079](https://pubmed.ncbi.nlm.nih.gov/10719079/) | 2000 | Preclinical | Brain Res | Phenytoin effects on brainstem neuronal firing in audiogenic seizures in rats |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1249R | Dilantin Infatabs | Tablet 50 mg (oral) | Indication text not available in the data compiled |

---

## Safety Considerations

Product Information warnings and contraindications were not available in the data compiled for this report, so please refer to the TGA-approved Product Information (PI) for label safety information.

**Contraindication-related conditions flagged in the knowledge graph** (these are not label text and should be verified against the PI):
- Cardiac: long QT syndrome (including familial), torsades de pointes, hypotensive disorder
- Hepatic: liver failure, liver disease, gallbladder disease, hepatic coma and encephalopathy
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, porphyria and other porphyrin metabolism disorders
- Other: kidney disease, systemic lupus erythematosus, anxiety and neurotic disorders, dysthymic disorder, substance abuse/dependence, sleep apnoea syndromes, congenital central hypoventilation syndrome

**Drug interactions:** The interaction screen returned 100 interactions. Those listed were mostly moderate in severity, including:
- Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, albiglutide
- Acid suppressants: famotidine, ranitidine, omeprazole
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Others: doxycycline, metronidazole, bupropion, aprepitant, morphine, cholecalciferol, calcifediol

Acetylsalicylic acid was the one minor interaction listed.

**Safety signals in the retrieved literature** include phenytoin-induced thrombocytopenia, hyperglycaemia and diabetic ketoacidosis, peripheral neuropathy, ophthalmoplegia at high serum levels, gingival hyperplasia, EMPACT syndrome (erythema multiforme with cranial radiation), bone health effects, and the exacerbation of acute porphyria.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, has no clinical trials, no supporting literature on a neoplasm and no plausible antitumour mechanism, so it is prediction-only (L5). The score looks like a TxGNN model (deep learning) artefact linked to trigeminal pain and seizure phenotypes. Trigeminal neuralgia (L3, with guideline-level and retrospective support) is the most credible new direction, but phenytoin remains a second-line option behind carbamazepine and oxcarbazepine, and no Phase 3 RCT was identified. The seizure subtypes largely fall under the existing epilepsy indication.

**To proceed, the following is needed:**
- Re-evaluate the candidate with trigeminal neuralgia as the lead indication, and check whether the original prediction is a labelling or mapping error
- Detailed mechanism of action data (MOA) from DrugBank
- TGA Product Information with warnings, contraindications and the approved indication text for ARTG 1249R
- A prospective or controlled evidence review for phenytoin in trigeminal neuralgia, including the oral formulation (the evidence found is mainly for IV use, whereas the registered product is an oral tablet)
- A safety plan covering the flagged cardiac, hepatic, haematological and metabolic risks and the high number of drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

