---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
description: "Indomethacin: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Indomethacin
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

## Indomethacin: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Indomethacin is a non-steroidal anti-inflammatory drug (NSAID) used for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout and related musculoskeletal conditions.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare genetic skeletal disorder.
There are **no clinical trials and no publications** supporting this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Indomethacin is generally understood to be a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation, pain and fever, and this underpins its use in inflammatory joint disease.

Brachydactyly-syndactyly syndromes are developmental skeletal disorders with a genetic basis. COX inhibition has no established role in their pathophysiology, and an anti-inflammatory drug is not expected to correct a structural genetic defect. The high score (rank 350 in the model's overall ranking) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It does not reflect a pharmacological rationale.

**No mechanistic link has been identified for this prediction.**

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2454E | Arthrexin | Capsule 25 mg (oral) | Not specified in the data compiled |

## Safety Considerations

Warning and contraindication text from the product label was not available. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

**Contraindication-related conditions (knowledge graph, not label text):** The knowledge graph links indomethacin with the following conditions. These should be verified against the PI.
- **Cardiovascular:** hypertension, myocardial infarction and coronary thrombosis, heart and cardiovascular disease, intracerebral haemorrhage
- **Gastrointestinal:** gastric, duodenal and active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, necrotising enterocolitis, oesophageal dyskinesia
- **Renal and hepatic:** kidney disease, liver disease, gallbladder disease
- **Haematological:** thrombocytopenia, blood coagulation disease, haemoglobinopathy
- **Respiratory:** asthma (intrinsic and allergic)
- **Neuropsychiatric:** epilepsy, anxiety, neurotic and dysthymic disorders
- **Other:** infectious disease, pyoureter

**Drug interactions:** The data list 252 recorded interactions. The entries reviewed (from DDInter) include:
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, aprepitant, potassium salts (citrate, bicarbonate), and bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes)
- **Minor:** H2 blockers (famotidine, ranitidine, cimetidine) and linaclotide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism for a genetic skeletal malformation. It does not justify further investment at this stage.

Among the other predictions, **juvenile idiopathic arthritis** (rank 8, evidence level L3) has a plausible mechanism and a dated double-blind comparison of ketoprofen and indomethacin in juvenile chronic arthritis (1978). It is also largely established practice, so its value as a new indication is limited. It may merit separate assessment if a repurposing question is pursued.

**To proceed, the following is needed:**
- Mechanism of action data to test whether any biological link exists to this condition
- Product Information (warnings, contraindications and approved indications) for ARTG 2454E, which is currently a blocking gap for safety screening
- Any preclinical or clinical evidence linking indomethacin to brachydactyly-syndactyly syndrome; without it, this candidate should not advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

