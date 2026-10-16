---
layout: default
title: Alendronic Acid
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alendronic Acid: predicted new indication HIV infectious disease (evidence level L5). Approved use: Postmenopausal osteoporosis, osteoporosis, Paget disease of bone"
---

# Alendronic Acid
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

# Alendronic Acid: From Postmenopausal Osteoporosis to HIV Infectious Disease

## One-Sentence Summary

Alendronic acid is a bisphosphonate originally used to treat osteoporosis (including postmenopausal osteoporosis) and Paget disease of bone.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but this is a computational prediction only, with **no clinical trials** and **no publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis, osteoporosis, Paget disease of bone (from the knowledge graph; no approved indication text is available for the ARTG entry) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 96.78% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, alendronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase and so reduces osteoclast-mediated bone resorption. Its efficacy in osteoporosis and Paget disease of bone is established.

No direct mechanistic link to HIV infection is established. A plausible but unverified indirect link is that alendronic acid could address HIV-associated bone loss. That would be a bone-health benefit, not an antiviral effect. The high TxGNN score is a model output only and should not be read as evidence of antiviral activity.

Other top-ranked predictions (simian immunodeficiency virus infection and feline acquired immunodeficiency syndrome) share the same score pattern. They are likely artefacts of the same graph neighbourhood as HIV, not independent signals. The remaining predictions (for example, deficiency anaemia, osteomesopyknosis and biotin metabolic disease) also have no supporting mechanism, trials or literature in the compiled data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13499L | APO-Alendronate | Tablet 70 mg (as alendronate sodium), oral | Not available in the compiled data |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug–disease contraindication links, not product label text):
  - Oesophageal conditions: achalasia, megaoesophagus, oesophageal dysmotility, oesophageal ulcer, oesophagitis (including eosinophilic and peptic), gastro-oesophageal reflux disease
  - Other gastrointestinal conditions: gastritis, duodenitis
  - Renal and mineral conditions: kidney disease, nephrolithiasis, nephrocalcinosis, hypercalcaemia, hyperphosphataemia, phosphorus metabolism disease
  - Bone and vitamin D conditions: osteomalacia, rickets, vitamin D deficiency, hypervitaminosis
  - Other: osteonecrosis of the jaw, atrial fibrillation, sarcoidosis, arteriosclerosis obliterans
- **Drug Interactions** (100 interactions recorded; examples listed):
  - Moderate: calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate), magnesium salts, aluminium hydroxide, iron, kaolin, attapulgite, magaldrate, acetylsalicylic acid, kanamycin
  - Minor: famotidine, ranitidine, cimetidine

Many of the moderate interactions involve products that reduce oral absorption of bisphosphonates. Please refer to the TGA-approved Product Information (PI) for authoritative warnings, contraindications and dosing advice.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no registered trials, no publications and no plausible antiviral mechanism. Any benefit is more likely to be limited to HIV-associated bone loss, which is a different question.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for the HIV link (antiviral versus bone-protective)
- A systematic literature search, including HIV-associated bone loss and in vitro antiviral studies
- The TGA-approved Product Information (PI), including approved indications, warnings and contraindications for APO-Alendronate
- If pursued, a defined target population and endpoint (for example, bone mineral density in people living with HIV), with consideration of oesophageal and renal safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

