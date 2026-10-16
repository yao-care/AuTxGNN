---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Haloperidol: predicted new indication Congenital disorder of glycosylation with defective fucosylation (evidence level L5). Approved use: Psychotic disorders, including schizophrenia…"
monitor_inn: "Haloperidol"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Haloperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Haloperidol: From Psychotic Disorders to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is an antipsychotic originally used for psychotic disorders, including schizophrenia, schizoaffective disorder and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**.
This prediction has **no clinical trials** and **no publications** supporting it, and it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorders, including schizophrenia, schizophreniform disorder, schizoaffective disorder and Tourette syndrome (taken from the knowledge graph, because the Australian record has no indication text) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the data compiled for this report. Haloperidol is generally understood to be a dopamine D2 receptor antagonist and a typical antipsychotic. Its efficacy in psychotic disorders is well established.

No mechanistic link to this predicted indication could be identified. Nothing connects dopamine antagonism to fucosylation pathways or to the biology of this glycosylation disorder. The very high TxGNN score reflects a pattern in the knowledge graph, not biological or clinical evidence. This prediction should be treated as a computational hypothesis only.

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
| ARTG 12519X | HALOPERIDOL MEDSURGE | Injection 5 mg in 1 mL | Not specified in the data compiled for this report |

Only an injectable form is registered. Please confirm the approved indications in the TGA Product Information.

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

**Note on other predictions:** In the same output, the lower-ranked prediction **manic bipolar affective disorder** (score 99.83%) has far stronger support. It has completed Phase 3 trials, including a haloperidol-controlled olanzapine trial (NCT00129220, n=224), and network meta-analyses of acute mania treatments. That use is close to existing clinical practice for haloperidol, so it is not true repurposing. It would warrant a separate evaluation, with monitoring for extrapyramidal symptoms, QTc prolongation and drug interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

