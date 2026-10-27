---
layout: default
title: Folic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 314
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L4). Approved use: Vitamin deficiency disorder"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease", "non-syndromic esophageal malformation", "esophageal disease", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "Plummer-Vinson syndrome", "inborn error of biotin metabolism", "gonococcal urethritis", "Ureaplasma urethritis", "esophageal ulcer", "urinary tract infection (disease)"]
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Folic Acid: From Folate-Deficiency and Other Anaemias to Biotin Metabolic Disease
{: .text-alpha }

## One-Sentence Summary

Folic acid is a B-vitamin originally used to treat vitamin deficiency disorders and anaemias, including folic acid deficiency anaemia and iron deficiency anaemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but there are currently **no registered clinical trials** and only **review-level literature** (about 20 publications, none showing a direct folic acid effect) behind this prediction.
The high score most likely reflects network proximity between B-vitamins rather than a true therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anaemia; iron deficiency anaemia (the ARTG entry in the compiled data has no approved indication text) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Folic acid is a B-vitamin that serves as a cofactor in one-carbon metabolism, and its efficacy in folate-deficiency anaemia is well established.

Folate and biotin are both B-vitamin cofactors, and the literature groups them together as "vitamin-responsive disorders". This shared grouping is probably what drives the high TxGNN score.

However, the mechanistic link is weak. Folic acid does not replace biotin function. Biotinidase deficiency and holocarboxylase synthetase deficiency are treated with biotin itself. The prediction should be read as a computational association among vitamins, not as evidence of a direct therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The retrieved literature is mainly narrative reviews of vitamins and metabolic disease. None of it tests folic acid in biotin metabolic disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Vitamin-responsive disorders (cobalamin, folate, biotin, B1, E); describes inborn errors of vitamin absorption, transport and metabolism |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases; some vitamin-dependent syndromes need pharmacological doses of the specific vitamin |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Vitamin B12 deficiency and the nervous system; notes the links among B12, biotin and folate in metabolic reactions |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; thiamine, pyridoxine and biotin levels are lower in people with diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Vitamins and type 2 diabetes; reports low B-group vitamin levels |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | B vitamins in dermatology; roles in cellular metabolism and red cell synthesis |
| [39828265](https://pubmed.ncbi.nlm.nih.gov/39828265/) | 2025 | Umbrella review | Asia Pac J Clin Nutr | Water-soluble vitamins and glycaemic control in type 2 diabetes; prior meta-analyses were inconsistent |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Narrative article | Arch Biochem Biophys | Micronutrient deficiencies (including folic acid and B12) may damage DNA; argues for optimised intake |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | Preclinical (rat) | Int J Cardiol | Folic acid reduced VCAM-1 expression in the aorta of rats with hyperhomocysteinaemia; not related to biotin |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Biotin and combined biotin and folic acid deficiency induced in rats; a deficiency model, not a treatment study |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10573L | Megafol 5 | Tablet 5 mg (oral) | Not available in the compiled data |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** The drug-disease contraindication links in the TxGNN knowledge graph include kidney disease, nephrolithiasis, sickle cell anaemia, hereditary haemochromatosis, Wilson disease, diabetes mellitus and diabetic ketoacidosis, inflammatory bowel disease, peptic ulcer disease, bipolar disorder, sarcoidosis, hyperparathyroidism and hypercalcaemia, among others. These are model-derived associations and should be checked against the approved Product Information before any clinical interpretation.
- **Drug Interactions:** 100 interactions were identified in total. The main graded ones are pancrelipase (Moderate) and sulfasalazine (Minor). Many others are listed with unknown severity, including metformin, omeprazole, pantoprazole, lansoprazole, glimepiride, acarbose, rosiglitazone, simvastatin, prednisone, triamcinolone, mesalazine, sucralfate, vancomycin, morphine, lactulose, nizatidine, palonosetron and calcitriol.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on no clinical trials and only indirect review literature. Biotin metabolic disorders are treated with biotin itself, and folic acid has no known role in correcting the defect. The high TxGNN score likely reflects similarity among vitamins rather than a therapeutic effect.

**To proceed, the following is needed:**
- Mechanism of action data and a clear biological rationale for folic acid in biotin metabolism
- Preclinical or clinical studies that test folic acid, not biotin, in biotinidase or holocarboxylase synthetase deficiency
- Retrieval of the TGA-approved Product Information (PI), including approved indications, warnings and contraindications
- Review of other predicted indications that may have a stronger rationale (for example, esophageal disease and Plummer-Vinson syndrome, which are research questions with indirect support only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

