---
layout: default
title: Ursodeoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 710
evidence_level: L5
indication_count: 10
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: Original Indication Not Documented → Homozygous Familial Hypercholesterolemia (Predicted)

## One-Sentence Summary

> The evidence pack does not contain documented original indication or mechanism-of-action data for ursodeoxycholic acid (DB01586), and the drug currently has no ARTG registration in Australia.
> The TxGNN model's top-ranked prediction is **Homozygous Familial Hypercholesterolemia**, with a very high model confidence score (99.86%),
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no real-world evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text found in the evidence pack (0 ARTG licences on file) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ursodeoxycholic acid is not available in this evidence pack. Based on the model's own rationale output, ursodeoxycholic acid is a hydrophilic bile acid that influences bile acid and cholesterol metabolism, but the pathophysiology of homozygous familial hypercholesterolemia is driven primarily by LDL-receptor gene defects. The rationale explicitly notes that the mechanistic link between UDCA's known cholesterol-lowering pathways (inhibition of cholesterol synthesis/absorption) and the LDL-receptor defect underlying this disease is weak.

This prediction is derived purely from TxGNN knowledge-graph embedding similarity, not from any documented pharmacological or clinical relationship. The high model score should be interpreted as a signal for further investigation, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

This drug currently has no ARTG entries in Australia (Market Status: **Not Marketed**, 0 licences on file). No product, dosage form, or approved indication information is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Homozygous Familial Hypercholesterolemia) has no supporting clinical trials or literature (Evidence Level L5, Decision Stage S0), and a Blocking data gap exists for TFDA/TGA safety warnings and contraindications, which prevents even an initial safety assessment (S1). Mechanism-of-action data is also unavailable, so mechanistic plausibility cannot be independently verified.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, contraindications, and drug interactions (Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or equivalent source (DG002)
- Documented original indication(s) and ARTG registration status, if the drug is intended for the Australian market
- Independent preclinical or clinical evidence specific to homozygous familial hypercholesterolemia before any advancement beyond hypothesis-generation

**Note for consideration:** among the 10 candidates in this evidence pack, rank 7 (**diabetic nephropathy**) — despite a lower TxGNN score (96.9%) — has meaningfully stronger support: 7 preclinical studies describing a plausible mechanism (UDCA reducing endoplasmic-reticulum stress, oxidative stress, and podocyte apoptosis in diabetic kidney models), reaching Evidence Level L4 and Decision Stage S1 ("Research Question"). This may be a more productive candidate for further evidence-gathering than the top-ranked but evidence-free prediction above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

