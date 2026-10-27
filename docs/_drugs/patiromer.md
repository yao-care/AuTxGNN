---
layout: default
title: Patiromer
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Patiromer: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA a… (evidence level L5). Approved use: Not stated in the data compiled for this report (patirome…"
monitor_inn: "Patiromer"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "exocrine pancreatic insufficiency", "colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "cecal disease", "lipoma of colon", "severe nonproliferative diabetic retinopathy", "colonic lymphangioma"]
---

# Patiromer
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

## Patiromer: From Hyperkalaemia (Presumed) to Mitochondrial Oxidative Phosphorylation Disorder
{: .text-alpha }

## One-Sentence Summary

Patiromer is a non-absorbed, potassium-binding polymer. The indication text for its Australian listing was not available in the data compiled for this report, but the drug is understood to be used for hyperkalaemia.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (patiromer is generally used to treat hyperkalaemia) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 98.72% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, patiromer is a non-absorbed polymer that exchanges calcium for potassium in the colon. It acts locally in the gut and is not systemically active.

Mitochondrial oxidative phosphorylation disorders arise from defects in nuclear-encoded respiratory chain components. A gut-restricted polymer cannot address these defects, so **no plausible mechanistic link was identified**. The high TxGNN score most likely reflects knowledge-graph artefacts rather than biological rationale.

The other top-ranked predictions show the same pattern. Most are colonic or caecal conditions (colonic neoplasm, caecal villous adenoma, colonic lipoma, colonic lymphangioma and others), which appear to reflect anatomical association with the colon. Exocrine pancreatic insufficiency and severe non-proliferative diabetic retinopathy were also predicted. The only speculative link, for retinopathy, is indirect: patiromer may allow continued RAAS inhibitor use, and any benefit would come from the RAAS inhibitor rather than from patiromer. None of these predictions has supporting trial or publication data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13609G | Veltassa | Powder for oral suspension 8.4 g | Not available in the compiled data |

## Safety Considerations

**Drug Interactions:** 48 potential interactions were identified (DDInter). The main ones are:

- **Major:** magnesium oxide, aluminium hydroxide, calcium carbonate
- **Moderate:** the proton pump inhibitors rabeprazole, omeprazole and dexlansoprazole; the corticosteroids hydrocortisone, dexamethasone, triamcinolone, beclomethasone and betamethasone; metformin; iron; attapulgite; and several calcium salts (phosphate, acetate, citrate, glubionate, gluconate, lactate)

Only 20 of the 48 interactions were available for review. Warnings and contraindications were not available in the compiled data. Please refer to the TGA-approved Product Information (PI) for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and the proposed mechanism is implausible for a non-absorbed, gut-restricted polymer. The same applies to all ten top-ranked predictions.

**To proceed, the following is needed:**
- Product Information (PI) review for the approved indication, warnings and contraindications
- Mechanism of action data
- A biologically plausible hypothesis linking patiromer to mitochondrial OXPHOS disorders, followed by preclinical evidence
- Evidence from any registered trial or published study in the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

