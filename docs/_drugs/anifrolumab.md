---
layout: default
title: Anifrolumab
parent: Model Prediction Only (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Anifrolumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Moderate to severe systemic lupus erythematosus (SLE)…"
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (Saphnelo) is an anti-type I interferon receptor (IFNAR1) antibody, first approved internationally for moderate to severe systemic lupus erythematosus (SLE) in patients receiving standard therapy.
The TxGNN model predicts it may be effective for **diabetic cataract**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly supporting this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe systemic lupus erythematosus (SLE), per international approval information. The Australian indication text was not available in the data compiled for this report. |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, anifrolumab is a monoclonal antibody that targets the type I interferon receptor subunit 1 (IFNAR1). It blocks signalling by all type I interferons, and this underlies its use in SLE.

No mechanistic link between type I interferon signalling and diabetic cataract is supported by the available data. Diabetic cataract is mainly driven by polyol-pathway activity and oxidative stress in the lens, which are not obviously related to the IFNAR pathway. The high TxGNN score most likely reflects the knowledge-graph neighbourhood shared by cataract-related conditions rather than biological evidence for anifrolumab.

The other top-ranked predictions are mostly cataract subtypes (craniostenosis, mature, tetanic, type 2 diabetes-associated, immature, cortical, nuclear senile and senile cataract), plus diabetic retinopathy. None has trial or mechanistic support in the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered for diabetic cataract.

## Literature Evidence

Currently no related literature available for diabetic cataract.

For context, one review was linked to a lower-ranked prediction (cortical cataract). It is not evidence for the lead prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/) | 2025 | Review | Int J Mol Sci | Ophthalmological safety considerations of emerging and conventional SLE therapies. It addresses ocular adverse effects of treatment, not efficacy against cataract. Cataract in SLE is often related to glucocorticoid exposure. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14189T | Saphnelo | Solution concentrate for I.V. infusion, 300 mg in 2 mL | Not available in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry. It identifies the drug's target (IFNAR1) rather than a clinical drug-drug interaction.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for diabetic cataract rests on a model score alone (L5). There are no registered trials, no supporting literature and no plausible mechanistic link. Warning and contraindication data are also unavailable.

**To proceed, the following is needed:**
- Detailed mechanism of action data (for example, from DrugBank)
- A documented biological rationale linking type I interferon signalling to lens or diabetic eye pathology
- The TGA Product Information, including the approved indication, warnings and contraindications
- Preclinical or observational evidence in lens or diabetic eye models
- Review of the ocular safety profile of anifrolumab in SLE
- A route-of-administration assessment, since the only Australian product is an intravenous infusion and the route required for an ocular indication has not been assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

