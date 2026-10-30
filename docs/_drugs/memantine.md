---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Memantine: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not recorded in the local data"
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Memantine: Pulmonary hypertension
{: .text-alpha }

*Note: The data compiled for this report did not include an approved indication for memantine. The original indication is therefore not stated in the Australian licence data. Memantine is widely known as an NMDA receptor antagonist used for moderate to severe Alzheimer's disease, but this should be confirmed against the TGA-approved Product Information.*

## One-Sentence Summary

Memantine is an oral NMDA receptor antagonist marketed in Australia. The TxGNN model ranks **pulmonary hypertension** first by score, but the best-supported prediction is **migraine disorder** (rank 2), backed by **1 completed Phase 3 trial** and **about 19 publications**, including meta-analyses and a placebo-controlled RCT in related migraine entries. The evidence is promising but limited by small studies, and reviews describe it as "big promise but little evidence".

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 (migraine disorder) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (migraine disorder); Hold for pulmonary hypertension and the other predictions |

**Overview of all 10 predictions**

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|---|---|---|---|---|
| 1 | Pulmonary hypertension | 0.9954 | L5 | Hold |
| 2 | Migraine disorder | 0.9952 | L1 | Proceed with Guardrails |
| 3 | Kyphoscoliotic heart disease | 0.9943 | L5 | Hold |
| 4 | Migraine with brainstem aura | 0.9941 | L5 | Research Question |

The sections below focus on migraine disorder, the best-supported prediction.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Memantine is known to be an uncompetitive NMDA receptor antagonist, and this is the basis of the mechanistic rationale below.

Glutamate and NMDA receptors contribute to cortical spreading depression, trigeminovascular sensitisation and central sensitisation in migraine. Higher glutamate levels have been reported in migraine patients, particularly during attacks, and genes involved in glutamate signalling have been implicated in the condition. Blocking NMDA receptors could therefore plausibly reduce attack frequency.

Clinical evidence is limited. One small Phase 3 trial compares memantine with sodium valproate, and a double-blind placebo-controlled RCT exists in migraine without aura (PMID 26638119). Reviews describe the overall evidence as promising but thin.

Related migraine entries share this rationale but have only indirect evidence. These are migraine with brainstem aura and migraine susceptibility. The pulmonary hypertension prediction has a high score but only a distant mechanistic link, through NMDA signalling in the pulmonary vasculature, and no direct evidence for memantine.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine vs sodium valproate for prophylaxis of episodic migraine. Head-to-head comparison with an active comparator; small sample limits inference |

No registered trials were found for the other predicted indications.

## Literature Evidence

Migraine disorder (most relevant publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Memantine vs placebo in migraine; efficacy described as controversial |
| [35467554](https://pubmed.ncbi.nlm.nih.gov/35467554/) | 2022 | Meta-analysis of RCTs | Clin Neuropharmacol | Effectiveness and safety of memantine vs placebo for headache |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic review | Headache | Efficacy and safety of memantine for prophylaxis of episodic migraine |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Systematic review | Ann Pharmacother | Efficacy and safety of memantine for prevention of primary headache disorders |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network meta-analysis | Front Pharmacol | Comparative efficacy and safety of oral preventive medications for migraine in adults |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT | Headache | Double-blind, placebo-controlled study of memantine for prophylaxis of migraine without aura |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedebergs Arch Pharmacol | Memantine and ketamine as potential anti-migraine agents |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary | Headache | "Big promise but little evidence" |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective study | J Headache Pain | Retrospective study of memantine for migraine prevention in 60 patients |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical practice guideline | Ann Intern Med | 2023 VA/DoD headache guideline covering treatment and prevention of migraine |

Other predictions have little supporting literature. For pulmonary hypertension, there is only a preclinical NMDA receptor study (PMID 33500723). A nitrate derivative of memantine (MN-08) is in development for pulmonary arterial hypertension (PMID 41739394), but this is a different compound.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1956Y | Memantine generichealth | Tablet containing memantine hydrochloride 10 mg | Not available in the data compiled for this report |

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease links, not label text): liver disease, gallbladder disease and impaired renal function.

**Drug interactions** (100 interactions identified; the first 20 retrieved are summarised):
- **Moderate:** anticholinergic and antimuscarinic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
- **Minor:** ranitidine, metformin, cimetidine and potassium citrate.
- **Unknown severity:** glimepiride, doxycycline, lansoprazole, loperamide, famotidine and acetylsalicylic acid.

For migraine, the supporting material highlights monitoring tolerability, especially dizziness, headache and interactions. Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (migraine disorder)**

**Rationale:**
- A completed Phase 3 trial, several meta-analyses and a placebo-controlled RCT support a plausible NMDA-mediated mechanism in migraine prophylaxis. However, the trial is small (n=33), and the authors of reviews describe the evidence as limited. The remaining predictions (pulmonary hypertension, rheumatoid arthritis and the rare disorders) should stay on **Hold**, while the migraine subtypes (brainstem aura, susceptibility) are **Research Questions** relying on extrapolated evidence.

**To proceed, the following is needed:**
- Larger, adequately powered placebo-controlled RCTs in migraine
- The approved indication, warnings and contraindications from the TGA Product Information, which were missing from the data compiled for this report
- Mechanism of action data confirmed from DrugBank
- A tolerability and interaction monitoring plan, particularly for anticholinergic co-medication, and for patients with renal or hepatic impairment
- Direct evidence for memantine before any further consideration of pulmonary hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

