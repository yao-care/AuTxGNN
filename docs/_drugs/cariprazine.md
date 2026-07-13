---
layout: default
title: Cariprazine
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Cariprazine
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

# Cariprazine: From Schizophrenia/Bipolar Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Cariprazine is an atypical antipsychotic acting as a dopamine D3/D2 receptor partial agonist, approved internationally (US, EU) for schizophrenia and bipolar disorder, but not currently registered in Australia.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, with **no clinical trials** and **15 background publications** identified — none of which are specific to Cariprazine in this condition.
This prediction is currently at hypothesis-generation stage only, and all 10 top-ranked predictions share the same L5 evidence level, warranting a uniform Hold decision at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia (overseas approved use: schizophrenia, bipolar disorder) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 98.70% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this Evidence Pack. Based on published international literature, Cariprazine (DrugBank DB06016) is a dopamine D3-preferring D2/D3 partial agonist with additional partial agonism at serotonin 5-HT1A receptors and antagonism at 5-HT2B receptors. It is approved by the US FDA and EMA for schizophrenia and bipolar I disorder (manic/mixed episodes and bipolar depression), marketed as Vraylar (US) and Reagila (EU). It has not received TGA approval in Australia.

The theoretical mechanistic link to retinal dystrophy is highly indirect. Dopaminergic signalling is present in retinal amacrine cells, which express D2 and D3 receptors and play a role in light adaptation, retinal circadian rhythmicity, and modulation of photoreceptor function. In principle, a D3/D2 partial agonist could theoretically influence retinal dopamine tone. However, retinal dystrophies such as the condition predicted here are predominantly caused by inherited mutations in photoreceptor-specific or ciliary genes (e.g. *RPGR*, *RPGRIP1*, *CEP290*), with pathology driven by photoreceptor degeneration rather than dopaminergic dysregulation.

This prediction is most likely an artefact of knowledge graph neighbourhood effects — Cariprazine's neurological drug class node sits in proximity to retinal and ocular disease nodes via shared neurological pathway edges, rather than a direct biological mechanism. The 15 publications retrieved are general ophthalmology reviews and case reports covering orbital infections, congenital ptosis, ocular motility disorders, and related structural conditions; none specifically investigate Cariprazine or any D2/D3 agent in retinal dystrophy. Substantial preclinical mechanistic validation would be required before any clinical consideration of this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> **Note:** The 15 publications retrieved are general ophthalmology background references. None are specific to Cariprazine or any dopamine receptor modulator in retinal dystrophy. They were returned based on keyword overlap with extraocular anomalies.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of paediatric ocular pathologies, including congenital lesions and retinal conditions |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies and associated anterior segment dysgenesis |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research | Int J Mol Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM) due to KIF21A/TUBB3 mutations |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Therapeutic Advances in Ophthalmology | Eye involvement across inherited metabolic disorders, including retinal and optic pathway changes |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | Neuroradiological evaluation and differential diagnosis of ophthalmoplegia |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Classification and clinical features of congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Research | American Journal of Ophthalmology | Pathogenesis and proposed treatment of maculopathy associated with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Isolated trochlear-oculomotor synkinesis in a child — rare congenital cranial dysinnervation variant |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis classification, pathophysiology, and surgical management options |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: myopia, vitreoretinal degeneration, and associated systemic anomalies |

---

## Australia Market Information

Cariprazine is not registered with the Therapeutic Goods Administration (TGA) and has **no ARTG entries**. It is not commercially available in Australia through standard channels. Prescribers seeking access would need to apply via the TGA's Special Access Scheme (SAS Category B) or Authorised Prescriber pathway, referencing international product information (US FDA label or EMA Summary of Product Characteristics).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Cariprazine is not registered in Australia, prescribers should consult the TGA Special Access Scheme documentation and international prescribing information for current safety data.

> Based on international labelling (not Evidence Pack data), Cariprazine carries class-level antipsychotic warnings including tardive dyskinesia, neuroleptic malignant syndrome, metabolic effects, and QT interval considerations. It is metabolised primarily via CYP3A4. These details must be verified against current international product information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked TxGNN predictions for Cariprazine are rated L5 (model prediction only), with no clinical trial evidence and no drug-specific literature supporting any of the predicted indications — which are predominantly rare structural, genetic, or developmental conditions with no plausible direct dopaminergic mechanistic link. Cariprazine's absence from the Australian market adds a further regulatory barrier to any repurposing pathway.

**To proceed, the following is needed:**

- **Regulatory baseline**: Establish a TGA registration or SAS access pathway for Cariprazine in Australia before any repurposing clinical work can be initiated
- **MOA documentation**: Obtain full mechanism of action data from DrugBank (currently a blocking data gap — DG002) and TGA/international PI
- **Safety profile review**: Download and parse international Product Information (FDA/EMA) to complete the blocking safety data gap (DG001) and confirm contraindications, warnings, and drug interactions
- **Mechanistic prioritisation**: If further evaluation is warranted, syndromic myopia (rank 6) represents the most mechanistically coherent candidate — retinal dopamine's known role in axial elongation and myopia protection is at least biologically grounded — and should be the first indication assessed in a formal scoping review
- **Preclinical evidence sweep**: Commission a targeted literature review specifically combining "cariprazine OR D3 agonist OR D2/D3 partial agonist" with retinal or ocular endpoints, to determine whether any in vitro or animal data exists before committing to clinical hypothesis testing
- **KG bias assessment**: Investigate whether the high TxGNN scores across these rare structural and developmental conditions reflect genuine biological signal or knowledge graph neighbourhood artefacts from proximity of psychiatric drug nodes to neurodevelopmental disease nodes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

