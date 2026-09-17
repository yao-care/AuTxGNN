---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
---

# Rabeprazole
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

# Rabeprazole: From Acid-Peptic Disorders to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) originally used to treat acid-peptic disorders such as GERD, gastric/duodenal ulcer and *Helicobacter pylori* eradication. The TxGNN model's top-ranked prediction suggests possible relevance to **Smouldering Systemic Mastocytosis**, but this candidate currently has **no supporting clinical trials and no supporting publications** — the prediction rests on mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-peptic disorders (GERD, gastric/duodenal ulcer, *H. pylori* eradication) — inferred from literature context in this pack; no ARTG/PI text available |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this pack (`original_moa` is a data gap). Based on known pharmacology, rabeprazole is a substituted-benzimidazole proton pump inhibitor that irreversibly inhibits the H+/K+-ATPase of gastric parietal cells, and its efficacy in acid-peptic disorders (GERD, peptic ulcer, *H. pylori*-related disease) is well established.

The proposed link to smouldering systemic mastocytosis is indirect: patients with systemic mastocytosis can develop gastric acid hypersecretion driven by mast-cell histamine release, producing a Zollinger-Ellison-like presentation. In theory, a PPI could relieve the resulting GI symptoms. However, this is a **symptomatic, supportive-care hypothesis**, not a disease-modifying mechanism — it does nothing to address the underlying mast-cell pathology that defines the condition.

No clinical trial or published literature in this evidence pack tests rabeprazole in mastocytosis of any kind. The prediction should be read as a model-generated hypothesis based on pathway proximity, not as evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

Rabeprazole is not currently registered on the ARTG (Australian Register of Therapeutic Goods) in this dataset — market status is "not marketed" with 0 licence entries, so no product table can be produced.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 — a model prediction only, with zero identified clinical trials or publications, and the mechanistic rationale is speculative (symptom relief in a histamine-driven hypersecretory state, not disease-targeted therapy). This does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Any case reports, case series, or preclinical data specifically addressing acid hypersecretion or GI symptom control in systemic mastocytosis
- Consider that this evidence pack contains substantially stronger candidates for the same drug — notably **active peptic ulcer disease** and **gastric ulcer (disease)**, both L1/S3 with multiple completed Phase 2–3 RCTs — which may be a more productive focus if the goal is a viable repurposing pathway rather than testing novel model output
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

