---
layout: default
title: Drospirenone
parent: Model Prediction Only (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Drospirenone: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
monitor_inn: "Drospirenone"
predicted_indications: ["zinc, elevated plasma", "dyschondrosteosis-nephritis syndrome", "torticollis-keloids-cryptorchidism-renal dysplasia syndrome", "infundibulopelvic stenosis-multicystic kidney syndrome", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "46,XX disorder of sex development-anorectal anomalies syndrome", "thyrocerebrorenal syndrome", "acrorenal syndrome", "radial hypoplasia-triphalangeal thumbs-hypospadias-maxillary diastema syndrome", "Mayer-Rokitansky-Kuster-Hauser syndrome"]
---

# Drospirenone
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

# Drospirenone: From Acne and Atrophic Vaginitis to Elevated Plasma Zinc

## One-Sentence Summary

Drospirenone is a progestin with antimineralocorticoid and antiandrogenic activity, originally used for conditions such as acne and postmenopausal atrophic vaginitis, and in Australia it is marketed as a progestogen-only oral pill.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but **no clinical trials** and **no publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne; postmenopausal atrophic vaginitis (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 98.74% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, drospirenone is a progestin that also blocks mineralocorticoid and androgen receptors, similar to its parent compound spironolactone. These actions explain its use in acne and in hormone-related conditions.

No known pathway links these actions to the regulation of plasma zinc, and the data compiled for this report found none. The high TxGNN score (98.74%) is a model output only. It most likely reflects network proximity in the knowledge graph rather than a clinical rationale. This prediction should be treated as a hypothesis with no supporting evidence.

Other predictions for this drug are not better supported. Ranks 2 to 10 are mostly ultra-rare congenital syndromes (for example, kidney or limb malformation syndromes and Mayer-Rokitansky-Kuster-Hauser syndrome). Each lacks a credible mechanistic link and has no clinical trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for elevated plasma zinc.

For context, the second-ranked prediction (dyschondrosteosis-nephritis syndrome) returned 20 publications. They cover premenstrual syndrome, polycystic ovary syndrome (PCOS) and drospirenone-containing contraceptives. They are keyword matches on the drug, not evidence for that disease, and are not counted here.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14791L | Slinda | Pack containing 24 tablets 4 mg and 4 inert tablets (oral) | Not available in the data compiled for this report |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

The following items come from a knowledge graph (not label text) and should be verified against the PI.

- **Conditions flagged as contraindications in the knowledge graph** include hypertensive disorders, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, adrenocortical insufficiency (Addison disease), hypothyroidism, systemic lupus erythematosus, asthma, diabetes mellitus (including diabetic ketoacidosis), hypertriglyceridemia, and hypercalcemia-related conditions.
- **Drug interactions:** 100 interactions were identified, and the main ones are listed below.
  - **Major:** clarithromycin.
  - **Moderate:** antidiabetic agents (for example acarbose, albiglutide, alogliptin, canagliflozin, dapagliflozin, empagliflozin, exenatide, glimepiride, glipizide, glyburide), aprepitant, acetylsalicylic acid, potassium citrate and clotrimazole.

Because drospirenone has antimineralocorticoid activity, potassium and renal function would be relevant to any new use. This should be confirmed against the PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for elevated plasma zinc is supported only by a model score, with no clinical trials, no relevant publications and no identified mechanistic link (Evidence Level L5). The other top-ranked predictions are likewise unsupported.

**To proceed, the following is needed:**
- A plausible mechanistic rationale linking drospirenone to plasma zinc regulation, plus mechanism of action data from DrugBank
- Preclinical or observational evidence specific to this indication
- Confirmation that there is a clinical need, since elevated plasma zinc is not an established treatment target for this drug
- The TGA Product Information, to complete safety screening (warnings, contraindications and the approved indication text for Slinda)
- Assessment of route compatibility and of the original-to-new indication similarity, both currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

