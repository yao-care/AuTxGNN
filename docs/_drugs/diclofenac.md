---
layout: default
title: Diclofenac
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diclofenac: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Osteoarthritis, rheumatoid arthritis, ankylosing spondylitis…"
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
---

# Diclofenac
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

## Diclofenac: From Osteoarthritis and Rheumatoid Arthritis to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Diclofenac is a nonsteroidal anti-inflammatory drug (NSAID) used for arthritis (osteoarthritis, rheumatoid arthritis, ankylosing spondylitis) and for skin conditions such as actinic keratosis.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare inherited hair-loss disorder.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, actinic keratosis and related skin conditions (taken from the knowledge-graph indication list, as no ARTG indication text was available) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Diclofenac is an NSAID, and its effects are generally attributed to inhibition of cyclo-oxygenase (COX) and the resulting reduction in prostaglandin-driven inflammation and pain. That mechanism underlies its use in arthritis and inflammatory skin conditions.

The link to the predicted indication is weak. Hypotrichosis simplex is a monogenic hair-loss disorder (for example, variants in *CDSN*, *APCDD1* or *RPL21*). It is not driven by COX- or prostaglandin-mediated inflammation. The only speculative angle is that prostaglandin signalling can influence the hair follicle cycle, but NSAIDs are not established hair-growth agents.

The high TxGNN score is therefore most likely a knowledge-graph artefact, probably reflecting network proximity to diclofenac's dermatological original indications rather than a shared biological pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1299J | Fenac EC | Enteric-coated tablet containing diclofenac sodium 25 mg (oral) | Not recorded in the data compiled for this report |

Only oral products are listed. No topical formulation appears in the Australian data compiled for this report.

---

## Safety Considerations

Safety data for this drug is limited to the following items. Please also refer to the TGA-approved Product Information (PI), because no label-based warnings or contraindications were available.

- **Contraindications and risk conditions (from the knowledge graph, not label text):** these include:
  - cardiovascular: hypertension, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, other heart and cardiovascular disease
  - gastrointestinal: active peptic ulcer disease, inflammatory bowel disease
  - hepatic: liver disease, liver failure, drug-induced liver injury, gallbladder disease
  - respiratory: asthma (including allergic and intrinsic asthma)
  - metabolic: diabetes mellitus, diabetic ketoacidosis
  - haematological: blood coagulation disorders, anaemia, haemoglobinopathy
  - other: substance abuse/dependence, keratitis
- **Drug interactions (DDInter, 100 interactions identified; the first 20 were reviewed here):**
  - Moderate: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, metformin, sulfonylureas (glimepiride, glipizide, chlorpropamide, acetohexamide), exenatide, mesalazine, balsalazide, aprepitant, fenfluramine and dexfenfluramine.
  - Minor: the acid-suppressing agents famotidine, ranitidine and cimetidine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypotrichosis simplex of the scalp has no supporting trials or literature and no plausible mechanistic link. The high score most likely reflects graph proximity rather than biology. Repurposing diclofenac for this disorder is not supported at this time.

Among the ten top-ranked predictions in the data compiled for this report, only juvenile idiopathic arthritis (rank 9) has any supporting literature. That evidence is small, older studies and reviews of diclofenac in juvenile arthritis (L3, Proceed with Guardrails). It is an extension of diclofenac's existing arthritis use rather than a new mechanism, and it would be a more useful focus for further evaluation.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a credible biological rationale linking COX/prostaglandin pathways to this hair-loss disorder
- Preclinical or early clinical evidence of any effect on hair growth
- TGA-approved PI warnings and contraindications, plus the ARTG-approved indication text for Fenac EC
- Assessment of whether a topical or other route would be needed, since only an oral tablet is currently registered in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

