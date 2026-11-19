---
layout: default
title: Cabotegravir
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Cabotegravir: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the data compiled for this report . Cabotegravir is kno…"
monitor_inn: "Cabotegravir"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
---

# Cabotegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor, marketed in Australia as an oral tablet (Vocabria) and as a long-acting injectable co-pack with rilpivirine (Cabenuva).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a computational prediction only, and the recommended decision is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the ARTG indication text is empty). Cabotegravir is known as an HIV-1 integrase inhibitor. |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (2 of 2 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for cabotegravir: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), label version 2025-04-11; accessed 2026-11-19.) Cabotegravir is known to be an HIV-1 integrase strand transfer inhibitor, which blocks viral DNA integration into the host genome.

No established mechanism links integrase inhibition to the pathophysiology of rheumatoid arthritis, which is driven by TNF, IL-6, JAK/STAT signalling and B- and T-cell activity. The high TxGNN score (0.9945; model rank 6338) reflects a TxGNN model (deep learning) prediction only. It is not backed by any clinical trial or publication, and it should be treated as a hypothesis-generating signal rather than a reasoned mechanistic proposal.

Other predicted indications, such as sclerosing cholangitis, bronchitis and several rare congenital syndromes, likewise have no supporting evidence or plausible mechanism. Several of these scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12939B | Vocabria | Tablet 30 mg | Not available in the compiled data |
| ARTG 12937X | Cabenuva | Pack containing 1 vial cabotegravir 600 mg in 3 mL and 1 vial rilpivirine 900 mg in 3 mL | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: Seven moderate-level interactions were identified, all with polyvalent cation-containing antacids and supplements: calcium carbonate, aluminium hydroxide, magnesium carbonate, magnesium hydroxide, magnesium oxide, sodium bicarbonate and sodium citrate. These interactions are relevant mainly to the oral formulation and should be checked against the Product Information for dosing separation.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score, with no clinical trials, no publications and no plausible mechanistic link between HIV integrase inhibition and rheumatoid arthritis. Evidence is at the lowest level (L5), and safety screening cannot proceed because label warnings and contraindications are missing.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a documented mechanistic hypothesis for rheumatoid arthritis
- Preclinical evidence (in vitro or animal models of inflammatory arthritis) to move beyond L5
- Approved indication text, warnings and contraindications from the TGA Product Information
- Route compatibility assessment (oral tablet versus long-acting intramuscular injection) for the proposed use
- A systematic literature and trial registry search (including ANZCTR) to confirm that no relevant studies exist

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

