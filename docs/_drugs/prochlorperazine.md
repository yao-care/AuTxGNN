---
layout: default
title: Prochlorperazine
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Prochlorperazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "Prochlorperazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Prochlorperazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Prochlorperazine: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Prochlorperazine is a phenothiazine dopamine antagonist, recorded in the knowledge graph as indicated for schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Prochlorperazine is a phenothiazine that blocks dopamine D2 receptors, and this action underlies its use in schizophrenia.

No mechanistic link was identified between D2 antagonism and inherited retinal dystrophies. These conditions arise from genetic defects in retinal structure and function, and prochlorperazine has no known effect on those pathways. The very high TxGNN score (99.998%, model rank 73) reflects similarity patterns in the knowledge graph rather than biological or clinical evidence.

The prediction should therefore be treated as a hypothesis-generating signal only.

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
| ARTG 2369Q | Stemetil | Injection containing prochlorperazine mesilate 12.5 mg in 1 mL | Not stated in the data compiled |

Only an injectable form is registered. Route compatibility with the predicted indication has not been assessed.

---

## Safety Considerations

Product Information warnings and contraindications were not available for this report. Please refer to the TGA-approved Product Information (PI) for label safety information.

**Contraindication signals from the knowledge graph** (these are graph-derived associations, not label text):
- **Cardiovascular:** hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, long QT syndrome (including familial), torsades de pointes, coronary artery disease, myocardial infarction
- **Neurological:** epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm
- **Haematological:** thrombocytopenia, neutropenia, agranulocytosis
- **Hepatic, renal and gastrointestinal:** liver disease, kidney disease, gallbladder disease, gastric ulcer
- **Metabolic and other:** hyperglycaemia, obesity disorders, benign prostatic hyperplasia, female breast carcinoma, substance abuse/dependence

The interaction query returned 100 interactions, and 20 are listed in the data compiled. **Major** interactions:
- Bupropion
- Potassium citrate

**Moderate** interactions include:
- Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, chlorpropamide)
- Anticholinergics (atropine, hyoscyamine, glycopyrronium)
- Morphine
- Clarithromycin
- Epinephrine
- Famotidine
- Loperamide
- Lorcaserin
- Bisacodyl
- Picosulfuric acid

For an inherited retinal dystrophy population, the neurological adverse effects of phenothiazines (such as extrapyramidal symptoms) would also need careful consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, no plausible mechanism, and the drug has a substantial safety burden. The evidence level is L5.

**To proceed, the following is needed:**
- A biologically plausible mechanistic hypothesis linking D2 antagonism to retinal degeneration, supported by preclinical data
- Mechanism of action data and the TGA Product Information safety sections (warnings and contraindications)
- An assessment of route compatibility, since only an injectable is registered in Australia
- A comparison with other model predictions for this drug. For example, **manic bipolar affective disorder** is more biologically plausible (D2 antagonists are an established class for mania), though the supporting literature is old and weak and no trials are registered. It may be a more productive research question than the retinal prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

