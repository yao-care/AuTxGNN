---
layout: default
title: Tiotropium
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-03
monitor_inn: "Tiotropium"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
description: "Tiotropium: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Tiotropium
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

## Tiotropium: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Tiotropium is a long-acting inhaled anticholinergic bronchodilator marketed in Australia as Spiriva Respimat.
The TxGNN model predicts it may be useful for **respiratory malformation**, but no study in the data compiled for this report directly examines that condition.
The report lists **3 clinical trials** (all in cystic fibrosis) and **2 publications** that are only indirectly related.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tiotropium belongs to the long-acting anticholinergic (muscarinic antagonist) class of inhaled bronchodilators. These drugs relax airway smooth muscle and may reduce airflow limitation.

The TxGNN score likely reflects the model's association between tiotropium and airway disease in general, not a specific mechanism for structural malformations. Bronchodilation could theoretically help secondary airflow limitation in some people with a malformed airway or lung. It would not correct the structural defect itself, and no study has tested this in a malformation population.

The score is a model output only and does not show that the drug works for this condition.

## Clinical Trial Evidence

The three trials below tested tiotropium via the Respimat inhaler in people with cystic fibrosis. None enrolled people with respiratory malformation, so they provide only indirect, contextual support on inhaled safety and lung function.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | Completed | 464 | Placebo-controlled trial of tiotropium 5 mcg once daily via Respimat for 12 weeks in cystic fibrosis, assessing efficacy and safety |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | Completed | 510 | Placebo-controlled dose-finding study of tiotropium 2.5 mcg and 5 mcg once daily for 12 weeks in cystic fibrosis, assessing lung function, safety and pharmacokinetics |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | Completed | 113 | Safety, tolerability and pharmacokinetics of single and multiple doses (28 days) in children and adults with cystic fibrosis |

## Literature Evidence

Only two of the retrieved publications touch on malformation or airway physiology. Neither studies tiotropium for respiratory malformation.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Case report | Rev Fac Cien Med Univ Nac Cordoba | COVID-19 in a young patient with pectus excavatum (a chest wall deformity), noting that altered lung function raised the risk of severe illness; no tiotropium data |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Preclinical | Chem Biol Interact | Mouse study of cholinergic mechanisms behind ventilatory dysfunction after nerve agent exposure; supports a general role for cholinergic signalling in breathing, not a malformation |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10509D | Spiriva Respimat | Solution for oral inhalation, 2.5 micrograms (as bromide monohydrate) per actuation (60 actuations) | Not stated in the data compiled for this report |

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 records. The main ones are other anticholinergic agents, rated Moderate, because additive anticholinergic effects are possible:
- Hyoscyamine, atropine, scopolamine
- Glycopyrronium (including topical), clidinium, dicyclomine
- Mepenzolate, methscopolamine, propantheline, trospium
- Eluxadoline, prucalopride and inhaled rapid-acting human insulin (Moderate)
- Cimetidine (Minor)

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trial or publication directly studies tiotropium in respiratory malformation, and the trials found were in cystic fibrosis. A fixed structural defect is also unlikely to respond to bronchodilation, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for tiotropium
- Clinical or observational studies in people with respiratory malformation
- A clear definition of which malformation types, if any, have a reversible airflow component
- Review of PI warnings and contraindications for the target population

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

