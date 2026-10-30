---
layout: default
title: Citric Acid
parent: Model Prediction Only (L5)
nav_order: 165
evidence_level: L5
indication_count: 8
monitor_inn: "Citric acid"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis"]
last_modified_at: 2026-10-30
description: "Citric Acid: predicted new indication stomach disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Citric Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Citric Acid: Acidulant and organic acid → stomach disease
{: .text-alpha }

## One-Sentence Summary

Citric acid is an organic acid widely used as an acidulant and buffering agent, and it is currently listed as a marketed single-ingredient product in Australia.
The TxGNN model predicts it may be relevant to **stomach disease**, but the data compiled for this report contain **0 clinical trials** and **20 publications**, none of which tests citric acid as a treatment for stomach disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | stomach disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Citric acid is an organic acid that acidifies its surroundings, and this property is plausibly relevant to gastric physiology, such as gastric pH.

The literature does not test this idea as a treatment. The closest item is a diagnostic study (PMID 31505905) in which a citric acid test meal was used to improve the accuracy of the 13C-urea breath test for *Helicobacter pylori*. This is a diagnostic adjunct, not a therapy. Other retrieved papers are general reviews on ulcer diet, *H. pylori* physiology, gastric cancer metabolomics, animal studies, or unrelated topics. The high TxGNN score is a computational output and is not backed by therapeutic evidence for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No cited study evaluates citric acid as a treatment for stomach disease. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Diagnostic clinical study | Gut and Liver | Editorial-style discussion of whether a citric acid meal improves accuracy of the 13C-urea breath test in Asian populations (diagnostic use) |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | Clinical study | Gut and Liver | Effect of citric acid on 13C-urea breath test accuracy after *H. pylori* eradication in a region with a high prevalence of atrophic gastritis (diagnostic use) |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | Experimental | Aliment Pharmacol Ther | Effect of citric, malic and ascorbic acids on intragastric urease activity |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet and nutrition in ulcer disease; restrictive diets not supported |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Physiology and metabolism of *H. pylori* |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Observational/metabolomics | Metabolomics | Serum citric acid and L-carnitine levels before gastric cancer onset in Koreans |
| [7106518](https://pubmed.ncbi.nlm.nih.gov/7106518/) | 1982 | Observational | Gastroenterology | Salivary secretion in reflux oesophagitis |

## Australia Market Information

The data compiled for this report list one valid single-ingredient licence (108Q). Product name, dosage form and approved indication text are not recorded, so no product table can be shown.

## Safety Considerations

**Drug Interactions** (15 recorded; one major, the rest moderate):
- **Major:** aluminium hydroxide (citrate can increase aluminium absorption).
- **Moderate:** quinolone antibiotics, including cinoxacin, ciprofloxacin, enoxacin, gatifloxacin, gemifloxacin, levofloxacin, lomefloxacin, moxifloxacin, nalidixic acid, norfloxacin, ofloxacin, trovafloxacin, grepafloxacin and sparfloxacin.

**Conditions flagged for caution in the data compiled for this report** (these are not label text): hypertension, kidney disease or impaired renal function, liver disease, congestive heart failure, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), peptic ulcer disease, anuria, gout, hypercalcaemia, nephrocalcinosis, thrombocytopenia, haemophilia, chronic diarrhoeal disease and others.

Please refer to the TGA-approved Product Information (PI) for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly tests citric acid for stomach disease, so the evidence level is L5. The TxGNN score of 0.9974 is a model output only, and the literature touches citric acid in diagnostic or off-topic contexts.

**To proceed, the following is needed:**
- Mechanism of action data for citric acid
- Clinical studies of citric acid for a defined gastric condition (for example dyspepsia)
- Product-level label details (indication, dosage form, warnings) for the Australian licence
- A safety review covering the flagged conditions and the aluminium hydroxide and quinolone interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

