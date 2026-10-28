---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 412
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Lansoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor originally used for gastric and duodenal ulcers, reflux disease, esophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **duodenal obstruction**, but there are **no registered clinical trials** and only **1 general review** supporting this direction, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lansoprazole belongs to the proton pump inhibitor class, which suppresses gastric acid by inhibiting the gastric H+/K+-ATPase. Its efficacy in acid-related upper gastrointestinal disease is well established.

Duodenogastric (bile) reflux is mainly a problem of motility and pyloric function, not of acid secretion. Acid suppression may ease symptoms from associated mucosal injury, but it does not address the underlying cause. The high TxGNN score (0.9968) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only supporting publication is a general review of proton pump inhibitors, with no direct evidence for this condition.

The other top-ranked predictions are summarised below to give context.

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Duodenal obstruction | 0.9968 | L5 | Hold |

They would add little as new indications.

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Update on proton pump inhibitors as first-choice drugs for peptic ulcer, H. pylori infection, GORD, NSAID-related lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux directly. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11669E | Zopral | Capsule 30 mg (oral) | Not stated in the data compiled |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** The graph links lansoprazole to a broad set of conditions, including long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, porphyria, osteoporosis, cardiovascular and cerebrovascular events (myocardial infarction, stroke), anaemia, blood coagulation disease, Clostridium difficile colitis and myasthenia gravis. These are graph associations, not confirmed contraindications, and need verification against the Product Information.
- **Drug Interactions:** 100 interactions were identified, and the entries reviewed include:
  - **Major:** acalabrutinib, atazanavir.
  - **Moderate:** hydrochlorothiazide, atorvastatin, fenofibrate, bromocriptine, apalutamide, aprepitant, bosutinib, brigatinib, amphetamine, amikacin, ampicillin, amphotericin B and abametapir (topical).
  - **Minor:** acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin.
- A published case report describes lansoprazole-associated thrombocytopenia (PMID 11978156).

Please also refer to the TGA-approved Product Information (PI) for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acid suppression does not address the cause of duodenogastric reflux, and there are no trials and no direct literature. The prediction rests on model scores alone (L4), which may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Direct clinical evidence (trials or cohort studies) of lansoprazole in duodenogastric reflux
- Mechanism of action data and a clearer rationale beyond acid suppression
- Product Information warnings and contraindications from the TGA, plus the approved indication text for the ARTG entry
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

