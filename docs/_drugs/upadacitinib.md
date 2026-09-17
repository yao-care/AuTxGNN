---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 708
evidence_level: L5
indication_count: 10
---

# Upadacitinib
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

# Upadacitinib: From Undocumented Original Indication to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

> Upadacitinib's original indication and mechanism of action were not recorded in this Evidence Pack, so its established clinical use cannot be summarised from the supplied data. The TxGNN model's top prediction is **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital developmental disorder — but this prediction is supported by **zero clinical trials and zero publications**, and the model's own rationale flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.61% (model rank 4,998 of full candidate set) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for upadacitinib was not provided in this Evidence Pack. What is generally known is that upadacitinib is a Janus kinase (JAK) inhibitor selective for JAK1, which mediates intracellular signalling for a range of inflammatory cytokines. Because the original indication field was also empty in this pack, no direct comparison can be drawn here between an established therapeutic use and the predicted new indication.

Critically, the model's own rationale for this top-ranked prediction is sceptical of its plausibility. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital condition involving ocular defects (coloboma/microphthalmia) and proximal limb skeletal dysplasia, arising from embryonic developmental gene defects. There is no known biological pathway connecting this pathophysiology to JAK1-mediated immune signalling. The Evidence Pack explicitly describes this as a high-scoring prediction that "lacks biological plausibility" and "may represent a false positive from knowledge graph embedding."

For context, other lower-ranked candidates in this same Evidence Pack — such as plasma cell myeloma and indolent plasma cell myeloma (ranks 3 and 7) — have a more coherent mechanistic rationale, since the IL-6/JAK/STAT3 pathway is a recognised driver in myeloma biology. These were scored "Research Question" rather than "Hold," suggesting the rank-1 prediction here is more likely statistical noise than a genuine signal worth pursuing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries are recorded for upadacitinib in this Evidence Pack. Market status is listed as **Not Marketed**, with 0 total licences on file. This may reflect a gap in this data collection pipeline rather than confirmed absence from the Australian market — it should be verified directly against the TGA ARTG database before being relied upon.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at Evidence Level L5 — a model score with no supporting clinical trials, literature, or credible mechanistic pathway. The Evidence Pack's own rationale identifies it as a probable false positive, and there is a Blocking-severity data gap on TGA/TFDA safety labelling that would prevent any safety pre-assessment regardless of efficacy evidence.

**To proceed, the following is needed:**
- Upadacitinib's original indication(s) and confirmed mechanism of action (DrugBank/product literature)
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently a Blocking gap
- Independent biological or preclinical rationale connecting JAK1 inhibition to this syndrome, beyond the current TxGNN score
- Confirmation of current ARTG registration status for upadacitinib in Australia
- If pursuing repurposing research further, consider redirecting attention to the higher-plausibility candidates in this pack (e.g., plasma cell myeloma, ALS) rather than the rank-1 result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

