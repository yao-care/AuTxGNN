---
layout: default
title: Brexpiprazole
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brexpiprazole: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Major depressive disorder (adjunctive) and schizophrenia"
---

# Brexpiprazole
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

# Brexpiprazole: From Major Depressive Disorder and Schizophrenia to Dysthymic Disorder

## One-Sentence Summary

Brexpiprazole is an atypical antipsychotic (serotonin-dopamine activity modulator) originally used for schizophrenia and as adjunctive treatment in major depressive disorder.
The TxGNN model predicts it may be effective for **dysthymic disorder**, but **no clinical trials and no publications** specific to this condition were found.
The prediction is supported by model score alone, and indirect evidence from the approved depression indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (adjunctive) and schizophrenia (the ARTG entry carries no indication text; indications are drawn from the knowledge graph) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From published pharmacology, brexpiprazole is a partial agonist at serotonin 5-HT1A and dopamine D2 receptors and an antagonist at 5-HT2A receptors. Its effect in major depressive disorder as an add-on to antidepressants is established.

Dysthymia (persistent depressive disorder) is a chronic, milder form of depression that sits close to major depressive disorder in the disease ontology. The model prediction likely reflects this proximity. A mechanistic overlap is plausible, but it is unverified, because no trials or literature were retrieved for dysthymia specifically.

**Other predictions reviewed (all lower priority):**

| Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|
| Benign paroxysmal torticollis of infancy | 98.30% | L5 | No rationale; antipsychotics can cause dystonic reactions, a safety concern in children |
| Agoraphobia | 98.23% | L5 | 5-HT1A/5-HT2A pharmacology is relevant to anxiety, but unverified |
| Neurotic disorder | 97.73% | L5 | Broad legacy category; likely reflects ontology proximity |
| Neurotic depression | 97.11% | L4 | Maps to the already-approved depression indication; indirect evidence only |
| Melancholia | 97.07% | L4 | Severe depression subtype; no subtype-specific analysis |
| Keppen-Lubinsky syndrome | 96.05% | L5 | Speculative; no established link |
| Ohdo syndrome and variants | 94.97% | L5 | No plausible mechanism |
| Retinal dystrophy with or without extraocular anomalies | 94.75% | L5 | No known disease-modifying role |
| Congenital isolated ACTH deficiency | 94.50% | L5 | No plausible mechanism |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder.

---

## Literature Evidence

Currently no related literature available for dysthymic disorder.

The closest evidence concerns the parent indication of depression (retrieved under the related predictions "neurotic depression" and "melancholia"). It is indirect and does not demonstrate efficacy in dysthymia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26301701](https://pubmed.ncbi.nlm.nih.gov/26301701/) | 2015 | RCT (Phase 3) | J Clin Psychiatry | Adjunctive brexpiprazole 2 mg in MDD with inadequate response to antidepressants |
| [42090141](https://pubmed.ncbi.nlm.nih.gov/42090141/) | 2026 | Network meta-analysis | JAMA Psychiatry | Adjunctive atypical antipsychotics in MDD |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Network meta-analysis | J Affect Disord | Augmentation strategies for treatment-resistant major depression |
| [38924903](https://pubmed.ncbi.nlm.nih.gov/38924903/) | 2024 | Network meta-analysis of RCTs | Psychiatry Res | Efficacy and safety of eight enhanced therapies for treatment-resistant depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Network meta-analysis | J Psychopharmacol | Antidepressant plus second-generation antipsychotic vs esketamine vs lithium |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | Antidepressants and atypical antipsychotics in treatment-resistant depression |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | Role of antipsychotics in treatment-resistant depression |
| [28331332](https://pubmed.ncbi.nlm.nih.gov/28331332/) | 2017 | Review | Ther Clin Risk Manag | Clinical role of brexpiprazole in depression and schizophrenia |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11184P | Rexulti | Tablet 4 mg (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Those listed below are from the first 20 returned; the full list should be reviewed.
  - **Major**: bupropion, aprepitant, morphine, lorcaserin, cimetidine, clarithromycin, clotrimazole
  - **Moderate**: antidiabetic agents (acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, dapagliflozin, acetohexamide), epinephrine, and anticholinergics (hyoscyamine, atropine, clidinium), loperamide
- For warnings and contraindications, please refer to the TGA-approved Product Information (PI). Antipsychotics can cause dystonic reactions, which is particularly relevant if paediatric use were ever considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dysthymia prediction has a high model score but no trials or publications, so it remains at evidence level L5. The nearby depression evidence supports the already-approved adjunctive MDD use, not a distinct new indication.

**To proceed, the following is needed:**
- Dysthymia-specific literature review and trial registry search (including ANZCTR)
- Detailed mechanism of action data
- TGA Product Information warnings and contraindications (a blocking gap for safety screening)
- Review of the full interaction list (100 interactions)
- Evaluation of whether dysthymia is distinct enough from the approved MDD indication to count as a repurposing opportunity
- Proof-of-concept trial design, if the sponsor wishes to pursue it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

