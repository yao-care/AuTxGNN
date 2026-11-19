---
layout: default
title: Benzatropine
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 2
monitor_inn: "Benzatropine"
predicted_indications: ["PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder"]
last_modified_at: 2026-11-20
description: "Benzatropine: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). In Australia: 4 PBS items (4 currently listed)"
---

# Benzatropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Benzatropine: anticholinergic (muscarinic receptor antagonist) → PLA2G6-associated neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Benzatropine is an anticholinergic medicine used for parkinsonism and related movement disorders. The TxGNN model predicts it may be relevant to **PLA2G6-associated neurodegeneration**, but **no clinical trials and no publications** were found to support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9917 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (4 of 4 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for benzatropine: "Benztropine mesylate possesses both anticholinergic and antihistaminic effects, although only the former have been established as therapeutically significant in the management of parkinsonism. In the isolated guinea pig ileum, the anticholinergic activity of this drug is about equal to that of atropine; however, when administered orally to unanesthetized cats, it is only about half as active as atropine." ([DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6), label version 2026-11-11; accessed 2026-11-19.) Based on general pharmacology, benzatropine is an anticholinergic that blocks muscarinic acetylcholine receptors and is also described as inhibiting dopamine reuptake.

PLA2G6-associated neurodegeneration can include dystonia-parkinsonism features (for example, juvenile-onset parkinsonism). A plausible, but unverified, link is that an anticholinergic could offer symptomatic relief of these movement features. This would not be disease modification, because the underlying defect lies in phospholipase A2 group VI function and lipid metabolism. This link is a hypothesis only and has not been tested in the data compiled here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11249C | Benzatropine Injection | Injection containing benzatropine mesilate 2 mg in 2 mL | Not recorded in the local data |

Four current single-ingredient PBS items are recorded: three injections and one oral tablet (Benztrop 2 mg).

<!-- review:begin au-lic-20261117-benzatropine-1 -->

> **Review correction (2026-11-17)**: Originally stated: "One licence is recorded and it is valid (single-ingredient product)." Corrected: the earlier wording counted only the PBS items originally collected for this page. The data now include the current PBS items for this ingredient (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-benzatropine-1 -->

---

## Safety Considerations

Specific warnings and contraindications from the approved label were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Drug Interactions**: 78 interacting drugs were identified. Major-level interactions include:
- Potassium chloride
- Potassium citrate

Moderate-level interactions include other anticholinergic or antimuscarinic agents (e.g. atropine, hyoscyamine, dicyclomine, glycopyrronium, propantheline, clidinium, mepenzolate, methscopolamine), opioids and related agents (morphine, loperamide, opium, eluxadoline), and others such as metoclopramide, dronabinol, nabilone and pramlintide.

**Conditions flagged for caution or contraindication in the compiled safety data** include:
- Eye: angle-closure and open-angle glaucoma
- Gastrointestinal: paralytic ileus, achalasia, megaesophagus, ulcerative colitis, inflammatory bowel disease, Clostridium difficile colitis, necrotizing enterocolitis, gastric ulcer, hiatus hernia
- Genitourinary: benign prostatic hyperplasia, pyoureter
- Neuromuscular: myasthenia gravis, neuromuscular junction disease
- Cardiovascular: coronary artery disease, heart conduction disease, sudden cardiac arrest, hypertension, hypotension
- Other: chronic obstructive pulmonary disease, kidney disease, liver disease, gallbladder disease

These are not drawn from label text and should be checked against the PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for PLA2G6-associated neurodegeneration is supported only by a computational score (0.9917), with no clinical trials or publications directly studying this disease. Any benefit would likely be symptomatic at best, and anticholinergic adverse effects need careful weighing in a neurodegenerative population.

**To proceed, the following is needed:**
- Literature review and trial search focused on PLA2G6-associated neurodegeneration and anticholinergic treatment of its dystonia-parkinsonism features
- Detailed mechanism of action data for benzatropine
- Review of the TGA Product Information for warnings, contraindications and approved indications
- A safety assessment covering anticholinergic burden, cognitive effects and the interaction profile in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: PBS item count updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

