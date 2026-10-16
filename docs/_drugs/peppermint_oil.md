---
layout: default
title: Peppermint Oil
parent: Model Prediction Only (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Peppermint Oil: predicted new indication Top-ranked: leprosy . Best-evidenced: cardiovascular disease (evidence level L5). Approved use: Not specified in the data compiled for this report"
monitor_inn: "Peppermint oil"
predicted_indications: ["leprosy", "pneumocystosis", "coronary artery disease", "myocardial ischemia", "echinococcus granulosus infectious disease", "polyp of vocal cord", "uterine polyp", "polyp of middle ear", "cardiovascular disease", "polyp of frontal sinus"]
---

# Peppermint Oil
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

# Peppermint Oil: From an Unspecified Original Indication to Cardiovascular Disease

## One-Sentence Summary

Peppermint oil is registered in Australia, but the data compiled for this report do not specify an approved indication.
The TxGNN model ranks **leprosy** first by score, yet that prediction has no supporting studies. The only prediction with real study data is **Cardiovascular Disease** (hypertension), with **1 completed clinical trial** and **2 directly relevant publications**, one of which is the trial report itself.
Because that trial is small and its results were not available to us, the evidence for any new indication remains early-stage.

## Quick Overview

The top-ranked prediction (leprosy) has no supporting evidence. This report therefore also covers the best-evidenced prediction, cardiovascular disease (ranked 9th).

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report |
| Predicted New Indication | Top-ranked: leprosy (no evidence). Best-evidenced: cardiovascular disease |
| TxGNN Prediction Score | Leprosy 99.80%; cardiovascular disease 99.13% |
| Evidence Level | Leprosy: L5. Cardiovascular disease: L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (leprosy and other L5 predictions). Cardiovascular disease: Hold pending trial results, treated as a research question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The original indication for peppermint oil is also not recorded in the data compiled for this report, so a direct link between the original and new indications cannot be drawn.

**Leprosy and the other top-ranked predictions** (pneumocystosis, echinococcosis, several polyp types) have no supporting trials or literature. The high scores for multiple polyp types suggest a model-level artefact rather than a disease-specific signal. These predictions should be regarded as computational output only.

**Cardiovascular disease** is the one area with a plausible, though still speculative, rationale. Menthol, the main constituent of peppermint oil, may affect vascular tone through calcium-channel and TRP-channel modulation. A physiological study in healthy volunteers (PMID 30070742) also suggested that gastric cooling and menthol increase cardiac parasympathetic activity. Whether this translates into a benefit in hypertension or coronary disease has not been shown in the data available. The same speculative vasodilation argument has been raised for coronary artery disease and myocardial ischaemia, but no evidence was supplied for either.

## Clinical Trial Evidence

Trials relate to cardiovascular disease, the only prediction with registered trials.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | Not applicable | Completed | 40 | Effects of peppermint oil on cardiometabolic outcomes in people with mild-moderate hypertension. It follows an earlier randomised trial suggesting oral peppermint improved systolic blood pressure and blood lipids in healthy people. Results were not available in the data compiled for this report. |

No ANZCTR trial identifiers were available. No registered trials were found for leprosy or the other predicted indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42024666](https://pubmed.ncbi.nlm.nih.gov/42024666/) | 2026 | Placebo-controlled RCT | PLoS One | Twice-daily peppermint oil supplementation and cardiometabolic outcomes in people with pre- and stage 1 hypertension. The abstract excerpt available does not include results. |
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT protocol | PLoS One | Protocol for the placebo-controlled trial above. Peppermint's menthol and flavonoids are proposed to have potential antihypertensive benefits. |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Physiological study | Exp Physiol | In healthy volunteers, gastric cooling and menthol increased cardiac parasympathetic activity and reduced heart rate. |

The remaining retrieved items were unrelated (lercanidipine and candesartan formulation studies, breath volatile monitoring, and an integrative-medicine commentary that includes peppermint oil for irritable bowel syndrome) and are not listed.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 342B | Not available | Not available | Not available |

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug interaction records were found in the data compiled for this report, and no contraindication data from the knowledge graph were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Leprosy and most other predictions (L5) are model outputs with no trials, literature or mechanistic support.
- Cardiovascular disease (L3) has one small, completed, non-phased trial (n=40) and a related RCT report, but outcome data were not available to us, so efficacy cannot be judged. It is best treated as a research question.

**To proceed, the following is needed:**
- Results of NCT05561543 and the full text of PMID 42024666, including blood pressure effect sizes and adverse events
- The approved indication, dosage form and product details for the ARTG entry
- Mechanism of action data for peppermint oil (for example from DrugBank)
- Safety information (warnings, contraindications) from the TGA Product Information
- Confirmation of route and formulation compatibility for any cardiovascular use
- For the other predicted indications, any independent supporting evidence before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

