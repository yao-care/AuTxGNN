---
layout: default
title: Opicapone
parent: Model Prediction Only (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Opicapone: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease (including juvenile-onset and other parkinsonian sy…"
monitor_inn: "Opicapone"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "lethal infantile mitochondrial myopathy", "X-linked intellectual disability-ataxia-apraxia syndrome", "X-linked intellectual disability-cerebellar hypoplasia syndrome"]
---

# Opicapone
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

# Opicapone: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Opicapone is a peripheral COMT inhibitor, originally used as adjunctive therapy alongside levodopa in Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (including juvenile-onset and other parkinsonian syndromes) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, opicapone is a peripheral catechol-O-methyltransferase (COMT) inhibitor. It reduces the breakdown of levodopa outside the brain and so extends its effect in Parkinson disease.

The link to the predicted indication is weak. Rasmussen encephalitis is an immune-mediated, T-cell driven inflammation of one brain hemisphere, causing intractable epilepsy. COMT inhibition and dopaminergic support have no established role in this process. The high TxGNN score most likely reflects closeness to other neurological disease nodes in the knowledge graph rather than a biological rationale.

For context, other predictions for this drug are more credible than the top-ranked one:
- **Lewy body dementia** (score 95.7%, L4): shares alpha-synuclein pathology and dopaminergic deficits with Parkinson disease. Levodopa response is often limited, and increased dopaminergic exposure may worsen psychosis or hallucinations. This warrants a focused literature and safety review.
- **Paralysis agitans, juvenile, of Hunt** (score 97.3%, L4): a historical term for juvenile parkinsonism that overlaps with the existing indications, so it is more a label overlap than true repurposing.
- **PLA2G6-associated neurodegeneration** (score 97.6%, L5): symptomatic dopaminergic support is conceivable, but opicapone does not address the underlying pathology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13206C | Ongentys | Capsule 50 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Drug Interactions:** The interaction screen identified 53 potential interactions. The main ones from the listed entries are below.

- **Major:** methylene blue.
- **Moderate (examples):**
  - Sympathomimetics: epinephrine (systemic, ophthalmic and topical forms) and sibutramine.
  - Opioids and related drugs: morphine (including liposomal), codeine, opium, diphenoxylate and difenoxin.
  - Cannabinoids: dronabinol and nabilone.
  - Sedating antihistamines: promethazine, chlorpheniramine, cetirizine and nasal azelastine.
  - Others: metoclopramide, dextromethorphan and ethanol.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no registered trials or publications, and no plausible mechanism links COMT inhibition to the pathology of Rasmussen encephalitis. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale for the predicted indication
- A systematic literature search on COMT inhibition and dopaminergic therapy in immune-mediated encephalitis
- The TGA-approved Product Information, including the approved indication text, warnings and contraindications
- If pursuing neurological alternatives, a focused efficacy and safety review for Lewy body dementia, particularly the risk of psychosis and hallucinations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

