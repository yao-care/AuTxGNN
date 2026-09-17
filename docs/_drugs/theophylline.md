---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 669
evidence_level: L5
indication_count: 10
---

# Theophylline
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

Using no additional skill — this is a straightforward structured-report generation task where the template and data are fully specified in the prompt; no coding, debugging, or design decision requires a process skill.

One data-quality note before the report: `predicted_indications[0]` in this pack is **thrombotic disease**, which the evidence pack's own `repurposing_rationale` flags as a likely false positive (no trials, weak/irrelevant literature). Per the template rules I've generated the report on this top-ranked entry as instructed, and flagged the discrepancy at the end rather than silently switching to a better-evidenced candidate (rank 5, obstructive lung disease) further down the list.

---

# Theophylline: From Bronchodilator Therapy to Thrombotic Disease

## One-Sentence Summary

> Theophylline is a long-established methylxanthine bronchodilator used in asthma and COPD.
> TxGNN's highest-scoring prediction suggests it may be effective for **Thrombotic Disease**,
> but this is supported by **0 clinical trials** and **19 publications**, almost none of which show a genuine mechanistic or clinical link — evidence review indicates this is likely a model artefact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no ARTG licence data); literature in this pack describes theophylline as a bronchodilator used in asthma/COPD, but this is not confirmed via formal regulatory data here |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for theophylline is not available in this evidence pack (flagged as a High-severity data gap). Based on the literature retrieved elsewhere in this pack, theophylline is a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist, long used as a bronchodilator with anti-inflammatory activity in airway disease. No component of this known mechanism describes platelet inhibition, anticoagulant activity, or antithrombotic effect.

The literature retrieved for the thrombotic disease prediction does not support a real biological link. Of the 19 papers returned, most concern unrelated antiplatelet drugs (e.g., ticlopidine), platelet-activation biomarker assays (PF4, sCLEC-2), or use theophylline purely as a laboratory reagent (e.g., an anticoagulant tube additive, or a compound detected by an aptasensor) rather than as a therapeutic agent being tested against thrombosis.

Given the absence of any clinical trial evidence and the largely tangential nature of the literature, this prediction is best interpreted as a knowledge-graph embedding similarity artefact rather than a credible repurposing hypothesis — a conclusion also reached in this pack's own internal rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Reviews the antiplatelet drug ticlopidine's pharmacokinetics; theophylline is not the subject drug and is not evaluated therapeutically. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Examines platelet/neutrophil activation in Behçet's disease; does not evaluate theophylline. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methodology | British Journal of Haematology | Describes a platelet factor 4 (PF4) radioimmunoassay; theophylline is used only as a laboratory anticoagulant additive, not as a treatment. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Methodology | Analytica Chimica Acta | Describes a biosensor for measuring blood theophylline levels; an analytical tool, not evidence of antithrombotic efficacy. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | General review of prostaglandins/thromboxane in platelet biology and atherosclerosis; does not evaluate theophylline. |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflammatory Bowel Diseases | Investigates platelet-leukocyte aggregates in IBD; theophylline not evaluated. |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Methodology | Platelets | Describes a sCLEC-2 assay for platelet activation detection; theophylline not evaluated as treatment. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Cohort | Cor et Vasa | Reports "theophylline-resistant" T-lymphocyte subsets (a laboratory classification method using theophylline, not a treatment) elevated in myocardial infarction/thrombophlebitis patients. |

**None of the above literature provides direct evidence of a therapeutic antithrombotic effect for theophylline.** Most references either study unrelated drugs or use theophylline solely as a laboratory reagent.

## Australia Market Information

Theophylline currently has **no ARTG (Australian Register of Therapeutic Goods) entries** in this evidence pack, and market status is recorded as **not marketed** in Australia. No product-level licence data is available to summarise here.

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interactions) is available in this evidence pack — this is recorded as a **Blocking** data gap (DG001: TFDA/TGA product information not yet retrieved). Given theophylline is not currently marketed in Australia under this data, there is no TGA-approved Product Information to reference. Independently of this evidence pack, theophylline is widely known to have a narrow therapeutic index and clinically significant CYP1A2-mediated drug interactions; this should be verified against current product information before any further evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN's top-ranked prediction (thrombotic disease) has zero supporting clinical trials, and the retrieved literature shows no credible mechanistic or clinical link to antiplatelet/anticoagulant activity. This pattern is consistent with a knowledge-graph embedding artefact rather than a genuine repurposing signal, and the evidence pack's own internal rationale reaches the same conclusion.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank) — currently a High-severity gap
- TFDA/TGA product information (warnings, contraindications, DDI) — currently a Blocking gap
- If this hypothesis is to be pursued further: dedicated preclinical or clinical evidence specifically testing theophylline's antiplatelet/anticoagulant activity, since none currently exists in this pack

**Separate note for reviewers:** within this same evidence pack, a lower TxGNN-ranked candidate — *obstructive lung disease* (rank 5, score 99.48%) — carries far stronger evidence (L1, multiple completed Phase 3/4 RCTs, "Proceed with Guardrails"). It largely reconfirms theophylline's known respiratory use rather than representing novel repurposing, but may warrant a separate evaluation report if that is the intended use case for this candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

