---
layout: default
title: Edaravone
parent: Model Prediction Only (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Edaravone: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Ischaemic stroke and amyotrophic lateral sclerosis"
monitor_inn: "Edaravone"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "bilateral parasagittal parieto-occipital polymicrogyria", "antithrombin deficiency type 2", "axial spondylometaphyseal dysplasia", "amyotrohpic lateral sclerosis type 22", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "Mills syndrome", "lower motor neuron syndrome with late-adult onset"]
---

# Edaravone
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

## Edaravone: From Ischaemic Stroke and ALS to Heparin Cofactor 2 Deficiency
{: .text-alpha }

## One-Sentence Summary

Edaravone is a free radical scavenger originally used to treat ischaemic stroke and amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ischaemic stroke and amyotrophic lateral sclerosis (the Australian licence record contains no approved indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on published knowledge, edaravone is a free radical scavenger that quenches hydroxyl radicals and inhibits lipid peroxidation. Its benefit in ischaemic stroke and ALS is thought to come from limiting oxidative injury to neurons.

Heparin cofactor 2 deficiency is a thrombophilia caused by reduced inhibition of thrombin. Edaravone does not act on the coagulation cascade, so no direct mechanistic link has been established. The high TxGNN score is probably driven by shared thrombosis- and stroke-related nodes in the knowledge graph. It should be read as a hypothesis-generating signal, not as evidence of benefit.

### Other predictions in the top 10

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Factor 5 excess with spontaneous thrombosis | 99.06% | L5 | Hypercoagulable state; no plausible link |
| 3 | Bilateral parasagittal parieto-occipital polymicrogyria | 98.99% | L5 | Established structural malformation; no plausible role |
| 4 | Antithrombin deficiency type 2 | 98.97% | L5 | Edaravone does not act on coagulation |
| 5 | Axial spondylometaphyseal dysplasia | 98.84% | L5 | No plausible link |
| 6 | ALS, susceptibility to | 98.79% | L4 | Overlaps with the existing ALS indication; preclinical and mechanistic support only |
| 7 | ALS type 22 | 98.77% | L4 | Genetic ALS subtype; indirect, class-level relevance only |
| 8 | Trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 98.66% | L5 | Extremely rare; prediction only |
| 9 | Mills syndrome | 98.65% | L4 | Motor neuron disease variant; indirect rationale only |
| 10 | Lower motor neuron syndrome with late-adult onset | 98.45% | L4 | Overlaps with the ALS spectrum; indirect rationale only |

The motor neuron disease predictions (ranks 6, 7, 9 and 10) are the most biologically plausible. They sit within or next to the ALS spectrum for which edaravone is already approved, so they are extensions of an existing use rather than true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for heparin cofactor 2 deficiency. No trials were identified for any of the top 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for heparin cofactor 2 deficiency.

For context, the literature retrieved for the ALS-related prediction (rank 6) is shown below. It is mechanistic or preclinical, and none of it is a clinical trial.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38474192](https://pubmed.ncbi.nlm.nih.gov/38474192/) | 2024 | Review | Int J Mol Sci | Update on edaravone as an antioxidant. Developed in Japan for acute cerebral infarction, later applied to ALS, with expanding use in neurodegenerative diseases |
| [32241621](https://pubmed.ncbi.nlm.nih.gov/32241621/) | 2020 | Review | Bioorg Med Chem | Chemical reactivity and uses of edaravone (PMP), also a laboratory reagent; notes approval for stroke and ALS |
| [36595221](https://pubmed.ncbi.nlm.nih.gov/36595221/) | 2023 | Preclinical (in vitro) | FEBS Open Bio | Mouse stem cell-derived motor neurons are susceptible to ferroptosis, a lipid peroxidation-driven cell death |
| [41331940](https://pubmed.ncbi.nlm.nih.gov/41331940/) | 2025 | Preclinical (zebrafish) | Acta Neuropathol Commun | Human TDP-43 overexpression in zebrafish motor neurons produces MND-like phenotypes |
| [40672281](https://pubmed.ncbi.nlm.nih.gov/40672281/) | 2025 | Preclinical (zebrafish, preprint) | bioRxiv | Preprint version of the TDP-43 zebrafish study |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14804E | Radicava | Solution concentrate for I.V. infusion, 30 mg in 20 mL | Not stated in the data compiled for this report |

---

## Safety Considerations

No warnings, contraindications or drug interaction data were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The heparin cofactor 2 deficiency prediction rests on a graph-based score alone. There are no trials or publications, and there is no plausible mechanistic link between a free radical scavenger and a thrombin-inhibitor deficiency. The ALS-spectrum predictions are better grounded but largely overlap with an existing indication, so they are research questions rather than repurposing candidates.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Approved indication text for the Australian licence
- Any preclinical or clinical evidence linking edaravone to the predicted thrombophilia
- If pursuing the motor neuron disease predictions, a separate assessment of the established ALS evidence and subtype-specific data (for example ALS type 22 or Mills syndrome)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

