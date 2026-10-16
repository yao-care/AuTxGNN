---
layout: default
title: Chloroform
parent: Model Prediction Only (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chloroform: predicted new indication Insomnia (evidence level L5). Approved use: Not recorded in the data compiled for this report (historically a gen…"
monitor_inn: "Chloroform"
predicted_indications: ["insomnia (disease)", "anxiety", "sleep disorder, initiating and maintaining sleep", "irritable bowel syndrome", "enterocolitis (disease)", "Jeune syndrome situs inversus", "bronchitis", "orofacial clefting syndrome", "partial deletion of the long arm of chromosome 22", "interventricular septum aneurysm"]
---

# Chloroform
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

# Chloroform: From No Recorded Indication to Insomnia

## One-Sentence Summary

Chloroform was historically used as an inhaled general anaesthetic, but the data compiled for this report contain no approved indication for it in Australia.
The TxGNN model predicts it may be effective for **insomnia**, but there are **0 clinical trials** and no human studies of chloroform for this use.
The prediction is computational only, and chloroform's toxicity makes it unsuitable as a therapeutic candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report (historically a general anaesthetic) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 98.87% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Chloroform historically acted as a central nervous system (CNS) depressant and general anaesthetic. This is probably through potentiation of GABA-A receptors and modulation of other ion channels, which could plausibly explain sedative effects.

That sedative action is the only conceptual link to insomnia, and to the related predictions of anxiety and sleep disorders (initiating and maintaining sleep). However, chloroform has a narrow therapeutic index. It is hepatotoxic, nephrotoxic and cardiotoxic, and is a probable carcinogen.

The retrieved literature does not study chloroform as a treatment. The two publications for insomnia are animal or plant-extract studies in which chloroform is only an extraction solvent. The TxGNN score is therefore a model output and not evidence of benefit.

Other high-scoring predictions in the data include anxiety (91.07%), sleep disorder (90.75%), irritable bowel syndrome (90.02%), enterocolitis (86.36%) and bronchitis (86.04%). None has clinical trial evidence, and several (such as Jeune syndrome, orofacial clefting syndrome and chromosome 22 deletion) are likely artefacts of the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32711536](https://pubmed.ncbi.nlm.nih.gov/32711536/) | 2020 | Preclinical (animal / docking) | BMC Complement Med Ther | Analgesic, anti-inflammatory and sedative activity of a compound from *Diospyros lotus*; not a study of chloroform as a drug |
| [27656145](https://pubmed.ncbi.nlm.nih.gov/27656145/) | 2016 | Preclinical (plant extract) | Front Pharmacol | *Ziziphus jujuba* root bark fractions protect against liver injury and inflammation; insomnia is mentioned only as a traditional use |

Literature for related predictions (such as anxiety) is similarly indirect: historical anaesthesia reviews and animal studies of plant extracts. One chloroform-specific case report (PMID 27788591, 2017, *Clinical Toxicology*) describes severe gastrointestinal injury, liver toxicity and dermatitis after ingestion, which is evidence of harm.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 187W | Not available | Not available | Not available |

---

## Safety Considerations

Safety information specific to Australia was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

Based on the retrieved literature and general toxicology knowledge, chloroform:
- Causes CNS and respiratory depression, and delayed hepatotoxicity after ingestion
- Is nephrotoxic and cardiotoxic, sensitising the myocardium to catecholamines and potentially causing arrhythmias
- Is a probable carcinogen and a suspected developmental toxicant
- Suppressed lung host defences in mice after inhalation (PMID 20925451)

No drug interaction data were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-based only (L5), with no clinical trials and no human evidence of benefit. The known toxicity profile makes chloroform unsuitable as a sleep or anxiety therapeutic.

**To proceed, the following is needed:**
- Confirmation of the product, dosage form and approved use behind the single Australian registration entry
- Mechanism of action data from DrugBank
- Product Information warnings and contraindications (a blocking gap for safety screening)
- Any human clinical evidence for the predicted indication, which is not currently available
- A clear rationale for why a safer, established sedative would not be preferred
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

