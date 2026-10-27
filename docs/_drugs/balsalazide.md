---
layout: default
title: Balsalazide
parent: Model Prediction Only (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Balsalazide: predicted new indication Gout (evidence level L5). Approved use: Ulcerative colitis, inflammatory bowel disease"
monitor_inn: "Balsalazide"
predicted_indications: ["gout", "congenital hypotrichosis with juvenile macular dystrophy", "ankylosing spondylitis", "rheumatoid arthritis", "rheumatoid vasculitis", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis", "anus disease"]
---

# Balsalazide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Balsalazide: From Ulcerative Colitis to Gout
{: .text-alpha }

## One-Sentence Summary

Balsalazide is a prodrug of mesalamine (5-ASA), originally used to treat ulcerative colitis and inflammatory bowel disease.
The TxGNN model predicts it may be effective for **gout**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease (from the TxGNN knowledge graph; no approved indication text is recorded in the ARTG data compiled for this report) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on general pharmacology, balsalazide is a prodrug that is cleaved by gut bacteria to release mesalamine (5-ASA). Mesalamine has anti-inflammatory activity, including inhibition of prostaglandin and leukotriene synthesis and modulation of NF-kB signalling. Its efficacy in ulcerative colitis is established.

Gout is driven by urate crystal-induced activation of the NLRP3 inflammasome, so a link through general anti-inflammatory activity is conceivable. However, this link is speculative. It rests on general pharmacology rather than on supplied data, and 5-ASA acts mainly locally in the gut mucosa. The high TxGNN score is a model prediction and is not clinical evidence.

For context, other top-ranked predictions for this drug were:

| Rank | Predicted Disease | Score | Plausibility (from the data compiled) |
|------|------|------|------|
| 3 | Ankylosing spondylitis | 99.71% | Biologically reasonable (IBD–spondyloarthritis axis), unverified; literature review needed |
| 4 | Rheumatoid arthritis | 99.64% | Uncertain; sulfasalazine's activity may depend on the sulfapyridine component, which balsalazide lacks |
| 7 | Inflammatory spondylopathy | 99.53% | Plausible, but clinical data on 5-ASA for axial inflammation are limited |
| 2, 6, 8 | Congenital hypotrichosis with juvenile macular dystrophy; hypermobility of coccyx; Kummell disease | 99.48–99.73% | No plausible mechanistic link; likely knowledge-graph artefacts |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11351K | Colazide | Capsule containing balsalazide sodium 750 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug–disease edges, not label text): kidney disease, pyoureter, pyloric stenosis.
- **Drug Interactions**: 100 interactions were identified. The sample reviewed shows mostly **Moderate** interactions, and one **Major** interaction: **intravenous human immunoglobulin G**. Moderate examples include:
  - NSAIDs: ibuprofen, ketorolac, celecoxib
  - Nephrotoxic agents: amphotericin B (including lipid formulations), amikacin, acyclovir, foscarnet, fosfomycin, gallium nitrate, bacitracin
  - Antibiotics: doxycycline, amoxicillin, ampicillin, azithromycin
  - Other: azathioprine, acetohexamide

  Many of these are agents with renal effects, which is relevant given the kidney disease signal. This is particularly relevant for gout, where NSAIDs are commonly used.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests on model score alone (L5). No trials or publications were found, and the mechanistic link is speculative. Safety data from the product label are also missing.

**To proceed, the following is needed:**
- A systematic literature search for 5-ASA/mesalamine and balsalazide in gout and urate-crystal inflammation, with preclinical (NLRP3) data if available
- Detailed mechanism of action data (MOA)
- Product Information warnings and contraindications for Colazide, and the approved indication text for the ARTG entry
- A renal safety and NSAID co-prescribing assessment, given the kidney disease signal and the common use of NSAIDs in gout
- Comparison against established gout therapies to define any unmet need
- Alternative candidates worth a literature review first: ankylosing spondylitis and inflammatory spondylopathy (both flagged as research questions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

