---
layout: default
title: Inclisiran
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-17
description: "Inclisiran: predicted new indication Potassium deficiency disease (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
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

## Inclisiran: From Lipid-Lowering Therapy to Potassium Deficiency Disease
{: .text-alpha }

## One-Sentence Summary

Inclisiran (Leqvio) is a small interfering RNA (siRNA) medicine that lowers LDL cholesterol by silencing PCSK9, and it is marketed in Australia.
The TxGNN model predicts it may be effective for **potassium deficiency disease**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG entry carries no indication text) |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for inclisiran: "Inclisiran is a double-stranded small interfering ribonucleic acid (siRNA), conjugated on the sense strand with triantennary N-Acetylgalactosamine (GalNAc) to facilitate uptake by hepatocytes. In hepatocytes, inclisiran utilizes the RNA interference mechanism and directs catalytic breakdown of mRNA for PCSK9." ([DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44), label version 2026-08-19; accessed 2026-11-19.) From general pharmacology, inclisiran is an siRNA that targets PCSK9 mRNA in hepatocytes, which raises LDL receptor recycling and lowers LDL-C.

The review found no plausible mechanistic link between PCSK9 silencing and potassium homeostasis. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it should not be read as evidence of efficacy.

Other top-ranked predictions are similarly unsupported: esophageal disease, atypical coarctation of aorta, migraine disorder (and related subtypes), esophageal ulcer and Raynaud disease all have no trials or literature. Aortic malformation was linked to two inclisiran trials, but these appear to be a mapping artefact (see below).

## Clinical Trial Evidence

Currently no related clinical trials are registered for potassium deficiency disease.

For context, the two trials below were linked to the lower-ranked prediction "aortic malformation". Both were graded as not relevant to that condition, because they are paediatric familial hypercholesterolaemia studies and do not test efficacy in the predicted indication.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 60 | Inclisiran vs placebo, then open-label, in children aged 6 to <12 years with heterozygous familial hypercholesterolaemia |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Inclisiran vs placebo, then open-label, in children aged 2 to <12 years with homozygous familial hypercholesterolaemia |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14087K | Leqvio | Injection 284 mg in 1.5 mL single-use pre-filled syringe | Not stated in the data compiled |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no supporting trials or literature and no plausible mechanistic link between PCSK9 silencing and potassium deficiency. The safety and original-indication data for the Australian product are also incomplete.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a defensible mechanistic hypothesis for potassium deficiency
- The TGA-approved Product Information, to confirm the approved indication, warnings and contraindications
- Any preclinical or clinical evidence in potassium disorders; none was found
- Verification of the trial-to-condition mapping for aortic malformation, if that prediction is to be pursued

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

