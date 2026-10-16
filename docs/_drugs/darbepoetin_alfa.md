---
layout: default
title: Darbepoetin Alfa
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Darbepoetin Alfa: predicted new indication Amenorrhoea (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Darbepoetin alfa"
predicted_indications: ["amenorrhea (disease)", "renin-angiotensin-aldosterone system-blocker-induced angioedema", "anaphylaxis", "psoriasis", "penile fibromatosis", "food-dependent exercise-induced anaphylaxis", "Peyronie disease", "Ledderhose disease", "infantile digital fibromatosis", "HER2 positive breast carcinoma"]
---

# Darbepoetin Alfa
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

# Darbepoetin alfa: From Anaemia (Erythropoiesis Stimulation) to Amenorrhoea

## One-Sentence Summary

Darbepoetin alfa is an erythropoiesis-stimulating agent (an EPO receptor agonist) marketed in Australia as Aranesp. The TxGNN model predicts it may be relevant to **amenorrhoea**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the ARTG entry has no indication text) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 96.73% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known pharmacology, darbepoetin alfa is an erythropoiesis-stimulating agent that acts on the erythropoietin receptor. It is generally used to correct anaemia in chronic disease settings.

A possible indirect link to amenorrhoea is that anaemia in chronic illness can accompany secondary amenorrhoea. Correcting the anaemia might help in that setting. This is speculative and is not supported by any trial or publication retrieved. The high TxGNN score reflects knowledge-graph associations, not demonstrated efficacy.

Other top-ranked predictions (for example RAAS-blocker-induced angioedema, anaphylaxis, psoriasis, and fibromatoses such as Peyronie and Ledderhose disease) also lack a clear mechanistic rationale. Anaphylaxis and hypersensitivity are safety concerns for protein therapeutics, which argues against a therapeutic role there.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly related to darbepoetin alfa in amenorrhoea is available.

For the lower-ranked prediction of psoriasis, one paper was retrieved, but it does not support darbepoetin:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40519492](https://pubmed.ncbi.nlm.nih.gov/40519492/) | 2025 | Case report | Cureus | Deucravacitinib used for psoriasis in a patient with myelodysplastic syndrome. It does not involve darbepoetin, and the link is incidental co-occurrence only. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 5637Q | Aranesp | Injection 10 micrograms in 0.4 mL pre-filled syringe | Not available in the data compiled |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph links the drug to hypertensive disorder and hypertension as contraindication-related conditions.
- **Drug Interactions** (17 recorded):
  - **Major**: carfilzomib, lenalidomide, pomalidomide, thalidomide
  - **Moderate**: cyclosporine, human C1-esterase inhibitor, conestat alfa
  - **Minor**: ACE inhibitors (fosinopril, benazepril, captopril, enalapril, lisinopril, moexipril, perindopril, quinapril, ramipril, trandolapril)
- Other concerns noted in the data: ESAs carry safety concerns about tumour progression and mortality in some cancer settings, and hypersensitivity reactions are possible with protein therapeutics.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or supporting publications, no established mechanism links EPO receptor signalling to amenorrhoea, and the safety profile (hypertension-related contraindication signal, major interactions with thalidomide-class agents) calls for caution.

**To proceed, the following is needed:**
- The approved indication text and the PI warnings and contraindications for Aranesp
- Detailed mechanism of action data
- A literature and trial search specific to darbepoetin or ESAs in amenorrhoea
- A plausible mechanistic or clinical rationale, such as amenorrhoea secondary to anaemia of chronic disease
- A route compatibility assessment and a safety review in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

