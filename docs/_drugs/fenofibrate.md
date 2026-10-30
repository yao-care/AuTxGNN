---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-30
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia…"
---

# Fenofibrate
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

## Fenofibrate: From Hypertriglyceridaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug, recorded in the knowledge graph for hypertriglyceridaemia and several familial and combined hyperlipidaemias.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but there are **no registered clinical trials** and only **3 preclinical or mechanistic publications**, none of which studies the disease directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, familial combined hyperlipidaemia, hypoalphalipoproteinaemia (relations recorded in the knowledge graph; the Australian licence record contains no approved indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, fenofibrate is a PPAR-alpha agonist. It lowers triglycerides and tends to raise HDL cholesterol, through effects on lipoprotein lipase, apoA-I/apoA-II and apoC-III expression. This is background knowledge, not drawn from the compiled data.

The link to CETP deficiency is indirect and weak:

- A 2010 mouse study combined a CETP inhibitor with a PPAR-alpha agonist (fenofibrate). It reported additive HDL-C increases and LDL-C reductions, but it did not involve a CETP-deficient population.
- A 2001 mouse study linked fenofibrate-induced PLTP gene expression to HDL enlargement. This is a mechanism that may overlap with the HDL remodelling seen in CETP deficiency.
- A 2018 study found that plasma HDL levels did not correlate with faecal cholesterol excretion or cholesterol efflux capacity. This undermines the assumption that raising HDL is a useful goal.

CETP deficiency already features markedly elevated HDL-C, so the case for giving an HDL-raising drug is weak, and the therapeutic target is unclear. The high TxGNN score is a model output and is not supported by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical (transgenic mice) | J Cardiovasc Pharmacol Ther | CETP inhibition (torcetrapib) plus PPAR-alpha agonism (fenofibrate) raised HDL-C and lowered LDL-C in human ApoB100/CETP transgenic mice |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclinical (mice) | J Biol Chem | Fenofibrate induced the PLTP gene, accounting for HDL enlargement in treated mice |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Preclinical/mechanistic | Front Physiol | Plasma HDL did not correlate with faecal cholesterol or cholesterol efflux capacity, so HDL function matters more than HDL-C level; not specific to fenofibrate in CETP deficiency |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13469X | FENOFIBRATE RBX | Tablet 48 mg (oral) | Not stated in the available record |

This is a single-ingredient product with a valid licence. The list is complete.

---

## Safety Considerations

**Contraindication relations recorded in the knowledge graph** (not label text) include:
- Liver failure and liver disease
- Pancreatitis
- Gallbladder disease, cholelithiasis and cholecystolithiasis
- Myopathy, muscular disease, rhabdomyolysis and familial periodic paralysis
- Impaired renal function
- Haematological conditions: thrombocytopenia, anaemia, leukopenia, agranulocytosis and neutropenia (including congenital forms)

**Drug interactions:** The interaction screen returned 100 records. The 20 shown are all rated Moderate, and the main groups are:
- Sulfonylureas: acetohexamide, chlorpropamide, glimepiride, glipizide and glyburide
- Many insulin products, including human, aspart, degludec, detemir, glargine, glulisine and lispro
- Chenodeoxycholic acid
- Esomeprazole

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies fenofibrate in CETP deficiency, so the evidence level is L5. The available preclinical work is only indirect. Because CETP deficiency already raises HDL-C, the clinical rationale for fenofibrate is unclear despite the high model score.

**To proceed, the following is needed:**
- A clear statement of the clinical benefit sought in CETP deficiency (the target is currently unclear)
- Direct clinical or mechanistic studies in CETP-deficient patients
- Mechanism of action data for fenofibrate
- Approved indication text and safety sections from the TGA Product Information for ARTG 13469X
- A safety review of the contraindication relations and interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

