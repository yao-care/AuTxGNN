---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 5
monitor_inn: "Ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-11-20
description: "Ambrisentan: predicted new indication Pulmonary arteriovenous malformation (evidence level L5). In Australia: 8 PBS items (8 currently listed)"
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ambrisentan: endothelin type A receptor antagonist → Pulmonary arteriovenous malformation
{: .text-alpha }

## One-Sentence Summary

Ambrisentan is an endothelin type A receptor antagonist. The TxGNN model predicts it may be relevant to **pulmonary arteriovenous malformation**, but no clinical trials are registered and the only linked publication is **1 case report**, which concerns pulmonary arterial hypertension rather than the malformation itself. This is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary arteriovenous malformation |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (8 of 8 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ambrisentan is an endothelin type A receptor antagonist. According to the Mechanism of Action section of the US FDA-approved prescribing information for ambrisentan: "Endothelin-1 (ET-1) is a potent autocrine and paracrine peptide. Two receptor subtypes, ET A and ET B, mediate the effects of ET-1 in the vascular smooth muscle and endothelium. […] Ambrisentan is a high-affinity (K i =0.011 nM) ET A receptor antagonist with a high selectivity for the ET A versus ET B receptor (>4000-fold)." ([DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844), label version 2026-06-22; accessed 2026-11-19.) This description reflects the drug's general class.

Pulmonary arteriovenous malformations are often associated with hereditary haemorrhagic telangiectasia (HHT) and involve dysregulated angiogenesis and vascular remodelling. Endothelin signalling is plausibly relevant to the associated pulmonary vascular disease, which is the basis for a possible mechanistic link.

However, this support is indirect. The only linked publication describes pulmonary arterial hypertension in a patient with HHT. It does not study treatment of the malformation itself. The high TxGNN score is a computational output and is not corroborated by direct studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World Journal of Clinical Cases | Report of pulmonary arterial hypertension in a patient with HHT, with family gene analysis, to raise awareness of this co-occurrence. It does not evaluate ambrisentan for the malformation. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12180C | Cipla Ambrisentan | Tablet 10 mg | Not recorded in the local data |

---

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. Those at moderate level include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Those at minor level include clarithromycin, miconazole and omeprazole.
- Systemic endothelin receptor blockade carries embryo-fetal toxicity concerns, so use in developmental or cosmetic conditions is hard to justify.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as label-based data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies ambrisentan in pulmonary arteriovenous malformation. The prediction rests on a model score and an indirect mechanistic link, so it remains a research question.

**To proceed, the following is needed:**
- Studies directly evaluating ambrisentan or other endothelin antagonists in pulmonary arteriovenous malformation, with or without HHT
- Detailed mechanism of action data
- Warnings and contraindications from the TGA Product Information, followed by a safety review for this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

