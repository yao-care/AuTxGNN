---
layout: default
title: Zinc
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zinc: predicted new indication Filariasis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Zinc"
predicted_indications: ["filariasis", "primary hereditary glaucoma", "dermatitis", "open-angle glaucoma", "acrodermatitis chronica atrophicans", "enterocolitis (disease)", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "amyopathic dermatomyositis"]
---

# Zinc
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

## Zinc: From an Unspecified Original Indication to Filariasis
{: .text-alpha }

## One-Sentence Summary

Zinc is an essential trace element with one ARTG entry in Australia, but the data compiled for this report contain no approved indication text for it.
The TxGNN model predicts it may be effective for **filariasis** (score 93.2%), but there are **0 clinical trials** and no literature testing zinc as a treatment for filarial infection.
The prediction is computational only, so this report recommends **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Filariasis |
| TxGNN Prediction Score | 93.19% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc is an essential micronutrient involved in enzyme function, immune function and tissue repair, but the data compiled for this report do not identify an approved indication, so no original-to-new indication link can be drawn.

The retrieved literature does not support the prediction. It covers zinc oxide nanoparticles as mosquito-vector larvicides, zinc-containing proteins and enzymes in filarial parasites, a machine-learning study of nutritional predictors of lymphatic filariasis progression, and computational screening against *Wolbachia* targets. None of it tests zinc as a treatment for human filarial infection. The high score should be treated as a computational hypothesis only.

Other predicted indications show stronger, though still limited, support:

- **Dermatitis** (score 91.7%, L3): Topical zinc oxide is already an established barrier agent in diaper dermatitis, and zinc deficiency causes dermatitis (acrodermatitis enteropathica). This is largely an existing use rather than a novel repurposing finding.
- **Enterocolitis** (score 90.7%, L3): Indirect support from neonatal zinc literature, including a Cochrane review of enteral zinc in preterm infants. The trials target broader outcomes and have no reported results.
- **Open-angle glaucoma** (score 91.5%, L4): Observational studies show altered zinc levels in glaucoma, but there is no evidence that supplementation helps.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for filariasis.

---

## Literature Evidence

The literature below was retrieved for the predicted filariasis indication. None of it tests zinc as a treatment in humans.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40524903](https://pubmed.ncbi.nlm.nih.gov/40524903/) | 2025 | Systematic review | J Trop Med | Metal-based nanoparticles as mosquito vector control agents |
| [40138337](https://pubmed.ncbi.nlm.nih.gov/40138337/) | 2025 | Observational (machine learning) | PLoS One | Nutritional predictors of lymphatic filariasis progression in Ghana (109 participants) |
| [40352769](https://pubmed.ncbi.nlm.nih.gov/40352769/) | 2025 | Preclinical | 3 Biotech | Green-synthesised ZnO nanoparticles with mosquito larvicidal activity |
| [36320445](https://pubmed.ncbi.nlm.nih.gov/36320445/) | 2022 | Preclinical | Biomass Convers Biorefin | Bio-fabricated ZnO nanoparticles against *Culex quinquefasciatus* (lymphatic filariasis vector) |
| [34666103](https://pubmed.ncbi.nlm.nih.gov/34666103/) | 2021 | In silico | Mol Biochem Parasitol | Computational screening of inhibitors of *Wolbachia* MurF in *Brugia malayi* |
| [15521106](https://pubmed.ncbi.nlm.nih.gov/15521106/) | 2004 | Double-blind RCT | Ann Trop Med Parasitol | Limb care with penicillin and/or diethylcarbamazine for adenolymphangitis in bancroftian filariasis (zinc is not the intervention) |
| [16870314](https://pubmed.ncbi.nlm.nih.gov/16870314/) | 2006 | Preclinical (animal) | Vaccine | A zinc-containing collagenase from *Setaria cervi* as a vaccine antigen against *Brugia malayi* in jirds |
| [18262499](https://pubmed.ncbi.nlm.nih.gov/18262499/) | 2008 | Preclinical | Acta Trop | Zinc-dependent leucine aminopeptidase characterised in *Setaria cervi* |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 7558T | Not available | Not available | Not available |

---

## Safety Considerations

No warnings, contraindications or drug interaction data were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The filariasis prediction rests on the model score alone. There are no clinical trials, and the literature concerns zinc oxide as a vector-control agent and parasite biology rather than zinc as a human treatment. Nor are there any approved-indication, mechanism or safety data to support progression.

**To proceed, the following is needed:**
- The approved indication, warnings and contraindications from the ARTG/TGA Product Information, which is a blocking gap
- Mechanism of action data from DrugBank
- Preclinical evidence that zinc has activity against filarial parasites
- Consideration of dermatitis (existing topical zinc oxide use) and preterm-neonate enterocolitis as better-supported research questions, subject to further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

