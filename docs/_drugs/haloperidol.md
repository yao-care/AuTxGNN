---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Haloperidol"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
description: "Haloperidol: predicted new indication Congenital disorder of glycosylation with defective fucosylation (evidence level L5). In Australia: 9 PBS items (9 currently listed)"
---

# Haloperidol
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

## Haloperidol: Congenital disorder of glycosylation with defective fucosylation
{: .text-alpha }

## One-Sentence Summary

Haloperidol is an antipsychotic originally used for psychotic disorders, including schizophrenia, schizoaffective disorder and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**.
This prediction has **no clinical trials** and **no publications** supporting it, and it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (9 of 9 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for haloperidol: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), label version 2026-11-03; accessed 2026-11-19.) Haloperidol is generally understood to be a dopamine D2 receptor antagonist and a typical antipsychotic. Its efficacy in psychotic disorders is well established.

No mechanistic link to this predicted indication could be identified. Nothing connects dopamine antagonism to fucosylation pathways or to the biology of this glycosylation disorder. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical evidence. This prediction should be treated as a computational hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 2761H | Serenace | Haloperidol | Tablet 500 micrograms | Valid |
| 2763K | Serenace | Haloperidol | Oral solution 2 mg per mL, 100 mL | Valid |
| 2765M | Haldol decanoate | haloperidol decanoate | I.M. injection equivalent to 50 mg haloperidol in 1 mL ampoule | Valid |
| 2766N | Haldol decanoate | haloperidol decanoate | I.M. injection equivalent to 150 mg haloperidol in 3 mL ampoule | Valid |
| 2767P | Serenace | Haloperidol | Tablet 1.5 mg | Valid |
| 2768Q | HALOPERIDOL MEDSURGE | Haloperidol | Injection 5 mg in 1 mL | Valid |
| 2770T | Serenace | Haloperidol | Tablet 5 mg | Valid |
| 3456X | HALOPERIDOL MEDSURGE | Haloperidol | Injection 5 mg in 1 mL | Valid |
| 12519X | HALOPERIDOL MEDSURGE | Haloperidol | Injection 5 mg in 1 mL | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

Injectable forms (including a depot decanoate injection), oral tablets and an oral solution are listed. Please confirm the approved indications in the TGA Product Information.

<!-- review:begin au-lic-20261124b-haloperidol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Only an injectable form is registered." Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261124b-haloperidol-1 -->

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease associations from the TxGNN knowledge graph, not product label text):
  - Cardiac: long QT syndrome (including familial), torsades de pointes.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, neuroleptic malignant syndrome.
  - Haematological: neutropenia (including congenital forms), agranulocytosis, leukopenia.
  - Endocrine and metabolic: hypothyroidism, myxedema, potassium deficiency.
  - Other: liver disease, gallbladder disease, hypotensive disorder, female breast carcinoma.
- **Drug Interactions:** The interaction screen returned 100 interactions. The major-level ones among the first 20 listed are:
  - bupropion
  - morphine
  - clarithromycin
  - dolasetron

  Many moderate-level interactions were also listed, including famotidine, epinephrine, hydrocortisone, amphotericin B, atropine and loperamide.

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature and no plausible mechanistic link. The knowledge graph also flags many safety concerns, including QT prolongation and neutropenia.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking haloperidol to fucosylation defects, supported by preclinical data
- Mechanism of action data for haloperidol
- Product Information warnings and contraindications for the Australian ARTG entry
- A safety assessment for a likely paediatric or rare-disease population

It has completed Phase 3 trials, including a haloperidol-controlled olanzapine trial (NCT00129220, n=224), and network meta-analyses of acute mania treatments. That use is close to existing clinical practice for haloperidol, so it is not true repurposing. It would warrant a separate evaluation, with monitoring for extrapyramidal symptoms, QTc prolongation and drug interactions.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data for this drug is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |
| 2026-11-24 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

