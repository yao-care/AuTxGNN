---
layout: default
title: Povidone-Iodine
parent: Model Prediction Only (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Povidone-Iodine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Not stated in the Australian licence data compiled for this report. T…"
---

# Povidone-Iodine
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

# Povidone-iodine: From Topical Antisepsis to Plasmodium falciparum Malaria

## One-Sentence Summary

Povidone-iodine is a broad-spectrum topical antiseptic. In Australia it is registered as an antiseptic dressing (Inadine).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Australian licence data compiled for this report. The registered product is a topical antiseptic dressing. |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 88.33% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, povidone-iodine is a complex of iodine and polyvinylpyrrolidone. It kills a wide range of bacteria, fungi and viruses by releasing iodine, which acts as an oxidising agent. Its effect on wounds and skin is well established.

Malaria is a blood-stage parasitic infection, and it is not obvious how a topical antiseptic would affect it. Povidone-iodine has no known systemic antiplasmodial activity. Its topical, non-systemic use makes a plausible mechanism for treating bloodstream parasites unlikely. The high TxGNN score reflects a statistical pattern in the knowledge graph (the model ranked this prediction 82,584th overall), not biological or clinical support. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10847X | Inadine | Dressing 9.5 cm x 9.5 cm | Not specified in the data compiled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (derived from drug-disease links in the PrimeKG knowledge graph, not from product label text): epilepsy, liver disease, gallbladder disease, respiratory failure, atrioventricular block, atrioventricular dissociation and heart block. These signals are unverified and should be confirmed against the label.

No drug interaction records were found.

For label-based warnings, contraindications and interactions, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score (L5). There are no clinical trials or publications. A topical antiseptic is also mechanistically unlikely to treat a blood-stage parasitic infection.

**To proceed, the following is needed:**
- Laboratory (in vitro) evidence of antiplasmodial activity at clinically achievable, safe concentrations
- Mechanism of action data and a plausible route of delivery for a systemic infection
- Label-based safety information from the TGA-approved PI, including the approved indication text

**Note for portfolio prioritisation:** Other TxGNN predictions for povidone-iodine have more evidence than malaria. These are pneumonia (L2, mainly COVID-19 viral-load and oral-care trials), appendicitis (L2, a Phase 2 paediatric irrigation pilot) and peritonitis (L3, with notable safety concerns for intraperitoneal use). If this drug is being considered for repurposing, these may be better candidates for a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

