---
layout: default
title: Penicillamine
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Penicillamine: predicted new indication Megaloblastic anaemia (evidence level L5). Approved use: Rheumatoid arthritis, cystinuria…"
monitor_inn: "Penicillamine"
predicted_indications: ["megaloblastic anemia (disease)", "tricarboxylic acid cycle disorder", "disease of transporter activity", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "adult polyglucosan body disease", "granulomatous disease, chronic, X-linked", "pyruvate metabolism disorder"]
---

# Penicillamine
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

# Penicillamine: From Rheumatoid Arthritis and Wilson Disease to Megaloblastic Anaemia

## One-Sentence Summary

Penicillamine is a copper-chelating drug originally used for conditions such as rheumatoid arthritis, Wilson disease and cystinuria.
The TxGNN model predicts it may be effective for **megaloblastic anaemia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no supporting evidence, and a plausible safety concern (penicillamine can itself cause haematological toxicity).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, cystinuria, Wilson disease and other metabolic disorders (the ARTG entry carries no indication text) |
| Predicted New Indication | Megaloblastic anaemia |
| TxGNN Prediction Score | 98.02% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, penicillamine is a copper chelator that is used in Wilson disease and cystinuria, and its efficacy in those conditions is established.

The data compiled for this report do not support a mechanistic link to megaloblastic anaemia. Megaloblastic anaemia is usually caused by folate or vitamin B12 deficiency, and copper chelation has no established role in correcting either. The high TxGNN score (0.98) most likely reflects network proximity in the knowledge graph (for example, shared links with other iron- and blood-related conditions) rather than a biological rationale.

Penicillamine is also associated with haematological toxicity, including anaemia and bone marrow suppression. A benefit in a blood disorder is therefore implausible without direct supporting evidence.

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
| ARTG 13425N | D-Penamine | Tablet 250 mg (oral) | Indication text not listed in the data compiled for this report |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** The knowledge graph links penicillamine with contraindications in several blood and related conditions. These are particularly relevant to a haematological indication:
  - Aplastic anaemia (including idiopathic)
  - Iron deficiency anaemia and other deficiency or hypochromic anaemias
  - Thrombocytopenia, leukopenia, agranulocytosis and neutropenia (including congenital forms)
  - Other signals: kidney disease, glomerulonephritis, pemphigus, myasthenia gravis and other neuromuscular junction disease, aphthous stomatitis
- **Drug Interactions:** 64 interactions were identified. The 20 listed are all of moderate severity. They are mainly with products that can reduce absorption by binding the drug:
  - Calcium salts (phosphate, acetate, carbonate, citrate, gluconate, lactate)
  - Magnesium salts (oxide, sulfate, chloride, carbonate, citrate, gluconate)
  - Zinc salts (sulfate, acetate)
  - Aluminium hydroxide, magaldrate, kaolin, attapulgite
  - Iron
- **G6PD deficiency:** The data raise a concern about haemolysis in G6PD-deficient patients, which should be reviewed before any further consideration.

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The known haematological toxicity and the knowledge-graph contraindications in anaemias argue against pursuing this indication.

**To proceed, the following is needed:**
- Any mechanistic or clinical evidence linking penicillamine to megaloblastic anaemia (none currently exists)
- Mechanism of action data
- TGA Product Information warnings and contraindications for D-Penamine, to complete the safety screen
- A haematological safety assessment, including G6PD status and bone marrow suppression risk

---

### Note on Other Predictions

The other top-ranked predictions were also reviewed:

- **Disease of transporter activity (rank 3, score 93.0%):** This category includes Wilson disease, which is already an established penicillamine indication, so it is not a new repurposing finding. It was classified as a research question; evidence for other transporter disorders is indirect.
- **Tricarboxylic acid cycle disorder (rank 2) and pyruvate metabolism disorder (rank 9):** Evidence is indirect and conceptual (copper homeostasis and cuproptosis reviews, historical cystinosis reports). Both are Hold.
- **Ranks 4–8 and 10:** These include a rare neurodevelopmental disorder, glycogen branching enzyme deficiency forms, adult polyglucosan body disease, X-linked chronic granulomatous disease and G6PD-deficiency haemolytic anaemia. All are model-only (L5) predictions or rely on irrelevant, keyword-matched literature, so all are Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

