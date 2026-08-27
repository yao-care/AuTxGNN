---
layout: default
title: Cannabidiol
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Cannabidiol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the report template you've supplied (this is a direct content-generation task from the Evidence Pack JSON, not a coding task, so no additional skill applies), here is the evaluation report.

A few data-fidelity notes before the report: `taiwan_regulatory.licenses` is empty (0 ARTG entries, market status "未上市"/Not Marketed), `drug.original_indications` is empty, and `original_moa` is `[Data Gap]`. Per the prohibition on outputting "[Data Gap]" literally, I've replaced these with plain-language statements rather than inventing regulatory text. I also flag a discrepancy in the source data: two of the four RLS-tagged trials (NCT02818777, NCT03582137) are titled and summarised as Parkinson's Disease tremor/motor-symptom studies, not RLS studies, despite being graded "A" for RLS relevance — I've reported them as written in `brief_summary` rather than silently correcting the mismatch, so you can judge relevance yourself.

---

# Cannabidiol: From Refractory Epilepsy to Restless Legs Syndrome

## One-Sentence Summary

Cannabidiol (CBD) is internationally best known as a treatment for severe, treatment-resistant epilepsy syndromes (e.g. Dravet syndrome, Lennox-Gastaut syndrome), though it is **not currently registered on the ARTG in Australia**. The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**, with **4 clinical trials** and **9 publications** currently identified as supporting evidence — though only one trial and one case series are specifically about RLS, with the remainder addressing related neurological/sleep conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Australian regulatory data (drug is not ARTG-registered); internationally associated with treatment-resistant epilepsy |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 96.17% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this specific product is not available in the current evidence pack. Based on general pharmacological knowledge, cannabidiol interacts with the endocannabinoid system (CB1/CB2 receptors) as well as TRPV1/TRPA1 channels, and has documented muscle-relaxant, anti-inflammatory and sleep-modulating effects. These pathways plausibly intersect with RLS pathophysiology, which is thought to involve dopaminergic dysfunction and nocturnal sensorimotor disturbance, and with peripheral nerve sensitisation more broadly.

RLS and CBD's better-established neurological uses (seizure disorders, tremor/motor symptoms in Parkinson's disease) share overlapping mechanistic territory — dopaminergic and motor-sensory circuit modulation — which gives the TxGNN prediction some biological plausibility. However, it is important to note that the strongest-graded clinical trial evidence in this evidence pack (NCT02818777, NCT03582137) was actually conducted in **Parkinson's disease tremor and motor symptoms**, not RLS itself. Only one completed case series (6 patients) and one not-yet-recruiting Phase 2 trial directly target RLS. This means the mechanistic story is reasonable, but direct clinical proof in RLS specifically remains thin.

Because no formal original indication or MOA record exists for this drug in the current dataset, this rationale should be treated as a starting hypothesis for further pharmacological review rather than a confirmed mechanistic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07224932](https://clinicaltrials.gov/study/NCT07224932) | Phase 2 | Not yet recruiting | 60 | Randomised, double-blind, placebo-controlled study of high-CBD cannabis extract (BRC-002) specifically for idiopathic Restless Legs Syndrome — tolerability and efficacy; not yet started. |
| [NCT02818777](https://clinicaltrials.gov/study/NCT02818777) | Phase 2 | Completed | 13 | Randomised, double-blind, placebo-controlled crossover trial of CBD (GWP42003) on **tremor in Parkinson's disease** — graded "A" relevance to RLS by the source pipeline, but the trial population/endpoint is Parkinson's tremor, not RLS. |
| [NCT03582137](https://clinicaltrials.gov/study/NCT03582137) | Phase 2 | Completed | 74 | Randomised, double-blind, placebo-controlled parallel trial of CBD on **motor symptoms in Parkinson's disease** (UPDRS Part III) — again graded "A" relevance to RLS, but the described population/endpoint is Parkinson's motor symptoms, not RLS. |
| [NCT05092191](https://clinicaltrials.gov/study/NCT05092191) | Phase 2 | Recruiting | 250 | CANSEP trial: cannabinoids vs standard treatment for symptom relief in **multiple sclerosis**; RLS is a possible secondary/co-morbid symptom rather than the primary study focus. |

**Note:** No dedicated, completed RCT in an RLS population currently exists. The most RLS-specific trial (NCT07224932) has not yet begun recruiting.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35749710](https://pubmed.ncbi.nlm.nih.gov/35749710/) | 2023 | Post hoc analysis (Phase 2/3 trial) | Cannabis and Cannabinoid Research | Post hoc exploratory analysis of CBD's effect on RLS/Willis-Ekbom Disease severity in Parkinson's disease patients with REM sleep behaviour disorder. |
| [28655453](https://pubmed.ncbi.nlm.nih.gov/28655453/) | 2017 | Case series | Sleep Medicine | Six patients with RLS treated with cannabis, reported symptom relief (abstract not available in source). |
| [32603954](https://pubmed.ncbi.nlm.nih.gov/32603954/) | 2020 | Systematic review (preclinical + clinical) | Sleep Medicine Reviews | Systematic review of cannabinoid therapies across sleep disorders, including limited RLS-relevant data; notes unclear efficacy and safety overall. |
| [39114536](https://pubmed.ncbi.nlm.nih.gov/39114536/) | 2024 | RCT protocol | Frontiers in Neurology | Protocol for the CANSEP trial comparing cannabinoids to standard care for symptom relief in multiple sclerosis (RLS not the primary target population). |
| [39612156](https://pubmed.ncbi.nlm.nih.gov/39612156/) | 2024 | Review | Current Psychiatry Reports | Updated review of cannabis/CBD use for sleep disorders generally. |
| [35459406](https://pubmed.ncbi.nlm.nih.gov/35459406/) | 2022 | Review | Journal of Primary Care & Community Health | Review of cannabinoid effects on sleep; includes a case of insomnia and mood disturbance during cannabinoid withdrawal. |
| [39502532](https://pubmed.ncbi.nlm.nih.gov/39502532/) | 2024 | Retrospective chart review (safety/DDI) | Frontiers in Pharmacology | Retrospective review of adverse events from interactions between cannabinoids and psychotropic drugs — relevant to safety monitoring, not efficacy. |
| [34987023](https://pubmed.ncbi.nlm.nih.gov/34987023/) | 2022 | Narrative review | Clinical Journal of the American Society of Nephrology | Narrative review of cannabinoids for symptom management in kidney failure (tangential to RLS). |
| [33216043](https://pubmed.ncbi.nlm.nih.gov/33216043/) | 2021 | Patient survey | Journal of Parkinson's Disease | Survey of Parkinson's disease patients' views on medical cannabis use (tangential to RLS). |

---

## Australia Market Information

Cannabidiol currently has **no ARTG entries** (Market Status: **Not Marketed**). No approved product information, dosage form, or indication text is available for the Australian market in this evidence pack. Any clinical use in Australia would currently need to proceed via the TGA Special Access Scheme or Authorised Prescriber pathway, subject to separate verification.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. **Note:** because cannabidiol is not currently ARTG-registered, no TGA-approved Australian PI exists for this product at present — a Blocking-severity data gap (DG001) flagged in this evidence pack confirms that formal warnings, contraindications, and interaction data have not yet been retrieved. A drug interaction (DDI) database query also returned no results (`not_found`). Safety review must be sourced from the PI of the jurisdiction where any product is obtained (e.g. overseas-approved CBD products) before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RLS prediction has moderate literature support (L2) but is undermined by two issues: the drug is not registered in Australia (0 ARTG entries), and there is a **Blocking**-severity data gap on safety/PI information that prevents entry into even a preliminary safety assessment (S1). The strongest-graded clinical trials in the evidence pack are actually in Parkinson's disease populations rather than RLS itself, so the direct clinical evidence for RLS specifically is limited to one small case series and one not-yet-recruiting trial.

**To proceed, the following is needed:**
- TGA-approved Product Information (or overseas PI) covering warnings, contraindications, and interactions (currently a Blocking data gap)
- Detailed mechanism of action data specific to this product/formulation
- Results from the RLS-specific Phase 2 trial (NCT07224932) once recruitment begins
- Clarification on whether the Parkinson's disease trials (NCT02818777, NCT03582137) were correctly classified as RLS-relevant, or whether this reflects a knowledge-graph/relevance-tagging error upstream
- A defined regulatory pathway assessment (Special Access Scheme vs formal ARTG submission) given current Not Marketed status
- Note: amyotrophic lateral sclerosis (rank 4, L3/S1) also emerged as a candidate indication with somewhat stronger trial-registry activity and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

