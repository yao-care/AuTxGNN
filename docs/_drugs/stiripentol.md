---
layout: default
title: Stiripentol
parent: Model Prediction Only (L5)
nav_order: 689
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Stiripentol: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Dravet syndrome"
monitor_inn: "Stiripentol"
predicted_indications: ["restless legs syndrome", "trigeminal nerve neoplasm", "West syndrome", "1q44 microdeletion syndrome", "episodic kinesigenic dyskinesia", "acute encephalopathy with biphasic seizures and late reduced diffusion", "PURA-related severe neonatal hypotonia-seizures-encephalopathy syndrome due to a point mutation", "neonatal period electroclinical syndrome", "Wernicke-Korsakoff syndrome", "myoclonic epilepsy, Hartung type"]
---

# Stiripentol
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

# Stiripentol: From Dravet Syndrome to Restless Legs Syndrome

## One-Sentence Summary

Stiripentol is an anti-seizure medicine originally used for severe childhood epileptic encephalopathies, including Dravet syndrome.
The TxGNN model predicts it may be effective for **restless legs syndrome**, but this is a graph-based prediction only,
with **no clinical trials** and **no publications** currently supporting this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dravet syndrome (also early myoclonic encephalopathy and developmental and epileptic encephalopathy, per the knowledge graph); the ARTG entry carries no indication text |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, stiripentol enhances GABA-A receptor signalling and inhibits lactate dehydrogenase. Its efficacy has been established in Dravet syndrome, and it may be applicable to other neurological conditions through these pathways.

The link to restless legs syndrome (RLS) is speculative. RLS is generally associated with dopaminergic and iron-related pathophysiology, which is quite different from the seizure disorders for which stiripentol is used. The high score (0.988) most likely reflects relationships within the knowledge graph rather than a validated biological connection. Because the mechanism data are incomplete, the proposed link cannot be tested.

**Other predicted indications.** The data also cover nine further predictions. Only one has any published literature:

- **West syndrome (infantile spasms)**, score 94.97%: a plausible candidate given its similarity to Dravet syndrome and the GABAergic rationale. However, the 18 retrieved publications (10 listed in the data) mostly concern Dravet syndrome and do not test stiripentol in West syndrome. Evidence level is L4, with a "Research Question" recommendation. This is the most credible lead among the predictions.
- **Closely related epilepsy-type conditions** (neonatal period electroclinical syndrome, myoclonic epilepsy Hartung type, PURA-related encephalopathy, 1q44 microdeletion syndrome): biologically plausible by disease-class similarity, but with no supporting data.
- **Poorly connected predictions** (trigeminal nerve neoplasm, Wernicke-Korsakoff syndrome, episodic kinesigenic dyskinesia, acute encephalopathy with biphasic seizures): no clear mechanistic link and likely network artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for restless legs syndrome.

## Literature Evidence

Currently no related literature available for restless legs syndrome.

For context, the literature retrieved for the rank 3 prediction (West syndrome) is summarised below. These items are indirect evidence and do not demonstrate stiripentol efficacy in West syndrome.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35490361](https://pubmed.ncbi.nlm.nih.gov/35490361/) | 2022 | Review (consensus) | Epilepsia | International consensus on diagnosis and management of Dravet syndrome |
| [26122601](https://pubmed.ncbi.nlm.nih.gov/26122601/) | 2015 | Review (task force) | Epilepsia | ILAE recommendations for managing infantile seizures; guideline, not stiripentol-specific |
| [31790543](https://pubmed.ncbi.nlm.nih.gov/31790543/) | 2020 | Clinical trial | JAMA Neurology | Fenfluramine reduced convulsive seizures in Dravet syndrome patients on stiripentol-containing regimens |
| [34274891](https://pubmed.ncbi.nlm.nih.gov/34274891/) | 2021 | Indirect comparison | Seizure | Compared add-on stiripentol, cannabidiol and fenfluramine in Dravet syndrome |
| [33388609](https://pubmed.ncbi.nlm.nih.gov/33388609/) | 2021 | Post-marketing surveillance | Epilepsy Research | Interim long-term safety and effectiveness of stiripentol in Japanese patients with Dravet syndrome |
| [39571208](https://pubmed.ncbi.nlm.nih.gov/39571208/) | 2025 | Clinical guide | Pediatric Neurology | Practical guide to using stiripentol in Dravet syndrome |
| [26933940](https://pubmed.ncbi.nlm.nih.gov/26933940/) | 2016 | Review | Expert Opinion on Pharmacotherapy | Stiripentol and vigabatrin roles in severe infantile-onset epilepsies |
| [35156171](https://pubmed.ncbi.nlm.nih.gov/35156171/) | 2022 | Review | CNS Drugs | Practical guide to anti-seizure treatment of Dravet syndrome |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12088F | Diacomit | Powder for oral suspension 500 mg | Not listed in the data compiled for this report |

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples below):

- **Major:** eliglustat.
- **Moderate:** rabeprazole, omeprazole, cimetidine, clarithromycin, aprepitant, morphine, pioglitazone, saxagliptin, dronabinol, diphenoxylate, difenoxin, eluxadoline, palonosetron, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide).

Warnings and contraindications are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for these details.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The restless legs syndrome prediction rests on the model score alone (L5). There are no trials or publications, and the mechanistic link to RLS is speculative.

**To proceed, the following is needed:**
- Mechanism of action data to assess biological plausibility
- Product Information warnings and contraindications for safety screening
- Direct preclinical or clinical evidence for stiripentol in RLS
- Separately, West syndrome could be explored as a research question, as its evidence (L4, indirect) is stronger than that of the other predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

