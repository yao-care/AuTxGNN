---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Lithium carbonate"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
description: "Lithium Carbonate: predicted new indication Pseudoachondroplasia (evidence level L5). In Australia: 2 PBS items (2 currently listed)"
---

# Lithium Carbonate
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

## Lithium Carbonate: Pseudoachondroplasia
{: .text-alpha }

## One-Sentence Summary

Lithium carbonate is a mood stabiliser, originally used to treat bipolar disorder and related affective disorders.
The TxGNN model predicts it may be effective for **pseudoachondroplasia**, a rare skeletal dysplasia,
but there are currently **0 clinical trials** and **0 publications** specific to this prediction. This is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lithium carbonate: "The mechanism of action of lithium as a mood stabilizing agent is unknown." ([DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544), label version 2022-11-03; accessed 2026-11-19.) Lithium is widely described as inhibiting glycogen synthase kinase-3 (GSK-3), which modulates Wnt signalling and autophagy. This is general background knowledge, not data from the compiled sources.

Pseudoachondroplasia is caused by COMP gene mutations, which lead to chondrocyte endoplasmic reticulum stress and defects in the extracellular matrix. Lithium's effects on Wnt signalling and autophagy could plausibly touch skeletal or chondrocyte pathways. However, this link is speculative. The score of 0.9998 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are also rare skeletal or developmental disorders (for example acromesomelic dysplasia, Hunter-Thompson type, 0.9996; brachyolmia, 0.9996; and brachydactyly-syndactyly syndrome, 0.9995). All have TxGNN scores of 0.9995 or higher and none has supporting clinical evidence, so the cluster may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

For context, the only publication retrieved across the top predictions was a general review for a related prediction (brachyolmia-amelogenesis imperfecta syndrome):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/) | 2019 | Review | Orphanet J Rare Dis | Overview of the evolving therapeutic landscape of genetic skeletal disorders. It is not specific to lithium. |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 3059B | Lithicarb | Lithium carbonate | Tablet containing lithium carbonate 250 mg | Valid |
| 8290H | Quilonum SR | Lithium carbonate | Tablet containing lithium carbonate 450 mg (slow release) | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from graph edges, not from label text): kidney disease, hypothyroidism, myxedema, congenital hypothyroidism, psoriasis, parapsoriasis, cognitive disorder, sudden cardiac arrest, heart conduction disease, diabetes insipidus (including central and neurohypophyseal forms) and pyoureter.
- **Drug interactions:** 100 interactions were identified. Those listed in the compiled data include:
  - **Major:** bupropion, lorcaserin.
  - **Moderate:** metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide, famotidine, loperamide, mesalazine, balsalazide, morphine, metronidazole, clarithromycin and potassium citrate.
  - **Minor:** doxycycline, epinephrine and acetylsalicylic acid.

Lithium has a narrow therapeutic index. Please refer to the TGA-approved Product Information (PI) for full warnings, contraindications and monitoring requirements.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning). There are no clinical trials or drug-specific publications, and the mechanistic link is speculative. Lithium also carries a notable safety burden (narrow therapeutic index, renal and thyroid effects, many interactions), and a postnatal drug is unlikely to correct a COMP-related structural defect.

**To proceed, the following is needed:**
- Mechanism of action data, and preclinical evidence (for example in COMP-mutant chondrocyte or mouse models) showing that lithium reduces ER stress or improves cartilage matrix
- TGA-approved Product Information, including warnings, contraindications and approved indications for Lithicarb
- A benefit-risk assessment for long-term lithium use in paediatric and young adult skeletal dysplasia populations
- Review of the other top-ranked predictions (such as Behr syndrome and WHIM syndrome), where biological plausibility may be somewhat higher, although they also have no clinical evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

