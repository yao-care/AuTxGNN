---
layout: default
title: Elafibranor
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Elafibranor"
predicted_indications: ["amenorrhea (disease)"]
description: "Elafibranor: predicted new indication Amenorrhea (disease) (evidence level L5). In Australia: 3 PBS items (3 currently listed)"
---

# Elafibranor
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

## Elafibranor: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Elafibranor (Iqirvo) is a dual PPAR-alpha/delta agonist, developed for non-alcoholic steatohepatitis (NASH) and later repositioned as a treatment for primary biliary cholangitis (PBC), the indication on which it was approved by the FDA and EMA in 2024. The TxGNN model predicts it may be effective for **amenorrhoea**, with a very high score of 0.9986. Currently there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Elafibranor is a dual agonist of PPAR-alpha and PPAR-delta (PPARA and PPARD). Its active metabolite, GFT-1007, is formed in the liver. Preclinical work showed reduced hepatic fat accumulation, inflammation and fibrosis. The pharmacology above comes from target-ligand records only. According to the Mechanism of Action section of the US FDA-approved prescribing information for elafibranor: "Elafibranor and its main active metabolite GFT1007 are peroxisome proliferator-activated receptor (PPAR) agonists, both of which activate PPAR-alpha, PPAR-gamma, and PPAR-delta in vitro. However, the mechanism by which elafibranor exerts its therapeutic effects in patients with PBC is not well understood." ([DailyMed: Iqirvo (elafibranor) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d78aa14f-6ec1-4b1d-a4ae-e48658137a25), label version 2026-08-11; accessed 2026-11-20.)

No direct mechanistic link between elafibranor and amenorrhoea has been established. PPAR signalling has been studied in ovarian and metabolic function, but any link to amenorrhoea is speculative. The very high TxGNN score is a computational prediction and is not supported by trials or literature. The relationship between the original indication (a cholestatic liver disease) and amenorrhoea has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 15084X | Iqirvo | Elafibranor | Tablet 80 mg | Valid |
| 15089E | Iqirvo | Elafibranor | Tablet 80 mg | Valid |
| 15107D | Iqirvo | Elafibranor | Tablet 80 mg | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: No drug-drug interactions were identified. The two records returned only describe the drug's pharmacological targets, PPAR-alpha and PPAR-beta/delta.
- **Pharmacological note**: PPAR-delta activation has context-dependent, sometimes pro-tumorigenic, effects reported in the literature. This warrants caution if oncology uses were ever explored.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for amenorrhoea has a high model score but no clinical trials, no literature and no plausible established mechanism, so evidence is at the lowest level (L5). It is not appropriate to progress at this stage.

**To proceed, the following is needed:**
- Retrieval of the TGA/ARTG Product Information, including approved indication, warnings and contraindications
- Detailed mechanism of action data, and a literature review of PPAR-alpha/delta signalling in reproductive endocrine function
- Preclinical or observational evidence linking elafibranor to amenorrhoea (or the underlying causes)
- A review of the safety implications in women of reproductive age, including pregnancy and hormonal effects
- Assessment of the other ranked predictions, noting that the PPAR-delta link to tumour biology needs particular caution

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism of action data are not otherwise available in the data compiled for this report, so the pharmacology above comes from target-ligand records only" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Iqirvo (elafibranor) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d78aa14f-6ec1-4b1d-a4ae-e48658137a25) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

