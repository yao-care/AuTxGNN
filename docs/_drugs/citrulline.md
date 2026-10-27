---
layout: default
title: Citrulline
parent: Model Prediction Only (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Citrulline: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available"
monitor_inn: "Citrulline"
predicted_indications: ["multiple endocrine neoplasia", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "dyspepsia", "benign mammary dysplasia", "exocrine pancreatic insufficiency", "pregnancy associated osteoporosis", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "succinyl-CoA:3-ketoacid CoA transferase deficiency"]
---

# Citrulline
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

## Citrulline: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Citrulline is an amino acid supplement listed in Australia as an oral tablet, but no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, with a high score of 97%.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the ARTG data compiled) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 97.00% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Citrulline is known to participate in the urea cycle and to be a precursor of arginine, which supports nitric oxide synthesis. Its original indication could not be determined from the data compiled.

No mechanistic link to multiple endocrine neoplasia (for example MEN1 or RET-driven endocrine tumours) has been identified. The high TxGNN score reflects a knowledge-graph association only, and it should not be read as evidence of clinical benefit.

**Other predictions in the data (all Hold):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Mitochondrial oxidative phosphorylation disorder (nuclear DNA anomalies) | 83.88% | L5 | Plausible via nitric oxide, but no trials or literature |
| 3 | Dyspepsia | 80.69% | L4 | Citrulline appears as a gut biomarker, not as a therapy |
| 5 | Exocrine pancreatic insufficiency | 73.56% | L4 | One cohort study using citrulline as an enterocyte marker |
| 4, 6–10 | Benign breast conditions, pregnancy-associated osteoporosis, succinyl-CoA:3-ketoacid CoA transferase deficiency | 68.80–74.48% | L5 | No supporting evidence |

## Clinical Trial Evidence

For the top-ranked prediction (multiple endocrine neoplasia), currently no related clinical trials are registered.

For context, the only trial identified across the top 10 predictions was for dyspepsia (rank 3). It is non-interventional and not a treatment study:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01849107](https://clinicaltrials.gov/study/NCT01849107) | NA | Completed | 49 | Plasma citrulline evaluated as a biomarker of radiation-induced small bowel toxicity. Citrulline was not tested as a treatment, and dyspepsia patients were not studied. |

## Literature Evidence

For the top-ranked prediction (multiple endocrine neoplasia), currently no related literature is available.

Literature found for lower-ranked predictions (all low-tier and indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39149805](https://pubmed.ncbi.nlm.nih.gov/39149805/) | 2024 | Cohort | J Pediatr Gastroenterol Nutr | Metabolomic comparison of postprandial distress syndrome patients with and without duodenal eosinophilia (dyspepsia). Associative only. |
| [30579666](https://pubmed.ncbi.nlm.nih.gov/30579666/) | 2019 | Cohort | Clin Nutr | Exocrine pancreatic and enterocyte function in advanced pancreatic cancer. Suggests citrulline is a marker of intestinal function, not a treatment. |
| [29732286](https://pubmed.ncbi.nlm.nih.gov/29732286/) | 2018 | Pilot study | Transl Androl Urol | Daily Revactin in men with erectile dysfunction. Off-topic for dyspepsia. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10736C | Citrulline Easy | Tablet 1 g, 300 (oral) | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

No drug interaction records were found, and no disease contraindications were identified from the knowledge graph. This reflects missing data, not confirmed safety.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The multiple endocrine neoplasia prediction is supported only by a knowledge-graph score (Evidence Level L5), with no trials, no literature and no identified mechanistic link. Key regulatory and safety data are also missing, so screening cannot proceed.

**To proceed, the following is needed:**
- The approved indication and Product Information (including warnings and contraindications) for Citrulline Easy
- Mechanism of action data for citrulline (for example from DrugBank)
- A plausible mechanistic link to multiple endocrine neoplasia, supported by preclinical or clinical evidence
- Route compatibility and dosing assessment for the predicted indication
- If the project is to continue, consider prioritising the mitochondrial disorder prediction (rank 2), which has a more plausible nitric oxide rationale, once supporting studies are found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

