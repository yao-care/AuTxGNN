---
layout: default
title: Buprenorphine
parent: Model Prediction Only (L5)
nav_order: 115
evidence_level: L5
indication_count: 6
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
last_modified_at: 2026-11-24
description: "Buprenorphine: predicted new indication acute intermittent porphyria (evidence level L5). In Australia: at least 20 PBS items"
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Buprenorphine: opioid partial agonist → acute intermittent porphyria
{: .text-alpha }

## One-Sentence Summary

Buprenorphine is an opioid medicine marketed in Australia as a transdermal patch (Norspan). The TxGNN model predicts it may be relevant to **acute intermittent porphyria**, but the data compiled for this report contain **no clinical trials** and only **1 publication**, a case report on anaesthetic management that does not show therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acute intermittent porphyria |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (at least 20 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for buprenorphine: "SUBLOCADE Injection contains buprenorphine. Buprenorphine is a partial agonist at the mu- opioid receptor and an antagonist at the kappa-opioid receptor." ([DailyMed: Sublocade (buprenorphine) prescribing information, Indivior Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6189fb21-9432-45f8-8481-0bfaf3ccde95), label version 2026-07-27; accessed 2026-11-19.) Buprenorphine is an opioid, and from its known drug class it acts as a partial agonist at the mu-opioid receptor. No established mechanistic link to acute intermittent porphyria has been identified.

The only publication retrieved describes the anaesthetic management of a patient who already had acute intermittent porphyria. It concerns perioperative drug safety, not treatment benefit. The high TxGNN score is therefore not supported by clinical or mechanistic evidence, and it should be treated as a model-generated hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Japanese Journal of Anesthesiology) | Anaesthetic management of a woman with suspected acute intermittent porphyria undergoing gynaecological cancer surgery; addresses perioperative safety, not efficacy |

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 10746N | Norspan | Buprenorphine | Transdermal patch 40 mg | Valid |
| 10755C | Norspan | Buprenorphine | Transdermal patch 30 mg | Valid |
| 10756D | Norspan | Buprenorphine | Transdermal patch 25 mg | Valid |
| 10770W | Norspan | Buprenorphine | Transdermal patch 15 mg | Valid |
| 10948F | Bupredermal | Buprenorphine | Transdermal patch 10 mg | Valid |
| 10949G | Norspan | Buprenorphine | Transdermal patch 30 mg | Valid |
| 10953L | Norspan | Buprenorphine | Transdermal patch 15 mg | Valid |
| 10957Q | Bupredermal | Buprenorphine | Transdermal patch 5 mg | Valid |
| 10959T | Norspan | Buprenorphine | Transdermal patch 40 mg | Valid |
| 10964C | Norspan | Buprenorphine | Transdermal patch 25 mg | Valid |
| 10970J | Bupredermal | Buprenorphine | Transdermal patch 20 mg | Valid |
| 13296T | Buvidal Weekly | Buprenorphine | Injection (modified release) 24 mg in 0.48 mL pre-filled syringe | Valid |
| 13297W | Buvidal Weekly | Buprenorphine | Injection (modified release) 16 mg in 0.32 mL pre-filled syringe | Valid |
| 13298X | Buvidal Monthly | Buprenorphine | Injection (modified release) 64 mg in 0.18 mL pre-filled syringe | Valid |
| 13302D | Buvidal Monthly | Buprenorphine | Injection (modified release) 128 mg in 0.36 mL pre-filled syringe | Valid |
| 13303E | Buvidal Monthly | Buprenorphine | Injection (modified release) 160 mg in 0.45 mL pre-filled syringe | Valid |
| 13309L | Buvidal Monthly | Buprenorphine | Injection (modified release) 96 mg in 0.27 mL pre-filled syringe | Valid |
| 13310M | Subutex | Buprenorphine | Tablet (sublingual) 400 micrograms (as hydrochloride) | Valid |
| 13314R | Buvidal Weekly | Buprenorphine | Injection (modified release) 32 mg in 0.64 mL pre-filled syringe | Valid |
| 13320C | Sublocade | Buprenorphine | Injection (modified release) 100 mg in 0.5 mL pre-filled syringe | Valid |

The table shows 20 of 29 PBS items for this ingredient in these data (items on the current PBS Schedule first).

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Major-level interactions in the listed entries include alvimopan, bupropion, morphine, cisapride and dolasetron. Moderate-level interactions include famotidine, hyoscyamine, loperamide, aprepitant, atropine, dexamethasone, clarithromycin and several anticholinergic or laxative agents.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trial or study evaluates buprenorphine as a treatment for acute intermittent porphyria, and the single publication addresses anaesthetic safety only.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic link to porphyria pathophysiology
- Any preclinical or clinical study directly testing buprenorphine in acute intermittent porphyria
- Review of the safety of buprenorphine in porphyria, based on the TGA Product Information
- Full Product Information warnings and contraindications for Norspan

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sublocade (buprenorphine) prescribing information, Indivior Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6189fb21-9432-45f8-8481-0bfaf3ccde95) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

