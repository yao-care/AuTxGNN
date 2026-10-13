---
layout: default
title: Candesartan
parent: Model Prediction Only (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Candesartan
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

# Candesartan: From Hypertension to Migraine Disorder

## One-Sentence Summary

Candesartan is an angiotensin II type 1 receptor blocker used for hypertension and registered in Australia as Atacand.
The TxGNN model predicts it may be effective for **migraine disorder**,
with **4 clinical trials** (3 directly relevant) and **20 publications** currently supporting this direction, including a 2025 randomised placebo-controlled trial in *The Lancet Neurology*.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (from pharmacology data compiled for this report; the ARTG entry has no indication text recorded) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (with caution: the key trials are Phase 2 or Phase 2/3, not two completed Phase 3 RCTs) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Candesartan blocks the angiotensin II type 1 (AT1) receptor, encoded by *AGTR1*. Detailed mechanism of action data is not available in the data compiled for this report, but this class action is well established.

Renin-angiotensin system modulation is proposed to reduce migraine frequency through effects on cerebrovascular tone, neuroinflammation and sympathetic activity. Migraine prevention is a plausible extension of a drug that already acts on vascular tone and is widely used for hypertension. Several blood pressure-lowering drugs, such as beta-blockers, are already used for migraine prevention.

This is supported by clinical data: randomised placebo-controlled and active-comparator trials, and a 2025 randomised trial in episodic migraine. An Australian review (Med J Aust, 2008) also described candesartan as a "new" prophylactic option with reasonably good but limited evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04574713](https://clinicaltrials.gov/study/NCT04574713) | Phase 2 | Completed | 450 | Triple-blind, placebo-controlled, multicentre trial of candesartan 8 mg and 16 mg for migraine prevention. Likely corresponds to the 2025 Lancet Neurology publication (PMID 40975098) |
| [NCT00884663](https://clinicaltrials.gov/study/NCT00884663) | Phase 2/3 | Completed | 72 | Double-blind, double-dummy, placebo-controlled triple cross-over comparing candesartan with propranolol. Small sample limits power |
| [NCT04138316](https://clinicaltrials.gov/study/NCT04138316) | N/A (observational) | Completed | 85 | CandeSpartan study: response predictors and tolerability in patients with migraine who had failed three or more preventives |
| [NCT07655440](https://clinicaltrials.gov/study/NCT07655440) | Phase 4 | Not yet recruiting | 120 | Compares migraine preventives with anti-CGRP therapies for tinnitus in people with migraine. Only indirectly relevant; no results |

No ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40975098](https://pubmed.ncbi.nlm.nih.gov/40975098/) | 2025 | RCT | The Lancet. Neurology | Randomised, triple-blind, placebo-controlled Phase 2 trial of candesartan for episodic migraine prevention (safety, tolerability and efficacy) |
| [37350141](https://pubmed.ncbi.nlm.nih.gov/37350141/) | 2023 | Systematic review and meta-analysis | Cephalalgia | Effect of blood pressure-lowering drugs on episodic migraine prevention |
| [38057728](https://pubmed.ncbi.nlm.nih.gov/38057728/) | 2023 | Systematic review and network meta-analysis | J Headache Pain | Ranks preventive drugs for chronic migraine in adults |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review with economic modelling | Health Technol Assess | Clinical and cost-effectiveness of preventive drugs for chronic migraine |
| [39899861](https://pubmed.ncbi.nlm.nih.gov/39899861/) | 2025 | Clinical guideline | Ann Intern Med | American College of Physicians guideline on pharmacological prevention of episodic migraine |
| [40571531](https://pubmed.ncbi.nlm.nih.gov/40571531/) | 2025 | Scoping review | Clin Ther | Candesartan shows potential as a migraine management option |
| [38663908](https://pubmed.ncbi.nlm.nih.gov/38663908/) | 2024 | Observational study | Cephalalgia | CandeSpartan: effectiveness, tolerability and response predictors, noting two earlier RCTs support candesartan |
| [18759728](https://pubmed.ncbi.nlm.nih.gov/18759728/) | 2008 | Review | Med J Aust | Australian review: evidence for candesartan in migraine prophylaxis is reasonably good but limited |
| [38307673](https://pubmed.ncbi.nlm.nih.gov/38307673/) | 2024 | Review | Handb Clin Neurol | Lists candesartan among non-specific oral agents for migraine prevention |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Review | Am Fam Physician | Overview of migraine prophylaxis |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13436E | Atacand | Tablet containing candesartan cilexetil 8 mg (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only pharmacology data (candesartan acting on the AT1 receptor) and no drug-drug interactions.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications. As an angiotensin receptor blocker, candesartan is generally known to carry fetal toxicity concerns in pregnancy, which is relevant when considering use in migraine, since the condition is common in women of reproductive age. One review in the data compiled for this report (PMID 15669052) describes case reports of oligohydramnios and pulmonary hypoplasia with this drug class.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, large (n=450) triple-blind placebo-controlled trial published in *The Lancet Neurology*, a Phase 2/3 active-comparator trial and supportive meta-analyses and guidelines give direct clinical evidence for migraine prevention. However, the pivotal trial is Phase 2 and the Phase 2/3 trial is small, so the evidence does not fully meet two completed Phase 3 RCTs.

**To proceed, the following is needed:**
- Review of the TGA Product Information for warnings and contraindications, particularly pregnancy and women of childbearing potential
- Detailed mechanism of action data
- Confirmation of the dose (8 mg vs 16 mg) and efficacy results from the 2025 trial
- Confirmation of the original approved indication text for ARTG 13436E
- A Phase 3 confirmatory trial or regulatory guidance on whether the current evidence suffices for an Australian indication extension

**Other predicted indications (for reference):** migraine with brainstem aura and migraine with or without aura (susceptibility) are subtypes or overlapping terms of migraine, with no trials registered under these specific terms (L4, research question). Pulmonary hypertension has only preclinical support (L4, Hold). Prinzmetal angina, kyphoscoliotic heart disease, atrophoderma vermiculata, ulerythema ophryogenesis, benign prostatic hyperplasia and alopecia rest on model prediction alone (L5, Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

