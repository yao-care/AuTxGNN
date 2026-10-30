---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 718
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-30
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis, pulmonary emphysema and related lung disease"
---

# Theophylline
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a xanthine bronchodilator, recorded in the knowledge graph as being used for asthma, bronchitis and emphysema.
The TxGNN model predicts it may be effective for **thrombotic disease**, but there are **0 registered clinical trials** and no retrieved publication that directly studies this use, so the prediction rests on the model score and a theoretical mechanism alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related lung disease (relations recorded in the knowledge graph; the Australian licence record contains no indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Theophylline is generally known as a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist. PDE inhibition raises cAMP in platelets, which could in theory reduce platelet aggregation. This is the most plausible basis for the high prediction score.

The mechanism is not straightforward, however. Adenosine receptor antagonism could oppose adenosine's own antiplatelet effect. No retrieved paper shows a clinical antithrombotic benefit of theophylline. The link between its respiratory use and thrombosis is therefore a model-derived hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Nineteen publications were retrieved, but none directly studies theophylline for thrombotic disease. Most concern platelet biology, laboratory methods or other drugs. Representative examples are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, a different antiplatelet drug; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostaglandins, platelets and atherosclerosis; background on platelet cAMP signalling |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone (a PDE inhibitor) inhibits human platelet aggregation and interacts with adenosine; indirect mechanistic relevance only |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Platelet and neutrophil activation in Behçet's disease; not about theophylline |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflammatory Bowel Diseases | Platelet-leukocyte aggregates in inflammatory bowel disease; not about theophylline |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory method | British Journal of Haematology | Theophylline used only as a sample-collection additive in a platelet factor 4 assay |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | Aptasensor for detecting theophylline; no clinical relevance to thrombosis |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2614N | Nuelin | Oral solution 133.3 mg per 25 mL, 500 mL | Not stated in the licence record |

## Safety Considerations

**Contraindication-type relations recorded in the knowledge graph (not label text):** hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis.

**Drug interactions:** 100 interactions were recorded. The ones shown include:
- **Major:** bupropion
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, clarithromycin, doxycycline, tetracycline, minocycline, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
- **Minor:** ephedrine

Theophylline has a narrow therapeutic window, so serum level monitoring is relevant. Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by any registered trial or any publication directly studying theophylline in thrombotic disease. The PDE-inhibition mechanism is plausible, but adenosine antagonism may work against it, and the evidence level is L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a focused analysis of platelet and thrombosis effects
- Preclinical or ex vivo platelet aggregation data for theophylline at clinically achievable concentrations
- Review of the TGA Product Information for warnings and contraindications
- A safety assessment of the narrow therapeutic window and the many interactions in patients likely to need antithrombotic therapy

## Other Predicted Indications (Brief Notes)

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Nasal cavity disease | 0.9953 | L5 | One small human nasal allergen challenge study in allergic rhinitis (PMID 9648963); design not confirmed; no registered trials |
| 3 | Laryngotracheitis | 0.9951 | L5 | No trials or literature |
| 4 | Tracheal disease | 0.9949 | L3 | Preclinical tracheal relaxation studies and a veterinary retrospective study in dogs (PMID 31565900); no human trial |
| 5 | Pharyngitis | 0.9946 | L4 as supplied | No retrieved study directly addresses theophylline in pharyngitis, so by the evidence ceiling rule this should be treated as L5 |
| 6 | Acute laryngopharyngitis | 0.9935 | L5 | No trials or literature |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

