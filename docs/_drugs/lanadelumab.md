---
layout: default
title: Lanadelumab
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Lanadelumab"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
description: "Lanadelumab: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). In Australia: 1 PBS item (1 currently listed)"
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lanadelumab: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Lanadelumab is a monoclonal antibody that inhibits plasma kallikrein and is marketed in Australia as Takhzyro.
The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, with a score of **0.9999**.
There are **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lanadelumab: "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), label version 2026-09-18; accessed 2026-11-19.) From the drug's target record, lanadelumab is an antibody directed against plasma kallikrein (gene KLKB1), so it acts on the kallikrein-bradykinin pathway.

The high model score most likely reflects network proximity to serpin biology, since the C1 inhibitor is itself a serpin. However, serpinopathies with toxic polymerization arise from intracellular accumulation of misfolded serpin protein, not from excess kallikrein activity. Inhibiting plasma kallikrein is therefore unlikely to address the underlying pathology. The link is speculative and should be treated as a model-generated hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12790E | Takhzyro | Injection 300 mg in 2 mL single use pre-filled syringe | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: One pharmacological entry is recorded, which is the drug's own target (kallikrein B1, KLKB1). It is not a drug-drug interaction with a co-administered medicine.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5), and the biology of toxic serpin polymerization does not point to a role for plasma kallikrein inhibition.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that plasma kallikrein inhibition affects this condition
- Detailed mechanism of action data
- Review of the TGA-approved Product Information for warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

