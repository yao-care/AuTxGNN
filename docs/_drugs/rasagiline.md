---
layout: default
title: Rasagiline
parent: Model Prediction Only (L5)
nav_order: 626
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rasagiline: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease"
monitor_inn: "Rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "congenital disorder of glycosylation with defective fucosylation", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "retinal dystrophy with or without extraocular anomalies"]
---

# Rasagiline
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

## Rasagiline: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Rasagiline is a monoamine oxidase B (MAO-B) inhibitor originally used to treat Parkinson disease.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration** (score 99.7%), but **no clinical trials and no publications** currently support this specific prediction.
Evidence is limited to model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian syndromes, per the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Rasagiline is generally known as a selective, irreversible MAO-B inhibitor with proven efficacy in Parkinson disease. It also has reported neuroprotective (anti-apoptotic) properties in laboratory studies.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism (PARK14). The plausible link is phenotypic overlap with parkinsonism, the original indication. However, MAO-B inhibition is not known to address the underlying lipid-metabolism and iron-accumulation pathology. Any benefit would be inferred from shared parkinsonian symptoms and has not been demonstrated.

**Other predictions in the data compiled for this report** (all lower-ranked, for context):
- **Lewy body dementia** (score 98.8%, L4): biologically plausible given shared alpha-synuclein pathology with Parkinson disease. The available literature is mostly preclinical or concerns related compounds and Alzheimer's disease. There are no direct rasagiline trials and no registered trials.
- **Retinal dystrophy with or without extraocular anomalies** (score 98.8%, L4): one mouse study of retinitis pigmentosa suggests rasagiline delays retinal degeneration via Bax/Bcl-2 modulation. There are no human data.
- **Paralysis agitans, juvenile, of Hunt** (score 99.2%, L5): a historical term for juvenile-onset parkinsonism. The high score likely reflects closeness to Parkinson disease in the ontology.
- Other predictions (Rasmussen encephalitis, myelitis, transaldolase deficiency, and several congenital metabolic or developmental disorders) have no evident mechanistic rationale and no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14458Y | Pharmacor Rasagiline | Tablet 1 mg (as mesilate) | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph-derived associations, not label text): hypertension and hypertensive disorder, multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, drug-induced dyskinesia, epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, melanoma, phaeochromocytoma (adrenal gland), sympathetic paraganglioma, and cancers of the duodenum, small intestine, heart and adrenal gland.
- **Drug Interactions**: 100 interactions were recorded. The list below shows the main ones from the portion available:
  - **Major**: bupropion, morphine
  - **Moderate**: epinephrine, chlorpropamide, cimetidine, diethylpropion, difenoxin, diphenoxylate, dronabinol, obeticholic acid, phentermine, glimepiride, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, inhaled human)

Product Information warnings and contraindications were not available for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no clinical trials or literature for PLA2G6-associated neurodegeneration, and the mechanistic link is only a shared parkinsonian phenotype. Of the other predictions, Lewy body dementia and retinal dystrophy are best supported (L4, preclinical only), and could be framed as research questions rather than treatment recommendations.

**To proceed, the following is needed:**
- Mechanism of action data for rasagiline (for example from DrugBank)
- TGA-approved Product Information, including warnings, contraindications and approved indication text
- Disease-specific preclinical or clinical evidence for PLA2G6-associated neurodegeneration (for example, patient-derived cell or animal model studies)
- A review of whether the knowledge-graph contraindications and the interaction burden are acceptable in this patient population, which is often paediatric or on multiple medicines
- An assessment of whether the Lewy body dementia prediction merits a separate evaluation, supported by direct clinical data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

