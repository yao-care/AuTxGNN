---
layout: default
title: Migalastat
parent: Model Prediction Only (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Migalastat: predicted new indication Hepatoportal sclerosis (evidence level L5). Approved use: Fabry disease"
monitor_inn: "Migalastat"
predicted_indications: ["hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatic porphyria", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "nodular regenerative hyperplasia of the liver"]
---

# Migalastat
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

## Migalastat: From Fabry Disease to Hepatoportal Sclerosis
{: .text-alpha }

## One-Sentence Summary

Migalastat is an oral pharmacological chaperone, originally used to treat Fabry disease in patients with amenable GLA variants.
The TxGNN model predicts it may be effective for **hepatoportal sclerosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fabry disease (the approved indication text is not available in the Australian registration data; the knowledge graph also lists chylomicron retention disease and lysosomal lipid storage disorder) |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Migalastat is a pharmacological chaperone that stabilises amenable mutant alpha-galactosidase A, and its efficacy in Fabry disease is established. It is an alternative to enzyme replacement therapy for suitable patients.

No mechanistic link to hepatoportal sclerosis (obliterative portal venopathy) has been established. Nothing in the available data connects alpha-galactosidase A chaperoning to the pathophysiology of this condition. The high TxGNN score most likely reflects graph proximity to liver-related nodes rather than a biological rationale, so it should be read as a hypothesis-generating signal only.

The same score (98.85%) was given to several other hepatic vascular or liver conditions, including primitive portal vein thrombosis, hepatopulmonary syndrome, early-onset familial noncirrhotic portal hypertension and idiopathic copper-associated cirrhosis. This clustering suggests a graph-driven pattern rather than disease-specific insight. The other predictions (hepatic porphyria, mitochondrial oxidative phosphorylation disorder, disorder of tyrosine metabolism, teratogenic Pierre Robin syndrome and nodular regenerative hyperplasia of the liver) also have no supporting trials or literature, and no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14573B | Galafold | Capsule containing 150 mg migalastat hydrochloride (equivalent to 123 mg migalastat); oral | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions:**
  - **Agalsidase beta** (moderate): the interaction is rated moderate in DDInter. Agalsidase beta is an enzyme replacement therapy for Fabry disease, so co-administration needs specialist review.
  - **Alpha glucosidase (GAA)**: this is a pharmacological target association rather than a graded interaction. No severity level is available.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as this information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and no plausible mechanistic link between migalastat's chaperone activity and hepatoportal sclerosis. The high TxGNN score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic-link analysis
- Warnings and contraindications from the TGA-approved Product Information, to allow safety screening
- Preclinical or mechanistic evidence linking migalastat to the pathophysiology of hepatoportal sclerosis
- A literature and trial registry search (including ANZCTR) to confirm that no relevant studies exist
- Approved indication text for the ARTG entry, to confirm the current regulatory scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

