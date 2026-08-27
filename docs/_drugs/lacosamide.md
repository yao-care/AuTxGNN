---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is an antiepileptic drug (AED) with an established role in focal (partial-onset) seizure management. The TxGNN model predicts it may also be effective for **Manic Bipolar Affective Disorder**, with **1 registered clinical trial** and **14 supporting publications** currently identified, though most of this literature is early-stage (case reports, an open-label pilot trial, and one retrospective comparison).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal (partial-onset) epilepsy / seizures — this is an international indication inferred from trial and literature context (e.g. "an anticonvulsant that is FDA-approved for treating partial seizures"); no local Australian indication text is available |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 (Observational studies) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Lacosamide is not available in the current data set (DrugBank query flagged as a High-severity data gap). Based on the supporting literature retrieved for this candidate, Lacosamide's known mechanism is selective enhancement of the slow inactivation of voltage-gated sodium channels, producing extended stabilisation of neuronal cell membranes (PMID 28845834). This membrane-stabilising action is the same broad pharmacological class effect that underlies the long-standing use of other AEDs as mood stabilisers in bipolar disorder.

Epilepsy and bipolar disorder are frequently comorbid, and psychiatric symptoms (depression, anxiety, mood instability) are well recognised in people with epilepsy. Several publications in this evidence set directly explore this overlap: a prospective multicentre study found Lacosamide improved depressive and anxiety symptoms in patients with focal epilepsy independent of seizure control (PMID 29253680), and a retrospective 30-day comparison assessed Lacosamide's effects specifically in bipolar disorder patients without epilepsy (PMID 30251375). An open-label pilot trial further tested Lacosamide as an augmentation strategy in bipolar depression (PMID 33666402).

Mechanistically, the rationale is plausible — AEDs have been repurposed as mood stabilisers since the 1950s due to shared membrane-stabilising and neuronal excitability-modulating properties. However, the evidence base remains early-stage: it consists mainly of case reports, one retrospective comparison, and one open-label (non-randomised) pilot trial, with only a single ongoing, not-yet-completed Phase 3 RCT (NCT07412132) directly testing this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Randomised, double-blind, parallel-group trial evaluating Lacosamide as an augmentation treatment to first-/second-line therapy in moderate-to-severe major depressive episodes of Bipolar Disorder Type I and II; built on prior observational and open-label signals of antidepressant/antimanic effect. Estimated completion January 2027. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label trial | Journal of Clinical Psychopharmacology | 12-week open-label pilot trial of Lacosamide for bipolar depression, providing the first prospective (non-randomised) efficacy/safety signal in this population. |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective comparison | Psychiatry and Clinical Neurosciences | 30-day hospital-based comparison of Lacosamide against a retrospective cohort treated with other antiepileptics in bipolar disorder patients without epilepsy. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicentre study | Epilepsy & Behavior | Lacosamide associated with improvement in depression and anxiety symptoms in focal epilepsy patients, assessed as independent of seizure-control effects. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Bio-Medica | Mood disorder comorbid with PTSD and fronto-temporal epilepsy stabilised with Lacosamide; proposes membrane-stabilising sodium-channel mechanism as basis for mood effect. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report | Indian Journal of Psychological Medicine | Neutropenia precipitated by Lacosamide in a patient with bipolar disorder and comorbid epilepsy — relevant safety signal for this population. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Complex case of a pregnant patient with Bipolar Disorder I and comorbid epilepsy/PNES, illustrating real-world multi-agent management including Lacosamide. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Therapeutic Drug Monitoring | Update on therapeutic drug monitoring of AEDs, noting expanding off-label use of AEDs, including for bipolar disorder management. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chemical Neuroscience | Reviews CRMP2 as a druggable neurological target; relevant to Lacosamide's proposed non-sodium-channel mechanism affecting mood/pain pathways. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Advanced Drug Delivery Reviews | Overview of chemical properties of AEDs approved 1990–2011, including Lacosamide, covering pharmacokinetic and tolerability profile. |
| [16732716](https://pubmed.ncbi.nlm.nih.gov/16732716/) | 2006 | Review | Expert Opinion on Investigational Drugs | Reviews second-generation AEDs (including precursors to Lacosamide's class) and their improved tolerability/interaction profile supporting broader therapeutic use. |

---

## Australia Market Information

Lacosamide currently has **no ARTG entries** and is **not marketed in Australia** (market status: Not Marketed). No product listings, dosage forms, or approved indication text are available from local regulatory records.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug–drug interactions) could be retrieved for Lacosamide in this evidence pack — this is flagged as a **Blocking** data gap (DG001), since Lacosamide is not currently registered in Australia and no TGA-approved Product Information exists locally.

> Please refer to the sponsor's international Product Information (e.g. the overseas Vimpat® PI) for provisional safety guidance, and obtain a TGA-approved PI before any Australian clinical use is considered. A dedicated safety review (including neutropenia risk noted in PMID 30275630) is required before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence supporting Lacosamide in manic bipolar affective disorder is currently limited to case reports, one retrospective comparison, and one open-label pilot trial — insufficient to meet L1/L2 thresholds. The only relevant registered trial (NCT07412132) is an ongoing, recruiting Phase 3 RCT not expected to complete until January 2027. Combined with the drug's non-registration in Australia (0 ARTG entries) and a Blocking safety data gap, there is not yet a sufficient basis to proceed.

**To proceed, the following is needed:**
- Results from NCT07412132 (Phase 3 RCT, estimated completion January 2027)
- TGA-approved (or sponsor international) Product Information covering warnings, contraindications, and drug–drug interactions
- Confirmed mechanism-of-action data from DrugBank (DG002)
- A defined ARTG registration pathway if Australian market entry is being pursued
- Larger, randomised controlled trials in bipolar disorder populations without comorbid epilepsy, to isolate the mood effect from seizure-control effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

