---
layout: default
title: Famotidine
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
description: "Famotidine: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Famotidine
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

## Famotidine: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Famotidine is an H2-receptor antagonist originally used for gastric and duodenal ulcers, gastroesophageal reflux disease, dyspepsia and Zollinger-Ellison syndrome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Famotidine is a well-established H2-receptor antagonist. By blocking H2 receptors on parietal cells, it reduces gastric acid secretion. Its efficacy in acid-related upper gastrointestinal conditions is proven.


**Other predictions in the model's top 10**

| Rank | Predicted Indication | Evidence Level | Comment |
|---|---|---|---|
| 2 | Duodenal obstruction | L5 | Mechanical condition; no clear mechanistic link |
| 3 | Active peptic ulcer disease | L4 | Essentially an existing labelled use |
| 4 | Gastrojejunal ulcer | L3 | Famotidine was only a comparator in one small trial; PPIs are generally preferred |
| 5 | Peptic ulcer perforation | L4 | Surgical complication; famotidine inferior to pantoprazole for recurrence prevention |
| 6 | Abnormality of glucagon secretion | L5 | Model prediction only |
| 7 | Gastroduodenitis | L2 | Partly indirect evidence, overlaps with labelled ulcer uses |
| 8 | Peptic ulcer disease | L1 | Already a labelled indication, so little repurposing novelty |
| 9 | Multiple endocrine neoplasia | L5 | Indirect, via Zollinger-Ellison syndrome |
| 10 | Acne | L5 | Model prediction only |

Several of these (ranks 3, 7 and 8) are essentially existing indications, so they add little true repurposing value.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Clinical study (design not confirmed) | World J Gastroenterol | Investigated the effect of famotidine on gastroesophageal and duodeno-gastro-esophageal reflux in critically ill patients, and possible mechanisms |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Clinical report (non-English) | Eksp Klin Gastroenterol | Famotidine 20 mg twice daily in early-stage gastroduodenal reflux disease, assessed clinically and endoscopically |

Both publications are small or indirect, and neither provides robust efficacy data.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 15047Y | Ausfam 20 | Tablet 20 mg (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease graph edges, not label text): kidney disease and impaired renal function, liver disease, gallbladder disease, nephrolithiasis, hypercalcaemia and related calcium or phosphorus disorders, sarcoidosis, hyperparathyroidism, diarrhoeal disease, constipation, and gastric cancer or neoplasm. Several of these look unusual for an H2 blocker and should be verified against the Product Information. Of note, renal impairment is a recognised reason for dose adjustment with famotidine.
- **Drug interactions**: 100 interactions were identified, and the first 20 are listed in the data. Most are rated Moderate, including abiraterone, acalabrutinib, tramadol, salbutamol, amiodarone, amitriptyline, aripiprazole and apalutamide. Minor interactions include alendronic acid and aluminium hydroxide. Please check the full list and clinical significance before co-prescribing.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Among the predictions, the better-evidenced ones largely duplicate existing ulcer indications and show famotidine as comparable or inferior to PPIs in several settings.

**To proceed, the following is needed:**
- Controlled clinical data of famotidine in duodenogastric reflux, ideally compared with a PPI or placebo
- Mechanism of action data
- TGA Product Information warnings and contraindications, and the approved indication text for the ARTG entry
- Review of the knowledge-graph contraindication signals and the key drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

