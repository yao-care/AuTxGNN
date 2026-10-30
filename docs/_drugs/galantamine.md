---
layout: default
title: Galantamine
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Galantamine: predicted new indication Psychogenic movement disorders (evidence level L5). Approved use: Alzheimer's disease"
monitor_inn: "Galantamine"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Galantamine: From Alzheimer's Disease to Psychogenic Movement Disorders
{: .text-alpha }

## One-Sentence Summary

Galantamine is a cholinesterase inhibitor and nicotinic receptor modulator, originally used to treat Alzheimer's disease.
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **no clinical trials and no publications** directly support this prediction.
The prediction is based on the model alone and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (the TGA indication text is not available in the data compiled for this report) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, galantamine is a cholinesterase inhibitor that also acts as an allosteric modulator of nicotinic receptors. Its efficacy in Alzheimer's disease is established, and in theory cholinergic modulation of basal ganglia circuits could influence movement control.

This link is speculative. Psychogenic movement disorders are driven by functional rather than cholinergic pathology, and no study was found that tests galantamine in this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the same set were also reviewed. Most are movement-related conditions with the same lack of evidence. The one with the most supporting literature is **lingual-facial-buccal dyskinesia (tardive dyskinesia)**, which is covered in the table below.

## Clinical Trial Evidence

Currently no related clinical trials registered for psychogenic movement disorders.

For context, the closest related finding is for tardive dyskinesia (predicted rank 7). A randomised, double-blind, placebo-controlled crossover trial of galantamine in tardive dyskinesia has been published (PMID 17388711), but the data compiled for this report did not include a registry entry or results.

## Literature Evidence

No literature was found for psychogenic movement disorders. The table below shows the most relevant publications retrieved for related movement-disorder predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17388711](https://pubmed.ncbi.nlm.nih.gov/17388711/) | 2007 | RCT (crossover) | J Clin Psychiatry | 30-week placebo-controlled trial of galantamine in tardive dyskinesia; results not available in the data compiled |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis | Prog Neuropsychopharmacol Biol Psychiatry | Cholinergic drugs for neuroleptic-induced tardive dyskinesia; class-level review, not specific to galantamine |
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Cholinergic medication for antipsychotic-induced tardive dyskinesia; class-level evidence |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier Cochrane review of cholinergic medication for tardive dyskinesia |
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic review | Brain Circ | Movement disorders associated with cholinesterase inhibitors in Alzheimer's dementia, suggesting possible aggravation rather than benefit |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | Pharmacovigilance study | Pharmacotherapy | Reports of Pisa syndrome (a form of dystonia) with cholinesterase inhibitors including galantamine |
| [25850380](https://pubmed.ncbi.nlm.nih.gov/25850380/) | 2015 | Preclinical (mouse) | J Pharmacol Sci | Interaction of galantamine with antipsychotics on extrapyramidal motor side effects |
| [18938211](https://pubmed.ncbi.nlm.nih.gov/18938211/) | 2008 | Preclinical (rat) | Neurosci Lett | Galantamine reduced striatal degeneration in a Huntington's disease model |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2463P | Reminyl | Capsule (prolonged release) 8 mg (as hydrobromide) | Not available in the data compiled |

## Safety Considerations

- **Contraindications and conditions of concern (from a knowledge graph, not label text):** familial long QT syndrome, atrioventricular block, liver failure and liver disease, kidney disease, epilepsy, asthma, chronic obstructive pulmonary disease, peptic and duodenal ulcer disease, gallbladder disease, bladder neck obstruction and pyoureter. These reflect cholinergic effects on the heart, airways, gut and urinary tract, and should be confirmed against the Product Information.
- **Drug Interactions:** 100 interactions were identified. The one rated **Major** was **bupropion**. Examples rated **Moderate** include:
  - Anticholinergics and antispasmodics (atropine, hyoscyamine, dicyclomine, glycopyrronium, clidinium, trospium), which may oppose galantamine's effect
  - Acid suppressants (famotidine, ranitidine, cimetidine)
  - Clarithromycin, metronidazole, loperamide, palonosetron, dolasetron, eliglustat and lorcaserin
- **Movement-related risk:** Cholinesterase inhibitors have been linked to movement disorders such as tremor, parkinsonism and Pisa syndrome (PMIDs 40224553, 24127392). This is a concern when the target condition is itself a movement disorder.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by the model score alone (L5), with no trials or publications for psychogenic movement disorders and no plausible mechanism. Related literature suggests cholinesterase inhibitors may worsen some movement disorders.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic rationale for functional movement disorders
- The TGA-approved Product Information, including indications, warnings and contraindications
- Any clinical or case-series evidence in psychogenic movement disorders
- If a movement-disorder direction is pursued, tardive dyskinesia is the more evidence-supported candidate. It would first need a galantamine-specific review of the existing RCT (PMID 17388711).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

