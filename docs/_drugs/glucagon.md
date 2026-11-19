---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 340
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "Glucagon"
predicted_indications: ["irritable bowel syndrome"]
description: "Glucagon: predicted new indication Irritable bowel syndrome (evidence level L5). In Australia: 3 PBS items (3 currently listed)"
---

# Glucagon
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

## Glucagon: Irritable bowel syndrome
{: .text-alpha }

## One-Sentence Summary

Glucagon is a peptide hormone used as an injectable in Australia. The TxGNN model predicts it may be relevant to **irritable bowel syndrome**, with a score of 0.9924. No study directly tests glucagon in this condition, so the evidence level is **L5**. The related trials and publications concern GLP-1 and GLP-1 receptor agonists, which are different drugs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (3 of 3 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for glucagon: "Glucagon increases blood glucose concentration by activating hepatic glucagon receptors, thereby stimulating glycogen breakdown and release of glucose from the liver. Hepatic stores of glycogen are necessary for glucagon to produce an antihypoglycemic effect." ([DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84), label version 2020-09-16; accessed 2026-11-19.) Glucagon and GLP-1 are both derived from proglucagon, and GLP-1 and its analogues inhibit antro-duodeno-jejunal motility. Glucagon itself is used clinically as a spasmolytic during gastrointestinal imaging and endoscopy.

Reduced gut motor activity is plausibly relevant to IBS, particularly diarrhoea-predominant and pain or spasm-related symptoms. It could also be a concern in constipation-predominant IBS. Most mechanistic and clinical data come from GLP-1 receptor agonists rather than glucagon, so the link to glucagon is indirect and remains a hypothesis.

## Clinical Trial Evidence

None of the trials below tests glucagon, so they support mechanism only.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue) and gastrointestinal motor function in women with constipation-predominant IBS. Enrolled the target population, but the drug is not glucagon. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 versus the analogue ROSE-010 on meal-related stomach, duodenal and jejunal motility in humans. Did not enrol IBS patients. |

## Literature Evidence

The publications below concern GLP-1 or GLP-1 receptor agonists, or IBS more broadly. None tests glucagon in IBS.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic review | Front Endocrinol | GLP-1 receptor agonists and IBS improvement; notes that GLP-1 and ROSE-010 reduce gut motility in IBS patients. |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic review | J Headache Pain | GLP-1 receptor agonists in headache and pain disorders; not specific to IBS. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescribing and discontinuation of GLP-1 receptor agonists among patients with IBS. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical study cross-analysis | Scand J Gastroenterol | Pain relief with ROSE-010 in IBS, by patient characteristics. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Role of GLP-1 and intestinal L-cells in IBS pathophysiology. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolised GLP-1 for diabetes and IBS. |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Review | J Clin Invest | Gut-brain interaction mechanisms, including incretin-based therapies. |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Brain-gut-microbiome axis. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1449G | GlucaGen Hypokit | Injection set containing glucagon hydrochloride 1 mg (1 I.U.) and 1 mL solvent in disposable syringe | Not available in the data compiled |

## Safety Considerations

- **Drug Interactions**: 25 interactions were identified in the interaction databases, and 20 are listed in the data compiled for this report. All listed are classed as Minor. They include warfarin and a range of beta-blockers (for example atenolol, metoprolol, propranolol, carvedilol, bisoprolol, labetalol, sotalol and timolol, including ophthalmic forms).

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests glucagon in irritable bowel syndrome. The supporting trials and publications involve GLP-1 and GLP-1 analogues, so the evidence level is L5 and the link to glucagon is indirect.

**To proceed, the following is needed:**
- Studies that test glucagon itself in IBS patients
- Mechanism of action data for glucagon
- Warnings and contraindications from the TGA-approved Product Information
- Clarification of effects in constipation-predominant versus diarrhoea-predominant IBS

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data for glucagon are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

