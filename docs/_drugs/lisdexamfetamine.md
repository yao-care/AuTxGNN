---
layout: default
title: Lisdexamfetamine
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 3
---

# Lisdexamfetamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lisdexamfetamine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Lisdexamfetamine is a prodrug of dextroamphetamine, originally developed and used for Attention-Deficit/Hyperactivity Disorder (ADHD). The TxGNN model predicts it may also be effective for **specific developmental disorder**, a prediction currently supported by **1 clinical trial** and **2 publications**, one of which is a completed Phase II/III RCT in paediatric ADHD patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lisdexamfetamine is a prodrug that is hydrolysed after absorption to release active dextroamphetamine, which promotes central dopamine and noradrenaline release. This mechanism is the pharmacological basis of its established core indication, ADHD.

ADHD is itself classified within the neurodevelopmental disorder spectrum, and the TxGNN-predicted indication ("specific developmental disorder") overlaps substantially with this existing, clinically validated use. Because ADHD already sits within the developmental disorder disease ontology, the mechanistic link here is stronger than a typical de novo repurposing signal — it is closer to an extension of an established indication into an adjacent or overlapping disease label.

One important caveat: "specific developmental disorder" is a broad disease-ontology term rather than a single, narrowly defined clinical entity. Confirming exactly how this label maps to specific developmental diagnoses (e.g., ADHD itself vs. other developmental disorders) is needed before treating this as a genuinely novel repurposing opportunity rather than a restatement of the existing ADHD indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Examined reinforcing mechanisms of smoking in adults with ADHD, including whether stimulant medication potentiates smoking's reinforcing effects. Not a direct efficacy trial for a developmental disorder indication — assessed as low direct relevance (Grade C: population/context-related but not a direct treatment-efficacy trial). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31718254](https://pubmed.ncbi.nlm.nih.gov/31718254/) | 2020 | RCT | Journal of Child and Adolescent Psychopharmacology | Multicentre, randomised, double-blind, placebo-controlled Phase II/III study of lisdexamfetamine (30/50/70 mg/day, 4 weeks) in 76 Japanese paediatric ADHD patients aged 6–17; evaluated change in ADHD-RS-IV total score from baseline. |
| [37849578](https://pubmed.ncbi.nlm.nih.gov/37849578/) | 2023 | Case Report | Cureus | Describes an 18-year-old female with intellectual disability, ADHD and dysmorphic facies, ultimately diagnosed with Hao-Fountain syndrome (a rare USP7-related neurodevelopmental disorder) after initially being suspected of Fragile X syndrome. Illustrative of diagnostic overlap between ADHD and broader developmental disorders rather than direct treatment evidence.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong — lisdexamfetamine's core approved indication (ADHD) already falls within the neurodevelopmental disorder spectrum predicted by TxGNN — and one completed Phase II/III RCT supports efficacy in a related paediatric ADHD population. However, the predicted indication label ("specific developmental disorder") is broad and not yet mapped to a precise clinical diagnosis, and the drug currently has no ARTG registration or Australian market presence, so safety and regulatory data specific to this market are unavailable.

**To proceed, the following is needed:**
- Clarification of exactly which developmental disorder diagnosis "specific developmental disorder" corresponds to in this prediction
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently a blocking data gap
- Confirmed mechanism of action documentation sourced directly from DrugBank (currently a data gap in the drug record)
- Assessment of local registration pathway, given the drug is not currently marketed in Australia (0 ARTG entries)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

