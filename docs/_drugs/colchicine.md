---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 2
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-30
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Not recorded in the local data"
---

# Colchicine
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

## Colchicine: Microtubule-disrupting agent (tubulin binder) → Plasmodium falciparum malaria
{: .text-alpha }

## One-Sentence Summary

Colchicine is a tubulin-binding, microtubule-disrupting agent registered in Australia as an oral tablet.
The TxGNN model predicts it may be relevant for **Plasmodium falciparum malaria**, but there are **0 clinical trials** and **2 publications**, and neither studies colchicine against this disease. Evidence for this prediction is limited to the model output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, colchicine binds tubulin and disrupts microtubules.

Microtubules are essential to the parasite's cell division, so a link to *P. falciparum* is biologically plausible. The two retrieved papers are indirect. One is a laboratory study of curcumin (not colchicine) that disrupts microtubules in *P. falciparum*. The other examines expression of the parasite's pfmdr1 gene in mammalian cells and its effect on chloroquine susceptibility. Neither tests colchicine as an antimalarial in people.

This is a plausible but unproven link. Colchicine also has a narrow therapeutic index and many drug interactions, which are a concern for any anti-infective use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro study | PloS one | Curcumin (not colchicine) disrupted microtubules in *P. falciparum* cells |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / cell-based study | Molecular and cellular biology | Expressing the parasite pfmdr1 gene in mammalian cells increased chloroquine susceptibility |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 3410L | Colcine | Tablet 500 micrograms | Not recorded in the local data |

---

## Safety Considerations

- **Drug Interactions**: The interaction query found 100 interacting drugs in total. Examples rated Major include aprepitant, clarithromycin, cobicistat, deferiprone, eliglustat, rolapitant, rosuvastatin and simvastatin. Examples rated Moderate include chloroquine, cimetidine, metronidazole, miconazole, ticagrelor and disulfiram. Chloroquine is relevant here because it is a standard antimalarial.

For warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No study directly examines colchicine in *P. falciparum* malaria, and the safety margin is narrow, so there is no basis to proceed.

**To proceed, the following is needed:**
- Laboratory data showing colchicine activity against *P. falciparum* at concentrations achievable in humans
- Detailed mechanism of action data
- Review of the TGA Product Information for warnings and contraindications
- A drug interaction assessment against standard antimalarials, particularly chloroquine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

