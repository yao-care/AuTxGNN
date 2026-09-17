---
layout: default
title: Rotigotine
parent: Model Prediction Only (L5)
nav_order: 608
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

Using the drug-repurposing report template directly (no additional skill needed — this is a self-contained content-generation task from the supplied Evidence Pack).

Note before the report: the pack has almost no usable original-indication text (`original_indications` is empty, `taiwan_regulatory.licenses` is empty, `original_moa` is `[Data Gap]`). Rather than guess, I pulled the original-indication and MOA context from the literature abstracts already inside the pack (PMID 37221270 explicitly states rotigotine "is used to treat PD and restless legs syndrome"; the repurposing rationale texts describe it as a non-ergot D1/D2/D3 dopamine agonist). This is cited, not invented.

---

# Rotigotine: From Parkinson's Disease / Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Rotigotine is a non-ergot dopamine receptor agonist used to treat Parkinson's disease and restless legs syndrome (RLS). The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, but currently **no clinical trials** and only **3 indirect publications** (none studying rotigotine in ADHD directly) support this direction — the evidence is essentially theoretical.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease / Restless legs syndrome (per literature context; no ARTG-approved indication text available) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A dedicated mechanism-of-action record for rotigotine is not available in this evidence pack. Based on information embedded in the supporting literature and rationale data, rotigotine is a non-ergot dopamine receptor agonist acting on D1, D2 and D3 receptors with D3 preference, and is an established treatment for Parkinson's disease and restless legs syndrome.

The ADHD hypothesis rests on the broader dopaminergic-deficit theory of ADHD — reduced prefrontal-striatal dopamine signalling, with DRD4/DRD5 gene variants implicated in the disorder. One cited paper (PMID 34182128) touches on α2A-adrenoceptor/D4-receptor heteromerisation relevant to ADHD pharmacology, but it does not study rotigotine itself. The other two cited papers (PMID 18656214, PMID 21476956) are reviews of restless legs syndrome, not ADHD, and were most likely surfaced by keyword overlap (dopamine, movement/neurological terms) rather than genuine topical relevance.

In short, the mechanistic story is biologically plausible in outline (dopamine agonism ↔ dopamine-deficit hypothesis of ADHD) but is not supported by any study that actually tests rotigotine in ADHD patients or models. This should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Pharmacology | Pharmacological research | Describes α2A-adrenoceptor/dopamine D4 receptor heteromerisation relevant to ADHD genetics; does not test rotigotine |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | Review of pharmacological treatment of restless legs syndrome in children; not about ADHD |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | General overview of restless legs syndrome; not about ADHD |

## Australia Market Information

Rotigotine is currently not marketed in Australia — no ARTG entries were found for this compound.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note: this drug is not currently registered in Australia, so no local PI exists yet; the evidence pack itself flags TGA-equivalent label warnings/contraindications and a drug-drug interaction profile as outstanding data gaps (one flagged as blocking).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted ADHD indication is supported only by TxGNN's knowledge-graph score (L5, no clinical trials, no ADHD-specific literature) and a plausible but unproven mechanistic hypothesis. A safety review cannot proceed while label warnings/contraindications data remain an outstanding blocking gap.

**To proceed, the following is needed:**
- Product Information / label warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action data from DrugBank or equivalent source
- Drug-drug interaction profile (currently not found)
- Any preclinical or clinical evidence directly linking rotigotine to ADHD before advancing past Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

