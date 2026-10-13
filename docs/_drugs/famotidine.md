---
layout: default
title: Famotidine
parent: Moderate Evidence (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 10
---

# Famotidine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Famotidine: From Gastric Ulcer to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is an H2-receptor antagonist originally used for gastric and duodenal ulcers, gastroesophageal reflux disease, dyspepsia and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but only **2 small or indirect publications** and **no registered clinical trials** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, duodenal ulcer, gastroesophageal reflux disease, esophagitis, dyspepsia, Zollinger-Ellison syndrome (from the knowledge graph; the ARTG entry has no indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Famotidine is a well-established H2-receptor antagonist. By blocking H2 receptors on parietal cells, it reduces gastric acid secretion. Its efficacy in acid-related upper gastrointestinal conditions is proven.

Duodenogastric reflux is closely related to these acid-related conditions, so acid suppression may plausibly relieve symptoms of mucosal irritation. However, famotidine does not correct the bile reflux itself, so any benefit would be symptomatic. The high TxGNN score likely reflects proximity to the existing ulcer and reflux indications in the knowledge graph rather than direct evidence.

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
| 9 | Multiple endocrine neoplasia | L4 | Indirect, via Zollinger-Ellison syndrome |
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
The prediction for duodenogastric reflux rests on a high model score and two small or indirect publications, with no registered trials (L4). Famotidine would act only on acid, not on bile reflux itself. Among the other predictions, the better-evidenced ones largely duplicate existing ulcer indications and show famotidine as comparable or inferior to PPIs in several settings.

**To proceed, the following is needed:**
- Controlled clinical data of famotidine in duodenogastric reflux, ideally compared with a PPI or placebo
- Mechanism of action data
- TGA Product Information warnings and contraindications, and the approved indication text for the ARTG entry
- Review of the knowledge-graph contraindication signals and the key drug interactions
- If the aim is genuine repurposing, a more novel candidate from the list (for example gastroduodenitis, at L2) could be explored, after confirming it is not already covered by the existing label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

