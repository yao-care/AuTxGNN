---
layout: default
title: Lansoprazole
parent: Moderate Evidence (L3-L4)
nav_order: 412
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Lansoprazole: predicted new indication Duodenogastric reflux (evidence level L4). Approved use: Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction", "peptic ulcer perforation", "gastrojejunal ulcer", "abnormality of glucagon secretion", "gastroduodenitis", "acne (disease)", "Smouldering systemic mastocytosis", "leather-bottle stomach", "duodenitis"]
---

# Lansoprazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Lansoprazole: From Gastric Ulcer and Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor originally used for gastric and duodenal ulcers, reflux disease, esophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but there are **no registered clinical trials** and only **1 general review** supporting this direction, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, duodenal ulcer, Zollinger-Ellison syndrome (the approved indication text on the Australian licence entry is blank) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lansoprazole belongs to the proton pump inhibitor class, which suppresses gastric acid by inhibiting the gastric H+/K+-ATPase. Its efficacy in acid-related upper gastrointestinal disease is well established.

Duodenogastric (bile) reflux is mainly a problem of motility and pyloric function, not of acid secretion. Acid suppression may ease symptoms from associated mucosal injury, but it does not address the underlying cause. The high TxGNN score probably reflects the proximity of this condition to approved upper gastrointestinal indications in the knowledge graph. The only supporting publication is a general review of proton pump inhibitors, with no direct evidence for this condition.

The other top-ranked predictions are summarised below to give context.

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Duodenal obstruction | 99.68% | L5 | Hold |
| 3 | Peptic ulcer perforation | 98.80% | L4 | Research question |
| 4 | Gastrojejunal ulcer | 98.80% | L4 | Research question |
| 5 | Abnormality of glucagon secretion | 98.60% | L5 | Hold |
| 6 | Gastroduodenitis | 97.57% | L3 | Proceed with Guardrails |
| 7 | Acne | 97.00% | L5 | Hold |
| 8 | Smouldering systemic mastocytosis | 95.61% | L5 | Hold |
| 9 | Leather-bottle stomach | 94.74% | L5 | Hold |
| 10 | Duodenitis | 94.67% | L3 | Proceed with Guardrails |

Gastroduodenitis and duodenitis have the most plausible rationale, but both overlap substantially with existing ulcer and esophagitis indications. They would add little as new indications.

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
Acid suppression does not address the cause of duodenogastric reflux, and there are no trials and no direct literature. The prediction rests on model proximity alone (L4).

**To proceed, the following is needed:**
- Direct clinical evidence (trials or cohort studies) of lansoprazole in duodenogastric reflux
- Mechanism of action data and a clearer rationale beyond acid suppression
- Product Information warnings and contraindications from the TGA, plus the approved indication text for the ARTG entry
- Route and formulation compatibility assessment
- Consideration of lower-risk candidates such as gastroduodenitis or duodenitis, noting their overlap with existing indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

