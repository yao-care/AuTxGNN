---
layout: default
title: Risdiplam
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Risdiplam
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

# Risdiplam: From Spinal Muscular Atrophy to Acne (Disease)

## One-Sentence Summary

Risdiplam's originally approved indication is not confirmed by regulatory data in this evidence pack (a flagged data gap), though the pack's own mechanistic notes associate it with spinal muscular atrophy (SMA), where it acts as an SMN2 pre-mRNA splicing modifier. The TxGNN model's top prediction is **Acne (disease)**, but this candidate — and all nine others in this pack — is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale explicitly finds no known mechanistic link to acne.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in regulatory data (empty in this pack); mechanism notes reference spinal muscular atrophy (SMA) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Risdiplam is not available in this evidence pack (flagged as a High-severity data gap). Partial mechanistic context is available in the model's own generated rationale text, which repeatedly describes Risdiplam as an SMN2 pre-mRNA splicing modifier acting on survival motor neuron gene expression — consistent with its known role in spinal muscular atrophy — but this text is not a substitute for a validated MOA record.

There is no apparent pharmacological relationship between SMN2 splicing modulation and acne pathophysiology, which is driven by sebaceous gland activity and androgen signalling. The evidence pack's own repurposing rationale for this candidate states explicitly that there is "no known mechanistic association" between the two.

This pattern is not unique to acne: across the top 10 TxGNN predictions for Risdiplam, the accompanying rationale text repeatedly flags an absence of mechanistic plausibility, and in several cases suggests the high scores may be artifacts of knowledge-graph embedding similarity rather than genuine pharmacological signal — for example, four separate melanoma subtypes (metastatic, non-cutaneous, epithelioid cell, eyelid) cluster together in the ranking, which the model's own notes attribute to node-similarity clustering rather than independent evidence, and rare conditions such as acrodermatitis chronica atrophicans are flagged as likely low-quality predictions due to sparse graph data. On the current evidence, none of the top 10 candidates — including acne — has independent biological or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

No ARTG entries were found for Risdiplam in this evidence pack. Market status is recorded as **Not marketed** in Australia, with 0 total licences on file.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Risdiplam, including the top-ranked acne candidate, carry L5 evidence — model prediction only, with zero supporting clinical trials or publications. The model's own mechanistic rationale finds no known biological link for most candidates and flags several (the melanoma subtype cluster, acrodermatitis chronica atrophicans) as likely artifacts of knowledge-graph structure rather than genuine signal.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action (MOA) from a validated source (currently a Blocking/High-severity data gap)
- TGA Product Information / ARTG registration data for safety review
- Independent clinical or preclinical evidence connecting Risdiplam's SMN2-splicing mechanism to any of the top-ranked predicted indications before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

