---
layout: default
title: Insulin Detemir
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Insulin detemir"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Detemir: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Insulin Detemir
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

## Insulin Detemir: Autoimmune oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin detemir is a long-acting basal insulin analogue, originally used to treat diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, insulin detemir is a soluble, long-acting human insulin analogue. A 14-carbon fatty acid (myristic acid) is attached to lysine at B29, and threonine at B30 is removed. This allows it to bind reversibly to albumin after subcutaneous injection, giving slow absorption and a prolonged, relatively predictable effect of up to 24 hours. It acts through the insulin receptor to replace deficient endogenous insulin.

Type 1 diabetes is defined by absolute insulin deficiency, so basal insulin replacement is the cornerstone of treatment. The original indication (diabetes mellitus) already includes type 1 diabetes. The high TxGNN score therefore reflects consistency with established clinical practice, not a new therapeutic direction.

## Clinical Trial Evidence

The data include 40 registered trials. The 10 most relevant are listed below. Phase 3 RCTs form the core of the direct evidence, and the large observational studies provide supportive real-world data. I could not find any ANZCTR identifiers in the data compiled for this report.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Detemir + aspart vs NPH + aspart in adults with type 1 diabetes; blood glucose control, efficacy and safety |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | Completed | 330 | 12-month double-blind safety and efficacy comparison of detemir from two manufacturing processes (basal-bolus with aspart) |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Detemir vs NPH insulin (both with aspart) in children and adolescents with type 1 diabetes |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Phase 3 | Completed | 71 | 32-week efficacy and safety comparison of detemir vs Semilente MC in children, adolescents and young adults |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | Completed | 520 | Detemir once vs twice daily in a basal-bolus regimen with aspart |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Phase 3 | Completed | 548 | Insulin degludec/aspart (IDegAsp) vs detemir + aspart in type 1 diabetes (BOOST: T1) |
| [NCT01440439](https://clinicaltrials.gov/study/NCT01440439) | Phase 4 | Unknown | 30 | Detemir vs glargine: glycaemic control and metabolism during exercise |
| [NCT00564018](https://clinicaltrials.gov/study/NCT00564018) | N/A | Terminated | 33 | Detemir, glargine and NPH compared on honeymoon-phase duration in newly diagnosed children (underpowered) |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | Completed | 4,464 | Observational study of safety, glycaemic control and weight with detemir in type 1 or type 2 diabetes |
| [NCT00655044](https://clinicaltrials.gov/study/NCT00655044) | N/A | Completed | 3,637 | Observational safety study of serious adverse drug reactions in routine care |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: insulin degludec vs detemir (both with aspart) in pregnant women with type 1 diabetes (non-inferiority) |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane systematic review | Cochrane Database Syst Rev | (Ultra-)long-acting insulin analogues in type 1 diabetes; benefit for complications and hypoglycaemia assessed |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic review | Drugs Today (Barc) | Insulin analogues, including detemir, for children and adolescents with type 1 diabetes |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Meta-analysis | Pol Arch Med Wewn | Detemir vs NPH insulin in type 1 diabetes |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network meta-analysis | Value Health | Relative efficacy and safety of basal insulin regimens in adults with type 1 diabetes |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Detemir has a less variable pharmacokinetic profile than NPH or ultralente and may lower hypoglycaemia risk, especially nocturnal |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Detemir has a more predictable, consistent effect than NPH, with less intrapatient variability |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Update on detemir as a basal analogue in type 1 and type 2 diabetes |
| [17881328](https://pubmed.ncbi.nlm.nih.gov/17881328/) | 2007 | Pharmacology review | Endocrinol Metab Clin North Am | Molecular properties and pharmacodynamics of detemir |
| [17881330](https://pubmed.ncbi.nlm.nih.gov/17881330/) | 2007 | Review | Endocrinol Metab Clin North Am | Weight data with detemir across trials and observational studies |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12236B | Levemir FlexPen | Injection (human analogue), cartridges, 100 units per mL, 3 mL | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the data compiled for this report. The main ones are listed below, and most are rated Moderate.
  - Other glucose-lowering drugs (metformin, pioglitazone, alogliptin, albiglutide): additive glucose-lowering effect.
  - Sympathomimetics and beta-agonists (epinephrine, salbutamol, formoterol, phenylephrine, pseudoephedrine): may alter glycaemic control.
  - Beta-blocker (acebutolol): may mask hypoglycaemia symptoms.
  - Corticosteroids (systemic hydrocortisone is Moderate; topical hydrocortisone and alclometasone are Minor).
  - Others: acetazolamide, hydrochlorothiazide, ethinylestradiol, estradiol, doxycycline, ethanol, alpelisib.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and several systematic reviews support insulin detemir in type 1 diabetes, and the product is already marketed in Australia. This is an established use rather than a true repurposing, so the guardrails relate to documentation and safety rather than efficacy.

**To proceed, the following is needed:**
- Review of the TGA-approved PI for warnings and contraindications, which are missing from the data compiled for this report
- Confirmation of the approved indication wording for the ARTG entry
- Detailed mechanism of action data
- A hypoglycaemia monitoring plan, and review of the interactions above in patients on multiple medicines

**Other predicted indications:** The remaining nine predictions have no supporting trials or publications and are rated Hold, except pancreatic agenesis.
- Pancreatic agenesis (L4, research question): insulin replacement is mechanistically plausible but dosing in neonates needs separate evaluation.
- The others (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome, drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy) are likely network artefacts or would treat only comorbid diabetes. For the lipodystrophy and lipoatrophy conditions, repeated insulin injection at the same site could worsen the condition.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

