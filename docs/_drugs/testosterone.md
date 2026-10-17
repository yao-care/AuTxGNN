---
layout: default
title: Testosterone
parent: Model Prediction Only (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Testosterone: predicted new indication Polysomy of X chromosome (evidence level L5). Approved use: Hypogonadotropic hypogonadism and related pituitary hormone deficienc…"
monitor_inn: "Testosterone"
predicted_indications: ["polysomy of X chromosome", "tetragametic chimerism", "penile/testicular agenesis", "testicular regression syndrome", "Leydig cell hypoplasia due to LH resistance", "urethral obstruction sequence", "46,XX disorder of sex development-anorectal anomalies syndrome", "freemartinism", "arthrogryposis epileptic seizures migrational brain disorder"]
---

# Testosterone
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

# Testosterone: From Hypogonadotropic Hypogonadism to Polysomy of X Chromosome

## One-Sentence Summary

Testosterone is an androgen replacement therapy, originally used for conditions of androgen deficiency such as hypogonadotropic hypogonadism and pituitary hormone deficiencies.
The TxGNN model predicts it may be effective for **polysomy of X chromosome** (a sex chromosome aneuploidy such as 47,XXX), with a high score of **94.9%**.
However, **no clinical trials and no publications** currently support this specific prediction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypogonadotropic hypogonadism and related pituitary hormone deficiencies (approved indication text is not listed for the Australian product) |
| Predicted New Indication | Polysomy of X chromosome |
| TxGNN Prediction Score | 94.88% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, testosterone is an androgen that replaces deficient sex hormone signalling. Its efficacy in hypogonadism is established, but there is no clear mechanistic rationale for polysomy X.

Polysomy X (for example 47,XXX or 48,XXXX) occurs in people with a female phenotype. The score appears to reflect the drug's closeness to sex-hormone and gonadal-disorder conditions in the model's network, not a specific biological pathway. A related condition, 47,XXY (Klinefelter syndrome), is treated with testosterone, but that benefit does not transfer to polysomy X.

This is therefore a weak, indirect prediction. Of the ten conditions the model ranked for testosterone, other candidates have stronger rationale (see the conclusion).

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
| ARTG 10378F | AndroForte 5 | Transdermal cream, 50 mg per mL, 50 mL | Not listed in the data compiled for this report |

Only a topical (transdermal cream) product is registered. Other routes of administration, such as injectable or implant forms, are not represented in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and the 20 shown in the data compiled for this report are all rated Moderate. The main groups are:
  - **Corticosteroids**: hydrocortisone, betamethasone, budesonide, dexamethasone
  - **Sulfonylureas**: acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide
  - **Insulins**: human, aspart, degludec, detemir, glargine, glulisine and others
  - **Other**: aprepitant, topical calcitriol
- **Conditions flagged for caution** (drug-disease associations in the model's knowledge base, not taken from the product label): hypertension, epilepsy, kidney disease, liver disease, congestive heart failure, diabetes mellitus, asthma, hypothyroidism, systemic lupus erythematosus, hypercalcaemia, benign prostatic hyperplasia, hypertriglyceridaemia, female breast carcinoma, thrombophlebitis and uterine leiomyoma.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as label-based data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by the model score alone (L5), with no registered trials or publications. There is also no plausible mechanism for benefit in people with a female phenotype and no documented androgen deficiency.

**To proceed, the following is needed:**
- A clear clinical rationale, for example specific patient subgroups with documented hypogonadism or androgen deficiency
- Mechanism of action data and a mechanistic link analysis
- Label-based warnings and contraindications from the PI, and an assessment of whether the registered topical cream suits the intended use
- Resources redirected to better-supported candidates from the same analysis:
  - **Testicular regression syndrome** (L3, Proceed with Guardrails): testosterone replacement is established practice, supported by reviews and clinical management papers, with no registered trials.
  - **Primary ovarian failure** (L1 by trial existence, Research Question): the Phase 3 trial NCT06343870 is recruiting and has no results yet.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

