---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans", "primary immunodeficiency due to a genetic defect in innate immunity", "sitosterolemia", "Smouldering systemic mastocytosis", "systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia", "hemoglobin H disease", "blepharo-cheilo-odontic syndrome"]
---

# Colchicine
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

## Colchicine: From Gout to Plasmodium falciparum Malaria
{: .text-alpha }

## One-Sentence Summary

Colchicine is an anti-inflammatory, microtubule-disrupting drug originally used for gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but there are **0 registered clinical trials** and only **2 indirect laboratory publications** supporting this direction.
This is a model-only prediction with no human efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (the Australian ARTG entry has no indication text recorded) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Colchicine is well known to bind tubulin and disrupt microtubules. This suppresses neutrophil activity and inflammasome-mediated inflammation, which underlies its use in gout and FMF.

The link to malaria is plausible but indirect. Microtubules are essential for the *P. falciparum* parasite, and the retrieved literature includes a study showing that curcumin disrupts parasite microtubules. That study did not involve colchicine. A second paper shows that expression of the parasite transporter gene *pfmdr1* in mammalian cells alters drug susceptibility. That work concerned chloroquine and is likewise an in vitro study.

No human antimalarial efficacy data for colchicine were found. Its narrow therapeutic index and extensive drug interactions are further concerns for an anti-infective use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro study | PLoS One | Curcumin (not colchicine) disrupts microtubules in *P. falciparum*, suggesting parasite microtubules are a drug target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / cell-based study | Mol Cell Biol | Expression of the parasite *pfmdr1* gene in mammalian cells altered drug susceptibility (chloroquine); the link to colchicine is indirect |

Neither paper tests colchicine as an antimalarial in humans.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 3410L | Colcine | Tablet 500 micrograms (oral) | Not recorded in the data compiled for this report |

---

## Cytotoxicity

Colchicine is not classed as an antineoplastic drug, so this section does not apply.

---

## Safety Considerations

Formal label warnings and contraindications were not available. Please refer to the TGA-approved Product Information (PI) for these.

- **Conditions flagged in the knowledge graph as contraindication-related** (these come from a knowledge graph, not label text, so confirm against the PI): liver failure, impaired renal function, haematological disease (including thrombocytopenia, leukopenia, agranulocytosis, neutropenia and aplastic anaemia), peptic ulcer disease, diarrhoeal disease, and muscle disorders (myopathy, rhabdomyolysis).
- **Drug Interactions:** The interaction screen identified 100 interacting drugs in total. Among those listed, the **Major** interactions are:
  - Aprepitant
  - Clarithromycin
  - Cobicistat
  - Deferiprone
  - Eliglustat
  - Rolapitant
  - Rosuvastatin
  - Simvastatin

  **Moderate** interactions include chloroquine, cimetidine, metronidazole, miconazole, tinidazole, ticagrelor, deferasirox, disulfiram, benznidazole, eluxadoline, fostamatinib and strontium-89 chloride.

  The interaction with chloroquine is relevant for any malaria context, since chloroquine is an antimalarial.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). The supporting papers are indirect in vitro studies, and none tests colchicine in malaria. Colchicine's narrow therapeutic index and extensive interaction profile add concern for an anti-infective use.

**To proceed, the following is needed:**
- In vitro and in vivo data on colchicine activity against *P. falciparum*, including its effect on parasite microtubules
- Detailed mechanism of action data, and a comparison with existing antimalarials
- The TGA Product Information (warnings, contraindications, indication text)
- An assessment of safety at doses and durations relevant to malaria, including interactions with standard antimalarials such as chloroquine

**Other predictions in this analysis:**
- **FMF, autosomal dominant:** Colchicine is already first-line therapy for FMF and FMF is among its original indications, so this is not a true repurposing candidate. The supplied literature is review-level (L4) and does not address the autosomal dominant subtype specifically.
- **Systemic mastocytosis:** Only a plausible indirect mechanism (microtubule-dependent mast cell degranulation) and one observational FMF paper exist (L4). No trials were found.
- **Dermatofibrosarcoma protuberans, primary immunodeficiency (innate immunity defect), sitosterolemia, smouldering systemic mastocytosis, lymphoadenopathic mastocytosis with eosinophilia, haemoglobin H disease and blepharo-cheilo-odontic syndrome:** Prediction only (L5), with no trials or literature. All are held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

