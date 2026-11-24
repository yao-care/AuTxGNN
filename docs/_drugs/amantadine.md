---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 4
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
last_modified_at: 2026-11-24
description: "Amantadine: predicted new indication Rasmussen subacute encephalitis (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Amantadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Amantadine: NMDA receptor antagonist and dopaminergic modulator → Rasmussen subacute encephalitis
{: .text-alpha }

## One-Sentence Summary

Amantadine is an oral medicine marketed in Australia as a 100 mg capsule. The TxGNN model predicts it may be relevant to **Rasmussen subacute encephalitis** with a score of 0.9948. No clinical trials or publications were supplied for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9948 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for amantadine: "The mechanism by which amantadine exerts efficacy in the treatment of dyskinesia in patients with Parkinson's disease or as adjunctive treatment to levodopa/carbidopa in patients with Parkinson's disease experiencing 'off' episodes is unknown. Amantadine is a weak uncompetitive antagonist of the NMDA receptor." ([DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28), label version 2026-10-05; accessed 2026-11-19.) Amantadine is generally understood to antagonise NMDA receptors and modulate dopaminergic signalling.

Rasmussen encephalitis is a rare, severe, drug-resistant form of epilepsy. Glutamate receptor-mediated excitotoxicity and autoimmune mechanisms have been proposed as contributors. A link to NMDA antagonism is therefore plausible, but it is unverified. No clinical support for amantadine in this condition was found in the data compiled, and the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 3016R | AMANTAMED | Amantadine | Capsule containing amantadine hydrochloride 100 mg | Valid |
| 14486K | AMANTAMED | Amantadine | Capsule containing amantadine hydrochloride 100 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 93 interactions were identified in the interaction databases. Notable examples:
  - Major: bupropion.
  - Moderate: anticholinergic agents (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium), metoclopramide, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate.
  - Interactions with calcitriol, pantoprazole, glimepiride, doxycycline and metformin are recorded without a severity grade.

Label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or publications for Rasmussen subacute encephalitis, so the evidence level is L5. The suggested NMDA-related link is plausible but unverified.

**To proceed, the following is needed:**
- Mechanism of action data and a documented rationale linking amantadine to Rasmussen encephalitis
- A structured literature search for case reports or preclinical studies in this disease
- TGA Product Information warnings and contraindications for a safety review
- Assessment of suitability for a rare paediatric-onset population, including dosing and renal function considerations

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

