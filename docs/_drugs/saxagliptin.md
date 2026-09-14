---
layout: default
title: Saxagliptin
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Saxagliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Saxagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Saxagliptin is a DPP-4 inhibitor originally developed for glycaemic control in type 2 diabetes mellitus. The TxGNN model's top-ranked prediction links it to **Opsismodysplasia**, a rare skeletal dysplasia, but this signal is currently supported by **0 clinical trials** and **0 publications**, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (DPP-4 inhibitor class; not captured in the supplied TFDA/ARTG fields, which are empty) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned in this evidence pack (marked as a High-severity data gap). Based on well-established pharmacology, saxagliptin inhibits dipeptidyl peptidase-4 (DPP-4), prolonging incretin (GLP-1/GIP) activity to improve insulin secretion in type 2 diabetes.

Opsismodysplasia is a rare autosomal recessive skeletal dysplasia caused by mutations in *INPPL1*, affecting bone growth and ossification. There is no established biological pathway connecting incretin/DPP-4 signalling to this skeletal developmental disorder.

The evidence pack's own mechanistic rationale for this candidate is explicit on this point: the high TxGNN score (0.981) reflects graph-topology similarity in the knowledge graph rather than any known or plausible biological mechanism. This candidate should be read as an unvalidated model output, not as a mechanistically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Saxagliptin is not TGA-registered (market status: not marketed), so no Australian Product Information exists for this drug. Key warnings, contraindications, and drug interaction data were not returned by any queried source in this evidence pack. Please refer to the manufacturer's overseas-approved Product Information (e.g. FDA/EMA labelling) for safety information until TGA-specific data becomes available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Opsismodysplasia) has an L5 evidence level — a model prediction with no supporting clinical trials, literature, or known mechanistic rationale. The evidence pack's own rationale text states there is no biological support for this specific drug–disease link, and no ARTG/TGA registration exists for the drug in Australia.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for saxagliptin (currently a data gap)
- Independent mechanistic or preclinical evidence connecting DPP-4/incretin biology to opsismodysplasia pathophysiology
- TFDA/TGA-sourced Product Information for a baseline safety profile
- Re-evaluation once any clinical trial or peer-reviewed literature becomes available for this pairing

---

## Other Candidate Indications from This Evidence Pack

This evidence pack ("multi") scored 10 candidate indications for saxagliptin. All are L5 except one, and all carry a Hold recommendation. None currently supports a repurposing case; this table is provided for context only.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|----------------------|-------------|-----------------|------|
| 1 | Opsismodysplasia | 98.09% | L5 | No mechanistic link identified |
| 2 | Classic stiff person syndrome | 97.66% | L5 | Autoimmune/GABAergic mechanism, unrelated to DPP-4 |
| 3 | Focal stiff limb syndrome | 97.66% | L5 | Variant of #2, same reasoning |
| 4 | Thiamine-responsive dysfunction syndrome | 97.50% | L5 | Diabetes phenotype present, but caused by thiamine transporter defect, not incretin pathway |
| 5 | Drug-induced localized lipodystrophy | 96.35% | L5 | Local/injection-site process, not systemic incretin effect |
| 6 | Pancreatic agenesis | 96.24% | **L4** | 2 publications found, but these describe **pancreatic histopathology risk from incretin-based drugs**, i.e. a potential safety signal, not efficacy evidence |
| 7 | Centrifugal lipodystrophy | 96.12% | L5 | No mechanistic link identified |
| 8 | Pressure-induced localized lipoatrophy | 96.02% | L5 | Physical/local mechanism, unrelated |
| 9 | Idiopathic localized lipodystrophy | 95.75% | L5 | Cause unknown, no link established |
| 10 | Autoimmune oophoritis | 85.22% | L5 | Lowest score of the set; autoimmune mechanism unrelated to DPP-4 |

Note: candidate #6 (pancreatic agenesis) is the only one with any literature support, but that literature flags a possible **safety concern** (incretin-associated pancreatic tissue changes) rather than a therapeutic rationale — worth noting for pharmacovigilance purposes even though it does not support repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

