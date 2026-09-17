---
layout: default
title: Quinagolide
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Quinagolide
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

# Quinagolide: From Hyperprolactinaemia to Insomnia

## One-Sentence Summary

Quinagolide is a dopamine D2-receptor agonist; structured registry data on its original indication and mechanism of action are currently a data gap, but pharmacological literature associates it with hyperprolactinaemia/prolactinoma. The TxGNN model's top-ranked prediction is **Insomnia**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and is mechanistically counter-intuitive since dopamine agonists more commonly cause insomnia as a side effect rather than treat it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinaemia / prolactinoma (per pharmacological literature referenced in the evidence review; not confirmed by structured registry data — see Data Gaps below) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 96.12% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record (flagged as a High-severity data gap). Based on the pharmacological class referenced within the evidence review itself, quinagolide is a selective D2 dopamine receptor agonist, and its efficacy in hyperprolactinaemia/prolactinoma is pharmacologically well established — though this original indication is not confirmed in the structured dataset provided.

The mechanistic case for insomnia is weak. Dopamine D2 agonists are clinically well known to *cause* insomnia as an adverse effect rather than treat it, so the direction of this prediction runs against established pharmacology. No clinical trial or literature evidence was found supporting the use of quinagolide for insomnia — this appears to be a model-driven association without empirical backing.

Two other candidates further down the prediction list carry somewhat stronger (though still limited) mechanistic plausibility and merit separate attention: **schizophrenia** (rank 10, evidence level L3, decision stage "Research Question") is supported by a systematic review/meta-analysis of pro-dopaminergic drugs for negative symptoms of schizophrenia, which is directionally consistent with quinagolide's dopamine-agonist activity. Conversely, **manic bipolar affective disorder** (rank 4, evidence level L4) is supported only by two case reports describing mania as an *adverse effect* of quinagolide — this is a safety signal, not a treatment opportunity, and should not be mistaken for supporting evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered for Insomnia.

## Literature Evidence

Currently no related literature available for Insomnia.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications, or drug-interaction data are currently available for quinagolide in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Insomnia) has no supporting clinical trial or literature evidence and is mechanistically counter-intuitive for a dopamine D2 agonist. Combined with a Blocking-severity data gap on TFDA/TGA-equivalent warnings and contraindications, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TGA-equivalent Product Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action and original indication from DrugBank/TGA sources — currently a High-severity data gap
- If pursuing repurposing further, prioritise re-evaluation of the schizophrenia signal (L3, "Research Question" stage) over the unsupported insomnia prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

