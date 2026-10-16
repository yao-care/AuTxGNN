---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydroxocobalamin: predicted new indication Esophageal varices without bleeding (evidence level L5). Approved use: Vitamin B12 deficiency, pernicious anaemia, cyanide poisoning"
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Varices Without Bleeding

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, originally used to treat vitamin B12 deficiency, pernicious anaemia and cyanide poisoning.
The TxGNN model predicts it may be effective for **esophageal varices without bleeding**, but this rests on model output alone: **no clinical trials** and **no publications** were found for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia, cyanide poisoning (the ARTG entry in the compiled data has no indication text) |
| Predicted New Indication | Esophageal varices without bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroxocobalamin is a vitamin B12 form that is converted in the body to the active cofactors methylcobalamin and adenosylcobalamin. It is also known to bind cyanide and scavenge nitric oxide. Its efficacy in B12 deficiency is well established.

For esophageal varices, however, we could not identify a clear mechanistic link. Varices arise from portal hypertension, and their management relies on established approaches such as non-selective beta-blockers and endoscopic band ligation. The high score most likely reflects proximity in the knowledge graph rather than relevant biology. The same score was given to the bleeding variant of the disease, which supports this interpretation.

Other top-ranked predictions show the same pattern:
- **Varicose disease:** only speculative, indirect links (nitric oxide scavenging, homocysteine and vascular function).
- **Inflammatory myopathies** (immune-mediated necrotizing myopathy, antisynthetase syndrome, focal myositis, and others): no supporting mechanism.
- **Congenital prothrombin deficiency:** no supporting mechanism.
- **Vitamin deficiency disorder** (rank 9): the only prediction with literature, but it largely restates the existing B12 deficiency indication rather than offering a new use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for esophageal varices without bleeding.

For context, the literature compiled for the rank 9 prediction (vitamin deficiency disorder) consists of reviews, guidelines and case reports about B12 deficiency, not trials in the predicted varices indication. Examples include [38987879](https://pubmed.ncbi.nlm.nih.gov/38987879/) (2024, Review, overview of B12 deficiency diagnosis and treatment) and [27905001](https://pubmed.ncbi.nlm.nih.gov/27905001/) (2017, Guideline, cobalamin-related remethylation disorders). These are not evidence for the varices prediction.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10577Q | Vita-B12 | Injection 1 mg (as acetate) in 1 mL | Not available in the compiled data |

## Safety Considerations

- **Contraindications (knowledge graph):** The TxGNN knowledge graph lists hypertensive disorder and hypertension as contraindication associations. This comes from graph edges, not label text, and should be verified against the Product Information. It is also relevant to portal hypertension.
- **Drug Interactions:** 32 potential interactions were identified. Those rated Moderate are:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Others have no severity rating (for example omeprazole, lansoprazole, ranitidine, simvastatin, prednisolone, aspirin, folic acid, valsartan, ramipril).

Please also refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no literature, no plausible mechanistic link, and an Evidence Level of L5. Established therapies already exist for esophageal varices.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a biological rationale connecting hydroxocobalamin to portal hypertension or variceal pathophysiology
- Preclinical or observational evidence in varices
- The approved indication and warnings from the TGA Product Information for ARTG 10577Q
- A safety review of the hypertension-related contraindication signal and the moderate-level interactions
- If B12-related uses are of interest, consider the vitamin deficiency disorder prediction, noting it overlaps with the existing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

