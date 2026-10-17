---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mecasermin: predicted new indication Monosomy X (evidence level L5). Approved use: Growth hormone insensitivity syndrome"
monitor_inn: "Mecasermin"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices with bleeding", "esophageal varices without bleeding", "autosomal ichthyosis syndrome with fatal disease course", "Gaucher disease", "varicose disease", "congenital pulmonary lymphangiectasia", "cholesteryl ester storage disease"]
---

# Mecasermin
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

# Mecasermin: From Growth Hormone Insensitivity Syndrome to Monosomy X

## One-Sentence Summary

Mecasermin is a recombinant form of insulin-like growth factor 1 (IGF-1), originally used for growth hormone insensitivity syndrome (including Laron syndrome).
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**, but **no clinical trials and no publications** were identified to support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Growth hormone insensitivity syndrome; Laron syndrome (from the TxGNN knowledge graph, as no approved indication text was available for the ARTG entry) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mecasermin is an IGF-1 replacement, its use in growth hormone insensitivity (severe primary IGF-1 deficiency) is established, and mechanistically it may be relevant to other conditions of impaired growth.

Monosomy X (Turner syndrome) is characterised by short stature, and the growth axis is connected to IGF-1 biology. However, Turner syndrome is typically not a state of GH/IGF-1 insensitivity, and it is usually managed with growth hormone. The high score (0.996) is therefore a computational prediction only, and the mechanistic link is weak.

Other conditions in the top 10 predictions have little or no biological rationale:
- **Growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant** (score 99.06%) is the closest mechanistic match, being a GH-insensitivity subtype (STAT5B-related). It is likely a subtype of the existing indication rather than a true repurposing candidate, and label coverage should be verified manually.
- Predictions such as Wolman disease, cholesteryl ester storage disease, Gaucher disease, esophageal varices (bleeding and non-bleeding, which appear to be duplicate entries), ichthyosis syndrome, varicose disease and congenital pulmonary lymphangiectasia show no identified mechanistic link and likely reflect network-level associations in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13116H | Increlex | Solution for injection 40 mg in 4 mL (10 mg per mL) | Not available in the data compiled for this report |

## Safety Considerations

**Drug Interactions:** 24 interactions were recorded, all rated Moderate. They involve glucose-lowering agents, which is consistent with the hypoglycaemia risk of mecasermin:
- **Sulfonylureas:** chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide
- **Meglitinide:** nateglinide
- **Insulins:** human (regular, isophane, zinc, zinc extended, inhaled rapid-acting), aspart (including protamine), degludec, detemir, glargine, glulisine, lispro (including protamine)

Only 20 of the 24 interactions were listed in the data compiled for this report.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. Known concerns for mecasermin, noted in the rationale for varicose disease, include hypoglycaemia, intracranial hypertension and tissue proliferation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature. The mechanistic link is weak, because Turner syndrome is not usually a GH/IGF-1 insensitivity state and is already managed with growth hormone. The safety profile (hypoglycaemia, intracranial hypertension, tissue proliferation) also calls for evidence before any new use.

**To proceed, the following is needed:**
- Mechanism of action data for mecasermin
- The TGA Product Information, including approved indication, warnings and contraindications
- A systematic literature and trial registry search (including ANZCTR) for mecasermin in Turner syndrome
- Manual review of the STAT5B-related GH insensitivity subtype to check whether it already falls within the approved indication
- Clinical input on whether IGF-1 therapy has any role alongside standard growth hormone treatment in Turner syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

