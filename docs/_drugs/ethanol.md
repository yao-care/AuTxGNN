---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Ethanol
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

# Ethanol: From Unspecified Original Use to Migraine Disorder

## One-Sentence Summary

Ethanol (DB00898) has no documented original therapeutic indication in this evidence pack and is not currently marketed as a registered medicine in Australia. The TxGNN model predicts a strong knowledge-graph association with **Migraine Disorder** (99.29% score), but the supporting clinical trial and literature evidence indicates this association reflects ethanol's role as a well-documented **migraine trigger, not a treatment** — this is a mechanistic red flag rather than a repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — no ARTG entry or original indication data available for ethanol in this evidence pack |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for ethanol was not available in this evidence pack (flagged as a High-severity data gap, DG002). However, the supporting literature does describe a clear pharmacological mechanism: ethanol is metabolised to acetaldehyde, which activates the TRPA1 ion channel and CGRP receptor pathway on trigeminal/meningeal Schwann cells and nociceptors (PMID 37101198) — the same CGRP/meningeal-nociceptor pathway implicated in migraine pain generation, including via ATP-sensitive potassium channel opening at meningeal nociceptors (PMID 40785517).

Critically, this mechanistic pathway runs in the **opposite direction** to what a repurposing candidate requires. Rather than relieving migraine, ethanol (alcohol) is one of the most consistently reported dietary/environmental trigger factors for migraine and other primary headache attacks — confirmed across a 2023 systematic review and meta-analysis (PMID 37612595), a 2025 narrative review (PMID 41305669), and multiple older reviews (PMID 18231712, PMID 36373782, PMID 8681169). The high TxGNN score (99.29%) most likely reflects the strength of the ethanol–migraine *association* in the underlying knowledge graph (co-occurrence as trigger/comorbidity), not a therapeutic relationship. No clinical trial identified in this evidence pack tests ethanol as a migraine treatment.

---

## Clinical Trial Evidence

The search returned 32 trials on the query terms "Ethanol" + "migraine disorder," but review of relevance grading found **no trial that actually evaluates ethanol as a migraine treatment** — all reviewed matches are keyword-search false positives (different active drug, or an unrelated disease/topic). The 10 graded trials are listed below for transparency:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05351086](https://clinicaltrials.gov/study/NCT05351086) | Phase 1 | Completed | 26 | Tests PUR3100, not ethanol — not relevant |
| [NCT06508411](https://clinicaltrials.gov/study/NCT06508411) | N/A | Completed | 1661 | Observational study on pain and sexual health in cancer patients — unrelated to ethanol/migraine |
| [NCT05175521](https://clinicaltrials.gov/study/NCT05175521) | N/A | Active, not recruiting | 50 | Tests inhaled isopropyl alcohol vapour (not ethanol) for migraine-associated nausea — drug mismatch |
| [NCT02169830](https://clinicaltrials.gov/study/NCT02169830) | N/A | Terminated | 35 | Tests nortriptyline vs topiramate for vestibular migraine — unrelated to ethanol |
| [NCT07297901](https://clinicaltrials.gov/study/NCT07297901) | N/A | Enrolling by invitation | 30 | App-based breathing/biofeedback programme — non-pharmacological, unrelated |
| [NCT05685225](https://clinicaltrials.gov/study/NCT05685225) | Phase 2 | Withdrawn | 0 | Tests naltrexone/acetaminophen for acute migraine — unrelated to ethanol |
| [NCT06476392](https://clinicaltrials.gov/study/NCT06476392) | Phase 3 | Active, not recruiting | 220 | Melatonin for chronic back pain — different disease, unrelated |
| [NCT05266469](https://clinicaltrials.gov/study/NCT05266469) | N/A | Completed | 168 | Real-world cohort of ofatumumab/ocrelizumab in multiple sclerosis — unrelated keyword match |
| [NCT06517446](https://clinicaltrials.gov/study/NCT06517446) | N/A | Recruiting | 48 | VR-based vestibular rehabilitation — non-pharmacological, unrelated |
| [NCT06263920](https://clinicaltrials.gov/study/NCT06263920) | N/A | Recruiting | 360 | Late-onset epilepsy/stroke/dementia cohort — unrelated to ethanol treatment of migraine |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37612595](https://pubmed.ncbi.nlm.nih.gov/37612595/) | 2023 | Systematic Review/Meta-analysis | J Headache Pain | Confirms alcohol is associated with increased risk of migraine and tension-type headache; migraine patients typically avoid alcohol as a trigger |
| [41305669](https://pubmed.ncbi.nlm.nih.gov/41305669/) | 2025 | Review | Nutrients | Reviews alcohol as a headache trigger across migraine, tension-type headache and other primary headaches; mechanism remains incompletely defined |
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Describes the complex, bidirectional relationship between alcohol consumption and migraine |
| [18231712](https://pubmed.ncbi.nlm.nih.gov/18231712/) | 2008 | Review | J Headache Pain | MEDLINE review finding ~1/3 of migraine patients report alcohol as a trigger, at least occasionally |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Case-control (genetic) | Headache | Alcohol dehydrogenase (ADH2) genotype investigated as a modifier of migraine risk from alcohol exposure |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Mechanistic/Animal | J Biomed Sci | Ethanol's metabolite acetaldehyde activates CGRP receptor and TRPA1 on Schwann cells, driving periorbital allodynia relevant to migraine — a pro-migraine mechanism |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | Mechanistic/Animal | Cephalalgia | KATP channel opening activates meningeal nociceptors, a proposed contributor to migraine headache origin |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | Cohort | Aerosp Med Hum Perform | Cohort study of migraine outcomes in military pilots, assessing modifiable aggravating factors |
| [6352219](https://pubmed.ncbi.nlm.nih.gov/6352219/) | 1983 | Mechanistic Review | Drug Alcohol Depend | Explores prostaglandin-mediated mechanisms of alcohol intolerance and hangover headache |
| [8681169](https://pubmed.ncbi.nlm.nih.gov/8681169/) | 1996 | Review | Rev Neurol | Reviews dietary triggers of migraine, including alcohol-containing beverages |

---

## Safety Considerations

No TGA-approved Product Information exists for ethanol as a registered medicine in Australia (0 ARTG entries; not marketed). Key warnings, contraindications, and drug–drug interaction data were not available in the sources queried (DrugBank, TGA/TFDA equivalents). Detailed regulatory safety data (TFDA label warnings/contraindications) is flagged as a **Blocking** data gap (DG001) and would need to be sourced before any safety assessment could proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic and clinical literature indicates ethanol is a documented *trigger* of migraine attacks (via acetaldehyde/CGRP/TRPA1 and meningeal nociceptor pathways), not a therapeutic agent — the opposite of what a repurposing candidate requires. No clinical trial evaluates ethanol as a migraine treatment, ethanol is not marketed as a medicine in Australia, and MOA/safety data are incomplete (one Blocking gap).

**To proceed, the following is needed:**
- Confirmation of whether the TxGNN association reflects a genuine therapeutic hypothesis or a trigger/comorbidity relationship, before any further clinical validation is considered
- TFDA/TGA-equivalent product warnings and contraindications (currently a Blocking data gap)
- Verified DrugBank mechanism-of-action data
- Given the directionally adverse mechanistic signal, this candidate is not recommended to advance past Hold without a substantive change in evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

