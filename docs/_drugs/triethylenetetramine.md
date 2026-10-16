---
layout: default
title: Triethylenetetramine
parent: Model Prediction Only (L5)
nav_order: 754
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Triethylenetetramine: predicted new indication Thyroid gland undifferentiated (anaplastic) carcinoma (evidence level L5). Approved use: Wilson disease . No approved indication text is recorded for th…"
monitor_inn: "Triethylenetetramine"
predicted_indications: ["thyroid gland undifferentiated (anaplastic) carcinoma", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "hepatic porphyria", "disorder of tyrosine metabolism", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma"]
---

# Triethylenetetramine
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

# Triethylenetetramine: From Wilson Disease to Thyroid Gland Undifferentiated (Anaplastic) Carcinoma

## One-Sentence Summary

Triethylenetetramine (trientine) is a copper chelator, originally used to treat **Wilson disease**.
The TxGNN model predicts it may be effective for **anaplastic thyroid carcinoma**,
but **no clinical trials and no publications** were found to support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wilson disease (also listed in the knowledge graph: renal cell carcinoma subtypes, iron metabolism disease, hereditary haemochromatosis). No approved indication text is recorded for the Australian entry. |
| Predicted New Indication | Thyroid gland undifferentiated (anaplastic) carcinoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, triethylenetetramine is a copper chelator that is established in Wilson disease, a copper-overload disorder. Mechanistically, it may be applicable to anaplastic thyroid carcinoma.

A plausible but unvalidated link is copper depletion. Copper is a cofactor in angiogenesis and tumour signalling, and copper-depleting agents have been explored preclinically in several cancers. The high TxGNN score is a computational prediction only. Because the original mechanism data is missing, the link cannot be checked against the drug's known mechanism.

Other high-scoring predictions from the same model run are also unsupported by evidence:
- **Idiopathic copper-associated cirrhosis** is the most mechanistically coherent. Copper chelation has a clear rationale in copper-overload liver disease, and this is flagged as a research question. A targeted literature search is a reasonable next step.
- **Renal cell carcinoma subtypes** (TFE3-fusion and neuroblastoma-associated) probably score highly because renal cell carcinoma is already in the drug's knowledge-graph indication list. This is not independent validation.
- Portal hypertension, portal vein thrombosis, hepatopulmonary syndrome, hepatic porphyria and tyrosine metabolism disorder likely reflect graph proximity to hepatic and metabolic disease. No supported mechanism was identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13124R | Trientine Waymade | Oral capsule containing trientine dihydrochloride 250 mg (equivalent to 166.7 mg trientine) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Drug interactions:** 27 interactions were identified, and the 20 detailed entries are all rated Moderate. They fall into three groups:
  - **Calcium salts:** phosphate, acetate, carbonate, citrate, glubionate, gluconate and lactate.
  - **Magnesium salts:** oxide, carbonate, chloride and citrate.
  - **Iron and trace minerals:** iron, ferrous fumarate, ferrous gluconate, ferrous sulfate, iron protein succinylate, tetraferric tricitrate, selenium, manganese sulfate and copper gluconate.
  These are consistent with metal-binding (chelation) interactions, so dose separation from mineral products is likely to matter.
- **Knowledge-graph contraindication signals** (from the model's graph, not product label text, so they need confirmation against the PI): hypertension, long QT syndrome and torsades de pointes, liver failure, drug-induced liver injury, adrenocortical insufficiency, hypothyroidism, myocardial infarction, hyperbilirubinaemia, diarrhoeal disease, hereditary haemorrhagic telangiectasia, and peripheral vascular disease, among others.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). No trials or publications were found, and the original mechanism data is missing. Label-based safety data is also unavailable, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Obtain the TGA PI (warnings, contraindications, approved indication text) for ARTG 13124R.
- Obtain mechanism of action data from DrugBank.
- Run a targeted literature search on copper chelation in anaplastic thyroid carcinoma and other cancers.
- Prioritise the copper-associated cirrhosis question, which has the strongest mechanistic rationale, for a separate review.
- Define a plan for managing mineral interactions and monitoring copper status if any new use is pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

