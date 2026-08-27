---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Modafinil
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

# Modafinil: From Narcolepsy to Insomnia (Disease)

## One-Sentence Summary

> Modafinil is a wakefulness-promoting agent whose established use is for excessive daytime sleepiness associated with narcolepsy (this remains its top TxGNN-ranked match, confirming the model recognises its known biology).
> The model's **rank 1 novel candidate** is **Insomnia (disease)**, but the supporting evidence is largely a knowledge-graph mismatch — most of the associated trials describe excessive sleepiness disorders (narcolepsy, obstructive sleep apnoea, Parkinson's disease), not insomnia, and the drug's core pharmacology (wake-promotion) runs counter to insomnia treatment.
> Only 2 of 29 linked trials are genuinely insomnia-focused, both in narrow oncology populations; overall evidence level is **L4**, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy / excessive daytime sleepiness (modafinil's established wake-promoting use; not captured in local ARTG data because the product is not currently marketed in Australia) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this evidence pack. Based on what is otherwise well established for modafinil (and consistent with the trial evidence collected under other candidate indications in this same dataset), modafinil is a wake-promoting agent that inhibits dopamine reuptake and activates hypothalamic orexin/histamine signalling to sustain alertness — this is the mechanism underlying its approved uses in narcolepsy, obstructive sleep apnoea-associated sleepiness, and shift-work disorder.

This mechanism creates a **direct conflict** with the predicted indication of insomnia. Insomnia is a disorder of difficulty initiating or maintaining sleep; a drug that pharmacologically promotes wakefulness would be expected to worsen, not improve, insomnia. The evidence pack's own trial-relevance annotations support this concern: of the 29 clinical trials linked to this candidate, the majority (e.g. NCT00174174, NCT03083132, NCT03620253) are actually narcolepsy, Parkinson's disease, or post-depression cognitive-impairment trials that appear to have been mapped to the "insomnia" disease node in error. Only two trials are genuinely insomnia-focused (NCT01011218, NCT00124384), and both are limited in scope.

On balance, this candidate should be read as a probable **knowledge-graph node-mapping artefact** rather than a genuine pharmacological repurposing signal.

---

## Clinical Trial Evidence

Note: most trials below were retrieved because they share a disease-node link with "insomnia" in the knowledge graph, not because they studied insomnia directly — this is flagged per trial.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | The only trial with a purpose-built primary insomnia population; examined modafinil's effect on daytime functioning and insomnia severity, alone or with CBT-I |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot RCT of behavioural insomnia therapy ± armodafinil in breast cancer patients (relevance graded B — genuinely insomnia-related but confined to an oncology subgroup) |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | CBT ± armodafinil for insomnia and fatigue following chemotherapy in cancer survivors |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I and armodafinil for insomnia in breast cancer patients post-chemotherapy (overlapping population with NCT01019187) |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | NA | Completed | 39 | Armodafinil and/or CBT-I for insomnia comorbid with sleep-disordered breathing |
| [NCT00174174](https://clinicaltrials.gov/study/NCT00174174) | NA | Completed | 30 | Relevance graded C — actually a narcolepsy/excessive daytime sleepiness trial, mismapped to the insomnia node; clinical direction is opposite to insomnia treatment |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Relevance graded C — terminated after enrolling only 2 of a planned cohort; minimal evidentiary value |
| [NCT03083132](https://clinicaltrials.gov/study/NCT03083132) | Phase 2 | Completed | 21 | Parkinson's disease freezing-of-gait trial — unrelated to insomnia; another apparent node mismatch |
| [NCT03620253](https://clinicaltrials.gov/study/NCT03620253) | Phase 3 | Terminated | 9 | Post-depression residual cognitive impairment trial, terminated early — unrelated to insomnia |
| [NCT07295834](https://clinicaltrials.gov/study/NCT07295834) | Phase 2 | Not yet recruiting | 70 (planned) | Inflammatory bowel disease-related fatigue feasibility study, not yet started — unrelated to insomnia |

---

## Literature Evidence

None of the following specifically studies modafinil as a treatment for primary insomnia; they were retrieved via shared disease-node associations and mostly concern excessive daytime sleepiness in other conditions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-based review | Drugs | Broad review of approved and investigational uses of modafinil, based on RCT data in sleepiness-related conditions |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic review/meta-analysis | PloS one | Modafinil's efficacy on fatigue and excessive daytime sleepiness across neurological disorders |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic review | Parkinsonism & Related Disorders | Pharmacological interventions for daytime sleepiness in Parkinson's disease |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Profile of pitolisant (an alternative agent) in narcolepsy management |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opinion on Emerging Drugs | Emerging treatments for narcolepsy and related hypersomnolence disorders |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Revue Neurologique | Narcolepsy with cataplexy — clinical overview |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Review | Neurotherapeutics | Treatment of sleep disorders associated with Parkinson's disease |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review | Parkinsonism & Related Disorders | Excessive daytime sleepiness in Parkinson's disease |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Burden of illness and management of shift-work sleep disorder |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | Journal of Head Trauma Rehabilitation | Randomised trial of modafinil for fatigue and excessive daytime sleepiness after traumatic brain injury |

---

## Australia Market Information

Modafinil is not currently registered on the Australian Register of Therapeutic Goods (ARTG); no marketed product entries or approved indication text are available for this drug in Australia.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No drug-drug interaction records, key warnings, or contraindication data were returned for modafinil in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic direction is contradictory — a wake-promoting agent is not a plausible treatment for insomnia — and the supporting trial base is dominated by clinical trials that appear to be knowledge-graph mismatches to unrelated sleepiness disorders (narcolepsy, Parkinson's disease, post-depression cognitive impairment) rather than genuine insomnia studies. The two directly relevant trials are small and confined to cancer-related insomnia, which does not support a general insomnia indication.

**To proceed, the following is needed:**
- Confirmation/correction of the TxGNN disease-node mapping for "insomnia (disease)" to rule out a knowledge-graph artefact
- TGA-approved Product Information for modafinil (currently unavailable, as the product is not marketed in Australia)
- Detailed mechanism of action data to formally document the wake-promoting vs. insomnia conflict

**Note for reviewers:** this evidence pack also contains three other candidates with stronger, internally consistent evidence — hypersomnia (L1, "Proceed with Guardrails"), circadian rhythm/shift-work sleep disorder (L1, "Proceed with Guardrails"), and narcolepsy susceptibility (L1, "Proceed with Guardrails") — which largely re-confirm modafinil's own established wakefulness-disorder indications rather than representing novel repurposing opportunities. ADHD (L1, "Hold") has substantial trial support but was historically declined by the FDA for paediatric use due to serious skin reaction risk (Stevens-Johnson syndrome), making it a safety-driven Hold rather than an evidence-driven one. These may be more productive candidates for further pharmacist review than the insomnia signal above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

