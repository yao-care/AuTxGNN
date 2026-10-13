---
layout: default
title: Corifollitropin Alfa
parent: Model Prediction Only (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Corifollitropin Alfa
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

# Corifollitropin alfa: From Controlled Ovarian Stimulation to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa is a long-acting recombinant follicle-stimulating hormone (FSH) agonist, used in controlled ovarian stimulation for assisted reproduction.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but this is a computational prediction only.
There are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Controlled ovarian stimulation (the ARTG indication text was not available in the data compiled for this report; this is based on the drug's known pharmacology) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, corifollitropin alfa is a recombinant FSH-beta chain fused with the C-terminal peptide of hCG, which acts as an FSH receptor agonist with a prolonged duration of action.

No plausible mechanistic link between FSH receptor stimulation and gastroduodenal inflammation has been identified. The high TxGNN score is a graph-based prediction and likely reflects network artefacts rather than biology. The same applies to the other top predictions:

- **Upper gastrointestinal conditions** (peptic ulcer disease, peptic oesophagitis): no known connection to FSH signalling, and likely clustering with other GI indications in the knowledge graph.
- **Migraine-related conditions** (migraine disorder, migraine with brainstem aura, migraine susceptibility): hormonal fluctuations are known migraine modulators, but ovarian stimulation raises oestradiol and could plausibly worsen rather than treat migraine. These predictions come from one disease cluster and are not independent evidence.
- **Vascular and cardiopulmonary conditions** (Raynaud disease, pulmonary hypertension, kyphoscoliotic heart disease): no established vascular benefit, and the thrombotic and fluid-shift risks of ovarian stimulation argue for caution.
- **Atrophoderma vermiculata**: no mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5816D | Elonva | Solution for injection 100 micrograms in 0.5 mL single dose pre-filled syringe | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

Points from the data compiled for this report:
- No drug interaction records were found.
- No contraindication edges were found in the knowledge graph.
- Ovarian stimulation carries known risks (for example, ovarian hyperstimulation syndrome with fluid shifts and thromboembolic risk), which are relevant when considering any use in vascular or cardiopulmonary conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are supported only by model scores, with no clinical trials or literature, and no plausible mechanistic link. Several (migraine, Raynaud disease, pulmonary hypertension) raise potential safety concerns rather than therapeutic promise.

**To proceed, the following is needed:**
- Product Information warnings and contraindications from the TGA/PBS source (currently a blocking data gap)
- Mechanism of action data from DrugBank
- The approved indication text for ARTG 5816D
- Any mechanistic, preclinical or clinical evidence linking FSH receptor agonism to the predicted conditions
- Route and formulation compatibility assessment (the product is injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

